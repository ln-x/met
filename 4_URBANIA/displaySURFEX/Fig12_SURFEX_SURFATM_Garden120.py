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

file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/_S21_GD120_Ref/SURF_ATM_DIAGNOSTICS.OUT.nc'
file2 = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/_S21_GD120/SURF_ATM_DIAGNOSTICS.OUT.nc'
fh = Dataset(file, mode='r')
fh2 = Dataset(file2, mode='r')
# 22.7.0h [103],6h[109], 12h [115],                           18h [121]
hour = 12
hour2 = 18
index = 103+hour
index2 = 103+hour2
print index

lons = fh.variables['xx'][:]  #lon
lats = fh.variables['yy'][:]  #lat

RN0 = fh.variables['RN'][:] #270(time)x135(lon)x174(lat)
H0 = fh.variables['H'][:] #270(time)x135(lon)x174(lat)
LE0 = fh.variables['LE'][:] #270(time)x135(lon)x174(lat)
GFLUX0 = fh.variables['GFLUX'][:] #270(time)x135(lon)x174(lat)
tair0 = fh.variables['T2M'][:] #270(time)x135(lon)x174(lat)

RN20 = fh2.variables['RN'][:] #270(time)x135(lon)x174(lat)
H20 = fh2.variables['H'][:] #270(time)x135(lon)x174(lat)
LE20 = fh2.variables['LE'][:] #270(time)x135(lon)x174(lat)
GFLUX20 = fh2.variables['GFLUX'][:] #270(time)x135(lon)x174(lat)
tair20 = fh2.variables['T2M'][:] #270(time)x135(lon)x174(lat)

RN = fh.variables['RN'][index]
H = fh.variables['H'][index]
LE = fh.variables['LE'][index]
GFLUX = fh.variables['GFLUX'][index]

RN2 = fh2.variables['RN'][index]
H2 = fh2.variables['H'][index]
LE2 = fh2.variables['LE'][index]
GFLUX2 = fh2.variables['GFLUX'][index]

RN_2 = fh.variables['RN'][index2]
H_2 = fh.variables['H'][index2]
LE_2 = fh.variables['LE'][index2]
GFLUX_2 = fh.variables['GFLUX'][index2]

RN2_2 = fh2.variables['RN'][index2]
H2_2 = fh2.variables['H'][index2]
LE2_2 = fh2.variables['LE'][index2]
GFLUX2_2 = fh2.variables['GFLUX'][index2]

dRN0 = RN20 - RN0
dH0 = H20 - H0
dLE0 = LE20 - LE0
dGFLUX0 = GFLUX20 - GFLUX0

dRN = RN2 - RN
dH = H2 - H
dLE = LE2 - LE
dGFLUX = GFLUX2 - GFLUX

dRN_2 = RN2_2 - RN_2
dH_2 = H2_2 - H_2
dLE_2 = LE2_2 - LE_2
dGFLUX_2 = GFLUX2_2 - GFLUX_2

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


'''PLOT DIURNAL'''
Stations = {'11034': ['Wien-Innere Stadt',85,53],'11090':['Wien-Donaufeld',99,72],
             'add1': ['Seestadt Aspern', 110,72]}
             #'11035':  ["Wien-Hohe Warte",83,69],
             #'11036': ['Schwechat',129,25], '11037':['Gross-Enzersdorf',127,54],
             #'11040': ['Wien-Unterlaa',97,29], '11042':['Wien-Stammersdorf',94,88],
             #'11077': ['Brunn am Gebirge',65,24], '11080':['Wien-Mariabrunn',56,56]}
for i in Stations:
  x = Stations[i][1]
  y = Stations[i][2]
  print i, x, y
  RN_timeseries = RN0[:,y,x]
  RN_ts = np.array(RN_timeseries[103:127])#[8:176])
  H_timeseries = H0[:,y,x]
  H_ts = np.array(H_timeseries[103:127])#[8:176])
  LE_timeseries = LE0[:,y,x]
  LE_ts = np.array(LE_timeseries[103:127])#[8:176])
  GFLUX_timeseries = GFLUX0[:,y,x]
  GFLUX_ts = np.array(GFLUX_timeseries[103:127])#[8:176])
  tair_timeseries = tair0[:, y, x]
  tair_ts = np.array(tair_timeseries[103:127])  # [8:176])
  tair_tsC = RN_ts - 273.15
  bal = RN_ts+H_ts+LE_ts+GFLUX_ts

  dRN_timeseries = dRN0[:,y,x]
  dRN_ts = np.array(dRN_timeseries[103:127])#[8:176])
  dH_timeseries = dH0[:,y,x]
  dH_ts = np.array(dH_timeseries[103:127])#[8:176])
  dLE_timeseries = dLE0[:,y,x]
  dLE_ts = np.array(dLE_timeseries[103:127])#[8:176])
  dGFLUX_timeseries = dGFLUX0[:,y,x]
  dGFLUX_ts = np.array(dGFLUX_timeseries[103:127])#[8:176])
  #dtair_timeseries = dtair0_C[:, y, x]
  #dtair_ts = np.array(dtair_timeseries[103:127])  # [8:176])
  #dtair_tsC = dRN_ts - 273.15
  dbal = dRN_ts+dH_ts+dLE_ts+dGFLUX_ts

  fig = plt.figure()
  plt.title(Stations[i][0])
  plt.plot(RN_ts, color='orange', label=u"Q*")
  plt.plot(H_ts, color='red', label=u"H")
  plt.plot(LE_ts, color='blue', label=u"LE")
  plt.plot(GFLUX_ts, color='violet', label=u"G")
  #plt.plot(bal, color='black', label=u"Bal")
  plt.xlabel("hours[UTC]")
  plt.ylabel(r"energy flux density $W m-2$", size="large")
  plt.legend(loc='upper right')
  plt.ylim(-300, 1000)
  plt.xlim(0, 24)
  plt.show()

  fig2 = plt.figure()
  plt.title(Stations[i][0])
  plt.plot(dRN_ts, color='orange', label=u"Q*")
  plt.plot(dH_ts, color='red', label=u"H")
  plt.plot(dLE_ts, color='blue', label=u"LE")
  plt.plot(dGFLUX_ts, color='violet', label=u"G")
  #plt.plot(dbal, color='black', label=u"Bal")
  plt.xlabel("hours[UTC]")
  plt.ylabel(r"difference in energy flux density $W m-2$", size="large")
  plt.legend(loc='lower right')
  plt.xlim(0, 24)
  plt.ylim(-400, 120)
  plt.show()

exit()

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

cs = m.pcolor(xi,yi,np.squeeze(dRN))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Radiation Balance Unseal-Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-230,100)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dGFLUX))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Ground Heat Flux Unseal-Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-230,100)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dH))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Sensible Heat Flux Unseal-Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-230,100)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dLE))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Latent Heat Flux Unseal-Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-230,100)
plt.show()


cs = m.pcolor(xi,yi,np.squeeze(dRN_2))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Radiation Balance Unseal-Ref 2015-07-22 %s UTC' %(hour2))
plt.clim(-230,100)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dGFLUX_2))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Ground Heat Flux Unseal-Ref 2015-07-22 %s UTC' %(hour2))
plt.clim(-230,100)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dH_2))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Sensible Heat Flux Unseal-Ref 2015-07-22 %s UTC' %(hour2))
plt.clim(-230,100)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dLE_2))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Latent Heat Flux Unseal-Ref 2015-07-22 %s UTC' %(hour2))
plt.clim(-230,100)
plt.show()

exit()

'''Air temperature'''

dtair_C = tair2_C - tair_C

cs = m.pcolor(xi,yi,np.squeeze(dtair_C))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(tairC_units)
plt.title('2m Air Temperature Unseal-Ref 2015-07-22 %s UTC' %(hour))
#plt.clim(21,35)
plt.show()

