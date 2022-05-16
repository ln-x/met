# -*- coding: utf-8 -*-
__author__ = 'lnx'
#version history: cleaned version 20211105 building on:
# 1_VAL_SM_VOC_20192020
# 1_VAL_SM_VOC_20192020_onlycorrelations_inklSIF_inklO3.py
from sklearn import linear_model
import numpy as np
import scipy
from scipy.stats import shapiro
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
#print(pff_clear[datetime(2018,1,1):datetime(2020,12,31)])
pff_clear2 = pff_clear.loc[pff_clear["GR"] >= 4500]
#print(pff_clear2[datetime(2018,1,1):datetime(2020,12,31)])
pff_clear2_o3high = pff_clear2.loc[pff_clear2["O3"] > 100]
#print(pff_clear2_o3high[datetime(2018,1,1):datetime(2020,12,31)]["O3"])
pff_clear2_o3low = pff_clear2.loc[pff_clear2["O3"] <= 100]
#print(pff_clear2_o3low[datetime(2018,1,1):datetime(2020,12,31)]["O3"])
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
    SRho_AT, Sp_AT = (stats.spearmanr(x5[idxAT], y5[idxAT]))
    SRho_GR, Sp_GR = (stats.spearmanr(x5_GR[idxGR], y5[idxGR]))
    SRho_VPD, Sp_VPD = (stats.spearmanr(x5_VPD[idxVPD], y5[idxVPD]))
    SRho_SM, Sp_SM = (stats.spearmanr(x5_SM[idxSM], y5[idxSM]))
    SRho_SIF, Sp_SIF = (stats.spearmanr(x5_SIF[idxSIF], y5[idxSIF]))
    SRho_NOX, Sp_NOX = (stats.spearmanr(x5_NOx[idxNOX], y5[idxNOX]))
    SRho_O3, Sp_O3 = (stats.spearmanr(x5_O3[idxO3], y5[idxO3]))
    SRho_PBL, Sp_PBL = (stats.spearmanr(x5_PBL[idxPBL], y5[idxPBL]))

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

    print(x5_2)
    SRho_AT_2, Sp_AT_2 = (stats.spearmanr(x5_2[idxAT_2], y5_2[idxAT_2]))
    SRho_GR_2, Sp_GR_2 = (stats.spearmanr(x5_GR_2[idxGR_2], y5_2[idxGR_2]))
    SRho_VPD_2, Sp_VPD_2 = (stats.spearmanr(x5_VPD_2[idxVPD_2], y5_2[idxVPD_2]))
    SRho_SM_2, Sp_SM_2 = (stats.spearmanr(x5_SM_2[idxSM_2], y5_2[idxSM_2]))
    SRho_SIF_2, Sp_SIF_2 = (stats.spearmanr(x5_SIF_2[idxSIF_2], y5_2[idxSIF_2]))
    SRho_NOX_2, Sp_NOX_2 = (stats.spearmanr(x5_NOx_2[idxNOX_2], y5_2[idxNOX_2]))
    SRho_O3_2, Sp_O3_2 = (stats.spearmanr(x5_O3_2[idxO3_2], y5_2[idxO3_2]))
    SRho_PBL_2, Sp_PBL_2 = (stats.spearmanr(x5_PBL_2[idxPBL_2], y5_2[idxPBL_2]))
    Lw_AT, Lp_AT = scipy.stats.levene(x5[idxAT], y5[idxAT])
    Lw_GR, Lp_GR = scipy.stats.levene(x5[idxGR], y5[idxGR])
    Lw_VPD, Lp_VPD = scipy.stats.levene(x5[idxVPD], y5[idxVPD])
    Lw_SM, Lp_SM = scipy.stats.levene(x5[idxSM], y5[idxSM])
    Lw_SIF, Lp_SIF = scipy.stats.levene(x5[idxSIF], y5[idxSIF])
    Lw_O3, Lp_O3 = scipy.stats.levene(x5[idxO3], y5[idxO3])
    Lw_AT_2, Lp_AT_2 = scipy.stats.levene(x5_2[idxAT_2], y5_2[idxAT_2])
    Lw_GR_2, Lp_GR_2 = scipy.stats.levene(x5_2[idxGR_2], y5_2[idxGR_2])
    Lw_VPD_2, Lp_VPD_2 = scipy.stats.levene(x5_2[idxVPD_2], y5_2[idxVPD_2])
    Lw_SM_2, Lp_SM_2 = scipy.stats.levene(x5_2[idxSM_2], y5_2[idxSM_2])
    Lw_SIF_2, Lp_SIF_2 = scipy.stats.levene(x5_2[idxSIF_2], y5_2[idxSIF_2])
    Lw_O3_2, Lp_O3_2 = scipy.stats.levene(x5_2[idxO3_2], y5_2[idxO3_2])


    print("Shapiro/Normality")
    print("AT", shapiro(x5[idxAT]).pvalue, "GR", shapiro(x5_GR[idxGR]).pvalue, "VDP", shapiro(x5_VPD[idxVPD]).pvalue,
          "SM", shapiro(x5_SM[idxSM]).pvalue, "SIF", shapiro(x5_SIF[idxSIF]).pvalue, "O3", shapiro(x5_O3[idxO3]).pvalue,
          "Hcho", shapiro(y5[idxAT]).pvalue)
    print("Variance")
    var = [np.var(x, ddof=1) for x in [x5, x5_GR, x5_VPD, x5_SM, x5_SIF, x5_O3]]
    print(var)
    print([np.var(x, ddof=1) for x in [x5, x5_GR, x5_VPD, x5_SM, x5_SIF, x5_O3]])
    print("Levene Test/Homoscedasticity")
    print("AT", Lp_AT, "GR", Lp_GR, "VPD", Lp_VPD, "SM", Lp_SM, "SIF", Lp_SIF, "O3", Lp_O3)
    print("AT", Lp_AT_2, "GR", Lp_GR_2, "VPD", Lp_VPD_2, "SM", Lp_SM_2, "SIF", Lp_SIF_2, "O3", Lp_O3_2)
    print("Spearman Test/Significance of Linear Regression:")
    print("AT", Sp_AT, "GR", Sp_GR, "VPD", Sp_VPD, "SM", Sp_SM, "SIF", Sp_SIF, "O3", Sp_O3)
    print("AT", Sp_AT_2, "GR", Sp_GR_2, "VPD", Sp_VPD_2, "SM", Sp_SM_2, "SIF", Sp_SIF_2, "O3", Sp_O3_2)


    m5_2, b5_2 = np.polyfit(x5_2[idxAT_2], y5_2[idxAT_2], 1)
    m5GR_2, b5GR_2 = np.polyfit(x5_GR_2[idxGR_2], y5_2[idxGR_2], 1)
    m5SM_2, b5SM_2 = np.polyfit(x5_SM_2[idxSM_2], y5_2[idxSM_2], 1)
    m5VPD_2, b5VPD_2 = np.polyfit(x5_VPD_2[idxVPD_2], y5_2[idxVPD_2], 1)
    m5SIF_2, b5SIF_2 = np.polyfit(x5_SIF_2[idxSIF_2], y5_2[idxSIF_2], 1)
    m5NOx_2, b5NOx_2 = np.polyfit(x5_NOx_2[idxNOX_2], y5_2[idxNOX_2], 1)
    m5O3_2, b5O3_2 = np.polyfit(x5_O3_2[idxO3_2], y5_2[idxO3_2], 1)
    m5PBL_2, b5PBL_2 = np.polyfit(x5_PBL_2[idxPBL_2], y5_2[idxPBL_2], 1)

    color1= "palegreen"
    color2= "mediumseagreen"
    color3= "thistle"
    color4="mediumpurple"
    a = 0
    fig, axs = plt.subplots(2, 3, figsize=(8, 6), dpi=100)
    #fig.suptitle(title, fontsize="small")
    axs[0, 0].scatter(x5[a:], y5[a:], color=color1, s=5)
    y_est = m5 * x5 + b5
    axs[0, 0].plot(x5, y_est, color=color2)
    axs[0, 0].set_title('(a) \n p_lowO3={:.2f} \n p_highO3={:.2f}'.format(Sp_AT, Sp_AT_2), fontsize='small')
    axs[0, 0].scatter(x5_2[a:], y5_2[a:], color=color3, s=5)
    y_est_2 = m5_2 * x5_2 + b5_2
    axs[0, 0].plot(x5_2, y_est_2, color=color4)
    # ax0.fill_between(x5, y_est - y_err_AT, y_est + y_err_AT, alpha=0.2)
    axs[0, 0].set_ylabel("HCHO [ppb]", size="small")
    axs[0, 0].set_xlabel("air temp [C°]", size="small")

    axs[0, 1].set_title('(b) \n p_lowO3={:.2f} \n p_highO3={:.2f}'.format(Sp_GR, Sp_GR_2), fontsize='small')
    axs[0, 1].scatter(x5_GR[a:], y5[a:], color=color1, s=5)
    axs[0, 1].plot(x5_GR, m5GR * x5_GR + b5GR, color=color2)
    axs[0, 1].scatter(x5_GR_2[a:], y5_2[a:], color=color3, s=5)
    axs[0, 1].plot(x5_GR_2, m5GR_2 * x5_GR_2 + b5GR_2, color=color4)
    axs[0, 1].set_xlabel(r"GR [kWhm⁻²]", size="medium")

    axs[0, 2].set_title('(c) \n p_lowO3={:.2f} \n p_highO3={:.2f}'.format(Sp_O3, Sp_O3_2), fontsize='small')
    axs[0, 2].scatter(x5_O3[a:], y5[a:], color=color1,s=5)
    axs[0, 2].plot(x5_O3, m5O3 * x5_O3 + b5O3, color=color2)
    axs[0, 2].scatter(x5_O3_2[a:], y5_2[a:], color=color3, s=5)
    axs[0, 2].plot(x5_O3_2, m5O3_2 * x5_O3_2 + b5O3_2, color=color4)
    axs[0, 2].set_xlabel("O3 [μg/m³]", size="medium")

    axs[1, 0].set_title('(d) \n p_lowO3={:.2f} \n p_highO3={:.2f}'.format(Sp_SM, Sp_SM_2), fontsize='small')
    axs[1, 0].scatter(x5_SM[a:], y5[a:], color=color1,s=5)
    axs[1, 0].plot(x5_SM, m5SM * x5_SM + b5SM, color=color2)
    axs[1, 0].scatter(x5_SM_2[a:], y5_2[a:], color=color3, s=5)
    axs[1, 0].plot(x5_SM_2, m5SM_2 * x5_SM_2 + b5SM_2, color=color4)
    axs[1, 0].set_xlabel("RSS [-]", size="medium")
    axs[1, 0].set_ylabel("HCHO [ppb]", size="small")

    axs[1, 1].set_title('(e) \n p_lowO3={:.2f} \n p_highO3={:.2f}'.format(Sp_SIF, Sp_SIF_2), fontsize='small')
    axs[1, 1].scatter(x5_SIF[a:], y5[a:], color=color1,s=5)
    axs[1, 1].plot(x5_SIF, m5SIF * x5_SIF + b5SIF, color=color2)
    axs[1, 1].scatter(x5_SIF_2[a:], y5_2[a:], color=color3, s=5)
    axs[1, 1].plot(x5_SIF_2, m5SIF_2 * x5_SIF_2 + b5SIF_2, color=color4)
    axs[1, 1].set_xlabel(r"SIF [mWm⁻²sr⁻¹nm⁻¹]", size="medium")

    axs[1, 2].set_title('(f) \n p_lowO3={:.2f} \n p_highO3={:.2f}'.format(Sp_VPD, Sp_VPD_2), fontsize='small')
    axs[1, 2].scatter(x5_VPD[a:], y5[a:],  color=color1,s=5)
    axs[1, 2].plot(x5_VPD, m5VPD * x5_VPD + b5VPD, color=color2)
    axs[1, 2].scatter(x5_VPD_2[a:], y5_2[a:], color=color3, s=5)
    axs[1, 2].plot(x5_VPD_2, m5VPD_2 * x5_VPD_2 + b5VPD_2, color=color4)
    axs[1, 2].set_xlabel("VPD [kPa]", size="medium")

    axs[0, 0].set_ylim(0, ylimit)
    axs[0, 1].set_ylim(0, ylimit)
    axs[0, 2].set_ylim(0, ylimit)
    axs[1, 0].set_ylim(0, ylimit)
    axs[1, 1].set_ylim(0, ylimit)
    axs[1, 2].set_ylim(0, ylimit)
    fig.tight_layout()
    plt.show()
    #plt.savefig("/home/heidit/Downloads/" + title + ".jpg")

Plot6var(pff_clear2_o3low,pff_clear2_o3high," ", ylimit=8)