# -*- coding: utf-8 -*-
__author__ = 'lnx'

import datetime

import matplotlib.pyplot as plt
from TEB.displaySURFEX.CONVERTSURFEXTEXTE import loadfile
from matplotlib.dates import DateFormatter

S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2016_365366NS/TCANYON.TXT"
S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N/2016_365366WO/TCANYON.TXT"

S201ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/201_Can_B_N/2016_365366NS/TCANYON.TXT"
S201wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/201_Can_B_N/2016_365366WO/TCANYON.TXT"

S205ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/205_Can_W_W/2016_365366NS/TCANYON.TXT"
S205wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/205_Can_W_W/2016_365366WO/TCANYON.TXT"

S200ns_allwhite = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_allwhite/2016_365366NS/TCANYON.TXT"
S200wo_allwhite = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_allwhite/2016_365366WO/TCANYON.TXT"

S200ns_horwhite = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_horwhite/2016_365366NS/TCANYON.TXT"
S200wo_horwhite = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_horwhite/2016_365366WO/TCANYON.TXT"

S200ns_whiteroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N_whiteroof/2016_365366NS/TCANYON.TXT"
S200wo_whiteroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/PVFINAL/200_Can_A_N_whiteroof/2016_365366WO/TCANYON.TXT"

S200NSvalues = loadfile(S200ns)
S200WOvalues = loadfile(S200wo)

S200NSwhiteroofvalues = loadfile(S200ns_whiteroof)
S200WOwhiteroofvalues = loadfile(S200wo_whiteroof)
#S200NSgreenroofvalues = loadfile(S200ns_greenroof)
#S200WOgreenroofvalues = loadfile(S200wo_greenroof)

S205NSvalues = loadfile(S205ns)
S205WOvalues = loadfile(S205wo)

S200NSallwhitevalues = loadfile(S200ns_allwhite)
S200WOallwhitevalues = loadfile(S200wo_allwhite)
S200NShorwhitevalues = loadfile(S200ns_horwhite)
S200WOhorwhitevalues = loadfile(S200wo_horwhite)

S201NSvalues = loadfile(S201ns)
S201WOvalues = loadfile(S201wo)

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
ax1.plot(timelist,S200WOvalues, label=r"$\alpha_{g}$:0,13;$\alpha_{w}$:0,20;$\alpha_{r}$:0,14 'STQ'", color="orange")#,linestyle="dashed")
#ax1.plot(timelist,S200NSvalues, color="orange",linestyle=":")
#Heller Boden
ax1.plot(timelist,S201WOvalues, label=r"$\alpha_{g}$:0,56;$\alpha_{w}$:0,20;$\alpha_{r}$:0,14 'heller Boden'", color="red")#,linestyle="dashed")
#ax1.plot(timelist,S201NSvalues, color="green",linestyle=":")
#Weißer Canyon
ax1.plot(timelist,S205WOvalues, label=r"$\alpha_{g}$:0,80;$\alpha_{w}$:0.80;$\alpha_{r}$:0,14 'weisser Canyon'", color="violet")
#ax1.plot(timelist,S205NSvalues, color="violet",linestyle=":")
#Weißes Dach
ax1.plot(timelist,S200WOwhiteroofvalues, label=r"$\alpha_{g}$:0,13;$\alpha_{w}$:0.20;$\alpha_{r}$:0,80 'weisses Dach'", color="green")#,linestyle="dashed")
#ax1.plot(timelist,S200NSwhiteroofvalues, color="green",linestyle=":")
#Heller Boden, Weißes Dach
ax1.plot(timelist,S200WOhorwhitevalues, label=r"$\alpha_{g}$:0,56;$\alpha_{w}$:0.13;$\alpha_{r}$;0,80 'helle Horizontale'", color="turquoise")
#ax1.plot(timelist,S200NShorwhitevalues, color="turquoise",linestyle=":")
#Alles Weiß
ax1.plot(timelist,S200WOallwhitevalues, label=r"$\alpha_{g}$:0,80;$\alpha_{w}$:0,80;$\alpha_{r}$:0,80 'alles Weiss'", color="blue" )
#ax1.plot(timelist,S200NSallwhitevalues, color="blue",linestyle=":")
ax1.set_ylabel(r"$T_{a}$"u'[°C]')
ax1.legend(loc="upper center",fontsize='small')
ax1.set_xlabel('[UTC]')
ax1.grid(True)
myFmt = DateFormatter("%H")
ax1.xaxis.set_major_formatter(myFmt)
plt.show()



