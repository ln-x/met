# -*- coding: utf-8 -*-
__author__ = 'lnx'
# evaluate an lasso regression model on the dataset
from numpy import mean
from numpy import std
from numpy import absolute
from numpy import arange
#from matplotlib.pyplot import semilogx
from sklearn.linear_model import LassoCV
from sklearn.linear_model import LassoLarsCV
from pandas import read_csv
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library import ReadinVindobona_Filter_fullperiod
import sys

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

#TSIF_743
tsif_r = pd.read_csv("/windata/DATA/remote/satellite/TROPOMI/TSIF_743_LAT48_28_LON16_23.csv", sep=",")
tsif = tsif_r.set_index(pd.to_datetime(tsif_r['time']))
tsif = tsif.drop(columns=['time'])
tsif.columns = ['SIF']

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
                o3_1990_2020_da["AT9STEF"],BOKUMetData_dailysum["WD"],BOKUMetData_dailysum["PC"],pbl["PBL"]], axis=1)
pff_full.columns = ['hcho', 'vpd', 'RSSg', 'RSSw', 'AT', 'GR', 'GRhigh', 'SIF', 'O3','WD','PC','PBL']
pff_clear = pff_full.dropna(subset=['GRhigh'])
#print(pff_clear)
pff_clear2 = pff_clear.loc[pff_clear["GR"] >= 4500]
pff_clear2_o3high = pff_clear2.loc[pff_clear2["O3"] > 100]
pff_clear2_o3low = pff_clear2.loc[pff_clear2["O3"] <= 100]
pff_clear2_o3high_NW = pff_clear2_o3high.loc[(pff_clear2_o3high['WD'] >=270) & (pff_clear2_o3high['WD'] <=360)]
pff_clear2_o3high_SE = pff_clear2_o3high.loc[(pff_clear2_o3high['WD'] >=90) & (pff_clear2_o3high['WD'] <=180)]
pff_weekly_rss_clear = pff_clear.resample("W").mean()

def LASSO(df, name):
    #df = df.dropna()
    # FROM: https://www.statology.org/lasso-regression-in-python/
    X = df[['vpd', 'RSSg', 'RSSw', 'AT', 'GR', 'GRhigh', 'SIF', 'O3', 'WD', 'PC', 'PBL']]
    y = df['hcho']
    print(X.head(),y.head())
    #define cross-validation method to evaluate model
    cv = RepeatedKFold(n_splits=5, n_repeats=10, random_state=0) #n_splits= number of folds
    #define model
    model = LassoCV(alphas=arange(0, 1, 0.01), cv=cv, n_jobs=-1)
    #fit model
    model.fit(X, y)
    print(name)
    print(np.around(model.coef_,decimals=5))
    #display lambda that produced the lowest test MSE
    print(model.alpha_)
    """
    figure = plt.figure
    #print(model.mse_path_)
    plt.semilogx(model.alphas_, model.mse_path_, ":")
    plt.plot(
        model.alphas_ ,
        model.mse_path_.mean(axis=-1),
        "k",
        label="Average across the folds",
        linewidth=2,
    )
    plt.axvline(
    model.alpha_, linestyle="--", color="k", label="alpha: CV estimate"
    )
    plt.legend()
    plt.xlabel("alphas")
    plt.ylabel("Mean square error")
    plt.title("Mean square error on each fold")
    plt.axis("tight")
    plt.show()
    #ymin, ymax = 50000, 250000
    #plt.ylim(ymin, ymax);
    """
    #Use best value for our final model:
    lasso_best = Lasso(alpha=model.alpha_)

df_full = pff_full[datetime(2018,1,1):datetime(2020,12,31)]
df_full = df_full.dropna()
LASSO(df_full,"full") #[ 4.4673e-01 -0.0000e+00 -0.0000e+00  4.8780e-02 -1.2000e-04 -0.0000e+00 5.1780e-02  1.5410e-02 -4.1500e-03  3.2000e-04 -4.2000e-04]

df_NW = df_full.loc[(df_full['WD'] >=270) & (df_full['WD'] <=360)]
#LASSO(df_NW,"full_NW")
df_MAM18 = df_full[datetime(2018,3,1):datetime(2018,5,31)]
np.set_printoptions(threshold=sys.maxsize)
print(df_MAM18)
LASSO(df_MAM18,"MAM18_NW")

np.set_printoptions(suppress=True)  #toggle on and off scientific notation during printing

df_MAM20 = df_NW[datetime(2020,3,1):datetime(2020,5,31)]
LASSO(df_MAM20,"MAM20_NW")  #[ 5.544e-01  5.019e-02 -1.980e-03  1.128e-02 -3.000e-05  0.000e+00  -2.917e-02  3.770e-03  3.620e-03 -4.010e-03  1.700e-04]
df_JJA20 = df_NW[datetime(2020,6,1):datetime(2020,8,31)]
LASSO(df_JJA20,"JJA20_NW")  #[-0. 0. 0. 0.20662 -0.00022 -0. 0. -0.00023  0.01222 -0. -0.0003 ]
df_JJA19 = df_NW[datetime(2019,6,1):datetime(2019,8,31)]
LASSO(df_JJA19,"JJA19_NW") #[-0.0000e+00  0.0000e+00  0.0000e+00  1.6502e-01  9.0000e-05  0.0000e+00 -0.0000e+00  2.2550e-02  1.2300e-02 -1.8700e-03 -1.0000e-05]

#df_MAM18 = df_full[datetime(2018,3,1):datetime(2018,5,31)]
#LASSO(df_MAM18,"MAM18")
#df_MAM20 = df_full[datetime(2020,3,1):datetime(2020,5,31)]
#LASSO(df_MAM20,"MAM20")
#df_JJA20 = df_full[datetime(2020,6,1):datetime(2020,8,31)]
#LASSO(df_JJA20,"JJA20")
#df_JJA19 = df_full[datetime(2019,6,1):datetime(2019,8,31)]
#LASSO(df_JJA19,"JJA19")


exit()
#FROM: https://machinelearningmastery.com/lasso-regression-with-python/
data = df.values
X, y = data[:, :-1], data[:, -1]
# define model
model = Lasso(alpha=1.0)
# define model evaluation method
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
# evaluate model

scores = cross_val_score(model, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
# force scores to be positive
scores = absolute(scores)
print('Mean MAE: %.3f (%.3f)' % (mean(scores), std(scores)))