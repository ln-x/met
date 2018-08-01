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

file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/_S13/SURF_ATM_DIAGNOSTICS.OUT.nc'
file2 = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/_S20_ALB/SURF_ATM_DIAGNOSTICS.OUT.nc'
fh = Dataset(file, mode='r')
fh2 = Dataset(file2, mode='r')
#starts at 17.7.18hUTC [0], hourly ->
# 18.7.0h [7],  6h[13],  12h [19], 14h [21],
# 19.7.0h [31],          12h [43],
# 20.7.0h [55], 6h[61],  12h [67], 14h [69], HOTTEST 15h[70], 18h [73]
# 22.7.0h [103],6h[109], 12h [115],                           18h [121]
hour = 18
index = 103+hour
print index

lons = fh.variables['xx'][:]  #lon
lats = fh.variables['yy'][:]  #lat

RN = fh.variables['RN'][index]
H = fh.variables['H'][index]
LE = fh.variables['LE'][index]
GFLUX = fh.variables['GFLUX'][index]

RN2 = fh2.variables['RN'][index]
H2 = fh2.variables['H'][index]
LE2 = fh2.variables['LE'][index]
GFLUX2 = fh2.variables['GFLUX'][index]

tair = fh.variables['T2M'][index]
tair2 = fh2.variables['T2M'][index]
wind10m =fh.variables['W10M'][73]

heatflux_units = fh.variables['RN'].units
tair_units = fh.variables['T2M'].units
wind10m_units = fh.variables['W10M'].units

fh.close()

'''CONVERSTION TO CELSIUS'''
def Kelvin_to_Celsius(tair):
    tairC = tair.copy()
    for i in range(len(tair)):
        for j in range(len(tair[i])):
            tairC[i][j] = tair[i][j] - 273.15
    return tairC

tairC_units = (u"°C")

tair_C = Kelvin_to_Celsius(tair)
tair2_C = Kelvin_to_Celsius(tair2)

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

'''Heat fluxes'''

dRN = RN2 - RN
dH = H2 - H
dLE = LE2 - LE
dGFLUX = GFLUX2 - GFLUX

cs = m.pcolor(xi,yi,np.squeeze(RN))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Radiation Balance Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-200, 200)  #so fit all energy fluxes
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dRN))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Radiation Balance HighAlb-Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-230,100)
plt.show()


cs = m.pcolor(xi,yi,np.squeeze(GFLUX))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Ground Heat Flux Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-200, 200)  #so fit all energy fluxes
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dGFLUX))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Ground Heat Flux HighAlb-Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-230,100)
plt.show()


cs = m.pcolor(xi,yi,np.squeeze(H))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Sensible Heat Flux Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-100,400)
#plt.clim(-200, 200)  #so fit all energy fluxes
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dH))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Sensible Heat Flux HighAlb-Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-230,100)
plt.show()


cs = m.pcolor(xi,yi,np.squeeze(LE))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Latent Heat Flux Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-200,200)  #so fit all energy fluxes
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dLE))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Latent Heat Flux HighAlb-Ref 2015-07-22 %s UTC' %(hour))
#plt.clim(21,35)
plt.show()

'''Air temperature'''

dtair_C = tair2_C - tair_C

#cs = m.pcolor(xi,yi,np.squeeze(tairC))
cs = m.pcolor(xi,yi,np.squeeze(tair_C))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
#cbar.set_label(tair_units)
cbar.set_label(tairC_units)
#cbar.set_label(wind10m_units)
plt.title('2m Air Temperature Ref 2015-07-22 %s UTC' %(hour))
#plt.title('10m Wind Speed - 2015-07-20 18UTC')
plt.clim(25.5,40.5)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dtair_C))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(tairC_units)
plt.title('2m Air Temperature HighAlb-Ref 2015-07-22 %s UTC' %(hour))
#plt.clim(21,35)
plt.show()

