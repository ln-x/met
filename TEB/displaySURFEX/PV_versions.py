# -*- coding: utf-8 -*-
__author__ = 'lnx'

import pandas as pd
import matplotlib.pyplot as plt
from CONVERTSURFEXTEXTE import loadfile

PVfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/TCANYON.TXT"
STQfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/TCANYON.TXT"
FORCfile = "/home/lnx/MODELS/SURFEX/3_input/met_forcing/201706_08_BOKU_ENGBA.txt"
PVvalues = loadfile(PVfile)
STQvalues = loadfile(STQfile)
FORCvalues = pd.read_csv(FORCfile, delimiter=r"\s+", skiprows=range(1,720)) #cut only last day = 30.8.2017
#FORCvalues = FORCvalues[720:]
print PVvalues, STQvalues, FORCvalues['Td']

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(PVvalues, label="PV(canyon)")
ax.plot(STQvalues, label="STQ(canyon)")
ax.plot(FORCvalues['Td'],label="FORC(roof)")
plt.legend()
plt.show()



