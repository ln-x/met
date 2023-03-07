# -*- coding: utf-8 -*-
__author__ = 'lnx'

import numpy as np
import pandas as pd
from datetime import datetime
import monthdelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import BOKUMet_Data
from Datetime_recipies import datestdtojd
from conversions import *
import ReadinVindobona_Filter_fullperiod

print(ugm3toppb_no2, ugm3toppb_no)


"read in VINDOBONA"
foldername_D = "/Users/lnx/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_f, hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))
hcho_w = hcho_dmax.resample("W").mean()

'''READ IN BOKU Metdata'''
BOKUMetData = BOKUMet_Data.BOKUMet()
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
BOKUMetData_weekly = BOKUMetData_dailysum.resample('W').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                      'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

vp_sat = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3))  #kPa sh. Dingman
vp_air = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3)) * (BOKUMetData_hourlymean["RH"]/100)
vpd = vp_sat - vp_air
#print(vp_sat,vp_air, vpd)
#vpd.plot()
#plt.show()
vpd_d = vpd.resample('D').mean()
vpd_dmax = vpd.resample('D').max()
vpd_dmax_w = vpd_dmax.resample('W').max()

'''READ IN EEA air pollution data'''
pathbase2 = "/Users/lnx/DATA/obs_point/chem/EEA/"
#"AT"+compound+"stationsname"+"year"+_"timeseries.csv"
nox_1990_2019_da = pd.read_csv(pathbase2 + "nox_da_1990-2019_AT_ppb.csv")
nox_1990_2019_da = nox_1990_2019_da.set_index(pd.to_datetime(nox_1990_2019_da['date']))
nox_1990_2019_da = nox_1990_2019_da.drop(columns=['date'])
no2_2020_mda1 = pd.read_csv(pathbase2 + "AT_NO2_2020.csv")
no2_2020_mda1 = no2_2020_mda1.set_index(pd.to_datetime(no2_2020_mda1['date']))
no2_2020_mda1 = no2_2020_mda1.drop(columns=['date'])

no2_2020_mda1 = no2_2020_mda1*0.5319148936 #ugm3toppb_no2
no2_2020_da = no2_2020_mda1.resample('D').mean()
no_2020_mda1 = pd.read_csv(pathbase2 + "AT_NO_2020.csv")
no_2020_mda1 = no_2020_mda1.set_index(pd.to_datetime(no_2020_mda1['date']))
no_2020_mda1 = no_2020_mda1.drop(columns=['date'])
no_2020_mda1 = no_2020_mda1*0.8 #ugm3toppb_no
no_2020_da = no_2020_mda1.resample('D').mean()
nox_2020_da = no_2020_da.add(no2_2020_da)
nox_1990_2020_da = pd.concat([nox_1990_2019_da, nox_2020_da], axis=0)
nox_1990_2020_da_w = nox_1990_2020_da.resample('W').mean()

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
o3_2020_mda8 = o3_2020_mda1.resample('8H', label='right').mean()
o3_2020_mda8 = o3_2020_mda8.resample('D').mean()
o3_1990_2020_mda8 = pd.concat([o3_1990_2019_mda8, o3_2020_mda8], axis=0)
o3_1990_2020_mda8 = o3_1990_2020_mda8#*ugm3toppb_o3 #MUG->PPB
o3_1990_2020_da = o3_1990_2020_mda8.resample('D').mean()
o3_1990_2020_m = o3_1990_2020_mda8.resample('M').mean()
o3_1990_2020_mda1_w = o3_1990_2020_mda1.resample('W').mean()
o3_1990_2020_mda8_w = o3_1990_2020_mda8.resample('W').mean()


'''READ in SOIL MOISTURE DATA'''

file_sm_2019_rutz = "/Users/lnx/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/RUT_10_min.xls"
sm = pd.read_excel(file_sm_2019_rutz, sheet_name="RUT_d", usecols="D,K,L,M,N,O,P", skiprows=11)#, converters={'A': pd.to_datetime})
sm.columns = ['datetime', 'VWC1 min[%]', 'VWC2 min[%]','VWC3 min[%]','VWC1 max[%]', 'VWC2 max[%]','VWC3 max[%]']
sm = sm.set_index(pd.to_datetime(sm['datetime']))
sm = sm.drop(columns=['datetime'])
#print(sm)
#exit()

file_rss_rutz = "/Users/lnx/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/2008_2020_Rutzendorf_ARIS_results_sepp.xlsx"
#rss = pd.read_excel(file_rss_rutz, sheet_name="RSS_top", usecols="A,B,C,D,E,F", skiprows=11)#, converters={'A': pd.to_datetime})
rss = pd.read_excel(file_rss_rutz, sheet_name="RSS_sub", usecols="A,B,C,D,E,F", skiprows=11)#, converters={'A': pd.to_datetime})
#rss.columns = ['datetime', 'RSS_top_maize', 'RSS_top_sBarley','RSS_top_sugBeet','RSS_top_wWheat', 'RSS_top_grass']
rss.columns = ['datetime', 'RSS_sub_maize', 'RSS_sub_sBarley','RSS_sub_sugBeet','RSS_sub_wWheat', 'RSS_sub_grass']  #TODO: local time!
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
tsif_r = pd.read_csv("/Users/lnx/DATA/remote/satellite/TROPOMI/TSIF_743_LAT48_28_LON16_23.csv", sep=",")
tsif = tsif_r.set_index(pd.to_datetime(tsif_r['time']))
tsif = tsif.drop(columns=['time'])
tsif.columns = ['SIF']
tsif_m =tsif.resample('M').mean()
tsif_w =tsif.resample('W').mean()


#osif_771_r = pd.read_csv("/windata/DATA/remote/satellite/OCO/OSIF_8100_771nm.csv", sep=",")
#osif_771 = osif_771_r.set_index(pd.to_datetime(osif_771_r['time']))
#osif_771 = osif_771.drop(columns=['time'])

osif_757_r = pd.read_csv("/Users/lnx/DATA/remote/satellite/OCO2/OSIF_8100_757nm.csv", sep=",")
osif_757 = osif_757_r.set_index(pd.to_datetime(osif_757_r['time']))
osif_757 = osif_757.drop(columns=['time'])
osif_757_m =osif_757.resample('M').mean()
osif_757_w =osif_757.resample('W').mean()
osif_757.columns = ['SIF']

sif_joint = pd.concat([osif_757[:datetime(2018,7,1)],tsif[datetime(2018,7,1):]], axis=0)

"read in EDO - fAPAR data"
fAPAR = pd.read_csv("/Users/lnx/DATA/obs_point/land/EDO/fAPAR.16_48.1990to2021.20211217133422.txt", delimiter="|",skiprows=2,header=0)

fAPAR['Date'] = fAPAR['Date'].str.replace('III', '20', regex=False)
fAPAR['Date'] = fAPAR['Date'].str.replace("II", "10")
fAPAR['Date'] = fAPAR['Date'].str.replace("I", "01")
#exit()
fAPAR = fAPAR.set_index(pd.to_datetime(fAPAR['Date'])) #utc=True
fAPAR = fAPAR.drop(columns=['Date'])

#Unified Graph Creator - (c) EDO 2021
#lon,lat|16.25,48.28
#Date|fAPAR Anomaly
#2017-01-I|-0.54
#2017-01-II|0.02

'''TIMESLICES'''
JJA19_s = datetime(2019, 6, 1, 00, 00)
JJA19_e = datetime(2019, 8, 31, 00, 00)
JJA19_e2 = datetime(2019, 9, 1, 00, 00)
JJA20_s = datetime(2020, 6, 1, 00, 00)
JJA20_e = datetime(2020, 8, 31, 00, 00)
JJA20_e2 = datetime(2020, 9, 7, 00, 00)

start = JJA19_s
end = datetime(2019, 9, 1, 00, 00)
start3 = datetime(2020, 7, 15, 00, 00)

hcho_sigma = hcho_d.std()
vpd_dmax_sigma = vpd_dmax.std()
tmax_sigma = BOKUMetData_dailymax["AT"][start:end].std()

'''
Plotting
'''
fig = plt.figure()
#plt.suptitle(f"OBS {JJA19_s} - {JJA19_e}")
ax1 = fig.add_subplot(611)
ax1.set_title('(a)', loc='left', size='medium')#, color='green')
x1 = plt.gca()
ax2 = ax1.twinx()
ax2.plot(o3_1990_2020_mda8_w['AT9STEF'][JJA19_s:JJA19_e2],linewidth="1", color='violet', linestyle="solid",label="O3") #label="O3,mda8,w",
ax2.plot(o3_1990_2020_mda8_w['AT9STEF'][JJA19_s:JJA19_e2].index, o3_1990_2020_mda8_w['AT9STEF'][JJA20_s:datetime(2020, 9, 7)].values,linewidth="1", color='violet', linestyle=":")
ax1.plot((BOKUMetData_weekly["GR"][JJA19_s:JJA19_e2])/1000, linewidth="1", color='orange', label="GR") #label="GR,sum,w"
ax1.plot(BOKUMetData_weekly["GR"][JJA19_s:JJA19_e2].index,BOKUMetData_weekly["GR"][JJA20_s:JJA20_e2].values/1000, linewidth="1", color='orange', linestyle=":")
ax1.grid()
ax1.set_xlim(JJA19_s,JJA19_e)
ax1.xaxis.set_major_formatter(mdates.DateFormatter(' '))

ax1.set_ylabel("[kWh/m²]", size="medium")
ax2.set_ylabel("[μg/m³]", size="medium")  #\mu
#ax1.legend(loc='upper left',framealpha=1, facecolor="white")
#ax2.legend(loc='lower left',framealpha=1, facecolor="white")

ax1 = fig.add_subplot(612)
ax1.set_title('(b)', loc='left', size='medium')#, color='green')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(tsif_w,color='violet', label="SIF") #label="SIF_w"
ax1.plot(tsif_w[datetime(2019, 6, 1):datetime(2019, 8, 31)].index, tsif_w[datetime(2020, 6, 1):datetime(2020, 9, 1)].values, color='violet',linestyle=":")#,label="OCO-2 SIF")
ax1.set_ylabel("[mW/m2/sr/nm]", size="medium")
ax2.plot(fAPAR[datetime(2019, 6, 1):datetime(2019, 9, 1)],color='green', label="fAPARa")#label="fAPAR anomaly"
ax2.plot(fAPAR[datetime(2019, 6, 1):datetime(2019, 9, 1)].index, fAPAR[datetime(2020, 6, 1):datetime(2020, 9, 1)].values,color='green', linestyle=":")
ax2.set_ylabel("[-]", size="medium")
ax1.xaxis.set_major_formatter(mdates.DateFormatter(' '))

ax1.grid()
ax1.set_xlim(JJA19_s,JJA19_e)
#ax1.legend(loc='upper left',framealpha=1, facecolor="white")
#ax2.legend(loc='lower left',framealpha=1, facecolor="white")

ax1 = fig.add_subplot(613)
ax1.set_title('(c)', loc='left', size='medium')#, color='green')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(vwc['RSS_sub_wWheat'][JJA19_s:JJA19_e],linewidth="1", color='orange', linestyle="solid", label="RSS_w") #label="RSS_sub_w",
ax1.plot(vwc['RSS_sub_wWheat'][JJA19_s:JJA19_e].index,vwc['RSS_sub_wWheat'][JJA20_s:JJA20_e].values,linewidth="1", color='orange', linestyle=":") #label="RSS_sub_w",
#ax1.plot(vwc['RSS_sub_grass'][JJA19_s:JJA19_e],linewidth="1", color='green', linestyle="solid", label="RSS_g") #label="RSS_sub_g"
#ax1.plot(vwc['RSS_sub_grass'][JJA19_s:JJA19_e].index,vwc['RSS_sub_grass'][JJA20_s:JJA20_e].values,linewidth="1", color='green', linestyle=":")
ax2.step(BOKUMetData_dailysum[JJA19_s:JJA19_e].index,(BOKUMetData_dailysum["PC"]*0.1)[JJA19_s:JJA19_e], linewidth="0.3", color='blue', label="PR") #{'pre', 'post', 'mid'} label="PR,sum"
ax2.step(BOKUMetData_dailysum[JJA19_s:JJA19_e].index,(BOKUMetData_dailysum["PC"]*0.1)[JJA20_s:JJA20_e].values, linewidth="0.3", color='blue', linestyle=":") #{'pre', 'post', 'mid'}  label="PR,sum",
ax2.set_ylabel("[mm]", size="medium")
ax1.set_ylabel("[-]", size="medium")
ax1.xaxis.set_major_formatter(mdates.DateFormatter(' '))

ax1.grid()
ax1.set_xlim(JJA19_s,JJA19_e)
#ax1.legend(loc='upper left', framealpha=1, facecolor="white")
#ax2.legend(loc='lower left', framealpha=1, facecolor="white")

ax1 = fig.add_subplot(614)
ax1.set_title('(d)', loc='left', size='medium')#, color='green')
ax1 = plt.gca()
#ax1.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
ax1.plot(vpd_dmax_w[JJA19_s:JJA19_e2], linewidth="1", color='green', label="VPD")#, label="vpd,dmax,w")
ax1.plot(vpd_dmax_w[JJA19_s:JJA19_e2].index, vpd_dmax_w[JJA20_s:datetime(2020, 9, 7)].values, linewidth="1", color='green', linestyle=":")
ax1.fill_between(vpd_dmax_w[JJA19_s:JJA19_e2].index, vpd_dmax_w[JJA19_s:JJA19_e2].values.flatten()+vpd_dmax_sigma,vpd_dmax_w[JJA19_s:JJA19_e2].values.flatten()-vpd_dmax_sigma, facecolor='green', alpha=0.1)
ax1.fill_between(vpd_dmax_w[JJA19_s:JJA19_e2].index, vpd_dmax_w[JJA20_s:JJA20_e2].values.flatten()+vpd_dmax_sigma,vpd_dmax_w[JJA20_s:JJA20_e2].values.flatten()-vpd_dmax_sigma, facecolor='grey', alpha=0.1)
ax1.set_xlim(JJA19_s,JJA19_e)
ax1.xaxis.set_major_formatter(mdates.DateFormatter(' '))
ax1.set_ylabel("[kPa]", size="medium")
ax1.grid()
#ax1.legend(loc='upper left',framealpha=1, facecolor="white")

ax1 = fig.add_subplot(615)
ax1.set_title('(e)', loc='left', size='medium')#, color='green')
ax1 = plt.gca()
#ax1.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
ax1.plot((BOKUMetData_weekly["AT"][JJA19_s:JJA19_e2]), linewidth="1", color='red', label="AT") #label="GR,sum,w"
ax1.plot(BOKUMetData_weekly["AT"][JJA19_s:JJA19_e2].index,BOKUMetData_weekly["AT"][JJA20_s:JJA20_e2].values, linewidth="1", color='red', linestyle=":")
ax1.fill_between(BOKUMetData_weekly["AT"][JJA19_s:JJA19_e2].index, BOKUMetData_weekly["AT"][JJA19_s:JJA19_e2].values.flatten()+tmax_sigma,BOKUMetData_weekly["AT"][JJA19_s:JJA19_e2].values.flatten()-tmax_sigma, facecolor='red', alpha=0.1)
ax1.fill_between(BOKUMetData_weekly["AT"][JJA19_s:JJA19_e2].index, BOKUMetData_weekly["AT"][JJA20_s:JJA20_e2].values.flatten()+tmax_sigma,BOKUMetData_weekly["AT"][JJA20_s:JJA20_e2].values.flatten()-tmax_sigma, facecolor='grey', alpha=0.1)
ax1.set_xlim(JJA19_s,JJA19_e)
#ax2.axvline(x=datetime(2020,5,10))
ax1.xaxis.set_major_formatter(mdates.DateFormatter(' '))
ax1.set_ylabel("[°C]", size="medium")
#ax1.legend(loc='upper left', framealpha=1, facecolor="white")
ax1.grid()

ax1 = fig.add_subplot(616)
ax1.set_title('(f)', loc='left', size='medium')#, color='green')
ax1 = plt.gca()
#ax1.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
ax1.plot(hcho_w[JJA19_s:datetime(2019, 9, 7)], linewidth="1", color='black',label="HCHO")#, label="HCHO,dmax,w", linestyle="solid")
ax1.plot(hcho_w[JJA19_s:datetime(2019, 9, 7)].index,hcho_w[JJA20_s:datetime(2020, 9, 7)].values, linewidth="1", color='black', linestyle=":")
ax1.fill_between(hcho_w[JJA19_s:JJA19_e2].index, hcho_w[JJA19_s:JJA19_e2].values.flatten()+hcho_sigma,hcho_w[JJA19_s:JJA19_e2].values.flatten()-hcho_sigma, facecolor='black', alpha=0.1)
ax1.fill_between(hcho_w[JJA19_s:JJA19_e2].index, hcho_w[JJA20_s:JJA20_e2].values.flatten()+hcho_sigma,hcho_w[JJA20_s:JJA20_e2].values.flatten()-hcho_sigma, facecolor='grey', alpha=0.1)
ax1.set_xlim(JJA19_s,JJA19_e)
#ax2.axvline(x=datetime(2020,5,10))
ax1.set_ylabel("[ppb]", size="medium")
#ax1.legend(loc='upper left',framealpha=1, facecolor="white")
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1.grid()
plt.show()
