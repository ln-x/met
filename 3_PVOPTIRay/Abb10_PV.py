# -*- coding: utf-8 -*-
__author__ = 'lnx'

import pandas as pd
import matplotlib.pyplot as plt
from TEB.displaySURFEX.CONVERTSURFEXTEXTE import loadfile
import numpy as np
import datetime
import matplotlib.gridspec as gridspec
from matplotlib.dates import DateFormatter

#S100 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/100_Platz_A_N/2017_170171/TCANYON.TXT"
S100ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/100_Platz_A_N/2017_170171WO/TCANYON.TXT"
S100wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/100_Platz_A_N/2017_170171NS/TCANYON.TXT"
#S100_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/100_Platz_A_N/2017_170171/TCANYON.TXT"
S100ns_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/100_Platz_A_N_PVroof/2017_170171NS/TCANYON.TXT"
S100wo_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/100_Platz_A_N_PVroof/2017_170171WO/TCANYON.TXT"
S110ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/110_Platz_A_PV70/2017_170171NS/TCANYON.TXT"
S110wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/110_Platz_A_PV70/2017_170171WO/TCANYON.TXT"
S111ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/111_Platz_B_PV70/2017_170171NS/TCANYON.TXT"
S111wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/111_Platz_B_PV70/2017_170171WO/TCANYON.TXT"

#S200 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171/TCANYON.TXT"
S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171NS/TCANYON.TXT"
S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171WO/TCANYON.TXT"
#S200_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171/TCANYON.TXT"
S200ns_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N_PVroof/2017_170171NS/TCANYON.TXT"
S200wo_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N_PVroof/2017_170171WO/TCANYON.TXT"
#S210 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/210_Can_A_PV70/2017_170171/TCANYON.TXT"
S210ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/210_Can_A_PV70/2017_170171NS/TCANYON.TXT"
S210wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/210_Can_A_PV70/2017_170171WO/TCANYON.TXT"
#S211 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/211_Can_B_PV70/2017_170171/TCANYON.TXT"
S211ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/211_Can_B_PV70/2017_170171NS/TCANYON.TXT"
S211wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/211_Can_B_PV70/2017_170171WO/TCANYON.TXT"

S100nsvalues = loadfile(S100ns)
S100wovalues = loadfile(S100wo)
S100nspvroofvalues = loadfile(S100ns_pvroof)
S100wopvroofvalues = loadfile(S100wo_pvroof)
S110nsvalues = loadfile(S110ns)
S110wovalues = loadfile(S110wo)
S111nsvalues = loadfile(S111ns)
S111wovalues = loadfile(S111wo)
#S200values = loadfile(S200)
S200nsvalues = loadfile(S200ns)
S200wovalues = loadfile(S200wo)
S200nspvroofvalues = loadfile(S200ns_pvroof)
S200wopvroofvalues = loadfile(S200wo_pvroof)
S210nsvalues = loadfile(S210ns)
S210wovalues = loadfile(S210wo)
S211nsvalues = loadfile(S211ns)
S211wovalues = loadfile(S211wo)

diff110wo = np.copy(S100nsvalues)
diff111wo = np.copy(S100nsvalues)
diff210wo = np.copy(S100nsvalues)
diff211wo = np.copy(S100nsvalues)
diff100wo_pvroof = np.copy(S100nsvalues)
diff200wo_pvroof = np.copy(S100nsvalues)

for i in range(len(S100wovalues)):
       diff110wo[i] = S110wovalues[i]-S100wovalues[i]
       diff111wo[i] = S111wovalues[i]-S100wovalues[i]
       diff100wo_pvroof[i] = S100wopvroofvalues[i]-S100wovalues[i]
       diff210wo[i] = S210wovalues[i]-S200wovalues[i]
       diff211wo[i] = S211wovalues[i]-S200wovalues[i]
       diff200wo_pvroof[i] = S200wopvroofvalues[i]-S200wovalues[i]

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

fig2 = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
#ax1.set_title(u"Einfluss PV/Boden, Platz - HW0.2, 19.6.2017")
ax1.plot(timelist,S100wovalues, label="Asphalt", color="black")
ax1.plot(timelist,S100wopvroofvalues, label="Asphalt + PVDach", color="orange")
ax1.plot(timelist,S110wovalues, label="Asphalt + 70%PV", color="green")
ax1.plot(timelist,S111wovalues, label="Beton + 70%PV", color="blue")
ax1.set_ylabel(r"$T_{a}$ " u"°C")
ax1.legend(loc="lower right",fontsize='small')
ax2.plot(timelist,diff100wo_pvroof, label="Aspalt,PVDach", color="orange")
ax2.plot(timelist,diff110wo, label="Aspalt,70%PV", color="green")
ax2.plot(timelist,diff111wo, label="Beton,70%PV", color="blue")
ax2.set_ylabel(r"$\Delta T_{a}$" u"°C")
ax2.set_xlabel('[UTC]')
ax1.grid(True)
ax2.grid(True)
myFmt = DateFormatter("%H")
ax1.xaxis.set_major_formatter(myFmt)
ax2.xaxis.set_major_formatter(myFmt)
plt.show()

fig3 = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
#ax1.set_title(u"Einfluss PV/Boden, Kreuzung - HW1, 19.6.2017")
ax1.plot(timelist,S200wovalues, label="Asphalt", color="black")
ax1.plot(timelist,S200wopvroofvalues, label="Asphalt + PVDach", color="orange")
ax1.plot(timelist,S210wovalues, label="Asphalt + 70%PV", color="green")
ax1.plot(timelist,S211wovalues, label="Beton + 70%PV", color="blue")
ax1.set_ylabel(r"$T_{a}$ " u"°C")
ax1.legend(loc="lower right",fontsize='small')
ax2.plot(timelist,diff200wo_pvroof, label="Aspalt,PVDach", color="orange")
ax2.plot(timelist,diff210wo, label="Aspalt,70%PV", color="green")
ax2.plot(timelist,diff211wo, label="Beton,70%PV", color="blue")
ax2.set_ylabel(r"$\Delta T_{a}$" u"°C")
ax2.set_xlabel('[UTC]')
ax1.grid(True)
ax2.grid(True)
myFmt = DateFormatter("%H")
ax1.xaxis.set_major_formatter(myFmt)
ax2.xaxis.set_major_formatter(myFmt)
plt.show()


