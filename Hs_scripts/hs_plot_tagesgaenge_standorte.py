# coding=utf-8
from Hs_scripts import hs9_loader
from Hs_scripts import hs_cdataloader

__author__ = 'lnx'
import matplotlib.pyplot as plt

filename = "C:\heatsource900b5_339\MessdatenPinkaGSbisMO_20130701_0829.txt"
mdata = hs9_loader.loadfile(filename=filename)
#print 'loaded: ', mdata

date_time = [i[0] for i in mdata]
#m0 = [i[1] for i in thedata] #Messdaten Glaserstrasse
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
m16 = [i[30] for i in mdata] #Messdaten Burg LF
m17 = [i[31] for i in mdata] #Messdaten Eisenberg
m18 = [i[32] for i in mdata] #Messdaten Deutsch-Kaltenbrunn Restwasser
m19 = [i[33] for i in mdata] #Messdaten Deutsch-Kaltenbrunn Pegel
m20 = [i[34] for i in mdata] #Messdaten Deutsch-Kaltenbrunn Unterwasser
m21 = [i[35] for i in mdata] #Messdaten Bildein Pegel
m22 = [i[36] for i in mdata] #Messdaten Bildein Unterwasser
m23 = [i[38] for i in mdata] #Messdaten Bildein Restwasser
m24 = [i[39] for i in mdata] #Messdaten Eberau
m25 = [i[40] for i in mdata] #Messdaten Postrum
m26 = [i[41] for i in mdata] #Messdaten Gaas - Rodlingbach
m27 = [i[42] for i in mdata] #Messdaten Gaas
#m28 = [i[43] for i in mdata] #Messdaten Moschendorf

filename = "C:\heatsource900b5_339\win32\Test\outputfiles\Temp_H2O.txt"
thedata = hs9_loader.loadfile(filename=filename)
#print 'loaded: ', thedata

#print i[43] TODO: Fehler: m28 = [i[43] for ...] list index out of range obwohl print i[43] funkt, kein sichtbares Prob.

date_time = [i[0] for i in thedata]
x1 = [i[8] for i in thedata] #km 88.92 Hundsmühlbach
x2 = [i[17] for i in thedata] #km 84.60 Tauchenbach
x3 = [i[26] for i in thedata] #km 80.10 Sinnersdorf
x4 = [i[48] for i in thedata] #km 69.16 Riedlingsdorf
x5 = [i[56] for i in thedata] #km 64.98 ober Oberwart
x6 = [i[61] for i in thedata] #km 62.62 unter Oberwart
x7 = [i[64] for i in thedata] #km 60.83 Unterwart
x8 = [i[75] for i in thedata] #km 55.56 Jabbing 1
x9 = [i[76] for i in thedata] #km 54.42 Jabbing 2
x10 = [i[77] for i in thedata] #km 54.26 Jabbing 3
x11 = [i[83] for i in thedata] #km 51.41 Jabbing 4
x12 = [i[92] for i in thedata] #km 46.70 Zickenbach 1
x13 = [i[93] for i in thedata] #km 46.51 Zickenbach 2
x14 = [i[96] for i in thedata] #km 44.65 Badersdorf
x15 = [i[104] for i in thedata] #km 40.96 Woppendorf
x16 = [i[110] for i in thedata] #km 38.19 Burg (BioClic)
x17 = [i[111] for i in thedata] #km 37.29 Burg (LowFlow)
x18 = [i[124] for i in thedata] #km 30.96 Eisenberg
x19 = [i[128] for i in thedata] #km 28.79 DeutschSchützen R
x20 = [i[129] for i in thedata] #km 28.44/28.38 DeutschSchützen P+U
x21 = [i[135] for i in thedata] #km 25.32 Bildein Pegel
x22 = [i[138] for i in thedata] #km 23.96/23.78 Bildein Unterwasser+R
x23 = [i[144] for i in thedata] #km 21.0 Eberau
x25 = [i[146] for i in thedata] #km 20.14 Postrum
x26 = [i[152] for i in thedata] #km 17.0 Gaas
x27 = [i[157] for i in thedata] #km 14.61 Moschendorf

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
ax.set_title('UW, J1, J2, J3')
ax.plot(date_time, x7, color='red', lw=0.2)       #UW
ax.plot(date_time, x8, color='darkred', lw=0.2)   #J1
ax.plot(date_time, x9, color='darkviolet', lw=0.2)#J2
ax.plot(date_time, x10, color='darkblue', lw=0.2) #J3
ax.plot(date_time, m7, color='red', lw=0.7)       #UW
ax.plot(date_time, m8, color='darkred', lw=0.7)   #J1
ax.plot(date_time, m9, color='darkviolet', lw=0.7)#J2
ax.plot(date_time, m10, color='darkblue', lw=0.7) #J3
fig.autofmt_xdate()

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax = fig.add_subplot(223)
ax.set_title('Z1, Z2, BD, WD, BG')
ax.plot(date_time, x12, color='red', lw=0.5) #Z1
ax.plot(date_time, x13, color='darkred', lw=0.5) #Z2
ax.plot(date_time, x14, color='violet', lw=0.5) #BD
ax.plot(date_time, x15, color='darkblue', lw=0.5) #WD
ax.plot(date_time, x16, color='darkblue', lw=0.5) #BG
ax.plot(date_time, m11, color='red', lw=0.7)        #Z1
ax.plot(date_time, m12, color='darkred', lw=0.7)    #Z2
ax.plot(date_time, m13, color='darkviolet', lw=0.7) #BD
ax.plot(date_time, m14, color='darkblue', lw=0.7)   #WD
ax.plot(date_time, m15, color='darkblue', lw=0.7)   #BG
plt.xlabel('time[h]')

ax = fig.add_subplot(224)
ax.set_title('DS_P, BI_P, EB, MO')
ax.plot(date_time, x20, color='red', lw=0.5, label='1') #DS_P+U
ax.plot(date_time, x21, color='darkred', lw=0.5,label='2') #BI_P
ax.plot(date_time, x23, color='violet', lw=0.5, label='3') #EB
ax.plot(date_time, x27, color='darkblue', lw=0.5, label='4') #MO
ax.plot(date_time, m19, color='red', lw=0.7)        #DS_P
ax.plot(date_time, m21, color='darkred', lw=0.7)    #BI_P
ax.plot(date_time, m24, color='darkviolet', lw=0.7) #EB
#ax.plot(date_time, m28, color='darkblue', lw=0.7)   #MO

fig.autofmt_xdate()
plt.xlabel('time[h]')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title="downstream")

plt.show()