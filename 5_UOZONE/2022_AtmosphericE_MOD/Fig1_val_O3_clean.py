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
wrf_LOB_i = 59 #16.5269 48.1625
wrf_LOB_j = 66
wrf_HER_i = 63 #16.2983 48.2708
wrf_HER_j = 60

path = '/windata/DATA/models/boku/EMEP/output/UOZONE/'
fh_o3 = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ug_O3_uozone_new2.nc", mode='r') #TODO: update join all files
emep_time_o3 = fh_o3.variables['time']
jd_o3 = netCDF4.num2date(emep_time_o3[:],emep_time_o3.units, only_use_cftime_datetimes=False)

emep_o3_d_STE = fh_o3.variables['SURF_ug_O3'][:, wrf_STE_i,wrf_STE_j] #(time, j, i)
emep_o3_d_STE = pd.Series(emep_o3_d_STE[:],index=jd_o3)
emep_o3_d_STE_w = emep_o3_d_STE.resample('W').mean()
emep_o3_d_LOB = fh_o3.variables['SURF_ug_O3'][:, wrf_LOB_i,wrf_LOB_j] #(time, j, i)
emep_o3_d_LOB = pd.Series(emep_o3_d_LOB[:],index=jd_o3)
emep_o3_d_LOB_w = emep_o3_d_LOB.resample('W').mean()
emep_o3_d_HER = fh_o3.variables['SURF_ug_O3'][:, wrf_HER_i,wrf_HER_j] #(time, j, i)
emep_o3_d_HER = pd.Series(emep_o3_d_HER[:],index=jd_o3)
emep_o3_d_HER_w = emep_o3_d_HER.resample('W').mean()
emep_o3_d_area = fh_o3.variables['SURF_ug_O3'][:,:,:]
emep_o3_d_area = emep_o3_d_area.mean(axis=(1, 2))
emep_o3_d_area = pd.Series(emep_o3_d_area[:],index=jd_o3)
emep_o3_d_area_w = emep_o3_d_area.resample('W').mean()

'''READ IN EEA air pollution data'''
pathbase2 = "/windata/DATA/obs_point/chem/EEA/"
o3_1990_2019_mda1 = pd.read_csv(pathbase2 + "o3_mda1_1990-2019_AT_mug.csv")
o3_1990_2019_mda1 = o3_1990_2019_mda1.set_index((pd.to_datetime(o3_1990_2019_mda1['date'])))
o3_1990_2019_mda1 = o3_1990_2019_mda1.drop(columns=['date'])
o3_1990_2019_mda8 = pd.read_csv(pathbase2 + "o3_mda8_1990-2019_AT_mug.csv")
o3_1990_2019_mda8 = o3_1990_2019_mda8.set_index(pd.to_datetime(o3_1990_2019_mda8['date']))
o3_1990_2019_mda8 = o3_1990_2019_mda8.drop(columns=['date'])
o3_2020_mda1 = pd.read_csv(pathbase2 + "AT_O3_2020.csv")
o3_2020_mda1 = o3_2020_mda1.set_index(pd.to_datetime(o3_2020_mda1['date']))
o3_2020_mda1 = o3_2020_mda1.drop(columns=['date'])
o3_1990_2020_mda1 = pd.concat([o3_1990_2019_mda1, o3_2020_mda1], axis=0)
#o3_1990_2020_mda1 = o3_1990_2020_mda1[datetime(2018,1,1):datetime(2020,12,31)] #TODO: Attention! Timeserie is filtered#

o3_2020_mda8 = o3_2020_mda1.resample('8H', label='right').mean()
o3_2020_mda8 = o3_2020_mda8.resample('D').mean()
o3_1990_2020_mda8 = pd.concat([o3_1990_2019_mda8, o3_2020_mda8], axis=0)
o3_1990_2020_mda8 = o3_1990_2020_mda8
o3_1990_2020_da = o3_1990_2020_mda8.resample('D').mean()
o3_1990_2020_m = o3_1990_2020_mda8.resample('M').mean()
o3_1990_2020_mda1_w = o3_1990_2020_mda1.resample('W').mean()
o3_1990_2020_mda8_w = o3_1990_2020_mda8.resample('W').mean()
#o3_1990_2020_mda1_w.plot()
#plt.show()
#exit()

'''
Plotting
'''
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, (1, 1))
plt.suptitle("1 validation")
ax1.plot(o3_1990_2020_mda1_w['AT9JAEG'],linewidth="1", color='darkgreen', label="JAEG", linestyle="-") #TODO mda1 vs da (mda8)
ax1.plot(o3_1990_2020_mda1_w['AT9STEF'],linewidth="1", color='violet', label="STEF", linestyle="-") #mda1 vs da (mda8)
ax1.plot(o3_1990_2020_mda1_w['AT90LOB'],linewidth="1", color='chartreuse', label="LOB", linestyle="-") #mda1 vs da (mda8)
ax1.plot(emep_o3_d_HER_w,color='darkgreen', linestyle=":")
ax1.plot(emep_o3_d_STE_w,color='violet', linestyle=":")
ax1.plot(emep_o3_d_LOB_w,color='chartreuse', linestyle=":")
ax1.plot(emep_o3_d_area_w,color="grey",linestyle=":", linewidth="5", label="area mean")
ax1.legend(loc='upper right')
#ax1.set_ylim(0, 150)
ax1.set_ylabel("[ug/m2]", size="medium")
plt.show()

exit()
data = pd.concat([o3_1990_2019_mda1['AT9JAEG'].resample("D").mean(), o3_1990_2019_mda1['AT9STEF'].resample("D").mean(),
                  o3_1990_2019_mda1['AT90LOB'].resample("D").mean(), emep_o3_d_HER.resample("D").mean(), emep_o3_d_STE.resample("D").mean(),
                  emep_o3_d_LOB.resample("D").mean()], axis=1)
data.columns = ['obs_her', 'obs_ste', 'obs_lob', 'mod_her', 'mod_ste', 'mod_lob']
data = data.dropna()
print(data)

SRho_her, Sp_her = stats.spearmanr(data['obs_her'], data['mod_her'])
SRho_ste, Sp_ste = stats.spearmanr(data['obs_ste'], data['mod_ste'])
SRho_lob, Sp_lob = stats.spearmanr(data['obs_her'], data['mod_lob'])

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.set_title('(a) JAE: \n R={:.2f} \n p={:.2f}'.format(SRho_her, Sp_her), fontsize='small')
ax2.set_title('(b) STE: \n R={:.2f} \n p={:.2f}'.format(SRho_ste, Sp_ste), fontsize='small')
ax3.set_title('(c) LOB: \n R={:.2f} \n p={:.2f}'.format(SRho_lob, Sp_lob), fontsize='small')
ax1.scatter(data['obs_her'], data['mod_her'],label="JAEG", s=1)
ax2.scatter(data['obs_ste'], data['mod_ste'],label="STEF", s=1)
ax3.scatter(data['obs_lob'], data['mod_lob'],label="LOB", s=1)
ax1.plot(range(180),range(180),linewidth=0.5)
ax2.plot(range(180),range(180),linewidth=0.5)
ax3.plot(range(180),range(180),linewidth=0.5)
ax1.set_ylim(0,180)
ax2.set_ylim(0,180)
ax3.set_ylim(0,180)
ax1.set_xlim(0,180)
ax2.set_xlim(0,180)
ax3.set_xlim(0,180)
ax1.set_ylabel("[ug/m³]", size="medium")
plt.show()


