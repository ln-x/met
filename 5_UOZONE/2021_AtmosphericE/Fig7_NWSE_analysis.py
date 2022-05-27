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

yM_m = [0,1,2,3,4,5,6,7,8,9,10,11]
yM = [15,46,74,105,135,166,196,227,258,288,319,349]
yM_ticks = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
yM18 = [15,46,74,105,135,166,196,227,258,288,319]
yM19 = [15,46,74,105,135,166,196,227,258,288]
yM20 = [15,46,74,105,135,166,196,227,258,288,319]
yM21 = [15,46,74,105,135,166,196,227]
start2017 = datetime(2017, 5, 1, 00, 00)
start2018 = datetime(2018, 1, 1, 00, 00)
start2019 = datetime(2019, 1, 1, 00, 00)
start2020 = datetime(2020, 1, 1, 00, 00)
end2020 = datetime(2020, 12, 31, 00, 00)
start2021 = datetime(2021, 1, 1, 00, 00)
end2021 = datetime(2021, 9, 1, 00, 00)

'''READ IN BOKU Metdata'''
BOKUMetData = met.library.BOKUMet_Data.BOKUMet() #10min values
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean, 'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean, 'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailymax = BOKUMetData_hourlymean.resample('D').agg({'DT': np.max, 'AT': np.max, 'RH': np.max, 'GR': np.max, 'WS': np.max,'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})
#JULIAN DAY
BOKUMetData_dailysum['JD'] = (BOKUMetData_dailysum.index)
f = lambda x: datestdtojd(str(x)[:-9])
BOKUMetData_dailysum['JD'] = BOKUMetData_dailysum['JD'].apply(f)

"read in VINDOBONA"

foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))

nw = pd.concat([hcho_dmax,BOKUMetData_dailysum["WD"][datetime(2017,5,1):datetime(2021,8,31)]],axis=1)
nw.columns =['hcho', 'WD']
nw.index.name = 'datetime'
nw =nw.loc[(nw['WD'] >=270) & (nw['WD'] <=359)]

#hcho_dmax_m = hcho_dmax.resample('M').mean()
#hcho_d_m = hcho_d.resample('M').mean()   #TODO switch between all data and nw only
hcho_dmax_nw = nw['hcho']
#hcho_d_m = nw['hcho'].resample('M').mean()

hcho_dmax17 = hcho_dmax[datetime(2017,5,1,0,0):datetime(2017,12,31,0,0)]
hcho_17fill = np.full(shape=120,fill_value=np.NaN)
hcho_dmax17_a = np.append(hcho_17fill, hcho_dmax17)
hcho_dmax18 = hcho_dmax[start2018:datetime(2018,12,31,0,0)]
hcho_dmax19 = hcho_dmax[start2019:datetime(2019,12,31,0,0)]
hcho_dmax20 = hcho_dmax[start2020:datetime(2020,12,31,0,0)]
hcho_dmax21 = hcho_dmax[start2021:end2021]

#print(hcho_dmax17_a,hcho_dmax18,hcho_dmax19,hcho_dmax20,hcho_dmax21)

#hcho_dmax17_m = hcho_dmax17.ffill()
#hcho_dmax17_m= hcho_dmax17_m.resample('W').mean()
#hcho_17fill_m = np.full(shape=4,fill_value=np.NaN)
#hcho_dmax17_a_m = np.append(hcho_17fill_m, hcho_dmax17_m)
hcho_dmax18 = hcho_dmax18.ffill()
hcho_dmax18_m = hcho_dmax18.resample('M').mean()
hcho_dmax19 = hcho_dmax19.ffill()
hcho_dmax19_m = hcho_dmax19.resample('M').mean()
hcho_dmax20 = hcho_dmax20.ffill()
hcho_dmax20_m = hcho_dmax20.resample('M').mean()
hcho_dmax21 = hcho_dmax21.ffill()
hcho_dmax21_m = hcho_dmax21.resample('M').mean()

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

pff = pd.concat([hcho_dmax, BOKUMetData_dailymax["AT"],HighGRdays["GR"],HighGRdays["WD"]],axis=1)
pff.columns =['hcho', 'AT', 'GR', 'WD']

pffNW = pff.loc[(pff['WD'] >=270) & (pff['WD'] <=359)]
pffNW = pffNW.dropna()
pffSE = pff.loc[(pff['WD'] >=90) & (pff['WD'] <=180)]
pffSE = pffSE.dropna()

N=7 #days
atmaxSE_5daymean = np.convolve(pffSE['AT'], np.ones(N)/N, mode='valid')
atmaxNW_5daymean = np.convolve(pffNW['AT'], np.ones(N)/N, mode='valid')
hchomaxSE_5daymean = np.convolve(pffSE['hcho'], np.ones(N)/N, mode='valid')
hchomaxNW_5daymean = np.convolve(pffNW['hcho'], np.ones(N)/N, mode='valid')


Runningmean_5daysSE = pffSE[6:]
Runningmean_5daysSE.insert(1,'AT5d', atmaxSE_5daymean.tolist())
Runningmean_5daysSE.insert(1,'hcho5d', hchomaxSE_5daymean.tolist())
#print(Runningmean_5daysSE['AT5d'])
Runningmean_5daysNW = pffNW[6:]
Runningmean_5daysNW.insert(1,'AT5d', atmaxNW_5daymean.tolist())
Runningmean_5daysNW.insert(1,'hcho5d', hchomaxNW_5daymean.tolist())
#print(Runningmean_5daysNW['AT5d'])
#exit()

pffSE_veg = pffSE.loc[(pffSE.index.month>=4)&(pffSE.index.month<=10)]
pffSE_noveg = pffSE.loc[(pffSE.index.month>=11)|(pffSE.index.month<=3)]
pffNW_veg = pffNW.loc[(pffNW.index.month>=4)&(pffNW.index.month<=10)]
pffNW_noveg = pffNW.loc[(pffNW.index.month>=11)|(pffNW.index.month<=3)]

pff = pff[:datetime(2019,12,31,0,0)]
pff_veg = pff.loc[(pff.index.month>=4)&(pff.index.month<=10)]
pff_veg = pff_veg.dropna()
pff_noveg = pff.loc[(pff.index.month>=11)|(pff.index.month<=3)]
#pff_noveg = pff.loc[(pff.index.month==2)]
pff_noveg = pff_noveg.dropna()
print(pff_veg)

m, b = np.polyfit(pff_noveg['AT'],pff_noveg['hcho'],1)
SRho, Sp = (stats.spearmanr(pff_noveg['AT'], pff_noveg['hcho']))
m_veg, b_veg = np.polyfit(pff_veg['AT'],pff_veg['hcho'],1)
SRho_veg, Sp_veg = (stats.spearmanr(pff_veg['AT'], pff_veg['hcho']))

m_NW, b5_NW = np.polyfit(pffNW['AT'], pffNW['hcho'], 1)
#SRhoNW, SpNW = (stats.spearmanr(pffNW['AT'], pffNW['hcho']))
m_vegNW, b5_vegNW = np.polyfit(pffNW_veg['AT'], pffNW_veg['hcho'], 1)
#SRho_veg, Sp_veg = (stats.spearmanr(pffNW_veg['AT'], pffNW_veg['hcho']))
m_novegNW, b5_novegNW = np.polyfit(pffNW_noveg['AT'], pffNW_noveg['hcho'], 1)
#SRho_noveg, Sp_noveg = (stats.spearmanr(pffNW_noveg['AT'], pffNW_noveg['hcho']))
m_vegSE, b5_vegSE = np.polyfit(pffSE_veg['AT'], pffSE_veg['hcho'], 1)
#SRho_veg, Sp_veg = (stats.spearmanr(pffNW_veg['AT'], pffNW_veg['hcho']))
m_novegSE, b5_novegSE = np.polyfit(pffSE_noveg['AT'], pffSE_noveg['hcho'], 1)

print("slope ALL veg, noveg, NW, veg, noveg", m_veg, m, m_vegNW, m_novegNW)
print("intercept ALL veg, noveg, NW, veg, noveg", b_veg, b, b5_vegNW, b5_novegNW)
print("\n\n")

AT_NW_veg = 22.6918403
AT_SE_veg = 24.787648
AT_diff = 1.98692453
AT_diff_noveg = 2.66448734
HCHO_diff = 1.147235
HCHO_diff_noveg = 0.85987319

print("****")
y_est_veg1 = m_vegNW*20 + b5_vegNW
y_est_veg2 = m_vegNW*21 + b5_vegNW
y_est_perdegC = y_est_veg2-y_est_veg1
print("for NW/VP:", y_est_perdegC, "ppb/degC")
print("Biogenic Part of HCHO: ", y_est_perdegC*AT_diff, "[ppb]")
print("Anthropogenic Part:", HCHO_diff-(y_est_perdegC*AT_diff), "[ppb]")

y_est_veg3 = m_NW*20 + b5_NW
y_est_veg4 = m_NW*21 + b5_NW
y_est_perdegC_2 = y_est_veg3-y_est_veg4
print("for NW/NVP:", y_est_perdegC_2, "ppb/degC")
print("Biogenic Part of HCHO: ", y_est_perdegC_2*AT_diff_noveg, "[ppb]")
print("Anthropogenic Part:", HCHO_diff_noveg-(y_est_perdegC_2*AT_diff_noveg), "[ppb]")

print("****")
y_est_veg1 = m_vegSE*20 + b5_vegSE
y_est_veg2 = m_vegSE*21 + b5_vegSE
y_est_perdegC = y_est_veg2-y_est_veg1
print("for SE/VP:", y_est_perdegC, "ppb/degC")
print("Biogenic Part of HCHO: ", y_est_perdegC*AT_diff, "[ppb]")
print("Anthropogenic Part:", HCHO_diff-(y_est_perdegC*AT_diff), "[ppb]")

y_est_veg3 = m_novegNW*20 + b5_novegNW
y_est_veg4 = m_novegNW*21 + b5_novegNW
y_est_perdegC_2 = y_est_veg3-y_est_veg4
print("for SE/NVP:", y_est_perdegC_2, "ppb/degC")
print("Biogenic Part of HCHO: ", y_est_perdegC_2*AT_diff_noveg, "[ppb]")
print("Anthropogenic Part:", HCHO_diff_noveg-(y_est_perdegC_2*AT_diff_noveg), "[ppb]")

print("****")

y_est_veg1a = m_veg*20 + b_veg
y_est_veg2a = m_veg*21 + b_veg
y_est_perdegCa = y_est_veg2a-y_est_veg1a
print("\nfor all:", y_est_perdegCa, "ppb/degC")
print("Biogenic Part in HCHO: ", y_est_perdegCa*AT_diff, "[ppb]")
print("Anthropogenic Part:", HCHO_diff-(y_est_perdegCa*AT_diff), "[ppb]")
print("****")


fig = plt.figure(figsize=(8, 6), dpi=100)
plt.scatter(pffNW_noveg['AT'], pffNW_noveg['hcho'], color='grey', s=5)
plt.scatter(pffNW_veg['AT'], pffNW_veg['hcho'], color='lightgreen', s=5)
y_est = m_NW * pffNW_noveg['AT'] + b5_NW
y2_est = m_vegNW * pffNW_veg['AT'] + b5_vegNW
plt.plot(pffNW_noveg['AT'], y_est, color='black')
plt.plot(pffNW_veg['AT'], y2_est, color='green')
plt.title('slope_NWnoveg={:.2f} slope_NWveg={:.2f}'.format(m_NW,m_vegNW), fontsize='small')
plt.ylabel("HCHO [ppb]", size="small")
plt.xlabel("AT [C°]", size="small")
plt.show()

print("\n noveg", "intercept:", m, "slope:", b, SRho, Sp)
print("veg","intercept:", m_veg, "slope:", b_veg, SRho_veg, Sp_veg)

print("NWall", m_NW, b5_NW, SRhoNW, SpNW)
print("NWveg", m_vegNW, b5_vegNW, SRho_veg, Sp_veg)
print("NWnoveg", m_novegNW, b5_novegNW, SRho_noveg, Sp_noveg)
#exit()

print("\n all: ")
#print(pffSE,pffNW)
print("AT SE:", pffSE['AT'].mean()," AT NW:", pffNW['AT'].mean()," hcho SE:", pffSE['hcho'].mean(), " hcho NW:", pffNW['hcho'].mean())
print("\n veg: ")
#print(pffSE_veg, pffNW_veg)
print("AT SE:", pffSE_veg['AT'].mean()," AT NW:", pffNW_veg['AT'].mean()," hcho SE:", pffSE_veg['hcho'].mean(), " hcho NW:", pffNW_veg['hcho'].mean())
print("\n noveg:")
#print(pffSE_noveg, pffNW_noveg)
print("AT SE:", pffSE_noveg['AT'].mean()," AT NW:", pffNW_noveg['AT'].mean()," hcho SE:", pffSE_noveg['hcho'].mean(), " hcho NW:", pffNW_noveg['hcho'].mean())


"""FIGURE 7"""
#commonstart = datetime(2017,6,14)
#commonend = datetime(2021,8,12)
start = datetime(2018,1,1)
end = datetime(2020,12,31)

figure = plt.figure
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax1 = plt.gca()
ax3 = plt.subplot(gs[1])
ax3 = plt.gca()
ax1.plot(Runningmean_5daysSE['hcho'][start:end],color='red',label="SE", linewidth=2,linestyle="",marker="o",markersize=5) #pffNW['AT']
ax1.plot(Runningmean_5daysNW['hcho'][start:end],color='blue',label="NW", linewidth=2,linestyle="",marker="o",markersize=5) #pffSE['AT']
ax1.set_ylabel("HCHO [ppb]")
ax3.plot(Runningmean_5daysSE['AT5d'][start:end],color='red',label="SE", linewidth=2,linestyle="",marker="o",markersize=5) #pffNW['AT']
ax3.plot(Runningmean_5daysNW['AT5d'][start:end],color='blue',label="NW", linewidth=2,linestyle="",marker="o",markersize=5) #pffSE['AT']
ax3.set_ylabel("AT [°C]")
ax1.legend(loc='upper right')
#plt.xlabel("time [days]")
plt.show()

