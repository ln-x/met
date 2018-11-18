#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:17:29 2018

@author: mariaw
"""
import xarray as xr
import glob
from netCDF4 import Dataset
import os.path
import numpy as np
from netCDF4 import date2num
from datetime import datetime

ds = xr.open_dataset('xy.nc')

savename = 'xyz.nc'
param = 'pr'

dataset = Dataset(savename,'w',format='NETCDF4_CLASSIC')

dataset.createDimension("time", None)

#*******************************************************************
# Lambert conformal conic
dim_x = ds['x'].shape[0]
dim_y = ds['y'].shape[0]
dataset.createDimension("x", dim_x)
dataset.createDimension("y",dim_y)

x_var = dataset.createVariable("x", "f4", ("x"))
y_var = dataset.createVariable("y", "f4", ("y"))
times = dataset.createVariable("time","f8",("time",))
lats = dataset.createVariable("lat", "f4", ("y","x",))
lons = dataset.createVariable("lon", "f4", ("y","x",))
var = dataset.createVariable(param, "f4", ("time", "y","x",), fill_value = -9999)
crs = dataset.createVariable("lambert_conformal_conic", "c", ())

x_var.long_name = 'x coordinate of projection'
x_var.units = 'km'
x_var.standard_name = 'projection_x_coordinate'
x_var[:] = ds['x']
x_var.axis = 'X'

y_var.long_name = 'y coordinate of projection'
y_var.units = 'km'
y_var.standard_name = 'projection_y_coordinate'
y_var[:] = ds['y']
y_var.axis = 'Y'

crs.grid_mapping_name = "lambert_conformal_conic" ;
crs.longitude_of_central_meridian = 15.0 ;
crs.standard_parallel = 43.0 ;
crs.latitude_of_projection_origin = 43.0 ;

var.coordinates = "lat lon"
var.grid_mapping = "lambert_conformal_conic"

#*******************************************************************
# Rotated Latitude Longitude

dim_rlat = ds['rlat'].shape[0]
dim_rlon = ds['rlon'].shape[0]
dataset.createDimension("rlat", dim_rlat)
dataset.createDimension("rlon",dim_rlon)
rlon = dataset.createVariable("rlon", "f4", ("rlon"))
rlat = dataset.createVariable("rlat", "f4", ("rlat"))
    
# create variable
times = dataset.createVariable("time","f8",("time",))
lats = dataset.createVariable("lat", "f4", ("rlat","rlon",))
lons = dataset.createVariable("lon", "f4", ("rlat","rlon",))
var = dataset.createVariable('pr', "f4", ("time", "rlat","rlon",), fill_value = -9999)
crs = dataset.createVariable("rotated_latitude_longitude", "c", ())

rlon.long_name = 'longitude in rotated pole grid'
rlon.units = 'degrees'
rlon.standard_name = 'grid_longitude'
rlon[:] = ds['rlon']

rlat.long_name = 'latitude in rotated pole grid'
rlat.units = 'degrees'
rlat.standard_name = 'grid_latitude'
rlat[:] = ds['rlat']

crs.grid_mapping_name = "rotated_latitude_longitude"
crs.grid_north_pole_latitude = 39.25
crs.grid_north_pole_longitude = -162.
crs.north_pole_grid_longitude = 0.

var.coordinates = "lat lon"
var.grid_mapping = "rotated_latitude_longitude"

#**********************************************************************

lats.units = 'degrees_north'
lats.long_name = 'latitude'
lats.standard_name = 'latitude'
lats._CoordinateAxisType = 'Lat'
lats[:] = ds['lat'].data

lons.units = 'degrees_east'
lons.long_name = 'longitude'
lons.standard_name = 'longitude'
lons._CoordinateAxisType = 'Lon'
lons[:] = ds['lon'].data

# replace nan values with proper fill value (-9999)
ds[param].data[np.isnan(ds[param].data)] = -9999
var[:] = ds[param].data

dataset.close()
