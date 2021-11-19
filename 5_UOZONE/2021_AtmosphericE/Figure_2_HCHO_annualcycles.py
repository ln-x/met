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

hcho_dmax17 = hcho_dmax[:start2018]
hcho_17fill = np.full(shape=120,fill_value=np.NaN)
hcho_dmax17_a = np.append(hcho_17fill, hcho_dmax17)
hcho_dmax18 = hcho_dmax[start2018:start2019]
hcho_dmax19 = hcho_dmax[start2019:start2020]
hcho_dmax20 = hcho_dmax[start2020:start2021]
hcho_dmax21 = hcho_dmax[start2021:end2021]

yM = [15,46,74,105,135,166,196,227,258,288,319,349]
yM_ticks = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
print(hcho_dmax17_a,hcho_dmax18,hcho_dmax19,hcho_dmax20,hcho_dmax21)

yM = [15,46,74,105,135,166,196,227,258,288,319,349]
yM_ticks = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
yM21 = [15,46,74,105,135,166,196,227]
hcho_dmax17_m = hcho_dmax17.resample('M').mean()
hcho_17fill_m = np.full(shape=4,fill_value=np.NaN)
hcho_dmax17_a_m = np.append(hcho_17fill_m, hcho_dmax17_m)

hcho_dmax18_m = hcho_dmax18.resample('M').mean()
hcho_dmax19_m = hcho_dmax19.resample('M').mean()
hcho_dmax20_m = hcho_dmax20.resample('M').mean()
hcho_dmax21_m = hcho_dmax21.resample('M').mean()
print(hcho_dmax17_a_m, hcho_dmax18_m,hcho_dmax19_m,hcho_dmax20_m,hcho_dmax21_m)

pff = pd.concat([hcho_dmax, BOKUMetData_dailymax["AT"],HighGRdays["GR"],HighGRdays["WD"]],axis=1)
pff.columns =['hcho', 'AT', 'GR', 'WD']
pff = pff.dropna()
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



figure = plt.figure
plt.plot(range(len(hcho_dmax17_a)), hcho_dmax17_a, color='violet', label="2017", linewidth=0.2)
plt.plot(range(len(hcho_dmax18)), hcho_dmax18, color='blue', label="2018",linewidth=0.2)
plt.plot(range(len(hcho_dmax19)), hcho_dmax19, color='green',label="2019", linewidth=0.2)
plt.plot(range(len(hcho_dmax20)), hcho_dmax20, color='orange',label="2020", linewidth=0.2)
plt.plot(range(len(hcho_dmax21)), hcho_dmax21, color='red',label="2021", linewidth=0.2)
plt.plot(yM,hcho_dmax17_a_m[:-1], color='violet', linewidth=2)
plt.plot(yM,hcho_dmax18_m[:-1], color='blue', linewidth=2)
plt.plot(yM,hcho_dmax19_m[:-1], color='green', linewidth=2)
plt.plot(yM,hcho_dmax20_m[:-1], color='orange', linewidth=2)
plt.plot(yM21,hcho_dmax21_m, color='red', linewidth=2)
plt.xticks(yM, yM_ticks)
plt.xlabel("days")
plt.ylabel("hcho [ppb]")
plt.legend()
plt.show()

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

figure = plt.figure
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(pffNW['AT'],color='powderblue',label="NW AT_max", linewidth=2)
ax1.plot(pffSE['AT'],color='peachpuff',label="SE AT_max", linewidth=2)
#ax1.plot(pffKNW['AT'],color='lightblue',label="NW AT_max", linestyle="-", linewidth=2)
#ax1.plot(pffKSE['AT'],color='lightred',label="SE AT_max",  linestyle="-", linewidth=2)
#ax1.plot(BOKUMetData_dailymax['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=0.5)
#ax1.plot(BOKUMetData_dailymax_m['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=1)
#ax1.plot(BOKUMetData_dailymax_w['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=2)
ax2.plot(pffNW['hcho'], color='blue', label="NW hcho_max D", marker="x", linestyle="-", linewidth=0.5)
ax2.plot(pffSE['hcho'], color='red', label="SE hcho_max D", marker="x", linestyle="-", linewidth=0.5)
ax2.plot(pffKNW['hcho'], color='turquoise', label="NW hcho_max K", marker="x", linestyle="-", linewidth=0.5)
ax2.plot(pffKSE['hcho'], color='orange', label="SE hcho_max K", marker="x", linestyle="-", linewidth=0.5)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
#plt.xticks(yM, yM_ticks)
plt.xlabel("time [days]")
ax2.set_ylabel("VMR hcho [ppb]")
ax1.set_ylabel("air temperature [°C]")
ax1.set_ylim(-5, 80)
#ax2.set_ylim(0, 6)
plt.legend()
plt.show()


#exit()
figure = plt.figure
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(BOKUMetData_dailymax['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=0.1)
ax1.plot(BOKUMetData_dailymax_m['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=1)
ax1.plot(BOKUMetData_dailymax_w['AT'][start2017:end2021],color='grey',label="AT_max", linewidth=2)
ax2.plot(hcho_dmax17, color='violet', label="2017", linewidth=0.1)
ax2.plot(hcho_dmax18, color='blue', label="2018", linewidth=0.1)
ax2.plot(hcho_dmax19, color='green', label="2019", linewidth=0.1)
ax2.plot(hcho_dmax20, color='orange', label="2020", linewidth=0.1)
ax2.plot(hcho_dmax21, color='violet', label="2021", linewidth=0.1)
ax2.plot(hcho_dmax_m, color="violet",label="monthly mean",linewidth=1)
ax2.plot(hcho_dmax_w, color="violet",label="weekly mean",linewidth=2)
plt.legend()
#plt.xticks(yM, yM_ticks)
plt.xlabel("time [days]")
ax2.set_ylabel("VMR hcho [ppb]")
ax1.set_ylabel("air temperature [°C]")
ax1.set_ylim(-5, 80)
ax2.set_ylim(0, 6)
plt.legend()
plt.show()
