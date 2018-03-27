# -*- coding: utf-8 -*-
__author__ = 'lnx'

import datetime

import matplotlib.pyplot as plt
import numpy as np
from TEB.displaySURFEX.CONVERTSURFEXTEXTE import loadfile
from TEB.displaySURFEX.CONVERTSURFEXTEXTE_UTCI import loadfile as loadfile_utci

S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171NS/UTCI_OUTSUN.TXT"
S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171WO/UTCI_OUTSUN.TXT"
S201ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/201_Can_B_N/2017_170171NS/UTCI_OUTSUN.TXT"
S201wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/201_Can_B_N/2017_170171WO/UTCI_OUTSUN.TXT"
S202ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/202_Can_A_A/2017_170171NS/UTCI_OUTSUN.TXT"
S202wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/202_Can_A_A/2017_170171WO/UTCI_OUTSUN.TXT"
S203ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B/2017_170171NS/UTCI_OUTSUN.TXT"
S203wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B/2017_170171WO/UTCI_OUTSUN.TXT"
S204ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/204_Can_B_W/2017_170171NS/UTCI_OUTSUN.TXT"#
S204wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/204_Can_B_W/2017_170171WO/UTCI_OUTSUN.TXT"#
S205ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/205_Can_W_W/2017_170171NS/UTCI_OUTSUN.TXT"
S205wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/205_Can_W_W/2017_170171WO/UTCI_OUTSUN.TXT"

S200nsT = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171NS/TCANYON.TXT"
S200woT = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171WO/TCANYON.TXT"
S201nsT = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/201_Can_B_N/2017_170171NS/TCANYON.TXT"
S201woT = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/201_Can_B_N/2017_170171WO/TCANYON.TXT"
S202nsT = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/202_Can_A_A/2017_170171NS/TCANYON.TXT"
S202woT = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/202_Can_A_A/2017_170171WO/TCANYON.TXT"
S203nsT = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B/2017_170171NS/TCANYON.TXT"
S203woT = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B/2017_170171WO/TCANYON.TXT"
S204nsT = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/204_Can_B_W/2017_170171NS/TCANYON.TXT"#
S204woT = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/204_Can_B_W/2017_170171WO/TCANYON.TXT"#
S205nsT = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/205_Can_W_W/2017_170171NS/TCANYON.TXT"
S205woT = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/205_Can_W_W/2017_170171WO/TCANYON.TXT"


S200NSvalues = loadfile_utci(S200ns)
S200WOvalues = loadfile_utci(S200wo)
S201NSvalues = loadfile_utci(S201ns)
S201WOvalues = loadfile_utci(S201wo)
S202NSvalues = loadfile_utci(S202ns)
S202WOvalues = loadfile_utci(S202wo)
S203NSvalues = loadfile_utci(S203ns)
S203WOvalues = loadfile_utci(S203wo)
S204NSvalues = loadfile_utci(S204ns)
S204WOvalues = loadfile_utci(S204wo)
S205NSvalues = loadfile_utci(S205ns)
S205WOvalues = loadfile_utci(S205wo)

S200NSvaluesT = loadfile(S200nsT)
S200WOvaluesT = loadfile(S200woT)
S201NSvaluesT = loadfile(S201nsT)
S201WOvaluesT = loadfile(S201woT)
S202NSvaluesT = loadfile(S202nsT)
S202WOvaluesT = loadfile(S202woT)
S203NSvaluesT = loadfile(S203nsT)
S203WOvaluesT = loadfile(S203woT)
S204NSvaluesT = loadfile(S204nsT)
S204WOvaluesT = loadfile(S204woT)
S205NSvaluesT = loadfile(S205nsT)
S205WOvaluesT = loadfile(S205woT)

#diff201 = np.copy(S200values)
#diff202 = np.copy(S200values)
#diff203 = np.copy(S200values)
#diff204 = np.copy(S200values)
#diff205 = np.copy(S200values)

#for i in range(len(S200values)):
#       diff201[i] = S201values[i]-S200values[i]
#       diff202[i] = S202values[i]-S200values[i]
#       diff203[i] = S203values[i]-S200values[i]
#       diff204[i] = S204values[i]-S200values[i]
#       diff205[i] = S205values[i]-S200values[i]

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
ax =fig.add_subplot(111)
ax2 = ax.twinx()

x = [0.2,0.56,0.8]
y = [np.max(S201WOvalues),np.max(S203WOvalues),np.max(S204WOvalues)]
z = [np.max(S201NSvalues),np.max(S203NSvalues),np.max(S204WOvalues)]
UT11_wo = [np.mean(S201WOvalues[63:70]),np.mean(S203WOvalues[63:70]),np.mean(S204WOvalues[63:70])]
UT14_wo = [np.mean(S201WOvalues[78:85]),np.mean(S203WOvalues[78:85]),np.mean(S204WOvalues[78:85])]
UT11_ns = [np.mean(S201NSvalues[63:70]),np.mean(S203NSvalues[63:70]),np.mean(S204NSvalues[63:70])]
UT14_ns = [np.mean(S201NSvalues[78:85]),np.mean(S203NSvalues[78:85]),np.mean(S204NSvalues[78:85])]

Ty = [np.max(S201WOvaluesT),np.max(S203WOvaluesT),np.max(S204WOvaluesT)]
Tz = [np.max(S201NSvaluesT),np.max(S203NSvaluesT),np.max(S204WOvaluesT)]
TUT11_wo = [np.mean(S201WOvaluesT[63:70]),np.mean(S203WOvaluesT[63:70]),np.mean(S204WOvaluesT[63:70])]
TUT14_wo = [np.mean(S201WOvaluesT[78:85]),np.mean(S203WOvaluesT[78:85]),np.mean(S204WOvaluesT[78:85])]
TUT11_ns = [np.mean(S201NSvaluesT[63:70]),np.mean(S203NSvaluesT[63:70]),np.mean(S204NSvaluesT[63:70])]
TUT14_ns = [np.mean(S201NSvaluesT[78:85]),np.mean(S203NSvaluesT[78:85]),np.mean(S204NSvaluesT[78:85])]

plt.title(r"$\alpha_{g}$=0.56")
ax.set_xlabel(r"$\alpha_{w}$")
ax.set_ylabel(r"$T_{a}$"u'[°C]')
ax2.set_ylabel(u"UTCI [°C]")
ax2.plot(x, y, "o",color="red",label="UTCI_max")
ax2.plot(x, z, "s",color="red")#label="max")
ax.plot(x, Ty, "+",color="blue",label="Ta_max")
ax.plot(x, Tz, "*",color="blue")#label="max")
ax2.plot(x, UT11_wo, "o",color="orange",label="UTCI_UT11")
ax2.plot(x, UT11_ns, "s",color="orange")#,label="UT11")
ax.plot(x, TUT11_wo, "+",color="turquoise",label="Ta_UT11")
ax.plot(x, TUT11_ns, "*",color="turquoise")#,color="turquoise")
ax2.plot(x, UT14_wo, "o",color="violet",label="UTCI_UT14")
ax2.plot(x, UT14_ns, "s",color="violet")#label="UT14_wo")
ax.plot(x, TUT14_wo, "+",color="green",label="Ta_UT14")
ax.plot(x, TUT14_ns, "*",color="green")#label="UT14_wo")

plt.xlim([0,1])
ax.set_ylim(25,45)
ax2.set_ylim(35,50)
ax.legend(loc="upper center",ncol=3)
ax2.legend(loc="lower center",ncol=3)
ax.grid(True)

plt.show()

