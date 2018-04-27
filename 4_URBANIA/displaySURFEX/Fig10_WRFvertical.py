# -*- coding: utf-8 -*-
__author__ = 'lnx'

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
file = '/home/lnx/MODELS/WRF/3_testdata/Urbania/Tair_d03.nc'
fh = Dataset(file, mode='r')

lons = fh.variables['lon'][:]  #lon
lats = fh.variables['lat'][:]  #lat
tair = fh.variables['Tair']
tair0UTC = fh.variables['Tair'][55]
tair6UTC = fh.variables['Tair'][61]
tair12UTC = fh.variables['Tair'][67]
tair18UTC = fh.variables['Tair'][73]
RH =fh.variables['RH']
terrain =fh.variables['HGT']
Xwind =fh.variables['U']
Ywind =fh.variables['V']
Zwind =fh.variables['W']
LU =fh.variables['LU']

print tair[67,:,120,150] #[104 x 39 x 135 x 174] t - z -y - x ; z=0 ...lowest level; x,y=0 -> left lower corner

tair_units = fh.variables['Tair'].units

fh.close()

m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')

lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lon, lat)
cs = m.pcolor(xi,yi,np.squeeze(tair[67,:,:,150]))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")


#cbar.set_label(tair_units)
#plt.title('2m Air Temperature STQ 2015-07-20 0UTC')
#plt.clim(21,35)
#plt.show()

