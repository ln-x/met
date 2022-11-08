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

'''READ IN BOKU Metdata'''
BOKUMetData = met.library.BOKUMet_Data.BOKUMet()
#print(BOKUMetData) #10min values
#DAILY MEANS
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
#DAILY MAX
BOKUMetData_dailymax = BOKUMetData_hourlymean.resample('D').agg({'DT': np.max, 'AT': np.max, 'RH': np.max, 'GR': np.max, 'WS': np.max,
                                                      'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})
#JULIAN DAY
BOKUMetData_dailysum['JD'] = (BOKUMetData_dailysum.index)
f = lambda x: datestdtojd(str(x)[:-9])
BOKUMetData_dailysum['JD'] = BOKUMetData_dailysum['JD'].apply(f)

#MONTHLY MEANS
BOKUMetData_monthly = BOKUMetData.resample('M').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                      'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_weekly = BOKUMetData_dailysum.resample('W').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                      'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})


'''READ IN EMEP data'''
#see manual check in script FinNearest_EMEP_gridpoints.py
wrf_STE_i = 60 #16.3742 48.2086
wrf_STE_j = 62
wrf_LOB_i = 59 #16.5269 48.1625
wrf_LOB_j = 66
wrf_HER_i = 63 #16.2983 48.2708
wrf_HER_j = 60

path = '/windata/DATA/models/boku/EMEP/output/UOZONE'


fh_sw = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SWDNB_uozone_part_all.nc", mode='r') #TODO: update join all files
#fh_lw = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/LWDNB_uozone_part_all.nc", mode='r') #TODO: update join all files

wrf_time = fh_sw.variables['XTIME']
jd_sw = netCDF4.num2date(wrf_time[:],wrf_time.units, only_use_cftime_datetimes=False)

sw_STE = fh_sw.variables['SWDNB'][:, wrf_STE_i,wrf_STE_j] #(time, j, i)
sw_STE = pd.DataFrame(sw_STE[:],index=jd_sw)
sw_STE.columns = ['SWDNB']
sw_STE = sw_STE[sw_STE['SWDNB'] >= 500]#!= 0]
print(sw_STE)
sw_STE_d = sw_STE.resample('D').sum()
sw_STE_w = sw_STE_d.resample('W').mean()
sw_STE_w.plot()
plt.show()

#lw_STE = fh_lw.variables['LWDNB'][:, wrf_STE_i,wrf_STE_j] #(time, j, i)
#lw_STE = pd.Series(lw_STE[:],index=jd_sw)
#lw_STE_d = lw_STE.resample('D').sum()
#lw_STE_w = lw_STE_d.resample('W').mean()
#lw_STE_w.plot()
#plt.show()



#gr_STE_d = sw_STE_d + lw_STE_d
#gr_STE_w = sw_STE_w + lw_STE_w

'''
Plotting
'''
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, (1, 1))
plt.suptitle("1 validation")
ax1.plot(BOKUMetData_weekly['GR'][datetime(2018,1,1):datetime(2020,12,31)],linewidth="1", color='orange', label="OBS_BOKU", linestyle="-")
ax1.plot(sw_STE_w,color='darkgreen', linestyle=" ", marker=".", label="WRF_STE", )
#ax1.plot(BOKUMetData_dailysum['GR'],linewidth="1", color='orange', label="OBS_BOKU", linestyle="-")
ax1.legend(loc='upper right')
#ax1.set_ylim(0, 150)
ax1.set_ylabel("[kW/w]", size="medium")
plt.show()

data = pd.concat([BOKUMetData_dailysum['GR'].resample("D").mean(), sw_STE_d.resample("D").mean()], axis=1)
data.columns = ['obs_gr', 'mod_gr']
data = data.dropna()
#data = data.loc[~(data==0).all(axis=1)]
#data = data[(data.T != 0).any()]
data = data[data['mod_gr'] != 0]
data = data[datetime(2018,1,1):datetime(2020,12,31)]
print(data)

SRho_gr, Sp_gr = stats.spearmanr(data['obs_gr'], data['mod_gr'])

fig, (ax1) = plt.subplots(1, 1)
ax1.set_title('GR: \n R={:.2f} \n p={:.2f}'.format(SRho_gr, Sp_gr), fontsize='small')
ax1.scatter(data['obs_gr'], data['mod_gr'],label="GR", s=1)
#ax1.plot(range(180),range(180),linewidth=0.5)
#ax2.plot(range(180),range(180),linewidth=0.5)
#ax3.plot(range(180),range(180),linewidth=0.5)
#ax1.set_ylim(0,180)
#ax2.set_ylim(0,180)
#ax3.set_ylim(0,180)
#ax1.set_xlim(0,180)
#ax2.set_xlim(0,180)
#ax3.set_xlim(0,180)
ax1.set_ylabel("[kW/m²]", size="medium")
plt.show()


