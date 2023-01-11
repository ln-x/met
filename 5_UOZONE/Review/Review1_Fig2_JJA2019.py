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
from met.library import ReadinVindobona_Filter_fullperiod
from met.library import ReadinPROBAV_LAI_300m
#TODO: include fAPARa and AT?

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
no2_2020_mda1 = no2_2020_mda1*ugm3toppb_no2
no2_2020_da = no2_2020_mda1.resample('D').mean()
no_2020_mda1 = pd.read_csv(pathbase2 + "AT_NO_2020.csv")
no_2020_mda1 = no_2020_mda1.set_index(pd.to_datetime(no_2020_mda1['date']))
no_2020_mda1 = no_2020_mda1.drop(columns=['date'])
no_2020_mda1 = no_2020_mda1*ugm3toppb_no
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
tsif_r = pd.read_csv("/windata/DATA/remote/satellite/TROPOMI/TSIF_743_LAT48_196613_LON16_382294.csv", sep=",")
#tsif_r = pd.read_csv("/windata/DATA/remote/satellite/TROPOMI/TSIF_743_LAT48_28_LON16_23.csv", sep=",")
tsif = tsif_r.set_index(pd.to_datetime(tsif_r['time']))
tsif = tsif.drop(columns=['time'])
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

'''READ IN CEILOMETER DATA'''
file_pbl = "/windata/DATA/obs_point/met/ZAMG/Ceilometer/MH_Wien_Hohe_Warte_20170101_20201231.csv"
pbl = pd.read_csv(file_pbl,skiprows=2, parse_dates={'datetime':[0,1]})
pbl.columns = ['datetime','PBL']  #UTC
pbl = pbl.set_index(pbl['datetime'])
pbl = pbl.drop(columns=['datetime'])
pbl = pbl.resample('D').max()
pbl_w_km = pbl.resample('W').mean()/1000
#pbl_sigma = pbl.std()
pbl_sigma = 0.57383519

'''READ IN PROBAV_LAI300m'''
LAI_df = ReadinPROBAV_LAI_300m.LAI()

'''TIMESLICES'''
start = datetime(2018, 1, 1, 00, 00)
emd = datetime(2020, 12, 31, 00, 00)
MAM18_s = datetime(2018, 3, 1, 00, 00)
MAM18_e = datetime(2018, 5, 31, 00, 00)
MAM19_s = datetime(2019, 3, 1, 00, 00)
MAM19_e = datetime(2019, 5, 31, 00, 00)
MAM20_s = datetime(2020, 3, 1, 00, 00)
MAM20_e = datetime(2020, 5, 31, 00, 00)
JJA19_s = datetime(2019, 6, 1, 00, 00)
JJA19_e = datetime(2019, 8, 31, 00, 00)
JJA20_s = datetime(2020, 6, 1, 00, 00)
JJA20_e = datetime(2020, 8, 31, 00, 00)
"""
print("fAPAR mean")
print("MAM18:", fAPAR[MAM18_s:MAM18_e].mean())
print("MAM19:", fAPAR[MAM19_s:MAM19_e].mean())
print("MAM20:", fAPAR[MAM20_s:MAM20_e].mean())
print("JJA20:", fAPAR[JJA20_s:JJA20_e].mean())
print("JJA19:", fAPAR[JJA19_s:JJA19_e].mean())

print("May18:", fAPAR[datetime(2018, 5, 1, 00, 00):MAM18_e].mean())
print("May19:", fAPAR[datetime(2019, 5, 1, 00, 00):MAM18_e].mean())
print("May20:", fAPAR[datetime(2020, 5, 1, 00, 00):MAM20_e].mean())
print("Aug20:", fAPAR[datetime(2020, 8, 1, 00, 00):JJA20_e].mean())
print("Aug19:", fAPAR[datetime(2019, 8, 1, 00, 00):JJA19_e].mean())


print("LAI mean")
print("MAM18:", LAI_df[MAM18_s:MAM18_e].mean())
print("MAM19:", LAI_df[MAM19_s:MAM19_e].mean())
print("MAM20:", LAI_df[MAM20_s:MAM20_e].mean())
print("JJA20:", LAI_df[JJA20_s:JJA20_e].mean())
print("JJA19:", LAI_df[JJA19_s:JJA19_e].mean())

print("Mar18:", LAI_df[datetime(2018, 3, 1, 00, 00):datetime(2018, 3, 31, 00, 00)].mean())
print("Mar19:", LAI_df[datetime(2019, 3, 1, 00, 00):datetime(2019, 3, 31, 00, 00)].mean())
print("Mar20:", LAI_df[datetime(2020, 3, 1, 00, 00):datetime(2020, 3, 31, 00, 00)].mean())

print("Apr18:", LAI_df[datetime(2018, 4, 1, 00, 00):datetime(2018, 4, 30, 00, 00)].mean())
print("Apr20:", LAI_df[datetime(2020, 4, 1, 00, 00):datetime(2020, 4, 30, 00, 00)].mean())

print("May18:", LAI_df[datetime(2018, 5, 1, 00, 00):MAM18_e].mean())
print("May19:", LAI_df[datetime(2019, 5, 1, 00, 00):MAM18_e].mean())
print("May20:", LAI_df[datetime(2020, 5, 1, 00, 00):MAM20_e].mean())
print("Aug20:", LAI_df[datetime(2020, 8, 1, 00, 00):JJA20_e].mean())
print("Aug19:", LAI_df[datetime(2019, 8, 1, 00, 00):JJA19_e].mean())
#exit()
"""

'''
Plotting
'''
start = datetime(2019, 6, 1)
end = datetime(2019, 8, 31)

hcho_sigma = hcho_d.std()
vpd_sigma = vpd_dmax.std()
ws_sigma = BOKUMetData_weekly["WS"][start:end].std()
gr = BOKUMetData_weekly["GR"][start:end]/1000
gr_sigma = gr.std()
o3_sigma = o3_1990_2020_mda8_w['AT9STEF'][start:end].std()
osif_sigma = osif_757.std()
tsif_sigma = tsif.std()
#print(tsif_sigma.values, osif_sigma)
tsif_sigma = 0.50563181
osif_sigma = 0.674449


fig = plt.figure()
plt.suptitle(f"OBS {start} - {end}")
ax1 = fig.add_subplot(511)
ax1.set_title('(a)', loc='right', size='medium')#, color='green')
ax2 = ax1.twinx()
ax1.plot(gr, linewidth="1", color='orange')#, label="GR sum BOKUR")
ax2.plot(o3_1990_2020_mda8_w['AT9STEF'][start:end],linewidth="1", color='violet', linestyle="solid") #label="o3 OBS mda8",
ax1.fill_between(gr.index, gr.values+gr_sigma,gr.values-gr_sigma, facecolor='orange', alpha=0.1)
ax2.fill_between(o3_1990_2020_mda8_w['AT9STEF'][start:end].index, o3_1990_2020_mda8_w['AT9STEF'][start:end].values+o3_sigma,o3_1990_2020_mda8_w['AT9STEF'][start:end].values-o3_sigma, facecolor='violet', alpha=0.1)
ax1.set_xlim(start,end)
ax1.set_ylabel("GR[kWh/m²]", size="medium", color="orange")
ax2.set_ylabel("O3[μg/m³]", size="medium", color="violet")
ax1.grid()
#ax1.set_xticks([])
ax1.axvspan(MAM18_s, MAM18_e, color='orange', alpha=0.3)
ax1.axvspan(MAM20_s, MAM20_e, color='orange', alpha=0.3)
ax1.axvspan(JJA19_s, JJA19_e, color='red', alpha=0.3)
ax1.axvspan(JJA20_s, JJA20_e, color='red', alpha=0.3)

ax1 = fig.add_subplot(512)
ax1.set_title('(b)', loc='right', size='medium')#, color='green')
ax1 = plt.gca()
#ax2 = ax1.twinx()
ax3 = ax1.twinx()
# Offset the right spine of twin2.  The ticks and label have already been
# placed on the right by twinx above.
#ax2.spines.right.set_position(("axes", 2.0))
#ax3.spines.right.set_position(("axes", 1.15))
ax1.plot(tsif_w,color='violet', label="TROP")
ax1.plot(osif_757_w,color='red',label="OCO-2")
ax1.fill_between(tsif_w[start:end].index, tsif_w[start:end].values.flatten()+tsif_sigma,tsif_w[start:end].values.flatten()-tsif_sigma, facecolor='violet', alpha=0.1)
ax1.fill_between(osif_757_w[start:end].index, osif_757_w[start:end].values.flatten()+osif_sigma,osif_757_w[start:end].values.flatten()-osif_sigma, facecolor='red', alpha=0.1)
ax1.set_ylabel("SIF[mW/m2/sr/nm]", size="medium")
#ax1.plot(fAPAR,color='blue', label="fAPAR anomaly")
ax3.plot(LAI_df[start:end].index, LAI_df[start:end].LAI, color="green")
#ax1.plot(fAPAR[start:end].index, fAPAR[start:end].values/2, color="lightblue", label="fAPARa/2 [-]")
ax3.set_ylabel("LAI[-]", color="green")
#ax2.set_ylabel("fAPARa[-]", color="blue")
ax1.axvspan(MAM18_s, MAM18_e, color='orange', alpha=0.3)
ax1.axvspan(MAM20_s, MAM20_e, color='orange', alpha=0.3)
ax1.axvspan(JJA19_s, JJA19_e, color='red', alpha=0.3)
ax1.axvspan(JJA20_s, JJA20_e, color='red', alpha=0.3)
#ax1.set_xlabel("days")
#ax1.set_ylabel("[degree]", size="medium")
#ax1.set_ylim(0, 3500)
#ax2.set_ylabel("[ppb]", size="medium")
#ax1.set_ylabel("LAI [m2 m-2]", size="medium") #TODO convert degree to m2 m-2
#ax2.set_ylabel("dry deposition velocity [cm s-1]", size="medium")
ax1.grid()
ax2.grid(False)
ax3.grid(False)
#ax1.set_xticks([])
ax1.set_xlim(start,end)
ax1.legend(loc='upper left')

ax1 = fig.add_subplot(513)
ax1.set_title('(c)', loc='right', size='medium')#, color='green')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(vwc['RSS_sub_wWheat'][start:end],linewidth="1", color='brown', label="wwheat", linestyle="solid") #label="rss 40-100 cm ARIS wWheat"
ax1.plot(vwc['RSS_sub_grass'][start:end],linewidth="1", color='purple', label="grass", linestyle="solid")  #label="rss 40-100 cm ARIS grass"
ax2.plot((BOKUMetData_dailysum["PC"]*0.1)[start:end], linewidth="1", color='blue')#, label="prec BOKUR OBS")
ax2.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
ax2.set_ylabel("PR[mm]", size="medium", color="blue")
ax1.set_ylabel("RSS[-]", size="medium")
ax1.set_xlim(start,end)
ax1.legend(loc='upper left',fontsize="small")
ax1.grid()
#ax1.set_xticks([])
#ax2.set_xticks([])
ax1.axvspan(MAM18_s, MAM18_e, color='orange', alpha=0.3)
ax1.axvspan(MAM20_s, MAM20_e, color='orange', alpha=0.3)
ax1.axvspan(JJA19_s, JJA19_e, color='red', alpha=0.3)
ax1.axvspan(JJA20_s, JJA20_e, color='red', alpha=0.3)

ax1 = fig.add_subplot(514)
ax1.set_title('(d)', loc='right', size='medium')#, color='green')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
ax2.plot(vpd_dmax_w[start:end], linewidth="1", color='green')#, label="vpd dmax")
ax2.fill_between(vpd_dmax_w[start:end].index, vpd_dmax_w[start:end].values+vpd_sigma,vpd_dmax_w[start:end].values-vpd_sigma, facecolor='black', alpha=0.1)
ax1.plot(hcho_dmax[start:end], linewidth="1", color='black', linestyle="solid") #274 = Julian Day 30.Sept2020 #label="hcho D OBS d",
ax1.fill_between(hcho_w[start:end].index, hcho_w[start:end].values+hcho_sigma,hcho_w[start:end].values-hcho_sigma, facecolor='black', alpha=0.1)
ax1.set_xlim(start,end)
ax2.set_ylabel("VDP[kPa]", size="medium", color="green")
ax1.set_ylabel("HCHO[ppb]", size="medium")
ax1.grid()
ax1.axvspan(MAM18_s, MAM18_e, color='orange', alpha=0.3)
ax1.axvspan(MAM20_s, MAM20_e, color='orange', alpha=0.3)
ax1.axvspan(JJA19_s, JJA19_e, color='red', alpha=0.3)
ax1.axvspan(JJA20_s, JJA20_e, color='red', alpha=0.3)

ax1 = fig.add_subplot(515)
ax1.set_title('(e)', loc='right', size='medium')#, color='green')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(BOKUMetData_dailysum["WS"][start:end], linewidth="1", color='blue') #label="GR,sum,w"
ax1.fill_between(BOKUMetData_weekly["WS"][start:end].index, BOKUMetData_weekly["WS"][start:end]+ws_sigma,BOKUMetData_weekly["WS"][start:end]- ws_sigma, facecolor='blue', alpha=0.1)
ax2.plot(BOKUMetData_dailysum["WD"][start:end], linewidth="1", color='grey') #label="GR,sum,w"
##ax2.plot(pbl_w_km[start:end], linewidth="1", color='grey', linestyle="solid", label="PBL_MAM18")
##ax2.fill_between(pbl_w_km[start:end].index, pbl_w_km[start:end].values.flatten()+pbl_sigma,pbl_w_km[start:end].values.flatten()-pbl_sigma, facecolor='grey', alpha=0.1)
ax1.set_xlim(start,end)
#ax2.axvline(x=datetime(2020,5,10))
ax1.set_ylabel("WS[m s-1]", size="medium", color="blue")
##ax2.set_ylabel("PBL[km]", size="medium", color="grey")
#ax1.legend(loc='upper left')
#ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1.grid()
ax1.axvspan(MAM18_s, MAM18_e, color='orange', alpha=0.3)
ax1.axvspan(MAM20_s, MAM20_e, color='orange', alpha=0.3)
ax1.axvspan(JJA19_s, JJA19_e, color='red', alpha=0.3)
ax1.axvspan(JJA20_s, JJA20_e, color='red', alpha=0.3)

plt.show()

