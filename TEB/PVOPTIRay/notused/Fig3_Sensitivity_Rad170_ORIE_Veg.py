# -*- coding: utf-8 -*-
__author__ = 'lnx'

import pandas as pd
import matplotlib.pyplot as plt
from TEB.displaySURFEX.CONVERTSURFEXTEXTE_UTCI import loadfile
import numpy as np
import datetime
import matplotlib.gridspec as gridspec

#S200 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170/UTCI_OUTSHAD.TXT"
#S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170NS/UTCI_OUTSHAD.TXT"
#S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170WO/UTCI_OUTSHAD.TXT"
S200wo2_WSN_RD = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171WO/WSN_RD1.TXT"
S200wo2_RSN_RD = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171WO/RSN_RD1.TXT"
S200wo2 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171WO/UTCI_OUTSHAD.TXT"
#S200nsGrass = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_25Grass/2017_170NS/UTCI_OUTSHAD.TXT"
S200woGrass = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_25Grass/2017_170171WO/UTCI_OUTSHAD.TXT"
#S200nsTrees = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_25Trees/2017_170NS/UTCI_OUTSHAD.TXT"
S200woTrees = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_25Trees/2017_170171WO/UTCI_OUTSHAD.TXT"
S200woGrass50 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_50Grass/2017_170171WO/UTCI_OUTSHAD.TXT"
S200woTrees50 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_50Trees/2017_170171WO/UTCI_OUTSHAD.TXT"
#S200woTrees100 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_100Trees/2017_170171WO/UTCI_OUTSHAD.TXT"
"""
S203 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B/2017_170/UTCI_OUTSUN.TXT"
S203ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B/2017_170NS/UTCI_OUTSUN.TXT"
S203wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B/2017_170WO/UTCI_OUTSUN.TXT"
S203nsGrass = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B_25Grass/2017_170NS/UTCI_OUTSUN.TXT"
S203woGrass = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B_25Grass/2017_170WO/UTCI_OUTSUN.TXT"
S203nsTrees = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B_25Trees/2017_170NS/UTCI_OUTSUN.TXT"
S203woTrees = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B_25Trees/2017_170WO/UTCI_OUTSUN.TXT"

S200values = loadfile(S200)
S200NSvalues = loadfile(S200ns)
S200WOvalues = loadfile(S200wo)
S200NSgrassvalues = loadfile(S200nsGrass)
S200NStreesvalues = loadfile(S200nsTrees)
"""
S200wo2values = loadfile(S200wo2)
S200WOgrassvalues = loadfile(S200woGrass)
S200WOtreesvalues = loadfile(S200woTrees)
S200WOtrees50values = loadfile(S200woTrees50)
S200WOgrass50values = loadfile(S200woGrass50)

S200wo2_RSN_RD = loadfile(S200wo2_RSN_RD)
S200wo2_WSN_RD = loadfile(S200wo2_WSN_RD)


"""
S203values = loadfile(S203)
S203NSvalues = loadfile(S203ns)
S203WOvalues = loadfile(S203wo)
S203NSgrassvalues = loadfile(S203nsGrass)
S203WOgrassvalues = loadfile(S203woGrass)
S203NStreesvalues = loadfile(S203nsTrees)
S203WOtreesvalues = loadfile(S203woTrees)
"""
#diff200ns = np.copy(S200values)
#diff200wo = np.copy(S200values)
#diff200nsG = np.copy(S200values)
diff200woG = np.copy(S200wo2values)
diff200woG50 = np.copy(S200wo2values)
#diff200nsT = np.copy(S200values)
diff200woT = np.copy(S200wo2values)
diff200woT50 = np.copy(S200wo2values)
#diff203 = np.copy(S200values)
#diff203ns = np.copy(S200values)
#diff203wo= np.copy(S200values)
#diff203nsG = np.copy(S200values)
#diff203woG = np.copy(S200values)
#diff203nsT = np.copy(S200values)
#diff203woT = np.copy(S200values)

for i in range(len(S200wo2values)):
       #diff200ns[i] = S200NSvalues[i]-S200values[i]
       #diff200wo[i] = S200WOvalues[i]-S200values[i]
       #diff200nsG[i] = S200NSgrassvalues[i]-S200values[i]
       diff200woG[i] = S200WOgrassvalues[i]-S200wo2values[i]
       diff200woG50[i] = S200WOgrass50values[i]-S200wo2values[i]
       #diff200nsT[i] = S200NStreesvalues[i]-S200values[i]
       diff200woT[i] = S200WOtreesvalues[i]-S200wo2values[i]
       diff200woT50[i] = S200WOtrees50values[i]-S200wo2values[i]
       #diff203ns[i] = S203NSvalues[i]-S200values[i]
       #diff203wo[i] = S203WOvalues[i]-S200values[i]
       #diff203nsG[i] = S203NSgrassvalues[i]-S200values[i]
       #diff203woG[i] = S203WOgrassvalues[i]-S200values[i]
       #diff203nsT[i] = S203NStreesvalues[i]-S200values[i]
       #diff203woT[i] = S203WOtreesvalues[i]-S200values[i]

start = datetime.datetime(2017,6,19,0)
#print start.hour
#numminutes= 1440
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
#print len(S200values)
#print xaxis

fig1 = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax1.set_title(u"Vegetation,Asphalt,Canyon:HW1,20.6.2017")
#ax1.plot(timelist,S200values, label="Asphalt,Putz", color="orange")


ax1.plot(timelist[:-144],S200wo2_WSN_RD[:-144], label="Asphalt-WSNRD", color="violet")#,linestyle="dashed")
ax1.plot(timelist[:-144],S200wo2_RSN_RD[:-144], label="Asphalt-RSNRD", color="red")#,linestyle="dashed")

ax1.plot(timelist[:-144],S200wo2values[:-144], label="Asphalt", color="black")#,linestyle="dashed")
ax1.plot(timelist[:-144],S200WOgrassvalues[:-144], label=u"25% Wiese", color="green")#,linestyle="dashed")
ax1.plot(timelist[:-144],S200WOgrass50values[:-144], label=u"50% Wiese", color="green",linestyle=":")#,linestyle="dashed")
ax1.plot(timelist[:-144],S200WOtreesvalues[:-144], label=u"25% Bäume", color="blue")#,linestyle="dashed")
ax1.plot(timelist[:-144],S200WOtrees50values[:-144], label=u"50% Bäume", color="blue",linestyle=":")#,linestyle="dashed")


#ax1.plot(timelist,S200WOvalues, label="Asphalt", color="orange")#,linestyle="dashed")
#ax1.plot(timelist,S200NSvalues, color="orange",linestyle=":")
#ax1.plot(timelist,S200NSgrassvalues, color="green",linestyle=":")
#ax1.plot(timelist,S200NStreesvalues, color="blue",linestyle=":")
#ax1.plot(timelist,S203values, label="Beton,Beton", color="turquoise")
#ax1.plot(timelist,S203WOvalues, label=r"$\alpha$ :0.56,0.56", color="turquoise",linestyle="dashed")
#ax1.plot(timelist,S203NSvalues, color="turquoise",linestyle=":")
#ax2.plot(timelist,diff200nsG, color="green",linestyle=":")
ax2.plot(timelist,diff200woG, color="green")
ax2.plot(timelist,diff200woG50, color="green",linestyle=":")
#ax2.plot(timelist,diff200nsT, color="blue", linestyle=":")
ax2.plot(timelist,diff200woT, color="blue",)
ax2.plot(timelist,diff200woT50, color="blue",linestyle=":")
#ax2.plot(timelist,diff203, label="Beton,Beton", color="turquoise")
ax2.set_ylabel(u'Diff. zu Asphalt+Putz[°C]')

ax1.legend(loc="lower center",fontsize='small')
ax1.set_ylabel(u'UTCI [°C]')
ax2.set_xlabel('[UTC]')
plt.show()
exit()

fig2 = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax1.set_title(u"Vegetation,Beton,Straßenorientierung,Canyon:HW1, 19.6.2017")
#ax1.plot(timelist,S200values, label="Asphalt,Putz", color="orange")
ax1.plot(timelist,S203WOvalues, label="Beton", color="orange")#,linestyle="dashed")
ax1.plot(timelist,S203NSvalues, color="orange",linestyle=":")
ax1.plot(timelist,S203WOgrassvalues, label=u"25% Wiese", color="green")#,linestyle="dashed")
ax1.plot(timelist,S203NSgrassvalues, color="green",linestyle=":")
ax1.plot(timelist,S203WOtreesvalues, label=u"25% Bäume", color="blue")#,linestyle="dashed")
ax1.plot(timelist,S203NStreesvalues, color="blue",linestyle=":")
#ax1.plot(timelist,S203values, label="Beton,Beton", color="turquoise")
#ax1.plot(timelist,S203WOvalues, label=r"$\alpha$ :0.56,0.56", color="turquoise",linestyle="dashed")
#ax1.plot(timelist,S203NSvalues, color="turquoise",linestyle=":")
ax1.set_ylabel(u'UTCI Shade[°C]')
ax1.legend(loc="lower center",fontsize='small')
ax2.plot(timelist,diff203nsG, color="green",linestyle=":")
ax2.plot(timelist,diff203woG, color="green")
ax2.plot(timelist,diff203nsT, color="blue", linestyle=":")
ax2.plot(timelist,diff203woT, color="blue",)
#ax2.plot(timelist,diff203, label="Beton,Beton", color="turquoise")
ax2.set_ylabel(u'Diff. zu Asphalt+Putz[°C]')
ax2.set_xlabel('[UTC]')
plt.show()