# -*- coding: utf-8 -*-
__author__ = 'lnx'

import datetime

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from TEB.displaySURFEX.CONVERTSURFEXTEXTE import loadfile

#S200 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170/TCANYON.TXT"
#S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170NS/TCANYON.TXT"
S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171WO/TCANYON.TXT"
#S200nsGrass = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_25Grass/2017_170NS/TCANYON.TXT"
S200woGrass = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_25Grass/2017_170171WO/TCANYON.TXT"
S200woGrass50 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_50Grass/2017_170171WO/TCANYON.TXT"
#S200nsTrees = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_25Trees/2017_170NS/TCANYON.TXT"
S200woTrees = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_25Trees/2017_170171WO/TCANYON.TXT"
S200woTrees50 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N_50Trees/2017_170171WO/TCANYON.TXT"

S203 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B/2017_170/TCANYON.TXT"
S203ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B/2017_170NS/TCANYON.TXT"
S203wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B/2017_170WO/TCANYON.TXT"
S203nsGrass = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B_25Grass/2017_170NS/TCANYON.TXT"
S203woGrass = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B_25Grass/2017_170WO/TCANYON.TXT"
S203nsTrees = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B_25Trees/2017_170NS/TCANYON.TXT"
S203woTrees = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B_25Trees/2017_170WO/TCANYON.TXT"

#S200values = loadfile(S200)
#S200NSvalues = loadfile(S200ns)
S200WOvalues = loadfile(S200wo)
#S200NSgrassvalues = loadfile(S200nsGrass)
S200WOgrassvalues = loadfile(S200woGrass)
S200WOgrass50values = loadfile(S200woGrass50)
#S200NStreesvalues = loadfile(S200nsTrees)
S200WOtreesvalues = loadfile(S200woTrees)
S200WOtrees50values = loadfile(S200woTrees50)

S203values = loadfile(S203)
S203NSvalues = loadfile(S203ns)
S203WOvalues = loadfile(S203wo)
S203NSgrassvalues = loadfile(S203nsGrass)
S203WOgrassvalues = loadfile(S203woGrass)
S203NStreesvalues = loadfile(S203nsTrees)
S203WOtreesvalues = loadfile(S203woTrees)

#diff200ns = np.copy(S200values)
diff200wo = np.copy(S200WOvalues)
#diff200nsG = np.copy(S200values)
diff200woG = np.copy(S200WOvalues)
diff200woG50 = np.copy(S200WOvalues)
#diff200nsT = np.copy(S200values)
diff200woT = np.copy(S200WOvalues)
diff200woT50 = np.copy(S200WOvalues)
#diff203 = np.copy(S200values)
#diff203ns = np.copy(S200values)
#diff203wo= np.copy(S200values)
#diff203nsG = np.copy(S200values)
#diff203woG = np.copy(S200values)
#diff203nsT = np.copy(S200values)
#diff203woT = np.copy(S200values)


for i in range(len(S200WOvalues)):
       #diff200ns[i] = S200NSvalues[i]-S200values[i]
       #diff200wo[i] = S200WOvalues[i]-S200values[i]
       #diff200nsG[i] = S200NSgrassvalues[i]-S200values[i]
       diff200woG[i] = S200WOgrassvalues[i]-S200WOvalues[i]
       diff200woG50[i] = S200WOgrass50values[i]-S200WOvalues[i]
       #diff200nsT[i] = S200NStreesvalues[i]-S200values[i]
       diff200woT[i] = S200WOtreesvalues[i]-S200WOvalues[i]
       diff200woT50[i] = S200WOtrees50values[i]-S200WOvalues[i]
       #diff203ns[i] = S203NSvalues[i]-S200values[i]
       #diff203wo[i] = S203WOvalues[i]-S200values[i]
       #diff203nsG[i] = S203NSgrassvalues[i]-S200values[i]
       #diff203woG[i] = S203WOgrassvalues[i]-S200values[i]
       #diff203nsT[i] = S203NStreesvalues[i]-S200values[i]
       #diff203woG[i] = S203WOgrassvalues[i]-S200values[i]

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
#print timelist
#print len(S200values)
#print xaxis

fig1 = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax1.set_title(u"Vegetation,Straßenorientierung, Canyon:HW1, 20.6.2017")
#ax1.plot(timelist,S200values, label="Asphalt,Putz", color="orange")
ax1.plot(timelist[:-144],S200WOvalues[:-144], label="Asphalt", color="orange")#,linestyle="dashed")
#ax1.plot(timelist,S200NSvalues, color="orange",linestyle=":")
ax1.plot(timelist[:-144],S200WOgrassvalues[:-144], label=u"25% Wiese", color="green")#,linestyle="dashed")
ax1.plot(timelist[:-144],S200WOgrass50values[:-144], label=u"50% Wiese", color="green",linestyle=":")
#ax1.plot(timelist,S200NSgrassvalues, color="green",linestyle=":")
ax1.plot(timelist[:-144],S200WOtreesvalues[:-144], label=u"25% Bäume", color="blue")#,linestyle="dashed")
ax1.plot(timelist[:-144],S200WOtrees50values[:-144], label=u"50% Bäume", color="blue",linestyle=":")
#ax1.plot(timelist,S200NStreesvalues, color="blue",linestyle=":")
#ax1.plot(timelist,S203values, label="Beton,Beton", color="turquoise")
#ax1.plot(timelist,S203WOvalues, label=r"$\alpha$ :0.56,0.56", color="turquoise",linestyle="dashed")
#ax1.plot(timelist,S203NSvalues, color="turquoise",linestyle=":")
ax1.set_ylabel(u'Lufftemperatur 2m [°C]')
ax1.legend(loc="lower center",fontsize='small')
#ax2.plot(timelist,diff200nsG, color="green",linestyle=":")
ax2.plot(timelist[:-144],diff200woG[:-144], color="green")
ax2.plot(timelist[:-144],diff200woG50[:-144], color="green", linestyle=":")
#ax2.plot(timelist,diff200nsT, color="blue", linestyle=":")
ax2.plot(timelist[:-144],diff200woT[:-144], color="blue",)
ax2.plot(timelist[:-144],diff200woT50[:-144], color="blue", linestyle=":")
#ax2.plot(timelist,diff203, label="Beton,Beton", color="turquoise")
ax2.set_ylabel(u'Diff. zu Asphalt+Putz[°C]')
ax2.set_xlabel('[UTC]')
plt.show()

exit()

fig2 = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax1.set_title(u"Einfluss PV/Boden, Platz - HW0.2, 19.6.2017")
#ax.plot(PVvalKreuzungues, label="Asphalt + PV")
ax1.plot(timelist,S110values, label="Asphalt + 70%PV", color="orange")
#ax.plot(S113values, label="Asphalt + 100%PV", color="red")
ax1.plot(timelist,S111values, label="Beton + 70%PV", color="turquoise")
#ax.plot(S112values, label="Beton + 100%PV", color="blue")
#ax.plot(FORCvalues['Td'],label="Forcing (Dach)")
ax1.set_ylabel(u'Lufftemperatur 2m [°C]')
ax1.legend(loc="lower center",fontsize='small')
ax2.plot(timelist,diff110, label="Aspalt,PV", color="orange")
ax2.plot(timelist,diff111, label="Beton,PV", color="turquoise")
ax2.set_ylabel(u'Diff. zu Asphalt+Putz[°C]')
ax2.set_xlabel('[UTC]')
plt.show()
plt.show()


fig3 = plt.figure()
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax1.set_title(u"Einfluss PV/Boden, Kreuzung - HW1, 19.6.2017")
#ax.plot(PVvalKreuzungues, label="Asphalt + PV")
ax1.plot(timelist,S210values, label="Asphalt,70%PV", color="orange")
#ax1.plot(timelist,S210NSvalues, label="Asphalt,70%PV,N-S", color="orange", linestyle="dashed" )
ax1.plot(timelist,S210WOvalues, label="Asphalt,70%PV,W-O", color="orange",linestyle=":")
#ax.plot(S213values, label="Asphalt + 100%PV", color="red")
#ax1.plot(timelist,S211values, label="Beton,70%PV", color="turquoise")
#ax1.plot(timelist,S211NSvalues, label="Beton,70%PV,N-S", color="turquoise", linestyle="dashed")
ax1.plot(timelist,S211WOvalues, label="Beton,70%PV,W-O", color="turquoise", linestyle=":")
#ax.plot(S212values, label="Beton + 100%PV", color="blue")
#ax1.plot(timelist,FORCvalues['Td'],label="Forcing (Dach)")
ax1.set_ylabel(u'Lufftemperatur 2m [°C]')
ax1.legend(loc="lower center",fontsize='small')
ax2.plot(timelist,diff210, label="Asphalt,PV", color="orange")
ax2.plot(timelist,diff211, label="Beton,PV", color="turquoise")
ax2.set_ylabel(u'Diff. zu Asphalt+Putz[°C]')
ax2.set_xlabel('[UTC]')
plt.show()
plt.show()



fig = plt.figure()
ax = fig.add_subplot(111)
plt.title("Einfluss des Vegetation bei Asphalt")
#ax.plot(PVvalues, label="PV(canyon)")
#ax.plot(test, label="test")
ax.plot(STQvalues, label="keine Vegetation")
ax.plot(S2values, label="Wiese")
ax.plot(S3values, label="Park")
#ax.plot(FORCvalues['Td'],label="Forcing (Dach)")
ax.set_ylabel(u'Lufftemperatur 2m [°C]')
ax.set_xlabel('[10min seit 0UTC]')
ax.legend(loc="upper left")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
plt.title("Einfluss des Vegetation bei Beton")
#ax.plot(PVvalues, label="PV(canyon)")
ax.plot(S4values, label="keine Vegetation")
ax.plot(S5values, label="Wiese")
ax.plot(S6values, label="Park")
ax.plot(FORCvalues['Td'],label="Forcing (Dach)")
ax.set_ylabel(u'Lufftemperatur 2m [°C]')
ax.set_xlabel('[10min seit 0UTC]')
plt.legend(loc="upper left")
plt.show()


