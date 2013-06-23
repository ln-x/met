# coding=utf-8
import datetime as dt
from math import exp
import matplotlib.pyplot as plt
import numpy
import pickle
from Sonnenstand_berechnen import CalcSolarPosition

# In diesem Skript werden Rohdaten aus einem Pickle-file eingelesen
# und die mittleren Tagesgänge berechnet und dargestellt

# x: Zeit, gs: Globalstrahlung auf Feld 13, 8: frei
# Referenzflaechen: 2: Blech, 7: Folie (schwarz), 10: Kies
# 1: 7cm Pflanzsubstrat Bauder ext. + 5cm EPS Drain
# 3: 10cm Pflanzsubstrat RE leicht + 2cm Drain Speicher
# 4: 10cm Pauliberg +10cm Agroperl
# 5: 15cm Pauliberg + 15cm Agroperl
# 6: ZinCo
# 9: 7cm Claylith organ. + 5cm Claylith Drain
# 11: 7cm Pflanzsubstrat RE leicht + 5cm LiaDrain
# 12: 12cm Pauliberg	SlrkW_Avg
# 14: 7cm Rath
# 15: 7cm Claylith organ. + 5cm Claylith Drain
# 16: 7cm Claylith organ. + 5cm Claylith Drain
# 17: 7cm Recycling Ziegel + 5cm Recycling Ziegel
# 18: 15cm Recycling Ziegel + 5cm Recycling Ziegel

filename = 'graph_albedo_dict.pickle'


def safenumber(value):  # verwenden statt 'float' -> auch bei NAN und ' ' kein Problem
    try:
        num = float(value)
    except ValueError:
        num = 0.0
    return num


class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


with open(filename, 'r') as f:  # Picklefile als 'alldata' laden (Typ: Autovivification Dictionary)
    alldata = pickle.load(f)

#for key in alldata_dict.keys():                   # Printstatement to better understand dictionaries
#    print alldata_dict[key]['gs']

#daylist = [day.time() for day in alldata.keys()]  # Version 1a (listcomprehension)

#daylist = []                   # Version 1b
#for x in alldata.keys():
#    daylist.append(x.time())

#timesset = set(daylist)        # Continue 1a or 1b
#times = list(timesset)

#  Set mit allen Zeitpunkten an einem Tag, die in 'alldata' vorkommen -> Konvertierung in Liste:
#  keys ist eine Methode von dictionaries, die eine Liste mit allen Schlüsseln in dictionaries ausgibt


#Einschränken des Zeitraumes
startdate = dt.date(2012, 6, 1)
enddate = dt.date(2012, 6, 30)
starttime = dt.time(5,0, 0)
endtime = dt.time(17, 0, 0)

a_zenith = 0.2

#actualtimestamp = dt.datetime.strptime(line[0], "%d.%m.%Y %H:%M")

times = list(set([day.time() for day in alldata.keys() if (starttime <= day.time() <= endtime and  startdate <= day.date() <= enddate) ]))
times.sort()  # die Liste 'times' sortieren
print 'times', times
mittelwert_s_dict = AutoVivification()  # Anlegen eines Autovivification dictionaries für Mittelwert - Ergebnisse
mittelwert_c_dict = AutoVivification()

for t in times:   # Interieren über Liste 'times'
    #print t
    # Iterieren über alle Zeitpunkte in 'alldata' und vergleich mit Zeitpunkten in Liste 'times':

    zeitpunkte = [zeitpunkt for zeitpunkt in alldata.keys() if (startdate <= zeitpunkt.date() <= enddate \
        and zeitpunkt.time() == t)]
    #print 'zeitpunkte' , zeitpunkte

    #print zeitpunkte
    values_s = []
    values_c = []
    # Iterieren über alle Elemente in Zeitpunkte und wenn wert für a4 >0 dann hinzufügen zu Liste, über die gemittelt
    # wird, Mittelwert wird für den entsprechenden Zeitpunkt in dict. mittelwert eingeschrieben
    for zeit in zeitpunkte:
        wert = safenumber(alldata[zeit]['a4'])
        #print wert
        if wert > 0.0:                   # Einschränken des Wertes für Tage mit vorherrschend direkter Sonnenstr.
            values_s.append(wert)
        elif 0 < wert < 0.0:             # Einschränken des Wertes für Tage mit vorherrschend diffuser Sonnestr.
            values_c.append(wert)
        #print values

    average_s = numpy.mean(values_s)
    average_c = numpy.mean(values_c)
    #print average
    mittelwert_s_dict[t] = average_s
    mittelwert_c_dict[t] = average_c

keysliste_s = mittelwert_s_dict.keys()
keysliste_s.sort()

keysliste_c = mittelwert_c_dict.keys()
keysliste_c.sort()

plot_x_s = []
plot_y_s = []
plot_x_c = []
plot_y_c = []
plot_a_calc = []

for t in times:  ##Berechnen des Albedos nach Formel von Patt + Paltridge
    tt = startdate.timetuple()
    Altitude, Zenith, Daytime, direction = CalcSolarPosition(47, 16, t.hour, t.minute, 0, 0, tt.tm_yday)
    #print Altitude, Zenith, Daytime, direction
    a_calc = a_zenith + (1- a_zenith) * exp(-0.1*(90 - Zenith))
    print t, tt.tm_yday, Zenith, a_calc
    plot_a_calc.append(a_calc)

#dummydatetime = dt.datetime
for key in keysliste_s:
    #print key, mittelwert_s_dict[key]
    plot_x_s.append(dt.datetime(2013, 1, 1, key.hour, key.minute))
    plot_y_s.append(mittelwert_s_dict[key])

for key in keysliste_c:
    print key, mittelwert_c_dict[key]
    plot_x_c.append(dt.datetime(2013, 1, 1, key.hour, key.minute))
    plot_y_c.append(mittelwert_c_dict[key])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(plot_x_s, plot_y_s, color="black", linestyle='solid', lw=0.8, label='sun,ext')
ax.plot(plot_x_c, plot_y_c, color="black", linestyle='dashed', lw=0.8, label='cloud,ext')
ax.plot(plot_x_s, plot_a_calc, color="black", linestyle='dotted', lw=0.8, label='calc')

fig.autofmt_xdate()
plt.show()
plt.legend()
