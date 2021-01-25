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
import BOKUMet_Data

BOKUMetData = BOKUMet_Data.BOKUMet()
#print(BOKUMetData["AT"])

isLowWS = BOKUMetData["WS"] < 0.3  #m/s
LowWSdays = BOKUMetData[isLowWS]
print(LowWSdays.shape)
print(LowWSdays)

juliandays = range(365)
thres_glob = []

#APOLIS in kWh/m2 (Tagessumme Globalstrahlung) !!
#x = 1
#thres_glob = ((1.25e-12)*(x**5)+ (7.38e-9)*(x**4) - (5.365e-6)*(x**3) + 0.000926*(x**2) - 0.00036*x + 1.08)*0.9
#print(thres_glob)

for x in juliandays:
    thres_glob.append(((1.25e-12)*(x**5)+ (7.38e-9)*(x**4) - (5.365e-6)*(x**3) + 0.000926*(x**2) - 0.00036*x + 1.08)*0.9)
    #min 90% der max. Strahlung (von Monika, Quelle? Für welchen Punkt?)
print(thres_glob)

#isLowWS_Sun



exit()

"""
Liebe Heidi,
In der BOKUbox sind die pm, NO, NO2, O3, HCHO (in DSCD) und met Daten 1.1.2017 – 04/2020-  zusätzlich Tmin in °C (Spartacus) und APOLIS in kWh/m2 (Tagessumme Globalstrahlung) für die O3-Stationen, denn die ZAMG hat nur Jan – April hergegeben. Wenn du komplette*.nc files Spartacus oder Apolis brauchst, dann  bitte einfach melden habe Daten von 1990 – 2019.

"""

Vindobona = "/windata/GOOGLEDrive/DATA/remote/ground/maxdoas/Monika/"  # in DSCD
tframe = '60T'
AxisD = pd.read_csv(Vindobona + "hcho_D_1.6.2017-31.5.2020.csv")
AxisD = AxisD.set_index(pd.to_datetime(AxisD['date']))
AxisD_drop = AxisD.drop(columns=['date'])
AxisD_hr_mean = AxisD_drop.resample(tframe).mean()
#df.groupby('a').resample('3T').sum()
#print(AxisG_hr_mean.dt.dayofweek)

AxisK = pd.read_csv(Vindobona + "hcho_K_1.6.2017-31.5.2020.csv")#, parse_dates=["date"])
AxisK = AxisK.set_index(pd.to_datetime(AxisK['date']))
AxisK_drop = AxisK.drop(columns=['date'])
AxisK_hr_mean = AxisK_drop.resample(tframe).mean()






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
    print("Oops!", sys.exc_info()[0], "occurred.")
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

