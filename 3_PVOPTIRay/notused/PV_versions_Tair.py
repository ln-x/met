# -*- coding: utf-8 -*-
__author__ = 'lnx'

import matplotlib.pyplot as plt
import pandas as pd
from TEB.displaySURFEX.CONVERTSURFEXTEXTE import loadfile

#PVfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/TCANYON.TXT"
#STQfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/TCANYON.TXT"
STQfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/1_Platz_A_N/TCANYON.TXT"
S2 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/2_Platz_A_N_Wiese/TCANYON.TXT"
S3 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/3_Platz_A_N_Park/TCANYON.TXT"
S4 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/4_Platz_B_N/TCANYON.TXT"
S5 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/5_Platz_B_N_Wiese/TCANYON.TXT"
S6 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/6_Platz_B_N_Park/TCANYON.TXT"
FORCfile = "/home/lnx/MODELS/SURFEX/3_input/met_forcing/201706_08_BOKU_ENGBA.txt"
#PVvalues = loadfile(PVfile)
STQvalues = loadfile(STQfile)

FORCvalues = pd.read_csv(FORCfile, delimiter=r"\s+", skiprows=range(1,720)) #cut only last day = 30.8.2017
#FORCvalues = FORCvalues[720:]
#print PVvalues, STQvalues, FORCvalues['Td']

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(PVvalues, label="PV(canyon)")
ax.plot(STQvalues, label="STQ(canyon)")
ax.plot(FORCvalues['Td'],label="FORC(roof)")
plt.legend()
plt.show()



