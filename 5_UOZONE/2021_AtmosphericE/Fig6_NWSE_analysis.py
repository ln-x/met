import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from scipy import stats
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVindobona_Filter_fullperiod
from met.library import ReadinVindobona_Glyoxal
import matplotlib.gridspec as gridspec

from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits import axisartist
import matplotlib.pyplot as plt


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
#print(HighGRdays[datetime(2018,1,1):])

"read in VINDOBONA"
foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))

data = pd.concat([hcho_dmax,BOKUMetData_dailymax["AT"], BOKUMetData_dailysum["WD"], HighGRdays["GR"]],axis=1)
data.columns =['hcho', 'AT', 'WD', 'GRhigh']
data = data[datetime(2018,1,1):datetime(2020,12,31)]
data.index.name = 'datetime'
data = data.dropna(subset=['GRhigh'])
nw =data.loc[(data['WD'] >=270) & (data['WD'] <=359)]
nw = nw.dropna()
se = data.loc[(data['WD'] >=90) & (data['WD'] <=180)]
se = se.dropna()

pffSE_veg = se.loc[(se.index.month>=4)&(se.index.month<=10)]
pffSE_noveg = se.loc[(se.index.month>=11)|(se.index.month<=3)]
pffNW_veg = nw.loc[(nw.index.month>=4)&(nw.index.month<=10)]
pffNW_noveg = nw.loc[(nw.index.month>=11)|(nw.index.month<=3)]

m_vegNW, b5_vegNW = np.polyfit(pffNW_veg['AT'], pffNW_veg['hcho'], 1)
SRho_vegNW, Sp_vegNW = (stats.spearmanr(pffNW_veg['AT'], pffNW_veg['hcho']))

m_novegNW, b5_novegNW = np.polyfit(pffNW_noveg['AT'], pffNW_noveg['hcho'], 1)
SRho_novegNW, Sp_novegNW = (stats.spearmanr(pffNW_noveg['AT'], pffNW_noveg['hcho']))

m_vegSE, b5_vegSE = np.polyfit(pffSE_veg['AT'], pffSE_veg['hcho'], 1)
SRho_vegSE, Sp_vegSE = (stats.spearmanr(pffSE_veg['AT'], pffSE_veg['hcho']))

m_novegSE, b5_novegSE = np.polyfit(pffSE_noveg['AT'], pffSE_noveg['hcho'], 1)
SRho_novegSE, Sp_novegSE = (stats.spearmanr(pffSE_noveg['AT'], pffSE_noveg['hcho']))

#print("slope NW, veg, noveg",  m_vegNW, m_novegNW)
#print("intercept NW, veg, noveg", b5_vegNW, b5_novegNW)
#print("\n\n")

AT_diff = pffSE_veg["AT"].mean() - pffNW_veg["AT"].mean() #1.98692453; #AT_NW_veg = 22.6918403, AT_SE_veg = 24.787648
AT_diff_noveg = pffSE_noveg["AT"].mean() - pffNW_noveg["AT"].mean() #2.66448734

HCHO_diff = pffSE_veg["hcho"].mean() - pffNW_veg["hcho"].mean() #1.147235
HCHO_diff_noveg = pffSE_noveg["hcho"].mean() - pffNW_noveg["hcho"].mean() #0.85987319

print("****")
y_est_veg1 = m_vegNW*20 + b5_vegNW
y_est_veg2 = m_vegNW*21 + b5_vegNW
y_est_perdegC = y_est_veg2-y_est_veg1
print("for NW/VP:", y_est_perdegC, "ppb/degC")
print("AT (diff to SE):", AT_diff, "hcho (diff to SE):", HCHO_diff) #pffNW_veg['AT'].mean(),pffNW_veg['hcho'].mean(),
print("temperature dependent rise:", y_est_perdegC*AT_diff, "[ppb]")
print("remaining difference (antrop?):", HCHO_diff-(y_est_perdegC*AT_diff), "[ppb]")

y_est_veg3 = m_novegNW*20 + b5_novegNW
y_est_veg4 = m_novegNW*21 + b5_novegNW
y_est_perdegC_2 = y_est_veg4-y_est_veg3
print("for NW/NVP:", y_est_perdegC_2, "ppb/degC")
print("AT (mean,diff to SE):", pffNW_noveg['AT'].mean(), AT_diff_noveg, "hcho (mean,diff to SE):", pffNW_noveg['hcho'].mean(), HCHO_diff_noveg)
print("temperature dependent rise:", y_est_perdegC_2*AT_diff_noveg, "[ppb]")
print("remaining difference (antrop?):", HCHO_diff_noveg-(y_est_perdegC_2*AT_diff_noveg), "[ppb]")

print("****")
y_est_veg1 = m_vegSE*20 + b5_vegSE
y_est_veg2 = m_vegSE*21 + b5_vegSE
y_est_perdegC = y_est_veg2-y_est_veg1
print("for SE/VP:", y_est_perdegC, "ppb/degC")
print("AT SE:", pffSE_veg['AT'].mean()," hcho SE:", pffSE_veg['hcho'].mean())
print("temperature dependent rise:", y_est_perdegC*AT_diff, "[ppb]")
print("remaining difference (antrop?):", HCHO_diff-(y_est_perdegC*AT_diff), "[ppb]")

y_est_veg3 = m_novegSE*20 + b5_novegSE
y_est_veg4 = m_novegSE*21 + b5_novegSE
y_est_perdegC_2 = y_est_veg4-y_est_veg3
print("for SE/NVP:", y_est_perdegC_2, "ppb/degC")
print("AT SE:", pffSE_noveg['AT'].mean()," hcho SE:", pffSE_noveg['hcho'].mean())
print("temperature dependent rise:", y_est_perdegC_2*AT_diff_noveg, "[ppb]")
print("remaining difference (antrop?):", HCHO_diff_noveg-(y_est_perdegC_2*AT_diff_noveg), "[ppb]")

print("****")
fig = plt.figure(figsize=(8, 6), dpi=100)
plt.scatter(pffNW_veg['AT'], pffNW_veg['hcho'], color='blue', s=5, label="NW_VP")
plt.scatter(pffNW_noveg['AT'], pffNW_noveg['hcho'], color='powderblue', s=5, label="NW_NVP")
plt.scatter(pffSE_veg['AT'], pffSE_veg['hcho'], color='red', s=5, label="SE_VP")
plt.scatter(pffSE_noveg['AT'], pffSE_noveg['hcho'], color='salmon', s=5, label="SE_NOVP")

y_est = m_novegNW * pffNW_noveg['AT'] + b5_novegNW
y2_est = m_vegNW * pffNW_veg['AT'] + b5_vegNW
ySE_est = m_novegSE * pffSE_noveg['AT'] + b5_novegSE
y2SE_est = m_vegSE * pffSE_veg['AT'] + b5_vegSE

#Absolute Mean Error
AME_NWveg = np.mean(np.abs(pffNW_veg['hcho'] - y2_est))
AME_SEveg = np.mean(np.abs(pffSE_veg['hcho'] - y2SE_est))

print("Absolute Mean Error NW/SE:", AME_NWveg, AME_SEveg)
#(Absolute) variance of residual Error
var_absNW = np.var(np.abs(pffNW_veg['hcho'] - y2_est))
var_absSE = np.var(np.abs(pffSE_veg['hcho'] - y2SE_est))
#var = np.var(y_true - y_pred)
print("Absolute variance of Error NW/SE:", var_absNW, var_absSE)

plt.plot(pffNW_noveg['AT'], y_est, color='powderblue',linewidth="0.5")
plt.plot(pffNW_veg['AT'], y2_est, color='blue',linewidth="0.5")
plt.plot(pffSE_noveg['AT'], ySE_est, color='salmon',linewidth="0.5")
plt.plot(pffSE_veg['AT'], y2SE_est, color='red',linewidth="0.5")
#plt.title('SRho: NW_veg={:.2f}, NW_noveg={:.2f}, SE_veg={:.2f}, SE_noveg={:.2f}'.format(SRho_vegNW,SRho_novegNW,SRho_vegSE,SRho_novegSE), fontsize='small')
plt.ylabel("HCHO [ppb]", size="small")
plt.xlabel("AT [C°]", size="small")
plt.legend()
plt.show()

"""FIGURE 7"""
N=7 #days
atmaxSE_xdaymean = np.convolve(se['AT'], np.ones(N)/N, mode='valid')
atmaxNW_xdaymean = np.convolve(nw['AT'], np.ones(N)/N, mode='valid')
hchomaxSE_xdaymean = np.convolve(se['hcho'], np.ones(N)/N, mode='valid')
hchomaxNW_xdaymean = np.convolve(nw['hcho'], np.ones(N)/N, mode='valid')

mean_SE = se[6:]
mean_SE.insert(1,'ATxd', atmaxSE_xdaymean.tolist())
mean_SE.insert(1,'hchoxd', hchomaxSE_xdaymean.tolist())
mean_NW = nw[6:]
mean_NW.insert(1,'ATxd', atmaxNW_xdaymean.tolist())
mean_NW.insert(1,'hchoxd', hchomaxNW_xdaymean.tolist())

figure = plt.figure
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax1 = plt.gca()
ax3 = plt.subplot(gs[1])
ax3 = plt.gca()
ax1.plot(mean_SE['hcho'],color='red',label="SE", linewidth=2,linestyle="",marker="o",markersize=5)
ax1.plot(mean_NW['hcho'],color='blue',label="NW", linewidth=2,linestyle="",marker="o",markersize=5)
ax1.set_ylabel("HCHO [ppb]")
ax3.plot(mean_SE['ATxd'],color='red',label="SE", linewidth=2,linestyle="",marker="o",markersize=5)
ax3.plot(mean_NW['ATxd'],color='blue',label="NW", linewidth=2,linestyle="",marker="o",markersize=5)
ax3.set_ylabel("AT [°C]")
ax1.legend(loc='upper right')
plt.show()

