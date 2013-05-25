# coding=utf-8
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

import datetime as dt
import matplotlib.pyplot as plt
import numpy
import pickle

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

times = list(set([day.time() for day in alldata.keys()]))
times.sort()  # die Liste 'times' sortieren

mittelwert_dict = AutoVivification()  # Anlegen eines Autovivification dictionaries für Mittelwert - Ergebnisse

for t in times:   # Interieren über Liste 'times'
    #print t
    # Iterieren über alle Zeitpunkte in 'alldata' und vergleich mit Zeitpunkten in Liste 'times':
    zeitpunkte = [zeitpunkt for zeitpunkt in alldata.keys() if zeitpunkt.time() == t]
    #print zeitpunkte
    values = []
    # Iterieren über alle Elemente in Zeitpunkte und wenn wert für a4 >0 dann hinzufügen zu Liste, über die gemittelt
    # wird, Mittelwert wird für den entsprechenden Zeitpunkt in dict. mittelwert eingeschrieben
    for zeit in zeitpunkte:
        wert = safenumber(alldata[zeit]['a4'])
        if wert > 0:
            values.append(wert)
    #print values
    average = numpy.mean(values)
    #print average
    mittelwert_dict[t] = average


keysliste = mittelwert_dict.keys()
keysliste.sort()

plot_x = []
plot_y = []
dummydatetime = dt.datetime
for key in keysliste:
    print key, mittelwert_dict[key]
    plot_x.append(dt.datetime(2013, 1, 1, key.hour, key.minute))
    plot_y.append(mittelwert_dict[key])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot_date(plot_x, plot_y, color='orange', label='ext')
fig.autofmt_xdate()
plt.show()

plt.legend()
