# -*- coding: utf-8 -*-
__author__ = 'lnx'
#version history: cleaned version 20211105 building on:
# 1_VAL_SM_VOC_20192020
# 1_VAL_SM_VOC_20192020_onlycorrelations_inklSIF_inklO3.py
import numpy as np
from sklearn import linear_model
import scipy
import statsmodels.api as sm
from scipy.stats import shapiro
from scipy.stats import kstest
from scipy.stats import ks_2samp
import statsmodels.api as smod
from statsmodels.formula.api import ols
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
#print(isHighGR)  #boolean (False/True)
#print(HighGRdays[datetime(2018,1,1):])
#BOKUMetData_hourlymean['GR'].to_csv("/windata/DATA/BOKUMet_DATA_GR_noindex.csv",index=False)

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

#rss_sub['month'] = rss_sub['datetime'].dt.month
#rss_sub['day'] = rss_sub['datetime'].dt.day
#rss_sub['date'] = rss_sub['day'].astype(str) +' '+rss_sub['month'].astype(str)
#rss_sub['date'] = pd.to_datetime(rss_sub['date'])

#rss_sub['datetime'] = rss_sub['datetime'].replace(year=2000)

#rss_sub_x = rss_sub.replace(year=2000)
#print(rss_sub)
#rss_sub_grouped = rss_sub.groupby(by=['date']).mean()

#print(rss_sub_grouped)
#exit()

    #['RSS_sub_wWheat']
#extract "date" from "datetime"
#regroup and average accoarding to data

#GLIDING MEAN for GR, AT, SM?
N=5 #days
grsum_5daymean = np.convolve(BOKUMetData_dailysum['GR'], np.ones(N)/N, mode='valid')
rss_sub_5daymean = np.convolve(rss_sub['RSS_sub_wWheat'], np.ones(N)/N, mode='valid')
atmax_5daymean = np.convolve(BOKUMetData_dailymax['AT'], np.ones(N)/N, mode='valid')

Runningmean_5d = BOKUMetData_dailysum[4:]
Runningmean_5d.insert(1,'GR5d', grsum_5daymean.tolist()) #TODO A value is trying to be set on a copy of a slice from a DataFrame. Try using .loc[row_indexer,col_indexer] = value instead
Runningmean_5d.insert(1,'AT5d', atmax_5daymean.tolist())
#print(Runningmean_5d['GR5d'])
#exit()

#print(len(grsum_sub_5daymean))
#print(len(BOKUMetData_dailysum['GR']))
#y = range(len(grsum_sub_5daymean))
#figure = plt.figure
#plt.plot(y, grsum_sub_5daymean, color='violet', label="5day gliding mean")
#plt.plot(y, BOKUMetData_dailysum['GR'][4:], label="daily mean")
#plt.legend()
#plt.show()
#np.savetxt('/home/heidit/Downloads/grsum_sub_5daymean.csv', grsum_sub_5daymean, delimiter=",")

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

'''
Plotting
'''
o3_1990_2020_da = o3_1990_2020_da.resample('D').mean()

pff_full = pd.concat([hcho_dmax,vpd_dmax, rss_sub["RSS_sub_grass"], rss_sub["RSS_sub_wWheat"], BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"],HighGRdays["GR"], sif_join,
                o3_1990_2020_da["AT9STEF"],BOKUMetData_dailysum["WD"],BOKUMetData_dailysum["WS"], BOKUMetData_dailysum["PC"],pbl["PBL"]], axis=1)
pff_full.columns = ['hcho', 'vpd', 'RSSg', 'RSSw', 'AT', 'GR', 'GRhigh', 'SIF', 'O3','WD','WS','PC','PBL']

pff_NW = pff_full.loc[(pff_full['WD'] >=270) & (pff_full['WD'] <=359)]
pff_SE = pff_full.loc[(pff_full['WD'] >=90) & (pff_full['WD'] <=180)]
#pff_clear = pff_full.dropna(subset=['GRhigh'])
#pff_clear = pff_NW.dropna(subset=['GRhigh'])
#print(pff_clear)
#pff_clear2 = pff_clear.loc[pff_clear["GR"] >= 4500]
#pff_clear2_o3high = pff_clear2.loc[pff_clear2["O3"] > 100]
#pff_clear2_o3low = pff_clear2.loc[pff_clear2["O3"] <= 100]
#pff_clear2_o3high_NW = pff_clear2_o3high.loc[(pff_clear2_o3high['WD'] >=270) & (pff_clear2_o3high['WD'] <=360)]
#pff_clear2_o3high_SE = pff_clear2_o3high.loc[(pff_clear2_o3high['WD'] >=90) & (pff_clear2_o3high['WD'] <=180)]
#pff_weekly_rss_clear = pff_clear.resample("W").mean()

#pffMAM_18 = pff_clear[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
#pffMAM_20 = pff_clear[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pffMAM_18 = pff_NW[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pffMAM_20 = pff_NW[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()

#SUMMER: JJA
#pffJJA_19 = pff_clear[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
#pffJJA_20 = pff_clear[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pffJJA_19 = pff_NW[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
pffJJA_20 = pff_NW[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
len = len(pffMAM_20['hcho'].values)

#hcho_set = np.concatenate((pffMAM_20['hcho'].values,np.full((1,len),np.nan)))
#print(hcho_set)
#exit()
#hcho_set[-1,:3] = pffJJA_20['hcho'].values
# concatenate an array of the correct shape filled with np.nan
#arr1_arr2 = np.concatenate((arr1, np.full((1, arr1.shape[1]), np.nan)))
# fill concatenated row with values from arr2

pffMAM_20 = pffMAM_20.reset_index(drop=True)
pffMAM_18 = pffMAM_18.reset_index(drop=True)
pffJJA_19 = pffJJA_19.reset_index(drop=True)
pffJJA_20 = pffJJA_20.reset_index(drop=True)
hcho_set = pd.concat([pffMAM_20['hcho'],pffMAM_18['hcho']], axis=1)
GR_set = pd.concat([pffMAM_20['GR'],pffMAM_18['GR'],pffJJA_19['GR'],pffJJA_20['GR']], axis=1)
O3_set = pd.concat([pffMAM_20['O3'],pffMAM_18['O3'],pffJJA_19['O3'],pffJJA_20['O3']], axis=1)
AT_set = pd.concat([pffMAM_20['AT'],pffMAM_18['AT'],pffJJA_19['AT'],pffJJA_20['AT']], axis=1)
PBL_set = pd.concat([pffMAM_20['PBL'],pffMAM_18['PBL'],pffJJA_19['PBL'],pffJJA_20['PBL']], axis=1)
WS_set = pd.concat([pffMAM_20['WS'],pffMAM_18['WS'],pffJJA_19['WS'],pffJJA_20['WS']], axis=1)

GR_set2 = pd.concat([pffJJA_19['GR'],pffJJA_20['GR']], axis=1)
O3_set2 = pd.concat([pffJJA_19['O3'],pffJJA_20['O3']], axis=1)
AT_set2 = pd.concat([pffJJA_19['AT'],pffJJA_20['AT']], axis=1)
PBL_set2 = pd.concat([pffJJA_19['PBL'],pffJJA_20['PBL']], axis=1)
WS_set2 = pd.concat([pffJJA_19['WS'],pffJJA_20['WS']], axis=1)

GR_set3 = pd.concat([pffMAM_20['GR'],pffMAM_18['GR']], axis=1)
O3_set3 = pd.concat([pffMAM_20['O3'],pffMAM_18['O3']], axis=1)
AT_set3 = pd.concat([pffMAM_20['AT'],pffMAM_18['AT']], axis=1)
PBL_set3 = pd.concat([pffMAM_20['PBL'],pffMAM_18['PBL']], axis=1)
WS_set3 = pd.concat([pffMAM_20['WS'],pffMAM_18['WS']], axis=1)

fs=10
fig, axes = plt.subplots(nrows=2, ncols=2)#, sharey='row') #sharex='col', figsize=(6, 6))
#fig.set_size_inches(3.39,2.54)
axes[0, 0].boxplot(GR_set.dropna())
axes[0, 0].set_ylabel(u'global radiation [Wh m-2]', fontsize=fs)
axes[0, 0].set(xticklabels=('MAM20_d','MAM18_r','JJA19_d','JJA20_r'))

axes[0, 1].boxplot(O3_set.dropna())
axes[0, 1].set_ylabel(u'O3 [ppb]', fontsize=fs)
axes[0, 1].set(xticklabels=('MAM20_d','MAM18_r','JJA19_d','JJA20_r'))

axes[1, 0].boxplot(WS_set.dropna())
axes[1, 0].set_ylabel(u'wind speed [m s-1]', fontsize=fs)
axes[1, 0].set(xticklabels=('MAM20_d','MAM18_r','JJA19_d','JJA20_r'))

axes[1, 1].boxplot(PBL_set.dropna())
axes[1, 1].set_ylabel(u'PBL [m]', fontsize=fs)
axes[1, 1].set(xticklabels=('MAM20_d','MAM18_r','JJA19_d','JJA20_r'))
#fig.subplots_adjust(hspace=0.4)
#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure3_total_5days_vegcomp.tiff')
plt.show()

fig = plt.figure()  #figsize=(4,3)
#axisrange = [0,2,16,30]
#plt.axis(axisrange)
plt.boxplot(hcho_set.dropna())
#plt.title('', fontsize=fs)
plt.ylabel(u'HCHO [ppb]', fontsize=fs)
#ax = gca()
#ax.xaxis.set_ticklabels(['V0','STQ','V100'])
plt.show()

fig, axes = plt.subplots(nrows=2, ncols=2)#, sharey='row') #sharex='col', figsize=(6, 6))
#fig.set_size_inches(3.39,2.54)
axes[0, 0].boxplot(GR_set3.dropna())
#axes[0, 0].set_title('MAM20_dry', fontsize=fs)
axes[0, 0].set_ylabel(u'global radiation [Wh m-2]', fontsize=fs)
#axes[0, 0].set_xticks(1,labels=['MAM20_dry'])
axes[0, 0].set(xticklabels=('JJA19_d','JJA20_r'))

axes[0, 1].boxplot(O3_set3.dropna())
#axes[0, 1].set_title('MAM18_ref', fontsize=fs)
axes[0, 1].set_ylabel(u'O3 [ppb]', fontsize=fs)
axes[0, 1].set(xticklabels=('JJA19_d','JJA20_r'))

axes[1, 0].boxplot(WS_set3.dropna())
#axes[1, 0].set_title('JJA19_dry', fontsize=fs)
axes[1, 0].set_ylabel(u'wind speed [m s-1]', fontsize=fs)
axes[1, 0].set(xticklabels=('JJA19_d','JJA20_r'))

axes[1, 1].boxplot(PBL_set3.dropna())
#axes[1, 1].set_title('JJA20_ref', fontsize=fs)
axes[1, 1].set_ylabel(u'PBL [m]', fontsize=fs)
axes[1, 1].set(xticklabels=('JJA19_d','JJA20_r'))
#fig.subplots_adjust(hspace=0.4)
#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure3_total_5days_vegcomp.tiff')
plt.show()
exit()

"""Table 2"""
print("\n ******")
print("Table 2")
pff_MAM_18 = pff_full[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pff_MAM_20 = pff_full[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pff_JJA_20 = pff_full[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pff_JJA_19 = pff_full[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()

title = "MAM18"
Plot6var(pff_MAM_18,title, ylimit=8)
title = "MAM20"
Plot6var(pff_MAM_20,title, ylimit=8)
title = "JJA20"
Plot6var(pff_JJA_20,title, ylimit=8)
title = "JJA19"
Plot6var(pff_JJA_19,title, ylimit=8)





"""Table 3"""
print("\n ******")
print("Table 3")
#title = "full year,clear+>4.5kWh/day"
#Plot6var(pff_clear2, title, ylimit=8)

title = "full year, clear + >4.5kWh/day, > 100ug/m³mda8 daily max"
Plot6var(pff_clear2_o3high, title, ylimit=8)

title = "full year, clear + >4.5kWh/day, <= 100ug/m³mda8 daily max"
Plot6var(pff_clear2_o3low, title, ylimit=8)

title = "full year, clear + >4.5kWh/day, > 100ug/m³mda8 daily max, NW"
Plot6var(pff_clear2_o3high_NW, title, ylimit=8)

title = "full year, clear + >4.5kWh/day, > 100ug/m³mda8 daily max, SE"
Plot6var(pff_clear2_o3high_SE, title, ylimit=8)

#pff_20_I = pff_full[datetime(2020, 4, 20, 00, 00):datetime(2020, 5, 10, 00, 00)].resample('D').mean()
#pff_20_II = pff_full[datetime(2020, 5, 10, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
#title = "dry episode start"
#Plot6var(pff_20_I,title, ylimit=8)
#title = "dry episode end"
#Plot6var(pff_20_II,title, ylimit=8)

"""Table 4 + 5 """
print("\n ******")
print("Table 4+5")
pff_NW = pff_full.loc[(pff_full['WD'] >=270) & (pff_full['WD'] <=359)]
pff_SE = pff_full.loc[(pff_full['WD'] >=90) & (pff_full['WD'] <=180)]
#pff_NW = pff_clear.loc[(pff_full['WD'] >=270) & (pff_clear2['WD'] <=359)]
#pff_SE = pff_clear.loc[(pff_full['WD'] >=90) & (pff_clear2['WD'] <=180)]
pff_NW_MAM_18 = pff_NW[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pff_NW_MAM_19 = pff_NW[datetime(2019, 3, 1, 00, 00):datetime(2019, 5, 31, 00, 00)].resample('D').mean()
pff_NW_MAM_20 = pff_NW[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pff_NW_M18 = pff_NW[datetime(2018, 5, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pff_NW_M19 = pff_NW[datetime(2019, 5, 1, 00, 00):datetime(2019, 5, 31, 00, 00)].resample('D').mean()
pff_NW_M20 = pff_NW[datetime(2020, 5, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
#pff_SE_MAM_18 = pff_SE[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
#pff_SE_MAM_20 = pff_SE[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pff_NW_JJA_20 = pff_NW[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pff_NW_JJA_19 = pff_NW[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
pff_NW_A20 = pff_NW[datetime(2020, 8, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pff_NW_A19 = pff_NW[datetime(2019, 8, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
#pff_SE_JJA_20 = pff_SE[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
#pff_SE_JJA_19 = pff_SE[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()

title = "full year, no filter"
Plot6var(pff_full, title, ylimit=8)
title = "full year, clear"
Plot6var(pff_clear, title, ylimit=8)

title = "MAM18, NW"
Plot6var(pff_NW_MAM_18,title, ylimit=4)
title = "MAM19, NW"
Plot6var(pff_NW_MAM_19,title, ylimit=4)
title = "MAM20, NW"
Plot6var(pff_NW_MAM_20,title, ylimit=4)
#title = "MAM18, SE"
#Plot6var(pff_SE_MAM_18,title, ylimit=4)
#title = "MAM20, SE"
#Plot6var(pff_SE_MAM_20,title, ylimit=4)
title = "May18"
Plot6var(pff_NW_M18,title, ylimit=8)
title = "May20"
Plot6var(pff_NW_M20,title, ylimit=8)

title = "JJA19, NW"
Plot6var(pff_NW_JJA_19,title, ylimit=4)
title = "JJA20, NW"
Plot6var(pff_NW_JJA_20,title, ylimit=4)
#title = "JJA19, SE"
#Plot6var(pff_SE_JJA_19,title, ylimit=4)
#title = "JJA20, SE"
#Plot6var(pff_SE_JJA_20,title, ylimit=4)
title = "Aug19"
Plot6var(pff_NW_A19,title, ylimit=8)
title = "Aug20"
Plot6var(pff_NW_A20,title, ylimit=8)



"Table C.1"
print("\n ******")
print("Table C.1")

Plot6var(pff_full, "full year, no filter", ylimit=8)
Plot6var(pff_clear, "full year, 90% GR", ylimit=8)
pff_clear_w = pff_clear.resample("W").mean()
Plot6var(pff_clear_w, "full year, 90% GR_w", ylimit=8)

#SPRING: MAM
pffMAM_18 = pff_full[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pffMAM_19 = pff_full[datetime(2019, 3, 1, 00, 00):datetime(2019, 5, 31, 00, 00)].resample('D').mean()
pffMAM_20 = pff_full[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pffMAM = pd.concat([pffMAM_18,pffMAM_19,pffMAM_20])

#SUMMER: JJA
pffJJA_18 = pff_full[datetime(2018, 6, 1, 00, 00):datetime(2018, 8, 31, 00, 00)].resample('D').mean()
pffJJA_19 = pff_full[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
pffJJA_20 = pff_full[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pffJJA = pd.concat([pffJJA_18,pffJJA_19,pffJJA_20])

#SUMMER: SON
pffSON_18 = pff_full[datetime(2018, 9, 1, 00, 00):datetime(2018, 11, 30, 00, 00)].resample('D').mean()
pffSON_19 = pff_full[datetime(2019, 9, 1, 00, 00):datetime(2019, 11, 30, 00, 00)].resample('D').mean()
pffSON_20 = pff_full[datetime(2020, 9, 1, 00, 00):datetime(2020, 11, 30, 00, 00)].resample('D').mean()
pffSON = pd.concat([pffSON_18,pffSON_19,pffSON_20])

#SUMMER: DJF
pffDJF_18 = pff_full[datetime(2018, 12, 1, 00, 00):datetime(2019, 2, 28, 00, 00)].resample('D').mean()
pffDJF_19 = pff_full[datetime(2019, 12, 1, 00, 00):datetime(2020, 2, 29, 00, 00)].resample('D').mean()
pffDJF_20 = pff_full[datetime(2020, 12, 1, 00, 00):datetime(2021, 2, 28, 00, 00)].resample('D').mean()
pffDJF = pd.concat([pffDJF_18,pffDJF_19,pffDJF_20])

pffMAM_18 = pff_clear[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pffMAM_19 = pff_clear[datetime(2019, 3, 1, 00, 00):datetime(2019, 5, 31, 00, 00)].resample('D').mean()
pffMAM_20 = pff_clear[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pffMAM_c = pd.concat([pffMAM_18,pffMAM_19,pffMAM_20])
pffMAM_c_w = pffMAM_c.resample("W").mean()

#SUMMER: JJA
pffJJA_18 = pff_clear[datetime(2018, 6, 1, 00, 00):datetime(2018, 8, 31, 00, 00)].resample('D').mean()
pffJJA_19 = pff_clear[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
pffJJA_20 = pff_clear[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pffJJA_c = pd.concat([pffJJA_18,pffJJA_19,pffJJA_20])
pffJJA_c_w = pffJJA_c.resample("W").mean()

#SUMMER: SON
pffSON_18 = pff_clear[datetime(2018, 9, 1, 00, 00):datetime(2018, 11, 30, 00, 00)].resample('D').mean()
pffSON_19 = pff_clear[datetime(2019, 9, 1, 00, 00):datetime(2019, 11, 30, 00, 00)].resample('D').mean()
pffSON_20 = pff_clear[datetime(2020, 9, 1, 00, 00):datetime(2020, 11, 30, 00, 00)].resample('D').mean()
pffSON_c = pd.concat([pffSON_18,pffSON_19,pffSON_20])
pffSON_c_w = pffSON_c.resample("W").mean()

#SUMMER: DJF
pffDJF_18 = pff_clear[datetime(2018, 12, 1, 00, 00):datetime(2019, 2, 28, 00, 00)].resample('D').mean()
pffDJF_19 = pff_clear[datetime(2019, 12, 1, 00, 00):datetime(2020, 2, 28, 00, 00)].resample('D').mean()
pffDJF_20 = pff_clear[datetime(2020, 12, 1, 00, 00):datetime(2021, 2, 28, 00, 00)].resample('D').mean()
pffDJF_c = pd.concat([pffDJF_18,pffDJF_19,pffDJF_20])
pffDJF_c_w = pffDJF_c.resample("W").mean()


Plot6var(pffMAM, "MAM, no filter", ylimit=8)
Plot6var(pffMAM_c, "MAM, 90% GR", ylimit=8)
Plot6var(pffMAM_c_w, "MAM, 90% GR, weekly", ylimit=8)

Plot6var(pffJJA, "JJA, no filter", ylimit=8)
Plot6var(pffJJA_c, "JJA, 90% GR", ylimit=8)
Plot6var(pffJJA_c_w, "JJA, 90% GR, weekly", ylimit=8)

Plot6var(pffSON, "SON, no filter", ylimit=8)
Plot6var(pffSON_c, "SON, 90% GR", ylimit=8)
Plot6var(pffSON_c_w, "SON, 90% GR, weekly", ylimit=8)

Plot6var(pffDJF, "DJF, no filter", ylimit=8)
Plot6var(pffDJF_c, "DJF, 90% GR", ylimit=8)
Plot6var(pffDJF_c_w, "DJF, 90% GR", ylimit=8)
