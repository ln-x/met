# -*- coding: utf-8 -*-
__author__ = 'lnx'

from netCDF4 import Dataset
from pylab import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime

'''This file plots 2D maps of SURFEX.nc files.  
This is the cleaned version of the script, for all comments see Fig4_plotSURFFEXDIFF_nc1.py
For hourly loop look at Fig5_plotSURFEX_nc1_hourly.py'''

#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/_S13/SURF_ATM_DIAGNOSTICS.OUT.nc'
#file2 = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/_S20_ALB/SURF_ATM_DIAGNOSTICS.OUT.nc'
outpath ='/media/lnx/Norskehavet/OFFLINE/plots'
file_ref_pro = '/media/lnx/Norskehavet/OFFLINE/2069REF/dx345corr/TEB_PROGNOSTIC.OUT.nc'
file_alb_pro = '/media/lnx/Norskehavet/OFFLINE/2069ALB/TEB_PROGNOSTIC.OUT.nc'
file_iso_pro = '/media/lnx/Norskehavet/OFFLINE/2069ISO/TEB_PROGNOSTIC.OUT.nc'
file_grr_pro = '/media/lnx/Norskehavet/OFFLINE/2069GRR/TEB_PROGNOSTIC.OUT.nc'
file_grr_grr_pro = '/media/lnx/Norskehavet/OFFLINE/2069GRR/GREENROOF_PROGNOSTIC.OUT.nc'
file_den_pro = '/media/lnx/Norskehavet/OFFLINE/2069DEN/TEB_PROGNOSTIC.OUT.nc'
file_pvr_pro = '/media/lnx/Norskehavet/OFFLINE/2069PVR/TEB_PROGNOSTIC.OUT.nc'
file_spr_pro = '/media/lnx/Norskehavet/OFFLINE/2069SPR/TEB_PROGNOSTIC.OUT.nc'
file_opt_pro = '/media/lnx/Norskehavet/OFFLINE/2069OPT/dx345corr/TEB_PROGNOSTIC.OUT.nc'

f_ref = Dataset(file_ref_pro, mode='r')
f_alb = Dataset(file_alb_pro, mode='r')
f_iso = Dataset(file_iso_pro, mode='r')
f_grr = Dataset(file_grr_pro, mode='r')
f_grr_grr = Dataset(file_grr_grr_pro, mode='r')
f_den = Dataset(file_den_pro, mode='r')
f_pvr = Dataset(file_pvr_pro, mode='r')
f_spr = Dataset(file_spr_pro, mode='r')
f_opt = Dataset(file_opt_pro, mode='r')

'''cut for subregions'''
TSURFACE_units = f_ref.variables['TROOF1'].units

TROOF1_ref_ce = f_ref.variables['TROOF1'][:,50:59,80:89]
TWALL1_ref_ce = f_ref.variables['TWALL1'][:,50:59,80:89]
TGROUND1_ref_ce = f_ref.variables['TROAD1'][:,50:59,80:89]

TROOF1_alb_ce = f_alb.variables['TROOF1'][:,50:59,80:89]
TWALL1_alb_ce = f_alb.variables['TWALL1'][:,50:59,80:89]
TGROUND1_alb_ce = f_alb.variables['TROAD1'][:,50:59,80:89]

TROOF1_iso_ce = f_iso.variables['TROOF1'][:,50:59,80:89]
TWALL1_iso_ce = f_iso.variables['TWALL1'][:,50:59,80:89]
TGROUND1_iso_ce = f_iso.variables['TROAD1'][:,50:59,80:89]

TROOF1_opt_ce = f_opt.variables['TROOF1'][:,50:59,80:89]
TWALL1_opt_ce = f_opt.variables['TWALL1'][:,50:59,80:89]
TGROUND1_opt_ce = f_opt.variables['TROAD1'][:,50:59,80:89]

TWALL1_den_ce = f_den.variables['TWALL1'][:,50:59,80:89]
TGROUND1_den_ce = f_den.variables['TROAD1'][:,50:59,80:89]

#TROOF1_grr_ce = f_grr.variables['TROOF1'][:,50:59,80:89]
TROOF1_grr_ce = f_grr_grr.variables['GR_TG1'][:,50:59,80:89]
TROOF1_pvr_ce = f_pvr.variables['TROOF1'][:,50:59,80:89]


f_ref.close()
f_alb.close()
f_iso.close()
f_den.close()
f_grr.close()
f_pvr.close()
#f_spr.close()
#f_opt.close()

TROOF1_ref_ce = TROOF1_ref_ce.reshape(174,81)
TROOF1_ref_ce_ts = TROOF1_ref_ce.mean(axis=1) - 273.15
TWALL1_ref_ce = TWALL1_ref_ce.reshape(174,81)
TWALL1_ref_ce_ts = TWALL1_ref_ce.mean(axis=1) - 273.15
TGROUND1_ref_ce = TGROUND1_ref_ce.reshape(174,81)
TGROUND_ref_ce_ts = TGROUND1_ref_ce.mean(axis=1) - 273.15

TROOF1_alb_ce = TROOF1_alb_ce.reshape(174,81)
TROOF1_alb_ce_ts = TROOF1_alb_ce.mean(axis=1) - 273.15
TWALL1_alb_ce = TWALL1_alb_ce.reshape(174,81)
TWALL1_alb_ce_ts = TWALL1_alb_ce.mean(axis=1) - 273.15
TGROUND1_alb_ce = TGROUND1_alb_ce.reshape(174,81)
TGROUND_alb_ce_ts = TGROUND1_alb_ce.mean(axis=1) - 273.15

TROOF1_iso_ce = TROOF1_iso_ce.reshape(174,81)
TROOF1_iso_ce_ts = TROOF1_iso_ce.mean(axis=1) - 273.15
TWALL1_iso_ce = TWALL1_iso_ce.reshape(174,81)
TWALL1_iso_ce_ts = TWALL1_iso_ce.mean(axis=1) - 273.15
TGROUND1_iso_ce = TGROUND1_iso_ce.reshape(174,81)
TGROUND_iso_ce_ts = TGROUND1_iso_ce.mean(axis=1) - 273.15

TROOF1_opt_ce = TROOF1_opt_ce.reshape(174,81)
TROOF1_opt_ce_ts = TROOF1_opt_ce.mean(axis=1) - 273.15
TWALL1_opt_ce = TWALL1_opt_ce.reshape(174,81)
TWALL1_opt_ce_ts = TWALL1_opt_ce.mean(axis=1) - 273.15
TGROUND1_opt_ce = TGROUND1_opt_ce.reshape(174,81)
TGROUND_opt_ce_ts = TGROUND1_opt_ce.mean(axis=1) - 273.15

TWALL1_den_ce = TWALL1_den_ce.reshape(174,81)
TWALL1_den_ce_ts = TWALL1_den_ce.mean(axis=1) - 273.15
TGROUND1_den_ce = TGROUND1_den_ce.reshape(174,81)
TGROUND_den_ce_ts = TGROUND1_den_ce.mean(axis=1) - 273.15

TROOF1_grr_ce = TROOF1_grr_ce.reshape(174,81)
TROOF1_grr_ce_ts = TROOF1_grr_ce.mean(axis=1) - 273.15

TROOF1_pvr_ce = TROOF1_pvr_ce.reshape(174,81)
TROOF1_pvr_ce_ts = TROOF1_pvr_ce.mean(axis=1) - 273.15

start = datetime.datetime(2069,7,1,19,0)  #1...174
stop = datetime.datetime(2069,7,9,0,0)
delta = datetime.timedelta(hours=1)
dates = mpl.dates.drange(start,stop,delta)
#print dates.shape
#exit()
#date_format = mpl.dates.DateFormatter('%d %B %Y')
date_format = mpl.dates.DateFormatter('      %H') #Meteorol. Z. Format:  %H%M UTC %d %B %Y

fig = plt.figure()
plt.title("ROOF")
plt.plot(dates, TROOF1_ref_ce_ts, color='black', label=u"REF")
#plt.plot(TROOF1_opt_ce_ts, color='green', label=u"OPT")
plt.plot(dates, TROOF1_alb_ce_ts, color='violet', label=u"ALB")#, linestyle=":")
plt.plot(dates, TROOF1_iso_ce_ts, color='red', label=u"INS")#, linestyle=":")
plt.plot(dates, TROOF1_grr_ce_ts, color='darkgreen', label=u"GRR")#, linestyle=":")
plt.plot(dates, TROOF1_pvr_ce_ts, color='blue', label=u"PVR")#, linestyle=":")
plt.xlabel("Time [UTC]")
plt.ylabel(u"Surface temperature [°C]", size="large")
plt.legend(loc='lower right', ncol=3)
plt.ylim(0, 100)
#plt.ylim(-5, 10)

ax1 = gca()
days = DayLocator(range(2, 9), interval=1)
hours = HourLocator(range(0, 23), interval=6)
ax1.xaxis.set_major_locator(hours)
ax1.xaxis.set_major_formatter(date_format)
ax1.grid(linestyle=":")
plt.xticks(rotation='vertical', fontsize='small')
plt.subplots_adjust(bottom=.3)

plt.show()
#exit()

fig = plt.figure()
plt.title("WALL")
plt.plot(dates, TWALL1_ref_ce_ts, color='black', label=u"REF")
#plt.plot(TWALL1_opt_ce_ts, color='green', label=u"OPT")
plt.plot(dates, TWALL1_alb_ce_ts, color='violet', label=u"ALB")#, linestyle=":")
plt.plot(dates, TWALL1_iso_ce_ts, color='red', label=u"INS")#, linestyle=":")
#plt.plot(TWALL1_grr_ce_ts, color='darkgreen', label=u"GRR", linestyle=":")
#plt.plot(TWALL1_pvr_ce_ts, color='blue', label=u"PVR", linestyle=":")
plt.xlabel("Time [UTC]", size="large")
plt.ylabel(u"Surface temperature [°C]", size="large")
plt.legend(loc='lower right', ncol=3)
plt.ylim(0, 100)
#plt.ylim(-5, 10)
ax2 = gca()
hours = HourLocator(range(0, 23), interval=6)
ax2.xaxis.set_major_locator(hours)
ax2.xaxis.set_major_formatter(date_format)
ax2.grid(linestyle=":")
plt.xticks(rotation='vertical', fontsize='small')
plt.subplots_adjust(bottom=.3)
plt.show()

fig = plt.figure()
plt.title("ROAD")
plt.plot(dates, TGROUND_ref_ce_ts, color='black', label=u"REF")
#plt.plot(TGROUND_opt_ce_ts, color='green', label=u"OPT")
plt.plot(dates, TGROUND_alb_ce_ts, color='violet', label=u"ALB")#, linestyle=":")
plt.plot(dates, TGROUND_iso_ce_ts, color='red', label=u"INS")#, linestyle=":")
#plt.plot(TWALL1_grr_ce_ts, color='darkgreen', label=u"GRR", linestyle=":")
#plt.plot(TWALL1_pvr_ce_ts, color='blue', label=u"PVR", linestyle=":")
plt.xlabel("Time [UTC]", size="large")
plt.ylabel(u"Surface temperature [°C]", size="large")
plt.legend(loc='lower right', ncol=3)
plt.ylim(0, 100)
#plt.ylim(-5, 10)
ax3 = gca()
days = DayLocator(range(2, 9), interval=1)
hours = HourLocator(range(0, 23), interval=6)
ax3.xaxis.set_major_locator(hours)
ax3.xaxis.set_major_formatter(date_format)
ax3.grid(linestyle=":")
plt.xticks(rotation='vertical', fontsize='small')
plt.subplots_adjust(bottom=.3)
plt.show()

