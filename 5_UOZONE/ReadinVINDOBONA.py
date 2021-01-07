# -*- coding: utf-8 -*-
__author__ = 'lnx'
import datetime
import numpy as np
import os
import pandas as pd

# 1.Spalte: Zeit(UTC)
# 2.Spalte: solar zenith angle[°]
# 3.Spalte: horizontal optical path length[km]
# 4.Spalte: effective height[km]
# 5.Spalte: averaged volume mixing ratios HCHO[ppb]

def loadfile(foldername, filename, julianday):
    timeaxis = []
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
            splitdata.append(i.split())  # Splitten der Listenelemente   split(":")  Seperator ":"

        begin = datetime.datetime(2020, 1, 1, 0, 0, 0)
        for j in splitdata:
           hour = round(float(j[0]))
           #hour, frac = float(j[0]).split('.')  # split bei '.'
           #minute = round((float(frac)*60/100))
           date_time = begin + datetime.timedelta(days=julianday - 1) \
                       + datetime.timedelta(hours=int(hour)) #+ datetime.timedelta(minutes=minute)
           timeaxis.append(date_time)
           hcho.append(j[3])
    #converteddata = np.concatenate((np.array(timeaxis), np.array(hcho)), axis=1)
    timeaxis_df = pd.DataFrame(timeaxis)
    hcho_df = pd.DataFrame(hcho)
    converteddata_df = pd.concat([timeaxis_df, hcho_df], axis=1)
    #print converteddata_df.head()

    return converteddata_df.values

if __name__ == '__main__':
    foldername = "/home/lnx/DATACHEM/StefanSchreier/2001_2004_DQ_91_HCHO_mixing_ratio/"
    files = os.listdir(foldername)
    #print files
    julianday = 0
    for i in files:
        julianday += 1
        #filename = "200101DQ_91_HCHO_mixing_ratio.asc"
        thedata = loadfile(foldername=foldername, filename=i, julianday=julianday)
        #print 'loaded: '
        for d in thedata:
            print(d)
