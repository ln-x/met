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

filename = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/Ref_Heidi_Lu_2015_1stRun/wrfout_d03_2015-08-05_18_00_00.nc'
savename = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/Ref_Heidi_Lu_2015_1stRun/wrfout_d03_2015-08-05_18_00_00_nest_teb_cf-conform.nc'

ds = xr.open_dataset(filename)

param = 'T2'

dataset = Dataset(savename,'w',format='NETCDF4_CLASSIC')

dataset.createDimension("time", None)

#*******************************************************************
""" Lambert conformal conic"""

#print ds['XLONG'][0][0]

dim_x = ds['west_east'].shape[0] #175
dim_y = ds['south_north'].shape[0] #135
dataset.createDimension("x", dim_x)
dataset.createDimension("y",dim_y)

x_var = dataset.createVariable("x", "f4", ("x"))
y_var = dataset.createVariable("y", "f4", ("y"))
times = dataset.createVariable("time","f8",("time",))
lats = dataset.createVariable("lat", "f4", ("y","x",))
lons = dataset.createVariable("lon", "f4", ("y","x",))
var = dataset.createVariable(param, "f4", ("time", "y","x",), fill_value = -9999)
crs = dataset.createVariable("lambert_conformal_conic", "i", ())

x_var.long_name = 'x coordinate of projection'
x_var.units = 'm'
x_var.standard_name = 'projection_x_coordinate'
x_var[:] = np.array(ds['west_east'])
x_var.axis = 'X'

y_var.long_name = 'y coordinate of projection'
y_var.units = 'm'
y_var.standard_name = 'projection_y_coordinate'
y_var[:] = np.array(ds['south_north'])
y_var.axis = 'Y'

crs.grid_mapping_name = "lambert_conformal_conic" ;
crs.longitude_of_central_meridian = 16.37247 ;
crs.standard_parallel = 30.0 ;
crs.latitude_of_projection_origin = 48.24166 ; #43.0 ;

var.coordinates = "lat lon"
var.grid_mapping = "lambert_conformal_conic"

lats.units = 'degrees_north'
lats.long_name = 'latitude'
lats.standard_name = 'latitude'
lats._CoordinateAxisType = 'Lat'
#print lats.shape #(135,174)
#print ds['XLAT'][0].data.shape
lats[:] = ds['XLAT'][0].data

lons.units = 'degrees_east'
lons.long_name = 'longitude'
lons.standard_name = 'longitude'
lons._CoordinateAxisType = 'Lon'
lons[:] = ds['XLONG'][0].data

# replace nan values with proper fill value (-9999)
ds[param].data[np.isnan(ds[param].data)] = -9999
var[:] = ds[param].data

"""
print "lons , lats, gridpoints"
for i in range(len(lons)):
        for j in range(len(lons[i])):
                print lons[i][j],",", lats[i][j],", %s-%s" %(j+1,i+1)  #j+1, i+1 for 1 based gridpoints
"""
dataset.close()

