# -*- coding: utf-8 -*-
__author__ = 'lnx'

import matplotlib.pyplot as plt
from TEB.displaySURFEX.CONVERTSURFEXTEXTE import loadfile
import datetime
from matplotlib.dates import DateFormatter

#S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2016_365366NS/TCANYON.TXT"
#S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2016_365366WO/TCANYON.TXT"
S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171NS/TCANYON.TXT"
S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171WO_corr/TCANYON.TXT"

2017_170171WO_CanopyT_Road40.001

S201ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170171NS/TCANYON.TXT"
S201wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170171WO/TCANYON.TXT"
S201ns_iso = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Can_B_N_isolated/2017_170171NS/TCANYON.TXT"
S201wo_iso = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Can_B_N_isolated/2017_170171WO/TCANYON.TXT"

S200ns_allwhite = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Can_allwhite/2017_170171NS/TCANYON.TXT"
S200wo_allwhite = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Can_allwhite/2017_170171WO/TCANYON.TXT"

S200ns_horwhite = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Can_horwhite/2017_170171NS/TCANYON.TXT"
S200wo_horwhite = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Can_horwhite/2017_170171WO/TCANYON.TXT"

S200ns_horwhite_iso = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Can_horwhite_isolated/2017_170171NS/TCANYON.TXT"
S200wo_horwhite_iso = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Can_horwhite_isolated/2017_170171WO/TCANYON.TXT"


S200ns_isolated = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_isolated/2017_170171NS/TCANYON.TXT"
S200wo_isolated = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_isolated/2017_170171WO/TCANYON.TXT"
S200ns_whiteroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_whiteroof/2017_170171NS/TCANYON.TXT"
S200wo_whiteroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_whiteroof/2017_170171WO/TCANYON.TXT"
#S200ns_greenroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_greenroof/2017_170171NS/TCANYON.TXT"
#S200wo_greenroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_greenroof/2017_170171WO/TCANYON.TXT"
S200ns_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_PVroof/2017_170171NS/TCANYON.TXT"
S200wo_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_PVroof/2017_170171WO/TCANYON.TXT"

S205ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/205_Kreuzung_W_W/2017_170171NS/TCANYON.TXT"
S205wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/205_Kreuzung_W_W/2017_170171WO/TCANYON.TXT"


S200NSvalues = loadfile(S200ns)
S200WOvalues = loadfile(S200wo)
S200NSisolatedvalues = loadfile(S200ns_isolated)
S200WOisolatedvalues = loadfile(S200wo_isolated)
S200NSwhiteroofvalues = loadfile(S200ns_whiteroof)
S200WOwhiteroofvalues = loadfile(S200wo_whiteroof)
#S200NSgreenroofvalues = loadfile(S200ns_greenroof)
#S200WOgreenroofvalues = loadfile(S200wo_greenroof)
S200NSpvroofvalues = loadfile(S200ns_pvroof)
S200WOpvroofvalues = loadfile(S200wo_pvroof)

S205NSvalues = loadfile(S205ns)
S205WOvalues = loadfile(S205wo)

S200NSallwhitevalues = loadfile(S200ns_allwhite)
S200WOallwhitevalues = loadfile(S200wo_allwhite)
S200NShorwhitevalues = loadfile(S200ns_horwhite)
S200WOhorwhitevalues = loadfile(S200wo_horwhite)

S200NShorwhiteisovalues = loadfile(S200ns_horwhite_iso)
S200WOhorwhiteisovalues = loadfile(S200wo_horwhite_iso)

S201NSvalues = loadfile(S201ns)
S201WOvalues = loadfile(S201wo)
S201NSisovalues = loadfile(S201ns_iso)
S201WOisovalues = loadfile(S201wo_iso)

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
ax1.set_title(u"Canyon:HW1,West-Ost, 19 - 20.6.2017")
#STQ
ax1.plot(timelist,S200WOvalues, label=r"$\alpha_{G}$:0,13;$\alpha_{W}$:0,20;$\alpha_{R}$:0,14 'STQ'", color="orange")#,linestyle="dashed")
#ax1.plot(timelist,S200NSvalues, color="orange",linestyle=":")
#ax1.plot(timelist,S200WOisolatedvalues, label=r"$\alpha_{G}$:0,13;$\alpha_{W}$:0,20;$\alpha_{R}$:0,14, iso", color="grey")#,linestyle="dashed")
#ax1.plot(timelist,S200NSisolatedvalues, color="red",linestyle=":")
#Heller Boden
ax1.plot(timelist,S201WOvalues, label=r"$\alpha_{G}$:0,56;$\alpha_{W}$:0,20;$\alpha_{R}$:0,14 'heller Boden'", color="red")#,linestyle="dashed")
#ax1.plot(timelist,S201NSvalues, color="green",linestyle=":")
#ax1.plot(timelist,S201WOisovalues, label=r"$\alpha_{G}$:0,56;$\alpha_{W}$:0,20;$\alpha_{R}$:0,14, iso", color="pink")#,linestyle="dashed")
#ax1.plot(timelist,S201NSisovalues, color="red",linestyle=":")
#Weißer Canyon
ax1.plot(timelist,S205WOvalues, label=r"$\alpha_{G}$:0,80;$\alpha_{W}$:0.80;$\alpha_{R}$:0,14 'weisser Canyon'", color="violet")
#ax1.plot(timelist,S205NSvalues, color="violet",linestyle=":")
#Weißes Dach
ax1.plot(timelist,S200WOwhiteroofvalues, label=r"$\alpha_{G}$:0,13;$\alpha_{W}$:0.20;$\alpha_{R}$:0,80 'weisses Dach'", color="green")#,linestyle="dashed")
#ax1.plot(timelist,S200NSwhiteroofvalues, color="green",linestyle=":")
#Heller Boden, Weißes Dach
ax1.plot(timelist,S200WOhorwhitevalues, label=r"$\alpha_{G}$:0,56;$\alpha_{W}$:0.13;$\alpha_{R}$;0,80 'helle Horizontale'", color="turquoise")
#ax1.plot(timelist,S200NShorwhitevalues, color="turquoise",linestyle=":")
#Alles Weiß
ax1.plot(timelist,S200WOallwhitevalues, label=r"$\alpha_{G}$:0,80;$\alpha_{W}$:0,80;$\alpha_{R}$:0,80 'alles Weiss'", color="blue" )
#ax1.plot(timelist,S200NSallwhitevalues, color="blue",linestyle=":")
#PV Dach
#ax1.plot(timelist,S200WOpvroofvalues, label=r"PV Dach, $\eta$=0.2", color="blue")#,linestyle="dashed")
#ax1.plot(timelist,S200NSpvroofvalues, color="blue",linestyle=":")
#Gründach
#ax1.plot(timelist,S200WOgreenroofvalues, label=u"Gründach, intensiv", color="green")#,linestyle="dashed")
#ax1.plot(timelist,S200NSgreenroofvalues, color="green",linestyle=":")
ax1.set_ylabel(u'Lufftemperatur 2m [°C]')
ax1.legend(loc="upper left",fontsize='small')
ax1.set_xlabel('[UTC]')
myFmt = DateFormatter("%H")
ax1.xaxis.set_major_formatter(myFmt)
plt.show()



