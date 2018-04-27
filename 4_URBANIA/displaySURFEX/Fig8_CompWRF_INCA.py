# -*- coding: utf-8 -*-
__author__ = 'lnx'
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

IS = pd.read_csv('/home/lnx/METDATA/Imran_StationExtraction/D3_INCA_SURFEX_Innerestadt.txt', delimiter=r"\s+")
GE = pd.read_csv('/home/lnx/METDATA/Imran_StationExtraction/D3_INCA_GrossEnzersdorf.txt', delimiter=r"\s+")
#print GE["INCA"].head()

R2_WRF_IS = (stats.spearmanr(IS["D3"], IS["INCA"])[0]**2)
R2_S0_IS = (stats.spearmanr(IS["S0"], IS["INCA"])[0]**2)
R2_WRF_GE = (stats.spearmanr(GE["D3"], GE["INCA"])[0]**2)
Bias_WRF_IS = np.average(IS["D3"]- IS["INCA"])
Bias_S0_IS = np.average(IS["S0"]- IS["INCA"])
Bias_WRF_GE = np.average(GE["D3"]- GE["INCA"])
#print R2_WRF_GE,R2_WRF_IS

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.plot(IS["INCA"][:175], color='black', label="OBS")
ax1.plot(IS["D3"][:175],color='blue', label="WRF")
ax1.plot(IS["S0"][:175], color='red', label="WRF/S")
ax1.set_xlabel("hours[UTC]")
ax1.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
ax1.legend(loc='upper right')
ax1.set_xlim(0, 255)
ax1.set_title(u"Innere Stadt", size="large")

ax2 = fig.add_subplot(222)
ax2.scatter(IS["D3"], IS["INCA"], color='blue', label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_WRF_IS, Bias_WRF_IS)))
ax2.scatter(IS["S0"], IS["INCA"], color='red', label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_S0_IS, Bias_S0_IS)))
ax2.set_xlabel(r"$T_{air_2m}$"u'[°C]', size="large")
ax2.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
ax2.legend(loc='upper left')

ax3 = fig.add_subplot(223)
ax3.plot(GE["D3"], color='black', label="WRF")
ax3.plot(GE["INCA"], color='blue', label="OBS")
ax3.set_xlabel("hours[UTC]")
ax3.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
ax3.legend(loc='upper right')
ax3.set_xlim(0, 255)
ax3.set_title(u"Groß-Enzersdorf", size="large")  # +"2m air temperature"))

ax4 = fig.add_subplot(224)
ax4.scatter(GE["D3"], GE["INCA"], color='blue', label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_WRF_GE, Bias_WRF_GE)))  # , s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax4.set_xlabel(r"$T_{air_2m}$"u'[°C]', size="large")
ax4.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
ax4.legend(loc='upper left')

#plt.suptitle(u"Groß-Enzersdorf", size="large")  # +"2m air temperature"))
plt.show()
