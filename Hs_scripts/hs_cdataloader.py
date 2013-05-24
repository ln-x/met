from __future__ import division

__author__ = 'lnx'
import datetime


def loadfile(filename):
    with open(filename, "r") as f:    # Einlesen des Files in eine Liste
        alldata = f.readlines()
        print len(alldata)
        print type(alldata)

    data = alldata[1:]  # Liste ab 2.Zeile der alten Liste - Beginn der Rohdaten

    splitdata = []       # splitlistcomp = [i.split() for i in data]
    for i in data:
        splitdata.append(i.split())  # Splitten der Listenelemente   split(":")  Seperator ":"

    converteddata = []
    for j in splitdata:
        jliste = []
        thedate = j[0] + ' ' + j[1]
        date_time = datetime.datetime.strptime(thedate, "%m/%d/%y %H:%M")
        jliste.append(date_time)
        #werte wandeln
        for value in j[2:]:
            jliste.append(float(value))
        converteddata.append(jliste)

    return converteddata


if __name__ == '__main__':
    filename = "../HStest/Continousdata_HS808_20130415.txt"
    thedata = loadfile(filename=filename)
    print 'loaded: '
    for d in thedata:
        print d
