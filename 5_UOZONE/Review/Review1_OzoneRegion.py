# -*- coding: utf-8 -*-
__author__ = 'lnx'

import numpy as np
import pandas as pd
from datetime import datetime
from loess.loess_1d import loess_1d
import monthdelta
import netCDF4
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVindobona_Filter_fullperiod

#TODO include colorbar
#TODO include MAM20!

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
o3_2020_mda8 = o3_2020_mda1.resample('8H', label='right').mean()
o3_2020_mda8 = o3_2020_mda8.resample('D').mean()
o3_1990_2020_mda8 = pd.concat([o3_1990_2019_mda8, o3_2020_mda8], axis=0)
o3_1990_2020_mda8 = o3_1990_2020_mda8#*ugm3toppb_o3 #MUG->PPB
o3_1990_2020_da = o3_1990_2020_mda8.resample('D').mean()
o3_1990_2020_m = o3_1990_2020_mda8.resample('M').mean()
o3_1990_2020_mda1_w = o3_1990_2020_mda1.resample('W').mean()
o3_1990_2020_mda8_w = o3_1990_2020_mda8.resample('W').mean()

'''TIMESLICES'''
MAM18_s = datetime(2018, 3, 1, 00, 00)
MAM18_e = datetime(2018, 5, 31, 00, 00)
MAM20_s = datetime(2020, 3, 1, 00, 00)
MAM20_e = datetime(2020, 5, 31, 00, 00)

#o3 = o3_1990_2020_mda8_w[MAM18_s:MAM18_e]
#wd = BOKUMetData_dailysum["WD"].resample("W").mean()
o3 = o3_1990_2020_mda8[MAM18_s:MAM18_e]
wd = BOKUMetData_dailysum["WD"]
wd = wd[MAM18_s:MAM18_e]
wd = wd[:-1]
print(len(wd), len(o3))

fs = 10  #fontsize
fig, axs = plt.subplots(2,2)
axs[0, 0].scatter(o3['AT9STEF'], o3['AT30801'], c=wd, label="O3_nw", cmap='viridis') #Irnfritz
#axs[0, 0].set_title('Axis [0, 0]')
axs[0, 1].scatter(o3['AT9STEF'], o3['AT31301'], c=wd, label="O3_ne")  #Mistelbach
#axs[0, 1].set_title('Axis [0, 1]')
axs[1, 0].scatter(o3['AT9STEF'], o3['AT30603'], c=wd, label="O3_se") #Himberg
#axs[1, 0].set_title('Axis [0, 1]')
axs[1, 1].scatter(o3['AT9STEF'], o3['AT32101'], c=wd, label="O3_s") #Wiesmath
#axs[1, 1].set_title('Axis [0, 1]')
#ax1.scatter(o3['AT9STEF'], o3['AT30801'], marker=">", label="O3_nw") #Irnfritz c=wd,
#ax1.scatter(o3['AT9STEF'], o3['AT31301'], marker="<", label="O3_ne") #Mistelbach
#ax1.scatter(o3['AT9STEF'], o3['AT30603'], marker="o", label="O3_se") #Himberg
#ax1.scatter(o3['AT9STEF'], o3['AT32101'], marker="^", label="O3_s") #Wiesmath
#ax1.set_ylabel("O3_vienna_center [μg/m³]", size="medium")
#ax1.set_ylabel("O3_region [μg/m³]", size="medium")
#legend2 = ax1.legend(*scatter.legend_elements(**kw),
#                    loc="lower right", title="Price")
#axs[0,0].legend(loc='upper left')
# colorscale
#cb = fig.colorbar(hexbins, ax=ax)
#cb.set_label('Color Scale')
plt.colorbar(o3['AT9STEF'], o3['AT30801'], ax=axs[0,0])
#plt.colorbar(im, ax=ax[i, j])

plt.show()