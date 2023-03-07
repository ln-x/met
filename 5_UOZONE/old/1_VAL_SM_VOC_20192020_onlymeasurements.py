# -*- coding: utf-8 -*-
__author__ = 'lnx'

import numpy as np
import pandas as pd
from datetime import datetime
import monthdelta
import matplotlib.pyplot as plt
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVindobona_Filter
from met.library import ReadinVindobona_Filter2019

"read in VINDOBONA"

foldername = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2020/DQ/"
foldername2019 = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2019/"
foldername_A = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2020/AQ/"
foldername_K = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2020/KQ/"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter.loadfileALL(foldername)
hcho19_d, hcho19_dmax, hcho19_m = ReadinVindobona_Filter2019.loadfileALL(foldername2019)
hcho_d_A, hcho_dmax_A, hcho_m_A = ReadinVindobona_Filter.loadfileALL(foldername_A)
hcho_d_K, hcho_dmax_K, hcho_m_K = ReadinVindobona_Filter.loadfileALL(foldername_K)

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

'''READ IN EEA air pollution data'''
pathbase2 = "/windata/DATA/obs_point/chem/EEA/"
#"AT"+compound+"stationsname"+"year"+_"timeseries.csv"
nox_1990_2019_da = pd.read_csv(pathbase2 + "nox_da_1990-2019_AT_ppb.csv")
nox_1990_2019_da = nox_1990_2019_da.set_index(pd.to_datetime(nox_1990_2019_da['date']))
nox_1990_2019_da = nox_1990_2019_da.drop(columns=['date'])
no2_2020_mda1 = pd.read_csv(pathbase2 + "AT_NO2_2020.csv")
no2_2020_mda1 = no2_2020_mda1.set_index(pd.to_datetime(no2_2020_mda1['date']))
no2_2020_da = no2_2020_mda1.resample('D').mean()
no_2020_mda1 = pd.read_csv(pathbase2 + "AT_NO_2020.csv")
no_2020_mda1 = no_2020_mda1.set_index(pd.to_datetime(no_2020_mda1['date']))
no_2020_da = no_2020_mda1.resample('D').mean()
nox_2020_da = no_2020_da.add(no2_2020_da)
nox_1990_2020_da = pd.concat([nox_1990_2019_da, nox_2020_da], axis=0)

o3_1990_2019_mda1 = pd.read_csv(pathbase2 + "o3_mda1_1990-2019_AT_mug.csv")
o3_1990_2019_mda1 = o3_1990_2019_mda1.set_index((pd.to_datetime(o3_1990_2019_mda1['date'])))
o3_1990_2019_mda1 = o3_1990_2019_mda1.drop(columns=['date'])
o3_1990_2019_mda8 = pd.read_csv(pathbase2 + "o3_mda8_1990-2019_AT_mug.csv")
o3_1990_2019_mda8 = o3_1990_2019_mda8.set_index(pd.to_datetime(o3_1990_2019_mda8['date']))
o3_1990_2019_mda8 = o3_1990_2019_mda8.drop(columns=['date'])
o3_2020_mda1 = pd.read_csv(pathbase2 + "AT_O3_2020.csv")
o3_2020_mda1 = o3_2020_mda1.set_index(pd.to_datetime(o3_2020_mda1['date']))
o3_2020_mda1 = o3_2020_mda1.drop(columns=['date'])
o3_1990_2020_mda1 = pd.concat([o3_1990_2019_mda1, o3_2020_mda1], axis=0)
o3_1990_2020_da = o3_1990_2020_mda1.resample('D').mean()
o3_1990_2020_m = o3_1990_2020_mda1.resample('M').mean()
#print(o3_1990_2020_da["AT90LOB"])
#o3_1990_2020_da["AT90LOB"].plot()
#plt.show()



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

vwc = rutz_fc_top_Layer - (1-rss)*rutz_afc_top_Layer
vwc_grass = grass_fc_top_Layer - (1-rss)*grass_afc_top_Layer

starttime = datetime(2019, 1, 1, 0, 00)
wrfc_time_construct_months = np.array([starttime + monthdelta.monthdelta(i) for i in range(24)])
wrflai_megan = [471,540,562,1278,2367,2456,2047,1718,1685,1335,807,1003,471,540,562,1278,2367,2456,2047,1718,1685,1335,807,1003]
wrflai_megan = pd.Series(wrflai_megan[:],index=wrfc_time_construct_months)
#print(hcho.index[starttime])

#TSIF_743
tsif_r = pd.read_csv("/windata/DATA/remote/satellite/TROPOMI/TSIF_743.csv", sep=",")
tsif = tsif_r.set_index(pd.to_datetime(tsif_r['time']))
tsif = tsif.drop(columns=['time'])
tsif_d =tsif.resample('M').mean()

#osif_771_r = pd.read_csv("/windata/DATA/remote/satellite/OCO/OSIF_8100_771nm.csv", sep=",")
#osif_771 = osif_771_r.set_index(pd.to_datetime(osif_771_r['time']))
#osif_771 = osif_771.drop(columns=['time'])

osif_757_r = pd.read_csv("/windata/DATA/remote/satellite/OCO2/OSIF_8100_757nm.csv", sep=",")
osif_757 = osif_757_r.set_index(pd.to_datetime(osif_757_r['time']))
osif_757 = osif_757.drop(columns=['time'])
osif_757_d =osif_757.resample('M').mean()

'''TIMESLICES'''
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
NW3_e = datetime(2019, 8, 24, 00, 00)

'''
Plotting
'''
#start = datetime(2020, 1, 1, 00, 00)
start = datetime(2019, 1, 1, 00, 00)
#start = datetime(2017, 1, 1, 00, 00)
#end = datetime(2020, 1, 1, 00, 00)
end = datetime(2020, 9, 27, 00, 00)
end2 = datetime(2020, 10, 30, 00, 00)

fig = plt.figure()
plt.suptitle(f"OBS/MOD {start} - {end}")

ax1 = fig.add_subplot(411)
#ax1 = fig.add_subplot(211)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.plot(o3_1990_2020_da['AT9STEF'][start:end]*ugm3toppb_o3,linewidth="1", color='violet', label="o3 OBS da", linestyle="solid")
ax2.plot(nox_1990_2020_da['AT9STEF'][start:end],linewidth="1", color='blue', label="nox OBS da", linestyle="solid")
ax1.plot(hcho_d[start:end], linewidth="1", color='black', label="hcho D OBS d", linestyle="solid") #274 = Julian Day 30.Sept2020
ax1.plot(hcho19_d[start:end], linewidth="1", color='black', linestyle="solid")
#ax1.plot(hcho_dmax[start:end], linewidth="1", color='black', label="hcho OBS dmax", linestyle="solid") #274 = Julian Day 30.Sept2020
ax1.plot(hcho_m[start:end], linewidth="0.5", color='black', label="hcho D OBS mmax", linestyle="-") #274 = Julian Day 30.Sept2020
ax1.plot(hcho_m_A[start:end], linewidth="0.5", color='grey', label="hcho A OBS mmax", linestyle="-") #274 = Julian Day 30.Sept2020
ax1.plot(hcho_m_K[start:end], linewidth="0.5", color='darkgrey', label="hcho K OBS mmax", linestyle="-") #274 = Julian Day 30.Sept2020
#ax1.set_ylim(0, 8)
ax1.axvspan(DP1_s, DP1_e, color='red', alpha=0.2)
ax1.axvspan(DP2_s, DP2_e, color='red', alpha=0.2)
ax1.axvspan(DP3_s, DP3_e, color='red', alpha=0.2)
ax1.axvspan(DP4_s, DP4_e, color='red', alpha=0.2)
ax1.set_xlabel("days")
ax1.set_xlim(start,end)
ax1.set_ylabel("[ppb]", size="medium")
ax2.set_ylabel("[ppb]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

ax1 = fig.add_subplot(412)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.plot(tsif[start:end], color='violet', label="Tropomi SIF 743nm", marker="x", linestyle=" ")
ax2.plot(tsif_d[start:end],color='violet')
ax2.plot(osif_757, color='red', label="OCO2 SIF 757nm", marker="x", linestyle=" ")
ax2.plot(osif_757_d,color='red')
ax2.set_ylabel("[mW/m2/sr/nm]", size="medium")
#ax1.plot(wrfc2020_lai[start:end],linewidth="0.5", color='blue', label="lai_wrfc", linestyle="dashed")
ax1.plot(wrflai_megan[start:end], linewidth="0.5", color='blue', label="lai_wrf_megan", linestyle="solid")
#ax1.set_ylim(-5, 35)
ax1.axvspan(DP1_s, DP1_e, color='red', alpha=0.2)
ax1.axvspan(DP2_s, DP2_e, color='red', alpha=0.2)
ax1.axvspan(DP3_s, DP3_e, color='red', alpha=0.2)
ax1.axvspan(DP4_s, DP4_e, color='red', alpha=0.2)
ax1.set_xlabel("days")
ax1.set_ylabel("[degree]", size="medium")
ax1.set_ylim(0, 3500)
#ax2.set_ylabel("[ppb]", size="medium")
#ax1.set_ylabel("LAI [m2 m-2]", size="medium") #TODO convert degree to m2 m-2
#ax2.set_ylabel("dry deposition velocity [cm s-1]", size="medium")
ax1.set_xlim(start,end)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

ax1 = fig.add_subplot(413)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(sm['VWC1 min[%]'][start:end],linewidth="1", color='black', label="sm_rutz1 min 0-30 cm OBS ", linestyle="solid")
ax1.plot(sm['VWC2 min[%]'][start:end],linewidth="1", color='darkgrey', label="sm_rutz2 min 0-30 cm  OBS ", linestyle="solid")
ax1.plot(sm['VWC3 min[%]'][start:end],linewidth="1", color='lightgrey', label="sm_rutz3 min 0-30 cm OBS ", linestyle="solid")
ax1.plot(sm['VWC1 max[%]'][start:end],linewidth="0.5", color='black', label="sm_rutz1 max 0-30 cm OBS ", linestyle="solid")
ax1.plot(sm['VWC2 max[%]'][start:end],linewidth="0.5", color='darkgrey', label="sm_rutz2 max 0-30 cm OBS ", linestyle="solid")
ax1.plot(sm['VWC3 max[%]'][start:end],linewidth="0.5", color='lightgrey', label="sm_rutz3 max 0-30 cm OBS ", linestyle="solid")
#ax1.plot(rss['RSS_top_wWheat'][start:end],linewidth="1", color='darkred', label="rss rutz2 0-40 cm ARIS", linestyle="solid")
ax1.plot(vwc['RSS_top_wWheat'][start:end],linewidth="1", color='red', label="sm rutz2 0-40 cm ARIS wWheat", linestyle="solid")
ax1.plot(vwc['RSS_top_maize'][start:end],linewidth="1", color='orange', label="sm rutz2 0-40 cm ARIS maize", linestyle="solid")
ax1.plot(vwc['RSS_top_sBarley'][start:end],linewidth="1", color='brown', label="sm rutz2 0-40 cm ARIS sBarley", linestyle="solid")
ax1.plot(vwc['RSS_top_sugBeet'][start:end],linewidth="1", color='purple', label="sm rutz2 0-40 cm ARIS sugBeet", linestyle="solid")
ax1.plot(vwc_grass['RSS_top_grass'][start:end],linewidth="1", color='green', label="sm rutz2 0-40 cm ARIS grass", linestyle="solid")

ax2.plot((BOKUMetData_dailysum["PC"]*0.1)[start:end], linewidth="1", color='turquoise', label="prec BOKUR OBS")
ax1.axvspan(DP1_s, DP1_e, color='red', alpha=0.2)
ax1.axvspan(DP2_s, DP2_e, color='red', alpha=0.2)
ax1.axvspan(DP3_s, DP3_e, color='red', alpha=0.2)
#ax1.axvspan(DP4_s, DP4_e, color='red', alpha=0.2)
ax2.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
ax1.set_xlabel("days")
ax2.set_ylabel("[mm]", size="medium")
ax1.set_ylabel("[m3 m-3]", size="medium")
ax1.set_xlim(start,end)
ax1.legend(loc='upper left',fontsize="small")
ax2.legend(loc='upper right',fontsize="small")

ax1 = fig.add_subplot(414)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
ax1.plot(BOKUMetData_dailymax["AT"][start:end], linewidth="1", color='lightsalmon', label="t2dmax BOKUR OBS")
#ax1.plot(BOKUMetData_monthly["AT"][start:end], linewidth="1", color='lightsalmon', label="t2_obs_BOKUR_m")
ax2.plot(BOKUMetData_dailysum["GR"][start:end], linewidth="1", color='orange', label="gr dmax BOKUR OBS")
#ax2.plot(BOKUMetData_monthly["GR"][start:end], linewidth="1", color='orange', label="gr_obs_BOKUR_m")
#ax1.plot(tas_m[start:end]-273.15,linewidth="1", color='darkred', label="t2_wrfc_m", linestyle="dashed")
#ax1.set_ylim(-5, 35)
ax1.set_xlim(start,end)
ax1.axvspan(DP1_s, DP1_e, color='red', alpha=0.2)
ax1.axvspan(DP2_s, DP2_e, color='red', alpha=0.2)
ax1.axvspan(DP3_s, DP3_e, color='red', alpha=0.2)
#ax1.axvspan(DP4_s, DP4_e, color='red', alpha=0.2)
ax1.set_xlabel("days")
ax1.set_ylabel("[degC]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()
