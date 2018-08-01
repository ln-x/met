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

file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S12/SURF_ATM_DIAGNOSTICS.OUT.nc'
file2 = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S13/SURF_ATM_DIAGNOSTICS.OUT.nc'
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S12_FORC_WRF_333_STQ_2DURBPARAM_long/SURF_ATM_DIAGNOSTICS.OUT.nc'
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S17_XUNIF/SURF_ATM_DIAGNOSTICS.OUT.nc'
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S15_XUNIF/SURF_ATM_DIAGNOSTICS.OUT.nc'
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S15_XUNIF/SURF_ATM_DIAGNOSTICS.OUT.nc'
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/DIFF_S4_S0_SURF_ATM_D.nc'
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S0_FORC_WRF_333_STQ_long/SURF_ATM_DIAGNOSTICS.OUT.nc'
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S3_LNX_WRF_333_nGD/SURF_ATM_DIAGNOSTICS.OUT.nc'
#file = '/home/lnx/MODELS/SURFEX/3_input/met_forcing/FORCING_new.nc'
fh = Dataset(file, mode='r')
fh2 = Dataset(file2, mode='r')
hour = 12
hour2 = 18

lons = fh.variables['xx'][:]  #lon
lats = fh.variables['yy'][:]  #lat

RN = fh.variables['RN'][115]
H = fh.variables['H'][115]
LE = fh.variables['LE'][115]
GFLUX = fh.variables['GFLUX'][115]

RN2 = fh2.variables['RN'][115]
H2 = fh2.variables['H'][115]
LE2 = fh2.variables['LE'][115]
GFLUX2 = fh2.variables['GFLUX'][115]

RN_2 = fh.variables['RN'][121]
H_2 = fh.variables['H'][121]
LE_2 = fh.variables['LE'][121]
GFLUX_2 = fh.variables['GFLUX'][121]

RN2_2 = fh2.variables['RN'][121]
H2_2 = fh2.variables['H'][121]
LE2_2 = fh2.variables['LE'][121]
GFLUX2_2 = fh2.variables['GFLUX'][121]

tair0UTC = fh.variables['T2M'][55]
tair6UTC = fh.variables['T2M'][61]
tair12UTC = fh.variables['T2M'][67]
tair18UTC = fh.variables['T2M'][73]
wind10m =fh.variables['W10M'][73]

#starts at 17.7.18hUTC [0], hourly ->
# 18.7.0h [7],6h[13], 12h [19], 14h [21], 18h [42], 6h [54]
# 20.7.  COLDEST: 0h[55], 5h[60], 6h[61], 12h [67], 14h[69], HOTTEST 15h[70], 18h [73]
# 22.7.  0h[103], 6h[109], 12h [115], 18h [121]

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

dRN_2 = RN2_2 - RN_2
dH_2 = H2_2 - H_2
dLE_2 = LE2_2 - LE_2
dGFLUX_2 = GFLUX2_2 - GFLUX_2

cs = m.pcolor(xi,yi,np.squeeze(RN))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Radiation Balance STQ 2015-07-22 %s UTC' %(hour))
#plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dRN))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Radiation Balance Ref-STQ 2015-07-22 %s UTC' %(hour))
plt.clim(-20,20)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(GFLUX))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Ground Heat Flux STQ 2015-07-22 %s UTC' %(hour))
#plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dGFLUX))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Ground Heat Flux Ref-STQ 2015-07-22 %s UTC' %(hour))
plt.clim(-20,20)
#plt.show()


cs = m.pcolor(xi,yi,np.squeeze(H))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Sensible Heat Flux STQ 2015-07-22 %s UTC' %(hour))
#plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dH))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Sensible Heat Flux Ref-STQ 2015-07-22 %s UTC' %(hour))
plt.clim(-20,20)
plt.show()


cs = m.pcolor(xi,yi,np.squeeze(LE))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Latent Heat Flux STQ 2015-07-22 %s UTC' %(hour))
#plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dLE))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Latent Heat Flux Ref-STQ 2015-07-22 %s UTC' %(hour))
plt.clim(-20,20)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dRN_2))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Radiation Balance Ref-STQ 2015-07-22 %s UTC' %(hour2))
plt.clim(-20,20)
plt.show()


cs = m.pcolor(xi,yi,np.squeeze(GFLUX_2))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Ground Heat Flux STQ 2015-07-22 %s UTC' %(hour2))
#plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dGFLUX_2))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Ground Heat Flux Ref-STQ 2015-07-22 %s UTC' %(hour2))
plt.clim(-20,20)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dH_2))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Sensible Heat Flux Ref-STQ 2015-07-22 %s UTC' %(hour2))
plt.clim(-20,20)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dLE_2))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Latent Heat Flux Ref-STQ 2015-07-22 %s UTC' %(hour2))
plt.clim(-20,20)
plt.show()

exit()


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


