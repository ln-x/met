# -*- coding: utf-8 -*-
__author__ = 'lnx'

import pandas as pd
import matplotlib.pyplot as plt
from TEB.displaySURFEX.CONVERTSURFEXTEXTE import loadfile
import numpy as np
import datetime
import matplotlib.gridspec as gridspec
from matplotlib.dates import DateFormatter

S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171NS/TCANYON.TXT"
S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171WO/TCANYON.TXT"
S201ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/201_Can_B_N/2017_170171NS/TCANYON.TXT"
S201wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/201_Can_B_N/2017_170171WO/TCANYON.TXT"
S202ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/202_Can_A_A/2017_170171NS/TCANYON.TXT"
S202wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/202_Can_A_A/2017_170171WO/TCANYON.TXT"
S203ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B/2017_170171NS/TCANYON.TXT"
S203wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/203_Can_B_B/2017_170171WO/TCANYON.TXT"
S204ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/204_Can_B_W/2017_170171NS/TCANYON.TXT"#
S204wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/204_Can_B_W/2017_170171WO/TCANYON.TXT"#
S205ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/205_Can_W_W/2017_170171NS/TCANYON.TXT"
S205wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/205_Can_W_W/2017_170171WO/TCANYON.TXT"

S200NSvalues = loadfile(S200ns)
S200WOvalues = loadfile(S200wo)
S201NSvalues = loadfile(S201ns)
S201WOvalues = loadfile(S201wo)
S202NSvalues = loadfile(S202ns)
S202WOvalues = loadfile(S202wo)
S203NSvalues = loadfile(S203ns)
S203WOvalues = loadfile(S203wo)
S204NSvalues = loadfile(S204ns)
S204WOvalues = loadfile(S204wo)
S205NSvalues = loadfile(S205ns)
S205WOvalues = loadfile(S205wo)

diff201wo = np.copy(S200WOvalues)
diff202wo = np.copy(S200WOvalues)
diff203wo = np.copy(S200WOvalues)
diff204wo = np.copy(S200WOvalues)
diff205wo = np.copy(S200WOvalues)

for i in range(len(S200WOvalues)):
       diff201wo[i] = S201WOvalues[i]-S200WOvalues[i]
       diff202wo[i] = S202WOvalues[i]-S200WOvalues[i]
       diff203wo[i] = S203WOvalues[i]-S200WOvalues[i]
       diff204wo[i] = S204WOvalues[i]-S200WOvalues[i]
       diff205wo[i] = S205WOvalues[i]-S200WOvalues[i]

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
ax1 = fig.add_subplot(111)

gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
#ax1.set_title(u"Materialien,Straßenorientierung, Canyon:HW1, 19.6.2017")
#ax1.plot(timelist,S202values, label=u"Asphalt,dunkle Fassade", color="red") #u"α=0.13,0.13"
ax1.plot(timelist,S202WOvalues, label=r"$\alpha_{g}$:0,13;$\alpha_{w}$:0,10", color="red")#,linestyle="dashed")
ax1.plot(timelist,S202NSvalues, color="red",linestyle=":")
#ax1.plot(timelist,S200values, label="Asphalt,Putz", color="orange")
#ax1.plot(timelist,S200WOwhiteroofvalues, label=r"$\alpha$ :0.13,0.20,0.80", color="black")#,linestyle="dashed")
#ax1.plot(timelist,S200NSwhiteroofvalues, color="pink",linestyle=":")
ax1.plot(timelist,S200WOvalues, label=r"$\alpha_{g}$:0,13;$\alpha_{w}$:0,20", color="orange")#,linestyle="dashed")
ax1.plot(timelist,S200NSvalues, color="orange",linestyle=":")
#ax1.plot(timelist,S201values, label="Beton,Putz", color="green")
ax1.plot(timelist,S201WOvalues, label=r"$\alpha_{g}$:0,56;$\alpha_{w}$:0,20", color="green")#,linestyle="dashed")
ax1.plot(timelist,S201NSvalues, color="green",linestyle=":")
#ax1.plot(timelist,S203values, label="Beton,Beton", color="turquoise")
ax1.plot(timelist,S203WOvalues, label=r"$\alpha_{g}$:0,56;$\alpha_{w}$:0,56", color="turquoise")#,linestyle="dashed")
ax1.plot(timelist,S203NSvalues, color="turquoise",linestyle=":")
#ax1.plot(timelist,S204values, label=u"Beton,Weiß", color="blue")
ax1.plot(timelist,S204WOvalues, label=r"$\alpha_{g}$:0,56;$\alpha_{w}$:0,80", color="blue")#,linestyle="dashed")
ax1.plot(timelist,S204NSvalues, color="blue",linestyle=":")
#ax1.plot(timelist,S205values, label=u"Weiß,Weiß", color="violet")
ax1.plot(timelist,S205WOvalues, label=r"$\alpha_{g}$:0,80;$\alpha_{w}$:0,80", color="violet")#,linestyle="dashed")
ax1.plot(timelist,S205NSvalues, color="violet",linestyle=":")
ax1.set_ylabel(r"$T_{a}$"u'[°C]')
ax1.set_ylim(16,37)
ax1.legend(loc="lower right",fontsize='small')
ax2.plot(timelist,diff201wo, label="Beton,Putz", color="green")
ax2.plot(timelist,diff202wo, label="Asphalt,dunkle Fassade", color="red")
ax2.plot(timelist,diff203wo, label="Beton,Beton", color="turquoise")
ax2.plot(timelist,diff204wo, label=u"Beton,Weiß", color="blue")
ax2.plot(timelist,diff205wo, label=u"Weiß,Weiß", color="violet")
ax2.set_ylabel(r"$\Delta T_{a}$" u"°C")
ax1.set_xlabel('[UTC]')
ax1.grid(True)
ax2.grid(True)
myFmt = DateFormatter("%H")
ax1.xaxis.set_major_formatter(myFmt)
plt.show()
