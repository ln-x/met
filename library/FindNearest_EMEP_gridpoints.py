# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset

fh_o3 = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ug_O3_uozone_new2.nc", mode='r')
lons = fh_o3.variables['lon'][:][:]
lats = fh_o3.variables['lat'][:][:] #[60]

STE_LAT = 48.2086
STE_LON = 16.3742
STE_y = 60
STE_x = 62
print(lats[60][62],lons[60][62])

LOB_LAT = 48.1625
LOB_LON = 16.5269
LOB_y = 59
LOB_x = 66
print(lats[LOB_y][LOB_x],lons[LOB_y][LOB_x])

HER_LAT = 48.2708
HER_LON = 16.2983
HER_y = 63
HER_x = 60
print(lats[HER_y][HER_x],lons[HER_y][HER_x])



