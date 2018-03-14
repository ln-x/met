# coding=utf-8
from BIOCLIC import hs9_loader
from BIOCLIC import hs_cdataloader

__author__ = 'lnx'
import matplotlib.pyplot as plt

filename = "C:\heatsource900b5_339\MessdatenPinkaGSbisBG_20130702_09.txt"
mdata = hs9_loader.loadfile(filename=filename)
print 'loaded: ', mdata

date_time = [i[0] for i in mdata]
#x4 = [i[1] for i in thedata] #Messdaten Glaserstrasse
m1 = [i[3] for i in mdata] #Messdaten Hundsmühlbach
m2 = [i[5] for i in mdata] #Messdaten Tauchenbach
m3 = [i[8] for i in mdata] #Messdaten Sinnersdorf
m4 = [i[8] for i in mdata] #Messdaten Riedlingsdorf
m5 = [i[9] for i in mdata] #Messdaten ober Oberwart
m6 = [i[10] for i in mdata] #Messdaten unter Oberwart
m7 = [i[11] for i in mdata] #Messdaten Unterwart
m8 = [i[13] for i in mdata] #Messdaten Jabbing1
m9 = [i[14] for i in mdata] #Messdaten Jabbing2
m10 = [i[15] for i in mdata] #Messdaten Jabbing3
m11 = [i[16] for i in mdata] #Messdaten Zickenbach1
m12 = [i[17] for i in mdata] #Messdaten Zickenbach2
m13 = [i[18] for i in mdata] #Messdaten Badersdorf
m14 = [i[19] for i in mdata] #Messdaten Woppendorf
m15 = [i[20] for i in mdata] #Messdaten Burg
# m16 = [i[30] for i in mdata] #Messdaten Burg LF
# m17 = [i[31] for i in mdata] #Messdaten Eisenberg
# m18 = [i[32] for i in mdata] #Messdaten Deutsch-Kaltenbrunn Restwasser
# m19 = [i[33] for i in mdata] #Messdaten Deutsch-Kaltenbrunn Pegel
# m20 = [i[34] for i in mdata] #Messdaten Deutsch-Kaltenbrunn Unterwasser
# m21 = [i[35] for i in mdata] #Messdaten Bildein Pegel
# m22 = [i[36] for i in mdata] #Messdaten Bildein Unterwasser
# m23 = [i[38] for i in mdata] #Messdaten Bildein Restwasser
# m24 = [i[39] for i in mdata] #Messdaten Eberau
# m25 = [i[40] for i in mdata] #Messdaten Postrum
# m26 = [i[41] for i in mdata] #Messdaten Gaas - Rodlingbach
# m27 = [i[42] for i in mdata] #Messdaten Gaas
#m28 = [i[43] for i in mdata] #Messdaten Moschendorf

filename = "C:\heatsource900b5_339\win32\Test\outputfiles\Temp_H2O.txt"
thedata = hs9_loader.loadfile(filename=filename)
print 'loaded: ', thedata

date_time = [i[0] for i in thedata]
x1 = [i[10] for i in thedata] #km 88.5 Hundsmühlbach
x2 = [i[18] for i in thedata] #km 84.5 Tauchenbach
x3 = [i[28] for i in thedata] #km 79.5 Sinnersdorf
x4 = [i[49] for i in thedata] #km 69 Riedlingsdorf
#x5 = [i[58] for i in thedata] #km 64.5 ober Oberwart
#x6 = [i[64] for i in thedata] #km 61.5 unter Oberwart
x7 = [i[66] for i in thedata] #km 60.5 Unterwart
x8 = [i[76] for i in thedata] #km 55.5 Jabbing 1
x9 = [i[79] for i in thedata] #km 54 Jabbing 2+3
x10 = [i[85] for i in thedata] #km 51 Jabbing 4
x11 = [i[94] for i in thedata] #km 46.5 Zickenbach 1+2
x12 = [i[98] for i in thedata] #km 44.5 Badersdorf
x13 = [i[106] for i in thedata] #km 40.5 Woppendorf
x14 = [i[113] for i in thedata] #km 37 Burg (BioClic)
x15 = [i[130] for i in thedata] #km 28.5 DeutschSchützen
x16 = [i[140] for i in thedata] #km 23.5 Bildein Unterwasser
x17 = [i[144] for i in thedata] #km 21.5 Eberau
x18 = [i[154] for i in thedata] #km 16.5 Moschendorf

fig = plt.figure()

ax = fig.add_subplot(221)
ax.set_title('HB, TB, SD, RD')
ax.plot(date_time, x1, color='red', lw=0.2)      #S HB
ax.plot(date_time, x2, color='darkred', lw=0.2)  #S TB
ax.plot(date_time, x3, color='violet', lw=0.2)   #S SD
ax.plot(date_time, x4, color='darkblue', lw=0.2) #S RD
ax.plot(date_time, m1, color='red', lw=0.7)      #M HB
ax.plot(date_time, m2, color='darkred', lw=0.7)  #M TB
ax.plot(date_time, m3, color='violet', lw=0.7)   #M SD
ax.plot(date_time, m4, color='darkblue', lw=0.7) #M RD
plt.ylabel('water temperature[degC]')
fig.autofmt_xdate()

ax = fig.add_subplot(222)
ax.set_title('UW, J1, J2+3, J4')
ax.plot(date_time, x7, color='red', lw=0.2)
ax.plot(date_time, x8, color='darkred', lw=0.2)
ax.plot(date_time, x9, color='darkviolet', lw=0.2)
ax.plot(date_time, x10, color='darkblue', lw=0.2)
ax.plot(date_time, m7, color='red', lw=0.7)       #UW
ax.plot(date_time, m8, color='darkred', lw=0.7)   #J1
ax.plot(date_time, m9, color='darkviolet', lw=0.7)#J2
ax.plot(date_time, m10, color='darkblue', lw=0.7) #J3
fig.autofmt_xdate()

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax = fig.add_subplot(223)
ax.set_title('ZB1+2, BD, WD, BG')
ax.plot(date_time, x11, color='red', lw=0.5)
ax.plot(date_time, x12, color='darkred', lw=0.5)
ax.plot(date_time, x13, color='violet', lw=0.5)
ax.plot(date_time, x14, color='darkblue', lw=0.5)
ax.plot(date_time, m11, color='red', lw=0.7)        #Z1
ax.plot(date_time, m12, color='darkred', lw=0.7)    #Z2
ax.plot(date_time, m13, color='darkviolet', lw=0.7) #BD
ax.plot(date_time, m14, color='darkblue', lw=0.7)   #WO
ax.plot(date_time, m15, color='darkblue', lw=0.7)   #BG
plt.xlabel('time[h]')

ax = fig.add_subplot(224)
ax.set_title('DS, BI_U, EB, MD')
ax.plot(date_time, x15, color='red', lw=0.5, label='1')
ax.plot(date_time, x16, color='darkred', lw=0.5,label='2')
ax.plot(date_time, x17, color='violet', lw=0.5, label='3')
ax.plot(date_time, x18, color='darkblue', lw=0.5, label='4')
# ax.plot(date_time, m19, color='red', lw=0.7)        #DS_P
# ax.plot(date_time, m21, color='darkred', lw=0.7)    #BI_P
# ax.plot(date_time, m24, color='darkviolet', lw=0.7) #EB
# #ax.plot(date_time, m28, color='darkblue', lw=0.7)   #MO

fig.autofmt_xdate()
plt.xlabel('time[h]')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title="downstream")

plt.show()