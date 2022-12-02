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
foldername_ol20 = "/data1/models/nilu/SEEDS/MEGAN/2020/ol/ISOP/"  #MGNOUT_CAMS_BIG_ISOP_20190102.nc
foldername_as20 = "/data1/models/nilu/SEEDS/MEGAN/2020/assim_LAI/ISOP/"

#The isoprene emissions are in units of mole m-2 s-1.
# bottom-up isoprene emissions for 2019 using the MEGAN-SURFEX coupling at NILU has been completed.
# This includes the correction to PAR, and the emission totals are now much more consistent with existing datasets,
# e.g., CAMS-GLOBAL-BIOGENIC. For instance, for 2019, using the SURFEX data from the assimilation of LAI,
# we get an annual total of 5.15 Tg yr-1 (see attached) compared to approx. 4.95 Tg yr-1 from CAMS-GLOBAL-BIO v3.1 and
# 4.65 Tg yr-1 from CAMS-GLOBAL-BIO v3.0.

def EmisSEEDS(foldername):
    files = os.listdir(foldername)
    files = sorted(files)
    dateaxis=[]
    Emis_max=[]
    Emis_noontime=[]
    Emis_noon=[]
    index_lat = 202  #LAT 48.25°N
    index_lon = 422 #LON 16.25°E (city rim to Wienerwald) or 421: LON 16.15°E (middle Wienerwald)
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

Emis_ol18, Emis_ol_noontime18 = EmisSEEDS(foldername_ol18)
Emis_assim18, Emis_assim_noontime18 = EmisSEEDS(foldername_as18)
#Emis_ol, Emis_ol_noontime = EmisSEEDS(foldername_ol)
#Emis_assim, Emis_assim_noontime = EmisSEEDS(foldername_as)
Emis_ol20, Emis_ol_noontime20 = EmisSEEDS(foldername_ol20)
Emis_assim20, Emis_assim_noontime20 = EmisSEEDS(foldername_as20)

Emis_MAM2018 = Emis_assim_noontime18[datetime(2018, 3, 1, 00, 00): datetime(2018, 5, 31, 00, 00)]
Emis_MAM2020 = Emis_assim_noontime20[datetime(2020, 3, 1, 00, 00): datetime(2020, 5, 31, 00, 00)]


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

vp_sat = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3))  #kPa sh. Dingman
vp_air = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3)) * (BOKUMetData_hourlymean["RH"]/100)
vpd = vp_sat - vp_air
#print(vp_sat,vp_air, vpd)
#vpd.plot()
#plt.show()
vpd_d = vpd.resample('D').mean()
vpd_dmax = vpd.resample('D').max()
vpd_dmax_w = vpd_dmax.resample('W').max()

'''READ IN EEA air pollution data'''
pathbase2 = "/windata/DATA/obs_point/chem/EEA/"
#"AT"+compound+"stationsname"+"year"+_"timeseries.csv"
nox_1990_2019_da = pd.read_csv(pathbase2 + "nox_da_1990-2019_AT_ppb.csv")
nox_1990_2019_da = nox_1990_2019_da.set_index(pd.to_datetime(nox_1990_2019_da['date']))
nox_1990_2019_da = nox_1990_2019_da.drop(columns=['date'])
no2_2020_mda1 = pd.read_csv(pathbase2 + "AT_NO2_2020.csv")
no2_2020_mda1 = no2_2020_mda1.set_index(pd.to_datetime(no2_2020_mda1['date']))
no2_2020_mda1 = no2_2020_mda1.drop(columns=['date'])

no2_2020_mda1 = no2_2020_mda1*0.5319148936 #ugm3toppb_no2
no2_2020_da = no2_2020_mda1.resample('D').mean()
no_2020_mda1 = pd.read_csv(pathbase2 + "AT_NO_2020.csv")
no_2020_mda1 = no_2020_mda1.set_index(pd.to_datetime(no_2020_mda1['date']))
no_2020_mda1 = no_2020_mda1.drop(columns=['date'])
no_2020_mda1 = no_2020_mda1*0.8 #ugm3toppb_no
no_2020_da = no_2020_mda1.resample('D').mean()
nox_2020_da = no_2020_da.add(no2_2020_da)
nox_1990_2020_da = pd.concat([nox_1990_2019_da, nox_2020_da], axis=0)
nox_1990_2020_da_w = nox_1990_2020_da.resample('W').mean()

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
start = MAM20_s
end = datetime(2020, 6, 1, 00, 00)
start2 = datetime(2020, 4, 15, 00, 00)
end2 = datetime(2020, 6, 1, 00, 00)
start3 = datetime(2018, 4, 15, 00, 00)


fig = plt.figure()
plt.suptitle("MAM20 vs. MAM18")
"""
ax1 = fig.add_subplot(11)
ax1.set_title('(a)', loc='left', size='medium')#, color='green')
x1 = plt.gca()
ax2 = ax1.twinx()
ax2.plot(o3_1990_2020_mda8_w['AT9STEF'][start:end],linewidth="1", color='violet', linestyle="solid",label="O3_vie") #label="O3,mda8,w",
ax2.plot(o3_1990_2020_mda8_w['AT9STEF'][start:end].index, o3_1990_2020_mda8_w['AT9STEF'][datetime(2018, 3, 1):datetime(2018, 6, 7)].values,linewidth="1", color='violet', linestyle=":")
#ax1.plot(BOKUMetData_dailysum["GR"][start:end], linewidth="0.1", color='orange')  #label="GR,sum"
ax1.plot(BOKUMetData_weekly["GR"][start:end]/1000, linewidth="1", color='orange', label="GR") #label="GR,sum,w"
ax1.plot(BOKUMetData_weekly["GR"][start:end].index, (BOKUMetData_weekly["GR"][datetime(2018, 3, 1):datetime(2018, 6, 7)].values)/1000, linewidth="1", color='orange', linestyle=":")
ax1.set_xlim(start,end)
ax1.set_ylabel("[kWh/m²]", size="medium")
ax2.set_ylabel("[μg/m³]", size="medium")
ax1.grid()
ax1.set_xticks([])
ax1.legend(loc='upper left')
ax2.legend(loc='lower left')
"""
ax1 = fig.add_subplot(211)
ax1.set_title('(a)', loc='left', size='medium')#, color='green')
ax1.plot(o3_1990_2020_mda8_w['AT30701'][start:end],linewidth="1", color='darkblue', linestyle="solid",label="O3_nw") #Irnfritz
ax1.plot(o3_1990_2020_mda8_w['AT30701'][start:end].index, o3_1990_2020_mda8_w['AT30701'][datetime(2018, 3, 1):datetime(2018, 6, 7)].values,linewidth="1", color='darkblue', linestyle=":")
ax1.plot(o3_1990_2020_mda8_w['AT31301'][start:end],linewidth="1", color='blue', linestyle="solid",label="O3_ne") #Mistelbach
ax1.plot(o3_1990_2020_mda8_w['AT31301'][start:end].index, o3_1990_2020_mda8_w['AT31301'][datetime(2018, 3, 1):datetime(2018, 6, 7)].values,linewidth="1", color='blue', linestyle=":")
ax1.plot(o3_1990_2020_mda8_w['AT30603'][start:end],linewidth="1", color='violet', linestyle="solid",label="O3_se") #Himberg
ax1.plot(o3_1990_2020_mda8_w['AT30603'][start:end].index, o3_1990_2020_mda8_w['AT30603'][datetime(2018, 3, 1):datetime(2018, 6, 7)].values,linewidth="1", color='violet', linestyle=":")
ax1.plot(o3_1990_2020_mda8_w['AT32101'][start:end],linewidth="1", color='purple', linestyle="solid",label="O3_s") #Wiesmath
ax1.plot(o3_1990_2020_mda8_w['AT32101'][start:end].index, o3_1990_2020_mda8_w['AT32101'][datetime(2018, 3, 1):datetime(2018, 6, 7)].values,linewidth="1", color='purple', linestyle=":")
ax1.set_ylabel("[μg/m³]", size="medium")
ax1.grid()
ax1.set_xticks([])
ax1.set_xlim(start,end)
ax1.legend(loc='upper left')
"""
ax1 = fig.add_subplot(513)
ax1.set_title('(c)', loc='left', size='medium')#, color='green')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.plot(o3_1990_2020_mda8_w['AT30603'][start:end],linewidth="1", color='violet', linestyle="solid",label="O3_se") #Himberg
ax2.plot(o3_1990_2020_mda8_w['AT30603'][start:end].index, o3_1990_2020_mda8_w['AT9STEF'][datetime(2018, 3, 1):datetime(2018, 6, 7)].values,linewidth="1", color='violet', linestyle=":")
ax2.set_ylabel("[μg/m³]", size="medium")
ax1.set_xticks([])
ax1.grid()
ax1.set_xlim(start,end)
ax1.legend(loc='upper left',fontsize="small")
ax2.legend(loc='lower left',fontsize="small")
ax1.grid()

ax1 = fig.add_subplot(514)
ax1.set_title('(d)', loc='left', size='medium')#, color='green')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.plot(o3_1990_2020_mda8_w['AT31301'][start:end],linewidth="1", color='violet', linestyle="solid",label="O3_ne") #Mistelbach
ax2.plot(o3_1990_2020_mda8_w['AT31301'][start:end].index, o3_1990_2020_mda8_w['AT9STEF'][datetime(2018, 3, 1):datetime(2018, 6, 7)].values,linewidth="1", color='violet', linestyle=":")
ax2.set_ylabel("[μg/m³]", size="medium")
ax2.plot(o3_1990_2020_mda8_w['AT32101'][start:end],linewidth="1", color='violet', linestyle="solid",label="O3_s") #Wiesmath
ax2.plot(o3_1990_2020_mda8_w['AT32101'][start:end].index, o3_1990_2020_mda8_w['AT9STEF'][datetime(2018, 3, 1):datetime(2018, 6, 7)].values,linewidth="1", color='violet', linestyle=":")
ax1.set_xlim(start,end)
ax1.set_xticks([])
ax1.legend(loc='upper left')
ax2.legend(loc='lower left')
ax1.grid()
"""
ax1 = fig.add_subplot(212)
ax1.set_title('(b)', loc='left', size='medium')#, color='green')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(BOKUMetData_dailysum["WS"][start:end]/3.6, linewidth="1", color='blue', label="WS") #label="GR,sum,w"
ax1.plot(BOKUMetData_dailysum["WS"][start:end].index, (BOKUMetData_dailysum["WS"][datetime(2018, 3, 1):datetime(2018, 6, 1)].values)/3.6, linewidth="1", color='blue', linestyle=":")
ax2.plot(pbl[start:end]/1000, linewidth="1", color='violet', label="PBL") #label="GR,sum,w"
ax2.plot(pbl[start:end].index, (pbl[datetime(2018, 3, 1):datetime(2018, 6, 1)].values)/1000, linewidth="1", color='violet', linestyle=":")
ax1.set_xlim(start,end)
#ax2.axvline(x=datetime(2020,5,10))
ax1.set_ylabel("[m s-1]", size="medium")
ax2.set_ylabel("[km]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='lower left')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1.grid()
plt.show()

print(Emis_assim_noontime20[start:end])

#fig = plt.figure()
fig = plt.figure(figsize=(8, 3), dpi=100)
ax1 = fig.add_subplot(211)
ax1.set_title('(a) OBS', loc='center', size='medium')#, color='green')
ax1.plot(hcho_d[start:end], linewidth="1", color='black', label="HCHO_20dry")#, label="HCHO") #,dmax", linestyle="solid")
ax1.plot(hcho_d[start:end].index,hcho_d[MAM18_s: datetime(2018, 6, 1)].values, linewidth="1", color='black', linestyle=":", label="HCHO_18ref")
ax1.set_ylabel("[ppb]", size="medium")
ax1.legend(loc='upper left')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
#ax1.set_xlim(start,end)
ax1.grid()
#ax1.set_xticks([])
#ax1.set_yticks([])

ax2 = fig.add_subplot(212)
ax2.set_title('(b) MOD', loc='center', size='medium')#, color='green')
ax2.plot(Emis_assim_noontime20[start:end], linewidth="1", color='orange', label="ISO_20dry") #label="GR,sum,w"
ax2.plot(Emis_assim_noontime20[start:end].index,Emis_assim_noontime18[MAM18_s:datetime(2018, 6, 1)].values, linewidth="1", color='orange', linestyle=":", label="ISO_18ref")
#ax1.set_ylim(0,2E-8)
ax2.set_ylabel("[mol s-1 m-2]", size="medium")
ax2.legend(loc='upper left')
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax2.grid()
#ax2.set_xticks([])
#ax2.set_yticks([])
plt.show()
exit()

fig = plt.figure(figsize=(8, 3), dpi=100)
plt.suptitle("MAM20_dry vs. MAM18_ref")
ax1 = fig.add_subplot(111)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.plot(Emis_assim_noontime20[start:end], linewidth="1", color='orange', label="ISO_dry_mod") #label="GR,sum,w"
ax2.plot(Emis_assim_noontime20[start:end].index,Emis_assim_noontime18[MAM18_s:datetime(2018, 6, 1)].values, linewidth="1", color='orange', linestyle=":", label="ISO_ref_mod")
ax1.plot(hcho_d[start:end], linewidth="1", color='black', label="HCHO_dry_obs")#, label="HCHO") #,dmax", linestyle="solid")
#ax1.plot(hcho_w[start:end], linewidth="1", color='black',label="HCHO_dry")#, label="HCHO,dmax,w", linestyle="solid")
ax1.plot(hcho_d[start:end].index,hcho_d[MAM18_s: datetime(2018, 6, 1)].values, linewidth="1", color='black', linestyle=":", label="HCHO_ref_obs")
#ax1.plot(hcho_w[start:end].index,hcho_w[MAM18_s: datetime(2018, 6, 7)].values, linewidth="1", color='black', linestyle=":",label="HCHO_ref")
ax1.set_xlim(start,end)
ax2.set_ylim(0,2E-8)
#ax2.axvline(x=datetime(2020,5,10))
ax2.set_ylabel("[mol s-1 m-2]", size="medium")
ax1.set_ylabel("[ppb]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1.grid()
ax1.set_xticks([])
plt.show()