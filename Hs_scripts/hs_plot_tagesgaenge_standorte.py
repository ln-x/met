# coding=utf-8
from Hs_scripts import hs9_loader
from Hs_scripts import hs_cdataloader

__author__ = 'lnx'
import matplotlib.pyplot as plt

filename = "C:\heatsource900b5_339\win32\Test\outputfiles\Temp_H2O.txt"
thedata = hs9_loader.loadfile(filename=filename)
print 'loaded: ', thedata

date_time = [i[0] for i in thedata]
x1 = [i[10] for i in thedata] #km 88.5 Hundsmühlbach
x2 = [i[18] for i in thedata] #km 84.5 Tauchenbach
x3 = [i[28] for i in thedata] #km 79.5 Sinnersdorf
x4 = [i[49] for i in thedata] #km 69 Riedlingsdorf
#x4 = [i[58] for i in thedata] #km 64.5 ober Oberwart
#x5 = [i[64] for i in thedata] #km 61.5 unter Oberwart
#x1 = [i[66] for i in thedata] #km 60.5 Unterwart
#x2 = [i[76] for i in thedata] #km 55.5 Jabbing 1
#x3 = [i[79] for i in thedata] #km 54 Jabbing 2+3
#x4 = [i[85] for i in thedata] #km 51 Jabbing 4
#x4 = [i[94] for i in thedata] #km 46.5 Zickenbach 1+2
#x4 = [i[98] for i in thedata] #km 44.5 Badersdorf
#x4 = [i[106] for i in thedata] #km 40.5 Woppendorf
#x4 = [i[113] for i in thedata] #km 37 Burg (BioClic)
#x4 = [i[130] for i in thedata] #km 28.5 DeutschSchützen
#x4 = [i[140] for i in thedata] #km 23.5 Bildein Unterwasser
#x4 = [i[144] for i in thedata] #km 21.5 Eberau
#x4 = [i[154] for i in thedata] #km 16.5 Moschendorf

filename = "C:\heatsource900b5_339\win32\Test\outputfiles\Temp_H2O.txt"
thedata2 = hs9_loader.loadfile(filename=filename)
print 'loaded: ', thedata2

date_time = [i[0] for i in thedata2]
b1 = [i[66] for i in thedata] #km 60.5 Unterwart
b2 = [i[76] for i in thedata] #km 55.5 Jabbing 1
b3 = [i[79] for i in thedata] #km 54 Jabbing 2+3
b4 = [i[85] for i in thedata] #km 51 Jabbing 4


filename = "C:\heatsource900b5_339\win32\Test\outputfiles\Hyd_Hyp.txt"
thedata3 = hs9_loader.loadfile(filename=filename)
print 'loaded: ', thedata3

date_time = [i[0] for i in thedata2]
c1 = [i[94] for i in thedata] #km 46.5 Zickenbach 1+2
c2 = [i[98] for i in thedata] #km 44.5 Badersdorf
c3 = [i[106] for i in thedata] #km 40.5 Woppendorf
c4 = [i[113] for i in thedata] #km 37 Burg (BioClic)

filename = "C:\heatsource900b5_339\win32\Test\outputfiles\Hyd_Vel.txt"
thedata4 = hs9_loader.loadfile(filename=filename)
print 'loaded: ', thedata4

date_time = [i[0] for i in thedata4]
d1 = [i[130] for i in thedata] #km 28.5 DeutschSchützen
d2 = [i[140] for i in thedata] #km 23.5 Bildein Unterwasser
d3 = [i[144] for i in thedata] #km 21.5 Eberau
d4 = [i[154] for i in thedata] #km 16.5 Moschendorf


#filename = "/home/lnx/PycharmProjects/Messdatenauswertung/HStest/Continousdata_HS808_20130415.txt"
#thedata5 = hs_cdataloader.loadfile(filename=filename)
#print 'loaded: ', thedata5

# date_time2 = [i[0] for i in thedata5]
# e1 = [i[3] for i in thedata5]

# matches = list(set(date_time) & set(date_time2))
# matches.sort()
# for m in matches:
#     print(m)
#
#
# eld = []
# for d in matches:
#     index = date_time2.index(d)
#     eld.append(thedata5[index][2])
#     print index
#
# print eld
# e1 = [i[3] for i in thedata5]

fig = plt.figure()

ax = fig.add_subplot(221)
ax.set_title('HB, TB, SD, RD')
ax.plot(date_time, x1, color='red', lw=0.5)
ax.plot(date_time, x2, color='darkred', lw=0.5)
ax.plot(date_time, x3, color='violet', lw=0.5)
ax.plot(date_time, x4, color='darkblue', lw=0.5)
plt.ylabel('water temperature[degC]')
fig.autofmt_xdate()

ax = fig.add_subplot(222)
ax.set_title('UW, J1, J2+3, J4')
ax.plot(date_time, b1, color='red', lw=0.5)
ax.plot(date_time, b2, color='darkred', lw=0.5)
ax.plot(date_time, b3, color='violet', lw=0.5)
ax.plot(date_time, b4, color='darkblue', lw=0.5)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax = fig.add_subplot(223)
ax.set_title('ZB1+2, BD, WD, BG')
ax.plot(date_time, c1, color='red', lw=0.5)
ax.plot(date_time, c2, color='darkred', lw=0.5)
ax.plot(date_time, c3, color='violet', lw=0.5)
ax.plot(date_time, c4, color='darkblue', lw=0.5)
plt.xlabel('time[h]')

ax = fig.add_subplot(224)
ax.set_title('DS, BI_U, EB, MD')
ax.plot(date_time, d1, color='red', lw=0.5, label='1')
ax.plot(date_time, d2, color='darkred', lw=0.5,label='2')
ax.plot(date_time, d3, color='violet', lw=0.5, label='3')
ax.plot(date_time, d4, color='darkblue', lw=0.5, label='4')

fig.autofmt_xdate()
plt.xlabel('time[h]')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title="downstream")

#plt.legend()
# fig.savefig('albedo.png')
plt.show()