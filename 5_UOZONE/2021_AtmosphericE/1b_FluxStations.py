# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.dates
import matplotlib.pyplot as plt
from scipy import stats
import sys
import met.library.BOKUMet_Data
from datetime import datetime, timedelta

#Vielsalm indices: [south_north: 89, west_east: 27]
#reading in WRF-CHEM: 9km!
path = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era-interim/HCera_9km_2007-16_ATTR/'
path1 = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era-interim/HCera_9km_2007-16_ATTR/model_base_results/'
#f_xtime = Dataset(path + 'XTIME.nc', mode='r')
f_eiso1 = Dataset(path + 'part19/wrfout_d01_2009-06-19_01_EISO.nc', mode='r')
f_eiso2 = Dataset(path + 'part20/wrfout_d01_2009-08-08_01_EISO.nc', mode='r')
f_eiso3 = Dataset(path + 'part21/wrfout_d01_2009-09-27_01_EISO.nc', mode='r')
#all = Dataset(path + 'part19/wrfout_d01_2009-06-19_01_EISO.nc',path + 'part20/wrfout_d01_2009-08-08_01_EISO.nc')
EBIO_ISO1 = f_eiso1.variables['EBIO_ISO']
EBIO_ISO2 = f_eiso2.variables['EBIO_ISO']
EBIO_ISO3 = f_eiso3.variables['EBIO_ISO']

f_eiso = Dataset(path1 + 'HC2007t16-W-E-Cam-TNO3ATTR_EBISO.nc', mode='r')
EBIO_ISO_vs = f_eiso.variables['EBISO'][:,89,27]
EBIO_ISO_hp = f_eiso.variables['EBISO'][:,11,16]
EBIO_ISO_bf = f_eiso.variables['EBISO'][:,23,62]
#print(len(EBIO_ISO))
starttime = datetime(2007, 1, 1, 1, 00)
wrfc_time_construct = np.array([starttime + timedelta(hours=i) for i in range(87673)])
ebioiso = pd.Series(EBIO_ISO_vs[:],index=wrfc_time_construct) #wrfc_o3_d =wrfc_o3.resample('D').mean() #TODO Only valid with DatetimeIndex, TimedeltaIndex or PeriodINdex, but got instance of 'Index'
ebioiso_vs_d =ebioiso.resample('D').mean()
ebioiso_vs_dmax =ebioiso.resample('D').max()

ebioiso = pd.Series(EBIO_ISO_hp[:],index=wrfc_time_construct) #wrfc_o3_d =wrfc_o3.resample('D').mean() #TODO Only valid with DatetimeIndex, TimedeltaIndex or PeriodINdex, but got instance of 'Index'
ebioiso_hp_d =ebioiso.resample('D').mean()
ebioiso_hp_dmax =ebioiso.resample('D').max()

ebioiso = pd.Series(EBIO_ISO_bf[:],index=wrfc_time_construct) #wrfc_o3_d =wrfc_o3.resample('D').mean() #TODO Only valid with DatetimeIndex, TimedeltaIndex or PeriodINdex, but got instance of 'Index'
ebioiso_bf_d =ebioiso.resample('D').mean()
ebioiso_bf_dmax =ebioiso.resample('D').max()

molhkm2mghm2 = 1/1000000*68.11622*1000  #mol h-1 km-2 > mg h-1 m-2

start = datetime(2009, 7, 1, 1, 00)
end = datetime(2012, 12, 31, 1, 00)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1 = plt.gca()
ax1.plot((ebioiso_vs_d[start:end])*molhkm2mghm2, color='blue', linestyle=":", label="wrfchem_iso_da @Vielsalm") #[mol h-1 km-2] 9 km
ax1.plot((ebioiso_vs_dmax[start:end])*molhkm2mghm2, color='blue', label="wrfchem_iso_dmax @Vielsalm") #[mol h-1 km-2] 9 km
ax1.plot((ebioiso_hp_d[start:end])*molhkm2mghm2, color='green', linestyle=":", label="wrfchem_iso_da @HauteProvence") #[mol h-1 km-2] 9 km
ax1.plot((ebioiso_hp_dmax[start:end])*molhkm2mghm2, color='green', label="wrfchem_iso_dmax @HauteProvence") #[mol h-1 km-2] 9 km
ax1.plot((ebioiso_bf_d[start:end])*molhkm2mghm2, color='orange', linestyle=":", label="wrfchem_iso_da @BoscoFontana") #[mol h-1 km-2] 9 km
ax1.plot((ebioiso_bf_dmax[start:end])*molhkm2mghm2, color='orange', label="wrfchem_iso_dmax @BoscoFontana") #[mol h-1 km-2] 9 km
#ax2.plot((BOKUMetAT_hourly.values[116:315]), color='black', linestyle="dotted", linewidth="0.5", label="obs_T2")
ax1.set_xlabel("days")
ax1.set_ylabel("mg m-2 h-1", size="medium")
#ax2.set_ylabel("degC", size="medium")
ax1.legend(loc='upper center')
#ax2.legend(loc='upper right')
ax1.set_ylim(0, 5)
#ax2.set_ylim(10, 50)
plt.suptitle(f"WRFChem@Vielsalm {start} - {end}")

plt.show()


exit()

fig = plt.figure()
#fig.set_size_inches(3.39,2.54)
ax1 = fig.add_subplot(311)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot((EBIO_ISO1[:,89,27])*molhkm2mghm2, color='violet', label="wrfchem_iso_6_19...") #[mol h-1 km-2] 9 km
#ax2.plot((BOKUMetAT_hourly.values[116:315]), color='black', linestyle="dotted", linewidth="0.5", label="obs_T2")
ax1.set_xlabel("days")
ax1.set_ylabel("mg m-2 h-1", size="medium")
#ax2.set_ylabel("degC", size="medium")
ax1.legend(loc='upper center')
#ax2.legend(loc='upper right')
ax1.set_ylim(0, 5)
#ax2.set_ylim(10, 50)
plt.suptitle("2009 WRFChem@Vielsalm")

ax1 = fig.add_subplot(312)
ax1 = plt.gca()
#ax2 = ax1.twinx()
ax1.plot((EBIO_ISO2[:,89,27])*molhkm2mghm2, color='violet', label="wrfchem_iso_8_8...") #[mol h-1 km-2] 9 km
#ax2.plot((BOKUMetAT_hourly.values[116:315]), color='black', linestyle="dotted", linewidth="0.5", label="obs_T2")
ax1.set_xlabel("days")
ax1.set_ylabel("mg m-2 h-1", size="medium")
#ax2.set_ylabel("degC", size="medium")
ax1.legend(loc='upper center')
#ax2.legend(loc='upper right')
ax1.set_ylim(0, 5)
#ax2.set_ylim(10, 50)

ax1 = fig.add_subplot(313)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot((EBIO_ISO3[:,89,27])*molhkm2mghm2, color='violet', label="wrfchem_iso_9_27...") #[mol h-1 km-2] 9 km
#ax2.plot((BOKUMetAT_hourly.values[116:315]), color='black', linestyle="dotted", linewidth="0.5", label="obs_T2")
ax1.set_xlabel("days")
ax1.set_ylabel("mg m-2 h-1", size="medium")
#ax2.set_ylabel("degC", size="medium")
ax1.legend(loc='upper center')
#ax2.legend(loc='upper right')
ax1.set_ylim(0, 5)
#ax2.set_ylim(10, 50)



plt.show()
