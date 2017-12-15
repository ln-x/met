# -*- coding: utf-8 -*-
__author__ = 'lnx'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from CONVERTSURFEXNC_TXT import loadfile2
"""
11034 Wien-Innere Stadt (85.5, 54.4, [16.366944444444446, 48.19833333333333])
11035 Wien-Hohe Warte (82.2, 69.7, [16.35638888888889, 48.24861111111111])
11036 Schwechat (147.3, 27.5, [16.56972222222222, 48.11027777777778])
11037 Gross-Enzersdorf (144.1, 54.8, [16.559166666666666, 48.19972222222222])
11040 Wien-Unterlaa (101.5, 32.0, [16.419444444444444, 48.125])
11042 Wien-Stammersdorf (97.2, 87.1, [16.405555555555555, 48.30583333333333])
11077 Brunn am Gebirge (55.9, 26.5, [16.27, 48.106944444444444])
11080 Wien-Mariabrunn (43.5, 57.0, [16.229444444444443, 48.206944444444446])
11090 Wien-Donaufeld (105.1, 72.3, [16.43138888888889, 48.257222222222225])
ZAMGname=[, , Schwechat,Gross-Enzersdorf
"""
#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
ZAMGnames = {'11034': 'Wien-Innere Stadt', '11035':  "Wien-Hohe Warte", '11036': 'Schwechat',
             '11037':'Gross-Enzersdorf', '11040':'Wien-Unterlaa', '11042':'Wien-Stammersdorf',
             '11077':'Brunn am Gebirge', '11080':'Wien-Mariabrunn', '11090':'Wien-Donaufeld'}

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

'''
HERE THE CORRECT DATE AND TIME NEEDS TO BE ADAPTED
'''

for i in ZAMGNo:
  ZAMGstation = "/home/lnx/METDATA/ZAMG/tawes_" + i + "_year_2015.txt"
  ZAMGdata = pd.read_csv(ZAMGstation, delimiter=r"\s+")#, parse_dates=['datum'])
  ZAMGdata_episode = ZAMGdata.loc[ZAMGdata['datum'] == 1150717] #cut episode
  ZAMGdata_episode = ZAMGdata_episode.loc[ZAMGdata['stdmin'] >= 1800] #cut episode
  ZAMGdata_episode2 = ZAMGdata.loc[ZAMGdata['datum'] == 1150718] #cut episode
  ZAMG_episode = pd.concat([ZAMGdata_episode, ZAMGdata_episode2], axis=0)
  #print ZAMG_episode.head(), ZAMG_episode.tail()
  #extract date:
  date = ZAMG_episode['datum'].iloc[0]
  date1 = str(date).split()
  date2 = date1[0][5:7] +"." +date1[0][3:5] +".20"+ date1[0][1:3]
  #print date2
  ZAMG_TA = ZAMG_episode['tl']/10                     #extract 2M air temperature and bring to °C
  ZAMG_TA_hourly = ZAMG_TA[0::6] #s[i:j:k]  slice of s from i to j with step k
  print len(ZAMG_TA_hourly)

  '''
  HERE THE CORRECT FILEPATHS NEED TO BE ADAPTED
  '''
  SURFEXfile1 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/" \
                "S0_FORC_WRF_333_STQ/T2M_" + i +".txt"
  #SURFEXfile1 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/" \
  #           "hapex/S7_FORC_WRFnormal_333_STQ/T2M_" + i +".txt"
  #SURFEXfile2 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/" \
  #           "hapex/S6_FORC_WRFUCM_333_STQ/T2M_" + i +".txt"
  #SURFEXfile = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/output_vienne_wrf_solar1/WIENHW_TA.txt"
  SURFEXdata1 = loadfile2(SURFEXfile1)
  #SURFEXdata2 = loadfile2(SURFEXfile2)
 # print len(SURFEXdata1), len(ZAMG_TA_hourly)

  fig = plt.figure()
  ax = fig.add_subplot(111)
  plt.title(ZAMGnames[i] + ", " + date2)#+"2m air temperature"))
  ax.plot(np.array(ZAMG_TA_hourly), label="ZAMG")
  ax.plot(np.array(SURFEXdata1), label="WRF/TEB")
  #ax.plot(np.array(SURFEXdata2), label=("WRFUCM/TEB"))
  plt.legend(loc='upper left')
  plt.show()
