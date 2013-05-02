# coding=utf-8
from hs_scripts import hs_loader
from hs_scripts import hs_cdataloader

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

filename = "/home/lnx/PycharmProjects/Messdatenauswertung/HStest/v808_20130429_c10_v01_f05/Temp_H2O.txt"
thedata3 = hs_loader.loadfile(filename=filename)
print 'loaded: ', thedata3

#date_time = [i[0] for i in thedata3]
c1 = [i[1] for i in thedata3]
c2 = [i[2] for i in thedata3]
c3 = [i[3] for i in thedata3]
c4 = [i[4] for i in thedata3]

filename = "/home/lnx/PycharmProjects/Messdatenauswertung/HStest/v808_20130429_c10_v01_f30/Temp_H2O.txt"
thedata4 = hs_loader.loadfile(filename=filename)
print 'loaded: ', thedata4

#date_time = [i[0] for i in thedata4]
d1 = [i[1] for i in thedata4]
d2 = [i[2] for i in thedata4]
d3 = [i[3] for i in thedata4]
d4 = [i[4] for i in thedata4]

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

C1 = [m - n for m,n in zip(c1,eld)] #zwei Listen subtrahieren
C2 = [m - n for m,n in zip(c2,eld)]
C3 = [m - n for m,n in zip(c3,eld)]
C4 = [m - n for m,n in zip(c4,eld)]

D1 = [m - n for m,n in zip(d1,eld)] #zwei Listen subtrahieren
D2 = [m - n for m,n in zip(d2,eld)]
D3 = [m - n for m,n in zip(d3,eld)]
D4 = [m - n for m,n in zip(d4,eld)]

fig = plt.figure()


ax = fig.add_subplot(221)
ax.plot(date_time, X1, color='red', lw=0.5)
ax.plot(date_time, X2, color='darkred', lw=0.5)
ax.plot(date_time, X3, color='violet', lw=0.5)
ax.plot(date_time, X4, color='darkblue', lw=0.5)
#ax.plot(date_time, eld, color='black', lw=0.5)
#ax.plot(graphiken['RO'][12], color='blue', lw=0.5)
#plt.axis([0, 15, -15, 15])
#plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
#plt.text(20, 18, 'I', fontsize=20)
plt.ylabel('water temperature[degC], cloudiness = 0%')
#plt.ylim(-15,15)

ax = fig.add_subplot(222)
ax.plot(date_time, B1, color='red', lw=0.5)
ax.plot(date_time, B2, color='darkred', lw=0.5)
ax.plot(date_time, B3, color='violet', lw=0.5)
ax.plot(date_time, B4, color='darkblue', lw=0.5)
#ax.plot(date_time, eld, color='black', lw=0.5)
# plt.text(20, 18, 'II', fontsize=20)
# plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
# plt.axis([1, 23, 5, 20])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


ax = fig.add_subplot(223)
ax.plot(date_time, C1, color='red', lw=0.5)
ax.plot(date_time, C2, color='darkred', lw=0.5)
ax.plot(date_time, C3, color='violet', lw=0.5)
ax.plot(date_time, C4, color='darkblue', lw=0.5)
#ax.plot(date_time, eld, color='black', lw=0.5)
# plt.axis([1, 23, 5, 20])
# plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
# plt.text(20, 18, 'III', fontsize=20)
plt.ylabel('cloudiness = 100%')
plt.xlabel('time[h], flow = 0.5cms')

ax = fig.add_subplot(224)
ax.plot(date_time, D1, color='red', lw=0.5, label='0.65')
ax.plot(date_time, D2, color='darkred', lw=0.5, label='0.40')
ax.plot(date_time, D3, color='violet', lw=0.5, label='0.15')
ax.plot(date_time, D4, color='darkblue', lw=0.5, label='0.00')
#ax.plot(date_time, eld, color='black', lw=0.5, label='meas')
# plt.axis([1, 23, 5, 20])
# plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
# plt.text(20, 18, 'IV', fontsize=20)
fig.autofmt_xdate()
plt.xlabel('time[h], flow = 3cms')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title="km")


#plt.legend()
# fig.savefig('albedo.png')
plt.show()