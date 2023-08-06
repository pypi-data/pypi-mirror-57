#!/usr/bin/env python
# Kyle Fitzsimmons, 2019
import click
from collections import namedtuple
import logging
import sys

from tripkit import TripKit, utils

logger = logging.getLogger('itinerum-tripkit-cli.runners.itinerum')


def setup(cfg):
    tripkit = TripKit(config=cfg)
    tripkit.setup(force=False)
    return tripkit


def load_users(tripkit, user_id):
    if user_id:
        logger.info(f'Loading user by ID: {user_id}')
        return [tripkit.load_users(uuid=user_id)]
    return tripkit.load_users()


def detect_trips(tripkit, user, write_geo=False, append_to=None):
    parameters = {
        'subway_entrances': tripkit.database.load_subway_entrances(),
        'break_interval_seconds': tripkit.config.TRIP_DETECTION_BREAK_INTERVAL_SECONDS,
        'subway_buffer_meters': tripkit.config.TRIP_DETECTION_SUBWAY_BUFFER_METERS,
        'cold_start_distance': tripkit.config.TRIP_DETECTION_COLD_START_DISTANCE_METERS,
        'accuracy_cutoff_meters': tripkit.config.TRIP_DETECTION_ACCURACY_CUTOFF_METERS,
    }
    user.trips = tripkit.process.trip_detection.triplab.v2.algorithm.run(user.coordinates, parameters=parameters)
    tripkit.database.save_trips(user, user.trips)
    if write_geo:
        write_geodata_trips(tripkit, user)
    trip_summaries = tripkit.process.trip_detection.triplab.v2.summarize.run(user, tripkit.config.TIMEZONE)
    fn_base = append_to if append_to else user.uuid
    tripkit.io.csv.write_trip_summaries(fn_base=fn_base, summaries=trip_summaries, append=append_to)


def detect_complete_day_summaries(tripkit, user, append=False):
    complete_day_summaries = tripkit.process.complete_days.triplab.counter.run(user.trips, tripkit.config.TIMEZONE)
    tripkit.database.save_trip_day_summaries(user, complete_day_summaries, tripkit.config.TIMEZONE)
    tripkit.io.csv.write_complete_days({user.uuid: complete_day_summaries}, append=append)


def detect_activity_summaries(tripkit, user, append=False):
    locations = utils.itinerum.create_activity_locations(user)
    activity = tripkit.process.activities.triplab.detect.run(user, locations, tripkit.config.ACTIVITY_LOCATION_PROXIMITY_METERS)
    activity_summaries_full = tripkit.process.activities.triplab.summarize.run_full(activity, tripkit.config.TIMEZONE)
    duration_cols = [
        'commute_time_work_s',
        'commute_time_study_s',
        'dwell_time_home_s',
        'dwell_time_work_s',
        'dwell_time_study_s',
    ]
    tripkit.io.csv.write_activities_daily(activity_summaries_full, extra_cols=duration_cols, append=append)


def write_input_data(tripkit, user):
    output_fmt = tripkit.config.GIS_OUTPUT_FORMAT
    if output_fmt.lower() == 'shp':
        tripkit.io.shapefile.write_inputs(
            fn_base=user.uuid,
            coordinates=user.coordinates,
            prompts=user.prompt_responses,
            cancelled_prompts=user.cancelled_prompt_responses,
        )
    elif output_fmt.lower() == 'gpkg':
        tripkit.io.geopackage.write_inputs(
            fn_base=user.uuid,
            coordinates=user.coordinates,
            prompts=user.prompt_responses,
            cancelled_prompts=user.cancelled_prompt_responses,
        )
    elif output_fmt.lower() == 'geojson':
        tripkit.io.geojson.write_inputs(
            fn_base=user.uuid,
            coordinates=user.coordinates,
            prompts=user.prompt_responses,
            cancelled_prompts=user.cancelled_prompt_responses,
        )
    else:
        msg = f'Error: file format {output_fmt} not recognized.'
        click.echo(msg)
        sys.exit(1)


def write_geodata_trips(tripkit, user):
    output_fmt = tripkit.config.GIS_OUTPUT_FORMAT
    if output_fmt.lower() == 'shp':
        tripkit.io.shapefile.write_trips(fn_base=user.uuid, trips=user.trips)
    elif output_fmt.lower() == 'gpkg':
        tripkit.io.geopackage.write_trips(fn_base=user.uuid, trips=user.trips)
    elif output_fmt.lower() == 'geojson':
        tripkit.io.geojson.write_trips(fn_base=user.uuid, trips=user.trips)
    else:
        msg = f'Error: file format {output_fmt} not recognized.'
        click.echo(msg)
        sys.exit(1)


@click.command()
@click.option('-u', '--user', 'user_id', help='The user ID to process a single user only.')
@click.option('-t', '--trips', 'trips_only', is_flag=True, help='Detect only trips for the given user(s).')
@click.option('-cd', '--complete-days', 'complete_days_only', is_flag=True, help='Detect only complete day summaries for the given user(s).')
@click.option('-a', '--activities', 'activity_summaries_only', is_flag=True, help='Detect only activities summaries for the given user(s).')
@click.option('-cn', '--condensed', 'condensed_output', is_flag=True, help='(QStarz only) Create a condensed output with a locations file, trips summaries, and aggregate survey summary.')
@click.option('-wi', '--write-inputs', is_flag=True, help='Write input .csv coordinates data to GIS format.')
@click.option('-wg', '--write-geo', is_flag=True, help='Write output GIS data for each user in survey.')
@click.pass_context
def run(ctx, user_id, trips_only, complete_days_only, activity_summaries_only, condensed_output, write_inputs, write_geo):
    if sum([trips_only, complete_days_only, activity_summaries_only, condensed_output]) > 1:
        click.echo('Error: Only one exclusive mode can be used at a time.')
        sys.exit(1)
    if condensed_output:
        click.echo('Error: condensed output mode is only available for QStarz datasets.')
        sys.exit(1)

    cfg = ctx.obj['config']
    tripkit = setup(cfg)
    users = load_users(tripkit, user_id)
    append_fn_base = cfg.SURVEY_NAME if not user_id else None
    append_mode = user_id is None

    for user in users:
        if write_inputs:
            if len(users) > 1:
                click.echo('Warning: Multiple users selected, continue writing input data? (y/n)')
                sys.exit(1)
            write_input_data(tripkit, user)

        if trips_only:
            if not user.coordinates.count():
                click.echo(f'No coordinates available for user: {user.uuid}')
            else:
                detect_trips(tripkit, user, write_geo, append_to=append_fn_base)
        elif complete_days_only:
            if not user.trips:
                click.echo(f'No trips available for user: {user.uuid}')
            else:
                detect_complete_day_summaries(tripkit, user, append=append_mode)
        elif activity_summaries_only:
            if not user.trips:
                click.echo(f'No trips available for user: {user.uuid}')
            else:
                detect_activity_summaries(tripkit, user, append=append_mode)
        else:
            detect_trips(tripkit, user, write_geo, append_to=append_fn_base)
            if not user.trips:
                click.echo(f'No trips available for user: {user.uuid}')
            else:
                detect_complete_day_summaries(tripkit, user, append=append_mode)
                detect_activity_summaries(tripkit, user, append=append_mode)
