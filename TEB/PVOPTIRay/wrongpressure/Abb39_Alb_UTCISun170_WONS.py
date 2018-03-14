# -*- coding: utf-8 -*-
__author__ = 'lnx'

import pandas as pd
import matplotlib.pyplot as plt
from TEB.displaySURFEX.CONVERTSURFEXTEXTE_UTCI import loadfile
import numpy as np
import datetime
import matplotlib.gridspec as gridspec

#PVfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/TCANYON.TXT"
#STQfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/TCANYON.TXT"
#test = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/TCANYON.TXT"
S100 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/100_Platz_A_N/2017_170/UTCI_OUTSUN.TXT"
S101 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/101_Platz_B_N/2017_170/UTCI_OUTSUN.TXT"
S102 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/102_Platz_A_A/2017_170/UTCI_OUTSUN.TXT"
S103 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/103_Platz_B_B/2017_170/UTCI_OUTSUN.TXT"

S200 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170/UTCI_OUTSUN.TXT"
S200ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170NS/UTCI_OUTSUN.TXT"
S200wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170WO/UTCI_OUTSUN.TXT"

S201 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170/UTCI_OUTSUN.TXT"
S201ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170NS/UTCI_OUTSUN.TXT"
S201wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170WO/UTCI_OUTSUN.TXT"
S201ns_t = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170NS/TCANYON.TXT"
S201wo_t = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170WO/TCANYON.TXT"


S202 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/202_Kreuzung_A_A/2017_170/UTCI_OUTSUN.TXT"
S202ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/202_Kreuzung_A_A/2017_170NS/UTCI_OUTSUN.TXT"
S202wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/202_Kreuzung_A_A/2017_170WO/UTCI_OUTSUN.TXT"

S203 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B/2017_170/UTCI_OUTSUN.TXT"
S203ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B/2017_170NS/UTCI_OUTSUN.TXT"
S203wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B/2017_170WO/UTCI_OUTSUN.TXT"
S203ns_t = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B/2017_170NS/TCANYON.TXT"
S203wo_t = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/203_Kreuzung_B_B/2017_170WO/TCANYON.TXT"


S204 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/204_Kreuzung_B_W/2017_170/UTCI_OUTSUN.TXT"
S204ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/204_Kreuzung_B_W/2017_170NS/UTCI_OUTSUN.TXT"#
S204wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/204_Kreuzung_B_W/2017_170WO/UTCI_OUTSUN.TXT"#
S204ns_t = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/204_Kreuzung_B_W/2017_170NS/TCANYON.TXT"
S204wo_t = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/204_Kreuzung_B_W/2017_170WO/TCANYON.TXT"



S205 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/205_Kreuzung_W_W/2017_170/UTCI_OUTSUN.TXT"
S205ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/205_Kreuzung_W_W/2017_170NS/UTCI_OUTSUN.TXT"
S205wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/205_Kreuzung_W_W/2017_170WO/UTCI_OUTSUN.TXT"


S110 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/110_Platz_A_PV70/2017_170/UTCI_OUTSUN.TXT"
S111 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/111_Platz_B_PV70/2017_170/UTCI_OUTSUN.TXT"
S112 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/112_Platz_A_PV100/2017_170/UTCI_OUTSUN.TXT"
S113 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/113_Platz_B_PV100/2017_170/UTCI_OUTSUN.TXT"

S210 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/210_Kreuzung_A_PV70/2017_170/UTCI_OUTSUN.TXT"
S210ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/210_Kreuzung_A_PV70/2017_170_NS/UTCI_OUTSUN.TXT"
S210wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/210_Kreuzung_A_PV70/2017_170_WO/UTCI_OUTSUN.TXT"

S211 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/211_Kreuzung_B_PV70/2017_170/UTCI_OUTSUN.TXT"
S211ns = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/211_Kreuzung_B_PV70/2017_170_NS/UTCI_OUTSUN.TXT"
S211wo = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/211_Kreuzung_B_PV70/2017_170_WO/UTCI_OUTSUN.TXT"

S212 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/212_Kreuzung_A_PV100/2017_170/UTCI_OUTSUN.TXT"
S213 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/213_Kreuzung_B_PV100/2017_170/UTCI_OUTSUN.TXT"

#FORCfile = "/home/lnx/MODELS/SURFEX/3_input/met_forcing/201706_08_BOKU_ENGBA.txt"
#PVvalues = loadfile(PVfile)
#test = loadfile(test)
S200values = loadfile(S200)
S200NSvalues = loadfile(S200ns)
S200WOvalues = loadfile(S200wo)
S201values = loadfile(S201)
S201NSvalues = loadfile(S201ns)
S201WOvalues = loadfile(S201wo)
S201NSvaluesT = loadfile(S201ns_t)
S201WOvaluesT = loadfile(S201wo_t)
S202values = loadfile(S202)
S202NSvalues = loadfile(S202ns)
S202WOvalues = loadfile(S202wo)
S203values = loadfile(S203)
S203NSvalues = loadfile(S203ns)
S203WOvalues = loadfile(S203wo)
S203NSvaluesT = loadfile(S203ns_t)
S203WOvaluesT = loadfile(S203wo_t)
S204values = loadfile(S204)
S204NSvalues = loadfile(S204ns)
S204WOvalues = loadfile(S204wo)
S204NSvaluesT = loadfile(S204ns_t)
S204WOvaluesT = loadfile(S204wo_t)
S205values = loadfile(S205)
S205NSvalues = loadfile(S205ns)
S205WOvalues = loadfile(S205wo)
S100values = loadfile(S100)
S101values = loadfile(S101)
S102values = loadfile(S102)
S103values = loadfile(S103)
S210values = loadfile(S210)
S210NSvalues = loadfile(S210ns)
S210WOvalues = loadfile(S210wo)
S211values = loadfile(S211)
S211NSvalues = loadfile(S211ns)
S211WOvalues = loadfile(S211wo)

S212values = loadfile(S212)
S213values = loadfile(S213)
S110values = loadfile(S110)
S111values = loadfile(S111)
S112values = loadfile(S112)
S113values = loadfile(S113)
#FORCvalues = pd.read_csv(FORCfile, delimiter=r"\s+", skiprows=range(1,720)) #cut only last day = 30.8.2017
#FORCvalues = FORCvalues[720:]
#print PVvalues, STQvalues, FORCvalues['Td']
diff101 = np.copy(S100values)
diff102 = np.copy(S100values)
diff103 = np.copy(S100values)
diff201 = np.copy(S100values)
diff202 = np.copy(S100values)
diff203 = np.copy(S100values)
diff204 = np.copy(S100values)
diff205 = np.copy(S100values)
diff210 = np.copy(S100values)
diff211 = np.copy(S100values)
diff110 = np.copy(S100values)
diff111 = np.copy(S100values)

for i in range(len(S100values)):
       diff101[i] = S101values[i]-S100values[i]
       diff102[i] = S102values[i]-S100values[i]
       diff103[i] = S103values[i]-S100values[i]
       diff110[i] = S110values[i]-S100values[i]
       diff111[i] = S111values[i]-S100values[i]

       diff201[i] = S201values[i]-S200values[i]
       diff202[i] = S202values[i]-S200values[i]
       diff203[i] = S203values[i]-S200values[i]
       diff204[i] = S204values[i]-S200values[i]
       diff205[i] = S205values[i]-S200values[i]
       diff210[i] = S210values[i]-S200values[i]
       diff211[i] = S211values[i]-S200values[i]

start = datetime.datetime(2017,6,19,0)
#print start.hour
numminutes = 1440
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
print len(S100values)
print xaxis

fig = plt.figure()
ax1 = fig.add_subplot(111)

#gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
#ax1 = plt.subplot(gs[0])
#ax2 = plt.subplot(gs[1])
ax1.set_title(u"Materialien,Straßenorientierung, Canyon:HW1, 19.6.2017")
#ax1.plot(timelist,S202values, label=u"Asphalt,dunkle Fassade", color="red") #u"α=0.13,0.13"
ax1.plot(timelist,S202WOvalues, label=r"$\alpha_{g}$:0,13;$\alpha_{w}$:0,13", color="red")#,linestyle="dashed")
ax1.plot(timelist,S202NSvalues, color="red",linestyle=":")
#ax1.plot(timelist,S200values, label="Asphalt,Putz", color="orange")
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
ax1.set_ylabel(u'UTCI 2m [°C]')
ax1.legend(loc="lower center",fontsize='small')
#ax2.plot(timelist,diff201, label="Beton,Putz", color="green")
#ax2.plot(timelist,diff202, label="Asphalt,dunkle Fassade", color="red")
#ax2.plot(timelist,diff203, label="Beton,Beton", color="turquoise")
#ax2.plot(timelist,diff204, label=u"Beton,Weiß", color="blue")
#ax2.plot(timelist,diff205, label=u"Weiß,Weiß", color="violet")
#ax2.set_ylabel(u'Diff. zu Asphalt+Putz[°C]')
ax1.set_xlabel('[UTC]')
#plt.show()

#10:30-11:30: -> [63:70;207:214]
#13:30-14:30: -> [78:85;222:229]



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

axes = plt.gca()
#m1, b1 = np.polyfit(UT11_wo,x,1)
#m2, b2 = np.polyfit(UT14_wo,x,1)
#m3, b3 = np.polyfit(TUT11_wo,x,1)
#m4, b4 = np.polyfit(TUT14_wo,x,1)
#X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
#ax.plot(X_plot, m1*X_plot + b1, '-', color="#d95f02")
#ax.plot(X_plot, m2*X_plot + b2, '-', color="grey")
#ax2.plot(X_plot, m3*X_plot + b3, '-', color="blue") ##1b9e77
#ax2.plot(X_plot, m4*X_plot + b4, '-', color="orange")

plt.title(r"$\alpha_{g}$=0.56")
ax.set_xlabel(r"$\alpha_{w}$")
ax.set_ylabel(u"air temperature [°C]")
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
ax.set_ylim(29,33)
ax2.set_ylim(38,41.5)
ax.legend(loc="upper center",ncol=3)
ax2.legend(loc="lower center",ncol=3)
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
ax.legend(loc="upper center")
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
plt.legend(loc="upper center")
plt.show()


