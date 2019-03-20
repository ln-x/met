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

#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/_S13/SURF_ATM_DIAGNOSTICS.OUT.nc'
#file2 = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/_S20_ALB/SURF_ATM_DIAGNOSTICS.OUT.nc'
outpath ='/media/lnx/Norskehavet/OFFLINE/plots'
file_ref = '/media/lnx/Norskehavet/OFFLINE/2069REF/dx345corr/SURF_ATM_DIAGNOSTICS.OUT.nc'
file_alb = '/media/lnx/Norskehavet/OFFLINE/2069ALB/SURF_ATM_DIAGNOSTICS.OUT.nc'
file_iso = '/media/lnx/Norskehavet/OFFLINE/2069ISO/SURF_ATM_DIAGNOSTICS.OUT.nc'
file_grr = '/media/lnx/Norskehavet/OFFLINE/2069GRR/SURF_ATM_DIAGNOSTICS.OUT.nc'
file_den = '/media/lnx/Norskehavet/OFFLINE/2069DEN/SURF_ATM_DIAGNOSTICS.OUT.nc'
file_pvr = '/media/lnx/Norskehavet/OFFLINE/2069PVR/SURF_ATM_DIAGNOSTICS.OUT.nc'
file_spr = '/media/lnx/Norskehavet/OFFLINE/2069SPR/SURF_ATM_DIAGNOSTICS.OUT.nc'
file_opt = '/media/lnx/Norskehavet/OFFLINE/2069OPT/dx345corr/SURF_ATM_DIAGNOSTICS.OUT.nc'

f_ref = Dataset(file_ref, mode='r')
f_alb = Dataset(file_alb, mode='r')
f_iso = Dataset(file_iso, mode='r')
f_grr = Dataset(file_grr, mode='r')
f_den = Dataset(file_den, mode='r')
f_pvr = Dataset(file_pvr, mode='r')
f_spr = Dataset(file_spr, mode='r')
f_opt = Dataset(file_opt, mode='r')
var_units = f_ref.variables['RN'].units

'''cut for subregions'''
RN_ref = f_ref.variables['RN'][:]
RN_ref_ce = f_ref.variables['RN'][:,50:59,80:89]
H_ref = f_ref.variables['H'][:] #270(time)x135(lon)x174(lat)
LE_ref = f_ref.variables['LE'][:] #270(time)x135(lon)x174(lat)
GFLUX_ref = f_ref.variables['GFLUX'][:] #270(time)x135(lon)x174(lat)
tair_ref = f_ref.variables['T2M'][:] #270(time)x135(lon)x174(lat)

RN_alb = f_alb.variables['RN'][:]
H_alb = f_alb.variables['H'][:] #270(time)x135(lon)x174(lat)
LE_alb = f_alb.variables['LE'][:] #270(time)x135(lon)x174(lat)
GFLUX_alb = f_alb.variables['GFLUX'][:] #270(time)x135(lon)x174(lat)
tair_alb = f_alb.variables['T2M'][:] #270(time)x135(lon)x174(lat)

RN_iso = f_iso.variables['RN'][:]
H_iso = f_iso.variables['H'][:] #270(time)x135(lon)x174(lat)
LE_iso = f_iso.variables['LE'][:] #270(time)x135(lon)x174(lat)
GFLUX_iso = f_iso.variables['GFLUX'][:] #270(time)x135(lon)x174(lat)
tair_iso = f_iso.variables['T2M'][:] #270(time)x135(lon)x174(lat)


#print H_ref - H_iso
#exit()

# 22.7.0h [103],6h[109], 12h [115],                           18h [121]
hour = 12
index = 103+hour

lons = f_ref.variables['xx'][:]  #lon
lats = f_ref.variables['yy'][:]  #lat

dRN0 = RN_alb - RN_ref
dH0 = H_alb - H_ref
dLE0 = LE_alb - LE_ref
dGFLUX0 = GFLUX_alb - GFLUX_ref
dGFLUX0 = GFLUX_alb - GFLUX_ref

#dRN = RN2 - RN
#dH = H2 - H
#dLE = LE2 - LE
#dGFLUX = GFLUX2 - GFLUX

heatflux_units = f_ref.variables['RN'].units

f_ref.close()
f_alb.close()
f_iso.close()
f_den.close()
f_grr.close()
f_pvr.close()
f_spr.close()
f_opt.close()


'''CONVERSTION TO CELSIUS'''
def Kelvin_to_Celsius(tair):
    tairC = tair.copy()
    for i in range(len(tair)):
        for j in range(len(tair[i])):
            tairC[i][j] = tair[i][j] - 273.15
    return tairC

tairC_units = (u"°C")

#tair_C = Kelvin_to_Celsius(tair)
#tair2_C = Kelvin_to_Celsius(tair2)
#tair0_C = Kelvin_to_Celsius(tair0)
#tair20_C = Kelvin_to_Celsius(tair20)

#dtair_C = tair2_C - tair_C
#dtair0_C = tair20_C - tair0_C


'''PLOT DIURNAL'''
Stations = {'11034': ['Wien-Innere Stadt',85,53],'11090':['Wien-Donaufeld',99,72],
             'add1': ['Seestadt Aspern', 111,72],
             '11035': ["Wien-Hohe Warte",83,69],
             '11036': ['Schwechat',129,25], '11037':['Gross-Enzersdorf',127,54],
             '11040': ['Wien-Unterlaa',97,29], '11042':['Wien-Stammersdorf',94,88],
             '11077': ['Brunn am Gebirge',65,24], '11080':['Wien-Mariabrunn',56,56]}

start = 1 #103
end = 270 #128

for i in Stations:
  x = Stations[i][1]
  y = Stations[i][2]
  print i, x, y
  RN_timeseries = RN_ref[:,y,x]
  RN_ts = np.array(RN_timeseries[start:end])#[8:176])
  H_timeseries = H_ref[:,y,x]
  H_ts = np.array(H_timeseries[start:end])#[8:176])
  LE_timeseries = LE_ref[:,y,x]
  LE_ts = np.array(LE_timeseries[start:end])#[8:176])
  GFLUX_timeseries = GFLUX_ref[:,y,x]
  GFLUX_ts = np.array(GFLUX_timeseries[start:end])#[8:176])
  tair_timeseries = tair_ref[:, y, x]
  tair_ts = np.array(tair_timeseries[start:end])  # [8:176])
  tair_tsC = RN_ts - 273.15
  bal = RN_ts+H_ts+LE_ts+GFLUX_ts

  dRN_timeseries = dRN0[:,y,x]
  dRN_ts = np.array(dRN_timeseries[start:end])#[8:176])
  dH_timeseries = dH0[:,y,x]
  dH_ts = np.array(dH_timeseries[start:end])#[8:176])
  dLE_timeseries = dLE0[:,y,x]
  dLE_ts = np.array(dLE_timeseries[start:end])#[8:176])
  dGFLUX_timeseries = dGFLUX0[:,y,x]
  dGFLUX_ts = np.array(dGFLUX_timeseries[start:end])#[8:176])
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
  #plt.xlim(0, 24)
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
  #plt.xlim(0, 24)
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


cs = m.pcolor(xi,yi,np.squeeze(RN))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Radiation Balance Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-300,1050)  #so fit all energy fluxes
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
plt.clim(-300,1050)  #so fit all energy fluxes
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
#plt.clim(-300,1050)  #so fit all energy fluxes
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dH))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Sensible Heat Flux HighAlb-Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-230,100)
plt.show()

#exit()

cs = m.pcolor(xi,yi,np.squeeze(LE))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Latent Heat Flux Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-300,1050)  #so fit all energy fluxes
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dLE))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Latent Heat Flux HighAlb-Ref 2015-07-22 %s UTC' %(hour))
#plt.clim(21,35)
plt.show()

'''Air temperature'''

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

