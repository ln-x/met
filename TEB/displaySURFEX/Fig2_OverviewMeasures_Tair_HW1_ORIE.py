# -*- coding: utf-8 -*-
__author__ = 'lnx'

import matplotlib.pyplot as plt
from CONVERTSURFEXTEXTE import loadfile
import datetime
from matplotlib.dates import DateFormatter

S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171NS/TCANYON.TXT"
S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171WO/TCANYON.TXT"
S200ns_isolated = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_isolated/2017_170171NS/TCANYON.TXT"
S200wo_isolated = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_isolated/2017_170171WO/TCANYON.TXT"
S200ns_whiteroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_whiteroof/2017_170171NS/TCANYON.TXT"
S200wo_whiteroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_whiteroof/2017_170171WO/TCANYON.TXT"
#S200ns_greenroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_greenroof/2017_170171NS/TCANYON.TXT"
#S200wo_greenroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_greenroof/2017_170171WO/TCANYON.TXT"
S200ns_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_PVroof/2017_170171NS/TCANYON.TXT"
S200wo_pvroof = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_PVroof/2017_170171WO/TCANYON.TXT"

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

#diff200_whiteroot = np.copy(S100values)
#for i in range(len(S100values)):
#       diff200_whiteroot[i] = S200whiteroofvalues[i]-S200values[i]

start = datetime.datetime(2017,6,19,0)
#print start.hour
numminutes = 2880
timelist = []
xaxis=[]
for x in range (0, numminutes,10):
    moment = start + datetime.timedelta(minutes = x)
    timelist.append(moment)
timelist = timelist[:-1]

fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax1.set_title(u"andere Methoden,Straßenorientierung, Canyon:HW1,20.6.2017")
ax1.plot(timelist[:-144],S200WOisolatedvalues[:-144], label="isoliert", color="red")#,linestyle="dashed")
ax1.plot(timelist[:-144],S200NSisolatedvalues[:-144], color="red",linestyle=":")
ax1.plot(timelist[:-144],S200WOwhiteroofvalues[:-144], label="weisses Dach", color="violet")#,linestyle="dashed")
ax1.plot(timelist[:-144],S200NSwhiteroofvalues[:-144], color="violet",linestyle=":")
ax1.plot(timelist[:-144],S200WOvalues[:-144], label=r"$\alpha_{G}$ :0.13,0.20", color="black")#,linestyle="dashed")
ax1.plot(timelist[:-144],S200NSvalues[:-144], color="black",linestyle=":")
ax1.plot(timelist[:-144],S200WOpvroofvalues[:-144], label=r"PV Dach, $\eta$=0.2", color="blue")#,linestyle="dashed")
ax1.plot(timelist[:-144],S200NSpvroofvalues[:-144], color="blue",linestyle=":")
#ax1.plot(timelist,S200WOgreenroofvalues, label=u"Gründach, intensiv", color="green")#,linestyle="dashed")
#ax1.plot(timelist,S200NSgreenroofvalues, color="green",linestyle=":")
ax1.set_ylabel(u'Lufftemperatur 2m [°C]')
ax1.legend(loc="lower center",fontsize='small')
ax1.set_xlabel('[UTC]')
myFmt = DateFormatter("%H")
ax1.xaxis.set_major_formatter(myFmt)
plt.show()



