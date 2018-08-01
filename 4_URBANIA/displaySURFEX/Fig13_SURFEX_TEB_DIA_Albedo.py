# -*- coding: utf-8 -*-
__author__ = 'lnx'

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import csv

'''This file plots 2D maps of SURFEX.nc files.  
This is the cleaned version of the script, for all comments see Fig4_plotSURFFEXDIFF_nc1.py
For hourly loop look at Fig5_plotSURFEX_nc1_hourly.py'''

file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/_S13/TEB_DIAGNOSTICS.OUT.nc'
file2 = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/_S20_ALB/TEB_DIAGNOSTICS.OUT.nc'
fh = Dataset(file, mode='r')
fh2 = Dataset(file2, mode='r')
#starts at 17.7.18hUTC [0], hourly ->
# 18.7.0h [7],6h[13], 12h [19], 14h [21],
# 19.7.0h [31],12h [43],
# 20.7.  COLDEST: 0h[55], 5h[60], 6h[61], 12h [67], 14h[69], HOTTEST 15h[70], 18h [73]
# 22.7.  0h[103], 6h[109], 12h [115], 18h [121]
hour = 12
index = 103+hour
print index

lons = fh.variables['xx'][:]  #lon
lats = fh.variables['yy'][:]  #lat
#RN = fh.variables['RN_TEB'][index]
#H = fh.variables['H_TEB'][index]
#LE = fh.variables['LE_TEB'][index]
#GFLUX = fh.variables['GFLUX_TEB'][index]
UTCIsun = fh.variables['UTCI_OUTSUN'][index]
UTCIshade = fh.variables['UTCI_OUTSHAD'][index]
UTCIsun2 = fh2.variables['UTCI_OUTSUN'][index]
UTCIshade2 = fh2.variables['UTCI_OUTSHAD'][index]
#starts at 17.7.18hUTC [0], hourly ->
# 18.7.0h [7],6h[13], 12h [19], 14h [21], 18h [42], 6h [54]
# 20.7.  0h[55], 5h[60], 6h[61], 12h [67], 14h[69], HOTTEST 15h[70], 18h [73]
# 22.7.  0h[103], 6h[109], 12h [115], 18h [121]
heatflux_units = fh.variables['RN_TEB'].units


fh.close()

'''CONVERSION TO LATLON'''
lons2,lats2 =[],[]
for i in lons:
    i2 = i*0.000014038 + 15.969 - (0.000014038*333)
    lons2.append(i2)
for i in lats:
    i2 = i*0.000009355 + 48.0322418 - (0.000009355*333)
    lats2.append(i2)

m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')

lon, lat = np.meshgrid(lons2, lats2)
xi, yi = m(lon, lat)


'''UTCI'''

dUTCIsun = UTCIsun2-UTCIsun
dUTCIshade = UTCIshade2-UTCIshade

cs = m.pcolor(xi,yi,np.squeeze(UTCIsun))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIsun Ref 2015-07-22 12UTC')
#plt.clim(30,50)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(UTCIshade))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIshade Ref 2015-07-22 12UTC')
#plt.clim(30,50)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dUTCIsun))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIsun HighAlb-Ref 2015-07-22 12UTC')
plt.clim(-0.5,0.5)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dUTCIshade))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIshade HighAlb-Ref 2015-07-22 12UTC')
plt.clim(-0.5,0.5)
plt.show()

exit()

'''Heat fluxes'''

cs = m.pcolor(xi,yi,np.squeeze(RN))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Radiation Balance STQ 2015-07-20 18UTC')
#plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(GFLUX))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Ground Heat Flux STQ 2015-07-20 18UTC')
#plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(H))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Sensible Heat Flux STQ 2015-07-20 18UTC')
#plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(LE))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Latent Heat Flux STQ 2015-07-20 18 UTC')
#plt.clim(21,35)
plt.show()

'''Air temperature'''

#cs = m.pcolor(xi,yi,np.squeeze(tairC))
cs = m.pcolor(xi,yi,np.squeeze(tair0UTC_C))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
#cbar.set_label(tair_units)
cbar.set_label(tairC_units)
#cbar.set_label(wind10m_units)
plt.title('2m Air Temperature STQ 2015-07-20 0UTC')
#plt.title('10m Wind Speed - 2015-07-20 18UTC')
plt.clim(21,35)
plt.show()


cs = m.pcolor(xi,yi,np.squeeze(tair6UTC_C))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(tairC_units)
plt.title('2m Air Temperature STQ 2015-07-20 6UTC')
plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(tair12UTC_C))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(tairC_units)
plt.title('2m Air Temperature STQ 2015-07-20 12UTC')
plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(tair18UTC_C))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(tairC_units)
plt.title('2m Air Temperature STQ 2015-07-20 18UTC')
plt.clim(21,35)
plt.show()


