# -*- coding: utf-8 -*-
__author__ = 'lnx'

import numpy as np
import pandas as pd
from datetime import datetime
import monthdelta
import netCDF4
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVindobona_Filter_fullperiod

#print(ugm3toppb_no2, ugm3toppb_no)
'''READ IN CEILOMETER DATA'''
file_pbl = "/windata/DATA/obs_point/met/ZAMG/Ceilometer/MH_Wien_Hohe_Warte_20170101_20201231.csv"
pbl = pd.read_csv(file_pbl,skiprows=2, parse_dates={'datetime':[0,1]})
pbl.columns = ['datetime','PBL']  #UTC
pbl = pbl.set_index(pbl['datetime'])
pbl = pbl.drop(columns=['datetime'])
pbl = pbl.resample('D').max()

"""READ IN MGNOUT CAMS"""
foldername_ol18 = "/data1/models/nilu/SEEDS/MEGAN/2018/ol/ISOP/"  #MGNOUT_CAMS_BIG_ISOP_20190102.nc
foldername_as18 = "/data1/models/nilu/SEEDS/MEGAN/2018/assim_LAI/ISOP/"
foldername_ol19 = "/data1/models/nilu/SEEDS/MEGAN/2019/ol/ISOP/"  #MGNOUT_CAMS_BIG_ISOP_20190102.nc
foldername_as19 = "/data1/models/nilu/SEEDS/MEGAN/2019/assim_LAI/ISOP/"
foldername_ol20 = "/data1/models/nilu/SEEDS/MEGAN/2020/ol/ISOP/"  #MGNOUT_CAMS_BIG_ISOP_20190102.nc
foldername_as20 = "/data1/models/nilu/SEEDS/MEGAN/2020/assim_LAI/ISOP/"

#The isoprene emissions are in units of mole m-2 s-1.
# bottom-up isoprene emissions for 2019 using the MEGAN-SURFEX coupling at NILU has been completed.
# This includes the correction to PAR, and the emission totals are now much more consistent with existing datasets,
# e.g., CAMS-GLOBAL-BIOGENIC. For instance, for 2019, using the SURFEX data from the assimilation of LAI,
# we get an annual total of 5.15 Tg yr-1 (see attached) compared to approx. 4.95 Tg yr-1 from CAMS-GLOBAL-BIO v3.1 and
# 4.65 Tg yr-1 from CAMS-GLOBAL-BIO v3.0.

def EmisSEEDS(foldername, index_lat, index_lon):
    files = os.listdir(foldername)
    files = sorted(files)
    dateaxis=[]
    Emis_max=[]
    Emis_noontime=[]
    Emis_noon=[]
    for i in range(len(files)):
        day = str(files[i][-5:-3])  # splitlistcomp[3:4]
        month = str(files[i][-7:-5])  # splitlistcomp[2:3]
        year = "20" + str(files[i][-9:-7])  # splitlistcomp[:2]
        #print(day,month,year)
        date = datetime(year=int(year), month=int(month), day=int(day))
        #print(date)
        dateaxis.append(date)
        path = foldername+files[i]
        infile = netCDF4.Dataset(path)  #path.decode('UTF-8')  #OSError: [Errno -51] NetCDF: Unknown file format: b'/windata/DATA/models/nilu/MEGAN3_SURFEX_SEEDS/MEGAN/ol/MGNOUT_CAMS_BIG_20190803.nc'
        Emis_hourlyvalue = infile.variables['Emiss'][:, index_lat, index_lon, 0]  #TODO: only first emission layer (ISO) read in
        Emis_max.append(Emis_hourlyvalue.max())
        #print(Emis_hourlyvalue)
        #Emis_hourly.append(Emis_hourlyvalue)
        Emis_noon = np.average(Emis_hourlyvalue[8:14])
        Emis_noontime.append(Emis_noon)
    Emis_max = pd.DataFrame({'datetime': dateaxis, 'ISO': Emis_max})
    Emis_max['datetime'] = pd.to_datetime(Emis_max['datetime'])
    Emis_max = Emis_max.set_index(['datetime'])
    Emis_noontime = pd.DataFrame({'datetime': dateaxis, 'ISO': Emis_noontime})
    Emis_noontime['datetime'] = pd.to_datetime(Emis_noontime['datetime'])
    Emis_noontime = Emis_noontime.set_index(['datetime'])
    return Emis_max, Emis_noontime

index_lat_city = 201 #202  #LAT 48.25°N     199/426: Leithagebirge! 202/422 city rim to Wienerwald!
index_lon_city = 424 #422 #LON 16.25°E (city rim to Wienerwald) or 421: LON 16.15°E (middle Wienerwald)
index_lat_leitha = 199
index_lon_leitha = 426
index_lat_ww = 202
index_lon_ww = 422
index_lat_lob = 201
index_lon_lob = 425
index_lat_LNeus = 196
index_lon_LNeus = 427

#Emis_ol18, Emis_ol_noontime18 = EmisSEEDS(foldername_ol18)
#Emis_assim18, Emis_assim_noontime18 = EmisSEEDS(foldername_as18)
Emis_ol, Emis_ol_noontime = EmisSEEDS(foldername_ol19,index_lat_ww, index_lon_ww)
Emis_assim, Emis_assim_noontime = EmisSEEDS(foldername_as19,index_lat_ww, index_lon_ww)
Emis_assim_city, Emis_assim_noontime_city = EmisSEEDS(foldername_as19,index_lat_city, index_lon_city)
Emis_assim_lob, Emis_assim_noontime_lob = EmisSEEDS(foldername_as19,index_lat_lob, index_lon_lob)
Emis_assim_leitha, Emis_assim_noontime_leitha = EmisSEEDS(foldername_as19,index_lat_leitha, index_lon_leitha)
Emis_assim_LNeus, Emis_assim_noontime_LNeus = EmisSEEDS(foldername_as19,index_lat_LNeus, index_lon_LNeus)
Emis_ol20, Emis_ol_noontime20 = EmisSEEDS(foldername_ol20,index_lat_ww, index_lon_ww)
Emis_assim20, Emis_assim_noontime20 = EmisSEEDS(foldername_as20,index_lat_ww, index_lon_ww)
Emis_assim20_city, Emis_assim_noontime20_city = EmisSEEDS(foldername_as20,index_lat_city, index_lon_city)



"read in VINDOBONA"
foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))
hcho_w = hcho_dmax.resample("W").mean()

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
#"AT"+compound+"stationsname"+"year"+_"timeseries.csv"
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
start = datetime(2019, 6, 1, 00, 00)
end = datetime(2019, 9, 1, 00, 00)
JJA19_s = datetime(2019, 6, 1, 00, 00)
JJA19_e = datetime(2019, 8, 31, 00, 00)
JJA20_s = datetime(2020, 6, 1, 00, 00)
JJA20_e = datetime(2020, 8, 31, 00, 00)
fs = 10  # fontsize

ISO20_JJA = Emis_assim_noontime20[JJA20_s:JJA20_e].values.flatten()
ISO19_JJA = Emis_assim_noontime[JJA19_s:JJA19_e].values.flatten()

filtered_hcho20_JJA = hcho_d[JJA20_s:JJA20_e].values[~np.isnan(hcho_d[JJA20_s:JJA20_e].values)]
filtered_hcho19_JJA = hcho_d[JJA19_s:JJA19_e].values[~np.isnan(hcho_d[JJA19_s:JJA19_e].values)]
"""
fig, axes = plt.subplots(nrows=2, ncols=2, sharey='row') #sharex='col', figsize=(6, 6))
#fig.set_size_inches(3.39,2.54)

axes[0, 0].boxplot(filtered_hcho19_JJA)
axes[0, 0].set_title('OBS_JJA19_dry', fontsize=fs)
axes[0, 0].set_ylabel(u'HCHO [ppb]', fontsize=fs)

axes[0, 1].boxplot(filtered_hcho20_JJA)
axes[0, 1].set_title('OBS_JJA20_ref', fontsize=fs)

axes[1, 0].boxplot(ISO19_JJA)
axes[1, 0].set_title('MOD_JJA19_dry', fontsize=fs)
axes[1, 0].set_ylabel(u'isoprene [mol s-1 m-2]', fontsize=fs)

axes[1, 1].boxplot(ISO20_JJA)
axes[1, 1].set_title('MOD_JJA20_ref', fontsize=fs)
plt.show()
"""

fig = plt.figure(figsize=(8, 3), dpi=100)
ax1 = fig.add_subplot(211)
ax1.set_title('(a) OBS', loc='center', size='medium')#, color='green')
ax1.plot(hcho_d[start:end], linewidth="1", color='black', label="HCHO_19dry")#, label="HCHO") #,dmax", linestyle="solid")
ax1.plot(hcho_d[start:end].index,hcho_d[datetime(2020,6,1): datetime(2020, 9, 1)].values, linewidth="1", color='black', linestyle=":", label="HCHO_20ref")
ax1.set_ylabel("[ppb]", size="medium")
ax1.legend(loc='upper left')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
#ax1.set_xlim(start,end)
ax1.grid()
#ax1.set_xticks([])
#ax1.set_yticks([])

ax2 = fig.add_subplot(212)
ax2.set_title('(b) MOD', loc='center', size='medium')#, color='green')
ax2.plot(Emis_assim_noontime_city[start:end], linewidth="1", color='orange', label="ISO_19dry") #label="GR,sum,w"
ax2.plot(Emis_assim_noontime_city[start:end].index,Emis_assim_noontime20_city[datetime(2020,6,1): datetime(2020, 9, 1)].values, linewidth="1", color='orange', linestyle=":", label="ISO_20ref")
#ax1.set_ylim(0,2E-8)
ax2.set_ylabel("[mol s-1 m-2]", size="medium")
ax2.legend(loc='upper left')
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax2.grid()
#ax2.set_xticks([])
#ax2.set_yticks([])
plt.show()

fig = plt.figure()
plt.suptitle("JJA19 vs. JJA20")
ax1 = fig.add_subplot(211)
ax1.set_title('(a)', loc='left', size='medium')#, color='green')
ax1.plot(o3_1990_2020_mda8_w['AT30701'][start:end],linewidth="1", color='darkblue', linestyle="solid",label="O3_nw") #Irnfritz
ax1.plot(o3_1990_2020_mda8_w['AT30701'][start:end].index, o3_1990_2020_mda8_w['AT30701'][datetime(2020, 6, 1):datetime(2020, 9, 7)].values,linewidth="1", color='darkblue', linestyle=":")
ax1.plot(o3_1990_2020_mda8_w['AT31301'][start:end],linewidth="1", color='blue', linestyle="solid",label="O3_ne") #Mistelbach
ax1.plot(o3_1990_2020_mda8_w['AT31301'][start:end].index, o3_1990_2020_mda8_w['AT31301'][datetime(2020, 6, 1):datetime(2020, 9, 7)].values,linewidth="1", color='blue', linestyle=":")
ax1.plot(o3_1990_2020_mda8_w['AT30603'][start:end],linewidth="1", color='violet', linestyle="solid",label="O3_se") #Himberg
ax1.plot(o3_1990_2020_mda8_w['AT30603'][start:end].index, o3_1990_2020_mda8_w['AT30603'][datetime(2020, 6, 1):datetime(2020, 9, 7)].values,linewidth="1", color='violet', linestyle=":")
ax1.plot(o3_1990_2020_mda8_w['AT32101'][start:end],linewidth="1", color='purple', linestyle="solid",label="O3_s") #Wiesmath
ax1.plot(o3_1990_2020_mda8_w['AT32101'][start:end].index, o3_1990_2020_mda8_w['AT32101'][datetime(2020, 6, 1):datetime(2020, 9, 7)].values,linewidth="1", color='purple', linestyle=":")
ax1.set_ylabel("[μg/m³]", size="medium")
ax1.grid()
ax1.set_xticks([])
ax1.set_xlim(start,end)
ax1.legend(loc='upper left')

ax1 = fig.add_subplot(212)
ax1.set_title('(b)', loc='left', size='medium')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(BOKUMetData_dailysum["WS"][start:end]/3.6, linewidth="1", color='blue', label="WS") #label="GR,sum,w"
ax1.plot(BOKUMetData_dailysum["WS"][start:end].index, (BOKUMetData_dailysum["WS"][datetime(2020, 6, 1):datetime(2020, 9, 1)].values)/3.6, linewidth="1", color='blue', linestyle=":")
ax2.plot(pbl[start:end]/1000, linewidth="1", color='violet', label="PBL") #label="GR,sum,w"
ax2.plot(pbl[start:end].index, (pbl[datetime(2020, 6, 1):datetime(2020, 9, 1)].values)/1000, linewidth="1", color='violet', linestyle=":")
ax1.set_xlim(start,end)
ax1.set_ylabel("[m s-1]", size="medium")
ax2.set_ylabel("[km]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='lower left')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1.grid()
plt.show()

#exit()
print(Emis_assim_noontime20[start:end])

fig = plt.figure(figsize=(8, 3), dpi=100)
plt.suptitle("JJA19 vs. JJA20")
ax1 = fig.add_subplot(111)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.plot(Emis_assim_noontime[start:end], linewidth="1", color='blue', label="ISO_WW dry_mod")
ax2.plot(Emis_assim_noontime_city[start:end], linewidth="1", color='red', label="ISO_CITY dry_mod")
ax2.plot(Emis_assim_noontime_lob[start:end], linewidth="1", color='turquoise', label="ISO_LOB dry_mod")
ax2.plot(Emis_assim_noontime_leitha[start:end], linewidth="1", color='green', label="ISO_LEITHA dry_mod")
ax2.plot(Emis_assim_noontime_LNeus[start:end], linewidth="1", color='violet', label="ISO_LakeNeusiedl dry_mod")
#ax2.plot(Emis_assim_noontime[start:end].index,Emis_assim_noontime20[datetime(2020, 6, 1):datetime(2020, 9, 1)].values, linewidth="1", color='orange', linestyle=":", label="ISO_ref_mod")
ax1.plot(hcho_d[start:end], linewidth="1", color='black', label="HCHO_dry_obs")
#ax1.plot(hcho_d[start:end].index,hcho_d[datetime(2020, 6, 1):datetime(2020, 9, 1)].values, linewidth="1", color='black', linestyle=":", label="HCHO_ref_obs")
ax1.set_xlim(start,end)
ax2.set_ylim(0,4E-8)
ax2.set_ylabel("[mol s-1 m-2]", size="medium")
ax1.set_ylabel("[ppb]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1.grid()
ax1.set_xticks([])
plt.show()