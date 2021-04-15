# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.dates
import matplotlib.pyplot as plt
from scipy import stats
import sys
import BOKUMet_Data

#reading in WRF-CHEM: 9km!
path = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era-interim/HCera_9km_2007-16_ATTR/part63/wrfout_d01_2015-06-28_01_'
f_xtime = Dataset(path + 'XTIME.nc', mode='r')
f_xlong = Dataset(path + 'XLONG.nc', mode='r')
f_xlat = Dataset(path + 'XLAT.nc', mode='r')
f_t2 = Dataset(path + 'T2.nc', mode='r')
f_swdown = Dataset(path + 'SWDOWN.nc', mode='r')
f_smois = Dataset(path + 'SMOIS.nc', mode='r')
f_eiso = Dataset(path + 'EISO.nc', mode='r')

XTIME = f_xtime.variables['XTIME']
LON = f_xlong.variables['XLONG'][1]
LAT = f_xlat.variables['XLAT'][1]
T2 = f_t2.variables['T2']
SM = f_smois.variables['SMOIS'][:,:,:,:]  #SMOIS, SH20
EBIO_ISO = f_eiso.variables['EBIO_ISO']

#reading in SURFEX
spath = '/windata/Google Drive/DATA/models/boku/SURFEX/URBANIAfinal/'
f_surfdia = Dataset(spath + 'SURF_ATM_DIAGNOSTICS.OUT.nc')
S_T2 = f_surfdia.variables['T2M']

#reading in MEGAN 333.33f!
mpath = '/windata/Google Drive/DATA/models/boku/MEGAN/MEGANv3/NILUfinal_readinSURFEX/'
f_mg_emis = Dataset(mpath + 'MGNOUT_vie_molsm2_20s_corr.nc', mode='r')
f_mg_canmet = Dataset(mpath + 'CANMET_vie_fullLAI.nc')
mg_iso = f_mg_emis.variables['Emiss'][:,:,:,1]
mg_sunleaf = f_mg_canmet.variables['SunleafTK'][4,:,:,:]
mg_sunshade = f_mg_canmet.variables['ShadeleafTK'][:,:,:,1]

print(len(EBIO_ISO[:,113,63]))  #time = 1200
print(len(mg_iso[:,1,1]))       #time = 199

#reading in OBS from BOKUMet roof station
BOKUMetData = BOKUMet_Data.BOKUMet()
BOKUMetAT_hourly = BOKUMetData.AT.resample('H').mean()
#print(BOKUMetAT_hourly)

MEGANyindex = 34  #TODO 0-134
MEGANxindex = 37 #TODO 0-173

fig1 = plt.figure()
ax1 = plt.gca()
ax2 = ax1.twinx()
#it is i,j = 110, 59, but in script I use vals[:,j-1,i-1] - because python computes from 0.
ax1.plot(EBIO_ISO[931:1130,109,58], color='violet', label="wrfchem_iso") #[mol h-1 km-2] 9 km
#ax1.plot((mg_iso[:,MEGANyindex,MEGANxindex]*1000000*3600), color='blue', label="megan_iso") #[mol h-1?? m-2]  0.33ff m
#ax1.plot((mg_iso[:,60,60]*1000000*3600), color='blue', label="megan_iso_2") #[mol h-1 m-2]  0.33ff m
#ax2.plot((mg_sunleaf[:,MEGANyindex,MEGANxindex])-273.15, color="red", linestyle="dashed", linewidth="0.5", label="megan_sunleafT")
#ax2.plot((mg_sunleaf[:,MEGANxindex,MEGANyindex])-273.15, color="blue", linestyle="dashed", linewidth="0.5", label="megan_shadeleafT")# SAME AS SUNLEAF
ax2.plot((T2[931:1130,109,58])-273.15, color='red', linestyle="dotted", linewidth="0.5", label="wrfchem_T2")
ax2.plot((S_T2[:,MEGANyindex,MEGANxindex])-273.15, color='violet', linestyle="dotted", linewidth="0.5", label="surfex_T2")
ax2.plot((BOKUMetAT_hourly.values[116:315]), color='black', linestyle="dotted", linewidth="0.5", label="obs_T2")
ax1.set_xlabel("days")
ax1.set_ylabel("mol km-2 h-1", size="medium")
ax2.set_ylabel("degC", size="medium")
ax1.legend(loc='upper center')
ax2.legend(loc='upper right')
#ax1.set_xlim(0, 240)
ax2.set_ylim(10, 50)
plt.suptitle("HW201508 (5.8 18UTC - 13.8. 23UTC)")#, Vienna region", size="large")#+"2m air temperature"))
  #myFmt = matplotlib.dates.DateFormatter("%d")
   #ax1.xaxis.set_major_formatter(myFmt)
   #fig1.autofmt_xdate()
plt.show()
