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
file_refISBA = '/media/lnx/Norskehavet/OFFLINE/2069REF/dx345corr/ISBA_PROGNOSTIC.OUT.nc'
file_refGD = '/media/lnx/Norskehavet/OFFLINE/2069REF/dx345corr/GARDEN_PROGNOSTIC.OUT.nc'

f_refISBA = Dataset(file_refISBA, mode='r')
f_refGD = Dataset(file_refGD, mode='r')

'''cut for subregions'''

WG1P7_ref_ru = f_refISBA.variables['WG1P7'][:,56:65,127:136]
WG2P7_ref_ru = f_refISBA.variables['WG2P7'][:,56:65,127:136]
WG3P7_ref_ru = f_refISBA.variables['WG3P7'][:,56:65,127:136]
WG1P8_ref_ru = f_refISBA.variables['WG1P8'][:,56:65,127:136]
GD_WG1_ref_ce = f_refGD.variables['GD_WG1'][:,50:59,80:89]
GD_WG1_ref_ce = f_refGD.variables['GD_WG1'][:,50:59,80:89]
GD_WG2_ref_ce = f_refGD.variables['GD_WG2'][:,50:59,80:89]
GD_WG3_ref_ce = f_refGD.variables['GD_WG3'][:,50:59,80:89]

f_refISBA.close()
f_refGD.close()

start = 1
end = 174

WG1P7_ref_ru = WG1P7_ref_ru.reshape(174,81)
WG1P7_ref_ru_ts = WG1P7_ref_ru.mean(axis=1)
WG2P7_ref_ru = WG2P7_ref_ru.reshape(174,81)
WG2P7_ref_ru_ts = WG2P7_ref_ru.mean(axis=1)
WG3P7_ref_ru = WG3P7_ref_ru.reshape(174,81)
WG3P7_ref_ru_ts = WG3P7_ref_ru.mean(axis=1)
WG1P8_ref_ru = WG1P8_ref_ru.reshape(174,81)
WG1P8_ref_ru_ts = WG1P8_ref_ru.mean(axis=1)
GD_WG1_ref_ce = GD_WG1_ref_ce.reshape(174,81)
GD_WG1_ref_ce_ts = GD_WG1_ref_ce.mean(axis=1)
GD_WG2_ref_ce = GD_WG2_ref_ce.reshape(174,81)
GD_WG2_ref_ce_ts = GD_WG2_ref_ce.mean(axis=1)
GD_WG3_ref_ce = GD_WG3_ref_ce.reshape(174,81)
GD_WG3_ref_ce_ts = GD_WG3_ref_ce.mean(axis=1)
"""
QCANYON_ref_ce = QCANYON_ref_ce.reshape(174,81)
QCANYON_ref_ce_ts = -(QCANYON_ref_ce.mean(axis=1))
TCANYON_ref_ce = TCANYON_ref_ce.reshape(174,81)
TCANYON_ref_ce_ts = TCANYON_ref_ce.mean(axis=1)

TRADSH_alb_ce = TRADSH_alb_ce.reshape(174,81)
TRADSH_alb_ce_ts = TRADSH_alb_ce.mean(axis=1)
U10M_alb_ce = U10M_alb_ce.reshape(174,81)
U10M_alb_ce_ts = U10M_alb_ce.mean(axis=1)
QCANYON_alb_ce = QCANYON_alb_ce.reshape(174,81)
QCANYON_alb_ce_ts = -(QCANYON_alb_ce.mean(axis=1))
TCANYONalb_ce = TCANYON_alb_ce.reshape(174,81)
TCANYONalb_ce_ts = TCANYONalb_ce.mean(axis=1)

TRADSH_iso_ce = TRADSH_iso_ce.reshape(174,81)
TRADSH_iso_ce_ts = TRADSH_iso_ce.mean(axis=1)
U10M_iso_ce = U10M_iso_ce.reshape(174,81)
U10M_iso_ce_ts = U10M_iso_ce.mean(axis=1)
QCANYON_iso_ce = QCANYON_iso_ce.reshape(174,81)
QCANYON_iso_ce_ts = -(QCANYON_iso_ce.mean(axis=1))
TCANYONiso_ce = TCANYON_iso_ce.reshape(174,81)
TCANYONiso_ce_ts = TCANYONiso_ce.mean(axis=1)

TRADSH_grr_ce = TRADSH_grr_ce.reshape(174,81)
TRADSH_grr_ce_ts = TRADSH_grr_ce.mean(axis=1)
U10M_grr_ce = U10M_grr_ce.reshape(174,81)
U10M_grr_ce_ts = U10M_grr_ce.mean(axis=1)
QCANYON_grr_ce = QCANYON_grr_ce.reshape(174,81)
QCANYON_grr_ce_ts = -(QCANYON_grr_ce.mean(axis=1))
TCANYONgrr_ce = TCANYON_grr_ce.reshape(174,81)
TCANYONgrr_ce_ts = TCANYONgrr_ce.mean(axis=1)

TRADSH_den_ce = TRADSH_den_ce.reshape(174,81)
TRADSH_den_ce_ts = TRADSH_den_ce.mean(axis=1)
U10M_den_ce = U10M_den_ce.reshape(174,81)
U10M_den_ce_ts = U10M_den_ce.mean(axis=1)
QCANYON_den_ce = QCANYON_den_ce.reshape(174,81)
QCANYON_den_ce_ts = -(QCANYON_den_ce.mean(axis=1))
TCANYONden_ce = TCANYON_den_ce.reshape(174,81)
TCANYONden_ce_ts = TCANYONden_ce.mean(axis=1)

TRADSH_pvr_ce = TRADSH_pvr_ce.reshape(174,81)
TRADSH_pvr_ce_ts = TRADSH_pvr_ce.mean(axis=1)
U10M_pvr_ce = U10M_pvr_ce.reshape(174,81)
U10M_pvr_ce_ts = U10M_pvr_ce.mean(axis=1)
QCANYON_pvr_ce = QCANYON_pvr_ce.reshape(174,81)
QCANYON_pvr_ce_ts = -(QCANYON_pvr_ce.mean(axis=1))
TCANYONpvr_ce = TCANYON_pvr_ce.reshape(174,81)
TCANYON_pvr_ce_ts = TCANYONpvr_ce.mean(axis=1)

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

#bal = TRADSH_ref_ce_ts+U10M_ref_ce_ts+QCANYON_ref_ce_ts+TCANYON_ref_ce_ts
dbal_alb = dTRADSH_alb_ce+dU10M_alb_ce+dQCANYON_alb_ce+dTCANYON_alb_ce
dbal_iso = dTRADSH_iso_ce+dU10M_iso_ce+dQCANYON_iso_ce+dTCANYON_iso_ce
dbal_grr = dTRADSH_grr_ce+dU10M_grr_ce+dQCANYON_grr_ce+dTCANYON_grr_ce
dbal_den = dTRADSH_den_ce+dU10M_den_ce+dQCANYON_den_ce+dTCANYON_den_ce
dbal_pvr = dTRADSH_pvr_ce+dU10M_pvr_ce+dQCANYON_pvr_ce+dTCANYON_pvr_ce
"""
fig = plt.figure()
plt.title("REF")
plt.plot(WG1P7_ref_ru_ts, color='green', label=u"WG1 RU")
plt.plot(WG2P7_ref_ru_ts, color='green', label=u"WG2 RU", linestyle = "--")
plt.plot(WG3P7_ref_ru_ts, color='green', label=u"WG3 RU", linestyle = ":")
#plt.plot(WG1P8_ref_ru_ts, color='darkgreen', label=u"WG1 RU [m³/m³]")
plt.plot(GD_WG1_ref_ce_ts, color='red', label=u"WG1 CE")
plt.plot(GD_WG2_ref_ce_ts, color='red', label=u"WG2 CE", linestyle = "--")
plt.plot(GD_WG3_ref_ce_ts, color='red', label=u"WG3 CE", linestyle = ":")
#plt.plot(QCANYON_ref_ce_ts, color='blue', label=u"QCANYON")
#plt.plot(TCANYON_ref_ce_ts, color='violet', label=u"TCANYON")
plt.xlabel("hours[UTC]")
plt.ylabel(r"soil water content [m³/m³]", size="large")
plt.legend(loc='lower left')
#plt.ylim(-300, 1500)
#plt.ylim(-5, 10)
plt.show()

exit()

fig2 = plt.figure()
plt.title("ALB-REF")
plt.plot(dTRADSH_alb_ce, color='red', label=u"TRADSH")
#plt.plot(dU10M_alb_ce, color='red', label=u"U10M")
#plt.plot(dQCANYON_alb_ce, color='blue', label=u"QCANYON")
plt.plot(dTCANYON_alb_ce, color='violet', label=u"TCANYON")
plt.xlabel("hours[UTC]")
plt.ylabel(r"difference in K", size="large")
plt.legend(loc='upper right')
#plt.xlim(0, 24)
plt.ylim(-5, 10)
plt.show()

fig3 = plt.figure()
plt.title("ISO-REF")
plt.plot(dTRADSH_iso_ce, color='red', label=u"TRADSH")
#plt.plot(dU10M_iso_ce, color='red', label=u"U10M")
#plt.plot(dQCANYON_iso_ce, color='blue', label=u"QCANYON")
plt.plot(dTCANYON_iso_ce, color='violet', label=u"TCANYON")
plt.xlabel("hours[UTC]")
plt.ylabel(r"difference in K", size="large")
plt.legend(loc='upper right')
#plt.xlim(0, 24)
plt.ylim(-5, 10)
plt.show()

fig4 = plt.figure()
plt.title("GRR-REF")
plt.plot(dTRADSH_grr_ce, color='red', label=u"TRADSH")
#plt.plot(dU10M_grr_ce, color='red', label=u"U10M")
#plt.plot(dQCANYON_grr_ce, color='blue', label=u"QCANYON")
plt.plot(dTCANYON_grr_ce, color='violet', label=u"TCANYON")
plt.xlabel("hours[UTC]")
plt.ylabel(r"difference in K", size="large")
plt.legend(loc='upper right')
#plt.xlim(0, 24)
plt.ylim(-5, 10)
plt.show()

fig5 = plt.figure()
plt.title("DEN-REF")
plt.plot(dTRADSH_den_ce, color='red', label=u"TRADSH")
#plt.plot(dU10M_den_ce, color='red', label=u"U10M")
#plt.plot(dQCANYON_den_ce, color='blue', label=u"QCANYON")
plt.plot(dTCANYON_den_ce, color='violet', label=u"TCANYON")
plt.xlabel("hours[UTC]")
plt.ylabel(r"difference in K", size="large")
plt.legend(loc='upper right')
#plt.xlim(0, 24)
plt.ylim(-5, 10)
plt.show()

fig6 = plt.figure()
plt.title("PVR-REF")
plt.plot(dTRADSH_pvr_ce, color='red', label=u"TRADSH")
#plt.plot(dU10M_pvr_ce, color='red', label=u"U10M")
#plt.plot(dQCANYON_pvr_ce, color='blue', label=u"QCANYON")
plt.plot(dTCANYON_pvr_ce, color='violet', label=u"TCANYON")
plt.xlabel("hours[UTC]")
plt.ylabel(r"difference in K", size="large")
plt.legend(loc='upper right')
#plt.xlim(0, 24)
plt.ylim(-5, 10)
plt.show()

exit()
