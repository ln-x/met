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

#def loadfile(foldername, filename, begin, dayofmeas):
def loadfile(foldername, filename, hcho_date):
    #print(dayofmeas)
    timeaxis = []
    sza = []
    hOPL = []
    h_eff = []
    hcho = []
    file = foldername+'/'+filename
    with open(file,"r") as f:    #Einlesen des Files in eine Liste
        alldata = f.readlines()
        splitdata = []  # splitlistcomp = [i.split() for i in data]
        for i in alldata:
            splitdata.append([float(x) for x in i.split()])
        for j in splitdata:
           # TODO if j[2]  horizontal optical path length <25 or >75 percentil
           if j[1] < 75:  #FILTER: only take values where Solar zenith is above 75°
                hour, frac = str(j[0]).split('.')  # split bei '.' #TODO make preciser
                minute = (int(frac[:2])/100)*60
                #date_time = begin + datetime.timedelta(days=dayofmeas - 1) \
                #       + datetime.timedelta(hours=int(hour)) + datetime.timedelta(minutes=minute) # + datetime.timedelta(seconds=second)
                date_time = hcho_date + datetime.timedelta(hours=int(hour)) + datetime.timedelta(minutes=minute) # + datetime.timedelta(seconds=second)
                timeaxis.append(date_time)
                sza.append(j[1])
                hOPL.append(j[2])
                h_eff.append(j[3])
                hcho.append(j[4])
           else:
               pass
    hcho_dft = pd.DataFrame({'datetime': timeaxis, 'hcho': hcho, 'sza': sza,'hOPL': hOPL})
    hcho_dft['datetime'] = pd.to_datetime(hcho_dft['datetime'])
    hcho_dft = hcho_dft.set_index(['datetime'])
    return(hcho_dft)

def loadfileALL(foldername,axis,begin):
    files = os.listdir(foldername)
    appended_data1 = []
    totalmeasdays = [*range(1,(len(files)+1),1)]

    for i in range(len(files)):
        #splitlistcomp = [j.split() for j in files[i]]
        day = str(files[i][4:6])# splitlistcomp[3:4]
        month = str(files[i][2:4])#splitlistcomp[2:3]
        year = "20"+ str(files[i][0:2]) #splitlistcomp[:2]
        print(day,month,year)
        hcho_date = datetime.datetime(year=int(year),month=int(month), day=int(day))
        print(hcho_date)
        #exit()
        dayofmeas = totalmeasdays[i]
        #data_hcho = loadfile(foldername=foldername, filename=files[i], begin=begin,dayofmeas=dayofmeas)
        data_hcho = loadfile(foldername=foldername, filename=files[i], hcho_date=hcho_date)
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
    hOPL_25 = hcho['hOPL'].quantile(q=0.25, interpolation='linear')
    hOPL_75 = hcho['hOPL'].quantile(q=0.75, interpolation='linear')
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

