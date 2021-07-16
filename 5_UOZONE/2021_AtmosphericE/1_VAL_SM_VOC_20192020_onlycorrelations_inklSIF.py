# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import netCDF4
import numpy as np
import csv
import pandas as pd
from datetime import datetime, timedelta
import monthdelta
import matplotlib.dates
import matplotlib.pyplot as plt
from scipy import stats
import sys
import os
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVINDOBONA
from met.library import ReadinVindobona_DA
from met.library import ReadinVindobona_Filter
from met.library import ReadinVindobona_Filter2019

from functools import reduce

"read in VINDOBONA"

foldername = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2020/DQ/"
foldername2019 = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2019/"
foldername_A = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2020/AQ/"
foldername_K = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2020/KQ/"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter.loadfileALL(foldername)
hcho19_d, hcho19_dmax, hcho19_m = ReadinVindobona_Filter2019.loadfileALL(foldername2019)
hcho_d_A, hcho_dmax_A, hcho_m_A = ReadinVindobona_Filter.loadfileALL(foldername_A)
hcho_d_K, hcho_dmax_K, hcho_m_K = ReadinVindobona_Filter.loadfileALL(foldername_K)
hcho_dmax = hcho19_dmax.append(hcho_dmax)

'''READ IN BOKU Metdata'''
BOKUMetData = met.library.BOKUMet_Data.BOKUMet()
#print(BOKUMetData) #10min values
#DAILY MEANS
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
#DAILY MAX
BOKUMetData_dailymax = BOKUMetData_hourlymean.resample('D').agg({'DT': np.max, 'AT': np.max, 'RH': np.max, 'GR': np.max, 'WS': np.max,
                                                      'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})
#JULIAN DAY
BOKUMetData_dailysum['JD'] = (BOKUMetData_dailysum.index)
f = lambda x: datestdtojd(str(x)[:-9])
BOKUMetData_dailysum['JD'] = BOKUMetData_dailysum['JD'].apply(f)

#MONTHLY MEANS
BOKUMetData_monthly = BOKUMetData.resample('M').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                      'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

'''READ in SOIL MOISTURE DATA'''
#file_sm_2019_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/2019_Parrots_Rutzendorf_4_Heidi.xls"
#sm = pd.read_excel(file_sm_2019_rutz, sheet_name="Data", usecols="A,B", skiprows=11)#, converters={'A': pd.to_datetime})
#sm.columns = ['datetime', 'Parrot mean [VWC%]']  #TODO: local time!
#sm = sm.set_index(pd.to_datetime(sm['datetime']))
#sm = sm.drop(columns=['datetime'])

file_sm_2019_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/RUT_10_min.xls"
sm = pd.read_excel(file_sm_2019_rutz, sheet_name="RUT_d", usecols="D,K,L,M,N,O,P", skiprows=11)#, converters={'A': pd.to_datetime})
sm.columns = ['datetime', 'VWC1 min[%]', 'VWC2 min[%]','VWC3 min[%]','VWC1 max[%]', 'VWC2 max[%]','VWC3 max[%]']  #TODO: local time!
sm = sm.set_index(pd.to_datetime(sm['datetime']))
sm = sm.drop(columns=['datetime'])
#print(sm)
#exit()

file_rss_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/2008_2020_Rutzendorf_ARIS_results_sepp.xlsx"
rss = pd.read_excel(file_rss_rutz, sheet_name="RSS_top", usecols="A,B,C,D,E,F", skiprows=11)#, converters={'A': pd.to_datetime})
rss.columns = ['datetime', 'RSS_top_maize', 'RSS_top_sBarley','RSS_top_sugBeet','RSS_top_wWheat', 'RSS_top_grass']  #TODO: local time!
rss = rss.set_index(pd.to_datetime(rss['datetime']))
rss = rss.drop(columns=['datetime'])
#vwc = rss['RSS_top_maize', 'RSS_top_sBarley','RSS_top_sugBeet','RSS_top_wWheat', 'RSS_top_grass']

#Grünland bei Gänserndorf (war das nächstliegende Grünland Pixel zu Rutzendorf)
#LON 652.750 LAT 494.250
grass_fc_top_Layer= 0.402768
grass_fc_sub_Layer= 0.287642
grass_afc_top_Layer= 0.218952
grass_afc_sub_Layer= 0.162540

#Acker bei Rutzendorf
#LON 644.250 LAT 484.250
rutz_fc_top_Layer= 0.380875
rutz_fc_sub_Layer= 0.268583
rutz_afc_top_Layer= 0.222250
rutz_afc_sub_Layer= 0.154833

#test1 = rutz_fc_top_Layer - (1-1)*rutz_afc_top_Layer
#test2 = rutz_fc_top_Layer - (1-0.5)*rutz_afc_top_Layer
#test3 = rutz_fc_top_Layer - (1-0)*rutz_afc_top_Layer
#print(test1,test2,test3)
vwc = rutz_fc_top_Layer - (1-rss)*rutz_afc_top_Layer
vwc_grass = grass_fc_top_Layer - (1-rss)*grass_afc_top_Layer

#TSIF_743
tsif_r = pd.read_csv("/windata/DATA/remote/satellite/TROPOMI/TSIF_743.csv", sep=",")
tsif = tsif_r.set_index(pd.to_datetime(tsif_r['time']))
tsif = tsif.drop(columns=['time'])
#print(tsif)

#osif_771_r = pd.read_csv("/windata/DATA/remote/satellite/OCO/OSIF_8100_771nm.csv", sep=",")
#osif_771 = osif_771_r.set_index(pd.to_datetime(osif_771_r['time']))
#osif_771 = osif_771.drop(columns=['time'])

osif_757_r = pd.read_csv("/windata/DATA/remote/satellite/OCO2/OSIF_8100_757nm.csv", sep=",")
osif_757 = osif_757_r.set_index(pd.to_datetime(osif_757_r['time']))
osif_757 = osif_757.drop(columns=['time'])

'''TIMESLICES'''
March19 = datetime(2019, 3, 1, 00, 00) #JD 2020=92
June19 = datetime(2019, 6, 1, 00, 00)  #JD 2020=183
Sept19 = datetime(2019, 9, 1, 00, 00)  #JD 2020=183
March = datetime(2020, 3, 1, 00, 00) #JD 2020=92
April = datetime(2020, 4, 1, 00, 00) #JD 2020=92
June = datetime(2020, 6, 1, 00, 00)  #JD 2020=183
July = datetime(2020, 7, 1, 00, 00)  #JD 2020=183
Sept = datetime(2020, 9, 1, 00, 00)  #JD 2020=183
DP1_s = datetime(2019, 3, 17, 00, 00) #drought period1 start
DP1_e = datetime(2019, 4, 29, 00, 00) #drought period1 end
DP2_s = datetime(2019, 6, 8, 00, 00) #drought period2 start
DP2_e = datetime(2019, 6, 30, 00, 00) #drought period2 end
DP3_s = datetime(2019, 8, 13, 00, 00) #drought period3 start
DP3_e = datetime(2019, 8, 31, 00, 00) #drought period3 end
DP4_s = datetime(2020, 3, 22, 00, 00) #drought period4 start
DP4_e = datetime(2020, 4, 11, 00, 00) #drought period4 end

SE1_s = datetime(2019, 4, 2, 00, 00) #drought south east period1 start
SE1_e = datetime(2019, 4, 8, 00, 00)
SE2_s = datetime(2019, 6, 9, 00, 00)
SE2_e = datetime(2019, 6, 16, 00, 00)
SE3_s = datetime(2019, 8, 25, 00, 00)
SE3_e = datetime(2019, 8, 30, 00, 00)
#SE4_s = datetime(2019, 8, 24, 00, 00)
#SE4_e = datetime(2019, 8, 30, 00, 00)

NW1_s = datetime(2019, 3, 24, 00, 00) #drought south east period1 start
NW1_e = datetime(2019, 3, 29, 00, 00) #TODO add one northwesterly day from before
NW2_s = datetime(2019, 4, 9, 00, 00)
NW2_e = datetime(2019, 4, 16, 00, 00)
NW3_s = datetime(2019, 8, 19, 00, 00)
NW3_e = datetime(2019, 8, 24, 00, 00) #TODO add one northwesterly day from before

'''
Plotting
'''

##NW DP
pff = pd.concat([hcho_dmax,vwc["RSS_top_wWheat"],BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"],tsif],axis=1, keys=['hcho','SM','AT','GR','SIF'])
pff5 = pff[NW2_s:NW2_e].dropna()
pff5_1 = pff[NW2_s:NW2_e].dropna()
pff5_2 = pff[NW3_s:NW3_e].dropna()
pff5 = pff5.append(pff5_1)
pff5 = pff5.append(pff5_2)
x5 = pff5['AT'].values.flatten() #AT!
x5_GR = pff5['GR'].values.flatten()
x5_SM = pff5['SM'].values.flatten()
x5_SIF = pff5['SIF'].values.flatten()
y5 = pff5['hcho'].values.flatten()
a=0#92*24
m5, b5 = np.polyfit(x5[a:], y5[a:], 1)
m5GR, b5GR = np.polyfit(x5_GR[a:], y5[a:], 1)
m5SM, b5SM = np.polyfit(x5_SM[a:], y5[a:], 1)
m5SIF, b5SIF = np.polyfit(x5_SIF[a:], y5[a:], 1)
fig, axes = plt.subplots(nrows=1, ncols=4)
plt.title(f"NW DPs")
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.scatter(x5[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x5, m5*x5+b5, color='red')
ax0.set_ylabel("HCHO [ppb]", size="medium")
ax0.set_xlabel("air temp [degC]", size="medium")
ax1.scatter(x5_GR[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x5_GR, m5GR*x5_GR + b5GR, color='red')
ax1.set_xlabel("GR [degC]", size="medium")
ax2.scatter(x5_SM[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.plot(x5_SM, m5SM*x5_SM + b5SM, color='red')
ax2.set_xlabel("SM [m3 m-3]", size="medium")
ax3.scatter(x5_SIF[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.plot(x5_SIF, m5SIF*x5_SIF + b5SIF, color='red')
ax3.set_xlabel("SIF [mW m-2 sr-1 nm-1]", size="medium")
#ax2.set_ylabel("HCHO [ppb]", size="medium")
fig.tight_layout()
plt.savefig("/home/heidit/Downloads/DP_NW.jpg")
plt.show()

#SW DP
pff5 = pff[SE2_s:SE2_e].dropna()
pff5_1 = pff[SE2_s:SE2_e].dropna()
pff5_2 = pff[SE3_s:SE3_e].dropna()
pff5 = pff5.append(pff5_1)
pff5 = pff5.append(pff5_2)
x5 = pff5['AT'].values.flatten() #AT!
x5_GR = pff5['GR'].values.flatten()
x5_SM = pff5['SM'].values.flatten()
x5_SIF = pff5['SIF'].values.flatten()
y5 = pff5['hcho'].values.flatten()
a=0
m5, b5 = np.polyfit(x5[a:], y5[a:], 1)
m5GR, b5GR = np.polyfit(x5_GR[a:], y5[a:], 1)
m5SM, b5SM = np.polyfit(x5_SM[a:], y5[a:], 1)
m5SIF, b5SIF = np.polyfit(x5_SIF[a:], y5[a:], 1)
fig, axes = plt.subplots(nrows=1, ncols=4)
plt.title(f"SE DPs")
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.scatter(x5[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x5, m5*x5+b5, color='red')
ax0.set_ylabel("HCHO [ppb]", size="medium")
ax0.set_xlabel("air temp [degC]", size="medium")
ax1.scatter(x5_GR[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x5_GR, m5GR*x5_GR + b5GR, color='red')
ax1.set_xlabel("GR [degC]", size="medium")
ax2.scatter(x5_SM[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.plot(x5_SM, m5SM*x5_SM + b5SM, color='red')
ax2.set_xlabel("SM [m3 m-3]", size="medium")
ax3.scatter(x5_SIF[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.plot(x5_SIF, m5SIF*x5_SIF + b5SIF, color='red')
ax3.set_xlabel("SIF [mW m-2 sr-1 nm-1]", size="medium")
fig.tight_layout()
plt.savefig("/home/heidit/Downloads/DP_SE.jpg")
plt.show()

#SPRING: MAM
pff5 = pff[March19:June19].dropna()
pff5_1 = pff[March:June].dropna()
pff5 = pff5.append(pff5_1)
x5 = pff5['AT'].values.flatten() #AT!
x5_GR = pff5['GR'].values.flatten()
x5_SM = pff5['SM'].values.flatten()
x5_SIF = pff5['SIF'].values.flatten()
y5 = pff5['hcho'].values.flatten()
a=0
m5, b5 = np.polyfit(x5[a:], y5[a:], 1)
m5GR, b5GR = np.polyfit(x5_GR[a:], y5[a:], 1)
m5SM, b5SM = np.polyfit(x5_SM[a:], y5[a:], 1)
m5SIF, b5SIF = np.polyfit(x5_SIF[a:], y5[a:], 1)
fig, axes = plt.subplots(nrows=1, ncols=4)
plt.title(f"MAM")
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.scatter(x5[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x5, m5*x5+b5, color='red')
ax0.set_ylabel("HCHO [ppb]", size="medium")
ax0.set_xlabel("air temp [degC]", size="medium")
ax1.scatter(x5_GR[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x5_GR, m5GR*x5_GR + b5GR, color='red')
ax1.set_xlabel("GR [degC]", size="medium")
ax2.scatter(x5_SM[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.plot(x5_SM, m5SM*x5_SM + b5SM, color='red')
ax2.set_xlabel("SM [m3 m-3]", size="medium")
ax3.scatter(x5_SIF[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.plot(x5_SIF, m5SIF*x5_SIF + b5SIF, color='red')
ax3.set_xlabel("SIF [mW m-2 sr-1 nm-1]", size="medium")
fig.tight_layout()
plt.savefig("/home/heidit/Downloads/MAM.jpg")
plt.show()

#SUMMER: JJA
pff5 = pff[June19:Sept19].dropna()
pff5_1 = pff[June:Sept].dropna()
pff5 = pff5.append(pff5_1)
x5 = pff5['AT'].values.flatten() #AT!
x5_GR = pff5['GR'].values.flatten()
x5_SM = pff5['SM'].values.flatten()
x5_SIF = pff5['SIF'].values.flatten()
y5 = pff5['hcho'].values.flatten()
a=0
m5, b5 = np.polyfit(x5[a:], y5[a:], 1)
m5GR, b5GR = np.polyfit(x5_GR[a:], y5[a:], 1)
m5SM, b5SM = np.polyfit(x5_SM[a:], y5[a:], 1)
m5SIF, b5SIF = np.polyfit(x5_SIF[a:], y5[a:], 1)
fig, axes = plt.subplots(nrows=1, ncols=4)
plt.title(f"JJA")
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.scatter(x5[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x5, m5*x5+b5, color='red')
ax0.set_ylabel("HCHO [ppb]", size="medium")
ax0.set_xlabel("air temp [degC]", size="medium")
ax1.scatter(x5_GR[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x5_GR, m5GR*x5_GR + b5GR, color='red')
ax1.set_xlabel("GR [degC]", size="medium")
ax2.scatter(x5_SM[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.plot(x5_SM, m5SM*x5_SM + b5SM, color='red')
ax2.set_xlabel("SM [m3 m-3]", size="medium")
ax3.scatter(x5_SIF[a:], y5[a:], color='red') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.plot(x5_SIF, m5SIF*x5_SIF + b5SIF, color='red')
ax3.set_xlabel("SIF [mW m-2 sr-1 nm-1]", size="medium")
fig.tight_layout()
plt.savefig("/home/heidit/Downloads/JJA.jpg")
plt.show()

#Total
pff5 = pff.dropna()
x5 = pff5['AT'].values.flatten() #AT!
x5_GR = pff5['GR'].values.flatten()
x5_SM = pff5['SM'].values.flatten()
x5_SIF = pff5['SIF'].values.flatten()
y5 = pff5['hcho'].values.flatten()
a=0
m5, b5 = np.polyfit(x5[a:], y5[a:], 1)
m5GR, b5GR = np.polyfit(x5_GR[a:], y5[a:], 1)
m5SM, b5SM = np.polyfit(x5_SM[a:], y5[a:], 1)
m5SIF, b5SIF = np.polyfit(x5_SIF[a:], y5[a:], 1)
fig, axes = plt.subplots(nrows=1, ncols=4)
plt.title(f"full period")
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.scatter(x5[a:], y5[a:], color='violet') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x5, m5*x5+b5, color='red')
ax0.set_ylabel("HCHO [ppb]", size="medium")
ax0.set_xlabel("air temp [degC]", size="medium")
ax1.scatter(x5_GR[a:], y5[a:], color='violet') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x5_GR, m5GR*x5_GR + b5GR, color='red')
ax1.set_xlabel("GR [degC]", size="medium")
ax2.scatter(x5_SM[a:], y5[a:], color='violet') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.plot(x5_SM, m5SM*x5_SM + b5SM, color='red')
ax2.set_xlabel("SM [m3 m-3]", size="medium")
ax3.scatter(x5_SIF[a:], y5[a:], color='violet') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.plot(x5_SIF, m5SIF*x5_SIF + b5SIF, color='red')
ax3.set_xlabel("SIF [mW m-2 sr-1 nm-1]", size="medium")
fig.tight_layout()
plt.savefig("/home/heidit/Downloads/fullperiod.jpg")
plt.show()

exit()

#fig = plt.figure()
#start = datetime(2020, 1, 1, 00, 00)
start = datetime(2019, 1, 1, 00, 00)
#start = datetime(2017, 1, 1, 00, 00)
#end = datetime(2020, 1, 1, 00, 00)
end = datetime(2020, 9, 27, 00, 00)
end2 = datetime(2020, 10, 30, 00, 00)

#pff = pd.concat([hcho19_dmax,sm['VWC1 max[%]'],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
#pff = pd.concat([hcho19_dmax,vwc["RSS_top_grass"],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
pff = pd.concat([hcho19_dmax,vwc["RSS_top_wWheat"],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
pff1 = pff[NW1_s:NW1_e].dropna()
pff1_1 = pff[NW2_s:NW2_e].dropna()
pff1_2 = pff[NW3_s:NW3_e].dropna()
pff1 = pff1.append(pff1_1)
pff1 = pff1.append(pff1_2)

x_i = pff1['4'].values.flatten()
x1= x_i       #FOR SIF
y1 = pff1['1'].values.flatten()
a=0#92*24
m1, b1 = np.polyfit(x1[a:], y1[a:], 1)

pff3 = pff[SE1_s:SE1_e].dropna()
pff4 = pff[SE2_s:SE2_e].dropna()
pff5 = pff[SE2_s:SE2_e].dropna()
pff3 = pff3.append(pff4)
pff3 = pff3.append(pff5)

x_i = pff3['4'].values.flatten()
x3= x_i       #FOR SIF
y3 = pff3['1'].values.flatten()
a=0#92*24
m3, b3 = np.polyfit(x3[a:], y3[a:], 1)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.set_title(f"NW")
ax0.scatter(x1[a:], y1[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x1, m1*x1+b1, color='red')
#ax0.legend(loc='upper right')
ax0.set_ylabel("HCHO [ppb]", size="medium")

#ax1.set_title(f"NW 2: {NW2_s.date()} - {NW2_e.date()}")
#ax1.scatter(x2[a:], y2[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
#ax1.plot(x2, m2*x2+b2, color='red')

ax2.set_title(f"SW")
ax2.scatter(x3[a:], y3[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.set_ylabel("HCHO [ppb]", size="medium")
ax2.set_xlabel("VWC [%]", size="medium")
ax2.plot(x3, m3*x3+b3, color='red')

#ax3.set_title(f"SW 2: {SE2_s.date()} - {SE2_e.date()}")
#ax3.scatter(x3[a:], y3[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
#ax3.set_xlabel("VWC [%]", size="medium")
#ax3.plot(x3, m3*x3+b3, color='red')

fig.tight_layout()
plt.show()

"""
#HCHO - RSS
"""
pff = pd.concat([hcho19_dmax,rss['RSS_top_wWheat'],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
pff1 = pff[DP1_s:DP1_e].dropna()
#pff1.columns = pff1.columns.droplevel(-1)
#isHighGRall = pff1["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff1[isHighGRall]
x_i = pff1['4'].values.flatten()
x1= x_i       #FOR SIF
y1 = pff1['1'].values.flatten()
a=0#92*24
m1, b1 = np.polyfit(x1[a:], y1[a:], 1)

pff2 = pff[DP2_s:DP2_e].dropna()
#pff2.columns = pff2.columns.droplevel(-1)
#isHighGRall = pff2["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff2[isHighGRall]
x_i = pff2['4'].values.flatten()
x2= x_i       #FOR SIF
y2 = pff2['1'].values.flatten()
a=0#92*24
m2, b2 = np.polyfit(x2[a:], y2[a:], 1)

pff3 = pff[DP3_s:DP3_e].dropna()
#pff3.columns = pff3.columns.droplevel(-1)
#isHighGRall = pff3["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff3[isHighGRall]
x_i = pff3['4'].values.flatten()
x3= x_i       #FOR SIF
y3 = pff3['1'].values.flatten()
a=0#92*24
m3, b3 = np.polyfit(x3[a:], y3[a:], 1)

pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,tsif,BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff4 = pff[DP4_s:DP4_e].dropna()
#pff4.columns = pff4.columns.droplevel(-1)
#isHighGRall = pff4["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff4[isHighGRall]
x_i = pff4['4'].values.flatten()
x4= x_i       #FOR SIF
y4 = pff4['1'].values.flatten()
yA4 = pff4['2'].values.flatten()
yK4 = pff4['3'].values.flatten()
a=0#92*24
m4, b4 = np.polyfit(x4[a:], y4[a:], 1)
#mA4, bA4 = np.polyfit(x4[a:], yA4[a:], 1)
#mK4, bK4 = np.polyfit(x4[a:], yK4[a:], 1)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.set_title(f"SPRING 1: {DP1_s.date()} - {DP1_e.date()}")
ax0.scatter(x1[a:], y1[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x1, m1*x1+b1, color='red')
#ax0.legend(loc='upper right')
ax0.set_ylabel("HCHO [ppb]", size="medium")

ax1.set_title(f"SUMMER 1: {DP2_s.date()} - {DP2_e.date()}")
ax1.scatter(x2[a:], y2[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x2, m2*x2+b2, color='red')

ax2.set_title(f"SPRING 2: {DP4_s.date()} - {DP4_e.date()}")
ax2.scatter(x4[a:], y4[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.set_ylabel("HCHO [ppb]", size="medium")
ax2.set_xlabel("RSS [%]", size="medium")
ax2.plot(x4, m4*x4+b4, color='red')

ax3.set_title(f"SUMMER 2: {DP3_s.date()} - {DP3_e.date()}")
ax3.scatter(x3[a:], y3[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.set_xlabel("RSS [%]", size="medium")
ax3.plot(x3, m3*x3+b3, color='red')

fig.tight_layout()
plt.show()

exit()
#HCHO - VWC/SM
pff = pd.concat([hcho19_dmax,sm['VWC1 max[%]'],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
pff1 = pff[DP1_s:DP1_e].dropna()
#pff1.columns = pff1.columns.droplevel(-1)
#isHighGRall = pff1["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff1[isHighGRall]
x_i = pff1['4'].values.flatten()
x1= x_i       #FOR SIF
y1 = pff1['1'].values.flatten()
a=0#92*24
m1, b1 = np.polyfit(x1[a:], y1[a:], 1)

pff2 = pff[DP2_s:DP2_e].dropna()
#pff2.columns = pff2.columns.droplevel(-1)
#isHighGRall = pff2["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff2[isHighGRall]
x_i = pff2['4'].values.flatten()
x2= x_i       #FOR SIF
y2 = pff2['1'].values.flatten()
a=0#92*24
m2, b2 = np.polyfit(x2[a:], y2[a:], 1)

pff3 = pff[DP3_s:DP3_e].dropna()
#pff3.columns = pff3.columns.droplevel(-1)
#isHighGRall = pff3["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff3[isHighGRall]
x_i = pff3['4'].values.flatten()
x3= x_i       #FOR SIF
y3 = pff3['1'].values.flatten()
a=0#92*24
m3, b3 = np.polyfit(x3[a:], y3[a:], 1)

pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,tsif,BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff4 = pff[DP4_s:DP4_e].dropna()
#pff4.columns = pff4.columns.droplevel(-1)
#isHighGRall = pff4["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff4[isHighGRall]
x_i = pff4['4'].values.flatten()
x4= x_i       #FOR SIF
y4 = pff4['1'].values.flatten()
yA4 = pff4['2'].values.flatten()
yK4 = pff4['3'].values.flatten()
a=0#92*24
m4, b4 = np.polyfit(x4[a:], y4[a:], 1)
#mA4, bA4 = np.polyfit(x4[a:], yA4[a:], 1)
#mK4, bK4 = np.polyfit(x4[a:], yK4[a:], 1)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.set_title(f"SPRING 1: {DP1_s.date()} - {DP1_e.date()}")
ax0.scatter(x1[a:], y1[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x1, m1*x1+b1, color='red')
#ax0.legend(loc='upper right')
ax0.set_ylabel("HCHO [ppb]", size="medium")

ax1.set_title(f"SUMMER 1: {DP2_s.date()} - {DP2_e.date()}")
ax1.scatter(x2[a:], y2[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x2, m2*x2+b2, color='red')

ax2.set_title(f"SPRING 2: {DP4_s.date()} - {DP4_e.date()}")
ax2.scatter(x4[a:], y4[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.set_ylabel("HCHO [ppb]", size="medium")
ax2.set_xlabel("VWC [%]", size="medium")
ax2.plot(x4, m4*x4+b4, color='red')

ax3.set_title(f"SUMMER 2: {DP3_s.date()} - {DP3_e.date()}")
ax3.scatter(x3[a:], y3[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.set_xlabel("VWC [%]", size="medium")
ax3.plot(x3, m3*x3+b3, color='red')

fig.tight_layout()
plt.show()



"""
#HCHO - RSS
"""
pff = pd.concat([hcho19_dmax,rss['RSS_top_wWheat'],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
pff1 = pff[DP1_s:DP1_e].dropna()
#pff1.columns = pff1.columns.droplevel(-1)
#isHighGRall = pff1["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff1[isHighGRall]
x_i = pff1['4'].values.flatten()
x1= x_i       #FOR SIF
y1 = pff1['1'].values.flatten()
a=0#92*24
m1, b1 = np.polyfit(x1[a:], y1[a:], 1)

pff2 = pff[DP2_s:DP2_e].dropna()
#pff2.columns = pff2.columns.droplevel(-1)
#isHighGRall = pff2["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff2[isHighGRall]
x_i = pff2['4'].values.flatten()
x2= x_i       #FOR SIF
y2 = pff2['1'].values.flatten()
a=0#92*24
m2, b2 = np.polyfit(x2[a:], y2[a:], 1)

pff3 = pff[DP3_s:DP3_e].dropna()
#pff3.columns = pff3.columns.droplevel(-1)
#isHighGRall = pff3["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff3[isHighGRall]
x_i = pff3['4'].values.flatten()
x3= x_i       #FOR SIF
y3 = pff3['1'].values.flatten()
a=0#92*24
m3, b3 = np.polyfit(x3[a:], y3[a:], 1)

pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,tsif,BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff4 = pff[DP4_s:DP4_e].dropna()
#pff4.columns = pff4.columns.droplevel(-1)
#isHighGRall = pff4["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff4[isHighGRall]
x_i = pff4['4'].values.flatten()
x4= x_i       #FOR SIF
y4 = pff4['1'].values.flatten()
yA4 = pff4['2'].values.flatten()
yK4 = pff4['3'].values.flatten()
a=0#92*24
m4, b4 = np.polyfit(x4[a:], y4[a:], 1)
#mA4, bA4 = np.polyfit(x4[a:], yA4[a:], 1)
#mK4, bK4 = np.polyfit(x4[a:], yK4[a:], 1)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.set_title(f"SPRING 1: {DP1_s.date()} - {DP1_e.date()}")
ax0.scatter(x1[a:], y1[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x1, m1*x1+b1, color='red')
#ax0.legend(loc='upper right')
ax0.set_ylabel("HCHO [ppb]", size="medium")

ax1.set_title(f"SUMMER 1: {DP2_s.date()} - {DP2_e.date()}")
ax1.scatter(x2[a:], y2[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x2, m2*x2+b2, color='red')

ax2.set_title(f"SPRING 2: {DP4_s.date()} - {DP4_e.date()}")
ax2.scatter(x4[a:], y4[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.set_ylabel("HCHO [ppb]", size="medium")
ax2.set_xlabel("RSS [%]", size="medium")
ax2.plot(x4, m4*x4+b4, color='red')

ax3.set_title(f"SUMMER 2: {DP3_s.date()} - {DP3_e.date()}")
ax3.scatter(x3[a:], y3[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.set_xlabel("RSS [%]", size="medium")
ax3.plot(x3, m3*x3+b3, color='red')

fig.tight_layout()
plt.show()
#"""
"""HCHO - TMAX"""
"""
pff = pd.concat([hcho19_dmax,BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
pff1 = pff[DP1_s:DP1_e].dropna()
#pff1.columns = pff1.columns.droplevel(-1)
#isHighGRall = pff1["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff1[isHighGRall]
x_i = pff1['4'].values.flatten()
x1= x_i       #FOR SIF
y1 = pff1['1'].values.flatten()
a=0#92*24
m1, b1 = np.polyfit(x1[a:], y1[a:], 1)

pff2 = pff[DP2_s:DP2_e].dropna()
#pff2.columns = pff2.columns.droplevel(-1)
#isHighGRall = pff2["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff2[isHighGRall]
x_i = pff2['4'].values.flatten()
x2= x_i       #FOR SIF
y2 = pff2['1'].values.flatten()
a=0#92*24
m2, b2 = np.polyfit(x2[a:], y2[a:], 1)

pff3 = pff[DP3_s:DP3_e].dropna()
#pff3.columns = pff3.columns.droplevel(-1)
#isHighGRall = pff3["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff3[isHighGRall]
x_i = pff3['4'].values.flatten()
x3= x_i       #FOR SIF
y3 = pff3['1'].values.flatten()
a=0#92*24
m3, b3 = np.polyfit(x3[a:], y3[a:], 1)

pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff4 = pff[DP4_s:DP4_e].dropna()
#pff4.columns = pff4.columns.droplevel(-1)
#isHighGRall = pff4["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff4[isHighGRall]
x_i = pff4['4'].values.flatten()
x4= x_i       #FOR SIF
y4 = pff4['1'].values.flatten()
yA4 = pff4['2'].values.flatten()
yK4 = pff4['3'].values.flatten()
a=0#92*24
m4, b4 = np.polyfit(x4[a:], y4[a:], 1)
#mA4, bA4 = np.polyfit(x4[a:], yA4[a:], 1)
#mK4, bK4 = np.polyfit(x4[a:], yK4[a:], 1)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.set_title(f"SPRING 1: {DP1_s.date()} - {DP1_e.date()}")
ax0.scatter(x1[a:], y1[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x1, m1*x1+b1, color='red')
#ax0.legend(loc='upper right')
ax0.set_ylabel("HCHO [ppb]", size="medium")

ax1.set_title(f"SUMMER 1: {DP2_s.date()} - {DP2_e.date()}")
ax1.scatter(x2[a:], y2[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x2, m2*x2+b2, color='red')

ax2.set_title(f"SPRING 2: {DP4_s.date()} - {DP4_e.date()}")
ax2.scatter(x4[a:], y4[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.set_ylabel("HCHO [ppb]", size="medium")
ax2.set_xlabel("Tmax [degC]", size="medium")
ax2.plot(x4, m4*x4+b4, color='red')

ax3.set_title(f"SUMMER 2: {DP3_s.date()} - {DP3_e.date()}")
ax3.scatter(x3[a:], y3[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.set_xlabel("Tmax [degC]", size="medium")
ax3.plot(x3, m3*x3+b3, color='red')

fig.tight_layout()
plt.show()
"""
"""HCHO - GLOBAL RADIATION"""
"""
pff = pd.concat([hcho19_dmax,BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
pff1 = pff[DP1_s:DP1_e].dropna()
x_i = pff1['GR'].values.flatten()
x1= x_i
y1 = pff1['1'].values.flatten()
a=0#92*24
m1, b1 = np.polyfit(x1[a:], y1[a:], 1)

pff2 = pff[DP2_s:DP2_e].dropna()
#pff2.columns = pff2.columns.droplevel(-1)
#isHighGRall = pff2["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff2[isHighGRall]
x_i = pff2['GR'].values.flatten()
x2= x_i       #FOR SIF
y2 = pff2['1'].values.flatten()
a=0#92*24
m2, b2 = np.polyfit(x2[a:], y2[a:], 1)

pff3 = pff[DP3_s:DP3_e].dropna()
#pff3.columns = pff3.columns.droplevel(-1)
#isHighGRall = pff3["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff3[isHighGRall]
x_i = pff3['GR'].values.flatten()
x3= x_i       #FOR SIF
y3 = pff3['1'].values.flatten()
a=0#92*24
m3, b3 = np.polyfit(x3[a:], y3[a:], 1)

pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff4 = pff[DP4_s:DP4_e].dropna()
#pff4.columns = pff4.columns.droplevel(-1)
#isHighGRall = pff4["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff4[isHighGRall]
x_i = pff4['GR'].values.flatten()
x4= x_i       #FOR SIF
y4 = pff4['1'].values.flatten()
yA4 = pff4['2'].values.flatten()
yK4 = pff4['3'].values.flatten()
a=0#92*24
m4, b4 = np.polyfit(x4[a:], y4[a:], 1)
#mA4, bA4 = np.polyfit(x4[a:], yA4[a:], 1)
#mK4, bK4 = np.polyfit(x4[a:], yK4[a:], 1)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.set_title(f"SPRING 1: {DP1_s.date()} - {DP1_e.date()}")
ax0.scatter(x1[a:], y1[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x1, m1*x1+b1, color='red')
#ax0.legend(loc='upper right')
ax0.set_ylabel("HCHO [ppb]", size="medium")

ax1.set_title(f"SUMMER 1: {DP2_s.date()} - {DP2_e.date()}")
ax1.scatter(x2[a:], y2[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x2, m2*x2+b2, color='red')

ax2.set_title(f"SPRING 2: {DP4_s.date()} - {DP4_e.date()}")
ax2.scatter(x4[a:], y4[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.set_ylabel("HCHO [ppb]", size="medium")
ax2.set_xlabel("global rad sum [Wh m-2]", size="medium")
ax2.plot(x4, m4*x4+b4, color='red')

ax3.set_title(f"SUMMER 2: {DP3_s.date()} - {DP3_e.date()}")
ax3.scatter(x3[a:], y3[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.set_xlabel("global rad sum [Wh m-2]", size="medium")
ax3.plot(x3, m3*x3+b3, color='red')

fig.tight_layout()
plt.show()
"""
"""FULL SEASON"""

pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
print(pff[March:])
pff5 = pff[:].dropna()
#pff4.columns = pff4.columns.droplevel(-1)
#isHighGRall = pff4["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff4[isHighGRall]
x5 = pff5['4'].values.flatten() #AT!
x5_GR = pff5['GR'].values.flatten()
y5 = pff5['1'].values.flatten()
yA5 = pff5['2'].values.flatten()
yK5 = pff5['3'].values.flatten()
a=0#92*24
m5, b5 = np.polyfit(x5[a:], y5[a:], 1)
mA5, bA5 = np.polyfit(x5[a:], yA5[a:], 1)
mK5, bK5 = np.polyfit(x5[a:], yK5[a:], 1)

m5GR, b5GR = np.polyfit(x5_GR[a:], y5[a:], 1)
mA5GR, bA5GR = np.polyfit(x5_GR[a:], yA5[a:], 1)
mK5GR, bK5GR = np.polyfit(x5_GR[a:], yK5[a:], 1)


fig, axes = plt.subplots(nrows=1, ncols=2)
#plt.set_title(f"full period")
ax0, ax1 = axes.flatten()
#ax0.set_title(f"SPRING 1: {DP1_s.date()} - {DP1_e.date()}")

ax0.scatter(x5[a:], y5[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.scatter(x5[a:], yA5[a:], color='violet',label='Axis A ') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.scatter(x5[a:], yK5[a:], color='green',label='Axis K ') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x5, m5*x5+b5, color='red')
ax0.plot(x5, mA5*x5+bA5, color='violet')
ax0.plot(x5, mK5*x5+bK5, color='green')

#ax0.legend(loc='upper right')
ax0.set_ylabel("HCHO [ppb]", size="medium")
ax0.set_xlabel("air temp [degC]", size="medium")

#ax1.set_title(f"SUMMER 1: {DP2_s.date()} - {DP2_e.date()}")
ax1.scatter(x5_GR[a:], y5[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.scatter(x5_GR[a:], yA5[a:], color='violet',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.scatter(x5_GR[a:], yK5[a:], color='green',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x5_GR, m5GR*x5_GR + b5GR, color='red')
ax1.plot(x5_GR, mA5GR*x5_GR + bA5GR, color='violet')
ax1.plot(x5_GR, mK5GR*x5_GR + bK5GR, color='green')
ax1.set_ylabel("HCHO [ppb]", size="medium")
ax1.set_xlabel("GR [degC]", size="medium")


fig.tight_layout()
plt.show()


pff = pd.concat([hcho_dmax,BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
print(pff[:])
pff5 = pff[:].dropna()
#pff4.columns = pff4.columns.droplevel(-1)
#isHighGRall = pff4["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff4[isHighGRall]
x5 = pff5['4'].values.flatten() #AT!
x5_GR = pff5['GR'].values.flatten()
y5 = pff5['1'].values.flatten()
a=0#92*24
m5, b5 = np.polyfit(x5[a:], y5[a:], 1)
m5GR, b5GR = np.polyfit(x5_GR[a:], y5[a:], 1)

fig, axes = plt.subplots(nrows=1, ncols=2)
#plt.set_title(f"full period")
ax0, ax1 = axes.flatten()
#ax0.set_title(f"SPRING 1: {DP1_s.date()} - {DP1_e.date()}")
ax0.scatter(x5[a:], y5[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x5, m5*x5+b5, color='red')
#ax0.legend(loc='upper right')
ax0.set_ylabel("HCHO [ppb]", size="medium")
ax0.set_xlabel("air temp [degC]", size="medium")
#ax1.set_title(f"SUMMER 1: {DP2_s.date()} - {DP2_e.date()}")
ax1.scatter(x5_GR[a:], y5[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x5_GR, m5GR*x5_GR + b5GR, color='red')
ax1.set_ylabel("HCHO [ppb]", size="medium")
ax1.set_xlabel("GR [degC]", size="medium")


fig.tight_layout()
plt.show()


""""
#BACKUP

#pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,wrfc2020_hcho1_dmax,metclass],axis=1, keys=['1','2','3','4','WLK'])
#pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,camx3_2020_HCHO_dmax,BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,tsif,BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff = pff[June:Sept].dropna()
pff.columns = pff.columns.droplevel(-1)
print(pff)
#pff = pff.drop(pff[pff.WLK == "C"].index)
#print(pff)

isHighGRall = pff["GR"] > 15000 #15 KWh (per day) Globalstrahlung
pff_HighGRdays = pff[isHighGRall]
print(pff_HighGRdays)

#pff = pff_HighGRdays

#print(wrfc2020_hcho1_dmax.values.shape)
x_i = pff['4'].values.flatten()
#print(x_i.shape)
#x= x_i*1000 #FOR WRF-CHEM + CAMX
x= x_i       #FOR SIF
y = pff['1'].values.flatten()
yA = pff['2'].values.flatten()
yK = pff['3'].values.flatten()

a=0#92*24
m, b = np.polyfit(x[a:], y[a:], 1)
mA, bA = np.polyfit(x[a:], yA[a:], 1)
mK, bK = np.polyfit(x[a:], yK[a:], 1)
print(m,mA,mK,b,bA,bK)

#R2_Forc_NO2concentr = (stats.spearmanr(o3, no2))[0] ** 2

fig2 = plt.figure()
plt.scatter(x[a:], y[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
plt.scatter(x[a:], yA[a:], color='violet',label='Axis A (Vetmed)') #label=r"$r$=%.2f" % (R_hcho))
plt.scatter(x[a:], yK[a:], color='green',label='Axis K (Wienerwald)')
plt.plot(x, m*x+b, color='red')
plt.plot(x, mA*x+bA, color='violet')
plt.plot(x, mK*x+bK, color='green')
#m, b = np.polyfit(x, y, 1)
#plt.plot(x, m * x + b)
plt.legend(loc='upper right')
#plt.xlabel("WRF [ppb]", size="medium")
#plt.xlabel("CAMX [ppb]", size="medium")
plt.xlabel("TROPOMI SIF [mW m-2 sr-1 nm-1]", size="medium")
plt.ylabel("MAXDOAS [ppb]", size="medium")
#plt.suptitle("HCHO dmax 2020 summer (JJA)")
plt.show()
"""