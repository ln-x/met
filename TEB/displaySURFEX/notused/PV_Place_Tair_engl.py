# -*- coding: utf-8 -*-
__author__ = 'lnx'

import pandas as pd
import matplotlib.pyplot as plt
from TEB.displaySURFEX.CONVERTSURFEXTEXTE import loadfile

PVfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/TCANYON.TXT"
#STQfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/TCANYON.TXT"
#test = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/TCANYON.TXT"
STQfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/1_Platz_A_N/2017_242/TCANYON.TXT"
S2 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/2_Platz_A_N_Wiese/2017_242/TCANYON.TXT"
S3 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/3_Platz_A_N_Park/2017_242/TCANYON.TXT"
S4 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/4_Platz_B_N/2017_242/TCANYON.TXT"
S5 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/5_Platz_B_N_Wiese/2017_242/TCANYON.TXT"
S6 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/6_Platz_B_N_Park/2017_242/TCANYON.TXT"
FORCfile = "/home/lnx/MODELS/SURFEX/3_input/met_forcing/201706_08_BOKU_ENGBA.txt"
PVvalues = loadfile(PVfile)
#test = loadfile(test)
STQvalues = loadfile(STQfile)
S2values = loadfile(S2)
S3values = loadfile(S3)
S4values = loadfile(S4)
S5values = loadfile(S5)
S6values = loadfile(S6)

FORCvalues = pd.read_csv(FORCfile, delimiter=r"\s+", skiprows=range(1,720)) #cut only last day = 30.8.2017
#FORCvalues = FORCvalues[720:]
#print PVvalues, STQvalues, FORCvalues['Td']

fig = plt.figure()
ax = fig.add_subplot(111)
plt.title(u"Influence of Materials")
ax.plot(PVvalues, label="asphalt + PV")
ax.plot(STQvalues, label="asphalt + plaster")#, color="red")
ax.plot(S4values, label="concrete + plaster")#, color="blue")
ax.plot(FORCvalues['Td'],label="forcing (roof)")
ax.set_ylabel(u'canyon air temperature [°C]')
ax.set_xlabel('[10min since 0UTC]')
ax.legend(loc="upper left")
plt.show()

exit()

fig = plt.figure()
ax = fig.add_subplot(111)
plt.title("Einfluss des Vegetation bei Asphalt")
#ax.plot(PVvalues, label="PV(canyon)")
#ax.plot(test, label="test")
ax.plot(STQvalues, label="keine Vegetation")
ax.plot(S2values, label="Wiese")
ax.plot(S3values, label="Park")
ax.plot(FORCvalues['Td'],label="Forcing (Dach)")
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


