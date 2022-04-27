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

"read in VINDOBONA"

foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
foldername_K = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_KQ"

hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))
#hchoK_d, hchoK_dmax, hchoK_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_K,"K", begin= datetime.datetime(2020, 1, 1, 0, 0, 0)))
#print(len(hchoK_dmax))
#print(len(hcho_dmax))

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
o3_2020_mda1 = pd.read_csv(pathbase2 + "AT_O3_2020.csv")                        #TODO! replace mda1 with mda8!
o3_2020_mda1 = o3_2020_mda1.set_index(pd.to_datetime(o3_2020_mda1['date']))
o3_2020_mda1 = o3_2020_mda1.drop(columns=['date'])
#print(o3_1990_2019_mda1)
o3_2020_mda8 = o3_2020_mda1.resample('8H', label='right').mean()
o3_2020_mda8 = o3_2020_mda8.resample('D').mean()

#o3_1990_2020_mda1 = pd.concat([o3_1990_2019_mda1, o3_2020_mda1], axis=0)
#o3_1990_2019_mda1 = o3_1990_2019_mda1**ugm3toppb_o3 #MUG->PPB
#o3_1990_2020_da = o3_1990_2020_mda8.resample('D').mean()
#o3_1990_2020_m = o3_1990_2020_mda8.resample('M').mean()
o3_1990_2020_mda8 = pd.concat([o3_1990_2019_mda8, o3_2020_mda8], axis=0)
o3_1990_2020_mda8 = o3_1990_2020_mda8**ugm3toppb_o3 #MUG->PPB
o3_1990_2020_da = o3_1990_2020_mda8.resample('D').mean()
o3_1990_2020_m = o3_1990_2020_mda8.resample('M').mean()

'''READ IN BOKU Metdata'''
BOKUMetData = met.library.BOKUMet_Data.BOKUMet() #10min values
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean, 'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean, 'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailymax = BOKUMetData_hourlymean.resample('D').agg({'DT': np.max, 'AT': np.max, 'RH': np.max, 'GR': np.max, 'WS': np.max,'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})

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
#print(HighGRdays)

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
#tsif_r = pd.read_csv("/windata/DATA/remote/satellite/TROPOMI/TSIF_743.csv", sep=",")
tsif_r = pd.read_csv("/windata/DATA/remote/satellite/TROPOMI/TSIF_743_LAT48_28_LON16_23.csv", sep=",")
tsif = tsif_r.set_index(pd.to_datetime(tsif_r['time']))
tsif = tsif.drop(columns=['time'])
#osif_771_r = pd.read_csv("/windata/DATA/remote/satellite/OCO/OSIF_8100_771nm.csv", sep=",")
#osif_771 = osif_771_r.set_index(pd.to_datetime(osif_771_r['time']))
#osif_771 = osif_771.drop(columns=['time'])
osif_757_r = pd.read_csv("/windata/DATA/remote/satellite/OCO2/OSIF_8100_757nm.csv", sep=",")
osif_757 = osif_757_r.set_index(pd.to_datetime(osif_757_r['time']))
osif_757 = osif_757.drop(columns=['time'])

'''READ IN CEILOMETER DATA'''
file_pbl = "/windata/DATA/obs_point/met/ZAMG/Ceilometer/MH_Wien_Hohe_Warte_20170101_20201231.csv"
pbl = pd.read_csv(file_pbl,skiprows=2, parse_dates={'datetime':[0,1]})
pbl.columns = ['datetime','PBL']  #UTC
pbl = pbl.set_index(pbl['datetime'])
pbl = pbl.drop(columns=['datetime'])
pbl = pbl.resample('D').max()
#print(pbl)

'''TIMESLICES'''

'''
Plotting
'''
nox_1990_2020_da = nox_1990_2020_da.resample('D').mean()
o3_1990_2020_da = o3_1990_2020_da.resample('D').mean()

#print(hcho_dmax) 2017-05-01 - 2021-08-31
#print(rss_sub_diff_w) 2017-05-01 - 2020-12-31
#print(BOKUMetData_dailymax) 2009-01-01 - 2021-10-21
#print(HighGRdays)
#print(tsif) 2018-05-01  - 2021-3-20
#print(o3_1990_2020_da)  1990-1-1 - 2020-12-31
#print(nox_1990_2020_da) 1990-1-1 - 2021-01-01
#print(pbl) 2017-01-01 - 2021-01-01

#VER8
pff_all = pd.concat([hcho_dmax,rss_sub["RSS_sub_wWheat"],BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"],tsif,
                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],BOKUMetData_dailysum["WD"],BOKUMetData_dailysum["PC"],pbl["PBL"]],axis=1)
pff_all.columns =['hcho', 'SM', 'AT', 'GR', 'SIF', 'O3', 'NOX','WD','PC','PBL']
pff_all.index.name = 'datetime'
#pff_all.dropna()

#VERS7 without GR filter
#pff_nofilter = pd.concat([hcho_dmax,rss_sub_diff_w,BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"],tsif,
#                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],BOKUMetData_dailysum["WD"],BOKUMetData_dailysum["PC"],pbl["PBL"]],axis=1)
#pff_nofilter.columns =['hcho', 'SM', 'AT', 'GR', 'SIF', 'O3','NOx','WD','PC','PBL']
#pff_nofilter.index.name = 'datetime'

#VERS6 including RSS_climatological diff instead of RSS, GR filter > 90%, Ceilometer PBL
#pff = pd.concat([hcho_dmax,rss_sub_diff_w,BOKUMetData_dailymax["AT"],HighGRdays["GR"],tsif,
#                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],HighGRdays["WD"],HighGRdays["PC"],pbl["PBL"]],axis=1)
#pff = pff.dropna(subset=['GR'])   #df.dropna(subset=['TotalMarks'])
#pd.set_option("display.max_rows", None, "display.max_columns", None)


#print(pff[June17:June18])
#exit()

#VERS5 including GR filter > 90%, Ceilometer PBL, gliding mean for AT and GR ??Runningmean_5d['RSS5d']
#pff = pd.concat([hcho_dmax,rss_sub["RSS_sub_grass"],Runningmean_5d['AT5d'],Runningmean_5d['GR5d'],tsif,
#                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],HighGRdays["WD"],HighGRdays["PC"],pbl["PBL"]], axis=1)

#VERS4 including GR filter > 90%, Ceilometer PBL
pff_clear = pd.concat([hcho_dmax,rss_sub["RSS_sub_wWheat"],BOKUMetData_dailymax["AT"],HighGRdays["GR"],tsif,
                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],HighGRdays["WD"],HighGRdays["PC"],pbl["PBL"]],axis=1)
pff_clear = pff_clear.dropna(subset=['GR'])   #df.dropna(subset=['TotalMarks'])

#VERS3 including GR filter > 90%, Ceilometer PBL, VWC
#pff = pd.concat([hcho_dmax,vwc_sub['VWC_sub_wWheat'],BOKUMetData_dailymax["AT"],HighGRdays["GR"],tsif,
#                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],HighGRdays["WD"],HighGRdays["PC"],pbl["PBL"]],axis=1)

#VERS2 including GR filter > 90%, CAMX PBL
#pff_vers2 = pd.concat([hcho_dmax,rss_sub["RSS_sub_wWheat"],BOKUMetData_dailymax["AT"],HighGRdays["GR"],tsif,
#                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],HighGRdays["WD"],HighGRdays["PC"],par1["zmla"]],axis=1)
#VERS1 without GR filter
#pff_nofilter = pd.concat([hcho_dmax,rss_sub["RSS_sub_wWheat"],BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"],tsif,
#                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],BOKUMetData_dailysum["WD"],BOKUMetData_dailysum["PC"],par1["zmla"]],axis=1)

#pff.columns =['hcho', 'SM', 'AT', 'GR', 'SIF', 'O3','NOx','WD','PC','PBL']
#pff.index.name = 'datetime'
pff_clear.columns = ['hcho', 'SM', 'AT', 'GR', 'SIF', 'O3','NOx','WD','PC','PBL']
pff_clear.index.name = 'datetime'

pffNW_clear = pff_clear.loc[(pff_clear['WD'] >=270) & (pff_clear['WD'] <=359)]
#pff_weekly_rss_clear = pff_vers4.resample("W").mean()

#TODO: nox_1990_2020_da["AT9STEF"],'NOx' procudes additional timesteps (1:00 instead of 0:00) which makes the boolean filters fail
"""LINEAR MODEL"""
""
def LinearModel(df,droppar):
    #pffPC = pff.loc[pff['PC'] == 0]
    #pffNW = pffPC.loc[(pffPC['WD'] >=270) & (pffPC['WD'] <=360)]
    #pffNW = pffNW.dropna()
    #pffSE = pffPC.loc[(pffPC['WD'] >=90) & (pffPC['WD'] <=180)]
    #pffSEMAM19 = pffSE[March19:June19].resample('D').mean()
    #pffSEMAM20 = pffSE[March:June].resample('D').mean()
    #pffSEMAM = pffSEMAM19.append(pffSEMAM20)
    #pffSEMAM = pffSEMAM.dropna()
    #pffSE = pffSE.dropna()
    #pffSEJJA19 = pffSE[June19:Sept19].resample('D').mean()
    #pffSEJJA20 = pffSE[June:Sept].resample('D').mean()
    #pffSEJJA = pffSEJJA19.append(pffSEMAM20)
    #pffSEJJA = pffSEJJA.dropna()
    #pff5 = pffSEJJA #[start:end]
    #pff5 = pffPC
    #print(droppar)
    X = df.drop(['hcho'], axis = 1)
    X = X.drop(droppar, axis = 1)
    #X = X.drop(['O3'], axis = 1)
    #X = X.drop(['NOx'], axis = 1)
    #X = X.drop(['WD'], axis = 1)
    #X = X.drop(['PC'], axis = 1)
    #X = X.drop(['GR'], axis = 1)
    #X = X.drop(['SIF'], axis = 1)
    #X = X.drop(['SM'], axis = 1)
    #X = X.drop(['AT'], axis = 1)
    #X = X.drop(['PBL'], axis = 1)
    #print(X.columns)
    #X = X.values.reshape(-1,8)
    y = df['hcho']
    #print(y.columns)
    ols = linear_model.LinearRegression()
    model = ols.fit(X, y)
    output = ("Model Coefficients:", model.coef_, "Model Intercept:", model.intercept_,"Model Score:", model.score(X, y))
    return output
    #Model Scores for PC=0 and GR>90%:
    # JJA20, NW f(SM,AT,GR,SIF,PBL) : 0.862053877091254
    # JJA20, SE f(SM,AT,GR,SIF,PBL) : 0.6779170809900591

    #MAM19+20, SE['SM', 'AT', 'GR', 'SIF', 'PBL']
    #Model Coefficients: [-7.46621888e-02 -6.40716503e-02  3.92873396e-04 -4.36954194e-01
    #  8.30631989e-04]
    #Model Intercept: -0.3686562673084044
    #Model Score: 0.15796381195269982

def Plot6var(df,title):
    x5 = df['AT'].values.flatten()
    x5_GR = df['GR'].values.flatten()
    x5_SM = df['SM'].values.flatten()
    x5_SIF = df['SIF'].values.flatten()
    x5_NOx = df['NOx'].values.flatten()
    x5_O3 = df['O3'].values.flatten()
    x5_PBL = df['PBL'].values.flatten()
    y5 = df['hcho'].values.flatten()
    idxAT = np.isfinite(x5) & np.isfinite(y5)
    idxGR = np.isfinite(x5_GR) & np.isfinite(y5)
    idxSIF = np.isfinite(x5_SIF) & np.isfinite(y5)
    idxSM = np.isfinite(x5_SM) & np.isfinite(y5)
    idxNOX = np.isfinite(x5_NOx) & np.isfinite(y5)
    idxO3 = np.isfinite(x5_O3) & np.isfinite(y5)
    idxPBL = np.isfinite(x5_PBL) & np.isfinite(y5)
    nAT = len(y5[idxAT])
    nGR = len(y5[idxGR])
    nSIF = len(y5[idxSIF])
    nSM = len(y5[idxSM])
    nNOx = len(y5[idxNOX])
    nO3 = len(y5[idxO3])
    nPBL = len(y5[idxPBL])
    print("hcho",len(y5),"nAT,nGR,nSIF,nSM,nNOx,nO3,nPBL", nAT,nGR,nSIF,nSM,nNOx,nO3,nPBL)
    m5, b5 = np.polyfit(x5[idxAT], y5[idxAT], 1)
    print("m5,b5, AT", m5,b5, title)
    m5GR, b5GR = np.polyfit(x5_GR[idxGR], y5[idxGR], 1)
    m5SM, b5SM = np.polyfit(x5_SM[idxSM], y5[idxSM], 1)
    m5SIF, b5SIF = np.polyfit(x5_SIF[idxSIF], y5[idxSIF], 1)
    m5NOx, b5NOx = np.polyfit(x5_NOx[idxNOX], y5[idxNOX], 1)
    m5O3, b5O3 = np.polyfit(x5_O3[idxO3], y5[idxO3], 1)
    m5PBL, b5PBL = np.polyfit(x5_PBL[idxPBL], y5[idxPBL], 1)

    SRho_AT, Sp_AT = (stats.spearmanr(x5[idxAT], y5[idxAT]))
    SRho_GR, Sp_GR = (stats.spearmanr(x5_GR[idxGR], y5[idxGR]))
    SRho_SM, Sp_SM = (stats.spearmanr(x5_SM[idxSM], y5[idxSM]))
    SRho_SIF, Sp_SIF = (stats.spearmanr(x5_SIF[idxSIF], y5[idxSIF]))
    SRho_NOX, Sp_NOX = (stats.spearmanr(x5_NOx[idxNOX], y5[idxNOX]))
    SRho_O3, Sp_O3 = (stats.spearmanr(x5_O3[idxO3], y5[idxO3]))
    SRho_PBL, Sp_PBL = (stats.spearmanr(x5_PBL[idxPBL], y5[idxPBL]))
    Pr_AT, p_AT = (stats.pearsonr(x5[idxAT], y5[idxAT]))
    Pr_GR, p_GR = (stats.pearsonr(x5_GR[idxGR], y5[idxGR]))
    Pr_SM, p_SM = (stats.pearsonr(x5_SM[idxSM], y5[idxSM]))
    Pr_SIF, p_SIF = (stats.pearsonr(x5_SIF[idxSIF], y5[idxSIF]))
    Pr_NOX, p_NOX = (stats.pearsonr(x5_NOx[idxNOX], y5[idxNOX]))
    Pr_O3, p_O3 = (stats.pearsonr(x5_O3[idxO3], y5[idxO3]))
    Pr_PBL, p_PBL = (stats.pearsonr(x5_PBL[idxPBL], y5[idxPBL]))
    print(title, "Spearman:", "AT", SRho_AT, Sp_AT, "GR", SRho_GR, Sp_GR, "SM", SRho_SM, Sp_SM, "SIF", SRho_SIF, Sp_SIF,
          "NOX", SRho_NOX, Sp_NOX, "O3", SRho_O3, Sp_O3, "PBL", SRho_PBL, Sp_PBL)
    print(title, "Pearson:", "AT", Pr_AT, p_AT, "GR", Pr_GR, p_GR, "SM", Pr_SM, p_SM, "SIF", Pr_SIF, p_SIF,
          "NOX", Pr_NOX, p_NOX, "O3", Pr_O3, p_O3, "PBL", Pr_PBL, p_PBL)
    #exit()

    #print(R_AT, R_GR, R_SM, R_SIF, R_NOX, R_O3)
    #R2_AT, R2_GR, R2_SM, R2_SIF, R2_NOX, R2_O3 = R_AT ** 2, R_GR ** 2, R_SM ** 2, R_SIF ** 2, R_NOX ** 2, R_O3 ** 2
    #print(R2_AT, R2_GR, R2_SM, R2_SIF, R2_NOX, R2_O3)
    # -0.11468772201686629 0.12327935222672066 0.26591170630878136 0.04979757085020243 -0.21842105263157893 0.12834008097165991
    # 0.013153273581417997 0.015197798685439858 0.07070903555204759 0.0024797980625809305 0.04770775623268697 0.016471176383812222
    a = 0
    fig, axes = plt.subplots(nrows=1, ncols=6, figsize=(8, 6), dpi=100)
    # fig, axes = plt.subplots(nrows=1, ncols=7, figsize=(8, 6), dpi=100)
    fig.suptitle(title, fontsize="small")
    ax0, ax1, ax2, ax3, ax5, ax6 = axes.flatten()
    # ax0, ax1, ax2, ax3, ax4, ax5, ax6 = axes.flatten()
    ax0.scatter(x5[a:], y5[a:], color='grey', s=5)
    ax0.plot(x5, m5 * x5 + b5, color='black')
    ax0.set_ylabel("HCHO [ppb]", size="small")
    ax0.set_xlabel("air temp [C°]", size="small")
    ax0.set_title('r={:.2f} \n p={:.2f} \n n={}'.format(Pr_AT,p_AT,nAT), fontsize='small')

    ax1.scatter(x5_GR[a:], y5[a:], color='grey', s=5)
    ax1.plot(x5_GR, m5GR * x5_GR + b5GR, color='black')
    ax1.set_xlabel(r"GR [$Wm⁻²$]", size="medium")
    ax1.set_title('r={:.2f} \n p={:.2f} \n n={}'.format(Pr_GR,p_GR,nGR), fontsize='small')

    ax2.scatter(x5_SM[a:], y5[a:], color='grey',s=5)
    ax2.plot(x5_SM, m5SM * x5_SM + b5SM, color='black')
    # ax2.set_xlabel("SM [$m^3$$m^(-3)$]", size="medium")
    ax2.set_xlabel("$\Delta$ RSS [-]", size="medium")
    ax2.set_title('r={:.2f} \n p={:.2f} \n n={}'.format(Pr_SM,p_SM,nSM), fontsize='small')

    ax3.scatter(x5_SIF[a:], y5[a:], color='grey',s=5)
    ax3.plot(x5_SIF, m5SIF * x5_SIF + b5SIF, color='black')
    ax3.set_xlabel(r"SIF [mWm⁻²sr⁻¹nm⁻¹]", size="medium")
    ax3.set_title('r={:.2f} \n p={:.2f} \n n={}'.format(Pr_SIF,p_SIF,nSIF), fontsize='small')

    #ax4.scatter(x5_NOx[a:], y5[a:], color='violet')
    #ax4.plot(x5_NOx, m5NOx * x5_NOx + b5NOx, color='red')
    #ax4.set_xlabel("NOx [ppb]", size="medium")
    #ax4.set_title('$R={:.2f}$'.format(R_NOX), fontsize='small')
    ax5.scatter(x5_O3[a:], y5[a:], color='grey',s=5)
    ax5.plot(x5_O3, m5O3 * x5_O3 + b5O3, color='black')
    ax5.set_xlabel("O3 [ppb]", size="medium")
    ax5.set_title('r={:.2f} \n p={:.2f} \n n={}'.format(Pr_O3,p_O3,nO3), fontsize='small')
    ax6.scatter(x5_PBL[a:], y5[a:], color='grey',s=5)
    ax6.plot(x5_PBL, m5PBL * x5_PBL + b5PBL, color='black')
    ax6.set_xlabel("PBL [m]", size="medium")
    ax6.set_title('r={:.2f} \n p={:.2f} \n n={}'.format(Pr_PBL,p_PBL,nPBL), fontsize='small')
    ax0.set_ylim(0, 8)
    ax1.set_ylim(0, 8)
    ax2.set_ylim(0, 8)
    ax3.set_ylim(0, 8)
    #ax4.ylim(0, 8)
    ax5.set_ylim(0, 8)
    ax6.set_ylim(0, 8)
    fig.tight_layout()
    plt.savefig("/home/heidit/Downloads/"+title+".jpg")
    plt.show()

def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)
    # the scatter plot:
    ax.scatter(x, y)
    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth
    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')

def CalcRegressionCoef(df):
    print("test1")
    #print(df['SM'].values.flatten())
    x5 = df['AT'].values.flatten()
    #x5_GR = df['GR'].values.flatten()
    x5_SM = df['SM'].values.flatten()
    x5_SIF = df['SIF'].values.flatten()
    #x5_NOx = df['NOx'].values.flatten()
    x5_O3 = df['O3'].values.flatten()
    #x5_PBL = df['PBL'].values.flatten()
    y5 = df['hcho'].values.flatten()
    #print(x5)
    idxAT = np.isfinite(x5) & np.isfinite(y5)
    #idxGR = np.isfinite(x5_GR) & np.isfinite(y5)
    idxSIF = np.isfinite(x5_SIF) & np.isfinite(y5)
    idxSM = np.isfinite(x5_SM) & np.isfinite(y5)
    #idxNOX = np.isfinite(x5_NOx) & np.isfinite(y5)
    idxO3 = np.isfinite(x5_O3) & np.isfinite(y5)
    #idxPBL = np.isfinite(x5_PBL) & np.isfinite(y5)
    #print(idxAT)
    nAT = len(y5[idxAT])
    #nGR = len(y5[idxGR])
    nSIF = len(y5[idxSIF])
    nSM = len(y5[idxSM])
    #nNOx = len(y5[idxNOX])
    nO3 = len(y5[idxO3])
    #nPBL = len(y5[idxPBL])
    #print("hcho",len(y5),"nAT,nGR,nSIF,nSM,nNOx,nO3,nPBL", nAT,nGR,nSIF,nSM,nNOx,nO3,nPBL)
    SRho_AT, Sp_AT = (stats.spearmanr(x5[idxAT], y5[idxAT]))
    #SRho_GR, Sp_GR = (stats.spearmanr(x5_GR[idxGR], y5[idxGR]))
    SRho_SM, Sp_SM = (stats.spearmanr(x5_SM[idxSM], y5[idxSM]))
    SRho_SIF, Sp_SIF = (stats.spearmanr(x5_SIF[idxSIF], y5[idxSIF]))
    #SRho_NOX, Sp_NOX = (stats.spearmanr(x5_NOx[idxNOX], y5[idxNOX]))
    SRho_O3, Sp_O3 = (stats.spearmanr(x5_O3[idxO3], y5[idxO3]))
    #SRho_PBL, Sp_PBL = (stats.spearmanr(x5_PBL[idxPBL], y5[idxPBL]))
    #Pr_AT, p_AT = (stats.pearsonr(x5[idxAT], y5[idxAT]))
    #Pr_GR, p_GR = (stats.pearsonr(x5_GR[idxGR], y5[idxGR]))
    #Pr_SM, p_SM = (stats.pearsonr(x5_SM[idxSM], y5[idxSM]))
    #Pr_SIF, p_SIF = (stats.pearsonr(x5_SIF[idxSIF], y5[idxSIF]))
    #Pr_NOX, p_NOX = (stats.pearsonr(x5_NOx[idxNOX], y5[idxNOX]))
    #Pr_O3, p_O3 = (stats.pearsonr(x5_O3[idxO3], y5[idxO3]))
    #Pr_PBL, p_PBL = (stats.pearsonr(x5_PBL[idxPBL], y5[idxPBL]))

    return(SRho_AT, SRho_SM, SRho_SIF, SRho_O3)
    #return(SRho_AT, SRho_GR, SRho_SM, SRho_SIF, SRho_NOX, SRho_O3, SRho_PBL, SRho_PBL)

"""FULL PERIOD"""
#"""
title = "full year, no filter"
#Plot6var(pff_nofilter, title)

title = "full year, no filter, weekly values, RSS"
pffNW_clear1 = pffNW_clear[datetime(2017,5,1,0,0):datetime(2020,12,31,0,0)]
pffNW_clear1 = pffNW_clear1.reset_index()

pff_clear1 = pff_clear[datetime(2017,5,1,0,0):datetime(2020,12,31,0,0)]
pff_clear1 = pff_clear1.reset_index()
pff_all1 = pff_all[datetime(2017,5,1,0,0):datetime(2020,12,31,0,0)]
pff_all1 = pff_all1.reset_index()
#print("print pff-all", pff_all1)
gNW_clear = pffNW_clear1.groupby(pd.Grouper(key='datetime', freq='M'))
g_clear = pff_clear1.groupby(pd.Grouper(key='datetime', freq='M'))
g_all = pff_all1.groupby(pd.Grouper(key='datetime', freq='M'))
#g_all = pff_all.groupby(pd.Grouper(key='datetime', freq='M'))
# groups to a list of dataframes with list comprehension
dfsNW_clear = [group for _,group in gNW_clear]
dfs_clear = [group for _,group in g_clear]
dfs = [group for _,group in g_all]
#print("print dfs", dfs)

SRho_SM_array,SRho_SIF_array,SRho_O3_array = [],[],[]
date = []
months = []
years = []

for i in dfsNW_clear:
    #i.dropna()
    #print(1)
    #print(i['datetime'])
    #print(i['datetime'].iloc[0].month)
    try:
        SRho_AT, SRho_SM, SRho_SIF, SRho_O3 = CalcRegressionCoef(i)
        print(SRho_SM)
        #date.append(datetime(year=i['datetime'].iloc[0].year,month=i['datetime'].iloc[0].month))
        #months.append(i['datetime'].iloc[0].month)
        #years.append(i['datetime'].iloc[0].year)


    except:
        pass
    SRho_SM_array.append(SRho_SM)
    SRho_SIF_array.append(SRho_SIF)
    SRho_O3_array.append(SRho_O3)
print(months)
print(SRho_SM_array)
print(SRho_SIF_array)
print(SRho_O3_array)

#exit()
#df = pd.DataFrame([SRho_SM_array,SRho_SIF_array,SRho_O3_array], columns=['RSS', 'SIF', 'O3'], index=date)
#print(df)
print(len(SRho_SM_array), len(SRho_SIF_array), len(SRho_O3_array)) #44 _ Mai/2017 -> Dez/(2020)
yM = [3,6,9,12,15,18,21,24,27,30,33,36,39,42]
yM_ticks = ["7/17","10/17","1/18","4/18","7/18","10/18","1/19","4/19","7/19","10/19","1/20","4/20","7/20","10/20"]

figure = plt.figure
plt.plot(range(len(SRho_SM_array)), SRho_SM_array, marker="x", linestyle=":", linewidth="0.5", color="orange", label="SRho RSS")
plt.plot(range(len(SRho_SM_array)), SRho_SIF_array, marker="x", linestyle=":",linewidth="0.5", color="green", label="SRho SIF")
plt.plot(range(len(SRho_SM_array)), SRho_O3_array, marker="x", linestyle=":",linewidth="0.5", color="violet", label="SRho O3")
plt.hlines(y=0,xmin=0, xmax=44)
plt.xticks(yM, yM_ticks)
plt.legend()
plt.show()

#plt.plot(df.index,df.RSS,label="SRho rss")
#plt.plot(df.index,df.SIF,label="SRho sif")
#plt.plot(df.index,df.O3,label="SRho O3")
#print(dfs)

exit()
#TODO
"""
dfs_for_boxplots = []
for i in dfs:
    dfs_for_boxplots = dfs_for_boxplots.append(i["hcho"])

figure = plt.figure()
plt.boxplot(len(range(44),dfs_for_boxplots) #TypeError: list indices must be integers or slices, not str
plt.show()

"""
exit()

Plot6var(pff_all, title)

title = "MAM, no filter"
#pffMAM = pff.loc[(pff["datetime"].dt.month==12)]
#print(pffMAM)
#exit()
pffMAM_17 = pff_nofilter[datetime(2017, 3, 1, 00, 00):datetime(2017, 5, 31, 00, 00)].resample('D').mean() #CHECKED OK
pffMAM_18 = pff_nofilter[datetime(2018, 3, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pffMAM_19 = pff_nofilter[datetime(2019, 3, 1, 00, 00):datetime(2019, 5, 31, 00, 00)].resample('D').mean()
pffMAM_20 = pff_nofilter[datetime(2020, 3, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pffMAM_21 = pff_nofilter[datetime(2021, 3, 1, 00, 00):datetime(2021, 5, 31, 00, 00)].resample('D').mean()
pffMAM = pd.concat([pffMAM_17,pffMAM_18,pffMAM_19,pffMAM_21])
Plot6var(pffMAM, title)

#SUMMER: JJA
title = "JJA, no filter"
pffJJA_17 = pff_nofilter[datetime(2017, 6, 1, 00, 00):datetime(2017, 8, 31, 00, 00)].resample('D').mean()
pffJJA_18 = pff_nofilter[datetime(2018, 6, 1, 00, 00):datetime(2018, 8, 31, 00, 00)].resample('D').mean()
pffJJA_19 = pff_nofilter[datetime(2019, 6, 1, 00, 00):datetime(2019, 8, 31, 00, 00)].resample('D').mean()
pffJJA_20 = pff_nofilter[datetime(2020, 6, 1, 00, 00):datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pffJJA_21 = pff_nofilter[datetime(2021, 6, 1, 00, 00):datetime(2021, 8, 31, 00, 00)].resample('D').mean()
pffJJA = pd.concat([pffJJA_17,pffJJA_18,pffJJA_19,pffJJA_20,pffJJA_21])
Plot6var(pffJJA, title)
#SUMMER: SON
title = "SON, no filter"
pffSON_17 = pff_nofilter[datetime(2017, 9, 1, 00, 00):datetime(2017, 11, 30, 00, 00)].resample('D').mean()
pffSON_18 = pff_nofilter[datetime(2018, 9, 1, 00, 00):datetime(2018, 11, 30, 00, 00)].resample('D').mean()
pffSON_19 = pff_nofilter[datetime(2019, 9, 1, 00, 00):datetime(2019, 11, 30, 00, 00)].resample('D').mean()
pffSON_20 = pff_nofilter[datetime(2020, 9, 1, 00, 00):datetime(2020, 11, 30, 00, 00)].resample('D').mean()
pffSON = pd.concat([pffSON_17,pffSON_18,pffSON_19,pffSON_20])
Plot6var(pffSON, title)
#SUMMER: DJF
title = "DJF, no filter"
pffDJF_17 = pff_nofilter[datetime(2017, 12, 1, 00, 00):datetime(2018, 2, 28, 00, 00)].resample('D').mean()
pffDJF_18 = pff_nofilter[datetime(2018, 12, 1, 00, 00):datetime(2019, 2, 28, 00, 00)].resample('D').mean()
pffDJF_19 = pff_nofilter[datetime(2019, 12, 1, 00, 00):datetime(2020, 2, 29, 00, 00)].resample('D').mean()
pffDJF_20 = pff_nofilter[datetime(2020, 12, 1, 00, 00):datetime(2021, 2, 28, 00, 00)].resample('D').mean()
pffDJF = pd.concat([pffDJF_17,pffDJF_18,pffDJF_19,pffDJF_20])
Plot6var(pffDJF, title)

title = "full year, 90% GR"
#pff5 = pff.dropna()
#print("pff", pff)
#print("after dropna", pff5)
#print(len(pff),len(pff5))
Plot6var(pff, title)
#exit()

title = "MAM, 90% GR"
#pffMAM = pff.loc[(pff["datetime"].dt.month==12)]
#print(pffMAM)
#exit()
pffMAM_17 = pff[March17:datetime(2017, 5, 31, 00, 00)].resample('D').mean()
pffMAM_18 = pff[March18:datetime(2018, 5, 31, 00, 00)].resample('D').mean()
pffMAM_19 = pff[March19:datetime(2019, 5, 31, 00, 00)].resample('D').mean()
pffMAM_20 = pff[March20:datetime(2020, 5, 31, 00, 00)].resample('D').mean()
pffMAM_21 = pff[March21:datetime(2021, 5, 31, 00, 00)].resample('D').mean()
pffMAM = pd.concat([pffMAM_17,pffMAM_18,pffMAM_19,pffMAM_21])
Plot6var(pffMAM, title)
#SUMMER: JJA
title = "JJA, 90% GR"
pffJJA_17 = pff[June17:datetime(2017, 8, 31, 00, 00)].resample('D').mean()
pffJJA_18 = pff[June18:datetime(2018, 8, 31, 00, 00)].resample('D').mean()
pffJJA_19 = pff[June19:datetime(2019, 8, 31, 00, 00)].resample('D').mean()
pffJJA_20 = pff[June20:datetime(2020, 8, 31, 00, 00)].resample('D').mean()
pffJJA_21 = pff[June21:datetime(2021, 8, 31, 00, 00)].resample('D').mean()
pffJJA = pd.concat([pffJJA_17,pffJJA_18,pffJJA_19,pffJJA_20,pffJJA_21])
Plot6var(pffJJA, title)
#SUMMER: SON
title = "SON, 90% GR"
pffSON_17 = pff[Sept17:datetime(2017, 11, 30, 00, 00)].resample('D').mean()
pffSON_18 = pff[Sept18:datetime(2018, 11, 30, 00, 00)].resample('D').mean()
pffSON_19 = pff[Sept19:datetime(2019, 11, 30, 00, 00)].resample('D').mean()
pffSON_20 = pff[Sept20:datetime(2020, 11, 30, 00, 00)].resample('D').mean()
pffSON = pd.concat([pffSON_17,pffSON_18,pffSON_19,pffSON_20])
Plot6var(pffSON, title)
#SUMMER: DJF
title = "DJF, 90% GR"
pffDJF_17 = pff[Dec17:datetime(2018, 2, 28, 00, 00)].resample('D').mean()
pffDJF_18 = pff[Dec18:datetime(2019, 2, 28, 00, 00)].resample('D').mean()
pffDJF_19 = pff[Dec19:datetime(2020, 2, 28, 00, 00)].resample('D').mean()
pffDJF_20 = pff[Dec20:datetime(2021, 2, 28, 00, 00)].resample('D').mean()
pffDJF = pd.concat([pffDJF_17,pffDJF_18,pffDJF_19,pffDJF_20])
Plot6var(pffDJF, title)
#"
#monthley:



#NW episodes
#title = "NW selected episodes, 90% GR"
#pffSPI_spring1 = pff[datetime(2019, 4, 1, 00, 00):datetime(2019, 4, 30, 00, 00)]
#pffSPI_spring2 = pff[datetime(2020, 4, 1, 00, 00):datetime(2019, 5, 31, 00, 00)]
#pffSPI_spring =
#pffNW = pff.loc[(pff['WD'] >=270) & (pff['WD'] <=359)]

#pffNW_1 = pff[datetime(2019, 3, 24, 00, 00):datetime(2019, 3, 29, 00, 00)].resample('D').mean()
#pffNW_2 = pff[datetime(2019, 4, 9, 00, 00):datetime(2019, 4, 16, 00, 00)].resample('D').mean()
#pffNW_3 = pff[datetime(2019, 4, 9, 00, 00):datetime(2019, 4, 16, 00, 00)].resample('D').mean()
#pffDJF_19 = pff[Dec19:datetime(2020, 2, 28, 00, 00)].resample('D').mean()
#pffDJF_20 = pff[Dec20:datetime(2021, 2, 28, 00, 00)].resample('D').mean()
#pffDJF = pd.concat([pffDJF_17,pffDJF_18,pffDJF_19,pffDJF_20])


"""METFILTER"""

pffPC = pff.loc[pff['PC'] == 0]  #CHECKED OK
pffAT = pffPC.loc[(pffPC['AT'] > 15)] #and (pffPC['AT'] < 25)]
#(pffAT)
pffRSS_low = pffAT.loc[pffAT['SM'] <= 0.0] #relative soil moisture RSS sub wWheat (40-100cm)
pffRSS_high = pffAT.loc[pffAT['SM'] > 0.0] #relative soil moisture RSS sub wWheat (40-100cm)
print(pffRSS_low)

#print(len(pffRSS))
#NW
pffNW_low = pffRSS_low.loc[(pffRSS_low['WD'] >=270) & (pffRSS_low['WD'] <=359)]
#pffNW_low = pffNW_low.dropna()
#droppar = ["03","NOx","WD","PC","GR","SIF","SM","AT","PBL"]
print(pffNW_low)
droppar = ["AT"]
try:
    title = "PR=0, GR=90%, ATmax>15, RSS<climate mean"
    #LinearModel(pffNW_low, droppar)
    Plot6var(pffRSS_low, title)
except:
    print("RSS_low empty")
    pass
try:
    title = "PR=0, GR=90%, ATmax>15, RSS>climate mean"
    #LinearModel(pffNW_low, droppar)
    Plot6var(pffRSS_high, title)
except:
    print("RSS_high empty")
    pass
try:
    title = "NW, PR=0, GR=90%, ATmax>15, RSS<climate mean"
    #LinearModel(pffNW_low, droppar)
    Plot6var(pffNW_low, title)
except:
    print("NW_low empty")
    pass

title = "NW, PR=0, GR=90%, ATmax>30, RSS<climate mean"
pffNW_low = pffRSS_low.loc[(pffRSS_low['WD'] >=270) & (pffRSS_low['WD'] <=359)]
pffNW_low_hot = pffNW_low.loc[(pffNW_low['AT'] > 30)] #and (pffPC['AT'] < 25)]
#pffNW_low_hot = pffNW_low_hot.dropna()
#droppar = ["03","NOx","WD","PC","GR","SIF","SM","AT","PBL"]
droppar = ["AT"]
try:
    #LinearModel(pffNW_low_hot, droppar)
    Plot6var(pffNW_low_hot, title)
except:
    print("NW_low_hot empty")
    pass


"""title = "NW, PR=0, GR=90%, ATmax>15, RSS>climate mean" #WD=270°-360°,PC=0,GR>90%,ATmax>10 C°"""
#pffNW_high = pffRSS_high.loc[(pffRSS_high['WD'] >=270) & (pffRSS_high['WD'] <=359)]
#pffNW_high = pffNW_high.dropna()
#try:
#    Plot6var(pffNW_high, title)
#except:
#    print("NW_high empty")
#    pass

#SW
title = "SE, PR=0, GR=90%, ATmax>30, RSS<climate mean"
pffSE_low = pffRSS_low.loc[(pffRSS_low['WD'] >=90) & (pffRSS_low['WD'] <=180)]
pffSE_low_hot = pffSE_low.loc[(pffSE_low['AT'] > 30)] #and (pffPC['AT'] < 25)]
#pffSE_low_hot = pffSE_low_hot.dropna()
try:
    #LinearModel(pffSE_low_hot, droppar)
    Plot6var(pffSE_low_hot, title)
except:
    print("SE_low_hot empty")
    pass

#print("pffAT",pffAT[June19:Sept19])
#print("pffRSS_low",pffRSS_low[June19:Sept19])
#print("pffRSS_high",pffRSS_high[June19:Sept19])
#print("pffNW_low",pffRSS_high[June19:Sept19])
#print("pffSE_low",pffSE_low[June19:Sept19])
#exit()

"""title = "SE, PR=0, GR=90%, ATmax>15&<30, RSS<climate mean"""
#pffSE_low = pffRSS_low.loc[(pffRSS_low['WD'] >=90) & (pffRSS_low['WD'] <=180)]
#pffSE_low_ideal = pffRSS_low.loc[(pffRSS_low['AT'] > 15) & (pffRSS_low['AT'] < 30)]
#pffSE_low_ideal = pffSE_low_ideal.dropna()
#try:
#    LinearModel(pffSE_low_ideal, droppar)
#    Plot6var(pffSE_low_ideal, title)
#except:
#    print("SE_low_ideal empty")
#    pass

title = "SE, PR=0, GR=90%, ATmax>15, RSS<climate mean"
pffSE_low = pffRSS_low.loc[(pffRSS_low['WD'] >=90) & (pffRSS_low['WD'] <=180)]
#pffSE_low = pffSE_low.dropna()
try:
    #LinearModel(pffSE_low, droppar)
    Plot6var(pffSE_low, title)
except:
    print("SE_low empty")
    pass

"""title = "SE, PR=0, GR=90%, ATmax>15, RSS>climate mean" #WD=90°-180°,PC=0,GR>90%,ATmax>10 C°"""
#pffSE_high = pffRSS_high.loc[(pffRSS_high['WD'] >=90) & (pffRSS_high['WD'] <=180)]
#pffSE_high = pffSE_high.dropna()
#try:
#    LinearModel(pffSE_high, droppar)
#    Plot6var(pffSE_high, title)
#except:
#    print("SE_high empty")
#    pass

#SW:MAM
"""title = "MAM, SE, PR=0, GR=90%, ATmax>15, RSS<climate mean"""
#pffSEMAM19 = pffSE_low[March19:June19].resample('D').mean()
#pffSEMAM20 = pffSE_low[March:June].resample('D').mean()
#pffSEMAM = pffSEMAM19.append(pffSEMAM20)
#pffSEMAM = pffSEMAM.dropna()
#Plot6var(pffSEMAM, title)
"""title = "MAM, SE, PR=0, GR=90%, ATmax>15, RSS>climate mean" #WD=90°-180°,PC=0,GR>90%,ATmax>10 C°,"""
#pffSEMAM19 = pffSE_high[March19:June19].resample('D').mean()
#pffSEMAM20 = pffSE_high[March:June].resample('D').mean()
#pffSEMAM = pffSEMAM19.append(pffSEMAM20)
#pffSEMAM = pffSEMAM.dropna()
#Plot6var(pffSEMAM, title)

#SW:JJA
"""title = "JJA, SE,  PR=0, GR=90%, ATmax>15, RSS<climate mean"""
#pffSEJJA19 = pffSE_low[June19:Sept19].resample('D').mean()
#pffSEJJA20 = pffSE_low[June:Sept].resample('D').mean()
#pffSEJJA = pffSEJJA19.append(pffSEJJA20)
#print(pffSEJJA19)
#print(pffSEJJA20)
#print(pffSEJJA)
#pffSEJJA = pffSEJJA.dropna()
#Plot6var(pffSEJJA, title)
"""title = "JJA, SE, PR=0, GR=90%, ATmax>15, RSS>climate mean"""
#pffSEJJA19 = pffSE_high[June19:Sept19].resample('D').mean()
#pffSEJJA20 = pffSE_high[June:Sept].resample('D').mean()
#pffSEJJA = pffSEJJA19.append(pffSEJJA20)
#pffSEJJA = pffSEJJA.dropna()
#print(pffSEJJA)
#try:
#    LinearModel(pffSEJJA, droppar)
#    Plot6var(pffSEJJA, title)
#except:
#    print("SEJJA empty")
#    pass

#SPRING: MAM





