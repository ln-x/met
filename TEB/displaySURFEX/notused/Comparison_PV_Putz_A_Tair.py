# -*- coding: utf-8 -*-
__author__ = 'lnx'

import pandas as pd
import matplotlib.pyplot as plt
from TEB.displaySURFEX.CONVERTSURFEXTEXTE import loadfile

#PVfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/TCANYON.TXT"
#STQfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/TCANYON.TXT"
#test = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/TCANYON.TXT"
S100 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/100_Platz_A_N/2017_170/TCANYON.TXT"
S200 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170/TCANYON.TXT"
S110 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/110_Platz_A_PV70/2017_170/TCANYON.TXT"
S210 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/210_Kreuzung_A_PV70/2017_170/TCANYON.TXT"
#FORCfile = "/home/lnx/MODELS/SURFEX/3_input/met_forcing/201706_08_BOKU_ENGBA.txt"
#PVvalues = loadfile(PVfile)
#test = loadfile(test)
S200values = loadfile(S200)
S100values = loadfile(S100)
S210values = loadfile(S210)
S110values = loadfile(S110)
#FORCvalues = pd.read_csv(FORCfile, delimiter=r"\s+", skiprows=range(1,720)) #cut only last day = 30.8.2017
#FORCvalues = FORCvalues[720:]
#print PVvalues, STQvalues, FORCvalues['Td']

fig = plt.figure()
ax = fig.add_subplot(111)
plt.title(u"Vergleich HW, Putz vs. PV, 19.6.2017")
#ax.plot(PVvalKreuzungues, label="Asphalt + PV")
ax.plot(S100values, label="Asphalt + Putz, Platz ", color="orange", linestyle="dashed")
ax.plot(S110values, label="Asphalt + PV70%, Platz", color="blue", linestyle="dashed")
ax.plot(S200values, label="Asphalt + Putz, Kreuzung", color="orange")
ax.plot(S210values, label="Asphalt + PV70%, Kreuzung", color="blue")
#ax.plot(FORCvalues['Td'],label="Forcing (Dach)")
ax.set_ylabel(u'Lufftemperatur 2m [°C]')
ax.set_xlabel('[10min seit 0UTC]')
ax.legend(loc="lower right")
plt.show()
