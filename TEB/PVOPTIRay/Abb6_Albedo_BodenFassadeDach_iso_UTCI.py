# -*- coding: utf-8 -*-
__author__ = 'lnx'

import matplotlib.pyplot as plt
from TEB.displaySURFEX.CONVERTSURFEXTEXTE_UTCI import loadfile
import datetime
from matplotlib.dates import DateFormatter

S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171NS/UTCI_OUTSUN.TXT"
S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2017_170171WO/UTCI_OUTSUN.TXT"
S200ns_isolated = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N_iso/2017_170171NS/UTCI_OUTSUN.TXT"
S200wo_isolated = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N_iso/2017_170171WO/UTCI_OUTSUN.TXT"

S201ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/201_Can_B_N/2017_170171NS/UTCI_OUTSUN.TXT"
S201wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/201_Can_B_N/2017_170171WO/UTCI_OUTSUN.TXT"
S201ns_iso = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/201_Can_B_N_iso/2017_170171NS/UTCI_OUTSUN.TXT"
S201wo_iso = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/201_Can_B_N_iso/2017_170171WO/UTCI_OUTSUN.TXT"

S200ns_allwhite = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_allwhite/2017_170171NS/UTCI_OUTSUN.TXT"
S200wo_allwhite = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_allwhite/2017_170171WO/UTCI_OUTSUN.TXT"
S200ns_allwhite_iso = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_allwhite_iso/2017_170171NS/UTCI_OUTSUN.TXT"
S200wo_allwhite_iso = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_allwhite_iso/2017_170171WO/UTCI_OUTSUN.TXT"

S200NSvalues = loadfile(S200ns)
S200WOvalues = loadfile(S200wo)
S200NSisolatedvalues = loadfile(S200ns_isolated)
S200WOisolatedvalues = loadfile(S200wo_isolated)

S201NSvalues = loadfile(S201ns)
S201WOvalues = loadfile(S201wo)
S201NSisovalues = loadfile(S201ns_iso)
S201WOisovalues = loadfile(S201wo_iso)

S200NSallwhitevalues = loadfile(S200ns_allwhite)
S200WOallwhitevalues = loadfile(S200wo_allwhite)
S200NSallwhiteisovalues = loadfile(S200ns_allwhite_iso)
S200WOallwhiteisovalues = loadfile(S200wo_allwhite_iso)

#diff200_whiteroot = np.copy(S100values)
#for i in range(len(S100values)):
#       diff200_whiteroot[i] = S200whiteroofvalues[i]-S200values[i]

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
#ax1.set_title(u"Canyon:HW1,West-Ost, 19 - 20.6.2017")
#STQ
ax1.plot(timelist,S200WOvalues, label=r"$\alpha_{g}$:0,13;$\alpha_{w}$:0,20;$\alpha_{r}$:0,14; 'STQ'", color="orange")#,linestyle="dashed")
#ax1.plot(timelist,S200NSvalues, color="black",linestyle=":")
ax1.plot(timelist,S200WOisolatedvalues, label=r"$\alpha_{g}$:0,13;$\alpha_{w}$:0,20;$\alpha_{r}$:0,14; 'STQ isoliert'", color="orange",linestyle="dashed")
#ax1.plot(timelist,S200NSisolatedvalues, color="red",linestyle=":")
#Heller Boden
ax1.plot(timelist,S201WOvalues, label=r"$\alpha_{g}$:0,56;$\alpha_{w}$:0,20;$\alpha_{r}$:0,14; 'heller Boden'", color="red")#,linestyle="dashed")
#ax1.plot(timelist,S201NSvalues, color="black",linestyle=":")
ax1.plot(timelist,S201WOisovalues, label=r"$\alpha_{g}$:0,56;$\alpha_{w}$:0,20;$\alpha_{r}$:0,14; 'heller Boden isoliert'", color="red",linestyle="dashed")
#ax1.plot(timelist,S201NSisovalues, color="red",linestyle=":")
#Alles Weiß
ax1.plot(timelist,S200WOallwhitevalues, label=r"$\alpha_{g}$:0,80;$\alpha_{w}$:0,80;$\alpha_{r}$:0,80; 'alles Weiss'", color="blue" )
#ax1.plot(timelist,S200NSallwhitevalues, color="blue",linestyle=":")
ax1.plot(timelist,S200WOallwhiteisovalues, label=r"$\alpha_{g}$:0,80;$\alpha_{w}$:0,80;$\alpha_{r}$:0,80; 'alles Weiss isoliert'", color="blue",linestyle="dashed" )
#ax1.plot(timelist,S200NSallwhitevalues, color="blue",linestyle=":")
ax1.set_ylabel(u'UTCI [°C]')
ax1.legend(loc="upper left",fontsize='small')
ax1.set_xlabel('[UTC]')
ax1.set_ylim(15,65)
ax1.grid(True)
myFmt = DateFormatter("%H")
ax1.xaxis.set_major_formatter(myFmt)
plt.show()



