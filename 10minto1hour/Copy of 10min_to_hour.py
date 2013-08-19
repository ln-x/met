# coding=utf-8
import datetime
import csv

__author__ = 'lnx'

from library import csvtodict

filename = '/home/lnx/PycharmProjects/Messdatenauswertung/RAW/P1_20120522_20121102.csv'

mydata = csvtodict.CsvToDict(filename,"%m/%d/%Y %H:%M")

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


with open('P1_20120522_20121102_1h.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    spamwriter.writerow(['datetime','BV','GS','LS','LT','LF'])
    for t in times:
        spamwriter.writerow([t ,\
                        mydata[t]['BV'],\
                        mydata[t]['GS'],\
                        mydata[t]['LS'],\
                        mydata[t]['LT'],\
                        mydata[t]['LF']])



## special tasks for LRef:
## convert CGR4 to longwave:
#        t_body = POWER(0.0010295+(0.0002391*(LN(Resistance_thermistor*1000))+0.0000001568*POWER(LN(Resistance_termistor*1000),3)),-1)
#        r_lw = (volt_out/7.21)+(0.0000000567037*POWER(t_body,4))
## convert mV to shortwave:
#        r_sw = mV_sw*87.33
## convert RH 100 = 100% to 1= 100%
#        rh = rh_in/100


