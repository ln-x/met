# -*- coding: utf-8 -*-
__author__ = 'lnx'
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sys
from datetime import datetime
from datetime import timedelta
import numpy as np
from matplotlib import dates as d
import datetime as dt

"""
Liebe Heidi,
In der BOKUbox sind die pm, NO, NO2, O3, HCHO (in DSCD) und met Daten 1.1.2017 – 04/2020-  zusätzlich Tmin in °C (Spartacus) und APOLIS in kWh/m2 (Tagessumme Globalstrahlung) für die O3-Stationen, denn die ZAMG hat nur Jan – April hergegeben. Wenn du komplette*.nc files Spartacus oder Apolis brauchst, dann  bitte einfach melden habe Daten von 1990 – 2019.
Und hier der poly-fit für die Strahlungsdaten –„x“ ist Tag im Jahr (von 1 -> 365 (366)) clear sky , wenn mind 90% der max. Strahlung
# calculate 90% of max globrad -> threshold
thres.glob <- (1.25e-12*x^5+ 7.38E-09*x^4 - 5.365E-06*x^3 + 0.000926*x^2 - 0.00036*x + 1.08)*0.9
LG Monika
"""

Vindobona = "/windata/GOOGLEDrive/DATA/remote/ground/maxdoas/Monika/"  # in DSCD
tframe = '60T'
AxisA = pd.read_csv(Vindobona + "hcho_A_1.6.2017-31.5.2020.csv")#, parse_dates=["date"])
#print(AxisA.date)  #0        2017-06-01 04:39:34
#AxisA.date = pd.to_datetime(AxisA.date)
#print(type(AxisA.date)) #<class 'pandas.core.series.Series'>
#print(AxisA.index, AxisA.columns, AxisA.info, type(AxisA))
AxisA = AxisA.set_index(pd.to_datetime(AxisA['date']))
AxisA_drop = AxisA.drop(columns=['date'])
AxisA_hr_mean = AxisA_drop.resample(tframe).mean()
#AxisA_resampled = AxisA_drop.resample('60min') #DatetimeIndexResampler [freq=<15 * Minutes>, axis=0, closed=left, label=left, convention=start, origin=start_day]#

AxisB = pd.read_csv(Vindobona + "hcho_B_1.6.2017-31.5.2020.csv")
AxisB = AxisB.set_index(pd.to_datetime(AxisB['date']))
AxisB_drop = AxisB.drop(columns=['date'])
AxisB_hr_mean = AxisB_drop.resample(tframe).mean()

AxisC = pd.read_csv(Vindobona + "hcho_C_1.6.2017-31.5.2020.csv")
AxisC = AxisC.set_index(pd.to_datetime(AxisC['date']))
AxisC_drop = AxisC.drop(columns=['date'])
AxisC_hr_mean = AxisC_drop.resample(tframe).mean()

AxisD = pd.read_csv(Vindobona + "hcho_D_1.6.2017-31.5.2020.csv")
AxisD = AxisD.set_index(pd.to_datetime(AxisD['date']))
AxisD_drop = AxisD.drop(columns=['date'])
AxisD_hr_mean = AxisD_drop.resample(tframe).mean()

AxisF = pd.read_csv(Vindobona + "hcho_F_1.6.2017-31.5.2020.csv")
AxisF = AxisF.set_index(pd.to_datetime(AxisF['date']))
AxisF_drop = AxisF.drop(columns=['date'])
AxisF_hr_mean = AxisF_drop.resample(tframe).mean()

AxisG = pd.read_csv(Vindobona + "hcho_G_1.6.2017-31.5.2020.csv")
AxisG = AxisG.set_index(pd.to_datetime(AxisG['date']))
AxisG_drop = AxisG.drop(columns=['date'])
AxisG_hr_mean = AxisG_drop.resample(tframe).mean()
#df.groupby('a').resample('3T').sum()
#print(AxisG_hr_mean.dt.dayofweek)


Luftmessnetz = "/windata/GOOGLEDrive/DATA/obs_point/chem/Luftmessnetz/"
"""
LUFTMESSNETZ DATASET 2 - ONLY JAN-APRIL:

NO2_HMW = pd.read_csv(Luftmessnetz + "NO2_HMW_01-01-2017_19-04-2020.txt", delimiter=' ', parse_dates=True)                                                      #date parsed correct, missing time
timeaxis_NO2 = pd.to_datetime(NO2_HMW['date'].apply(str) + ' ' + NO2_HMW['time(MEZ)'])
#print(NO2_HMW[0::2])   #only 11280 values! but 57840 rows
#print(NO2_HMW.head, NO2_HMW.date , NO2_HMW.info())
#no2_meas_ppb = no2_meas.mul(1.88)
NO_HMW = pd.read_csv(Luftmessnetz + "NO_HMW_01-01-2017_19-04-2020.txt", delimiter=' ')
O3_HMW = pd.read_csv(Luftmessnetz + "O3_HMW_01-01-2017_19-04-2020.txt", delimiter=' ')
#PM10_HMW = pd.read_csv(Luftmessnetz + "PM10_HMW_01-01-2017_19-04-2020.txt", delimiter=' ')
#PM25_HMW = pd.read_csv(Luftmessnetz + "PM25_HMW_01-01-2017_19-04-2020.txt", delimiter=' ')
#timeaxis_PM10 = pd.to_datetime(PM10_HMW['date'].apply(str) + ' ' + PM10_HMW['time(MEZ)'])
"""
GL_SMW = pd.read_csv(Luftmessnetz + "GL_SMW_01-01-2017-26-04-2020.txt", delimiter=' ', parse_dates=True)
RR1H_SMW = pd.read_csv(Luftmessnetz + "RR1H_SMW_01-01-2017-26-04-2020.txt", delimiter=' ')
T2M_SMW = pd.read_csv(Luftmessnetz + "T2M_SMW_01-01-2017-26-04-2020.txt", delimiter=' ')
UU_SMW = pd.read_csv(Luftmessnetz + "UU_SMW_01-01-2017-26-04-2020.txt", delimiter=' ')
VV_SMW = pd.read_csv(Luftmessnetz + "VV_SMW_01-01-2017-26-04-2020.txt", delimiter=' ')
#sites = pd.read_csv(Luftmessnetz + "sites.txt", delimiter = ' ') # "STATION"
timeaxis_met = pd.to_datetime(GL_SMW['date'].apply(str) + ' ' + GL_SMW['time(MEZ)'])  #print(len(timeaxis_met),len(GL_SMW)) ... 11448 11448

#diff = len(GL_SMW[1:]) - len(NO2_HMW[1::2])
#print(len(NO2_HMW[1::2]))
#print(len(GL_SMW[:-diff]))

#both starting at: 1-1-2017 01:00
#print(len(NO2_HMW[1::2]))
#print(len(timeaxis_NO2[1::2]))
#print(len(GL_SMW["STEF"][1:-diff]))
#print(len(timeaxis_met[1:-diff]))

"""
try:
    fig = plt.figure()
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    ax1.plot(timeaxis_NO2[1::2], NO2_HMW["STEF"][1::2], color='blue', linestyle='none', marker='o', label="no2_obs")
    ax1.plot(timeaxis_NO[1::2], NO_HMW["STEF"][1::2], color='pink', linestyle='dotted', label="no_obs")
    ax1.plot(timeaxis_O3[1::2], O3_HMW["STEF"][1::2], color='violet', linestyle='dotted', label="o3_obs")
    #plt.plot(timeaxis_PM10[0::2], PM10_HMW["STEF"][0::2], color='orange', linestyle='dotted', label="pm10_obs")
    #plt.plot(timeaxis_PM10[0::2], PM25_HMW["STEF"][0::2], color='red', linestyle='dotted', label="pm25_obs")
    ax1.legend(loc='upper left')
    ax1.set_ylabel("ug m3", size="medium")

   # ax2.plot(timeaxis_met[1:-diff], GL_SMW["STEF"][1:-diff], color='yellow', label="glob_obs")
   # ax2.legend(loc='upper right')
   # ax2.set_ylabel("W m-2", size="medium")
    #plt.plot(timeaxis_met[0::2], RR1H_SMW["STEF"][0::2], color='black', label="rain_obs")
    #plt.plot(timeaxis_met[0::2], T2M_SMW["STEF"][0::2], color='red', label="o3_obs")
    #plt.plot(timeaxis_met[0::2], UU_SMW["STEF"][0::2], color='light blue', label="o3_obs")
    #plt.plot(timeaxis_met[0::2], VV_SMW["STEF"][0::2], color='blue', label="o3_obs")

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
"""


"""
LUFTMESSNETZ DATASET 1 - WHOLE YEARS:
"""
NO2_HMW = pd.read_csv(Luftmessnetz + "NO2_HMW_2017-19.4.2020.csv", parse_dates=["timestamp.MEZ"]) #start: 0      01-01-2017 00:30
NO_HMW = pd.read_csv(Luftmessnetz + "NO_HMW_2017-19.4.2020.csv", parse_dates=True)
O3_HMW = pd.read_csv(Luftmessnetz + "O3_HMW_1.1.2015_19.4.2020.csv", parse_dates=True) #start: 0      01-01-2015 00:30
#print(NO2_HMW["timestamp.MEZ"])
timeaxis_NO2 = pd.to_datetime(NO2_HMW["timestamp.MEZ"])
timeaxis_NO = pd.to_datetime(NO_HMW["timestamp.MEZ"])
timeaxis_O3 = pd.to_datetime(O3_HMW["Timestamp..MEZ."])

Spartacus_Tmin = "/windata/GOOGLEDrive/DATA/obs_point/met/Spartacus/tmin1990.2019_o3_stat.txt" # in degC
Apolis_GS = "/windata/GOOGLEDrive/DATA/obs_point/met/Apolis/apolis1990.2019_o3_stat.txt" # kWh/m2 (Tagessumme Globalstrahlung)
#Und hier der poly-fit für die Strahlungsdaten –„x“ ist Tag im Jahr (von 1 -> 365 (366)) clear sky , wenn mind 90% der max. Strahlung
## calculate 90% of max globrad -> threshold
#thres.glob <- (1.25e-12*x^5+ 7.38E-09*x^4 - 5.365E-06*x^3 + 0.000926*x^2 - 0.00036*x + 1.08)*0.9

"""FIG1 monthly mean diurnal cycles"""
"""
fig, ax = plt.subplots(1, figsize=(12,6))

#dataframe['Month'] = dataframe.index.map(lambda x: x.strftime("%m"))
#dataframe['Time'] = dataframe.index.map(lambda x: x.strftime("%H:%M"))
AxisA_hr_mean['Month'] = AxisA_hr_mean.index.month
AxisA_hr_mean['Time'] = AxisA_hr_mean.index.time

pd.plotting.register_matplotlib_converters()

colors = ["k","gray","silver","greenyellow","chartreuse","green","yellow","orange","red","sandybrown","goldenrod","saddlebrown", "grey"]

AxisA_monthly_mean = []
for month in AxisA_hr_mean['Month'].unique():
    df = AxisA_hr_mean.loc[AxisA_hr_mean['Month'] == month]
    df = df.groupby('Time').describe() #.mean()
    #print(df['HCHO']['mean'])       #12x24h ok!
    #print(df.index) #12x24h ok!
    ax.plot(df['HCHO']['mean'], linewidth=2.0, color=colors[month], label = month)
    AxisA_monthly_mean.append(df['HCHO']['mean'])
ax.legend()

#print(AxisA_monthly_mean)


ticks = ax.get_xticks()
ax.set_xticks(np.linspace(ticks[0], d.date2num(d.num2date(ticks[-1]) + dt.timedelta(hours=1)), 5))
ax.set_xticks(np.linspace(ticks[0], d.date2num(d.num2date(ticks[-1]) + dt.timedelta(hours=1)), 25), minor=True)
#plt.show()
"""
"""FIG 1 END"""


"""FIG 2 scatter plot """
"""
print(len(AxisD_hr_mean[:-1004]), len(timeaxis_NO2[7255::2]))  #JD 31.Mai: 151*(24*2 half hours)=7248
print(AxisD_hr_mean[:-1004])
print(timeaxis_NO2[7255::2])
try:
    fig = plt.figure()
    #plt.scatter(AxisA_hr_mean[:-1004], NO2_HMW["STEF"][7255::2], color='navy', label="hcho_obs_A vs. NO2_STEF")
    plt.scatter(AxisD_hr_mean[:-1003], NO2_HMW["STEF"][7255::2], color='navy', label="hcho_obs_D vs. NO2_STEF")
    plt.legend(loc='upper left')
    plt.show()
except:
    print("Oops!", sys.exc_info()[0], "occured.")
    pass
"""
"""FIG 2 END"""

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

