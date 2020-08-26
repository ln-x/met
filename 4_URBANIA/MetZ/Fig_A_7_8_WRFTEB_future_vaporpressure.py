# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import sys
from metpy.calc import *
from metpy.units import units
from datetime import datetime, timedelta

outpath ='/home/lnx'
file = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/FINAL/WRF-2019-Runs/REF_Run_2069/wrfout_d03_2069-07-01_18_00_00.nc'

fh = Dataset(file, mode='r')
#fh2 = Dataset(file2, mode='r')

'''time + 2dvariables'''
lons = fh.variables['XLONG'][1]  #lon (147x)135x174
lats = fh.variables['XLAT'][1]  #lat (147x)135x174
MR_WRFTEB = fh.variables['Q2'] #229x135x174 water vapour mixing ratio
P_WRFTEB = fh.variables['PSFC'] #229x135x174 water vapour mixing ratio

MR_WRFTEB_units = fh.variables['Q2'].units
PSFC_WRFTEB_units = fh.variables['PSFC'].units

print MR_WRFTEB_units

#start = datetime(2015,7,18,0)
#x = [start + timedelta(hours=i) for i in range(168)]

ZAMGnames = {'11034': ['Wien-Innere Stadt',85,53], '11035':  ["Wien-Hohe Warte",83,69]}#,
             #'11036': ['Schwechat',129,25], '11037':['Gross-Enzersdorf',127,54],
             #'11040': ['Wien-Unterlaa',97,29], '11042':['Wien-Stammersdorf',94,88],
             #'11077': ['Brunn am Gebirge',65,24], '11080':['Wien-Mariabrunn',56,56]}
for i in ZAMGnames:
  ZAMGstation = "/home/lnx/METDATA/ZAMG_filled/tawes_" + i + "_year_2017.txt"
  ZAMGdata = pd.read_csv(ZAMGstation, delimiter=r"\s+")#, parse_dates=['datum'])
  Day1 = ZAMGdata.loc[ZAMGdata['datum'] > 1170726]
  ZAMG_episode = Day1.loc[Day1['datum'] < 1170805]  # cut episode
  date = ZAMG_episode['datum'].iloc[0]
  date1 = str(date).split()
  date_start = date1[0][5:7] +"." +date1[0][3:5] +".20"+ date1[0][1:3]

  ZAMG_TA = (ZAMG_episode['tl']/10)+273.15 #extract 2M air temperature original 1/10 °C
  ZAMG_RF = ZAMG_episode['rf']/100 #extract relative humidty
  ZAMG_P = ZAMG_episode['p']/10 #pressure original:[1/10 hpasc]
  ZAMG_TA = units.Quantity(np.array(ZAMG_TA),"kelvin")
  ZAMG_RF = np.array(ZAMG_RF)
  ZAMG_P = units.Quantity(np.array(ZAMG_P),'hectopascal')
  ZAMG_MR = mixing_ratio_from_relative_humidity(ZAMG_RF,ZAMG_TA,ZAMG_P)
  ZAMG_VP = vapor_pressure(ZAMG_P, ZAMG_MR)
  #print ZAMG_TA[1], ZAMG_RF[1],ZAMG_P[1], ZAMG_MR[1], ZAMG_VP[1]

  ZAMG_P_hourly = ZAMG_P[0::6]
  ZAMG_MR_hourly = ZAMG_MR[0::6]  #s[i:j:k]  slice of s from i to j with step k
  ZAMG_VP_hourly = ZAMG_VP[0::6]  #s[i:j:k]  slice of s from i to j with step k

  '''convert to numpy array and bring to same filesize'''
  ZAMG_heatdays = np.array(ZAMG_MR_hourly)#[8:176])# np.vstack((np.array(ZAMG_TA_hourly[13:109]),np.array(ZAMG_TA_hourly[133:-98])))  #[13:]
  ZAMG_heatdays_VP = np.array(ZAMG_VP_hourly)
  #print len(ZAMG_heatdays)
  x = ZAMGnames[i][1]
  y = ZAMGnames[i][2]
  print i, x, y
  WRFdata = MR_WRFTEB[:,y,x]
  WRFdata_P = P_WRFTEB[:,y,x]
  WRFdata_heatdays = np.array(WRFdata[6:-7])#[8:176])
  WRFdata_heatdays_P = np.array(WRFdata_P[6:-7])/100
  #WRFdata_heatdays_VP = vapor_pressure(ZAMG_P_hourly, WRFdata_heatdays)
  WRFdata_heatdays_VP = vapor_pressure(WRFdata_heatdays_P, WRFdata_heatdays)
  WRFdata_heatdays_VP = np.array(WRFdata_heatdays_VP)

  print WRFdata_heatdays_VP.mean()

  try:
    '''
    Plotting
    '''
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(WRFdata_heatdays_VP, color='violet', label="WRF_TEB")  # 31
    # ax1.plot(WRFdata2_heatdays, color='blue', label="WRF(C)")  #31
    ax1.set_xlabel("hours [UTC]")
    ax1.set_ylabel(r"Water vapour pressure (2 m) "u'[hPa]', size="medium")
    ax1.legend(loc='upper left')
    # ax1.set_xlim(0, 125)
    # ax1.set_ylim(15, 40)
    # myFmt = DateFormatter("%d")
    # ax1.xaxis.set_major_formatter(myFmt)
    # fig.autofmt_xdate()

    plt.show()

  except:
    print("Oops!", sys.exc_info()[0], "occured.")
    pass

fh.close()



