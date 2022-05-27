# -*- coding: utf-8 -*-
__author__ = 'lnx'

import numpy as np
import pandas as pd
from datetime import datetime
import monthdelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVindobona_Filter_fullperiod

print(ugm3toppb_no2, ugm3toppb_no)


"read in VINDOBONA"
foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))
hcho_w = hcho_dmax.resample("W").mean()

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
pathbase2 = "/windata/DATA/obs_point/chem/EEA/"
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

file_sm_2019_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/RUT_10_min.xls"
sm = pd.read_excel(file_sm_2019_rutz, sheet_name="RUT_d", usecols="D,K,L,M,N,O,P", skiprows=11)#, converters={'A': pd.to_datetime})
sm.columns = ['datetime', 'VWC1 min[%]', 'VWC2 min[%]','VWC3 min[%]','VWC1 max[%]', 'VWC2 max[%]','VWC3 max[%]']
sm = sm.set_index(pd.to_datetime(sm['datetime']))
sm = sm.drop(columns=['datetime'])
#print(sm)
#exit()

file_rss_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/2008_2020_Rutzendorf_ARIS_results_sepp.xlsx"
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
tsif_r = pd.read_csv("/windata/DATA/remote/satellite/TROPOMI/TSIF_743_LAT48_28_LON16_23.csv", sep=",")
tsif = tsif_r.set_index(pd.to_datetime(tsif_r['time']))
tsif = tsif.drop(columns=['time'])
tsif.columns = ['SIF']
tsif_m =tsif.resample('M').mean()
tsif_w =tsif.resample('W').mean()


#osif_771_r = pd.read_csv("/windata/DATA/remote/satellite/OCO/OSIF_8100_771nm.csv", sep=",")
#osif_771 = osif_771_r.set_index(pd.to_datetime(osif_771_r['time']))
#osif_771 = osif_771.drop(columns=['time'])

osif_757_r = pd.read_csv("/windata/DATA/remote/satellite/OCO2/OSIF_8100_757nm.csv", sep=",")
osif_757 = osif_757_r.set_index(pd.to_datetime(osif_757_r['time']))
osif_757 = osif_757.drop(columns=['time'])
osif_757_m =osif_757.resample('M').mean()
osif_757_w =osif_757.resample('W').mean()
osif_757.columns = ['SIF']

sif_joint = pd.concat([osif_757[:datetime(2018,7,1)],tsif[datetime(2018,7,1):]], axis=0)


"read in EDO - fAPAR data"
fAPAR = pd.read_csv("/windata/DATA/obs_point/land/EDO/fAPAR.16_48.1990to2021.20211217133422.txt", delimiter="|",skiprows=2,header=0)

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
MAM18_s = datetime(2018, 3, 1, 00, 00)
MAM18_e = datetime(2018, 5, 31, 00, 00)
MAM20_s = datetime(2020, 3, 1, 00, 00)
MAM20_e = datetime(2020, 5, 31, 00, 00)
JJA19_s = datetime(2019, 6, 1, 00, 00)
JJA19_e = datetime(2019, 8, 31, 00, 00)
JJA20_s = datetime(2020, 6, 1, 00, 00)
JJA20_e = datetime(2020, 8, 31, 00, 00)

start = MAM20_s
end = datetime(2020, 6, 1, 00, 00)

start2 = datetime(2020, 4, 15, 00, 00)
end2 = datetime(2020, 6, 1, 00, 00)
start3 = datetime(2018, 4, 15, 00, 00)


'''
Plotting
'''
"""
#print(len((BOKUMetData_dailysum["PC"]*0.1)[start:end]))
#print(len(tsif[start:end]))
int(len(tsif[start:end]))

fig = plt.figure()
plt.suptitle(f"OBS {start2} - {end2}")
ax1 = fig.add_subplot(411)
#ax1 = fig.add_subplot(211)
x1 = plt.gca()
ax2 = ax1.twinx()
#ax2.plot(nox_1990_2020_da_w['AT9STEF'][start:end]*3,linewidth="1", color='blue', label="NOx*3", linestyle="solid") # label="O3,mda8"
#ax2.plot(nox_1990_2020_da_w['AT9STEF'][start:end].index,nox_1990_2020_da_w['AT9STEF'][datetime(2018, 3, 1):datetime(2018, 6, 7)].values*3, linewidth="1", color='blue', linestyle=":") # label="O3,mda8"
ax2.plot(o3_1990_2020_mda8['AT9STEF'][start2:end2],linewidth="0.3", color='violet', linestyle="solid", label="O3") #mda8
#ax2.axvline(x=datetime(2020,5,10))
#ax2.plot(o3_1990_2020_mda8_w['AT9STEF'][start2:end2],linewidth="1", color='violet', linestyle="solid",label="O3") #label="O3,mda8,w",
#ax2.plot(o3_1990_2020_mda8_w['AT9STEF'][start2:end2].index, o3_1990_2020_mda8_w['AT9STEF'][start3:datetime(2018, 6, 1)].values,linewidth="1", color='violet', linestyle=":")
ax1.plot(BOKUMetData_dailysum["GR"][start2:end2]/1000, linewidth="0.1", color='orange',label="GR") #sum
#ax1.plot(BOKUMetData_weekly["GR"][start2:end2], linewidth="1", color='orange', label="GR") #label="GR,sum,w"
#ax1.plot(BOKUMetData_weekly["GR"][start2:end2].index, BOKUMetData_weekly["GR"][start3:datetime(2018, 6, 1)].values, linewidth="1", color='orange', linestyle=":")
ax1.set_xlim(start2,end2)
ax1.set_ylabel("[kWh/m²]", size="medium")
ax2.set_ylabel("[μg/m³]", size="medium")  #\mu
ax1.grid()
ax1.set_xticks([])
ax1.legend(loc='upper left')
ax2.legend(loc='lower left')

ax1 = fig.add_subplot(412)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(sif_joint[start2:end2].index, tsif[start2:end2], linewidth="0.5", color='violet', label="SIF")  #, d", linestyle="", marker=".")
#ax1.plot(sif_joint[start2:end2].index, sif_joint[start3:datetime(2018, 6, 1)].values, linewidth="0.5", color='red', linestyle=":")#, label="SIF, d", linestyle="", marker=".")
ax1.plot(tsif_w,color='violet')#, label="SIF") #label="SIF_w"
#ax1.plot(tsif_w[start2:datetime(2020, 6, 1)].index, osif_757_w[start3:datetime(2018, 6, 1)].values,color='red',label="OCO-2 SIF",linestyle=":")
ax1.set_ylabel("[mW/m2/sr/nm]", size="medium")
ax2.plot(fAPAR[start2:datetime(2020, 6, 1)],color='green', label="fAPARa")#label="fAPAR anomaly"
ax2.plot(fAPAR[start2:datetime(2020, 6, 1)].index, fAPAR[start3:datetime(2018, 6, 1)].values,color='green', linestyle=":")
ax2.set_ylabel("[-]", size="medium")
#ax2.axvline(x=datetime(2020,5,10))
ax1.grid()
ax1.set_xticks([])
ax1.set_xlim(start2,end2)
ax1.legend(loc='upper left')
ax2.legend(loc='lower left')

ax1 = fig.add_subplot(413)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(vwc['RSS_sub_wWheat'][start2:end2],linewidth="1", color='orange', linestyle="solid", label="RSS_w") #label="RSS_sub_w",
#ax1.plot(vwc['RSS_sub_wWheat'][start2:end2].index,vwc['RSS_sub_wWheat'][start3:datetime(2018, 6, 1)].values,linewidth="1", color='orange', linestyle=":") #label="RSS_sub_w",
#ax1.plot(vwc['RSS_sub_grass'][start2:end2],linewidth="1", color='green', linestyle="solid", label="RSS_g") #label="RSS_sub_g"
#ax1.plot(vwc['RSS_sub_grass'][start2:end2].index,vwc['RSS_sub_grass'][start3:datetime(2018, 6, 1)].values,linewidth="1", color='green', linestyle=":")
ax2.step(BOKUMetData_dailysum[start2:end2].index,(BOKUMetData_dailysum["PC"]*0.1)[start2:end2], linewidth="0.3", color='blue', label="PR") #{'pre', 'post', 'mid'} label="PR,sum"
#ax2.step(BOKUMetData_dailysum[start2:end2].index,(BOKUMetData_dailysum["PC"]*0.1)[datetime(2018, 4, 15):datetime(2018, 6, 1)].values, linewidth="0.3", color='blue', linestyle=":") #{'pre', 'post', 'mid'}  label="PR,sum",
ax2.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
ax2.set_ylabel("[mm]", size="medium")
ax1.set_ylabel("[-]", size="medium")
#ax2.axvline(x=datetime(2020,5,10))
ax1.grid()
ax1.set_xlim(start2,end2)
ax1.legend(loc='upper left',fontsize="small")
ax2.legend(loc='lower left',fontsize="small")
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

ax1 = fig.add_subplot(414)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
ax2.plot(vpd_dmax[start2:end2], linewidth="0.3", color='green', label="VDP") #vpd,dmax")
#ax2.plot(vpd_dmax_w[start2:end2], linewidth="1", color='green', label="VPD")#, label="vpd,dmax,w")
#ax2.plot(vpd_dmax_w[start2:end2].index, vpd_dmax_w[start3:datetime(2018, 6, 1)].values, linewidth="1", color='green', linestyle=":")
ax1.plot(hcho_d[start2:end2], linewidth="0.3", color='black', label="HCHO") #,dmax", linestyle="solid")
ax1.plot(hcho_w[start2:end2], linewidth="1", color='black')#,label="HCHO")#, label="HCHO,dmax,w", linestyle="solid")
#ax1.plot(hcho_w[start2:end2].index,hcho_w[start3:datetime(2018, 6, 1)].values, linewidth="1", color='black', linestyle=":")
ax1.set_xlim(start2,end2)
ax2.axvline(x=datetime(2020,5,10))
ax1.grid()
ax2.set_ylabel("[kPa]", size="medium")
ax1.set_ylabel("[ppb]", size="medium")
ax1.set_xticks([])
ax1.legend(loc='upper left')
ax2.legend(loc='lower left')

plt.show()
"""


fig = plt.figure()
plt.suptitle(f"OBS {start} - {end}")
ax1 = fig.add_subplot(511)
ax1.set_title('(a)', loc='left', size='medium')#, color='green')
x1 = plt.gca()
ax2 = ax1.twinx()
ax2.plot(o3_1990_2020_mda8_w['AT9STEF'][start:end],linewidth="1", color='violet', linestyle="solid",label="O3_dry") #label="O3,mda8,w",
ax2.plot(o3_1990_2020_mda8_w['AT9STEF'][start:end].index, o3_1990_2020_mda8_w['AT9STEF'][datetime(2018, 3, 1):datetime(2018, 6, 7)].values,linewidth="1", color='violet', linestyle=":", label="O3_reg")
#ax1.plot(BOKUMetData_dailysum["GR"][start:end], linewidth="0.1", color='orange')  #label="GR,sum"
ax1.plot(BOKUMetData_weekly["GR"][start:end]/1000, linewidth="1", color='orange', label="GR_dry") #label="GR,sum,w"
ax1.plot(BOKUMetData_weekly["GR"][start:end].index, (BOKUMetData_weekly["GR"][datetime(2018, 3, 1):datetime(2018, 6, 7)].values)/1000, linewidth="1", color='orange', linestyle=":", label="GR_reg")
ax1.set_xlim(start,end)
ax1.set_ylabel("[kWh/m²]", size="medium")
ax2.set_ylabel("[μg/m³]", size="medium")
ax1.grid()
ax1.set_xticks([])
ax1.legend(loc='upper left')
ax2.legend(loc='lower left')

ax1 = fig.add_subplot(512)
ax1.set_title('(b)', loc='left', size='medium')#, color='green')
ax1 = plt.gca()
ax2 = ax1.twinx()
#ax1.step(sif_joint[start:end].index, tsif[start:end], linewidth="0.5", color='violet')#, label="SIF, d", linestyle="", marker=".")
#ax1.step(sif_joint[start:end].index, sif_joint[datetime(2018, 3, 1):datetime(2018, 6, 1)].values, linewidth="0.5", color='red', linestyle=":")#, label="SIF, d", linestyle="", marker=".")
ax1.plot(tsif_w,color='violet', label="SIF_dry (TROP)") #label="SIF_w"
ax1.plot(tsif_w[start:datetime(2020, 6, 1)].index, osif_757_w[datetime(2018, 3, 1):datetime(2018, 6, 7)].values,color='red',label="SIF_reg (OCO)",linestyle=":")
ax1.set_ylabel("[mW/m2/sr/nm]", size="medium")
ax2.plot(fAPAR[start:datetime(2020, 6, 1)],color='green', label="fAPARa_dry")#label="fAPAR anomaly"
ax2.plot(fAPAR[start:datetime(2020, 6, 1)].index, fAPAR[datetime(2018, 3, 1):datetime(2018, 6, 7)].values,color='green', linestyle=":", label="fAPARa_reg")
ax2.set_ylabel("[-]", size="medium")
ax1.grid()
ax1.set_xticks([])
ax1.set_xlim(start,end)
ax1.legend(loc='upper left')
ax2.legend(loc='lower left')

ax1 = fig.add_subplot(513)
ax1.set_title('(c)', loc='left', size='medium')#, color='green')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(vwc['RSS_sub_wWheat'][start:end],linewidth="1", color='orange', linestyle="solid", label="RSS_w_dry")
ax1.plot(vwc['RSS_sub_wWheat'][start:end].index,vwc['RSS_sub_wWheat'][datetime(2018, 3, 1):datetime(2018, 6, 1)].values,linewidth="1", color='orange', linestyle=":", label="RSS_sub_w_reg")
ax1.plot(vwc['RSS_sub_grass'][start:end],linewidth="1", color='green', linestyle="solid", label="RSS_g_dry") #label="RSS_sub_g"
ax1.plot(vwc['RSS_sub_grass'][start:end].index,vwc['RSS_sub_grass'][datetime(2018, 3, 1):datetime(2018, 6, 1)].values,linewidth="1", color='green', linestyle=":", label="RSS_g_reg")
ax2.step(BOKUMetData_dailysum[start:end].index,(BOKUMetData_dailysum["PC"]*0.1)[start:end], linewidth="0.3", color='blue', label="PR_dry") #{'pre', 'post', 'mid'} label="PR,sum"
ax2.step(BOKUMetData_dailysum[start:end].index,(BOKUMetData_dailysum["PC"]*0.1)[datetime(2018, 3, 1):datetime(2018, 6, 1)].values, linewidth="0.3", color='blue', linestyle=":", label="PR_reg") #{'pre', 'post', 'mid'}  label="PR,sum",
ax2.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
ax2.set_ylabel("[mm]", size="medium")
ax1.set_ylabel("[-]", size="medium")
ax1.set_xticks([])
ax1.grid()
ax1.set_xlim(start,end)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.grid()

ax1 = fig.add_subplot(514)
ax1.set_title('(d)', loc='left', size='medium')#, color='green')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
#ax2.plot(vpd_dmax[start:end], linewidth="0.1", color='green')#, label="vpd,dmax")
ax2.plot(vpd_dmax_w[start:end], linewidth="1", color='green', label="VPD_dry")#, label="vpd,dmax,w")
#ax2.plot(vpd_dmax[start:end].index, vpd_dmax[datetime(2018, 3, 1):datetime(2018, 6, 1)].values, linewidth="0.3", color='green', linestyle=":")
ax2.plot(vpd_dmax_w[start:end].index, vpd_dmax_w[datetime(2018, 3, 1):datetime(2018, 6, 7)].values, linewidth="1", color='green', linestyle=":", label="VPD_reg")
#ax1.plot(hcho_d[start:end], linewidth="0.1", color='black') #, label="HCHO,dmax", linestyle="solid")
ax1.plot(hcho_w[start:end], linewidth="1", color='black',label="HCHO_dry") #, label="HCHO,dmax,w", linestyle="solid")
#ax1.plot(hcho_d[start:end].index,hcho_d[MAM18_s: datetime(2018, 6, 1)].values, linewidth="0.3", color='black', linestyle=":")
ax1.plot(hcho_w[start:end].index,hcho_w[datetime(2018, 3, 1):datetime(2018, 6, 7)].values, linewidth="1", color='black', linestyle=":", label="HCHO_reg")
ax1.set_xlim(start,end)
ax1.set_xticks([])
ax2.set_ylabel("[kPa]", size="medium")
ax1.set_ylabel("[ppb]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='lower left')
ax1.grid()

ax1 = fig.add_subplot(515)
ax1.set_title('(e)', loc='left', size='medium')#, color='green')
ax1 = plt.gca()
ax2 = ax1.twinx()
#ax1.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
#ax2.plot(vpd_dmax[JJA19_s:JJA19_e], linewidth="0.3", color='green', label="VDP") #vpd,dmax")
#ax2.plot((BOKUMetData_dailymax["AT"][start:end]), linewidth="0.3", color='red')#, label="AT") #label="GR,sum,w"
ax2.plot((BOKUMetData_weekly["AT"][start:end]), linewidth="1", color='red', label="Tair_dry") #label="GR,sum,w"
#ax2.plot(BOKUMetData_dailysum["AT"][start:end].index,BOKUMetData_dailymax["AT"][MAM18_s:datetime(2018, 6, 1)].values, linewidth="0.3", color='red', linestyle=":")
ax2.plot(BOKUMetData_weekly["AT"][start:end].index,BOKUMetData_weekly["AT"][MAM18_s:datetime(2018, 6, 7)].values, linewidth="1", color='red', linestyle=":", label="Tair_reg")
#ax1.plot(hcho_d[start:end], linewidth="0.3", color='black')#, label="HCHO") #,dmax", linestyle="solid")
ax1.plot(hcho_w[start:end], linewidth="1", color='black',label="HCHO_dry")#, label="HCHO,dmax,w", linestyle="solid")
#ax1.plot(hcho_d[start:end].index,hcho_d[MAM18_s: datetime(2018, 6, 1)].values, linewidth="0.3", color='black', linestyle=":")
ax1.plot(hcho_w[start:end].index,hcho_w[MAM18_s: datetime(2018, 6, 7)].values, linewidth="1", color='black', linestyle=":",label="HCHO_dry")
ax1.set_xlim(start,end)
#ax2.axvline(x=datetime(2020,5,10))
ax2.set_ylabel("[°C]", size="medium")
ax1.set_ylabel("[ppb]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='lower left')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1.grid()
plt.show()

