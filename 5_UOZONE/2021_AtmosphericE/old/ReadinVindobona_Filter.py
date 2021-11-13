# -*- coding: utf-8 -*-
__author__ = 'lnx'
import datetime
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

# 1.Spalte: UTC  - Zeit(UTC)
# 2.Spalte: SZA  - solar zenith angle[°]
# 3.Spalte: hOPL - horizontal optical path length[km]
# 4.Spalte: h_eff - effective height[km]
# 5.Spalte: HCHO  - averaged volume mixing ratios HCHO[ppb]

def loadfile(foldername, filename, julianday):
    timeaxis = []
    sza = []
    hOPL = []
    h_eff = []
    hcho = []
    converteddata = []
    converteddata_df = pd.DataFrame(converteddata)
    file = foldername+filename
    with open(file,"r") as f:    #Einlesen des Files in eine Liste
        #s = filename
        #months = s[2:4]
        #days = s[4:6]
        alldata = f.readlines()

        splitdata = []  # splitlistcomp = [i.split() for i in data]
        for i in alldata:
            splitdata.append([float(x) for x in i.split()])
            #splitdata.append(i.split())  # Splitten der Listenelemente   split(":")  Seperator ":"

        begin = datetime.datetime(2020, 1, 1, 0, 0, 0)
        for j in splitdata:
           # TODO if j[2]  horizontal optical path length <25 or >75 percentil
           if j[1] < 75:  #FILTER: only take values where Solar zenith is above 75°
                hour, frac = str(j[0]).split('.')  # split bei '.' #TODO make preciser
                minute = (int(frac[:2])/100)*60
                #second = (int(frac[2:4])/100)*60
                #print(hour, frac, minute, second)
                date_time = begin + datetime.timedelta(days=julianday - 1) \
                       + datetime.timedelta(hours=int(hour)) + datetime.timedelta(minutes=minute) # + datetime.timedelta(seconds=second)
                #print(date_time)
                timeaxis.append(date_time)
                sza.append(j[1])
                hOPL.append(j[2])
                h_eff.append(j[3])
                hcho.append(j[4])
                #print(j[0],j[1],j[2],j[3],j[4])

           else:
               pass
    hcho_dft = pd.DataFrame({'datetime': timeaxis, 'hcho': hcho, 'sza': sza,'hOPL': hOPL})
    hcho_dft['datetime'] = pd.to_datetime(hcho_dft['datetime'])
    hcho_dft = hcho_dft.set_index(['datetime'])

    return(hcho_dft)

def loadfileALL(foldername):
    #foldername = "/home/lnx/DATACHEM/StefanSchreier/2001_2004_DQ_91_HCHO_mixing_ratio/"
    files = os.listdir(foldername)
    #print files
    julianday = 0
    appended_data1 = []
    for i in files:
        julianday += 1
        #filename = "200101DQ_91_HCHO_mixing_ratio.asc"
        data_hcho = loadfile(foldername=foldername, filename=i, julianday=julianday)
        appended_data1.append(data_hcho)

    hcho = pd.concat(appended_data1)
#    FILTER hOPL on a three month basis:

#    APR1 = datetime.datetime(2020, 4, 1, 00, 00)
#    JUL1 = datetime.datetime(2020, 7, 1, 00, 00)
#    OCT1 = datetime.datetime(2020, 10, 1, 00, 00)

#    hOPL_JFM25 = hcho[:APR1]['hOPL'].quantile(q=0.25, interpolation='linear')
#    hOPL_JFM75 = hcho[:APR1]['hOPL'].quantile(q=0.75, interpolation='linear')
#    hOPL_AMJ25 = hcho[APR1:JUL1]['hOPL'].quantile(q=0.25, interpolation='linear')
#    hOPL_AMJ75 = hcho[APR1:JUL1]['hOPL'].quantile(q=0.75, interpolation='linear')
#    hOPL_JAS25 = hcho[JUL1:OCT1]['hOPL'].quantile(q=0.25, interpolation='linear')
#    hOPL_JAS75 = hcho[JUL1:OCT1]['hOPL'].quantile(q=0.75, interpolation='linear')
#    hOPL_OND25 = hcho[OCT1:]['hOPL'].quantile(q=0.25, interpolation='linear')
#    hOPL_OND75 = hcho[OCT1:]['hOPL'].quantile(q=0.75, interpolation='linear')

#    print(hOPL_JFM25, hOPL_JFM75)
#    print(hOPL_AMJ25, hOPL_AMJ75)
#    print(hOPL_JAS25, hOPL_JAS75)
#    print(hOPL_OND25, hOPL_OND75)

#    hcho1 = hcho[:APR1]
#    hcho2 = hcho[APR1:JUL1]
#    hcho3 = hcho[JUL1:OCT1]
#    hcho4 = hcho[OCT1:]

#    isJFM1 = (hcho1['hOPL'] < hOPL_JFM75) & (hcho1['hOPL'] < hOPL_JFM25)
#    hcho1_f = hcho1[isJFM1]
#    isAMJ1 = (hcho2['hOPL'] < hOPL_AMJ75) & (hcho2['hOPL'] < hOPL_AMJ25)
#    hcho2_f = hcho2[isAMJ1]
#    isJAS1 = (hcho3['hOPL'] < hOPL_JAS75) & (hcho3['hOPL'] < hOPL_JAS25)
#    hcho3_f = hcho3[isJAS1]
#    isOND1 = (hcho4['hOPL'] < hOPL_OND75) & (hcho4['hOPL'] < hOPL_OND25)
#    hcho4_f = hcho4[isOND1]

#    hcho_f = pd.concat([hcho1_f, hcho2_f, hcho3_f, hcho4_f])
    hOPL_25 = hcho['hOPL'].quantile(q=0.10, interpolation='linear')
    hOPL_75 = hcho['hOPL'].quantile(q=0.99, interpolation='linear')
    #print(hOPL_75,hOPL_25)
    #exit()
    isJFM1 = (hcho['hOPL'] < hOPL_75) & (hcho['hOPL'] > hOPL_25)
    hcho_f = hcho[isJFM1]
    hcho_dmax = hcho_f.resample('D').max()
    hcho_d = hcho_f.resample('D').mean()
    hcho_m = hcho_dmax.resample('M').mean()

    hcho_f.to_csv("/home/heidit/Downloads/hcho_f.csv")
    #print(hcho_m['hcho'])
    #print(hOPL_JFM)
    #print(hcho_f.median())
    #print(hcho_f.describe())
    return(hcho_d['hcho'], hcho_dmax['hcho'],hcho_m['hcho'])


if __name__ == '__main__':
    foldername = "/windata/Google Drive/DATA/remote/ground/maxdoas/MAXDOAS2020/DQ/"
    hcho_d, hcho_dmax, hcho_m = loadfileALL(foldername)
    #print(hcho_d)
