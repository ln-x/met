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

start = 1
end = 174

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

"""
dTRADSH_alb_ce = TRADSH_alb_ce_ts - TRADSH_ref_ce_ts
dU10M_alb_ce = U10M_alb_ce_ts - U10M_ref_ce_ts
dQCANYON_alb_ce = QCANYON_alb_ce_ts - QCANYON_ref_ce_ts
dTCANYON_alb_ce = TCANYONalb_ce_ts - TCANYON_ref_ce_ts

dTRADSH_iso_ce = TRADSH_iso_ce_ts - TRADSH_ref_ce_ts
dU10M_iso_ce = U10M_iso_ce_ts - U10M_ref_ce_ts
dQCANYON_iso_ce = QCANYON_iso_ce_ts - QCANYON_ref_ce_ts
dTCANYON_iso_ce = TCANYONiso_ce_ts - TCANYON_ref_ce_ts

dTRADSH_grr_ce = TRADSH_grr_ce_ts - TRADSH_ref_ce_ts
dU10M_grr_ce = U10M_grr_ce_ts - U10M_ref_ce_ts
dQCANYON_grr_ce = QCANYON_grr_ce_ts - QCANYON_ref_ce_ts
dTCANYON_grr_ce = TCANYONgrr_ce_ts - TCANYON_ref_ce_ts

dTRADSH_den_ce = TRADSH_den_ce_ts - TRADSH_ref_ce_ts
dU10M_den_ce = U10M_den_ce_ts - U10M_ref_ce_ts
dQCANYON_den_ce = QCANYON_den_ce_ts - QCANYON_ref_ce_ts
dTCANYON_den_ce = TCANYONden_ce_ts - TCANYON_ref_ce_ts

dTRADSH_pvr_ce = TRADSH_pvr_ce_ts - TRADSH_ref_ce_ts
dU10M_pvr_ce = U10M_pvr_ce_ts - U10M_ref_ce_ts
dQCANYON_pvr_ce = QCANYON_pvr_ce_ts - QCANYON_ref_ce_ts
dTCANYON_pvr_ce = TCANYON_pvr_ce_ts - TCANYON_ref_ce_ts

bal = TRADSH_ref_ce_ts+U10M_ref_ce_ts+QCANYON_ref_ce_ts+TCANYON_ref_ce_ts
dbal_alb = dTRADSH_alb_ce+dU10M_alb_ce+dQCANYON_alb_ce+dTCANYON_alb_ce
dbal_iso = dTRADSH_iso_ce+dU10M_iso_ce+dQCANYON_iso_ce+dTCANYON_iso_ce
dbal_grr = dTRADSH_grr_ce+dU10M_grr_ce+dQCANYON_grr_ce+dTCANYON_grr_ce
dbal_den = dTRADSH_den_ce+dU10M_den_ce+dQCANYON_den_ce+dTCANYON_den_ce
dbal_pvr = dTRADSH_pvr_ce+dU10M_pvr_ce+dQCANYON_pvr_ce+dTCANYON_pvr_ce
"""
start = datetime.datetime(2069,7,1,20,0)  #1...174
stop = datetime.datetime(2069,7,9,2,0)
delta = datetime.timedelta(hours=1)
dates = mpl.dates.drange(start,stop,delta)

fig = plt.figure()
plt.title("ROOF")
plt.plot(dates, TROOF1_ref_ce_ts, color='black', label=u"REF")
#plt.plot(TROOF1_opt_ce_ts, color='green', label=u"OPT")
plt.plot(TROOF1_alb_ce_ts, color='violet', label=u"ALB")#, linestyle=":")
plt.plot(TROOF1_iso_ce_ts, color='red', label=u"INS")#, linestyle=":")
plt.plot(TROOF1_grr_ce_ts, color='darkgreen', label=u"GRR")#, linestyle=":")
plt.plot(TROOF1_pvr_ce_ts, color='blue', label=u"PVR")#, linestyle=":")
plt.xlabel("hours[UTC]")
plt.ylabel(u"surface temperature [°C]", size="large")
plt.legend(loc='lower right', ncol=3)
plt.ylim(0, 100)
#plt.ylim(-5, 10)

date_format = mpl.dates.DateFormatter('%d %B %Y')
ax = gca()

days = DayLocator(range(2, 9), interval=1)
ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(date_format)

plt.xticks(rotation='vertical', fontsize='small')
plt.subplots_adjust(bottom=.3)

plt.show()

fig = plt.figure()
plt.title("WALL")
plt.plot(TWALL1_ref_ce_ts, color='black', label=u"REF")
#plt.plot(TWALL1_opt_ce_ts, color='green', label=u"OPT")
plt.plot(TWALL1_alb_ce_ts, color='violet', label=u"ALB")#, linestyle=":")
plt.plot(TWALL1_iso_ce_ts, color='red', label=u"INS")#, linestyle=":")
#plt.plot(TWALL1_grr_ce_ts, color='darkgreen', label=u"GRR", linestyle=":")
#plt.plot(TWALL1_pvr_ce_ts, color='blue', label=u"PVR", linestyle=":")
plt.xlabel("hours[UTC]")
plt.ylabel(u"surface temperature [°C]", size="large")
plt.legend(loc='lower right', ncol=3)
plt.ylim(0, 100)
#plt.ylim(-5, 10)
plt.show()

fig = plt.figure()
plt.title("ROAD")
plt.plot(TGROUND_ref_ce_ts, color='black', label=u"REF")
#plt.plot(TGROUND_opt_ce_ts, color='green', label=u"OPT")
plt.plot(TGROUND_alb_ce_ts, color='violet', label=u"ALB")#, linestyle=":")
plt.plot(TGROUND_iso_ce_ts, color='red', label=u"INS")#, linestyle=":")
#plt.plot(TWALL1_grr_ce_ts, color='darkgreen', label=u"GRR", linestyle=":")
#plt.plot(TWALL1_pvr_ce_ts, color='blue', label=u"PVR", linestyle=":")
plt.xlabel("hours[UTC]")
plt.ylabel(u"surface temperature [°C]", size="large")
plt.legend(loc='lower right', ncol=3)
plt.ylim(0, 100)
#plt.ylim(-5, 10)
plt.show()

