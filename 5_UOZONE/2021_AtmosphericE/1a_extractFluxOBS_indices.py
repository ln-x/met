# -*- coding: utf-8 -*-
__author__ = 'lnx'
import netCDF4
import numpy as np

def geo_idx(dd, dd_array):
   """
     search for nearest decimal degree in an array of decimal degrees and return the index.
     np.argmin returns the indices of minium value along an axis.
     so subtract dd from all values in dd_array, take absolute value and find index of minium.
    """
   geo_idx = (np.abs(dd_array - dd)).argmin()
   return geo_idx

#Jans data
infile = '/media/heidit/Norskehavet/EMEPData/OUTPUT/2020_4/wrfout_d01_2020-03-31_01:00:00'
west_east = 189
south_north = 165
nci = netCDF4.Dataset(infile)

#find Bosco Fontana, IT
in_lat = 45.199292
in_lon = 10.7399
print(nci.variables['XLAT'][1,23,62])
print(nci.variables['XLONG'][1,23,62])

#find O3HP, FR  (Saint-Michel-l'Observatoire, 04870 France)
in_lat = 43.9311448
in_lon = 5.713935
print(nci.variables['XLAT'][1,11,16])
print(nci.variables['XLONG'][1,11,16])

exit()
#find Vielsalm, BE
in_lat = 50.30
in_lon = 5.99
print(nci.variables['XLAT'][1,89,27]) #
print(nci.variables['XLONG'][1,89,27])

lats = nci.variables['XLAT'][1,89,:]
lons = nci.variables['XLONG'][1,:,27]
lat_idx = geo_idx(in_lat, lats)
lon_idx = geo_idx(in_lon, lons)
print(lat_idx,lon_idx)
#iy = lat_idx%south_north
#ix = lon_idx%west_east
#50.332256
#5.9249268


