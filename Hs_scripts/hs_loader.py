from __future__ import division
__author__ = 'lnx'
import datetime


def loadfile(filename):
    with open(filename,"r") as f:    #Einlesen des Files in eine Liste
        alldata = f.readlines()
        #print len(alldata)
        #print type(alldata)

    name = alldata[1]
    header = alldata[6] #Liste mit Flusskilometern - Distance from Mouth
    data = alldata[6:]  #Liste ab 8.Zeile der alten Liste - Beginn der Rohdaten

    splitdata = []       #splitlistcomp = [i.split() for i in data]
    for i in data:
        splitdata.append(i.split())  #Splitten der Listenelemente   split(":")  Seperator ":"

    converteddata = []
    begin = datetime.datetime(1900,1,1,0,0,0) # Startdatum
    for j in splitdata:
        jliste = []
        # zeitstempel rechnen
        tage, frac = j[0].split('.')  # split bei '.'
        zeit = round((float(frac) * 24) / 1000000)   # 500000 = 12h, 250000 = 6h, 041667 = 1h
        date_time = begin + datetime.timedelta(days=float(tage)-2) \
                    + datetime.timedelta(hours=zeit)
        #print tage
        jliste.append(date_time)
        #werte wandeln
        for value in j[1:]:
            jliste.append(float(value))
        converteddata.append(jliste)

    return name, header, converteddata


if __name__ == '__main__':

    filename = "../HStest/v808_20130429_c00_v01_f05/Heat_SR4.txt"
    thedata = loadfile(filename=filename)
    print 'loaded: '
    for d in thedata:
        print d



