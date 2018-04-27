# -*- coding: utf-8 -*-
__author__ = 'lnx'

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import csv
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/diff_S13_S12_xunif.nc'
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/diff_S14_S13_xunif.nc'
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/diff_S13_S12.nc'
file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/diff_S17_S15_XUNIF.nc'
fh = Dataset(file, mode='r')

lons = fh.variables['xx'][:]  #lon
lats = fh.variables['yy'][:]  #lat
tair0UTC = fh.variables['T2M'][55]
tair6UTC = fh.variables['T2M'][61]
tair12UTC = fh.variables['T2M'][67]
tair18UTC = fh.variables['T2M'][73]

#wind10m =fh.variables['W10M'][73]
#starts at 17.7.18hUTC [0], hourly ->
# 18.7.0h [7],6h[13], 12h [19], 14h [21], 18h [42], 6h [54]
# 20.7.  COLDEST: 0h[55], 5h[60], 6h[61], 12h [67], 14h[69], HOTTEST 15h[70], 18h [73]

tair_units = fh.variables['T2M'].units
#wind10m_units = fh.variables['W10M'].units
fh.close()

'''CONVERSTION TO CELSIUS'''
def Kelvin_to_Celsius(tair):
    tairC = tair.copy()
    for i in range(len(tair)):
        for j in range(len(tair[i])):
            tairC[i][j] = tair[i][j] - 273.15
    return tairC

tairC_units = (u"°C")

tair0UTC_C = Kelvin_to_Celsius(tair0UTC)
tair6UTC_C = Kelvin_to_Celsius(tair6UTC)
tair12UTC_C = Kelvin_to_Celsius(tair12UTC)
tair18UTC_C = Kelvin_to_Celsius(tair18UTC)


'''CONVERSION TO LATLON'''
lons2,lats2 =[],[]
for i in lons:
    i2 = i*0.000014038 + 15.969 - (0.000014038*333)
    lons2.append(i2)
for i in lats:
    i2 = i*0.000009355 + 48.0322418 - (0.000009355*333)
    lats2.append(i2)

#print lons2[0], lons2[-1], lats2[0],lats2[-1],
#lon_0 = lons.mean()
#lat_0 = lats.mean()
m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')

# Add Grid Lines
m.drawparallels(np.arange(44.0, 50., 0.1), labels=[1,0,0,0], fontsize=10, linewidth=0.)
m.drawmeridians(np.arange(14.0, 17., 0.2), labels=[0,0,0,1], fontsize=10, linewidth=0.)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Because our lon and lat variables are 1D,
# use meshgrid to create 2D arrays
# Not necessary if coordinates are already in 2D arrays.
lon, lat = np.meshgrid(lons2, lats2)
xi, yi = m(lon, lat)
#lons = 174: 333 -57942, lats = 135:333 -44955, tair = 36[[][] ]
#lon, lat, xi,yi = 135x174
#print "lons=", lons, "lats=", lats, "tair=", tair,"lon=", lon, "lat=", lat, "xi=", xi, "yi=", yi
#print len(lons), len(lats), len(tair[0]), len(lon[0]), len(lat[0]), len(xi[0]),len(yi[0]),
# Plot Data

#clevs = [0,1,2.5,5,7.5,10,15,20,30,40,50,70,100,150,200,250,300,400,500,600,750]
#cs = m.contourf(x,y,data,clevs,cmap=cm.s3pcpn)

#cs = m.pcolor(xi,yi,np.squeeze(tairC))
cs = m.pcolor(xi,yi,np.squeeze(tair0UTC))
# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
#cbar.set_label(tair_units)
#cbar.set_label(tairC_units)
cbar.set_label(tair_units)
# Add Title
#plt.title('2m Air Temperature S1-STQ - 2015-07-20 0UTC')
plt.title('2m Air Temperature S3-STQ - 2015-07-20 0UTC')
#plt.clim(21,35)
plt.clim(-2,2)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(tair6UTC))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(tair_units)
plt.title('2m Air Temperature S3-STQ - 2015-07-20 6UTC')
plt.clim(-2,2)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(tair12UTC))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(tair_units)
plt.title('2m Air Temperature S3-STQ - 2015-07-20 12UTC')
plt.clim(-2,2)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(tair18UTC))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(tair_units)
plt.title('2m Air Temperature S3-STQ - 2015-07-20 18UTC')
plt.clim(-2,2)
plt.show()


'''
#oldtry
m = Basemap(llcrnrlon=15.969,   #lower left corner longitude
            llcrnrlat=48.0322418,       #lower left corner latitute
            urcrnrlon=16.778,     #upper right longitude
            urcrnrlat=48.4497643,      # upper right latitute
            projection='lcc',
            lat_1=30.,
            lat_2=60.,
            lat_0=48.24166,
            lon_0=16.37247,
            resolution='l')
'''