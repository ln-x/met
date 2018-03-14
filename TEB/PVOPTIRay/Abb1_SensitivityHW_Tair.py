# -*- coding: utf-8 -*-
__author__ = 'lnx'

import pandas as pd
import matplotlib.pyplot as plt
from TEB.displaySURFEX.CONVERTSURFEXTEXTE import loadfile
import numpy as np
import datetime
import matplotlib.gridspec as gridspec
from matplotlib.dates import DateFormatter

S100 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/100_Platz_A_N/2017_170171/TCANYON.TXT"
S101 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/101_Platz_B_N/2017_170171/TCANYON.TXT"
S102 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/102_Platz_A_A/2017_170171/TCANYON.TXT"
S103 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/103_Platz_B_B/2017_170171/TCANYON.TXT"

S200 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171/TCANYON.TXT"
S201 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/201_Can_B_N/2017_170171/TCANYON.TXT"
S202 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/202_Can_A_A/2017_170171/TCANYON.TXT"
S203 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B/2017_170171/TCANYON.TXT"

S200values = loadfile(S200)
S201values = loadfile(S201)
S202values = loadfile(S202)
S203values = loadfile(S203)
S100values = loadfile(S100)
S101values = loadfile(S101)
S102values = loadfile(S102)
S103values = loadfile(S103)

diff101 = np.copy(S100values)
diff102 = np.copy(S100values)
diff103 = np.copy(S100values)
diff201 = np.copy(S100values)
diff202 = np.copy(S100values)
diff203 = np.copy(S100values)

for i in range(len(S100values)):
       diff101[i] = S101values[i]-S100values[i]
       diff102[i] = S102values[i]-S100values[i]
       diff103[i] = S103values[i]-S100values[i]
       diff201[i] = S201values[i]-S200values[i]
       diff202[i] = S202values[i]-S200values[i]
       diff203[i] = S203values[i]-S200values[i]

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

fig = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
#ax1.set_title(u"Einfluss Materialien, Platz - HW0.2, 19.6.2017")
ax1.plot(timelist,S100values,label=r"$\alpha_{g}$:0,13;$\alpha_{w}$:0,20", color="orange")
ax1.plot(timelist,S102values, label=r"$\alpha_{g}$:0,13;$\alpha_{w}$:0,10", color="red")
ax1.plot(timelist,S101values, label=r"$\alpha_{g}$:0,56;$\alpha_{w}$:0,20", color="turquoise")
ax1.plot(timelist,S103values, label=r"$\alpha_{g}$:0,56;$\alpha_{w}$:0,56", color="blue")
ax1.set_ylabel(r"$T_{a}$ " u"°C")
ax1.legend(loc="upper left",fontsize='small',ncol=2)
ax2.plot(timelist,diff101, label="Beton,Putz", color="turquoise")
ax2.plot(timelist,diff102, label="Asphalt,dunkle Fassade", color="red")
ax2.plot(timelist,diff103, label="Beton,Beton", color="blue")
ax2.set_ylabel(r"$\Delta T_{a}$" u"°C")
ax2.set_xlabel('[UTC]')
myFmt = DateFormatter("%H")
ax1.xaxis.set_major_formatter(myFmt)
ax2.xaxis.set_major_formatter(myFmt)
ax1.grid(True)
ax2.grid(True)
plt.show()

fig1 = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
#ax1.set_title(u"Einfluss Materialien, Canyon, 19.6.2017")
ax1.plot(timelist,S202values, label=r"$\alpha_{g}$:0,13;$\alpha_{w}$:0,10", color="red") #u"α=0.13,0.10"
ax1.plot(timelist,S200values, label=r"$\alpha_{g}$:0,13;$\alpha_{w}$:0,20", color="orange")
ax1.plot(timelist,S201values, label=r"$\alpha_{g}$:0,56;$\alpha_{w}$:0,20", color="turquoise")
ax1.plot(timelist,S203values, label=r"$\alpha_{g}$:0,56;$\alpha_{w}$:0,56", color="blue")
ax1.set_ylabel(r"$T_{a}$ " u"°C")
ax1.legend(loc="upper left",fontsize='small',ncol=2)
ax2.plot(timelist,diff201, label="Beton,Putz", color="turquoise")
ax2.plot(timelist,diff202, label="Asphalt,dunkle Fassade", color="red")
ax2.plot(timelist,diff203, label="Beton,Beton", color="blue")
ax2.set_ylabel(r"$\Delta T_{a}$" u"°C")
ax2.set_xlabel('[UTC]')
ax1.grid(True)
ax2.grid(True)
myFmt = DateFormatter("%H")
ax1.xaxis.set_major_formatter(myFmt)
ax2.xaxis.set_major_formatter(myFmt)
plt.show()
