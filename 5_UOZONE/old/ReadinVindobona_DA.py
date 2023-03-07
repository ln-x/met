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
                second = (int(frac[2:4])/100)*60
                #print(hour, frac, minute, second)
                date_time = begin + datetime.timedelta(days=julianday - 1) \
                       + datetime.timedelta(hours=int(hour)) + datetime.timedelta(minutes=minute) + datetime.timedelta(seconds=second)
                #print(date_time)
                timeaxis.append(date_time)
                sza.append(j[1])
                hOPL.append(j[2])
                h_eff.append(j[3])
                hcho.append(j[4])
                #print(j[0],j[1],j[2],j[3],j[4])

           else:
               pass
           #print(hour, frac)
    hcho_dft = pd.DataFrame({'datetime': timeaxis, 'hcho': hcho})
    hcho_dft['datetime'] = pd.to_datetime(hcho_dft['datetime'])
    hcho_dft = hcho_dft.set_index(['datetime'])
    #hcho_dft = pd.DataFrame(hcho).set_index(pd.to_datetime(timeaxis))
    hcho_dmax = hcho_dft.resample('D').max()
    hcho_da = hcho_dft.resample('D').mean()
    #print(hcho_dmax)
    #print(hcho_da)
    return(hcho_dmax, hcho_da)

if __name__ == '__main__':
    #foldername = "/home/lnx/DATACHEM/StefanSchreier/2001_2004_DQ_91_HCHO_mixing_ratio/"
    foldername = "/windata/Google Drive/DATA/remote/ground/maxdoas/MAXDOAS2020/DQ/"
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

