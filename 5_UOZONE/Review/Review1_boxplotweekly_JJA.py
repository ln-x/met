# -*- coding: utf-8 -*-
__author__ = 'lnx'

import numpy as np
import pandas as pd
from datetime import datetime
import monthdelta
import netCDF4
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVindobona_Filter_fullperiod
import seaborn as sn

"""READ IN MGNOUT CAMS"""
foldername_ol18 = "/data1/models/nilu/SEEDS/MEGAN/2018/ol/ISOP/"  #MGNOUT_CAMS_BIG_ISOP_20190102.nc
foldername_as18 = "/data1/models/nilu/SEEDS/MEGAN/2018/assim_LAI/ISOP/"
foldername_ol19 = "/data1/models/nilu/SEEDS/MEGAN/2019/ol/ISOP/"  #MGNOUT_CAMS_BIG_ISOP_20190102.nc
foldername_as19 = "/data1/models/nilu/SEEDS/MEGAN/2019/assim_LAI/ISOP/"
foldername_ol20 = "/data1/models/nilu/SEEDS/MEGAN/2020/ol/ISOP/"  #MGNOUT_CAMS_BIG_ISOP_20190102.nc
foldername_as20 = "/data1/models/nilu/SEEDS/MEGAN/2020/assim_LAI/ISOP/"
def EmisSEEDS(foldername):
    files = os.listdir(foldername)
    files = sorted(files)
    dateaxis=[]
    Emis_max=[]
    Emis_noontime=[]
    Emis_noon=[]
    index_lat = 202  #LAT 48.25°N
    index_lon = 422 #LON 16.25°E (city rim to Wienerwald) or 421: LON 16.15°E (middle Wienerwald)
    for i in range(len(files)):
        day = str(files[i][-5:-3])  # splitlistcomp[3:4]
        month = str(files[i][-7:-5])  # splitlistcomp[2:3]
        year = "20" + str(files[i][-9:-7])  # splitlistcomp[:2]
        #print(day,month,year)
        date = datetime(year=int(year), month=int(month), day=int(day))
        #print(date)
        dateaxis.append(date)
        path = foldername+files[i]
        infile = netCDF4.Dataset(path)  #path.decode('UTF-8')  #OSError: [Errno -51] NetCDF: Unknown file format: b'/windata/DATA/models/nilu/MEGAN3_SURFEX_SEEDS/MEGAN/ol/MGNOUT_CAMS_BIG_20190803.nc'
        Emis_hourlyvalue = infile.variables['Emiss'][:, index_lat, index_lon, 0]  #TODO: only first emission layer (ISO) read in
        Emis_max.append(Emis_hourlyvalue.max())
        #print(Emis_hourlyvalue)
        #Emis_hourly.append(Emis_hourlyvalue)
        Emis_noon = np.average(Emis_hourlyvalue[8:14])
        Emis_noontime.append(Emis_noon)
    Emis_max = pd.DataFrame({'datetime': dateaxis, 'ISO': Emis_max})
    Emis_max['datetime'] = pd.to_datetime(Emis_max['datetime'])
    Emis_max = Emis_max.set_index(['datetime'])
    Emis_noontime = pd.DataFrame({'datetime': dateaxis, 'ISO': Emis_noontime})
    Emis_noontime['datetime'] = pd.to_datetime(Emis_noontime['datetime'])
    Emis_noontime = Emis_noontime.set_index(['datetime'])
    return Emis_max, Emis_noontime

#Emis_ol18, Emis_ol_noontime18 = EmisSEEDS(foldername_ol18)
#Emis_assim18, Emis_assim_noontime18 = EmisSEEDS(foldername_as18)
Emis_ol, Emis_ol_noontime = EmisSEEDS(foldername_ol19)
Emis_assim, Emis_assim_noontime = EmisSEEDS(foldername_as19)
Emis_ol20, Emis_ol_noontime20 = EmisSEEDS(foldername_ol20)
Emis_assim20, Emis_assim_noontime20 = EmisSEEDS(foldername_as20)
Emis_assim_noontime = Emis_assim_noontime.dropna()
Emis_assim_noontime20 = Emis_assim_noontime20.dropna()
print(Emis_assim_noontime20.ISO)

"read in VINDOBONA"
foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))
hcho_w = hcho_dmax.resample("W").mean()
#print(hcho_d)

"read in SIF"
tsif_r = pd.read_csv("/windata/DATA/remote/satellite/TROPOMI/TSIF_743_LAT48_196613_LON16_382294.csv", sep=",")
tsif = tsif_r.set_index(pd.to_datetime(tsif_r['time']))
tsif = tsif.drop(columns=['time'])
tsif_m =tsif.resample('M').mean()
tsif_w =tsif.resample('W').mean()
osif_757_r = pd.read_csv("/windata/DATA/remote/satellite/OCO2/OSIF_8100_757nm.csv", sep=",")
osif_757 = osif_757_r.set_index(pd.to_datetime(osif_757_r['time']))
osif_757 = osif_757.drop(columns=['time'])
osif_757_m =osif_757.resample('M').mean()
osif_757_w =osif_757.resample('W').mean()
#print(tsif.SIF)
#print(osif_757)
#exit()


'''READ IN BOKU Metdata'''
BOKUMetData = met.library.BOKUMet_Data.BOKUMet()
#print(BOKUMetData) #10min values
#DAILY MEANS
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
#DAILY MAX
BOKUMetData_dailymax = BOKUMetData_hourlymean.resample('D').agg({'DT': np.max, 'AT': np.max, 'RH': np.max, 'GR': np.max, 'WS': np.max,
                                                      'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})
#JULIAN DAY
BOKUMetData_dailysum['JD'] = (BOKUMetData_dailysum.index)
f = lambda x: datestdtojd(str(x)[:-9])
BOKUMetData_dailysum['JD'] = BOKUMetData_dailysum['JD'].apply(f)

#MONTHLY MEANS
BOKUMetData_monthly = BOKUMetData.resample('M').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                      'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_weekly = BOKUMetData_dailysum.resample('W').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                      'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

vp_sat = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3))  #kPa sh. Dingman
vp_air = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3)) * (BOKUMetData_hourlymean["RH"]/100)
vpd = vp_sat - vp_air
#print(vp_sat,vp_air, vpd)
#vpd.plot()
#plt.show()
vpd_d = vpd.resample('D').mean()
vpd_dmax = vpd.resample('D').max()
vpd_dmax_w = vpd_dmax.resample('W').max()


'''TIMESLICES'''
start = datetime(2019, 6, 1, 00, 00)
end = datetime(2019, 9, 1, 00, 00)
JJA19_s = datetime(2019, 6, 1, 00, 00)
JJA19_e = datetime(2019, 8, 31, 00, 00)
JJA20_s = datetime(2020, 6, 1, 00, 00)
JJA20_e = datetime(2020, 8, 31, 00, 00)

#fig, ax = plt.subplots(figsize=(20,5))
#sn.boxplot(x = hcho_d.index.week,y = hcho_d, ax = ax)
#plt.show()

#green triangle indicate mean value, black line meadian value, The box shows the quartiles of the dataset.
# while the whiskers extend to show the rest of the distribution, except for points that are determined to be “outliers”
# using a method that is a function of the inter-quartile range (whis=1.5)
#Maximum length of the plot whiskers is set to 1.5 times the interquartile range. the remaining data points are shown as outliers.

fig, axs = plt.subplots(nrows=4,ncols=2,sharey='row')#, sharex='col')#, figsize=(6, 6))
axs[0, 0].set_title('JJA2019')
sn.boxplot(x = hcho_d[JJA19_s:JJA19_e].index.week,y = hcho_d[JJA19_s:JJA19_e], ax = axs[0,0],showmeans=True)
axs[0, 1].set_title('JJA2020')
sn.boxplot(x = hcho_d[JJA20_s:JJA20_e].index.week,y = hcho_d[JJA20_s:JJA20_e], ax = axs[0,1],showmeans=True)

sn.boxplot(x = vpd_dmax[JJA19_s:JJA19_e].index.week,y = vpd_dmax[JJA19_s:JJA19_e], ax = axs[1,0],showmeans=True)
sn.boxplot(x = vpd_dmax[JJA20_s:JJA20_e].index.week,y = vpd_dmax[JJA20_s:JJA20_e], ax = axs[1,1],showmeans=True)

sn.boxplot(x = tsif[JJA19_s:JJA19_e].index.week,y = tsif.SIF[JJA19_s:JJA19_e], ax = axs[2,0],showmeans=True)
sn.boxplot(x = tsif[JJA20_s:JJA20_e].index.week,y = tsif.SIF[JJA20_s:JJA20_e], ax = axs[2,1],showmeans=True)

sn.boxplot(x = Emis_assim_noontime.ISO[JJA19_s:JJA19_e].index.week,y = Emis_assim_noontime.ISO[JJA19_s:JJA19_e], ax = axs[3,0],showmeans=True)
sn.boxplot(x = Emis_assim_noontime20.ISO[JJA20_s:JJA20_e].index.week,y = Emis_assim_noontime20.ISO[JJA20_s:JJA20_e], ax = axs[3,1],showmeans=True)

axs[0, 0].set_ylabel("HCHO [ppb]")#, ax=axs[:, 0])
axs[1, 0].set_ylabel("VPD [kPa]")
axs[2, 0].set_ylabel("TSIF [mW/m2/sr/nm]")
axs[3, 0].set_ylabel("ISO_mod [mol/s/m2]")
axs[3, 0].set_xlabel("weeks")
axs[3, 1].set_xlabel("weeks")

#pl1 = axs[0, 0].scatter(o3jja19['AT9STEF'], o3jja19['AT30801'], c=wdjja19, label="O3_nw", cmap='viridis') #Irnfritz
#axs[1, 0].scatter(o3jja19['AT9STEF'], o3jja19['AT31301'], c=wdjja19, label="O3_ne")  #Mistelbach
#axs[1,0].legend(loc="upper left") #axs[1, 0].set_title('NE')
#pl1 = axs[0,1].scatter(o3jja20['AT9STEF'],o3jja20['AT30801'], c=wdjja20, label="O3_nw", cmap='viridis') #Irnfritz
plt.show()
exit()
