# -*- coding: utf-8 -*-
__author__ = 'lnx'

import matplotlib.pyplot as plt
from CONVERTSURFEXTEXTE import loadfile
import datetime
from matplotlib.dates import DateFormatter

S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171WO/TCANYON.TXT"
S200wo_CanT = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171WO/T2M_TEB.TXT"
S200wo_CanF = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171WO_CanopyF/T2M_TEB.TXT"
S200wo_CanF_C = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171WO_CanopyF/TCANYON.TXT"
S200wo_CanT_r = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171WO_CanopyT_Road4_0_001/T2M_TEB.TXT"

S200WOvalues = loadfile(S200wo)
S200WOCanTvalues = loadfile(S200wo_CanT)
S200WOCanFvalues = loadfile(S200wo_CanF)
S200WOCanFCvalues = loadfile(S200wo_CanF_C)
S200WOCanTrvalues = loadfile(S200wo_CanT_r)

start = datetime.datetime(2017,6,19,0)
numminutes = 2880
timelist = []
xaxis=[]
for x in range (0, numminutes,10):
    moment = start + datetime.timedelta(minutes = x)
    timelist.append(moment)
timelist = timelist[:-1]

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title(u"Canyon:HW1,West-Ost, 19 - 20.6.2017")
#STQ
ax1.plot(timelist,S200WOvalues, label=r"$\alpha_{G}$:0,13;$\alpha_{W}$:0,20;$\alpha_{R}$:0,14 Can=T,road4=1; TCanyon", color="black")#,linestyle="dashed")
ax1.plot(timelist,S200WOCanTvalues, label=r"$\alpha_{G}$:0,13;$\alpha_{W}$:0,20;$\alpha_{R}$:0,14 Can=T,road4=1; T2M", color="orange")#,linestyle="dashed")
ax1.plot(timelist,S200WOCanFCvalues, label=r"$\alpha_{G}$:0,13;$\alpha_{W}$:0,20;$\alpha_{R}$:0,14 Can=T,road4=1; TCanyon", color="grey")
ax1.plot(timelist,S200WOCanTrvalues, label=r"$\alpha_{G}$:0,13;$\alpha_{W}$:0,20;$\alpha_{R}$:0,14 Can=T,road4=0.001; T2M", color="blue")#,linestyle="dashed")
ax1.set_ylabel(u'Lufftemperatur 2m [°C]')
ax1.legend(loc="upper left",fontsize='small')
ax1.set_xlabel('[UTC]')
myFmt = DateFormatter("%H")
ax1.xaxis.set_major_formatter(myFmt)
plt.show()



