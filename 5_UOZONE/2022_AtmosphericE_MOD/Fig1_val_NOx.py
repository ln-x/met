# -*- coding: utf-8 -*-
__author__ = 'lnx'

import numpy as np
import pandas as pd
from datetime import datetime
from scipy import stats
import cftime
import nc_time_axis
import monthdelta
import matplotlib.pyplot as plt
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVindobona_Filter_fullperiod
from met.library import ReadinCAMX_2
from met.library import ReadinPROBAV_LAI_300m
from netCDF4 import Dataset
import netCDF4

'''READ IN EMEP data'''
#see manual check in script FinNearest_EMEP_gridpoints.py
wrf_STE_i = 60 #16.3742 48.2086
wrf_STE_j = 62
wrf_LOB_i = 59 #16.5269 48.1625O
wrf_LOB_j = 66
wrf_HER_i = 63 #16.2983 48.2708
wrf_HER_j = 60

path = '/windata/DATA/models/boku/EMEP/output/UOZONE/'
fh_month = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/uozone_month_20180206_20201231.nc", mode='r')
emep_time_month = fh_month.variables['time']
jd_month = netCDF4.num2date(emep_time_month[:],emep_time_month.units, only_use_cftime_datetimes=False)

emep_no2_m_STE = fh_month.variables['SURF_ug_NO2'][:, wrf_STE_i,wrf_STE_j] #(time, j, i)
emep_no2_m_STE = pd.Series(emep_no2_m_STE[:],index=jd_month)
#emep_no2_d_STE_w = emep_no2_d_STE.resample('W').mean()
emep_no_m_STE = fh_month.variables['SURF_ug_NO'][:, wrf_STE_i,wrf_STE_j] #(time, j, i)
emep_no_m_STE = pd.Series(emep_no_m_STE[:],index=jd_month)
emep_nox_m_STE = emep_no_m_STE+emep_no2_m_STE
#emep_no_d_STE_w = emep_no_d_STE.resample('W').mean()

"""
emep_hcho_d_LOB = fh_hcho.variables['SURF_ppb_HCHO'][:, wrf_LOB_i,wrf_LOB_j] #(time, j, i)
emep_hcho_d_LOB = pd.Series(emep_hcho_d_LOB[:],index=jd_hcho)
emep_hcho_d_LOB_w = emep_hcho_d_LOB.resample('W').mean()
emep_hcho_d_HER = fh_hcho.variables['SURF_ppb_HCHO'][:, wrf_HER_i,wrf_HER_j] #(time, j, i)
emep_hcho_d_HER = pd.Series(emep_hcho_d_HER[:],index=jd_hcho)
emep_hcho_d_HER_w = emep_hcho_d_HER.resample('W').mean()
emep_hcho_d_area = fh_hcho.variables['SURF_ppb_HCHO'][:,:,:]
emep_hcho_d_area = emep_hcho_d_area.mean(axis=(1, 2))
emep_hcho_d_area = pd.Series(emep_hcho_d_area[:],index=jd_hcho)
emep_hcho_d_area_w = emep_hcho_d_area.resample('W').mean()
"""

'''READ IN EEA air pollution data'''
pathbase2 = "/windata/DATA/obs_point/chem/EEA/"
nox_1990_2019_da = pd.read_csv(pathbase2 + "nox_da_1990-2019_AT_ppb.csv")
nox_1990_2019_da = nox_1990_2019_da.set_index(pd.to_datetime(nox_1990_2019_da['date']))
nox_1990_2019_da = nox_1990_2019_da.drop(columns=['date'])
no2_2020_mda1 = pd.read_csv(pathbase2 + "AT_NO2_2020.csv")
no2_2020_mda1 = no2_2020_mda1.set_index(pd.to_datetime(no2_2020_mda1['date']))
no2_2020_da = no2_2020_mda1.resample('D').mean()
no_2020_mda1 = pd.read_csv(pathbase2 + "AT_NO_2020.csv")
no_2020_mda1 = no_2020_mda1.set_index(pd.to_datetime(no_2020_mda1['date']))
no_2020_da = no_2020_mda1.resample('D').mean()
nox_2020_da = no_2020_da.add(no2_2020_da)
nox_1990_2020_da = pd.concat([nox_1990_2019_da, nox_2020_da], axis=0)
nox_1990_2020_m = nox_1990_2020_da.resample('M').mean()
#nox_1990_2020_m['AT9STEF'].plot()
#plt.show()

'''
Plotting
'''
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, (1, 1))
plt.suptitle("1 validation NOx")
#ax1.plot(hcho_dmax_w,linewidth="1", color='darkgreen', label="MAXDOAS dmax", linestyle="-")
ax1.plot(nox_1990_2020_m['AT9STEF'],linewidth="1", color='violet', label="OBS_STE", linestyle="-")
#ax1.plot(emep_hcho_d_HER_w,color='darkgreen', linestyle=":",label="EMEP_HER")
#ax1.plot(emep_no2_m_STE,color='violet', linestyle=":", label="EMEP_STE")
#ax1.plot(emep_no_m_STE,color='purple', linestyle=":", label="EMEP_STE")
ax1.plot(emep_nox_m_STE,color='violet', linestyle=":", label="EMEP_STE")
#ax1.plot(emep_hcho_d_LOB_w,color='chartreuse', linestyle=":",label="EMEP_LOB")
#ax1.plot(emep_hcho_d_area_w,color="grey",linestyle=":", linewidth="5", label="EMEP_area_mean")
ax1.legend(loc='upper right')
#ax1.set_ylim(0, 150)
ax1.set_ylabel("[ug m-3]", size="medium")
plt.show()


data = pd.concat([nox_1990_2020_m['AT9STEF'].resample("M").mean(), emep_nox_m_STE.resample("M").mean()], axis=1)
data.columns = ['obs_ste', 'mod_ste']
data = data.dropna()
print(data['obs_ste'],data['mod_ste'])

SRho, Sp = stats.spearmanr(data['obs_ste'], data['mod_ste'])
m, b = np.polyfit(data['obs_ste'], data['mod_ste'], 1)
y_est = m * data['obs_ste'] + b

fig, ax1 = plt.subplots(1, 1)
ax1.set_title('R={:.2f} \n p={:.2f}'.format(SRho, Sp), fontsize='small')
ax1.scatter(data['obs_ste'], data['mod_ste'],label="STE", s=2)
ax1.plot(data['obs_ste'], y_est, linewidth=0.1)
#ax1.plot(range(35),range(35),linewidth=0.5)
#ax1.set_ylim(0,5)
#ax1.set_xlim(0,5)
ax1.set_xlabel("OBS [ug m-3]")
ax1.set_ylabel("MOD [ug m-3]")
plt.show()


