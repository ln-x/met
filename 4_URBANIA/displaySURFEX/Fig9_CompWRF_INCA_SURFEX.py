# -*- coding: utf-8 -*-
__author__ = 'lnx'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from CONVERTSURFEXNC_TXT import *
from scipy import stats
import sys
import matplotlib.gridspec as gridspec

IS = pd.read_csv('/home/lnx/METDATA/Imran_StationExtraction/D3_INCA_Innerestadt.txt', delimiter=r"\s+")
GE = pd.read_csv('/home/lnx/METDATA/Imran_StationExtraction/D3_INCA_GrossEnzersdorf.txt', delimiter=r"\s+")
#print GE["INCA"].head()

'''
ZAMG - groundstations 

Coordinates: 
11034 Wien-Innere Stadt (85.5, 54.4, [16.366944444444446, 48.19833333333333])
11035 Wien-Hohe Warte (82.2, 69.7, [16.35638888888889, 48.24861111111111])
11036 Schwechat (147.3, 27.5, [16.56972222222222, 48.11027777777778])
11037 Gross-Enzersdorf (144.1, 54.8, [16.559166666666666, 48.19972222222222])
11040 Wien-Unterlaa (101.5, 32.0, [16.419444444444444, 48.125])
11042 Wien-Stammersdorf (97.2, 87.1, [16.405555555555555, 48.30583333333333])
11077 Brunn am Gebirge (55.9, 26.5, [16.27, 48.106944444444444])
11080 Wien-Mariabrunn (43.5, 57.0, [16.229444444444443, 48.206944444444446])
11090 Wien-Donaufeld (105.1, 72.3, [16.43138888888889, 48.257222222222225])

Parameters:
datum = 1_year_month_day
stdmin = minutes
tl = air temperature [1/10 degC]
k27 = global radiation [Watt/m2]
rf = rel Feuchte [%]
rr = Niederschlag 1/10 mm 10-Min-Summe
p = Luftdruck 1/10 hpascal
ff = Windstaerke [1/10 m/s] (Vektorielles 10 min Mittel,bezogen auf dd)
so = Sonnenscheindauer [seconds]
ts = 5cm air temperature
'''

ZAMGstation = "/home/lnx/METDATA/ZAMG_filled/tawes_11040_year_2015.txt"
ZAMGdata = pd.read_csv(ZAMGstation, delimiter=r"\s+")#, parse_dates=['datum'])
Day1 = ZAMGdata.loc[ZAMGdata['datum'] == 1150717] #cut episode
Day1 = Day1.loc[ZAMGdata['stdmin'] >= 1800] #cut episode
Day2 = ZAMGdata.loc[ZAMGdata['datum'] == 1150718] #cut episode
Day3 = ZAMGdata.loc[ZAMGdata['datum'] == 1150719] #cut episode
Day4 = ZAMGdata.loc[ZAMGdata['datum'] == 1150720] #cut episode
Day5 = ZAMGdata.loc[ZAMGdata['datum'] == 1150721] #cut episode
Day6 = ZAMGdata.loc[ZAMGdata['datum'] == 1150722] #cut episode
Day7 = ZAMGdata.loc[ZAMGdata['datum'] == 1150723] #cut episode
Day8 = ZAMGdata.loc[ZAMGdata['datum'] == 1150724] #cut episode
Day9 = ZAMGdata.loc[ZAMGdata['datum'] == 1150725] #cut episode
Day10 = ZAMGdata.loc[ZAMGdata['datum'] == 1150726] #cut episode
Day11 = ZAMGdata.loc[ZAMGdata['datum'] == 1150727] #cut episode
Day12 = ZAMGdata.loc[ZAMGdata['datum'] == 1150728] #cut episode
ZAMG_episode = pd.concat([Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10, Day11, Day12], axis=0)
date = ZAMG_episode['datum'].iloc[0]
date1 = str(date).split()
date_start = date1[0][5:7] +"." +date1[0][3:5] +".20"+ date1[0][1:3]
ZAMG_TA = ZAMG_episode['tl']/10 #extract 2M air temperature and bring to °C
ZAMG_TA_hourly = ZAMG_TA[0::6]  #s[i:j:k]  slice of s from i to j with step k
#print ZAMG_TA_hourly
'''
WRF online and SURFEX offline runs ... HERE THE CORRECT FILEPATHS NEED TO BE CHECKED
'''
simpath="/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/"
#FORCING_IS = simpath+"FORCING/T2M_11034.txt"
SURFEX_S0_IS = simpath+"S0_FORC_WRF_333_STQ_long/T2M_11034.txt"
SURFEX_S12_IS = simpath+"S12_FORC_WRF_333_STQ_2DURBPARAM_long_corr/T2M_11034.txt"
FORCING_UL = simpath+"FORCING/T2M_11040.txt"
SURFEX_S0_UL = simpath+"S0_FORC_WRF_333_STQ_long/T2M_11040.txt"
SURFEX_S12_UL = simpath+"S12_FORC_WRF_333_STQ_2DURBPARAM_long_corr/T2M_11040.txt"

SURFEXdataS0_IS = loadfile1(SURFEX_S0_IS)
SURFEXdataS12_IS = loadfile1(SURFEX_S12_IS)
#WRFdata_IS = loadfile3(FORCING_IS)
SURFEXdataS0_UL = loadfile1(SURFEX_S0_UL)
SURFEXdataS12_UL = loadfile1(SURFEX_S12_UL)
WRFdata_UL = loadfile3(FORCING_UL)
 # print SURFEXdataS12[0], WRFdata[0]

print len(WRFdata_UL), len(ZAMG_TA_hourly), len(SURFEXdataS0_IS)
print len(IS["INCA"]), len(np.array(SURFEXdataS0_UL))

R2_WRF_IS = (stats.spearmanr(IS["D3"][:-1], IS["INCA"][:-1])[0]**2)
R2_SEC_IS = (stats.spearmanr(SURFEXdataS0_IS[:], IS["INCA"][:-1])[0]**2)
R2_SPM_IS = (stats.spearmanr(SURFEXdataS12_IS[:], IS["INCA"][:-1])[0]**2)
Bias_WRF_IS = np.average(IS["D3"][:]- IS["INCA"][:-1])
Bias_SEC_IS = np.average(SURFEXdataS0_IS[:]- IS["INCA"][:-1])
Bias_SPM_IS = np.average(SURFEXdataS12_IS[:]- IS["INCA"][:-1])

R2_SEC_UL = (stats.spearmanr(WRFdata_UL[:-1],ZAMG_TA_hourly[1:])[0]**2)
R2_SEC_UL = (stats.spearmanr(SURFEXdataS0_UL[:],ZAMG_TA_hourly[1:])[0]**2)
R2_SPM_UL = (stats.spearmanr(SURFEXdataS12_UL[:],ZAMG_TA_hourly[1:])[0]**2)
Bias_WRF_UL = np.average(WRFdata_UL[:-1] - ZAMG_TA_hourly[1:])
Bias_SEC_UL = np.average(SURFEXdataS0_IS[:]- ZAMG_TA_hourly[1:])
Bias_SPM_UL = np.average(SURFEXdataS12_IS[:]- ZAMG_TA_hourly[1:])

#print R2_WRF_GE,R2_WRF_IS

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.plot(IS["INCA"][:], color='black', label="OBS")
ax1.plot(IS["D3"][:],color='blue', label="WRF")
ax1.plot(np.array(SURFEXdataS0_IS[:]), color='red', label="WRF/S(EC)")
ax1.plot(np.array(SURFEXdataS12_IS[:]), color='orange', label="WRF/S(PM)")
#ax1.set_xlabel("hours[UTC]")
ax1.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
ax1.legend(loc='upper right')
#ax1.set_xlim(8, 180)
ax1.set_title(u"Innere Stadt", size="large")

ax2 = fig.add_subplot(222)
ax2.scatter(IS["D3"][:], IS["INCA"][:], color='blue', label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_WRF_IS, Bias_WRF_IS)))  # , s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.scatter(np.array(SURFEXdataS0_IS[:]), IS["INCA"][:-1], color='red', label= (r"$R^2$=%.2f, Bias=%.2f" % (R2_SEC_IS, Bias_SEC_IS)))  # , s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.scatter(np.array(SURFEXdataS12_IS[:]), IS["INCA"][:-1], color='orange', label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_SPM_IS, Bias_SPM_IS)))  # , s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.set_xlabel(r"$T_{air_2m}$"u'[°C]', size="large")
ax2.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
ax2.legend(loc='upper left')

ax3 = fig.add_subplot(223)
ax3.plot(np.array(ZAMG_TA_hourly[8:176]), color='black', label="OBS")
#ax3.plot(np.array(FORCING_UL[8:176]), color='blue', label="WRF(US)")
ax3.plot(np.array(SURFEXdataS0_UL[8:176]), color='red', label="WRF/S(EC)")
ax3.plot(np.array(SURFEXdataS12_UL[8:176]), color='orange', label="WRF/S(PM)")
ax3.set_xlabel("hours[UTC]")
ax3.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
ax3.legend(loc='upper right')
#ax3.set_xlim(0, 255)
ax3.set_title(u"Unterlaa", size="large")  # +"2m air temperature"))

ax4 = fig.add_subplot(224)
#ax4.scatter(np.array(FORCING_UL[8:176]), ZAMG_TA_hourly[8:176], color='blue')#, label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_WRF_GE, Bias_WRF_GE))) # , s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax4.scatter(np.array(SURFEXdataS0_UL[8:176]), ZAMG_TA_hourly[8:176], color='red', label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_SEC_UL, Bias_SEC_UL))) # , s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax4.scatter(np.array(SURFEXdataS12_UL[8:176]), ZAMG_TA_hourly[8:176], color='orange', label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_SPM_UL, Bias_SPM_UL))) # , s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax4.set_xlabel(r"$T_{air_2m}$"u'[°C]', size="large")
ax4.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
ax4.legend(loc='upper left')

#plt.suptitle(u"Groß-Enzersdorf", size="large")  # +"2m air temperature"))
plt.show()

