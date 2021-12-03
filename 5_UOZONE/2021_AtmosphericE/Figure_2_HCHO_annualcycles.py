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

BOKUMetData_dailymax_m = BOKUMetData_dailymax.resample('M').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

BOKUMetData_dailymax_w = BOKUMetData_dailymax.resample('W').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

"read in VINDOBONA"

foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
foldername_K = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_KQ"
foldername_glyoxal = "/windata/DATA/remote/ground/maxdoas/chocho2020"

hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))
hchoK_d, hchoK_dmax, hchoK_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_K,"K", begin= datetime(2020, 1, 1, 0, 0, 0))
#hchoK_d, hchoK_dmax, hchoK_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_K,"K", begin= datetime.datetime(2020, 1, 1, 0, 0, 0)))
#print(len(hchoK_dmax))
#print(len(hcho_dmax))
chochoD_dmax, chochoK_dmax = ReadinVindobona_Glyoxal.loadfileALL(foldername_glyoxal)

hcho_dmax_m = hcho_dmax.resample('M').mean()
hcho_dmax_w = hcho_dmax.resample('W').mean()

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
