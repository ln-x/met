# -*- coding: utf-8 -*-
__author__ = 'lnx'

import numpy as np
import pandas as pd
from datetime import datetime
#from loess.loess_1d import loess_1d
import monthdelta
import netCDF4
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import BOKUMet_Data
from Datetime_recipies import datestdtojd
from conversions import *
import ReadinVindobona_Filter_fullperiod

'''READ IN BOKU Metdata'''
BOKUMetData = BOKUMet_Data.BOKUMet()
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
pathbase2 = "/Users/lnx/DATA/obs_point/chem/EEA/"
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
JJA19_s = datetime(2019, 6, 1, 00, 00)
JJA19_e = datetime(2019, 8, 31, 00, 00)
JJA20_s = datetime(2020, 6, 1, 00, 00)
JJA20_e = datetime(2020, 8, 31, 00, 00)
#o3 = o3_1990_2020_mda8_w[MAM18_s:MAM18_e]
#wd = BOKUMetData_dailysum["WD"].resample("W").mean()
o3 = o3_1990_2020_mda8[MAM18_s:MAM18_e]
o320 = o3_1990_2020_mda8[MAM20_s:MAM20_e]
o3jja19 = o3_1990_2020_mda8[JJA19_s:datetime(2019, 9, 1, 00, 00)]
o3jja20 = o3_1990_2020_mda8[JJA20_s:JJA20_e]
print(o3jja20)

wd = BOKUMetData_dailysum["WD"]
wd18 = wd[MAM18_s:MAM18_e]
wd18 = wd18[:-1]
wd20 = wd[MAM20_s:MAM20_e]
wdjja19 = wd[JJA19_s:JJA19_e]
wdjja20 = wd[JJA20_s:JJA20_e]
print(wdjja20)
#exit()

fs = 10  #fontsize
fig, axs = plt.subplots(nrows=4,ncols=2,sharey='row', sharex='col')#, figsize=(6, 6))
axs[0, 0].set_title('JJA2019')
pl1 = axs[0, 0].scatter(o3jja19['AT9STEF'], o3jja19['AT30801'], c=wdjja19, label="O3_nw", cmap='viridis') #Irnfritz
axs[1, 0].scatter(o3jja19['AT9STEF'], o3jja19['AT31301'], c=wdjja19, label="O3_ne")  #Mistelbach
#axs[1,0].legend(loc="upper left") #axs[1, 0].set_title('NE')
axs[2, 0].scatter(o3jja19['AT9STEF'], o3jja19['AT30603'], c=wdjja19, label="O3_se") #Himberg
axs[3, 0].scatter(o3jja19['AT9STEF'], o3jja19['AT32101'], c=wdjja19, label="O3_s") #Wiesmath
axs[0, 1].set_title('JJA2020')
pl1 = axs[0,1].scatter(o3jja20['AT9STEF'],o3jja20['AT30801'], c=wdjja20, label="O3_nw", cmap='viridis') #Irnfritz
axs[1, 1].scatter(o3jja20['AT9STEF'], o3jja20['AT31301'], c=wdjja20, label="O3_ne")  #Mistelbach
axs[2, 1].scatter(o3jja20['AT9STEF'], o3jja20['AT30603'], c=wdjja20, label="O3_se") #Himberg
axs[3, 1].scatter(o3jja20['AT9STEF'], o3jja20['AT32101'], c=wdjja20, label="O3_s") #Wiesmath
axs[0, 0].set_ylabel("O3_nw [μg/m³]")#, ax=axs[:, 0])
axs[1, 0].set_ylabel("O3_ne [μg/m³]")
axs[2, 0].set_ylabel("O3_se [μg/m³]")
axs[3, 0].set_ylabel("O3_s [μg/m³]")
axs[3, 0].set_xlabel("O3_vie [μg/m³]")
axs[3, 1].set_xlabel("O3_vie [μg/m³]")
for ax in fig.get_axes():
    print(ax)
    ax.set_xlim(40,130)
    ax.set_ylim(40,150)
plt.colorbar(pl1, ax=axs[:, 1], shrink=0.6, label="WD [°]")
plt.show()

fs = 10  #fontsize
fig, axs = plt.subplots(nrows=4,ncols=2,sharey='row', sharex='col')#, figsize=(6, 6))
axs[0, 0].set_title('MAM2018')
pl1 = axs[0, 0].scatter(o3['AT9STEF'], o3['AT30801'], c=wd18, label="O3_nw", cmap='viridis') #Irnfritz
axs[1, 0].scatter(o3['AT9STEF'], o3['AT31301'], c=wd18, label="O3_ne")  #Mistelbach
#axs[1,0].legend(loc="upper left") #axs[1, 0].set_title('NE')
axs[2, 0].scatter(o3['AT9STEF'], o3['AT30603'], c=wd18, label="O3_se") #Himberg
axs[3, 0].scatter(o3['AT9STEF'], o3['AT32101'], c=wd18, label="O3_s") #Wiesmath
axs[0, 1].set_title('MAM2020')
pl1 = axs[0,1].scatter(o320['AT9STEF'],o320['AT30801'], c=wd20, label="O3_nw", cmap='viridis') #Irnfritz
axs[1, 1].scatter(o320['AT9STEF'], o320['AT31301'], c=wd20, label="O3_ne")  #Mistelbach
axs[2, 1].scatter(o320['AT9STEF'], o320['AT30603'], c=wd20, label="O3_se") #Himberg
axs[3, 1].scatter(o320['AT9STEF'], o320['AT32101'], c=wd20, label="O3_s") #Wiesmath
axs[0, 0].set_ylabel("O3_nw [μg/m³]")#, ax=axs[:, 0])
axs[1, 0].set_ylabel("O3_ne [μg/m³]")
axs[2, 0].set_ylabel("O3_se [μg/m³]")
axs[3, 0].set_ylabel("O3_s [μg/m³]")
axs[3, 0].set_xlabel("O3_vie [μg/m³]")
axs[3, 1].set_xlabel("O3_vie [μg/m³]")
for ax in fig.get_axes():
    print(ax)
    ax.set_xlim(40,130)
    ax.set_ylim(40,150)

plt.colorbar(pl1, ax=axs[:, 1], shrink=0.6, label="WD [°]")
plt.show()