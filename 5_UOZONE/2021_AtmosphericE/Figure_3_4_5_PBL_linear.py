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

#TODO: climatological mean
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
tsif_r = pd.read_csv("/windata/DATA/remote/satellite/TROPOMI/TSIF_743.csv", sep=",")
tsif = tsif_r.set_index(pd.to_datetime(tsif_r['time']))
tsif = tsif.drop(columns=['time'])
#osif_771_r = pd.read_csv("/windata/DATA/remote/satellite/OCO/OSIF_8100_771nm.csv", sep=",")
#osif_771 = osif_771_r.set_index(pd.to_datetime(osif_771_r['time']))
#osif_771 = osif_771.drop(columns=['time'])
osif_757_r = pd.read_csv("/windata/DATA/remote/satellite/OCO2/OSIF_8100_757nm.csv", sep=",")
osif_757 = osif_757_r.set_index(pd.to_datetime(osif_757_r['time']))
osif_757 = osif_757.drop(columns=['time'])


'''READ IN CAMX PBL'''
#starttime = datetime(2020, 1, 1, 0, 00)
#wrfc_time_construct = np.array([starttime + timedelta(hours=i) for i in range(6481)])
#camx3_y_vie_is = 76  #for Wien Innere Stadt 1,76,181
#camx3_x_vie_is = 181 #for Wien Innere Stadt

#i = 'zmla'
#file = "/windata/DATA/models/boku/CAMX/BOKU2020/4_CAMXoutput/BOKU2020_BASE_WRFchem9_202001-09_zmla.nc"
#f = Dataset(file, mode='r')
#par = f.variables[i][:, :, :]
#par1 = pd.DataFrame(par[:, 76, 181], index=wrfc_time_construct)
#globals()[f"camx3_2020_{i}_d"] = par1.resample('D').mean()
#globals()[f"camx3_2020_{i}_dmax"] = par1.resample('D').max()
#par1.columns = ["zmla"]
#par1 = par1.resample('D').max()

'''READ IN CEILOMETER DATA'''
file_pbl = "/windata/DATA/obs_point/met/ZAMG/Ceilometer/MH_Wien_Hohe_Warte_20170101_20201231.csv"
pbl = pd.read_csv(file_pbl,skiprows=2, parse_dates={'datetime':[0,1]})
pbl.columns = ['datetime','PBL']  #UTC
pbl = pbl.set_index(pbl['datetime'])
pbl = pbl.drop(columns=['datetime'])
pbl = pbl.resample('D').max()
#print(pbl)

'''TIMESLICES'''
start = datetime(2019, 1, 1, 00, 00)
end = datetime(2020, 12, 31, 00, 00)
March19 = datetime(2019, 3, 1, 00, 00) #JD 2020=92
June19 = datetime(2019, 6, 1, 00, 00)  #JD 2020=183
Sept19 = datetime(2019, 9, 1, 00, 00)  #JD 2020=183
March = datetime(2020, 3, 1, 00, 00) #JD 2020=92
June = datetime(2020, 6, 1, 00, 00)  #JD 2020=183
Sept = datetime(2020, 9, 1, 00, 00)  #JD 2020=183

'''
Plotting
'''
nox_1990_2020_da = nox_1990_2020_da.resample('D').mean()
o3_1990_2020_da = o3_1990_2020_da.resample('D').mean()

#VERS5 including GR filter > 90%, Ceilometer PBL, gliding mean for AT and GR ??Runningmean_5d['RSS5d']
#pff = pd.concat([hcho_dmax,rss_sub["RSS_sub_grass"],Runningmean_5d['AT5d'],Runningmean_5d['GR5d'],tsif,
#                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],HighGRdays["WD"],HighGRdays["PC"],pbl["PBL"]], axis=1)

#VERS4 including GR filter > 90%, Ceilometer PBL
pff = pd.concat([hcho_dmax,rss_sub["RSS_sub_grass"],BOKUMetData_dailymax["AT"],HighGRdays["GR"],tsif,
                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],HighGRdays["WD"],HighGRdays["PC"],pbl["PBL"]],axis=1)
#VERS3 including GR filter > 90%, Ceilometer PBL, VWC
#pff = pd.concat([hcho_dmax,vwc_sub['VWC_sub_wWheat'],BOKUMetData_dailymax["AT"],HighGRdays["GR"],tsif,
#                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],HighGRdays["WD"],HighGRdays["PC"],pbl["PBL"]],axis=1)

#VERS2 including GR filter > 90%, CAMX PBL
#pff = pd.concat([hcho_dmax,rss_sub["RSS_sub_wWheat"],BOKUMetData_dailymax["AT"],HighGRdays["GR"],tsif,
#                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],HighGRdays["WD"],HighGRdays["PC"],par1["zmla"]],axis=1)
#VERS1 without GR filter
#pff = pd.concat([hcho_dmax,rss_sub["RSS_sub_wWheat"],BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"],tsif,
#                o3_1990_2020_da["AT9STEF"],nox_1990_2020_da["AT9STEF"],BOKUMetData_dailysum["WD"],BOKUMetData_dailysum["PC"],par1["zmla"]],axis=1)

pff.columns =['hcho', 'SM', 'AT', 'GR', 'SIF', 'O3','NOx','WD','PC','PBL']
pff = pff.dropna()
pff = pff.resample('W').mean()
print(pff)
#TODO: nox_1990_2020_da["AT9STEF"],'NOx' procudes additional timesteps (1:00 instead of 0:00) which makes the boolean filters fail
#start_ph = datetime(2020, 1, 1, 00, 00)
#end_ph = datetime(2020, 8, 31, 00, 00)
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
    print(droppar)
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
    print(X.columns)
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
    idx = np.isfinite(x5) & np.isfinite(y5)
    m5, b5 = np.polyfit(x5[idx], y5[idx], 1)
    R_AT = (stats.spearmanr(x5[idx], y5[idx]))[0]
    idx = np.isfinite(x5_GR) & np.isfinite(y5)
    m5GR, b5GR = np.polyfit(x5_GR[idx], y5[idx], 1)
    R_GR = (stats.spearmanr(x5_GR[idx], y5[idx]))[0]
    idx = np.isfinite(x5_SM) & np.isfinite(y5)
    m5SM, b5SM = np.polyfit(x5_SM[idx], y5[idx], 1)
    R_SM = (stats.spearmanr(x5_SM[idx], y5[idx]))[0]
    idx = np.isfinite(x5_SIF) & np.isfinite(y5)
    m5SIF, b5SIF = np.polyfit(x5_SIF[idx], y5[idx], 1)
    R_SIF = (stats.spearmanr(x5_SIF[idx], y5[idx]))[0]
    idx = np.isfinite(x5_NOx) & np.isfinite(y5)
    m5NOx, b5NOx = np.polyfit(x5_NOx[idx], y5[idx], 1)
    R_NOX = (stats.spearmanr(x5_NOx[idx], y5[idx]))[0]
    idx = np.isfinite(x5_O3) & np.isfinite(y5)
    m5O3, b5O3 = np.polyfit(x5_O3[idx], y5[idx], 1)
    R_O3 = (stats.spearmanr(x5_O3[idx], y5[idx]))[0]
    idx = np.isfinite(x5_PBL) & np.isfinite(y5)
    m5PBL, b5PBL = np.polyfit(x5_PBL[idx], y5[idx], 1)
    R_PBL = (stats.spearmanr(x5_PBL[idx], y5[idx]))[0]
    #print(R_AT, R_GR, R_SM, R_SIF, R_NOX, R_O3)
    R2_AT, R2_GR, R2_SM, R2_SIF, R2_NOX, R2_O3 = R_AT ** 2, R_GR ** 2, R_SM ** 2, R_SIF ** 2, R_NOX ** 2, R_O3 ** 2
    #print(R2_AT, R2_GR, R2_SM, R2_SIF, R2_NOX, R2_O3)
    # -0.11468772201686629 0.12327935222672066 0.26591170630878136 0.04979757085020243 -0.21842105263157893 0.12834008097165991
    # 0.013153273581417997 0.015197798685439858 0.07070903555204759 0.0024797980625809305 0.04770775623268697 0.016471176383812222
    n = len(y5)
    a = 0
    fig, axes = plt.subplots(nrows=1, ncols=7, figsize=(8, 6), dpi=100)
    fig.suptitle(title+",n={}".format(n), fontsize="small")
    ax0, ax1, ax2, ax3, ax4, ax5, ax6 = axes.flatten()
    ax0.scatter(x5[a:], y5[a:], color='violet')
    ax0.plot(x5, m5 * x5 + b5, color='red')
    ax0.set_ylabel("HCHO [ppb]", size="small")
    ax0.set_xlabel("air temp [C°]", size="small")
    ax0.set_title('$R={:.2f}$'.format(R_AT), fontsize='small')
    ax1.scatter(x5_GR[a:], y5[a:], color='violet')
    ax1.plot(x5_GR, m5GR * x5_GR + b5GR, color='red')
    ax1.set_xlabel(r"GR [$Wm⁻²$]", size="medium")
    ax1.set_title('$R={:.2f}$'.format(R_GR), fontsize='small')
    ax2.scatter(x5_SM[a:], y5[a:], color='violet')
    ax2.plot(x5_SM, m5SM * x5_SM + b5SM, color='red')
    # ax2.set_xlabel("SM [$m^3$$m^(-3)$]", size="medium")
    ax2.set_xlabel("RSS [0-1]", size="medium")
    ax2.set_title('$R={:.2f}$'.format(R_SM), fontsize='small')
    ax3.scatter(x5_SIF[a:], y5[a:], color='violet')
    ax3.plot(x5_SIF, m5SIF * x5_SIF + b5SIF, color='red')
    ax3.set_xlabel(r"SIF [mWm⁻²sr⁻¹nm⁻¹]", size="medium")
    ax3.set_title('$R={:.2f}$'.format(R_SIF), fontsize='small')
    ax4.scatter(x5_NOx[a:], y5[a:], color='violet')
    ax4.plot(x5_NOx, m5NOx * x5_NOx + b5NOx, color='red')
    ax4.set_xlabel("NOx [ppb]", size="medium")
    ax4.set_title('$R={:.2f}$'.format(R_NOX), fontsize='small')
    ax5.scatter(x5_O3[a:], y5[a:], color='violet')
    ax5.plot(x5_O3, m5O3 * x5_O3 + b5O3, color='red')
    ax5.set_xlabel("O3 [ppb]", size="medium")
    ax5.set_title('$R={:.2f}$'.format(R_O3), fontsize='small')
    ax6.scatter(x5_PBL[a:], y5[a:], color='violet')
    ax6.plot(x5_PBL, m5PBL * x5_PBL + b5PBL, color='red')
    ax6.set_xlabel("PBL [m]", size="medium")
    ax6.set_title('$R={:.2f}$'.format(R_O3), fontsize='small')
    fig.tight_layout()
    plt.savefig("/home/heidit/Downloads/"+title+".jpg")
    plt.show()

    """
    #scatter histograms
    y = y5[a:]
    for i in [x5, x5_GR, x5_SM, x5_SIF, x5_NOx, x5_O3]:
        x = i[a:]
        # definitions for the axes
        left, width = 0.1, 0.65
        bottom, height = 0.1, 0.65
        spacing = 0.005
        rect_scatter = [left, bottom, width, height]
        rect_histx = [left, bottom + height + spacing, width, 0.2]
        rect_histy = [left + width + spacing, bottom, 0.2, height]
        # start with a square Figure
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_axes(rect_scatter)
        ax_histx = fig.add_axes(rect_histx, sharex=ax)
        ax_histy = fig.add_axes(rect_histy, sharey=ax)
        # use the previously defined function
        scatter_hist(x, y, ax, ax_histx, ax_histy)
        plt.show()
    """

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

"METFILTER"
pffPC = pff.loc[pff['PC'] == 0]
print(len(pffPC))
pffAT = pffPC.loc[(pffPC['AT'] > 15)] #and (pffPC['AT'] < 25)]
print(len(pffAT))
pffRSS_low = pffAT.loc[pffAT['SM'] <= 0.5] #relative soil moisture RSS sub wWheat (40-100cm)
pffRSS_high = pffAT.loc[pffAT['SM'] > 0.5] #relative soil moisture RSS sub wWheat (40-100cm)
#print(len(pffRSS))
#NW
title = "NW, metfilter, RSS<0.5" #WD=270°-360°,PC=0,GR>90%,ATmax>10 C°"
pffNW_low = pffRSS_low.loc[(pffRSS_low['WD'] >=270) & (pffRSS_low['WD'] <=359)]
pffNW_low = pffNW_low.dropna()
#droppar = ["03","NOx","WD","PC","GR","SIF","SM","AT","PBL"]
droppar = ["AT"]
try:
    LinearModel(pffNW_low, droppar)
    Plot6var(pffNW_low, title)

except:
    print("NW_low empty")
    pass
title = "NW, metfilter, RSS>0.5" #WD=270°-360°,PC=0,GR>90%,ATmax>10 C°"
pffNW_high = pffRSS_high.loc[(pffRSS_high['WD'] >=270) & (pffRSS_high['WD'] <=359)]
pffNW_high = pffNW_high.dropna()
try:
    Plot6var(pffNW_high, title)
except:
    print("NW_high empty")
    pass
#SW
title = "SE, metfilter, RSS<0.5" #WD=90°-180°,PC=0,GR>90%,ATmax>10 C°
pffSE_low = pffRSS_low.loc[(pffRSS_low['WD'] >=90) & (pffRSS_low['WD'] <=180)]
pffSE_low = pffSE_low.dropna()
try:
    LinearModel(pffSE_low, droppar)
    Plot6var(pffSE_low, title)
except:
    print("SE_low empty")
    pass

title = "SE, metfilter, RSS>0.5" #WD=90°-180°,PC=0,GR>90%,ATmax>10 C°
pffSE_high = pffRSS_high.loc[(pffRSS_high['WD'] >=90) & (pffRSS_high['WD'] <=180)]
pffSE_high = pffSE_high.dropna()
try:
    LinearModel(pffSE_high, droppar)
    Plot6var(pffSE_high, title)
except:
    print("SE_high empty")
    pass

#SW:MAM
title = "MAM, SE, metfilter, RSS<0.5" #WD=90°-180°,PC=0,GR>90%,ATmax>10 C°,
pffSEMAM19 = pffSE_low[March19:June19].resample('D').mean()
pffSEMAM20 = pffSE_low[March:June].resample('D').mean()
pffSEMAM = pffSEMAM19.append(pffSEMAM20)
pffSEMAM = pffSEMAM.dropna()
#Plot6var(pffSEMAM, title)

title = "MAM, SE, metfilter, RSS>0.5" #WD=90°-180°,PC=0,GR>90%,ATmax>10 C°,
pffSEMAM19 = pffSE_high[March19:June19].resample('D').mean()
pffSEMAM20 = pffSE_high[March:June].resample('D').mean()
pffSEMAM = pffSEMAM19.append(pffSEMAM20)
pffSEMAM = pffSEMAM.dropna()
#Plot6var(pffSEMAM, title)

#SW:JJA
title = "JJA, SE, metfilter, RSS<0.5" #WD=90°-180°,PC=0,GR>90%,ATmax>10 C°
pffSEJJA19 = pffSE_low[June19:Sept19].resample('D').mean()
pffSEJJA20 = pffSE_low[June:Sept].resample('D').mean()
pffSEJJA = pffSEJJA19.append(pffSEJJA20)
print(pffSEJJA19)
print(pffSEJJA20)
print(pffSEJJA)
pffSEJJA = pffSEJJA.dropna()
Plot6var(pffSEJJA, title)

title = "JJA, SE, metfilter, RSS>0.5" #WD=90°-180°,PC=0,GR>90%,ATmax>10 C°
pffSEJJA19 = pffSE_high[June19:Sept19].resample('D').mean()
pffSEJJA20 = pffSE_high[June:Sept].resample('D').mean()
pffSEJJA = pffSEJJA19.append(pffSEJJA20)
pffSEJJA = pffSEJJA.dropna()
print(pffSEJJA)
try:
    LinearModel(pffSEJJA, droppar)
    Plot6var(pffSEJJA, title)
except:
    print("SEJJA empty")
    pass

#SPRING: MAM
title = "MAM, no filter"
pff5 = pff[March19:June19].resample('D').mean()
pff5_1 = pff[March:June].resample('D').mean()
pff5 = pff5.append(pff5_1)
pffMAM = pff5.dropna()
Plot6var(pffMAM, title)
#SUMMER: JJA
title = "JJA, no filter"
pff5 = pff[June19:Sept19].resample('D').mean()
pff5_1 = pff[June:Sept].resample('D').mean()
pff5 = pff5.append(pff5_1)
pffJJA = pff5.dropna()
Plot6var(pffJJA, title)
#FULL PERIOD
title = "full year, no filter" #1.1.2019 -31.12.2020
pff5 = pff.dropna()
Plot6var(pff5, title)




