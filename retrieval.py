# Retrieval Helper Functions

import numpy as np
import pandas as pd
import xarray as xr
from datetime import datetime, timedelta
from siphon.ncss import NCSS
from requests import HTTPError


# Function to compile a full case set of archival data
def compile_archive(start, end, interval=timedelta(hours=6), show_status=True):

    # Get our first Dataset as our starting point (keeping only the needed levels)
    if show_status:
        print('Retrieving {}...'.format(start.strftime('%Y-%m-%d %H%MZ')))
    data = retrieve_gfs_analysis(start)
    data = data.where(50000.0 >= data.isobaric, drop=True).where(15000.0 <= data.isobaric, drop=True)

    # Loop over all times
    current_time = start + interval
    while current_time <= end:
        try:
            if show_status:
                print('Retrieving {}...'.format(current_time.strftime('%Y-%m-%d %H%MZ')))
            current_data = retrieve_gfs_analysis(current_time)
            current_data = current_data.where(50000.0 >= current_data.isobaric, drop=True).where(15000.0 <= current_data.isobaric, drop=True)
            data = xr.concat([data, current_data], dim='time')
        except HTTPError:
            # I don't really need to see this failed retrival unless watching status,
            # it will show up as an empty time slot in final Dataset
            if show_status:
                print('!! Failed retrieval for {} !!'.format(start.strftime('%Y-%m-%d %H%MZ')))
        finally:
            current_time += interval

    # Return the data
    return data


# Retrive an xr.Dataset of your data of interest from archived GFS analyses on NOMADS
def retrieve_gfs_analysis(time, lat=50, variables=['Geopotential_height_isobaric', 'u-component_of_wind_isobaric']):

    url = time.strftime('https://www.ncei.noaa.gov/thredds/ncss/grid/gfs-g3-anl-files/%Y%m/%Y%m%d/gfsanl_3_%Y%m%d_%H%M_000.grb2/')
    ncss = NCSS(url)

    query = ncss.query()
    query.all_times().variables(*variables)

    query.lonlat_box(north=lat, south=lat, east=360., west=0.)
    nc_north = ncss.get_data(query)

    query.lonlat_box(north=-lat, south=-lat, east=360., west=0.)
    nc_south = ncss.get_data(query)

    data_north = xr.open_dataset(xr.backends.NetCDF4DataStore(nc_north))
    data_south = xr.open_dataset(xr.backends.NetCDF4DataStore(nc_south))

    return xr.concat([data_north, data_south], dim='lat')