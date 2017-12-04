# -*- coding: utf-8 -*-
__author__ = 'lnx'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from CONVERTSURFEXNC_TXT import loadfile2

#11034 Wien-Innere Stadt 162201  481154 177
#11035 Wien-Hohe Warte   162123  481455 198
#11036 Schwechat         163411  480637 183
#11037 Gross-Enzersdorf  163333  481159 154
#11040 Wien-Unterlaa     162510  480730 200
#11042 Wien-Stammersdorf 162420  481821 191
#11077 Brunn am Gebirge  161612  480625 291
#11080 Wien-Mariabrunn   161346  481225 225
#11090 Wien-Donaufeld    162553  481526 160

#datum = 1_year_month_day
#stdmin = minutes
#tl = air temperature [1/10 degC]
#k27 = global radiation [Watt/m2]
#rf = rel Feuchte [%]
#rr = Niederschlag 1/10 mm 10-Min-Summe
#p = Luftdruck 1/10 hpascal
#ff = Windstaerke [1/10 m/s] (Vektorielles 10 min Mittel,bezogen auf dd)
#so = Sonnenscheindauer [seconds]
#ts = 5cm air temperature

ZAMGNo = ["11034","11035","11036","11037","11040","11042","11077","11080","11090"]
ZAMGstation = "/home/lnx/METDATA/ZAMG/tawes_" + ZAMGNo[0] + "_year_2015.txt"
ZAMGdata = pd.read_csv(ZAMGstation, delimiter=r"\s+")#, parse_dates=['datum'])
start_datum = (197*144)-2 + 108#"1150717" "1800" -> JD 198
end_datum = (199*144)-2  #"1150719"  -> JD 200
ZAMGdata_episode = ZAMGdata.loc[start_datum:end_datum] #cut episode
print ZAMGdata_episode
ZAMG_TA = ZAMGdata_episode['tl']/10                     #extract 2M air temperature and bring to °C
ZAMG_TA_hourly = ZAMG_TA[0::6] #s[i:j:k]  slice of s from i to j with step k

SURFEXfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/output_vienna_wrf_greenroof_garden1/WIENHW_TA.txt"
#SURFEXfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/output_vienne_wrf/WIENHW_TA.txt"
#SURFEXfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/output_vienne_wrf_solar1/WIENHW_TA.txt"

SURFEXdata = loadfile2(SURFEXfile)
print len(SURFEXdata), len(ZAMG_TA_hourly)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(np.array(ZAMG_TA_hourly), label="WienInnereStadt")
ax.plot(np.array(SURFEXdata), label="WienInnereStadt_Canyon)")
plt.legend()
plt.show()
