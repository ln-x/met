# -*- coding: utf-8 -*-
__author__ = 'lnx'
import pandas as pd
#from pandas.compat import StringIO
import matplotlib
import matplotlib.pyplot as plt
import sys
from datetime import datetime
from datetime import timedelta
import numpy as np
from matplotlib import dates as d
import datetime as dt
import pytz
from pytz import timezone

# DT = 'dewpoint temperature (degree C)'
# AT = 'air temperature (degree C)'
# RH = 'relative humidity (%)'
# GR = 'global radiation (W m^(-2))'
# WS = 'wind speed (km/h)'
# WD = 'wind direction (degree)'
# WS = 'wind speed - gust (km/h)'
# PS = 'precipitation (10^(-1) mm)'
# AP = 'air pressure (hPa)'

def BOKUMet():
    BOKUDachBASE = "/windata/DATA/obs_point/met/BOKU_Met_Dachstation/bokumet_"
    years = ['2009','2010','2011', '2012', '2013', '2014','2015','2016','2017','2018','2019','2020']
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    BOKUMetName = []
    BOKUMetpName = []
    for year in years:
        for month in months:
            BOKUMetName.append(BOKUDachBASE + year + month + "/bokumet_" + year + month + ".dat")
            BOKUMetpName.append(BOKUDachBASE + year + month + "/bokumet_ns_" + year + month + ".dat")
            #print(BOKUMetName, BOKUMetpName)

    frames = []

    for i in BOKUMetName:
        try:
            #print(i)
            File = pd.read_csv(i,
                sep="\s+",
                skiprows=1,
                na_values="-6999")

            File.columns = ["year", "month", "day", "hourMEZ", "min", "DT", "AT", "RH", "GR", "WS", "WD", "WSG", "PC", "AP"]
            File.insert(1, "DATE", pd.to_datetime(File[["year", "month", "day"]]) + pd.to_timedelta(File["hourMEZ"], unit='H') +
                    pd.to_timedelta(File["min"], unit='m'))

            #print(File['DATE'])
            # print(pytz.all_timezones)  #CET or Europe/Vienna or Etc/GMT+1
            #local = timezone('CET')
            #local_dt = local.localize(File['DATE'], is_dst=None)
            #utc_dt = local_dt.astimezone(pytz.utc)
            ## BOKUMetData.index = BOKUMetData.index.tz_localize(pytz.cet).tz_convert(utc)
            #print(local_dt['DATE'])
            #exit()
            File_dt = File.set_index(pd.to_datetime(File["DATE"]))
            File_dtd = File_dt.drop(columns=["year"])
            File_dtd1 = File_dtd.drop(columns=["month"])
            File_dtd2 = File_dtd1.drop(columns=["day"])
            File_dtd3 = File_dtd2.drop(columns=["hourMEZ"])
            File_dtd4 = File_dtd3.drop(columns=["min"])
            File_dtd5 = File_dtd4.drop(columns=["DATE"])

            #print(File_dtd5)
            frames.append(File_dtd5)

        except:
            #print("except")
            #print("Oops!", sys.exc_info()[0], "occurred.")
            pass

    result = pd.concat(frames)
    #result.replace('-6999', np.NaN)

    #print(result)

    return result

#BOKUMet()


'''

File = pd.read_csv("/windata/Google Drive/DATA/obs_point/met/BOKU_Met_Dachstation/bokumet_201706/bokumet_201706.dat",
                     sep="\s+",
                     skiprows=1)
                     #parse_dates=[['year','month','day','hour MEZ','min']])

File.columns = ["year", "month", "day", "hourMEZ", "min", "DT", "AT", "RH", "GR", "WS", "WD", "WDG", "PC", "AP"]
#DT = 'dewpoint temperature (degree C)'
#AT = 'air temperature (degree C)'
#RH = 'relative humidity (%)'
#GR = 'global radiation (W m^(-2))'
#WS = 'wind speed (km/h)'
#WD = 'wind direction (degree)'
#WS = 'wind speed - gust (km/h)'
#PS = 'precipitation (10^(-1) mm)'
#AP = 'air pressure (hPa)'

File.insert(1, "DATE", pd.to_datetime(File[["year","month","day"]]) + pd.to_timedelta(File["hourMEZ"],unit='H') + pd.to_timedelta(File["min"],unit='m'))
#print(File["DATE"])
#File_dt = File.set_index(pd.to_datetime(File[["year","month","day"]]))
File_dt = File.set_index(pd.to_datetime(File["DATE"]))
File_dtd = File_dt.drop(columns=["year"])
File_dtd1 = File_dtd.drop(columns=["month"])
File_dtd2 = File_dtd1.drop(columns=["day"])
File_dtd3 = File_dtd2.drop(columns=["hourMEZ"])
File_dtd4 = File_dtd3.drop(columns=["min"])
File_dtd5 = File_dtd4.drop(columns=["DATE"])

print(File_dtd5)

exit()
'''

