from __future__ import division
__author__ = 'lnx'
import datetime
import numpy as np


def loadfile(filename):
    with open(filename,"r") as f:    #Einlesen des Files in eine Liste
        alldata = f.readlines()
        #print len(alldata)
        #print type(alldata)

    data = alldata[7:]  #Liste ab 8.Zeile der alten Liste - Beginn der Rohdaten

    splitdata = []       #splitlistcomp = [i.split() for i in data]
    for i in data:
        splitdata.append(i.split())  #Splitten der Listenelemente   split(":")  Seperator ":"

    #print splitdata
    converteddata = []
    begin = datetime.datetime(1900,1,1,0,0,0) # Startdatum
    for j in splitdata:
        #print j[0]
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

    return converteddata

#diese Methode aus: wiki.scipy.org/Cookbook/InputOutput
def read_array(filename, dtype, separator=' '):
    cast = np.cast
    data = [[]for dummy in xrange(len(dtype))]
    for line in open(filename,'r'):
        fields = line.strip().split(separator)
        for i, number in enumerate(fields):
            data[i].append(number)
        for i in range(len(dtype)):
            data[i] = cast[dtype[i]]((data[i]))
        return np.rec.array(data, dtype=dtype)

    ##can be called with:
    #mydescr = N.dtype([('column1','int32'),('column2Name','uint32'),('co13',uint64'),('c4','float32')])
    #myrecarray = read_array('file.csv', mydescr)

def loadheader(filename):
    with open(filename,"r") as f:    #Einlesen des Files in eine Liste
        alldata = f.readlines()

    header = alldata[6]  #6.Zeile der alten Liste - Header
    #splitheader = []
    #for i in header:
    #    splitheader.append(i.split())  #FEHLER! macht jedes Zeichen! zu einem Listenelement
    #header = splitheader[1:]

    return header



if __name__ == '__main__':

    filename = "../HStest/v808_20130429_c00_v01_f05/Heat_SR4.txt"
    thedata = loadfile(filename=filename)
    print 'loaded: '
    for d in thedata:
        print d



