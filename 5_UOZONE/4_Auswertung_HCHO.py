# -*- coding: utf-8 -*-
__author__ = 'lnx'
import pandas as pd
import matplotlib.pyplot as plt
import sys
from datetime import datetime
from datetime import timedelta
"""
Liebe Heidi,
In der BOKUbox sind die pm, NO, NO2, O3, HCHO (in DSCD) und met Daten 1.1.2017 – 04/2020-  zusätzlich Tmin in °C (Spartacus) und APOLIS in kWh/m2 (Tagessumme Globalstrahlung) für die O3-Stationen, denn die ZAMG hat nur Jan – April hergegeben. Wenn du komplette*.nc files Spartacus oder Apolis brauchst, dann  bitte einfach melden habe Daten von 1990 – 2019.
Und hier der poly-fit für die Strahlungsdaten –„x“ ist Tag im Jahr (von 1 -> 365 (366)) clear sky , wenn mind 90% der max. Strahlung

# calculate 90% of max globrad -> threshold
thres.glob <- (1.25e-12*x^5+ 7.38E-09*x^4 - 5.365E-06*x^3 + 0.000926*x^2 - 0.00036*x + 1.08)*0.9
LG Monika
"""


Vindobona = "/windata/GOOGLEDrive/DATA/remote/ground/maxdoas/Monika/"  # in DSCD
AxisA = Vindobona + "hcho_A_1.5.2017-31.5.2020.csv"
AxisB = Vindobona + "hcho_B_1.5.2017-31.5.2020.csv"
AxisC = Vindobona + "hcho_C_1.5.2017-31.5.2020.csv"
AxisD = Vindobona + "hcho_D_1.5.2017-31.5.2020.csv"
AxisF = Vindobona + "hcho_F_1.5.2017-31.5.2020.csv"
AxisG = Vindobona + "hcho_G_1.5.2017-31.5.2020.csv"

Luftmessnetz = "/windata/GOOGLEDrive/DATA/obs_point/chem/Luftmessnetz/"
#df = pd.DataFrame(np.nan, columns=pd.date_range('00:00', '23:50', freq='10min'), index=pd.date_range('2017-10-29', '2018-03-24'))
d1 = datetime(2017, 1, 1, 00, 30)
d2 = datetime(2020, 4, 19, 23, 30)
index = pd.date_range(d1, d2)

NO2_HMW = pd.read_csv(Luftmessnetz + "NO2_HMW_01-01-2017_19-04-2020.txt", delimiter=' ')#, parse_dates=[["date", "time(MEZ)"]])
#print(NO2_HMW.head)
#NO2_STEF = NO2_HMW["STEF"][0::2]
NO_HMW = pd.read_csv(Luftmessnetz + "NO_HMW_01-01-2017_19-04-2020.txt", delimiter=' ')
O3_HMW = pd.read_csv(Luftmessnetz + "O3_HMW_01-01-2017_19-04-2020.txt", delimiter=' ')
PM10_HMW = pd.read_csv(Luftmessnetz + "PM10_HMW_01-01-2017_19-04-2020.txt", delimiter=' ')
PM25_HMW = pd.read_csv(Luftmessnetz + "PM25_HMW_01-01-2017_19-04-2020.txt", delimiter=' ')

GL_SMW = pd.read_csv(Luftmessnetz + "GL_SMW_01-01-2017-26-04-2020.txt", delimiter=' ')
RR1H_SMW = pd.read_csv(Luftmessnetz + "RR1H_SMW_01-01-2017-26-04-2020.txt", delimiter=' ')
T2M_SMW = pd.read_csv(Luftmessnetz + "T2M_SMW_01-01-2017-26-04-2020.txt", delimiter=' ')
UU_SMW = pd.read_csv(Luftmessnetz + "UU_SMW_01-01-2017-26-04-2020.txt", delimiter=' ')
VV_SMW = pd.read_csv(Luftmessnetz + "VV_SMW_01-01-2017-26-04-2020.txt", delimiter=' ')
#sites = pd.read_csv(Luftmessnetz + "sites.txt", delimiter = ' ') # "STATION"

#no2_meas_ppb = no2_meas.mul(1.88)
#no2_meas2b = no2_meas2[0::2]

Spartacus_Tmin = "/windata/GOOGLEDrive/DATA/obs_point/met/Spartacus/tmin1990.2019_o3_stat.txt" # in degC

Apolis_GS = "/windata/GOOGLEDrive/DATA/obs_point/met/Apolis/apolis1990.2019_o3_stat.txt" # kWh/m2 (Tagessumme Globalstrahlung)
#Und hier der poly-fit für die Strahlungsdaten –„x“ ist Tag im Jahr (von 1 -> 365 (366)) clear sky , wenn mind 90% der max. Strahlung
## calculate 90% of max globrad -> threshold
#thres.glob <- (1.25e-12*x^5+ 7.38E-09*x^4 - 5.365E-06*x^3 + 0.000926*x^2 - 0.00036*x + 1.08)*0.9

x = range(len(NO2_HMW["STEF"][0::2]))
print(x)
#print(type(NO2_STEF.values))
#exit()
print(type(NO2_HMW))

d1 = datetime(2017, 1, 1, 00, 30)
d2 = datetime(2020, 4, 19, 23, 30)
#delta = d2 - d1

#timeaxis = pd.date_range(start="2017-01-01", end="2020-04-19", freq='60min')#, periods=24)
timeaxis = pd.date_range(start=d1, end=d2, freq='60min')#, periods=24)


#timeaxis = pd.to_datetime(NO2_HMW["date"] + " " + NO2_HMW["time(MEZ)"])
print(timeaxis)
print(type(timeaxis))
print(len(timeaxis))
#exit()

try:
    fig = plt.figure()
    plt.plot(timeaxis, NO2_HMW["STEF"][0::2], color='blue', label="no2_obs")
    plt.plot(timeaxis, NO_HMW["STEF"][0::2], color='green', label="no_obs")
    plt.plot(timeaxis, O3_HMW["STEF"][0::2], color='violet', label="o3_obs")
    plt.plot(timeaxis, PM10_HMW["STEF"][0::2], color='orange', label="pm10_obs")
    plt.plot(timeaxis, PM25_HMW["STEF"][0::2], color='red', label="pm25_obs")

    plt.xlabel("hours")
    plt.ylabel("ug m3", size="medium")
    #ax2.set_ylabel("ppb", size="medium")
    plt.legend(loc='upper left')
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