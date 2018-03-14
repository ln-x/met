# -*- coding: utf-8 -*-
__author__ = 'lnx'

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

file = '/home/lnx/MODELS/SURFEX/3_input/met_forcing/FORCING_new.nc'
fh = Dataset(file, mode='r')

lons = fh.variables['lon'][:]     #lon
lats = fh.variables['lat'][:]  #lat
tair = fh.variables['Tair'][:]
tair_units = fh.variables['Tair'].units

fh.close()

#print len(lats[1]), len(lons[1])
print lats[54][86], lons[54][86]
print lats[70][84], lons[70][84]
print lats[26][130],lons[26][130]
print lats[55][128],lons[55][128]
print lats[30][98],lons[30][98]
print lats[89][95],lons[89][95]
print lats[25][66],lons[25][66]
print lats[57][57],lons[57][57]
print lats[73][100],lons[73][100]

exit()

##EXPORT LATLON
for i in range(len(lons)):
    for j in range(len(lons[i])):
        print lats[i][j],lons[i][j],0.5

exit()

# Get some parameters for the Stereographic Projection
lon_0 = lons.mean()
lat_0 = lats.mean()
#print lon_0, lat_0

m = Basemap(width=57942,height=44955,
            resolution='l',projection='lcc',
            lat_0=lat_0,lon_0=lon_0)
# Because our lon and lat variables are 1D,
# use meshgrid to create 2D arrays
# Not necessary if coordinates are already in 2D arrays.
lon, lat = np.meshgrid(lons, lats)
print lat,lon

xi, yi = m(lon, lat)
#print xi,yi

# Plot Data
cs = m.pcolor(xi,yi,np.squeeze(tair))

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

# Add Coastlines, States, and Country Boundaries
#m.drawcoastlines()
#m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(tair_units)

# Add Title
plt.title('DJF Maximum Temperature')

plt.show()



'''
/home/lnx/anaconda3/envs/geoenv/bin/python /home/lnx/PycharmProjects/1_GRUENSTADT/NETCDF/plot_SURFEX_nc.py
Traceback (most recent call last):
  File "/home/lnx/PycharmProjects/1_GRUENSTADT/NETCDF/plot_SURFEX_nc.py", line 33, in <module>
    xi, yi = m(lon, lat)
  File "/home/lnx/anaconda3/envs/geoenv/lib/python2.7/site-packages/mpl_toolkits/basemap/__init__.py", line 1148, in __call__
    xout,yout = self.projtran(x,y,inverse=inverse)
  File "/home/lnx/anaconda3/envs/geoenv/lib/python2.7/site-packages/mpl_toolkits/basemap/proj.py", line 286, in __call__
    outx,outy = self._proj4(x, y, inverse=inverse)
  File "/home/lnx/anaconda3/envs/geoenv/lib/python2.7/site-packages/mpl_toolkits/basemap/pyproj.py", line 383, in __call__
    iny, yisfloat, yislist, yistuple = _copytobuffer(lat)
  File "/home/lnx/anaconda3/envs/geoenv/lib/python2.7/site-packages/mpl_toolkits/basemap/pyproj.py", line 532, in _copytobuffer
    raise TypeError('input must be an array, list, tuple or scalar')
TypeError: input must be an array, list, tuple or scalar
'''