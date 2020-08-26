# -*- coding: utf-8 -*-
__author__ = 'lnx'

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import csv
from pylab import *
import matplotlib as mpl
import datetime

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
RN_ref_ce = f_ref.variables['RN'][:,50:59,80:89]
H_ref_ce = f_ref.variables['H'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
LE_ref_ce = f_ref.variables['LE'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
GFLUX_ref_ce = f_ref.variables['GFLUX'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
tair_ref_ce = f_ref.variables['T2M'][:,50:59,80:89] #270(time)x135(lon)x174(lat)

RN_alb_ce = f_alb.variables['RN'][:,50:59,80:89]
H_alb_ce = f_alb.variables['H'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
LE_alb_ce = f_alb.variables['LE'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
GFLUX_alb_ce = f_alb.variables['GFLUX'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
tair_alb_ce = f_alb.variables['T2M'][:,50:59,80:89] #270(time)x135(lon)x174(lat)

RN_iso_ce = f_iso.variables['RN'][:,50:59,80:89]
H_iso_ce = f_iso.variables['H'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
LE_iso_ce = f_iso.variables['LE'][:,50:59,80:89] #270(time)x135(ln)x174(lat)
GFLUX_iso_ce = f_iso.variables['GFLUX'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
tair_iso_ce = f_iso.variables['T2M'][:,50:59,80:89] #270(time)x135(lon)x174(lat)

RN_grr_ce = f_grr.variables['RN'][:,50:59,80:89]
H_grr_ce = f_grr.variables['H'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
LE_grr_ce = f_grr.variables['LE'][:,50:59,80:89] #270(time)x135(ln)x174(lat)
GFLUX_grr_ce = f_grr.variables['GFLUX'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
tair_grr_ce = f_grr.variables['T2M'][:,50:59,80:89] #270(time)x135(lon)x174(lat)

RN_den_ce = f_den.variables['RN'][:,50:59,80:89]
H_den_ce = f_den.variables['H'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
LE_den_ce = f_den.variables['LE'][:,50:59,80:89] #270(time)x135(ln)x174(lat)
GFLUX_den_ce = f_den.variables['GFLUX'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
tair_den_ce = f_den.variables['T2M'][:,50:59,80:89] #270(time)x135(lon)x174(lat)

RN_pvr_ce = f_pvr.variables['RN'][:,50:59,80:89]
H_pvr_ce = f_pvr.variables['H'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
LE_pvr_ce = f_pvr.variables['LE'][:,50:59,80:89] #270(time)x135(ln)x174(lat)
GFLUX_pvr_ce = f_pvr.variables['GFLUX'][:,50:59,80:89] #270(time)x135(lon)x174(lat)
tair_pvr_ce = f_pvr.variables['T2M'][:,50:59,80:89] #270(time)x135(lon)x174(lat)

heatflux_units = f_ref.variables['RN'].units

f_ref.close()
f_alb.close()
f_iso.close()
f_den.close()
f_grr.close()
f_pvr.close()
f_spr.close()
f_opt.close()

start = 1
end = 174

RN_ref_ce = RN_ref_ce.reshape(174,81)
RN_ref_ce_ts = RN_ref_ce.mean(axis=1)
H_ref_ce = H_ref_ce.reshape(174,81)
H_ref_ce_ts = H_ref_ce.mean(axis=1)
LE_ref_ce = LE_ref_ce.reshape(174,81)
LE_ref_ce_ts = (LE_ref_ce.mean(axis=1))
G_ref_ce = GFLUX_alb_ce.reshape(174,81)
G_ref_ce_ts = G_ref_ce.mean(axis=1)

RN_alb_ce = RN_alb_ce.reshape(174,81)
RN_alb_ce_ts = RN_alb_ce.mean(axis=1)
H_alb_ce = H_alb_ce.reshape(174,81)
H_alb_ce_ts = H_alb_ce.mean(axis=1)
LE_alb_ce = LE_alb_ce.reshape(174,81)
LE_alb_ce_ts = (LE_alb_ce.mean(axis=1))
G_alb_ce = GFLUX_alb_ce.reshape(174,81)
G_alb_ce_ts = G_alb_ce.mean(axis=1)

RN_iso_ce = RN_iso_ce.reshape(174,81)
RN_iso_ce_ts = RN_iso_ce.mean(axis=1)
H_iso_ce = H_iso_ce.reshape(174,81)
H_iso_ce_ts = H_iso_ce.mean(axis=1)
LE_iso_ce = LE_iso_ce.reshape(174,81)
LE_iso_ce_ts = (LE_iso_ce.mean(axis=1))
G_iso_ce = GFLUX_iso_ce.reshape(174,81)
G_iso_ce_ts = G_iso_ce.mean(axis=1)

RN_grr_ce = RN_grr_ce.reshape(174,81)
RN_grr_ce_ts = RN_grr_ce.mean(axis=1)
H_grr_ce = H_grr_ce.reshape(174,81)
H_grr_ce_ts = H_grr_ce.mean(axis=1)
LE_grr_ce = LE_grr_ce.reshape(174,81)
LE_grr_ce_ts = (LE_grr_ce.mean(axis=1))
G_grr_ce = GFLUX_grr_ce.reshape(174,81)
G_grr_ce_ts = G_grr_ce.mean(axis=1)

RN_den_ce = RN_den_ce.reshape(174,81)
RN_den_ce_ts = RN_den_ce.mean(axis=1)
H_den_ce = H_den_ce.reshape(174,81)
H_den_ce_ts = H_den_ce.mean(axis=1)
LE_den_ce = LE_den_ce.reshape(174,81)
LE_den_ce_ts = (LE_den_ce.mean(axis=1))
G_den_ce = GFLUX_den_ce.reshape(174,81)
G_den_ce_ts = G_den_ce.mean(axis=1)

RN_pvr_ce = RN_pvr_ce.reshape(174,81)
RN_pvr_ce_ts = RN_pvr_ce.mean(axis=1)
H_pvr_ce = H_pvr_ce.reshape(174,81)
H_pvr_ce_ts = H_pvr_ce.mean(axis=1)
LE_pvr_ce = LE_pvr_ce.reshape(174,81)
LE_pvr_ce_ts = (LE_pvr_ce.mean(axis=1))
G_pvr_ce = GFLUX_pvr_ce.reshape(174,81)
G_pvr_ce_ts = G_pvr_ce.mean(axis=1)

dRN_alb_ce = RN_alb_ce_ts - RN_ref_ce_ts
dH_alb_ce = H_alb_ce_ts - H_ref_ce_ts
dLE_alb_ce = LE_alb_ce_ts - LE_ref_ce_ts
dG_alb_ce = G_alb_ce_ts - G_ref_ce_ts

dRN_iso_ce = RN_iso_ce_ts - RN_ref_ce_ts
dH_iso_ce = H_iso_ce_ts - H_ref_ce_ts
dLE_iso_ce = LE_iso_ce_ts - LE_ref_ce_ts
dG_iso_ce = G_iso_ce_ts - G_ref_ce_ts

dRN_grr_ce = RN_grr_ce_ts - RN_ref_ce_ts
dH_grr_ce = H_grr_ce_ts - H_ref_ce_ts
dLE_grr_ce = LE_grr_ce_ts - LE_ref_ce_ts
dG_grr_ce = G_grr_ce_ts - G_ref_ce_ts

dRN_den_ce = RN_den_ce_ts - RN_ref_ce_ts
dH_den_ce = H_den_ce_ts - H_ref_ce_ts
dLE_den_ce = LE_den_ce_ts - LE_ref_ce_ts
dG_den_ce = G_den_ce_ts - G_ref_ce_ts

dRN_pvr_ce = RN_pvr_ce_ts - RN_ref_ce_ts
dH_pvr_ce = H_pvr_ce_ts - H_ref_ce_ts
dLE_pvr_ce = LE_pvr_ce_ts - LE_ref_ce_ts
dG_pvr_ce = G_pvr_ce_ts - G_ref_ce_ts

bal = RN_ref_ce_ts+H_ref_ce_ts+LE_ref_ce_ts+G_ref_ce_ts
dbal_alb = dRN_alb_ce+dH_alb_ce+dLE_alb_ce+dG_alb_ce
dbal_iso = dRN_iso_ce+dH_iso_ce+dLE_iso_ce+dG_iso_ce
dbal_grr = dRN_grr_ce+dH_grr_ce+dLE_grr_ce+dG_grr_ce
dbal_den = dRN_den_ce+dH_den_ce+dLE_den_ce+dG_den_ce
dbal_pvr = dRN_pvr_ce+dH_pvr_ce+dLE_pvr_ce+dG_pvr_ce

start = datetime.datetime(2069,7,1,19,0)  #1...174
stop = datetime.datetime(2069,7,9,0,0)
delta = datetime.timedelta(hours=1)
dates = mpl.dates.drange(start,stop,delta)
#print dates.shape
#exit()
#date_format = mpl.dates.DateFormatter('%d %B %Y')
date_format = mpl.dates.DateFormatter('      %H')# %d %B') #Meteorol. Z. Format:  %H%M UTC %d %B %Y


fig = plt.figure()
plt.title("REF", size="large")
plt.plot(dates, RN_ref_ce_ts, color='orange', label=u"Q*")
plt.plot(dates, H_ref_ce_ts, color='red', label=u"H")
plt.plot(dates, LE_ref_ce_ts, color='blue', label=u"LE")
plt.plot(dates, G_ref_ce_ts, color='violet', label=u"G")
plt.plot(dates, bal, color='black', label=u"Bal")
plt.xlabel("Time [UTC]", size="large")
plt.ylabel(r"Energy flux density $[W m-2]$", size="large")
#plt.legend(loc='upper right')
plt.ylim(-300, 1500)
#plt.xlim(0, 24)
ax1 = gca()
days = DayLocator(range(2, 9), interval=1)
hours = HourLocator(range(0, 23), interval=6)
ax1.xaxis.set_major_locator(hours)
ax1.xaxis.set_major_formatter(date_format)
ax1.grid(linestyle=":")
plt.xticks(rotation='vertical')#, fontsize='small')
plt.subplots_adjust(bottom=.3)
plt.show()

#exit()

fig2 = plt.figure()
plt.title("ALB-REF", size="large")
plt.plot(dates, dRN_alb_ce, color='orange', label=u"Q*")
plt.plot(dates, dH_alb_ce, color='red', label=u"H")
plt.plot(dates, dLE_alb_ce, color='blue', label=u"LE")
plt.plot(dates, dG_alb_ce, color='violet', label=u"G")
plt.plot(dates, dbal_alb, color='black', label=u"Bal")
plt.xlabel("Time [UTC]", size="large")
plt.ylabel(r"Difference in energy flux density $[W m-2]$", size="large")
#plt.legend(loc='lower right')
#plt.xlim(0, 24)
plt.ylim(-400, 300)
ax1 = gca()
days = DayLocator(range(2, 9), interval=1)
hours = HourLocator(range(0, 23), interval=6)
ax1.xaxis.set_major_locator(hours)
ax1.xaxis.set_major_formatter(date_format)
ax1.grid(linestyle=":")
plt.xticks(rotation='vertical', fontsize='small')
plt.subplots_adjust(bottom=.3)
plt.show()

fig3 = plt.figure()
plt.title("INS-REF", size="large")
plt.plot(dates, dRN_iso_ce, color='orange', label=u"Q*")
plt.plot(dates, dH_iso_ce, color='red', label=u"H")
plt.plot(dates, dLE_iso_ce, color='blue', label=u"LE")
plt.plot(dates, dG_iso_ce, color='violet', label=u"G")
plt.plot(dates, dbal_iso, color='black', label=u"Bal")
plt.xlabel("Time [UTC]", size="large")
plt.ylabel(r"Difference in energy flux density $[W m-2]$", size="large")
#plt.legend(loc='lower right')
#plt.xlim(0, 24)
plt.ylim(-400, 300)
ax1 = gca()
days = DayLocator(range(2, 9), interval=1)
hours = HourLocator(range(0, 23), interval=6)
ax1.xaxis.set_major_locator(hours)
ax1.xaxis.set_major_formatter(date_format)
ax1.grid(linestyle=":")
plt.xticks(rotation='vertical', fontsize='small')
plt.subplots_adjust(bottom=.3)
plt.show()

fig4 = plt.figure()
plt.title("GRR-REF", size="large")
plt.plot(dates, dRN_grr_ce, color='orange', label=u"Q*")
plt.plot(dates, dH_grr_ce, color='red', label=u"H")
plt.plot(dates, dLE_grr_ce, color='blue', label=u"LE")
plt.plot(dates, dG_grr_ce, color='violet', label=u"G")
plt.plot(dates, dbal_grr, color='black', label=u"Bal")
plt.xlabel("Time [UTC]" , size="large")
plt.ylabel(r"Difference in energy flux density $[W m-2]$", size="large")
#plt.legend(loc='lower right')
#plt.xlim(0, 24)
plt.ylim(-400, 300)
ax1 = gca()
days = DayLocator(range(2, 9), interval=1)
hours = HourLocator(range(0, 23), interval=6)
ax1.xaxis.set_major_locator(hours)
ax1.xaxis.set_major_formatter(date_format)
ax1.grid(linestyle=":")
plt.xticks(rotation='vertical', fontsize='small')
plt.subplots_adjust(bottom=.3)
plt.show()

fig5 = plt.figure()
plt.title("DEN-REF", size="large")
plt.plot(dates, dbal_den, color='black', label=u"Bal")
plt.plot(dates, dRN_den_ce, color='orange', label=u"Q*")
plt.plot(dates, dH_den_ce, color='red', label=u"H")
plt.plot(dates, dLE_den_ce, color='blue', label=u"LE")
plt.plot(dates, dG_den_ce, color='violet', label=u"G")
plt.xlabel("Time [UTC]", size="large")
plt.ylabel(r"Difference in energy flux density $[W m-2]$", size="large")
#plt.legend(loc='lower right')
#plt.xlim(0, 24)
plt.ylim(-400, 300)
ax1 = gca()
days = DayLocator(range(2, 9), interval=1)
hours = HourLocator(range(0, 23), interval=6)
ax1.xaxis.set_major_locator(hours)
ax1.xaxis.set_major_formatter(date_format)
ax1.grid(linestyle=":")
plt.xticks(rotation='vertical', fontsize='small')
plt.subplots_adjust(bottom=.3)
plt.show()

fig6 = plt.figure()
plt.title("PVR-REF", size="large")
plt.plot(dates, dRN_pvr_ce, color='orange', label=u"Q*")
plt.plot(dates, dH_pvr_ce, color='red', label=u"H")
plt.plot(dates, dLE_pvr_ce, color='blue', label=u"LE")
plt.plot(dates, dG_pvr_ce, color='violet', label=u"G")
plt.plot(dates, dbal_pvr, color='black', label=u"Bal")
plt.xlabel("Time [UTC]", size="large")
plt.ylabel(r"Difference in energy flux density $[W m-2]$", size="large")
#plt.legend(loc='lower right')
#plt.xlim(0, 24)
plt.ylim(-400, 300)
ax1 = gca()
days = DayLocator(range(2, 9), interval=1)
hours = HourLocator(range(0, 23), interval=6)
ax1.xaxis.set_major_locator(hours)
ax1.xaxis.set_major_formatter(date_format)
ax1.grid(linestyle=":")
plt.xticks(rotation='vertical', fontsize='small')
plt.subplots_adjust(bottom=.3)
plt.show()
exit()
