# -*- coding: utf-8 -*-
__author__ = 'lnx'
#version history: cleaned version 20211105 building on:
# 1_VAL_SM_VOC_20192020
# 1_VAL_SM_VOC_20192020_onlycorrelations_inklSIF_inklO3.py
from sklearn import linear_model
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from scipy import stats
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVindobona_Filter_fullperiod

#pd.set_option("display.max_rows", None, "display.max_columns", None) #TODO cool option to turn on and off weather to see all data or only start+end

"read in VINDOBONA"

foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
foldername_K = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_KQ"

hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))
#hchoK_d, hchoK_dmax, hchoK_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_K,"K", begin= datetime.datetime(2020, 1, 1, 0, 0, 0)))

'''READ IN EEA air pollution data'''
pathbase2 = "/windata/DATA/obs_point/chem/EEA/"
nox_1990_2019_da = pd.read_csv(pathbase2 + "nox_da_1990-2019_AT_ppb.csv")
nox_1990_2019_da = nox_1990_2019_da.set_index(pd.to_datetime(nox_1990_2019_da['date'])) #utc=True
nox_1990_2019_da = nox_1990_2019_da.drop(columns=['date'])
no2_2020_mda1 = pd.read_csv(pathbase2 + "AT_NO2_2020.csv")
no2_2020_mda1 = no2_2020_mda1.set_index(pd.to_datetime(no2_2020_mda1['date']))
no2_2020_da = no2_2020_mda1.resample('D').mean()  #offset='-1h', origin="1990-01-01"
no_2020_mda1 = pd.read_csv(pathbase2 + "AT_NO_2020.csv")
no_2020_mda1 = no_2020_mda1.set_index(pd.to_datetime(no_2020_mda1['date']))
no_2020_da = no_2020_mda1.resample('D').mean()
nox_2020_da = no_2020_da.add(no2_2020_da)
nox_1990_2020_da = pd.concat([nox_1990_2019_da, nox_2020_da], axis=0)

o3_1990_2019_mda1 = pd.read_csv(pathbase2 + "o3_mda1_1990-2019_AT_mug.csv")
o3_1990_2019_mda1 = o3_1990_2019_mda1.set_index(pd.to_datetime(o3_1990_2019_mda1['date']))
o3_1990_2019_mda1 = o3_1990_2019_mda1.drop(columns=['date'])
o3_1990_2019_mda8 = pd.read_csv(pathbase2 + "o3_mda8_1990-2019_AT_mug.csv")
o3_1990_2019_mda8 = o3_1990_2019_mda8.set_index(pd.to_datetime(o3_1990_2019_mda8['date']))
o3_1990_2019_mda8 = o3_1990_2019_mda8.drop(columns=['date'])
o3_2020_mda1 = pd.read_csv(pathbase2 + "AT_O3_2020.csv")
o3_2020_mda1 = o3_2020_mda1.set_index(pd.to_datetime(o3_2020_mda1['date']))
o3_2020_mda1 = o3_2020_mda1.drop(columns=['date'])
o3_2020_mda8_8h = o3_2020_mda1.resample('8H', label='right').mean()
o3_2020_mda8 = o3_2020_mda8_8h.resample('D').max()   #TODO: decide about max or mean!

#o3_1990_2020_mda1 = pd.concat([o3_1990_2019_mda1, o3_2020_mda1], axis=0)
#o3_1990_2019_mda1 = o3_1990_2019_mda1**ugm3toppb_o3 #MUG->PPB
#o3_1990_2020_da = o3_1990_2020_mda8.resample('D').mean()
#o3_1990_2020_m = o3_1990_2020_mda8.resample('M').mean()
o3_1990_2020_mda8 = pd.concat([o3_1990_2019_mda8, o3_2020_mda8], axis=0)
o3_1990_2020_mda8 = o3_1990_2020_mda8#*ugm3toppb_o3 #MUG->PPB
o3_1990_2020_da = o3_1990_2020_mda8.resample('D').mean()
o3_1990_2020_m = o3_1990_2020_mda8.resample('M').mean()

'''READ IN BOKU Metdata'''
BOKUMetData = met.library.BOKUMet_Data.BOKUMet() #10min values
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean, 'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean, 'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailymax = BOKUMetData_hourlymean.resample('D').agg({'DT': np.max, 'AT': np.max, 'RH': np.max, 'GR': np.max, 'WS': np.max,'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})

vp_sat = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3))  #kPa sh. Dingman
vp_air = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3)) * (BOKUMetData_hourlymean["RH"]/100)
vpd = vp_sat - vp_air
#print(vp_sat,vp_air, vpd)
#vpd.plot()
#plt.show()
vpd_d = vpd.resample('D').mean()
vpd_dmax = vpd.resample('D').max()

BOKUMetData_dailysum['JD'] = (BOKUMetData_dailysum.index) #JULIAN DAY
f = lambda x: datestdtojd(str(x)[:-9])
BOKUMetData_dailysum['JD'] = BOKUMetData_dailysum['JD'].apply(f)

#FILTER - GLOBAL RADIATION
juliandays = range(365)
thres_glob = []
#APOLIS in kWh/m2 (Tagessumme Globalstrahlung) ! thres_glob = ((1.25e-12)*(x**5)+ (7.38e-9)*(x**4) - (5.365e-6)*(x**3) + 0.000926*(x**2) - 0.00036*x + 1.08)*0.9
for x in juliandays:
    thres_glob.append(((1.25e-12)*(x**5)+ (7.38e-9)*(x**4) - (5.365e-6)*(x**3) + 0.000926*(x**2) - 0.00036*x + 1.08)*0.9*1000)  #in Wh/m2 Tagessumme

f2 = lambda x: (((1.25e-12)*(x**5)+ (7.38e-9)*(x**4) - (5.365e-6)*(x**3) + 0.000926*(x**2) - 0.00036*x + 1.08)*0.9*1000)
BOKUMetData_dailysum["GRthres"] = BOKUMetData_dailysum['JD'].apply(f2)

isHighGR = BOKUMetData_dailysum["GR"] > BOKUMetData_dailysum["GRthres"]
HighGRdays = BOKUMetData_dailysum[isHighGR]
#print(HighGRdays[datetime(2018,1,1):])

BOKUMetData_monthly = BOKUMetData.resample('M').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

'''READ in SOIL MOISTURE DATA'''
file_sm_2019_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/RUT_10_min.xls"
sm = pd.read_excel(file_sm_2019_rutz, sheet_name="RUT_d", usecols="D,K,L,M,N,O,P", skiprows=11)#, converters={'A': pd.to_datetime})
sm.columns = ['datetime', 'VWC1 min[%]', 'VWC2 min[%]','VWC3 min[%]','VWC1 max[%]', 'VWC2 max[%]','VWC3 max[%]']  #TODO: local time!
sm = sm.set_index(pd.to_datetime(sm['datetime']))
sm = sm.drop(columns=['datetime'])

file_rss_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/2008_2020_Rutzendorf_ARIS_results_sepp.xlsx"
rss = pd.read_excel(file_rss_rutz, sheet_name="RSS_top", usecols="A,B,C,D,E,F", skiprows=11)#, converters={'A': pd.to_datetime})
rss.columns = ['datetime', 'RSS_top_maize', 'RSS_top_sBarley','RSS_top_sugBeet','RSS_top_wWheat', 'RSS_top_grass']  #TODO: local time!
rss = rss.set_index(pd.to_datetime(rss['datetime']))
rss = rss.drop(columns=['datetime'])

rss_sub = pd.read_excel(file_rss_rutz, sheet_name="RSS_sub", usecols="A,B,C,D,E,F", skiprows=11)#, converters={'A': pd.to_datetime})
rss_sub.columns = ['datetime', 'RSS_sub_maize', 'RSS_sub_sBarley','RSS_sub_sugBeet','RSS_sub_wWheat', 'RSS_sub_grass']  #TODO: local time!
rss_sub = rss_sub.set_index(pd.to_datetime(rss_sub['datetime']))
rss_sub = rss_sub.drop(columns=['datetime'])

#RSS climatological mean difference
mean12yr_d = rss_sub.groupby([rss_sub.index.month, rss_sub.index.day]).mean()
mean12yr_d["new_index"] = mean12yr_d.index.map(lambda x:datetime(2000, x[0], x[1]))
mean12yr_d = mean12yr_d.set_index("new_index")
mean12yr_d_noleap = mean12yr_d.drop(pd.date_range('2000-02-29','2000-2-29'), errors='ignore') #remove 29.Feb

rss_sub17_diff_w = rss_sub['RSS_sub_wWheat'][datetime(2017,5,1):datetime(2017,12,31)].sub(mean12yr_d_noleap['RSS_sub_wWheat'][datetime(2000,5,1):].values)
rss_sub18_diff_w = rss_sub['RSS_sub_wWheat'][datetime(2018,1,1):datetime(2018,12,31)].sub(mean12yr_d_noleap['RSS_sub_wWheat'].values)
rss_sub19_diff_w = rss_sub['RSS_sub_wWheat'][datetime(2019,1,1):datetime(2019,12,31)].sub(mean12yr_d_noleap['RSS_sub_wWheat'].values)
rss_sub20_diff_w = rss_sub['RSS_sub_wWheat'][datetime(2020,1,1):datetime(2020,12,31)].sub(mean12yr_d['RSS_sub_wWheat'].values)
rss_sub_diff_w = pd.concat([rss_sub17_diff_w,rss_sub18_diff_w,rss_sub19_diff_w,rss_sub20_diff_w])

#GLIDING MEAN for GR, AT, SM?
N=5 #days
grsum_5daymean = np.convolve(BOKUMetData_dailysum['GR'], np.ones(N)/N, mode='valid')
rss_sub_5daymean = np.convolve(rss_sub['RSS_sub_wWheat'], np.ones(N)/N, mode='valid')
atmax_5daymean = np.convolve(BOKUMetData_dailymax['AT'], np.ones(N)/N, mode='valid')

Runningmean_5d = BOKUMetData_dailysum[4:]
Runningmean_5d.insert(1,'GR5d', grsum_5daymean.tolist()) #TODO A value is trying to be set on a copy of a slice from a DataFrame. Try using .loc[row_indexer,col_indexer] = value instead
Runningmean_5d.insert(1,'AT5d', atmax_5daymean.tolist())
#print(Runningmean_5d['GR5d'])
isWSD = (rss["RSS_top_wWheat"] < 0.5)
#vwc = rss['RSS_top_maize', 'RSS_top_sBarley','RSS_top_sugBeet','RSS_top_wWheat', 'RSS_top_grass']
#Grünland bei Gänserndorf (war das nächstliegende Grünland Pixel zu Rutzendorf)
#LON 652.750 LAT 494.250
grass_fc_top_Layer= 0.402768
grass_fc_sub_Layer= 0.287642
grass_afc_top_Layer= 0.218952
grass_afc_sub_Layer= 0.162540

#Acker bei Rutzendorf
##LON 644.250 LAT 484.250
rutz_fc_top_Layer= 0.380875
rutz_fc_sub_Layer= 0.268583
rutz_afc_top_Layer= 0.222250
rutz_afc_sub_Layer= 0.154833

vwc = rutz_fc_top_Layer - (1-rss)*rutz_afc_top_Layer
vwc_grass = grass_fc_top_Layer - (1-rss)*grass_afc_top_Layer
vwc_sub = rutz_fc_sub_Layer - (1-rss_sub)*rutz_afc_sub_Layer
vwc_sub_grass = grass_fc_sub_Layer - (1-rss_sub)*grass_afc_sub_Layer
vwc_sub.columns = ['VWC_sub_maize', 'VWC_sub_sBarley','VWC_sub_sugBeet','VWC_sub_wWheat', 'VWC_sub_grass']  #TODO: local time!
#print(vwc_sub)

#TSIF_743
tsif_r = pd.read_csv("/windata/DATA/remote/satellite/TROPOMI/TSIF_743_LAT48_28_LON16_23.csv", sep=",")
tsif = tsif_r.set_index(pd.to_datetime(tsif_r['time']))
tsif = tsif.drop(columns=['time'])
tsif.columns = ['SIF']

#osif_771_r = pd.read_csv("/windata/DATA/remote/satellite/OCO/OSIF_8100_771nm.csv", sep=",")
#osif_771 = osif_771_r.set_index(pd.to_datetime(osif_771_r['time']))
#osif_771 = osif_771.drop(columns=['time'])
osif_757_r = pd.read_csv("/windata/DATA/remote/satellite/OCO2/OSIF_8100_757nm.csv", sep=",")
osif_757 = osif_757_r.set_index(pd.to_datetime(osif_757_r['time']))
osif_757 = osif_757.drop(columns=['time'])
osif_757.columns = ['SIF']

sif_join = pd.concat([osif_757[:datetime(2018,5,31)],tsif[datetime(2018,6,1):]], axis=0)

'''READ IN CEILOMETER DATA'''
file_pbl = "/windata/DATA/obs_point/met/ZAMG/Ceilometer/MH_Wien_Hohe_Warte_20170101_20201231.csv"
pbl = pd.read_csv(file_pbl,skiprows=2, parse_dates={'datetime':[0,1]})
pbl.columns = ['datetime','PBL']  #UTC
pbl = pbl.set_index(pbl['datetime'])
pbl = pbl.drop(columns=['datetime'])
pbl = pbl.resample('D').max()
#print(pbl)

'''
Plotting
'''
nox_1990_2020_da = nox_1990_2020_da.resample('D').mean()
o3_1990_2020_da = o3_1990_2020_da.resample('D').mean()


pff_full = pd.concat([hcho_dmax,vpd_dmax, rss_sub["RSS_sub_wWheat"],BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"],HighGRdays["GR"], sif_join,
                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],BOKUMetData_dailysum["WD"],BOKUMetData_dailysum["PC"],pbl["PBL"]], axis=1)
pff_full.columns = ['hcho', 'vpd', 'SM', 'AT', 'GR', 'GRhigh', 'SIF', 'O3','NOx','WD','PC','PBL']
pff_clear = pff_full.dropna(subset=['GRhigh'])
print(pff_clear[datetime(2018,1,1):datetime(2020,12,31)])
pff_clear2 = pff_clear.loc[pff_clear["GR"] >= 4500]
print(pff_clear2[datetime(2018,1,1):datetime(2020,12,31)])
pff_clear2_o3high = pff_clear2.loc[pff_clear2["O3"] > 100]
print(pff_clear2_o3high[datetime(2018,1,1):datetime(2020,12,31)]["O3"])
pff_clear2_o3low = pff_clear2.loc[pff_clear2["O3"] <= 100]
print(pff_clear2_o3low[datetime(2018,1,1):datetime(2020,12,31)]["O3"])
pff_clear2_o3high_NW = pff_clear2_o3high.loc[(pff_clear2_o3high['WD'] >=270) & (pff_clear2_o3high['WD'] <=360)]
pff_clear2_o3high_SE = pff_clear2_o3high.loc[(pff_clear2_o3high['WD'] >=90) & (pff_clear2_o3high['WD'] <=180)]

pff_weekly_rss_clear = pff_clear.resample("W").mean()

def Plot6var(df1, df2, title, ylimit):
    df1 = df1[datetime(2018, 1, 1, 00, 00): datetime(2020, 12, 31, 00, 00)]
    df2 = df2[datetime(2018, 1, 1, 00, 00): datetime(2020, 12, 31, 00, 00)]
    x5 = df1['AT'].values.flatten()
    x5_GR = df1['GR'].values.flatten()/1000
    x5_SM = df1['SM'].values.flatten()
    x5_VPD = df1['vpd'].values.flatten()
    x5_SIF = df1['SIF'].values.flatten()
    x5_NOx = df1['NOx'].values.flatten()
    x5_O3 = df1['O3'].values.flatten()
    x5_PBL = df1['PBL'].values.flatten()
    y5 = df1['hcho'].values.flatten()
    idxAT = np.isfinite(x5) & np.isfinite(y5)
    idxGR = np.isfinite(x5_GR) & np.isfinite(y5)
    idxSIF = np.isfinite(x5_SIF) & np.isfinite(y5)
    idxVPD = np.isfinite(x5_VPD) & np.isfinite(y5)
    idxSM = np.isfinite(x5_SM) & np.isfinite(y5)
    idxNOX = np.isfinite(x5_NOx) & np.isfinite(y5)
    idxO3 = np.isfinite(x5_O3) & np.isfinite(y5)
    idxPBL = np.isfinite(x5_PBL) & np.isfinite(y5)
    m5, b5 = np.polyfit(x5[idxAT], y5[idxAT], 1)
    m5GR, b5GR = np.polyfit(x5_GR[idxGR], y5[idxGR], 1)
    m5SM, b5SM = np.polyfit(x5_SM[idxSM], y5[idxSM], 1)
    m5VPD, b5VPD = np.polyfit(x5_VPD[idxVPD], y5[idxVPD], 1)
    m5SIF, b5SIF = np.polyfit(x5_SIF[idxSIF], y5[idxSIF], 1)
    m5NOx, b5NOx = np.polyfit(x5_NOx[idxNOX], y5[idxNOX], 1)
    m5O3, b5O3 = np.polyfit(x5_O3[idxO3], y5[idxO3], 1)
    m5PBL, b5PBL = np.polyfit(x5_PBL[idxPBL], y5[idxPBL], 1)

    x5_2 = df2['AT'].values.flatten()
    x5_GR_2 = df2['GR'].values.flatten()/1000
    x5_SM_2 = df2['SM'].values.flatten()
    x5_VPD_2 = df2['vpd'].values.flatten()
    x5_SIF_2 = df2['SIF'].values.flatten()
    x5_NOx_2 = df2['NOx'].values.flatten()
    x5_O3_2 = df2['O3'].values.flatten()
    x5_PBL_2 = df2['PBL'].values.flatten()
    y5_2 = df2['hcho'].values.flatten()
    idxAT_2 = np.isfinite(x5_2) & np.isfinite(y5_2)
    idxGR_2 = np.isfinite(x5_GR_2) & np.isfinite(y5_2)
    idxSIF_2 = np.isfinite(x5_SIF_2) & np.isfinite(y5_2)
    idxVPD_2 = np.isfinite(x5_VPD_2) & np.isfinite(y5_2)
    idxSM_2 = np.isfinite(x5_SM_2) & np.isfinite(y5_2)
    idxNOX_2 = np.isfinite(x5_NOx_2) & np.isfinite(y5_2)
    idxO3_2 = np.isfinite(x5_O3_2) & np.isfinite(y5_2)
    idxPBL_2 = np.isfinite(x5_PBL_2) & np.isfinite(y5_2)
    m5_2, b5_2 = np.polyfit(x5_2[idxAT_2], y5_2[idxAT_2], 1)
    m5GR_2, b5GR_2 = np.polyfit(x5_GR_2[idxGR_2], y5_2[idxGR_2], 1)
    m5SM_2, b5SM_2 = np.polyfit(x5_SM_2[idxSM_2], y5_2[idxSM_2], 1)
    m5VPD_2, b5VPD_2 = np.polyfit(x5_VPD_2[idxVPD_2], y5_2[idxVPD_2], 1)
    m5SIF_2, b5SIF_2 = np.polyfit(x5_SIF_2[idxSIF_2], y5_2[idxSIF_2], 1)
    m5NOx_2, b5NOx_2 = np.polyfit(x5_NOx_2[idxNOX_2], y5_2[idxNOX_2], 1)
    m5O3_2, b5O3_2 = np.polyfit(x5_O3_2[idxO3_2], y5_2[idxO3_2], 1)
    m5PBL_2, b5PBL_2 = np.polyfit(x5_PBL_2[idxPBL_2], y5_2[idxPBL_2], 1)

    a = 0
    fig, axs = plt.subplots(2, 3, figsize=(8, 6), dpi=100)
    fig.suptitle(title, fontsize="small")
    axs[0, 0].scatter(x5[a:], y5[a:], color='grey', s=5)
    y_est = m5 * x5 + b5
    axs[0, 0].plot(x5, y_est, color='black')
    axs[0, 0].scatter(x5_2[a:], y5_2[a:], color='salmon', s=5)
    y_est_2 = m5_2 * x5_2 + b5_2
    axs[0, 0].plot(x5_2, y_est_2, color='red')
    # ax0.fill_between(x5, y_est - y_err_AT, y_est + y_err_AT, alpha=0.2)
    axs[0, 0].set_ylabel("HCHO [ppb]", size="small")
    axs[0, 0].set_xlabel("air temp [C°]", size="small")

    axs[0, 1].scatter(x5_GR[a:], y5[a:], color='grey', s=5)
    axs[0, 1].plot(x5_GR, m5GR * x5_GR + b5GR, color='black')
    axs[0, 1].scatter(x5_GR_2[a:], y5_2[a:], color='salmon', s=5)
    axs[0, 1].plot(x5_GR_2, m5GR_2 * x5_GR_2 + b5GR_2, color='red')
    axs[0, 1].set_xlabel(r"GR [$kWhm⁻²$]", size="medium")

    axs[0, 2].scatter(x5_O3[a:], y5[a:], color='grey',s=5)
    axs[0, 2].plot(x5_O3, m5O3 * x5_O3 + b5O3, color='black')
    axs[0, 2].scatter(x5_O3_2[a:], y5_2[a:], color='salmon', s=5)
    axs[0, 2].plot(x5_O3_2, m5O3_2 * x5_O3_2 + b5O3_2, color='red')
    axs[0, 2].set_xlabel("O3 [μg/m³]", size="medium")

    axs[1, 0].scatter(x5_SM[a:], y5[a:], color='grey',s=5)
    axs[1, 0].plot(x5_SM, m5SM * x5_SM + b5SM, color='black')
    axs[1, 0].scatter(x5_SM_2[a:], y5_2[a:], color='salmon', s=5)
    axs[1, 0].plot(x5_SM_2, m5SM_2 * x5_SM_2 + b5SM_2, color='red')
    axs[1, 0].set_xlabel("RSS [-]", size="medium")

    axs[1, 1].scatter(x5_SIF[a:], y5[a:], color='grey',s=5)
    axs[1, 1].plot(x5_SIF, m5SIF * x5_SIF + b5SIF, color='black')
    axs[1, 1].scatter(x5_SIF_2[a:], y5_2[a:], color='salmon', s=5)
    axs[1, 1].plot(x5_SIF_2, m5SIF_2 * x5_SIF_2 + b5SIF_2, color='red')
    axs[1, 1].set_xlabel(r"SIF [mWm⁻²sr⁻¹nm⁻¹]", size="medium")

    axs[1, 2].scatter(x5_VPD[a:], y5[a:],  color='grey',s=5)
    axs[1, 2].plot(x5_VPD, m5VPD * x5_VPD + b5VPD, color='black')
    axs[1, 2].scatter(x5_VPD_2[a:], y5_2[a:], color='salmon', s=5)
    axs[1, 2].plot(x5_VPD_2, m5VPD_2 * x5_VPD_2 + b5VPD_2, color='red')
    axs[1, 2].set_xlabel("VPD [kPa]", size="medium")

    axs[0, 0].set_ylim(0, ylimit)
    axs[0, 1].set_ylim(0, ylimit)
    axs[0, 2].set_ylim(0, ylimit)
    axs[1, 0].set_ylim(0, ylimit)
    axs[1, 1].set_ylim(0, ylimit)
    axs[1, 2].set_ylim(0, ylimit)
    fig.tight_layout()
    #plt.show()
    plt.savefig("/home/heidit/Downloads/" + title + ".jpg")

"""FULL PERIOD"""
"""
title = "full year, no filter"
Plot6var(pff_full, title, ylimit=8)

title = "full year, clear"
Plot6var(pff_clear, title, ylimit=8)

title = "full year,clear+>4.5kWh/day"
Plot6var(pff_clear2, title, ylimit=8)

title = "full year, clear + >4.5kWh/day, > 100ug/m³mda8 daily max"
Plot6var(pff_clear2_o3high, title, ylimit=8)

title = "full year, clear + >4.5kWh/day, <= 100ug/m³mda8 daily max"
Plot6var(pff_clear2_o3low, title, ylimit=8)

title = "full year, clear + >4.5kWh/day, > 100ug/m³mda8 daily max, NW"
Plot6var(pff_clear2_o3high_NW, title, ylimit=8)

title = "full year, clear + >4.5kWh/day, > 100ug/m³mda8 daily max, SE"
Plot6var(pff_clear2_o3high_SE, title, ylimit=8)

pff_20_I = pff_full[datetime(2020, 4, 20, 00, 00):datetime(2020, 5, 10, 00, 00)].resample('D').mean()
pff_20_II = pff_full[datetime(2020, 5, 10, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
title = "dry episode start"
Plot6var(pff_20_I,title, ylimit=8)
title = "dry episode end"
Plot6var(pff_20_II,title, ylimit=8)
"""
pff_M18 = pff_clear[datetime(2018, 4, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pff_M20 = pff_clear[datetime(2020, 4, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pff_A20 = pff_clear[datetime(2020, 7, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pff_A19 = pff_clear[datetime(2019, 7, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
Plot6var(pff_M18,pff_M20,"AprMay, 18 (black), 20 (red), clear", ylimit=8)
Plot6var(pff_A20,pff_A19,"JulAug,  20 (black), 19 (red), clear", ylimit=8)

exit()

pff_NW = pff_full.loc[(pff_full['WD'] >=270) & (pff_full['WD'] <=359)]
pff_SE = pff_full.loc[(pff_full['WD'] >=90) & (pff_full['WD'] <=180)]

#title = "NW"
#Plot6var(pff_NW,title, ylimit=8)
#title = "SE"
#Plot6var(pff_SE,title, ylimit=8)

pff_clear_NW = pff_clear.loc[(pff_clear['WD'] >=270) & (pff_clear['WD'] <=359)]
pff_clear_SE = pff_clear.loc[(pff_clear['WD'] >=90) & (pff_clear['WD'] <=180)]
"""
title = "NW, clear"
Plot6var(pff_clear_NW,title, ylimit=4)

pff_clear_NW_weekly = pff_clear_NW.resample("W").mean()
title = "NW, clear, weekly values"
Plot6var(pff_clear_NW_weekly,title, ylimit=4)
#LinearModel(pff_weekly_rss_clear_NW, droppar)

title = "SE, clear"
Plot6var(pff_clear_SE,title, ylimit=4)

pff_clear_SE_weekly = pff_clear_SE.resample("W").mean()
title = "SE, clear, weekly values"
Plot6var(pff_clear_SE_weekly,title, ylimit=4)

pff_weekly_rss_clear = pff_clear.resample("W").mean()
title = "full year, clear, weekly values, RSS"
Plot6var(pff_weekly_rss_clear, title, ylimit=4)
#LinearModel(pff_weekly_rss_clear, droppar)
"""
pff_NW_MAM_18 = pff_NW[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pff_NW_MAM_20 = pff_NW[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pff_SE_MAM_18 = pff_SE[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pff_SE_MAM_20 = pff_SE[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pff_NW_JJA_20 = pff_NW[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pff_NW_JJA_19 = pff_NW[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
pff_SE_JJA_20 = pff_SE[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pff_SE_JJA_19 = pff_SE[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()

Plot6var(pff_NW_MAM_18,pff_NW_MAM_20,"MAM18 NW (black), MAM20 NW (red)", ylimit=8)
Plot6var(pff_NW_JJA_20,pff_NW_JJA_19,"JJA20 NW (black), JJA19 NW (red)", ylimit=8)

exit()
title = "MAM18, NW"
Plot6var(pff_NW_MAM_18,title, ylimit=4)
#LinearModel(pff_weekly_rss_clear_MAM_18, droppar)
title = "MAM20, NW"
Plot6var(pff_NW_MAM_20,title, ylimit=4)
title = "MAM18, SE"
Plot6var(pff_SE_MAM_18,title, ylimit=4)
title = "MAM20, SE"
Plot6var(pff_SE_MAM_20,title, ylimit=4)
title = "JJA20, NW"
Plot6var(pff_NW_JJA_20,title, ylimit=4)
title = "JJA19, NW"
Plot6var(pff_NW_JJA_19,title, ylimit=4)
title = "JJA20, SE"
Plot6var(pff_SE_JJA_20,title, ylimit=4)
title = "JJA19, SE"
Plot6var(pff_SE_JJA_19,title, ylimit=4)


pff_clearNW_MAM_18 = pff_clear_NW[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pff_clearNW_MAM_20 = pff_clear_NW[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pff_clearNW_JJA_20 = pff_clear_NW[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pff_clearNW_JJA_19 = pff_clear_NW[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
title = "MAM18, clear, NW, RSS"
Plot6var(pff_clearNW_MAM_18,title, ylimit=8)
#LinearModel(pff_weekly_rss_clear_MAM_18, droppar)
title = "MAM20, clear, NW, RSS"
Plot6var(pff_clearNW_MAM_20,title, ylimit=8)
#LinearModel(pff_weekly_rss_clear_MAM_20, droppar)
title = "JJA20, clear, NW, RSS"
Plot6var(pff_clearNW_JJA_20,title, ylimit=8)
title = "JJA19, clear, NW, RSS"
Plot6var(pff_clearNW_JJA_19,title, ylimit=8)

pff_MAM_18 = pff_full[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pff_MAM_20 = pff_full[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pff_JJA_20 = pff_full[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pff_JJA_19 = pff_full[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
title = "MAM18"
Plot6var(pff_MAM_18,title, ylimit=8)
#LinearModel(pff_weekly_rss_clear_MAM_18, droppar)
title = "MAM20"
Plot6var(pff_MAM_20,title, ylimit=8)
#LinearModel(pff_weekly_rss_clear_MAM_20, droppar)
title = "JJA20"
Plot6var(pff_JJA_20,title, ylimit=8)
title = "JJA19"
Plot6var(pff_JJA_19,title, ylimit=8)


pff_weekly_rss_clear_MAM_18 = pff_weekly_rss_clear[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pff_weekly_rss_clear_MAM_20 = pff_weekly_rss_clear[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pff_weekly_rss_clear_JJA_20 = pff_weekly_rss_clear[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pff_weekly_rss_clear_JJA_19 = pff_weekly_rss_clear[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
title = "MAM18, clear, weekly values, RSS"
Plot6var(pff_weekly_rss_clear_MAM_18,title, ylimit=8)
#LinearModel(pff_weekly_rss_clear_MAM_18, droppar)
title = "MAM20, clear, weekly values, RSS"
Plot6var(pff_weekly_rss_clear_MAM_20,title, ylimit=8)
#LinearModel(pff_weekly_rss_clear_MAM_20, droppar)
title = "JJA20, clear, weekly values, RSS"
Plot6var(pff_weekly_rss_clear_JJA_20,title, ylimit=8)
title = "JJA19, clear, weekly values, RSS"
Plot6var(pff_weekly_rss_clear_JJA_19,title, ylimit=8)

title = "MAM, no filter"
#pffMAM = pff.loc[(pff["datetime"].dt.month==12)]
#print(pffMAM)
#exit()
pffMAM_17 = pff_full[datetime(2017, 3, 1, 00, 00):datetime(2017, 5, 31, 00, 00)].resample('D').mean() #CHECKED OK
pffMAM_18 = pff_full[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pffMAM_19 = pff_full[datetime(2019, 3, 1, 00, 00):datetime(2019, 5, 31, 00, 00)].resample('D').mean()
pffMAM_20 = pff_full[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pffMAM_21 = pff_full[datetime(2021, 3, 1, 00, 00):datetime(2021, 5, 31, 00, 00)].resample('D').mean()
pffMAM = pd.concat([pffMAM_17,pffMAM_18,pffMAM_19,pffMAM_21])
Plot6var(pffMAM, title, ylimit=8)
#LinearModel(pffMAM.dropna(), droppar)

#SUMMER: JJA
title = "JJA, no filter"
pffJJA_17 = pff_full[datetime(2017, 6, 1, 00, 00):datetime(2017, 8, 31, 00, 00)].resample('D').mean()
pffJJA_18 = pff_full[datetime(2018, 6, 1, 00, 00):datetime(2018, 8, 31, 00, 00)].resample('D').mean()
pffJJA_19 = pff_full[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
pffJJA_20 = pff_full[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pffJJA_21 = pff_full[datetime(2021, 6, 1, 00, 00):datetime(2021, 8, 31, 00, 00)].resample('D').mean()
pffJJA = pd.concat([pffJJA_17,pffJJA_18,pffJJA_19,pffJJA_20,pffJJA_21])
Plot6var(pffJJA, title, ylimit=8)
#LinearModel(pffJJA.dropna(), droppar)

#SUMMER: SON
title = "SON, no filter"
pffSON_17 = pff_full[datetime(2017, 9, 1, 00, 00):datetime(2017, 11, 30, 00, 00)].resample('D').mean()
pffSON_18 = pff_full[datetime(2018, 9, 1, 00, 00):datetime(2018, 11, 30, 00, 00)].resample('D').mean()
pffSON_19 = pff_full[datetime(2019, 9, 1, 00, 00):datetime(2019, 11, 30, 00, 00)].resample('D').mean()
pffSON_20 = pff_full[datetime(2020, 9, 1, 00, 00):datetime(2020, 11, 30, 00, 00)].resample('D').mean()
pffSON = pd.concat([pffSON_17,pffSON_18,pffSON_19,pffSON_20])
Plot6var(pffSON, title, ylimit=8)
#SUMMER: DJF
title = "DJF, no filter"
pffDJF_17 = pff_full[datetime(2017, 12, 1, 00, 00):datetime(2018, 2, 28, 00, 00)].resample('D').mean()
pffDJF_18 = pff_full[datetime(2018, 12, 1, 00, 00):datetime(2019, 2, 28, 00, 00)].resample('D').mean()
pffDJF_19 = pff_full[datetime(2019, 12, 1, 00, 00):datetime(2020, 2, 29, 00, 00)].resample('D').mean()
pffDJF_20 = pff_full[datetime(2020, 12, 1, 00, 00):datetime(2021, 2, 28, 00, 00)].resample('D').mean()
pffDJF = pd.concat([pffDJF_17,pffDJF_18,pffDJF_19,pffDJF_20])
Plot6var(pffDJF, title, ylimit=8)

title = "full year, 90% GR"
Plot6var(pff_clear, title, ylimit=8)


title = "MAM, 90% GR"
#pffMAM = pff.loc[(pff["datetime"].dt.month==12)]
#print(pffMAM)
#exit()
pffMAM_17 = pff_clear[datetime(2017, 3, 1, 00, 00):datetime(2017, 5, 31, 00, 00)].resample('D').mean()
pffMAM_18 = pff_clear[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pffMAM_19 = pff_clear[datetime(2019, 3, 1, 00, 00):datetime(2019, 5, 31, 00, 00)].resample('D').mean()
pffMAM_20 = pff_clear[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pffMAM_21 = pff_clear[datetime(2021, 3, 1, 00, 00):datetime(2021, 5, 31, 00, 00)].resample('D').mean()
pffMAM = pd.concat([pffMAM_17,pffMAM_18,pffMAM_19,pffMAM_21])
Plot6var(pffMAM, title, ylimit=8)
pffMAM_w = pffMAM.resample("W").mean()
title = "MAM, 90% GR, weekly"
Plot6var(pffMAM_w, title, ylimit=8)

#SUMMER: JJA
title = "JJA, 90% GR"
pffJJA_17 = pff_clear[datetime(2017, 6, 1, 00, 00):datetime(2017, 8, 31, 00, 00)].resample('D').mean()
pffJJA_18 = pff_clear[datetime(2018, 6, 1, 00, 00):datetime(2018, 8, 31, 00, 00)].resample('D').mean()
pffJJA_19 = pff_clear[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
pffJJA_20 = pff_clear[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pffJJA_21 = pff_clear[datetime(2021, 6, 1, 00, 00):datetime(2021, 8, 31, 00, 00)].resample('D').mean()
pffJJA = pd.concat([pffJJA_17,pffJJA_18,pffJJA_19,pffJJA_20,pffJJA_21])
Plot6var(pffJJA, title, ylimit=8)
pffJJA_w = pffJJA.resample("W").mean()
title = "JJA, 90% GR, weekly"
Plot6var(pffJJA_w, title, ylimit=8)


#SUMMER: SON
title = "SON, 90% GR"
pffSON_17 = pff_clear[datetime(2017, 9, 1, 00, 00):datetime(2017, 11, 30, 00, 00)].resample('D').mean()
pffSON_18 = pff_clear[datetime(2018, 9, 1, 00, 00):datetime(2018, 11, 30, 00, 00)].resample('D').mean()
pffSON_19 = pff_clear[datetime(2019, 9, 1, 00, 00):datetime(2019, 11, 30, 00, 00)].resample('D').mean()
pffSON_20 = pff_clear[datetime(2020, 9, 1, 00, 00):datetime(2020, 11, 30, 00, 00)].resample('D').mean()
pffSON = pd.concat([pffSON_17,pffSON_18,pffSON_19,pffSON_20])
Plot6var(pffSON, title, ylimit=8)
pffSON_w = pffSON.resample("W").mean()
title = "SON, 90% GR, weekly"
Plot6var(pffSON_w, title, ylimit=8)

#SUMMER: DJF
title = "DJF, 90% GR"
pffDJF_17 = pff_clear[datetime(2017, 12, 1, 00, 00):datetime(2018, 2, 28, 00, 00)].resample('D').mean()
pffDJF_18 = pff_clear[datetime(2018, 12, 1, 00, 00):datetime(2019, 2, 28, 00, 00)].resample('D').mean()
pffDJF_19 = pff_clear[datetime(2019, 12, 1, 00, 00):datetime(2020, 2, 28, 00, 00)].resample('D').mean()
pffDJF_20 = pff_clear[datetime(2020, 12, 1, 00, 00):datetime(2021, 2, 28, 00, 00)].resample('D').mean()
pffDJF = pd.concat([pffDJF_17,pffDJF_18,pffDJF_19,pffDJF_20])
Plot6var(pffDJF, title, ylimit=8)
pffDJF_w = pffDJF.resample("W").mean()
title = "DJF, 90% GR, weekly"
Plot6var(pffDJF_w, title, ylimit=8)

"""METFILTER"""

pffPC = pff_clear.loc[pff_clear['PC'] == 0]  #CHECKED OK
pffAT = pffPC.loc[(pffPC['AT'] > 15)] #and (pffPC['AT'] < 25)]

title = "SE, PR=0, GR=90%, ATmax>15"
pffSE_met = pffAT.loc[(pffAT['WD'] >=90) & (pffAT['WD'] <=180)]
try:
    Plot6var(pffSE_met, title, ylimit=8)
    LinearModel(pffSE_met, droppar)
except:
    print("SE_low empty")
    pass

pffSE_met_w = pffSE_met.resample("W").mean()
title = "SE, PR=0, GR=90%, ATmax>15, weekly"
Plot6var(pffSE_met_w, title, ylimit=8)

title = "NW, PR=0, GR=90%, ATmax>15"
pffNW_met = pffAT.loc[(pffAT['WD'] >=270) & (pffAT['WD'] <=360)]
pffNW_met = pffNW_met
try:
    Plot6var(pffNW_met, title, ylimit=8)
    LinearModel(pffNW_met, droppar)
except:
    print("NW_low empty")
    pass


pffNW_met_w = pffNW_met.resample("W").mean()
title = "NW, PR=0, GR=90%, ATmax>15, weekly"
Plot6var(pffNW_met_w, title, ylimit=8)