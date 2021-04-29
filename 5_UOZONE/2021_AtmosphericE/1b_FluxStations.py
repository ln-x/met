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
from met.library.conversions import molhkm2mghm2

#Vielsalm indices: [south_north: 89, west_east: 27]
#reading in WRF-CHEM: 9km!
path = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era-interim/HCera_9km_2007-16_ATTR/'
path1 = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era-interim/HCera_9km_2007-16_ATTR/model_base_results/'
#f_xtime = Dataset(path + 'XTIME.nc', mode='r')
#f_eiso1 = Dataset(path + 'part19/wrfout_d01_2009-06-19_01_EISO.nc', mode='r')
#f_eiso2 = Dataset(path + 'part20/wrfout_d01_2009-08-08_01_EISO.nc', mode='r')
#f_eiso3 = Dataset(path + 'part21/wrfout_d01_2009-09-27_01_EISO.nc', mode='r')
#all = Dataset(path + 'part19/wrfout_d01_2009-06-19_01_EISO.nc',path + 'part20/wrfout_d01_2009-08-08_01_EISO.nc')
#EBIO_ISO1 = f_eiso1.variables['EBIO_ISO']
#EBIO_ISO2 = f_eiso2.variables['EBIO_ISO']
#EBIO_ISO3 = f_eiso3.variables['EBIO_ISO']
f_eiso = Dataset(path1 + 'HC2007t16-W-E-Cam-TNO3ATTR_EBISO.nc', mode='r')
EBIO_ISO_hp = f_eiso.variables['EBISO'][:,11,16]

starttime = datetime(2007, 1, 1, 1, 00)
wrfc_time_construct = np.array([starttime + timedelta(hours=i) for i in range(87673)])

ebioiso = pd.Series(EBIO_ISO_hp[:],index=wrfc_time_construct)
ebioiso_hp_d =ebioiso.resample('D').mean()
ebioiso_hp_dmax =ebioiso.resample('D').max()
ebioiso_hp_mmax =ebioiso_hp_dmax.resample('M').mean()

f_iso = Dataset(path + 'wrfout_d01_2012-05-04_01_iso.nc', mode='r')
ISO_hp = f_iso.variables['iso'][:,0,11,16]
starttime = datetime(2012, 5, 4, 1, 00)
wrfc_time_construct2012 = np.array([starttime + timedelta(hours=i) for i in range(1200)])
iso = pd.Series(ISO_hp[:],index=wrfc_time_construct2012)
iso_hp_d =iso.resample('D').mean()
iso_hp_dmax =iso.resample('D').max()
iso_hp_mmax =iso_hp_dmax.resample('M').mean()

"""
EBIO_ISO_vs = f_eiso.variables['EBISO'][:,89,27]
ebioiso = pd.Series(EBIO_ISO_vs[:],index=wrfc_time_construct)
ebioiso_vs_d =ebioiso.resample('D').mean()
ebioiso_vs_dmax =ebioiso.resample('D').max()
ebioiso_vs_mmax =ebioiso_vs_dmax.resample('M').mean()

EBIO_ISO_bf = f_eiso.variables['EBISO'][:,23,62]
ebioiso = pd.Series(EBIO_ISO_bf[:],index=wrfc_time_construct)
ebioiso_bf_d =ebioiso.resample('D').mean()
ebioiso_bf_dmax =ebioiso.resample('D').max()
ebioiso_bf_mmax =ebioiso_bf_dmax.resample('M').mean()
"""
print("pass")

file = "/windata/Google Drive/DATA/obs_point/chem/FluxStations/O3HP/OHP_2012_2014_isoprene.xlsx"
hp = pd.read_excel(file, sheet_name="2012_FLux_10m", usecols="A,B", skiprows=4)#, converters={'A': pd.to_datetime})
hp.columns = ['datetime', 'isoprene flux [mg m-2 h-1]'] #TODO: local time?
hp = hp.set_index(pd.to_datetime(hp['datetime']))
hp = hp.drop(columns=['datetime'])
hp_iso_h =hp.resample('H').mean()
hp_iso_dmax =hp_iso_h.resample('D').max()
hp_iso_d =hp_iso_h.resample('D').mean()

print("pass")

hp_10m_ppb = pd.read_excel(file, sheet_name="2012_ISOP_10m", usecols="A,B", skiprows=2)#, converters={'A': pd.to_datetime})
hp_10m_ppb.columns = ['datetime', 'isoprene mixing ratio [ppb]']  #m/z 69  #TODO: local time!
hp_10m_ppb = hp_10m_ppb.set_index(pd.to_datetime(hp_10m_ppb['datetime']))
hp_10m_ppb = hp_10m_ppb.drop(columns=['datetime'])
hp_10m_ppb_h =hp_10m_ppb.resample('H').mean()
hp_10m_ppb_dmax = hp_10m_ppb_h.resample('D').max()
hp_10m_ppb_d = hp_10m_ppb_h.resample('D').mean()

print("pass")

hp_2m_ppb = pd.read_excel(file, sheet_name="2012_ISOP_2M", usecols="A,B", skiprows=1)#, converters={'A': pd.to_datetime})
hp_2m_ppb.columns = ['datetime', 'isoprene mixing ratio [ppb]']  #TODO: local time!
hp_2m_ppb = hp_2m_ppb.set_index(pd.to_datetime(hp_2m_ppb['datetime']))
hp_2m_ppb = hp_2m_ppb.drop(columns=['datetime'])
hp_2m_ppb_h =hp_2m_ppb.resample('H').mean()
hp_2m_ppb_dmax = hp_2m_ppb_h.resample('D').max()
hp_2m_ppb_d = hp_2m_ppb_h.resample('D').mean()

#start = datetime(2009, 7, 1, 1, 00)
#end = datetime(2012, 12, 31, 1, 00)

start = datetime(2012, 5, 20, 1, 00)
end = datetime(2012, 6, 20, 1, 00)

print("pass")

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1 = plt.gca()
ax1.plot((hp_iso_h[start:end]), color='black', linewidth="0.1",label="OBS h")
#ax1.plot((hp_iso_d[start:end]), color='black', linewidth="0.5",label="OBS d")
ax1.plot((hp_iso_dmax[start:end]), color='black',linewidth="0.5", linestyle=":", label="OBS dmax")

ax1.plot((ebioiso[start:end])*molhkm2mghm2, color='red', linewidth="0.1", label="wrfc h") #[mol h-1 km-2] 9 km
#ax1.plot((ebioiso_hp_d[start:end])*molhkm2mghm2, color='red', linewidth="0.5", label="wrfc d") #[mol h-1 km-2] 9 km
ax1.plot((ebioiso_hp_dmax[start:end])*molhkm2mghm2, color='red',linewidth="0.5", linestyle=":", label="wrfc dmax") #[mol h-1 km-2] 9 km
#ax1.plot((ebioiso_hp_mmax[start:end])*molhkm2mghm2, color='green', label="wrfc mmax") #[mol h-1 km-2] 9 km
ax1.set_xlabel("days")
ax1.set_ylabel("isoprene emissions [mg m-2 h-1]", size="medium")
ax1.legend(loc='upper left')
#ax1.set_ylim(0, 11)
#ax2.set_ylim(10, 50)
plt.suptitle(f"MOD/OBS @HP {start} - {end}")

ax1 = fig.add_subplot(212)
ax1 = plt.gca()
ax1.plot((hp_10m_ppb_h[start:end]), color='black', linewidth="0.1",label="OBS 10m h")
#ax1.plot((hp_10m_ppb_d[start:end]), color='black', linewidth="0.5",label="OBS 10m d")
ax1.plot((hp_10m_ppb_dmax[start:end]), color='black',linewidth="0.5", linestyle=":", label="OBS 10 m dmax")
ax1.plot((hp_2m_ppb_h[start:end]), color='green', linewidth="0.1",label="OBS 2m h")
#ax1.plot((hp_2m_ppb_d[start:end]), color='green', linewidth="0.5",label="OBS 2m d")
ax1.plot((hp_2m_ppb_dmax[start:end]), color='green',linewidth="0.5", linestyle=":", label="OBS 2m dmax")

ax1.plot((iso[start:end])*1000, color='red', linewidth="0.1",label="wrfc h") #[ppmv] 9 km
#ax1.plot((iso_hp_d[start:end]*1000), color='red', linewidth="0.5",label="wrfc d") #[ppmv] 9 km
ax1.plot((iso_hp_dmax[start:end]*1000), color='red',linewidth="0.5", linestyle=":", label="wrfc dmax") #[ppmv] 9 km

ax1.set_xlabel("days")
ax1.set_ylabel("isoprene mixing ratios [ppb]", size="medium")
ax1.legend(loc='upper left')

plt.show()

exit()


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1 = plt.gca()
#ax1.plot((ebioiso_vs_d[start:end])*molhkm2mghm2, color='blue', linestyle=":", label="wrfchem_iso_da @Vielsalm") #[mol h-1 km-2] 9 km
ax1.plot((ebioiso_vs_dmax[start:end])*molhkm2mghm2, color='blue', linewidth="0.1", label="wrfchem_iso_dmax @Vielsalm") #[mol h-1 km-2] 9 km
ax1.plot((ebioiso_vs_mmax[start:end])*molhkm2mghm2, color='blue', label="wrfchem_iso_mmax @Vielsalm") #[mol h-1 km-2] 9 km
#ax1.plot((ebioiso_hp_d[start:end])*molhkm2mghm2, color='green', linestyle=":", label="wrfchem_iso_da @HauteProvence") #[mol h-1 km-2] 9 km
ax1.plot((ebioiso_hp_dmax[start:end])*molhkm2mghm2, color='green',linewidth="0.1", label="wrfchem_iso_dmax @HauteProvence") #[mol h-1 km-2] 9 km
ax1.plot((ebioiso_hp_mmax[start:end])*molhkm2mghm2, color='green', label="wrfchem_iso_mmax @HauteProvence") #[mol h-1 km-2] 9 km
#ax1.plot((ebioiso_bf_d[start:end])*molhkm2mghm2, color='orange', linestyle=":", label="wrfchem_iso_da @BoscoFontana") #[mol h-1 km-2] 9 km
ax1.plot((ebioiso_bf_dmax[start:end])*molhkm2mghm2, color='orange',linewidth="0.1", label="wrfchem_iso_dmax @BoscoFontana") #[mol h-1 km-2] 9 km
ax1.plot((ebioiso_bf_mmax[start:end])*molhkm2mghm2, color='orange', label="wrfchem_iso_mmax @BoscoFontana") #[mol h-1 km-2] 9 km
plt.axhspan(2.1, 10, color='green', alpha=0.1)
plt.axhline(0.5, color='green')
plt.axhline(0.9, color='green')
plt.axhspan(0, 4, color='blue', alpha=0.1)
plt.axhline(0.6, color='blue')
plt.axhline(0.25, color='blue')
#ax2.plot((BOKUMetAT_hourly.values[116:315]), color='black', linestyle="dotted", linewidth="0.5", label="obs_T2")
ax1.set_xlabel("days")
ax1.set_ylabel("mg m-2 h-1", size="medium")
#ax2.set_ylabel("degC", size="medium")
ax1.legend(loc='upper center')
#ax2.legend(loc='upper right')
ax1.set_ylim(0, 11)
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
