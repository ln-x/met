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
#print(hcho_dmax17_m, hcho_dmax18_m,hcho_dmax19_m,hcho_dmax20_m,hcho_dmax21_m)

#print(hcho_dmax17, hcho_dmax18_m, hcho_dmax19_m, hcho_dmax20_m)


""" FIGURE 8 """

print(hcho_dmax18, hcho_dmax19, hcho_dmax20)

figure = plt.figure
#plt.plot(range(len(hcho_dmax17_a_m)),hcho_dmax18_m, color='purple', linestyle="-", marker="x", label="2017")
plt.plot(range(len(hcho_dmax18_m)),hcho_dmax18_m, color='blue', linestyle="-", marker="x", label="2018")
plt.plot(range(len(hcho_dmax19_m)),hcho_dmax19_m, color='green', linestyle="-", marker="x",label="2019")
plt.plot(range(len(hcho_dmax20_m)),hcho_dmax20_m, color='orange', linestyle="-", marker="x",label="2020")#
#plt.plot(yM21,hcho_dmax21_m, color='red', linewidth=1, marker="x",label="2021")
plt.title("NW days")
plt.grid(True)
plt.xticks(yM_m, yM_ticks)
plt.xlabel("months")
plt.ylabel("hcho [ppb]")
plt.legend()
plt.show()
exit()

figure = plt.figure
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
#plt.title("")
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax1.plot(range(len(hcho_dmax18_m)),hcho_dmax18_m, color='blue', linestyle="-", marker="x", label="2018")
ax1.plot(range(len(hcho_dmax19_m)),hcho_dmax19_m, color='green', linestyle="-", marker="x",label="2019")
ax1.plot(range(len(hcho_dmax20_m)),hcho_dmax20_m, color='orange', linestyle="-", marker="x",label="2020")
#plt.plot(yM21,hcho_dmax21_m, color='red', linewidth=1, marker="x",label="2021")
plt.title("NW days")
ax1.grid(True)
ax2.grid(True)
plt.xticks(yM, yM_ticks)
#ax2.plot(range(len(hcho_dmax20_m)),hcho_dmax20_m["hcho"]-hcho_dmax19_m["hcho"], color='green', linewidth=1, marker="x",label="2020-19")
#ax2.plot(range(len(hcho_dmax20_m)),hcho_dmax20_m-hcho_dmax18_m, color='blue', linewidth=1, marker="x",label="2020-18")
plt.xlabel("days")
plt.ylabel("hcho [ppb]")
plt.legend()
plt.show()

exit()

figure = plt.figure
ax1 = plt.gca()
ax2 = ax1.twinx()
#ax1.plot(pffNW['AT'],color='powderblue',label="NW AT_max", linewidth=2)
#ax1.plot(pffSE['AT'],color='peachpuff',label="SE AT_max", linewidth=2)
#ax1.plot(pffKNW['AT'],color='lightblue',label="NW AT_max", linestyle="-", linewidth=2)
#ax1.plot(pffKSE['AT'],color='lightred',label="SE AT_max",  linestyle="-", linewidth=2)
#ax1.plot(BOKUMetData_dailymax['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=0.5)
#ax1.plot(BOKUMetData_dailymax_m['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=1)
#ax1.plot(BOKUMetData_dailymax_w['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=2)
ax2.plot(pffNW['hcho'], color='blue', label="NW hcho_max D", marker="x", linestyle="-", linewidth=0.5)
ax2.plot(pffSE['hcho'], color='red', label="SE hcho_max D", marker="x", linestyle="-", linewidth=0.5)
ax2.plot(pffKNW['hcho'], color='turquoise', label="NW hcho_max K", marker="x", linestyle="-", linewidth=0.5)
ax2.plot(pffKSE['hcho'], color='orange', label="SE hcho_max K", marker="x", linestyle="-", linewidth=0.5)
ax1.plot(pffNWcho['chocho'], color='brown', label="NW chocho D", linestyle="-", linewidth=1)
ax1.plot(pffSEcho['chocho'], color='violet', label="SE chocho D", linestyle="-", linewidth=1)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
#plt.xticks(yM, yM_ticks)
plt.xlabel("time [days]")
ax2.set_ylabel("VMR hcho [ppb]")
ax1.set_ylabel("DSC [Molek / cmý]")
#ax1.set_ylabel("air temperature [°C]")
#ax1.set_ylim(-5, 80)
#ax2.set_ylim(0, 6)
plt.legend()
plt.show()

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

pffSE_veg = pffSE.loc[(pffSE.index.month>=4)&(pffSE.index.month<=10)]
pffSE_noveg = pffSE.loc[(pffSE.index.month>=11)|(pffSE.index.month<=3)]
pffNW_veg = pffNW.loc[(pffNW.index.month>=4)&(pffNW.index.month<=10)]
pffNW_noveg = pff.loc[(pffNW.index.month>=11)|(pffNW.index.month<=3)]

print("all: \n ")
print(pffSE,pffNW)
print("AT SE:", pffSE['AT'].mean()," AT NW:", pffNW['AT'].mean()," hcho SE:", pffSE['hcho'].mean(), " hcho NW:", pffNW['hcho'].mean())
print("veg: \n ")
print(pffSE_veg, pffNW_veg)
print("AT SE:", pffSE_veg['AT'].mean()," AT NW:", pffNW_veg['AT'].mean()," hcho SE:", pffSE_veg['hcho'].mean(), " hcho NW:", pffNW_veg['hcho'].mean())
print("noveg: \n ")
print(pffSE_noveg, pffNW_noveg)
print("AT SE:", pffSE_noveg['AT'].mean()," AT NW:", pffNW_noveg['AT'].mean()," hcho SE:", pffSE_noveg['hcho'].mean(), " hcho NW:", pffNW_noveg['hcho'].mean())



""" FIGURE 5 """
commonstart = datetime(2017,6,14)
commonend = datetime(2021,8,12)

figure = plt.figure
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax1 = plt.gca()
#ax2 = ax1.twinx()
ax3 = plt.subplot(gs[1])
ax3 = plt.gca()
#ax4 = ax3.twinx()
ax1.plot(Runningmean_5daysSE['AT5d'],color='red',label="SE", linewidth=2,linestyle="",marker="o",markersize=5) #pffNW['AT']
ax1.plot(Runningmean_5daysNW['AT5d'],color='blue',label="NW", linewidth=2,linestyle="",marker="o",markersize=5) #pffSE['AT']
#ax1.plot(pffKNW['AT'],color='lightblue',label="NW AT_max", linestyle="-", linewidth=2)
#ax1.plot(pffKSE['AT'],color='lightred',label="SE AT_max",  linestyle="-", linewidth=2)
#ax1.plot(BOKUMetData_dailymax['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=0.5)
#ax1.plot(BOKUMetData_dailymax_m['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=1)
#ax1.plot(BOKUMetData_dailymax_w['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=2)
#ax2.plot(pffNW['hcho'], color='blue', label="NW hcho_max D", marker="x", linestyle="-", linewidth=0.5)
#ax2.plot(pffSE['hcho'], color='red', label="SE hcho_max D", marker="x", linestyle="-", linewidth=0.5)
#ax2.plot(pffKNW['hcho'], color='turquoise', label="NW hcho_max K", marker="x", linestyle="-", linewidth=0.5)
#ax2.plot(pffKSE['hcho'], color='orange', label="SE hcho_max K", marker="x", linestyle="-", linewidth=0.5)
#plt.xticks(yM, yM_ticks)
ax1.set_ylabel("AT [°C]")
#ax1.set_ylim(-5, 80)
ax3.plot(Runningmean_5daysSE['hcho'],color='red',label="SE AT_max", linewidth=2,linestyle="",marker="o",markersize=5) #pffNW['AT']
ax3.plot(Runningmean_5daysNW['hcho'],color='blue',label="NW AT_max", linewidth=2,linestyle="",marker="o",markersize=5) #pffSE['AT']
ax3.set_ylabel("HCHO [ppb]")
#ax3.plot(Runningmean_5daysSE['AT5d'][commonstart:commonend] - Runningmean_5daysNW['AT5d'][commonstart:commonend], color='black',label="SE - NW AT_dmax 5 day gliding mean", linewidth=2)
#ax3.plot(pffNW['AT'].resample("2W").mean(),color='black',label="NW AT_dmax weekly", linewidth=2)
#ax3.plot(pffSE['AT'].resample("2W").mean() - pffNW['AT'].resample("2W").mean(),color='black',label="SE - NW AT_dmax weekly", linewidth=2)
#ax4.plot(Runningmean_5daysSE['hcho5d'][commonstart:commonend] - Runningmean_5daysNW['hcho5d'][commonstart:commonend], color='blue', label="SE - NW hcho dmax 5 day gliding mean", linewidth=2)
#ax3.set_ylabel(r"$\Delta$ air temperature [°C]")
#ax4.set_ylabel(r"$\Delta$ VMR hcho [ppb]")
#ax2.set_ylim(0, 6)
ax1.legend(loc='lower left')
#ax2.legend(loc='upper right')
#ax3.legend(loc='upper left')
#ax4.legend(loc='upper right')
plt.xlabel("time [days]")
plt.show()

""" FIGURE 1 """
figure = plt.figure
gs = gridspec.GridSpec(3, 1,height_ratios=[1,1,1])
#plt.title("wWheat, 40-100 cm")
ax1 = plt.subplot(gs[0])
#ax1 = plt.gca()
#ax2 = ax1.twinx()
#ax3 = ax1.twinx()
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])

#ax2.plot(hcho_dmax, color='black', label="HCHO dmean", linewidth=0.1)
#ax2.plot(hcho_dmax17, color='violet', label="2017", linewidth=0.1)
#ax2.plot(hcho_dmax18, color='blue', label="2018", linewidth=0.1)
#ax2.plot(hcho_dmax19, color='green', label="2019", linewidth=0.1)
#ax2.plot(hcho_dmax20, color='orange', label="2020", linewidth=0.1)
#ax2.plot(hcho_dmax21, color='violet', label="2021", linewidth=0.1)
AT = BOKUMetData_dailymax_m[start2017:end2021]['AT']
print(AT)
#ax1.plot(BOKUMetData_dailymax['AT'][start2017:end2021],color='grey',label="AT dmax", linewidth=0.1)
ax1.fill_between(AT.index, AT+AT_dmax_sigma,AT - AT_dmax_sigma, facecolor='grey', alpha=0.2)
#ax1.plot(AT,color='grey',label="AT dmax monthly", linewidth=1)
ax1.plot(BOKUMetData_dailymax_w['AT'][start2017:end2021],color='grey',label="AT dmax weekly", linewidth=2)

#interestingdates = [datetime(2017,9,30),datetime(2017,10,22),datetime(2018,8,5),datetime(2021,5,30)]
#ax1.axvline(x=interestingdates)
#ax1.axvline(x=datetime(2017,9,30))
#ax1.axvline(x=datetime(2017,10,22))
#ax1.axvline(x=datetime(2018,8,5))
#ax1.axvline(x=datetime(2021,5,30))
#ax2.axvline(x=datetime(2017,9,30))
#ax2.axvline(x=datetime(2017,10,22))
#ax2.axvline(x=datetime(2018,8,5))
#ax2.axvline(x=datetime(2021,5,30))
#ax3.axvline(x=datetime(2017,9,30))
#ax3.axvline(x=datetime(2017,10,22))
#ax3.axvline(x=datetime(2018,8,5))
#ax3.axvline(x=datetime(2021,5,30))

#ax1.axvline(x=datetime(2020,9,6))
#ax2.axvline(x=datetime(2020,9,6))
#ax3.axvline(x=datetime(2020,9,6))

#ax1.axvline(x=datetime(2019,10,6))
#ax2.axvline(x=datetime(2019,10,6))
#ax3.axvline(x=datetime(2019,10,6))


ax2.fill_between(hcho_dmax_m[start2017:end2021].index, hcho_dmax_m[start2017:end2021]+hcho_dmax_sigma, hcho_dmax_m[start2017:end2021] - hcho_dmax_sigma, facecolor='purple', alpha=0.2)
#ax2.plot(hcho_dmax_m[start2017:end2021], color="purple",label="HCHO dmax monthly",linewidth=1)
ax2.plot(hcho_dmax_w[start2017:end2021], color="purple",label="HCHO dax weekly",linewidth=2)
#ax2.set_title(r'hcho observation $\mu$ and $\pm \sigma$ interval')

ax3.plot(vpd_dmax_w[start2017:end2021], color="blue", label="vpd_dmax weekly", linewidth=2)
ax3.fill_between(vpd_dmax_w[start2017:end2021].index,vpd_dmax_w[start2017:end2021]+vpd_dmax_sigma, vpd_dmax_w[start2017:end2021]-vpd_dmax_sigma, facecolor="blue", alpha=0.2)
#ax3.plot(vpd_dmax[start2017:end2021], color="blue", label="vpd_dmax weekly", linewidth=0.1)
#ax3.plot(rss_sub_diff_w,color="black", label="rss_diff")
#ax3.axhline(y=0,color='black')
#upper = 0.0
#supper = np.ma.masked_where(rss_sub_diff_w > upper, rss_sub_diff_w)
#slower = np.ma.masked_where(rss_sub_diff_w < upper, rss_sub_diff_w)
#ax.plot(t, slower, t, supper)
#ax2.legend(loc="lower right")
#ax1.legend(loc="lower right")
#ax3.legend(loc="lower right")
#plt.xticks(yM, yM_ticks)
plt.xlabel("time [days]")
ax3.set_ylabel("VPD [kPa]")
ax2.set_ylabel("HCHO [ppb]")
ax1.set_ylabel("AT [°C]")
#ax1.set_ylim(-5, 80)
#ax2.set_ylim(0, 6)
plt.show()



start = datetime(1990,1,1)
start2017 = datetime(2017, 5, 1, 00, 00)
start2018 = datetime(2018, 1, 1, 00, 00)
start2019 = datetime(2019, 1, 1, 00, 00)
start2020 = datetime(2020, 1, 1, 00, 00)
start2021 = datetime(2021, 1, 1, 00, 00)
end2021 = datetime(2021, 9, 1, 00, 00)

pff = pd.concat([hcho_dmax, BOKUMetData_dailymax["AT"],HighGRdays["GR"],HighGRdays["WD"]],axis=1)
pff.columns =['hcho', 'AT', 'GR', 'WD']
#pff = pff.dropna()
pffNW = pff.loc[(pff['WD'] >=270) & (pff['WD'] <=359)]
pffNW = pffNW.dropna()
pffSE = pff.loc[(pff['WD'] >=90) & (pff['WD'] <=180)]
pffSE = pffSE.dropna()
pffK = pd.concat([hchoK_dmax, BOKUMetData_dailymax["AT"],HighGRdays["GR"],HighGRdays["WD"]],axis=1)
pffKNW = pffK.loc[(pff['WD'] >=270) & (pffK['WD'] <=359)]
pffKNW = pffKNW.dropna()
pffKSE = pffK.loc[(pff['WD'] >=90) & (pffK['WD'] <=180)]
pffKSE = pffKSE.dropna()
pffCHOCHO = pd.concat([chochoD_dmax, BOKUMetData_dailymax["AT"],HighGRdays["GR"],HighGRdays["WD"]],axis=1)
pff.columns =['chocho', 'AT', 'GR', 'WD']
pff = pff.dropna()
pffNWcho = pffCHOCHO.loc[(pff['WD'] >=270) & (pffCHOCHO['WD'] <=359)]
pffNWcho = pffNWcho.dropna()
pffSEcho = pffCHOCHO.loc[(pff['WD'] >=90) & (pffCHOCHO['WD'] <=180)]
pffSEcho = pffSEcho.dropna()

hcho_dmax = pffNW['hcho']  #TODO: keep changes for ONLY NW or delete this line to go back to not filtered version

hcho_dmax17 = hcho_dmax[datetime(2017,5,1,0,0):datetime(2017,12,31,0,0)]
hcho_17fill = np.full(shape=120,fill_value=np.NaN)
hcho_dmax17_a = np.append(hcho_17fill, hcho_dmax17)
hcho_dmax18 = hcho_dmax[start2018:datetime(2018,12,31,0,0)]
hcho_dmax19 = hcho_dmax[start2019:datetime(2019,12,31,0,0)]
hcho_dmax20 = hcho_dmax[start2020:datetime(2020,12,31,0,0)]
hcho_dmax21 = hcho_dmax[start2021:end2021]

#print(hcho_dmax17_a,hcho_dmax18,hcho_dmax19,hcho_dmax20,hcho_dmax21)

yM = [15,46,74,105,135,166,196,227,258,288,319,349]
yM_ticks = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
yM18 = [15,46,74,105,135,166,196,227,258,288,319]
yM19 = [15,46,74,105,135,166,196,227,258,288]
yM20 = [15,46,74,105,135,166,196,227,258,288,319]
yM21 = [15,46,74,105,135,166,196,227]
hcho_dmax17_m = hcho_dmax17.resample('M').mean()
hcho_17fill_m = np.full(shape=4,fill_value=np.NaN)
hcho_dmax17_a_m = np.append(hcho_17fill_m, hcho_dmax17_m)
hcho_dmax18_m = hcho_dmax18.resample('M').mean()
hcho_dmax19_m = hcho_dmax19.resample('M').mean()
hcho_dmax20_m = hcho_dmax20.resample('M').mean()
hcho_dmax21_m = hcho_dmax21.resample('M').mean()
#print(hcho_dmax17_a_m, hcho_dmax18_m,hcho_dmax19_m,hcho_dmax20_m,hcho_dmax21_m)

print(hcho_dmax17, hcho_dmax18_m, hcho_dmax19_m, hcho_dmax20_m)

"""read in soil moisture data"""
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
#print(mean12yr_d['RSS_sub_wWheat'])
mean12yr_d_noleap = mean12yr_d.drop(pd.date_range('2000-02-29','2000-2-29'), errors='ignore') #remove 29.Feb
#print(mean12yr_d['2000-02-28':'2000-03-2'])

rss_sub17_diff_w = rss_sub['RSS_sub_wWheat'][datetime(2017,5,1):datetime(2017,12,31)].sub(mean12yr_d_noleap['RSS_sub_wWheat'][datetime(2000,5,1):].values)
rss_sub18_diff_w = rss_sub['RSS_sub_wWheat'][datetime(2018,1,1):datetime(2018,12,31)].sub(mean12yr_d_noleap['RSS_sub_wWheat'].values)
rss_sub19_diff_w = rss_sub['RSS_sub_wWheat'][datetime(2019,1,1):datetime(2019,12,31)].sub(mean12yr_d_noleap['RSS_sub_wWheat'].values)
rss_sub20_diff_w = rss_sub['RSS_sub_wWheat'][datetime(2020,1,1):datetime(2020,12,31)].sub(mean12yr_d['RSS_sub_wWheat'].values)
rss_sub_diff_w = pd.concat([rss_sub17_diff_w,rss_sub18_diff_w,rss_sub19_diff_w,rss_sub20_diff_w])
#print(rss_sub_diff_w)

figure = plt.figure
#plt.plot(range(len(hcho_dmax17_a)), hcho_dmax17_a, color='violet', label="2017", linewidth=0.2)
#plt.plot(range(len(hcho_dmax18)), hcho_dmax18, color='blue', label="2018",linewidth=0.2)
#plt.plot(range(len(hcho_dmax19)), hcho_dmax19, color='green',label="2019", linewidth=0.2)
#plt.plot(range(len(hcho_dmax20)), hcho_dmax20, color='orange',label="2020", linewidth=0.2)
#plt.plot(range(len(hcho_dmax21)), hcho_dmax21, color='red',label="2021", linewidth=0.2)
plt.plot(yM,hcho_dmax17_a_m, color='violet', linewidth=1, marker="x", label="2017")
plt.plot(yM18,hcho_dmax18_m, color='blue', linewidth=1, marker="x", label="2018")
plt.plot(yM19,hcho_dmax19_m, color='green', linewidth=1, marker="x",label="2019")
plt.plot(yM20,hcho_dmax20_m, color='orange', linewidth=1, marker="x",label="2020")
plt.plot(yM21,hcho_dmax21_m, color='red', linewidth=1, marker="x",label="2021")
plt.xticks(yM, yM_ticks)
plt.xlabel("days")
plt.ylabel("hcho [ppb]")
plt.legend()
plt.show()

exit()
figure = plt.figure
ax1 = plt.gca()
ax2 = ax1.twinx()
#ax1.plot(pffNW['AT'],color='powderblue',label="NW AT_max", linewidth=2)
#ax1.plot(pffSE['AT'],color='peachpuff',label="SE AT_max", linewidth=2)
#ax1.plot(pffKNW['AT'],color='lightblue',label="NW AT_max", linestyle="-", linewidth=2)
#ax1.plot(pffKSE['AT'],color='lightred',label="SE AT_max",  linestyle="-", linewidth=2)
#ax1.plot(BOKUMetData_dailymax['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=0.5)
#ax1.plot(BOKUMetData_dailymax_m['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=1)
#ax1.plot(BOKUMetData_dailymax_w['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=2)
ax2.plot(pffNW['hcho'], color='blue', label="NW hcho_max D", marker="x", linestyle="-", linewidth=0.5)
ax2.plot(pffSE['hcho'], color='red', label="SE hcho_max D", marker="x", linestyle="-", linewidth=0.5)
ax2.plot(pffKNW['hcho'], color='turquoise', label="NW hcho_max K", marker="x", linestyle="-", linewidth=0.5)
ax2.plot(pffKSE['hcho'], color='orange', label="SE hcho_max K", marker="x", linestyle="-", linewidth=0.5)
ax1.plot(pffNWcho['chocho'], color='brown', label="NW chocho D", linestyle="-", linewidth=1)
ax1.plot(pffSEcho['chocho'], color='violet', label="SE chocho D", linestyle="-", linewidth=1)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
#plt.xticks(yM, yM_ticks)
plt.xlabel("time [days]")
ax2.set_ylabel("VMR hcho [ppb]")
ax1.set_ylabel("DSC [Molek / cmý]")
#ax1.set_ylabel("air temperature [°C]")
#ax1.set_ylim(-5, 80)
#ax2.set_ylim(0, 6)
plt.legend()
plt.show()

#exit()

N=7 #days
atmaxSE_5daymean = np.convolve(pffSE['AT'], np.ones(N)/N, mode='valid')
atmaxNW_5daymean = np.convolve(pffNW['AT'], np.ones(N)/N, mode='valid')
hchomaxSE_5daymean = np.convolve(pffSE['hcho'], np.ones(N)/N, mode='valid')
hchomaxNW_5daymean = np.convolve(pffNW['hcho'], np.ones(N)/N, mode='valid')

Runningmean_5daysSE = pffSE[6:]
Runningmean_5daysSE.insert(1,'AT5d', atmaxSE_5daymean.tolist())
Runningmean_5daysSE.insert(1,'hcho5d', hchomaxSE_5daymean.tolist())
print(Runningmean_5daysSE['AT5d'])
Runningmean_5daysNW = pffNW[6:]
Runningmean_5daysNW.insert(1,'AT5d', atmaxNW_5daymean.tolist())
Runningmean_5daysNW.insert(1,'hcho5d', hchomaxNW_5daymean.tolist())
print(Runningmean_5daysNW['AT5d'])

print("AT SE:", pffSE['AT'].mean()," AT NW:", pffNW['AT'].mean()," hcho SE:", pffSE['hcho'].mean(), " hcho NW:", pffNW['hcho'].mean())


commonstart = datetime(2017,6,14)
commonend = datetime(2021,8,12)

figure = plt.figure
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
ax1 = plt.subplot(gs[0])
ax1 = plt.gca()
#ax2 = ax1.twinx()
ax3 = plt.subplot(gs[1])
ax3 = plt.gca()
#ax4 = ax3.twinx()
ax1.plot(Runningmean_5daysSE['AT5d'],color='red',label="SE", linewidth=2) #pffNW['AT']
ax1.plot(Runningmean_5daysNW['AT5d'],color='blue',label="NW", linewidth=2) #pffSE['AT']
#ax1.plot(pffKNW['AT'],color='lightblue',label="NW AT_max", linestyle="-", linewidth=2)
#ax1.plot(pffKSE['AT'],color='lightred',label="SE AT_max",  linestyle="-", linewidth=2)
#ax1.plot(BOKUMetData_dailymax['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=0.5)
#ax1.plot(BOKUMetData_dailymax_m['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=1)
#ax1.plot(BOKUMetData_dailymax_w['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=2)
#ax2.plot(pffNW['hcho'], color='blue', label="NW hcho_max D", marker="x", linestyle="-", linewidth=0.5)
#ax2.plot(pffSE['hcho'], color='red', label="SE hcho_max D", marker="x", linestyle="-", linewidth=0.5)
#ax2.plot(pffKNW['hcho'], color='turquoise', label="NW hcho_max K", marker="x", linestyle="-", linewidth=0.5)
#ax2.plot(pffKSE['hcho'], color='orange', label="SE hcho_max K", marker="x", linestyle="-", linewidth=0.5)
#plt.xticks(yM, yM_ticks)
ax1.set_ylabel("air temperature [°C]")
#ax1.set_ylim(-5, 80)
ax3.plot(Runningmean_5daysSE['hcho'],color='red',label="SE AT_max", linewidth=2) #pffNW['AT']
ax3.plot(Runningmean_5daysNW['hcho'],color='blue',label="NW AT_max", linewidth=2) #pffSE['AT']
ax3.set_ylabel("VMR hcho [ppb]")
#ax3.plot(Runningmean_5daysSE['AT5d'][commonstart:commonend] - Runningmean_5daysNW['AT5d'][commonstart:commonend], color='black',label="SE - NW AT_dmax 5 day gliding mean", linewidth=2)
#ax3.plot(pffNW['AT'].resample("2W").mean(),color='black',label="NW AT_dmax weekly", linewidth=2)
#ax3.plot(pffSE['AT'].resample("2W").mean() - pffNW['AT'].resample("2W").mean(),color='black',label="SE - NW AT_dmax weekly", linewidth=2)
#ax4.plot(Runningmean_5daysSE['hcho5d'][commonstart:commonend] - Runningmean_5daysNW['hcho5d'][commonstart:commonend], color='blue', label="SE - NW hcho dmax 5 day gliding mean", linewidth=2)
#ax3.set_ylabel(r"$\Delta$ air temperature [°C]")
#ax4.set_ylabel(r"$\Delta$ VMR hcho [ppb]")
#ax2.set_ylim(0, 6)
ax1.legend(loc='lower left')
#ax2.legend(loc='upper right')
#ax3.legend(loc='upper left')
#ax4.legend(loc='upper right')
plt.xlabel("time [days]")
plt.show()

exit()
figure = plt.figure
gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
#plt.title("wWheat, 40-100 cm")
ax1 = plt.subplot(gs[0])
ax1 = plt.gca()
ax2 = ax1.twinx()
ax3 = plt.subplot(gs[1])
ax1.plot(BOKUMetData_dailymax['AT'][start2017:end2021],color='grey',label="AT dmax", linewidth=0.1)
ax1.plot(BOKUMetData_dailymax_m['AT'][start2017:end2021],color='grey',label="AT dmax monthly", linewidth=1)
ax1.plot(BOKUMetData_dailymax_w['AT'][start2017:end2021],color='grey',label="AT dmax weekly", linewidth=2)
ax2.plot(hcho_dmax, color='violet', label="HCHO dmean", linewidth=0.1)
#ax2.plot(hcho_dmax17, color='violet', label="2017", linewidth=0.1)
#ax2.plot(hcho_dmax18, color='blue', label="2018", linewidth=0.1)
#ax2.plot(hcho_dmax19, color='green', label="2019", linewidth=0.1)
#ax2.plot(hcho_dmax20, color='orange', label="2020", linewidth=0.1)
#ax2.plot(hcho_dmax21, color='violet', label="2021", linewidth=0.1)
ax2.plot(hcho_dmax_m, color="violet",label="HCHO dmean monthly",linewidth=1)
ax2.plot(hcho_dmax_w, color="violet",label="HCHO dmean weekly",linewidth=2)
ax3.plot(rss_sub_diff_w,color="black", label="rss_diff")
ax3.axhline(y=0,color='black')
#upper = 0.0
#supper = np.ma.masked_where(rss_sub_diff_w > upper, rss_sub_diff_w)
#slower = np.ma.masked_where(rss_sub_diff_w < upper, rss_sub_diff_w)
#ax.plot(t, slower, t, supper)

ax2.legend(loc="upper right")
ax1.legend(loc="upper left")
ax3.legend(loc="upper right")
#plt.xticks(yM, yM_ticks)
plt.xlabel("time [days]")
ax2.set_ylabel("VMR hcho [ppb]")
ax1.set_ylabel("air temperature [°C]")
ax1.set_ylim(-5, 80)
ax2.set_ylim(0, 6)
plt.legend()
plt.show()
