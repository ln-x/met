from __future__ import division
__author__ = 'lnx'
import datetime


def loadfile(filename):
    with open(filename,"r") as f:    #Einlesen des Files in eine Liste
        alldata = f.readlines()
        #print len(alldata)
        #print type(alldata)

    data = alldata[3:]  #Liste ab 4.Zeile der alten Liste - Beginn der Rohdaten

    splitdata = []       #splitlistcomp = [i.split() for i in data]
    for i in data:
        splitdata.append(i.split())  #Splitten der Listenelemente   split(":")  Seperator ":"

    converteddata = []
    begin = datetime.datetime(1900,1,1,0,0,0) #Startdatum
    for j in splitdata:
        tage,frac = j[0].split('.')
        zeit = round((float(frac)*24)/1000000)   # 500000 = 12h, 250000 = 6h, 041667 = 1h
        date_time = begin + datetime.timedelta(days=float(tage)) + datetime.timedelta(hours=zeit)
        x1 = float(j[1])
        x2 = float(j[2])
        x3 = float(j[3])
        x4 = float(j[4])
        converteddata.append([date_time,x1,x2,x3,x4])

#    for d in converteddata:
#        print d

    return converteddata


if __name__ == '__main__':
    filename = "/home/lnx/PycharmProjects/Messdatenauswertung/HStest/v808_20130411_c00_v01_f03/Heat_Cond.txt"
    thedata = loadfile(filename=filename)
    print 'loaded: ', thedata




