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
fh_hcho = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ppb_HCHO_uozone_new.nc", mode='r')
emep_time_hcho = fh_hcho.variables['time']
jd_hcho = netCDF4.num2date(emep_time_hcho[:],emep_time_hcho.units, only_use_cftime_datetimes=False)

emep_hcho_d_STE = fh_hcho.variables['SURF_ppb_HCHO'][:, wrf_STE_i,wrf_STE_j] #(time, j, i)
emep_hcho_d_STE = pd.Series(emep_hcho_d_STE[:],index=jd_hcho)
emep_hcho_d_STE_w = emep_hcho_d_STE.resample('W').mean()
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

"read in VINDOBONA"
foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1))
hcho_d_w = hcho_d.resample('W').mean()
hcho_dmax_w = hcho_dmax.resample('W').mean()
#print(hcho_d.index)

'''
Plotting
'''
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, (1, 1))
plt.suptitle("1 validation HCHO")
#ax1.plot(hcho_dmax_w,linewidth="1", color='darkgreen', label="MAXDOAS dmax", linestyle="-")
ax1.plot(hcho_d_w,linewidth="1", color='violet', label="MAXDOAS", linestyle="-")
ax1.plot(emep_hcho_d_HER_w,color='darkgreen', linestyle=":",label="EMEP_HER")
ax1.plot(emep_hcho_d_STE_w,color='violet', linestyle=":", label="EMEP_STE")
ax1.plot(emep_hcho_d_LOB_w,color='chartreuse', linestyle=":",label="EMEP_LOB")
ax1.plot(emep_hcho_d_area_w,color="grey",linestyle=":", linewidth="5", label="EMEP_area_mean")
ax1.legend(loc='upper right')
#ax1.set_ylim(0, 150)
ax1.set_ylabel("[ug/m2]", size="medium")
plt.show()

data = pd.concat([hcho_dmax.resample("D").mean(), hcho_d.resample("D").mean(), emep_hcho_d_STE.resample("D").mean()], axis=1)
data.columns = ['obs_dmax', 'obs_dmean', 'mod_ste']
data = data.dropna()
print(data)

SRho_dmax, Sp_dmax = stats.spearmanr(data['obs_dmax'], data['mod_ste'])
SRho_dmean, Sp_dmean = stats.spearmanr(data['obs_dmean'], data['mod_ste'])

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_title('(a) dmax: \n R={:.2f} \n p={:.2f}'.format(SRho_dmax, Sp_dmax), fontsize='small')
ax2.set_title('(b) dmean: \n R={:.2f} \n p={:.2f}'.format(SRho_dmean, Sp_dmean), fontsize='small')
ax1.scatter(data['obs_dmax'], data['mod_ste'],label="dmax", s=1)
ax2.scatter(data['obs_dmean'], data['mod_ste'],label="dmean", s=1)
ax1.plot(range(6),range(6),linewidth=0.5)
ax2.plot(range(6),range(6),linewidth=0.5)
ax1.set_ylim(0,5)
ax2.set_ylim(0,5)
ax1.set_xlim(0,5)
ax2.set_xlim(0,5)
ax1.set_xlabel("OBS_dmax")
ax2.set_xlabel("OBS_dmean")
ax1.set_ylabel("MOD")
ax1.set_ylabel("[ppb]", size="medium")
plt.show()


