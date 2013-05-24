# coding=utf-8
from Hs_scripts import hs_loader
from Hs_scripts import hs_cdataloader

__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np

filename = "/home/lnx/PycharmProjects/Messdatenauswertung/HStest/v808_20130429_c00_v01_f05/Temp_H2O.txt"
thedata = hs_loader.loadfile(filename=filename)
print 'loaded: ', thedata

date_time = [i[0] for i in thedata]
x1 = [i[1] for i in thedata]
x2 = [i[2] for i in thedata]
x3 = [i[3] for i in thedata]
x4 = [i[4] for i in thedata]

filename = "/home/lnx/PycharmProjects/Messdatenauswertung/HStest/v808_20130429_c00_v01_f30/Temp_H2O.txt"
thedata2 = hs_loader.loadfile(filename=filename)
print 'loaded: ', thedata2

#date_time = [i[0] for i in thedata2]
b1 = [i[1] for i in thedata2]
b2 = [i[2] for i in thedata2]
b3 = [i[3] for i in thedata2]
b4 = [i[4] for i in thedata2]

filename = "/home/lnx/PycharmProjects/Messdatenauswertung/HStest/Continousdata_HS808_20130415.txt"
thedata5 = hs_cdataloader.loadfile(filename=filename)
print 'loaded: ', thedata5

date_time2 = [i[0] for i in thedata5]
e1 = [i[3] for i in thedata5]

matches = list(set(date_time) & set(date_time2))
matches.sort()
for m in matches:
    print(m)


eld = []
for d in matches:
    index = date_time2.index(d)
    eld.append(thedata5[index][2])
    print index

print eld
e1 = [i[3] for i in thedata5]

# todo: umbauen und kürzen: np.array! e1 = np.array(e1)

X1 = [m - n for m,n in zip(x1,eld)] #zwei Listen subtrahieren
X2 = [m - n for m,n in zip(x2,eld)]
X3 = [m - n for m,n in zip(x3,eld)]
X4 = [m - n for m,n in zip(x4,eld)]

B1 = [m - n for m,n in zip(b1,eld)] #zwei Listen subtrahieren
B2 = [m - n for m,n in zip(b2,eld)]
B3 = [m - n for m,n in zip(b3,eld)]
B4 = [m - n for m,n in zip(b4,eld)]

#fig = plt.figure()

f, axarr = plt.subplots(2, sharex=True, sharey=True)

axarr[0].plot(date_time, X1, color='red', lw=0.5)
axarr[0].plot(date_time, X2, color='darkred', lw=0.5)
axarr[0].plot(date_time, X3, color='violet', lw=0.5)
axarr[0].plot(date_time, X4, color='darkblue', lw=0.5)
axarr[0].set_title('flow = 0.5cms')
#plt.grid(True)

axarr[1].plot(date_time, B1, color='red', lw=0.5, label='0.65')
axarr[1].plot(date_time, B2, color='darkred', lw=0.5, label='0.40')
axarr[1].plot(date_time, B3, color='violet', lw=0.5, label='0.15')
axarr[1].plot(date_time, B4, color='darkblue', lw=0.5, label='0.00')
axarr[1].set_title('flow = 3cms')
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title="km")
plt.ylabel('water temperature[degC]')
plt.xlabel('time[h]')
plt.ylim(-0.6,0.2)
f.autofmt_xdate()
#plt.grid(True)
#plt.axis([0, 15, -15, 15])
#plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))

# #plt.text(20, 18, 'I', fontsize=20)

plt.legend()
plt.show()