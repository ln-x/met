import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from scipy import stats
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVindobona_Filter_fullperiod
from matplotlib.dates import DateFormatter
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


'''READ in SOIL MOISTURE DATA'''
#file_sm_2019_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/RUT_10_min.xls"
#sm = pd.read_excel(file_sm_2019_rutz, sheet_name="RUT_d", usecols="D,K,L,M,N,O,P", skiprows=11)#, converters={'A': pd.to_datetime})
#sm.columns = ['datetime', 'VWC1 min[%]', 'VWC2 min[%]','VWC3 min[%]','VWC1 max[%]', 'VWC2 max[%]','VWC3 max[%]']  #TODO: local time!
#sm = sm.set_index(pd.to_datetime(sm['datetime']))
#sm = sm.drop(columns=['datetime'])

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
Runningmean_5d['GR5d'] = grsum_5daymean.tolist()
#Runningmean_5d['RSS5d'] = rss_sub_5daymean.tolist()
Runningmean_5d['AT5d'] = atmax_5daymean.tolist()
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

rss_sub08 = rss_sub[datetime(2008, 1, 1, 00, 00):datetime(2008, 12, 31, 00, 00)]
rss_sub09 = rss_sub[datetime(2009, 1, 1, 00, 00):datetime(2009, 12, 31, 00, 00)]
rss_sub10 = rss_sub[datetime(2010, 1, 1, 00, 00):datetime(2010, 12, 31, 00, 00)]
rss_sub11 = rss_sub[datetime(2011, 1, 1, 00, 00):datetime(2011, 12, 31, 00, 00)]
rss_sub12 = rss_sub[datetime(2012, 1, 1, 00, 00):datetime(2012, 12, 31, 00, 00)]
rss_sub13 = rss_sub[datetime(2013, 1, 1, 00, 00):datetime(2013, 12, 31, 00, 00)]
rss_sub14 = rss_sub[datetime(2014, 1, 1, 00, 00):datetime(2014, 12, 31, 00, 00)]
rss_sub15 = rss_sub[datetime(2015, 1, 1, 00, 00):datetime(2015, 12, 31, 00, 00)]
rss_sub16 = rss_sub[datetime(2016, 1, 1, 00, 00):datetime(2016, 12, 31, 00, 00)]
rss_sub17 = rss_sub[datetime(2017, 1, 1, 00, 00):datetime(2017, 12, 31, 00, 00)]
rss_sub18 = rss_sub[datetime(2018, 1, 1, 00, 00):datetime(2018, 12, 31, 00, 00)]
rss_sub19 = rss_sub[datetime(2019, 1, 1, 00, 00):datetime(2019, 12, 31, 00, 00)]
rss_sub20 = rss_sub[datetime(2020, 1, 1, 00, 00):datetime(2020, 12, 31, 00, 00)]

yM_ticks = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
yM = [15,46,74,105,135,166,196,227,258,288,319,349]

rss_08_m = rss_sub08.resample('M').mean()
rss_09_m = rss_sub09.resample('M').mean()
rss_10_m = rss_sub10.resample('M').mean()
rss_11_m = rss_sub11.resample('M').mean()
rss_12_m = rss_sub12.resample('M').mean()
rss_13_m = rss_sub13.resample('M').mean()
rss_14_m = rss_sub14.resample('M').mean()
rss_15_m = rss_sub15.resample('M').mean()
rss_16_m = rss_sub16.resample('M').mean()
rss_17_m = rss_sub17.resample('M').mean()
rss_18_m = rss_sub18.resample('M').mean()
rss_19_m = rss_sub19.resample('M').mean()
rss_20_m = rss_sub20.resample('M').mean()
#print(rss_17_m)

#print(rss_08_m["RSS_sub_grass"].values)
#print(rss_09_m["RSS_sub_grass"].values)

cultivar = "RSS_sub_grass"

matrix12yr_m1 = np.concatenate((np.matrix(rss_08_m["RSS_sub_grass"].values).T,np.matrix(rss_09_m["RSS_sub_grass"].values).T,
                              np.matrix(rss_10_m["RSS_sub_grass"].values).T,np.matrix(rss_11_m["RSS_sub_grass"].values).T,
                              np.matrix(rss_12_m["RSS_sub_grass"].values).T,np.matrix(rss_13_m["RSS_sub_grass"].values).T,
                              np.matrix(rss_14_m["RSS_sub_grass"].values).T,np.matrix(rss_15_m["RSS_sub_grass"].values).T,
                              np.matrix(rss_16_m["RSS_sub_grass"].values).T,np.matrix(rss_17_m["RSS_sub_grass"].values).T,
                              np.matrix(rss_18_m["RSS_sub_grass"].values).T,np.matrix(rss_19_m["RSS_sub_grass"].values).T),axis=1)
mean12yr_m_grass = np.mean(matrix12yr_m1,axis=1)

matrix12yr_m2 = np.concatenate((np.matrix(rss_08_m["RSS_sub_wWheat"].values).T,np.matrix(rss_09_m["RSS_sub_wWheat"].values).T,
                              np.matrix(rss_10_m["RSS_sub_wWheat"].values).T,np.matrix(rss_11_m["RSS_sub_wWheat"].values).T,
                              np.matrix(rss_12_m["RSS_sub_wWheat"].values).T,np.matrix(rss_13_m["RSS_sub_wWheat"].values).T,
                              np.matrix(rss_14_m["RSS_sub_wWheat"].values).T,np.matrix(rss_15_m["RSS_sub_wWheat"].values).T,
                              np.matrix(rss_16_m["RSS_sub_wWheat"].values).T,np.matrix(rss_17_m["RSS_sub_wWheat"].values).T,
                              np.matrix(rss_18_m["RSS_sub_wWheat"].values).T,np.matrix(rss_19_m["RSS_sub_wWheat"].values).T),axis=1)
mean12yr_m_wWheat = np.mean(matrix12yr_m2,axis=1)
mean12yr_d = rss_sub.groupby([rss_sub.index.month, rss_sub.index.day]).mean()
mean12yr_d["new_index"] = mean12yr_d.index.map(lambda x:datetime(2000, x[0], x[1]))
mean12yr_d = mean12yr_d.set_index("new_index")
#print(mean12yr_d['RSS_sub_wWheat'])
mean12yr_d_noleap = mean12yr_d.drop(pd.date_range('2000-02-29','2000-2-29'), errors='ignore') #remove 29.Feb
#print(mean12yr_d['2000-02-28':'2000-03-2'])
#print(rss_sub)

rss_sub17_diff_w = rss_sub17['RSS_sub_wWheat'][datetime(2017,5,1):].values - mean12yr_d_noleap['RSS_sub_wWheat'][datetime(2000,5,1):].values
rss_sub18_diff_w = rss_sub18['RSS_sub_wWheat'].values - mean12yr_d_noleap['RSS_sub_wWheat'].values
rss_sub19_diff_w = rss_sub19['RSS_sub_wWheat'].values - mean12yr_d_noleap['RSS_sub_wWheat'].values
rss_sub20_diff_w = rss_sub20['RSS_sub_wWheat'].values - mean12yr_d['RSS_sub_wWheat'].values  #leap year
rss_sub_diff_w = np.concatenate([rss_sub17_diff_w,rss_sub18_diff_w,rss_sub19_diff_w,rss_sub20_diff_w])

print(rss_sub_diff_w)

#mean12yr_m.to_csv("/home/heidit/Downloads/mean12yr_m.csv")
#mean12yr_d.to_csv("/home/heidit/Downloads/mean12yr_d.csv")

print(matrix12yr_m2, mean12yr_m_wWheat)
#exit()


fig = plt.figure()
ax1 = fig.add_subplot(111)

gs = gridspec.GridSpec(2, 1,height_ratios=[2,1])
plt.title("wWheat, 40-100 cm")
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax1.plot(range(len(rss_sub18)), rss_sub18["RSS_sub_wWheat"], color='blue',label="2018", linewidth=1)
ax1.plot(range(len(rss_sub19)), rss_sub19["RSS_sub_wWheat"], color='green',label="2019", linewidth=1)
ax1.plot(range(len(rss_sub20)), rss_sub20["RSS_sub_wWheat"], color='orange',label="2020", linewidth=1)
ax1.plot(range(365),mean12yr_d_noleap['RSS_sub_wWheat'].values,color='grey',label="2008-2020",linewidth=2)
#ax1.plot(yM,mean12yr_m_grass, color='grey', label="2008-2020")
ax1.set_ylabel("rss [0-1]")
ax1.set_xticks(yM)
ax1.legend(loc="lower left",fontsize='small')
#ax1.plot(range(len(rss_sub17)), rss_sub20["RSS_sub_wWheat"], color='orange',label="2017", linewidth=0.5)
#ax1.plot(timelist,S202WOvalues, label=r"$\alpha_{g}$:0,13;$\alpha_{w}$:0,10", color="red")#,linestyle="dashed")
#ax1.set_ylabel(r"$T_{a}$"u'[°C]')
#ax1.set_ylim(16,37)
#ax1.legend(loc="lower right",fontsize='small')
ax2.plot(range(len(rss_sub18_diff_w)), rss_sub18_diff_w, color='blue',label="2018", linewidth=1)
ax2.plot(range(len(rss_sub19_diff_w)), rss_sub19_diff_w, color='green',label="2019", linewidth=1)
ax2.plot(range(len(rss_sub20_diff_w)), rss_sub20_diff_w, color='orange',label="2020", linewidth=1)
ax2.set_ylabel(r"$\Delta$ rss [0-1]")
plt.xticks(yM, yM_ticks)
ax1.set_xlabel('time[days]')
ax1.grid(True)
ax2.grid(True)
#myFmt = DateFormatter("%M")
#ax1.xaxis.set_major_formatter(myFmt)
plt.show()

exit()

figure = plt.figure
plt.plot(range(len(rss_sub17)), rss_sub17["RSS_sub_grass"], color='violet', label="2017", linewidth=0.5)
plt.plot(range(len(rss_sub18)), rss_sub18["RSS_sub_grass"], color='blue', label="2018",linewidth=0.5)
plt.plot(range(len(rss_sub19)), rss_sub19["RSS_sub_grass"], color='green',label="2019", linewidth=0.5)
plt.plot(range(len(rss_sub20)), rss_sub20["RSS_sub_grass"], color='orange',label="2020", linewidth=0.5)
#plt.plot(range(len(rss_sub20)), rss_sub20, color='red',label="2021", linewidth=0.5)
plt.plot(yM,rss_17_m["RSS_sub_grass"], color='violet', linewidth=2)
plt.plot(yM,rss_18_m["RSS_sub_grass"], color='blue', linewidth=2)
plt.plot(yM,rss_19_m["RSS_sub_grass"], color='green', linewidth=2)
plt.plot(yM,rss_20_m["RSS_sub_grass"], color='orange', linewidth=2)
plt.plot(yM,mean12yr_m_grass, color='grey', label="2008-2020")
#plt.plot(yM,rss_21_m[:-1], color='orange', linewidth=2)
plt.xticks(yM, yM_ticks)
plt.xlabel("julian days")
plt.ylabel("rss 40-100 cm, grass [0-1]")
plt.legend()
plt.show()

figure = plt.figure
plt.plot(range(len(rss_sub17)), rss_sub17["RSS_sub_wWheat"], color='violet', label="2017", linewidth=0.5)
plt.plot(range(len(rss_sub18)), rss_sub18["RSS_sub_wWheat"], color='blue', label="2018",linewidth=0.5)
plt.plot(range(len(rss_sub19)), rss_sub19["RSS_sub_wWheat"], color='green',label="2019", linewidth=0.5)
plt.plot(range(len(rss_sub20)), rss_sub20["RSS_sub_wWheat"], color='orange',label="2020", linewidth=0.5)
#plt.plot(range(len(rss_sub20)), rss_sub20, color='red',label="2021", linewidth=0.5)
plt.plot(yM,rss_17_m["RSS_sub_wWheat"], color='violet', linewidth=2)
plt.plot(yM,rss_18_m["RSS_sub_wWheat"], color='blue', linewidth=2)
plt.plot(yM,rss_19_m["RSS_sub_wWheat"], color='green', linewidth=2)
plt.plot(yM,rss_20_m["RSS_sub_wWheat"], color='orange', linewidth=2)
plt.plot(yM,mean12yr_m_wWheat, color='grey', label="2008-2020")
#plt.plot(yM,rss_21_m[:-1], color='orange', linewidth=2)
plt.xticks(yM, yM_ticks)
plt.xlabel("julian days")
plt.ylabel("rss 40-100 cm, winter wheat [0-1]")
plt.legend()
plt.show()