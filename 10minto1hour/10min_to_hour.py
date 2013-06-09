# coding=utf-8
import datetime
import csv

__author__ = 'lnx'

from library import csvtodict

filename = '/home/lnx/PycharmProjects/Messdatenauswertung/RAW/LRef_20120522_20120911.csv'

mydata = csvtodict.CsvToDict(filename,"%m/%d/%y %H:%M")

#print mydata.keys()                               # alle keys ausgeben (alle Zeitpunkte)

#print mydata[datetime.datetime(2012,7,1,3,30)]    # einen Zeitpunkt ausgeben

#for key in mydata.keys():                         # Globalstrahlung für alle Zeitpunkte ausgeben
#    print mydata[key]['GS']

times = [x for x in mydata.keys() if x.time().minute == 0]
times.sort()

allegs = [mydata[t]['GS'] for t in times ]         #
print allegs

#for t in times:                                    # alle Zeitpunkte zur vollen Stunde ausgeben
#    print t
#    gs = mydata[t]['GS']
#    print gs


with open('XXX.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    spamwriter.writerow(['datetime','BV','GS','LS','LT','LF'])
    for t in times:
        spamwriter.writerow([t ,\
                        mydata[t]['BV'],\
                        mydata[t]['GS'],\
                        mydata[t]['LS'],\
                        mydata[t]['LT'],\
                        mydata[t]['LF']])