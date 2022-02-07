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

def find_nearest(array, value):
   array = np.asarray(array)
   idx = (np.abs(array - value)).argmin()
   return array[idx], idx

def find_nearest_xy(array1, value1, array2, value2):
   array1 = np.asarray(array1)
   array2 = np.asarray(array2)
   idx = (np.abs(array1 - value1)+np.abs(array2 - value2)).argmin()
   return array1[idx], array2[idx], idx


#Christians data 9km VIE center (exact: 48.196613 16.382294)
infile = '/windata/DATA/models/boku/wrf/120521/9km_3km_2domain/wrfout_d01_2019-07-01_00:00:00'
west_east = 198
south_north = 135
nci = netCDF4.Dataset(infile)
print(nci.variables['XLAT'][1,69,99]) #48.200005
print(nci.variables['XLONG'][1,69,99]) #16.400024
#Christians data 9km Rutzendorf  (exact: 48.206673 16.623864)
print(nci.variables['XLAT'][1,69,101])  #48.199753
print(nci.variables['XLONG'][1,69,101])  #16.642914

exit()

#TROPOMI SIF 1D
infile1 = netCDF4.Dataset('/windata/DATA/remote/satellite/TROPOMI/2020/06/TROPOSIF_L2B_2020-06-01.nc')
infile2 = netCDF4.Dataset('/windata/DATA/remote/satellite/TROPOMI/2020/06/TROPOSIF_L2B_2020-06-02.nc')
infile1_data = infile1['/PRODUCT']
infile2_data = infile2['/PRODUCT']
n_elem = 2421884
#print(infile1_data.variables['longitude'][1021884])  #48.192i142
#print(infile2_data.variables['longitude'][1021884])  #48.192142

#print(find_nearest(infile1_data.variables['longitude'], 16)
#print(find_nearest(infile1_data.variables['latitude'], 48))
print("CE", find_nearest_xy(infile1_data.variables['latitude'], 48.196613, infile1_data.variables['longitude'], 16.382294))
print("CE", find_nearest_xy(infile2_data.variables['latitude'], 48.196613, infile2_data.variables['longitude'], 16.382294))

print("RU", find_nearest_xy(infile1_data.variables['latitude'], 48.192142, infile1_data.variables['longitude'], 16.624939))
print("RU", find_nearest_xy(infile2_data.variables['latitude'], 48.192142, infile2_data.variables['longitude'], 16.624939))

exit()

#Jans data 3km VIE center
infile = '/media/heidit/Norskehavet/EMEPData/OUTPUT/wrfout_d02_2020-01-01_00:00:00'
nci = netCDF4.Dataset(infile)
#print(nci.variables['XLAT'][1,76,181])  #48.19662
#print(nci.variables['XLONG'][1,76,181])  #16.382263

#Jans data 9km VIE center
infile = '/media/heidit/Norskehavet/EMEPData/OUTPUT/2020_4/wrfout_d01_2020-03-31_01:00:00'
west_east = 189
south_north = 165
nci = netCDF4.Dataset(infile)
print(nci.variables['XLAT'][1,59,110]) #48.196613
print(nci.variables['XLONG'][1,59,110]) #16.382294
#Jans data 9km Rutzendorf
print(nci.variables['XLAT'][1,59,112])  #48.192142
print(nci.variables['XLONG'][1,59,112])  #16.624939

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


