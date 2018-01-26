# -*- coding: utf-8 -*-
__author__ = 'lnx'

import pandas as pd
import matplotlib.pyplot as plt
from CONVERTSURFEXTEXTE import loadfile
import numpy as np
import datetime
import matplotlib.gridspec as gridspec
from matplotlib.dates import DateFormatter

S100 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/100_Platz_A_N/2017_170171/TCANYON.TXT"
S100ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/100_Platz_A_N/2017_170171WO/TCANYON.TXT"
S100wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/100_Platz_A_N/2017_170171NS/TCANYON.TXT"
#S100_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/100_Platz_A_N/2017_170171/TCANYON.TXT"
S100ns_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/100_Platz_A_N/2017_170171NW/TCANYON.TXT"
S100wo_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/100_Platz_A_N/2017_170171WO/TCANYON.TXT"
S110 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/110_Platz_A_PV70/2017_170171/TCANYON.TXT"
S111 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/111_Platz_B_PV70/2017_170171/TCANYON.TXT"

S200 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171/TCANYON.TXT"
S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171NS/TCANYON.TXT"
S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171WO/TCANYON.TXT"
S200_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171/TCANYON.TXT"
S200ns_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171NS/TCANYON.TXT"
S200wo_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171WO/TCANYON.TXT"
S210 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/210_Can_A_PV70/2017_170171/TCANYON.TXT"
S210ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/210_Can_A_PV70/2017_170171_NS/TCANYON.TXT"
S210wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/210_Can_A_PV70/2017_170171_WO/TCANYON.TXT"
S211 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/211_Can_B_PV70/2017_170171/TCANYON.TXT"
S211ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/211_Can_B_PV70/2017_170171_NS/TCANYON.TXT"
S211wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/211_Can_B_PV70/2017_170171_WO/TCANYON.TXT"

S100values = loadfile(S100)
S100nsvalues = loadfile(S100ns)
S100wovalues = loadfile(S100wo)
S100nspvroofvalues = loadfile(S100ns_pvroof)
S100wopvroofvalues = loadfile(S100wo_pvroof)
S110values = loadfile(S110)
S111values = loadfile(S111)

S200values = loadfile(S200)
S200NSvalues = loadfile(S200ns)
S200WOvalues = loadfile(S200wo)
S200NSpvroofvalues = loadfile(S200ns_pvroof)
S200WOpvroofvalues = loadfile(S200wo_pvroof)
S210values = loadfile(S210)
S210NSvalues = loadfile(S210ns)
S210WOvalues = loadfile(S210wo)
S211values = loadfile(S211)
S211NSvalues = loadfile(S211ns)
S211WOvalues = loadfile(S211wo)

diff101 = np.copy(S100values)
diff102 = np.copy(S100values)
diff103 = np.copy(S100values)
diff201 = np.copy(S100values)
diff202 = np.copy(S100values)
diff203 = np.copy(S100values)
diff204 = np.copy(S100values)
diff205 = np.copy(S100values)
diff210 = np.copy(S100values)
diff211 = np.copy(S100values)
diff110 = np.copy(S100values)
diff111 = np.copy(S100values)

for i in range(len(S100values)):
       diff110[i] = S110values[i]-S100values[i]
       diff111[i] = S111values[i]-S100values[i]

       diff210[i] = S210values[i]-S200values[i]
       diff211[i] = S211values[i]-S200values[i]

start = datetime.datetime(2017,6,19,0)
#print start.hour
numminutes = 2880
timelist = []
xaxis=[]
for x in range (0, numminutes,10):
    moment = start + datetime.timedelta(minutes = x)
    hour = moment.hour
    timelist.append(moment)
    xaxis.append(hour)
xaxis = xaxis[:-1]
timelist = timelist[:-1]
#print timelist
print len(S100values)
print xaxis

fig2 = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
#ax1.set_title(u"Einfluss PV/Boden, Platz - HW0.2, 19.6.2017")
ax1.plot(timelist,S100values, label="Asphalt", color="black")
ax1.plot(timelist,S100wopvroofvalues, label="Asphalt + PVDach", color="orange")
ax1.plot(timelist,S110values, label="Asphalt + 70%PV", color="green")
ax1.plot(timelist,S111values, label="Beton + 70%PV", color="blue")
ax1.set_ylabel(r"$T_{a}$ " u"°C")
ax1.legend(loc="lower center",fontsize='small')
ax2.plot(timelist,diff110, label="Aspalt,PVDach", color="orange")
ax2.plot(timelist,diff110, label="Aspalt,70%PV", color="green")
ax2.plot(timelist,diff111, label="Beton,70%PV", color="blue")
ax2.set_ylabel(r"$\Delta T_{a}$" u"°C")
ax2.set_xlabel('[UTC]')
ax1.grid(True)
ax2.grid(True)
myFmt = DateFormatter("%H")
ax1.xaxis.set_major_formatter(myFmt)
ax2.xaxis.set_major_formatter(myFmt)
plt.show()
plt.show()


fig3 = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
#ax1.set_title(u"Einfluss PV/Boden, Kreuzung - HW1, 19.6.2017")
#ax.plot(PVvalKreuzungues, label="Asphalt + PV")
ax1.plot(timelist,S210values, label="Asphalt,70%PV", color="orange")
#ax1.plot(timelist,S210NSvalues, label="Asphalt,70%PV,N-S", color="orange", linestyle="dashed" )
ax1.plot(timelist,S210WOvalues, label="Asphalt,70%PV,W-O", color="orange",linestyle=":")
#ax.plot(S213values, label="Asphalt + 100%PV", color="red")
#ax1.plot(timelist,S211values, label="Beton,70%PV", color="turquoise")
#ax1.plot(timelist,S211NSvalues, label="Beton,70%PV,N-S", color="turquoise", linestyle="dashed")
ax1.plot(timelist,S211WOvalues, label="Beton,70%PV,W-O", color="turquoise", linestyle=":")
#ax.plot(S212values, label="Beton + 100%PV", color="blue")
#ax1.plot(timelist,FORCvalues['Td'],label="Forcing (Dach)")
ax1.set_ylabel(r"$T_{a}$ " u"°C")
ax1.legend(loc="lower center",fontsize='small')
ax2.plot(timelist,diff210, label="Asphalt,PV", color="orange")
ax2.plot(timelist,diff211, label="Beton,PV", color="turquoise")
ax2.set_ylabel(r"$\Delta T_{a}$" u"°C")
ax2.set_xlabel('[UTC]')
ax1.grid(True)
ax2.grid(True)
myFmt = DateFormatter("%H")
ax1.xaxis.set_major_formatter(myFmt)
ax2.xaxis.set_major_formatter(myFmt)
plt.show()


