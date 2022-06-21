# -*- coding: utf-8 -*-
__author__ = 'lnx'
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.axis import Axis
import sys
from datetime import datetime
from datetime import timedelta
import numpy as np
from matplotlib import dates as d
import datetime as dt
import met.library.BOKUMet_Data as BOKUMet_Data
from met.library.conversions import *

def datestdtojd (stddate):
    fmt='%Y-%m-%d'
    sdtdate = datetime.strptime(stddate, fmt)
    sdtdate = sdtdate.timetuple()
    jdate = sdtdate.tm_yday
    return(jdate)

def jdtodatestd (jdate):
    fmt = '%Y%j'
    datestd = datetime.strptime(jdate, fmt).date()
    return(datestd)

#print(jdtodatestd('20181'))
#print(datestdtojd('2018-01-01'))

BOKUMetData = BOKUMet_Data.BOKUMet()
# DT = 'dewpoint temperature (degree C)'
# AT = 'air temperature (degree C)'
# RH = 'relative humidity (%)'
# GR = 'global radiation (W m^(-2))'
# WS = 'wind speed (km/h)'
# WD = 'wind direction (degree)'
# WSG = 'wind speed - gust (km/h)'
# PC = 'precipitation (10^(-1) mm)'
# AP = 'air pressure (hPa)'

#DAILY MEANS
BOKUMetData_dailysum = BOKUMetData.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean,
                                                      'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

#JULIAN DAY
BOKUMetData_dailysum['JD'] = (BOKUMetData_dailysum.index)
f = lambda x: datestdtojd(str(x)[:-9])
BOKUMetData_dailysum['JD'] = BOKUMetData_dailysum['JD'].apply(f)

#FILTER - WIND
isLowWS = BOKUMetData["WS"] < 0.3  #m/s
LowWSdays = BOKUMetData[isLowWS]
#print(LowWSdays.shape)
#print(LowWSdays)

#FILTER - GLOBAL RADIATION
juliandays = range(365)
thres_glob = []
#APOLIS in kWh/m2 (Tagessumme Globalstrahlung) ! thres_glob = ((1.25e-12)*(x**5)+ (7.38e-9)*(x**4) - (5.365e-6)*(x**3) + 0.000926*(x**2) - 0.00036*x + 1.08)*0.9
for x in juliandays:
    thres_glob.append(((1.25e-12)*(x**5)+ (7.38e-9)*(x**4) - (5.365e-6)*(x**3) + 0.000926*(x**2) - 0.00036*x + 1.08)*0.9*1000)  #in Wh/m2 Tagessumme

f2 = lambda x: (((1.25e-12)*(x**5)+ (7.38e-9)*(x**4) - (5.365e-6)*(x**3) + 0.000926*(x**2) - 0.00036*x + 1.08)*0.9*1000)
BOKUMetData_dailysum["GRthres"] = BOKUMetData_dailysum['JD'].apply(f2)
#print(BOKUMetData_dailysum.shape)

isHighGR = BOKUMetData_dailysum["GR"] > BOKUMetData_dailysum["GRthres"]
HighGRdays = BOKUMetData_dailysum[isHighGR]
#print(HighGRdays.shape)
#print(HighGRdays)


'''READ IN EEA air pollution data'''
pathbase2 = "/windata/DATA/obs_point/chem/EEA/"
o3_1990_2019_mda8 = pd.read_csv(pathbase2 + "o3_mda8_1990-2019_AT_mug.csv")
o3_1990_2019_mda8 = o3_1990_2019_mda8.set_index(pd.to_datetime(o3_1990_2019_mda8['date']))
o3_1990_2019_mda8 = o3_1990_2019_mda8.drop(columns=['date'])
o3_2020_mda1 = pd.read_csv(pathbase2 + "AT_O3_2020.csv")
o3_2020_mda1 = o3_2020_mda1.set_index(pd.to_datetime(o3_2020_mda1['date']))
o3_2020_mda1 = o3_2020_mda1.drop(columns=['date'])
o3_2020_mda8 = o3_2020_mda1.resample('8H', label='right').mean()
o3_2020_mda8 = o3_2020_mda8.resample('D').mean()
o3_1990_2020_mda8 = pd.concat([o3_1990_2019_mda8, o3_2020_mda8], axis=0)
o3_1990_2020_mda8 = o3_1990_2020_mda8*ugm3toppb_o3 #MUG->PPB
o3_1990_2020_da = o3_1990_2020_mda8.resample('D').mean()
o3_1990_2020_m = o3_1990_2020_mda8.resample('M').mean()
o3_1990_2020_mda8_w = o3_1990_2020_mda8.resample('W').mean()

#HCHO DATA
Vindobona = "/windata/DATA/remote/ground/maxdoas/Monika/"  # in DSCD
tframe = '60T'
AxisA = pd.read_csv(Vindobona + "hcho_A_1.6.2017-31.5.2020.csv")
AxisA = AxisA.set_index(pd.to_datetime(AxisA['date']))
AxisA= AxisA.rename(columns={'HCHO': 'HCHO_A'})
AxisA_drop = AxisA.drop(columns=['date'])
AxisA_hr_mean = AxisA_drop.resample(tframe).mean()
AxisA_d_mean = AxisA_hr_mean.resample('D').mean()
AxisA_d_max = AxisA_hr_mean.resample('D').max()

AxisB = pd.read_csv(Vindobona + "hcho_B_1.6.2017-31.5.2020.csv")
AxisB = AxisB.set_index(pd.to_datetime(AxisB['date']))
AxisB= AxisB.rename(columns={'HCHO': 'HCHO_B'})
AxisB_drop = AxisB.drop(columns=['date'])
AxisB_hr_mean = AxisB_drop.resample(tframe).mean()
AxisB_d_mean = AxisB_hr_mean.resample('D').mean()
AxisB_d_max = AxisB_hr_mean.resample('D').max()

AxisC = pd.read_csv(Vindobona + "hcho_C_1.6.2017-31.5.2020.csv")
AxisC = AxisC.set_index(pd.to_datetime(AxisC['date']))
AxisC = AxisC.rename(columns={'HCHO': 'HCHO_C'})
AxisC_drop = AxisC.drop(columns=['date'])
AxisC_hr_mean = AxisC_drop.resample(tframe).mean()
AxisC_d_mean = AxisC_hr_mean.resample('D').mean()
AxisC_d_max = AxisC_hr_mean.resample('D').max()

AxisD = pd.read_csv(Vindobona + "hcho_D_1.6.2017-31.5.2020.csv")
AxisD = AxisD.set_index(pd.to_datetime(AxisD['date']))
AxisD = AxisD.rename(columns={'HCHO': 'HCHO_D'})
AxisD_drop = AxisD.drop(columns=['date'])
AxisD_hr_mean = AxisD_drop.resample(tframe).mean()
AxisD_d_mean = AxisD_hr_mean.resample('D').mean()
AxisD_d_max = AxisD_hr_mean.resample('D').max()
#print(AxisD_d_mean)

AxisF = pd.read_csv(Vindobona + "hcho_F_1.6.2017-31.5.2020.csv")
AxisF = AxisF.set_index(pd.to_datetime(AxisF['date']))
AxisF = AxisF.rename(columns={'HCHO': 'HCHO_F'})
AxisF_drop = AxisF.drop(columns=['date'])
AxisF_hr_mean = AxisF_drop.resample(tframe).mean()
AxisF_d_mean = AxisF_hr_mean.resample('D').mean()
AxisF_d_max = AxisF_hr_mean.resample('D').max()

AxisG = pd.read_csv(Vindobona + "hcho_G_1.6.2017-31.5.2020.csv")
AxisG = AxisG.set_index(pd.to_datetime(AxisG['date']))
AxisG = AxisG.rename(columns={'HCHO': 'HCHO_G'})
AxisG_drop = AxisG.drop(columns=['date'])
AxisG_hr_mean = AxisG_drop.resample(tframe).mean()
AxisG_d_mean = AxisG_hr_mean.resample('D').mean()
AxisG_d_max = AxisG_hr_mean.resample('D').max()

AxisK = pd.read_csv(Vindobona + "hcho_K_13.3.2019-31.5.2020.csv")#, parse_dates=["date"])
AxisK = AxisK.set_index(pd.to_datetime(AxisK['date']))
AxisK = AxisK.rename(columns={'HCHO': 'HCHO_K'})
AxisK_drop = AxisK.drop(columns=['date'])
AxisK_hr_mean = AxisK_drop.resample(tframe).mean()
AxisK_d_mean = AxisK_hr_mean.resample('D').mean()
AxisK_d_max = AxisK_hr_mean.resample('D').max()

#print(AxisK_d_mean)
HCHO_met = pd.concat([BOKUMetData_dailysum, AxisD_d_mean, AxisK_d_mean], axis=1)
HCHO_met_hr = pd.concat([BOKUMetData, AxisD_hr_mean, AxisK_hr_mean], axis=1)

HCHO_met_hr['Month'] = HCHO_met_hr.index.month
HCHO_met_hr['Time'] = HCHO_met_hr.index.time
#print(HCHO_met_hr)

isHighGRall = HCHO_met["GR"] > HCHO_met["GRthres"]
HCHO_HighGRdays = HCHO_met[isHighGRall]
#print(HighGRdays.shape)
#print(HighGRdays)
#df.groupby('a').resample('3T').sum()
#print(AxisG_hr_mean.dt.dayofweek)

print(HCHO_met_hr.shape)
isLowWSall = HCHO_met_hr["WS"] < 3.0  #m/s
HCHO_LowWS_hr = HCHO_met_hr[isLowWSall]
print(HCHO_LowWS_hr)
"""
fig = plt.figure()
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(HCHO_HighGRdays['HCHO_K'], color='orange', label="hcho_obs_K_sun")
ax1.plot(HCHO_HighGRdays['HCHO_D'], color='orange', linestyle='dotted', label="hcho_obs_D_sun")
ax1.plot(HCHO_HighGRdays['HCHO_K'], color='red', label="hcho_obs_K_calm")
ax1.plot(HCHO_HighGRdays['HCHO_D'], color='red', linestyle='dotted', label="hcho_obs_D_calm")
ax1.plot(HCHO_met['HCHO_K'], color='navy', label="hcho_obs_K")
ax1.plot(HCHO_met['HCHO_D'], color='navy', linestyle='dotted', label="hcho_obs_D")
ax1.legend(loc='upper left')
ax1.set_ylabel("ug m3", size="medium")
ax1.legend()
#plt.show()
"""

"""FIG 0 - only sunny days
fig, ax = plt.subplots(1, figsize=(12,6))
pd.plotting.register_matplotlib_converters()
colors = ["k","gray","silver","greenyellow","chartreuse","green","yellow","orange","red","sandybrown","goldenrod","saddlebrown", "grey"]
#HCHO_HighGRdays_monthly_mean = []
for month in HCHO_LowWS_hr['Month'].unique():
    df = HCHO_LowWS_hr.loc[HCHO_LowWS_hr['Month'] == month]
    df = df.groupby('Time').describe() #mean()
    ax.plot(df['HCHO_K']['mean'], linewidth=2.0, linestyle='dotted', color=colors[month], label = month)
    #print(df['HCHO_K'])
    #ax.plot(df['HCHO_D']['mean'], linewidth=2.0, linestyle='dotted', color=colors[month], label = month)
    #ax.plot(df['HCHO_K']['mean'], linewidth=2.0, linestyle='solid', color=colors[month], label = month)
    #HCHO_HighGRdays_monthly_mean.append(df['HCHO_D']['mean'])
    #HCHO_HighGRdays_monthly_mean.append(df['HCHO_K']['mean'])
ax.legend()
ax.set_xlabel("time[hours]", size="medium")
ax.set_ylabel("HCHO[DSCD]", size="medium")
plt.title("WS < 3.0 m s-1")
myFmt = matplotlib.dates.DateFormatter("%m")
ax.xaxis.set_major_formatter(myFmt)
plt.show()

exit()
FIG 0 END """


"""FIG1 monthly mean diurnal cycles"""

fig, ax = plt.subplots(1, figsize=(12,6))
#dataframe['Month'] = dataframe.index.map(lambda x: x.strftime("%m"))
#dataframe['Time'] = dataframe.index.map(lambda x: x.strftime("%H:%M"))
AxisD_hr_mean['Month'] = AxisD_hr_mean.index.month
AxisD_hr_mean['Time'] = AxisD_hr_mean.index.time
AxisK_hr_mean['Month'] = AxisK_hr_mean.index.month
AxisK_hr_mean['Time'] = AxisK_hr_mean.index.time

pd.plotting.register_matplotlib_converters()
colors = ["k","gray","silver","greenyellow","chartreuse","green","yellow","orange","red","sandybrown","goldenrod","saddlebrown", "grey"]
AxisD_monthly_mean = []
AxisK_monthly_mean = []
for month in AxisD_hr_mean['Month'].unique():
    df = AxisD_hr_mean.loc[AxisD_hr_mean['Month'] == month]
    df = df.groupby('Time').describe() #.mean()
    #print(df['HCHO_D']['mean'])       #12x24h ok!
    #print(df.index) #12x24h ok!
    ax.plot(df['HCHO_D']['mean'], linewidth=2.0, color=colors[month], label = month)
    AxisD_monthly_mean.append(df['HCHO_D']['mean'])
ax.legend()

for month in AxisK_hr_mean['Month'].unique():
    df = AxisK_hr_mean.loc[AxisK_hr_mean['Month'] == month]
    df = df.groupby('Time').describe() #.mean()
    ax.plot(df['HCHO_K']['mean'], linewidth=2.0, linestyle='dotted', color=colors[month])#, label = month)
    AxisK_monthly_mean.append(df['HCHO_K']['mean'])

ax.set_xlabel("time [hours]", size="medium")
ax.set_ylabel("HCHO DSCD [molec cm-2]", size="medium")
plt.title("all weather conditions: D (city) - solid, K (vineyard, forest) - dotted ")

#hours = d.HourLocator()
#ax.xaxis.set_major_locator(hours)


fig.autofmt_xdate()
plt.show()

"""FIG 1 END"""

exit()

"""FIG 2 scatter plot """

start=datetime(2018,1,1)
start2=datetime(2020,1,1)
end=datetime(2020,5,31)

#print(len(AxisD_hr_mean[:-1004]), len(timeaxis_NO2[7255::2]))  #JD 31.Mai: 151*(24*2 half hours)=7248
#print(AxisD_hr_mean[:-1004])
#print(timeaxis_NO2[7255::2])

print(AxisA_d_mean[start:end])
print(o3_1990_2020_da["AT9STEF"][start:end])


try:
    fig = plt.figure()
    plt.scatter(AxisA_d_max[start:end], o3_1990_2020_da["AT9STEF"][start:end], color='navy', label="A", marker=".")
    plt.scatter(AxisB_d_max[start:end], o3_1990_2020_da["AT9STEF"][start:end], color='green', label="B", marker=".")
    plt.scatter(AxisC_d_max[start:end], o3_1990_2020_da["AT9STEF"][start:end], color='yellow', label="C", marker=".")
    plt.scatter(AxisD_d_max[start:end], o3_1990_2020_da["AT9STEF"][start:end], color='red', label="D", marker=".")
    plt.scatter(AxisF_d_max[start:end], o3_1990_2020_da["AT9STEF"][start:end], color='turquoise', label="F", marker=".")
    plt.scatter(AxisG_d_max[start:end], o3_1990_2020_da["AT9STEF"][start:end], color='purple', label="G", marker=".")
    plt.scatter(AxisK_d_max[start2:end], o3_1990_2020_da["AT9STEF"][start2:end], color='black', label="K", marker=".")
    plt.legend(loc='lower right')
    plt.ylabel("O3 mda8 [ppb]")
    plt.xlabel("HCHO dmax DSCD [molec cm-2]")
    plt.show()
except:
    print("Oops!", sys.exc_info()[0], "occurred.")
    pass


try:
    fig = plt.figure()
    plt.scatter(AxisA_d_mean[start:end], o3_1990_2020_da["AT9STEF"][start:end], color='navy', label="A", marker=".")
    plt.scatter(AxisB_d_mean[start:end], o3_1990_2020_da["AT9STEF"][start:end], color='green', label="B", marker=".")
    plt.scatter(AxisC_d_mean[start:end], o3_1990_2020_da["AT9STEF"][start:end], color='yellow', label="C", marker=".")
    plt.scatter(AxisD_d_mean[start:end], o3_1990_2020_da["AT9STEF"][start:end], color='red', label="D", marker=".")
    plt.scatter(AxisF_d_mean[start:end], o3_1990_2020_da["AT9STEF"][start:end], color='turquoise', label="F", marker=".")
    plt.scatter(AxisG_d_mean[start:end], o3_1990_2020_da["AT9STEF"][start:end], color='purple', label="G", marker=".")
    plt.scatter(AxisK_d_mean[start2:end], o3_1990_2020_da["AT9STEF"][start2:end], color='black', label="K", marker=".")
    plt.legend(loc='lower right')
    plt.ylabel("O3 mda8 [ppb]")
    plt.xlabel("HCHO dmean DSCD [molec cm-2]")
    plt.show()
except:
    print("Oops!", sys.exc_info()[0], "occurred.")
    pass

"""FIG 2 END"""
exit()

NO2_HMW = NO2_HMW.set_index(pd.to_datetime(NO2_HMW['timestamp.MEZ']))
NO2_HMW_drop = NO2_HMW.drop(columns=['timestamp.MEZ'])
NO2_SMW_STEF = NO2_HMW_drop["STEF"][1::2]
print(NO2_SMW_STEF)
NO2_SMW_STEF['Month'] = NO2_SMW_STEF.index.month
NO2_SMW_STEF['Time'] = NO2_SMW_STEF.index.time
pd.plotting.register_matplotlib_converters()
#colors = ["k","gray","silver","greenyellow","chartreuse","green","yellow","orange","red","sandybrown","goldenrod","saddlebrown", "grey"]
NO2STEF_monthly_mean = []
for month in NO2_SMW_STEF['Month'].unique():
    df = NO2_SMW_STEF.loc[NO2_SMW_STEF['Month'] == month]
    df = df.groupby('Time').describe() #.mean()
    print(df)
    print(df.index)
    #ax.plot(df['HCHO']['mean'], linewidth=2.0, color=colors[month], label = month)
    #NO2STEF_monthly_mean.append(df['HCHO']['mean'])

exit()

"""FIG 3 simple timeseries """
try:
    fig = plt.figure()
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    #ax1.plot(AxisA_hr_mean, color='navy', label="hcho_obs_A")
    #ax1.plot(AxisB_hr_mean, color='royalblue', label="hcho_obs_B")
    #ax1.plot(AxisC_hr_mean, color='cyan', label="hcho_obs_C")
    #ax1.plot(AxisD_hr_mean, color='yellow', label="hcho_obs_D")
    #ax1.plot(AxisF_hr_mean, color='red', label="hcho_obs_F")
    #ax1.plot(AxisG_hr_mean, color='brown', label="hcho_obs_G")

    #ax1.plot(NO2_HMW["STEF"][1::2], color='blue', label="no2_obs")
    #ax1.plot(timeaxis_NO2[1::2], NO2_HMW["STEF"][1::2], color='blue', label="no2_obs")
    #ax1.plot(timeaxis_NO[1::2], NO_HMW["STEF"][1::2], color='pink', label="no_obs")
    #ax1.plot(timeaxis_O3[1::2], O3_HMW["HMW.O3.STEF.09.ug.m3.."][1::2], color='violet', label="o3_obs")

    ax1.plot(AxisA_hr_mean[:-1004], timeaxis_NO2[7255::2], color='navy', label="hcho_obs_A vs. NO2_STEF")

    ax1.legend(loc='upper left')
    ax1.set_ylabel("ug m3", size="medium")

   # ax2.plot(timeaxis_met[1:-diff], GL_SMW["STEF"][1:-diff], color='yellow', label="glob_obs")
   # ax2.legend(loc='upper right')
   # ax2.set_ylabel("W m-2", size="medium")

    #plt.xlabel("hours")

    #ax2.set_ylabel("ppb", size="medium")
    #ax1.set_xlim(0, 240)
    #ax1.set_ylim(0, 50)
    #plt.title("NO2,Stefansplatz")#, Vienna region", size="large")#+"2m air temperature"))
    #myFmt = matplotlib.dates.DateFormatter("%d")
    #ax1.xaxis.set_major_formatter(myFmt)
    #fig1.autofmt_xdate()
    plt.show()
except:
    print("Oops!", sys.exc_info()[0], "occured.")
    pass
