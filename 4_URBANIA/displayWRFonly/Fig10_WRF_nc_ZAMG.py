# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from CONVERTSURFEXNC_TXT import *
from scipy import stats
import sys
from datetime import datetime, timedelta

outpath ='/home/lnx'
file = '/media/lnx/98C4EEA4C4EE83BA/WRF-TEB-NC_Files/wrfout_d03_2015-07-13_12_00_00_nest_teb.nc'
file2 = '/media/lnx/98C4EEA4C4EE83BA/WRF-TEB-NC_Files/wrfout_d03_2015-07-13_12_00_00_no_teb_nested.nc'
file2 = '/media/lnx/98C4EEA4C4EE83BA/WRF-TEB-NC_Files/wrfout_d03_2015-07-13_12_00_00_no_teb_nested.nc'

fh = Dataset(file, mode='r')
fh2 = Dataset(file2, mode='r')

'''time + 2dvariables'''
lons = fh.variables['XLONG'][1]  #lon (147x)135x174
lats = fh.variables['XLAT'][1]  #lat (147x)135x174
tair = fh.variables['T2'] #147x135x174
tair_units = fh.variables['T2'].units

lons2 = fh2.variables['XLONG'][1]  #lon (147x)135x174
lats2 = fh2.variables['XLAT'][1]  #lat (147x)135x174
tair2 = fh2.variables['T2'] #147x135x174

#start = datetime(2015,7,18,0)
#x = [start + timedelta(hours=i) for i in range(168)]

ZAMGnames = {'11034': ['Wien-Innere Stadt',85,53], '11035':  ["Wien-Hohe Warte",83,69],
             '11036': ['Schwechat',129,25], '11037':['Gross-Enzersdorf',127,54],
             '11040': ['Wien-Unterlaa',97,29], '11042':['Wien-Stammersdorf',94,88],
             '11077': ['Brunn am Gebirge',65,24], '11080':['Wien-Mariabrunn',56,56]}
for i in ZAMGnames:
  ZAMGstation = "/home/lnx/METDATA/ZAMG_filled/tawes_" + i + "_year_2015.txt"
  ZAMGdata = pd.read_csv(ZAMGstation, delimiter=r"\s+")#, parse_dates=['datum'])
  Day1 = ZAMGdata.loc[ZAMGdata['datum'] > 1150713]
  ZAMG_episode = Day1.loc[Day1['datum'] < 1150719]  # cut episode
  date = ZAMG_episode['datum'].iloc[0]
  date1 = str(date).split()
  date_start = date1[0][5:7] +"." +date1[0][3:5] +".20"+ date1[0][1:3]
  ZAMG_TA = ZAMG_episode['tl']/10 #extract 2M air temperature and bring to °C
  ZAMG_TA_hourly = ZAMG_TA[0::6]  #s[i:j:k]  slice of s from i to j with step k

  '''convert to numpy array and bring to same filesize'''
  ZAMG_heatdays = np.array(ZAMG_TA_hourly)#[8:176])# np.vstack((np.array(ZAMG_TA_hourly[13:109]),np.array(ZAMG_TA_hourly[133:-98])))  #[13:]
  #print len(ZAMG_heatdays)
  x = ZAMGnames[i][1]
  y = ZAMGnames[i][2]
  print i, x, y
  WRFdata = tair[:,y,x]
  WRFdata_heatdays = np.array(WRFdata[12:-15])#[8:176])
  WRFdata_heatdays = WRFdata_heatdays - 273.15
  print len(WRFdata_heatdays), len(ZAMG_heatdays)

  WRFdata2 = tair2[:, y, x]
  WRFdata2_heatdays = np.array(WRFdata2[12:-24])  # [8:176])
  WRFdata2_heatdays = WRFdata2_heatdays - 273.15
  print len(WRFdata2_heatdays), len(ZAMG_heatdays)

  '''calculation of bias'''
  Bias_Forc_i = np.average(WRFdata_heatdays-ZAMG_heatdays)
  Bias_Forc_i2 = np.average(WRFdata2_heatdays-ZAMG_heatdays)
  #print i, Bias_Forc_i

  '''calculation of Regression coefficients'''
  #print stats.spearmanr(ZAMG_heatdays, WRFdata_heatdays, axis=0)
  R2_Forc_i = (stats.spearmanr(ZAMG_heatdays, WRFdata_heatdays))[0] ** 2
  R2_Forc_i2 = (stats.spearmanr(ZAMG_heatdays, WRFdata2_heatdays))[0] ** 2
  #print i, R2_Forc_i

  try:
    '''
    Plotting
    '''
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.plot(ZAMG_heatdays, color='black', label=u"Ground station")
    ax1.plot(WRFdata_heatdays, color='violet', label="WRF_TEB(C)")  #31
    ax1.plot(WRFdata2_heatdays, color='blue', label="WRF(C)")  #31
    ax1.set_xlabel("hours[UTC]")
    ax1.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
    ax1.legend(loc='upper right')
    ax1.set_xlim(0, 125)
    ax1.set_ylim(15, 40)
    #myFmt = DateFormatter("%d")
    #ax1.xaxis.set_major_formatter(myFmt)
    #fig.autofmt_xdate()

    ax2 = fig.add_subplot(122)
    plt.scatter(ZAMG_heatdays, WRFdata_heatdays, color='blue', label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
    plt.scatter(ZAMG_heatdays, WRFdata2_heatdays, color='violet', label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i2, Bias_Forc_i2)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
    ax2.set_xlabel(r"$T_{air_2m}$"u'[°C]', size="large")
    ax2.set_ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
    ax2.legend(loc='upper left')
    #plt.suptitle(ZAMGnames[i] + ", 14 - 21 July 2015", size="large")#+"2m air temperature"))
    plt.suptitle(ZAMGnames[i][0] + ", 14 - 18 July 2015", size="large")#+"2m air temperature"))
    figname = outpath + i + "WRFTEBZAMG.png"
    #plt.savefig(figname)
    plt.show()
  except:
    print("Oops!", sys.exc_info()[0], "occured.")
    pass


fh.close()



