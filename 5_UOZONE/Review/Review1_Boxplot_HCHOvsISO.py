# -*- coding: utf-8 -*-
__author__ = 'lnx'

import numpy as np
import pandas as pd
from datetime import datetime
import monthdelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVindobona_Filter_fullperiod
import os
import netCDF4
print(ugm3toppb_no2, ugm3toppb_no)
"read in VINDOBONA"
foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))
hcho_w = hcho_dmax.resample("W").mean()

"""READ IN MGNOUT CAMS"""
foldername_ol18 = "/data1/models/nilu/SEEDS/MEGAN/2018/ol/ISOP/"  #MGNOUT_CAMS_BIG_ISOP_20190102.nc
foldername_as18 = "/data1/models/nilu/SEEDS/MEGAN/2018/assim_LAI/ISOP/"
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

Emis_ol18, Emis_ol_noontime18 = EmisSEEDS(foldername_ol18)
Emis_assim18, Emis_assim_noontime18 = EmisSEEDS(foldername_as18)
#Emis_ol, Emis_ol_noontime = EmisSEEDS(foldername_ol)
#Emis_assim, Emis_assim_noontime = EmisSEEDS(foldername_as)
Emis_ol20, Emis_ol_noontime20 = EmisSEEDS(foldername_ol20)
Emis_assim20, Emis_assim_noontime20 = EmisSEEDS(foldername_as20)

ISO_MAM18 = Emis_assim_noontime18.ISO[datetime(2018, 3, 1, 00, 00): datetime(2018, 5, 31, 00, 00)]
ISO_MAM20 = Emis_assim_noontime20.ISO[datetime(2020, 3, 1, 00, 00): datetime(2020, 5, 31, 00, 00)]

'''TIMESLICES'''
MAM18_s = datetime(2018, 3, 1, 00, 00)
MAM18_e = datetime(2018, 5, 31, 00, 00)
MAM20_s = datetime(2020, 3, 1, 00, 00)
MAM20_e = datetime(2020, 5, 31, 00, 00)
JJA19_s = datetime(2019, 6, 1, 00, 00)
JJA19_e = datetime(2019, 8, 31, 00, 00)
JJA20_s = datetime(2020, 6, 1, 00, 00)
JJA20_e = datetime(2020, 8, 31, 00, 00)
'''
Plotting
'''
fs = 10  # fontsize
#hcho_d_comp = np.concatenate((hcho_d[MAM20_s:MAM20_e].values, hcho_d[MAM18_s:MAM18_e].values), axis=1)
#hcho_d_comp = np.append(hcho_d[MAM20_s:MAM20_e].values, [hcho_d[MAM18_s:MAM18_e].values], axis=1)
filtered_hcho20 = hcho_d[MAM20_s:MAM20_e].values[~np.isnan(hcho_d[MAM20_s:MAM20_e].values)]
filtered_hcho18 = hcho_d[MAM18_s:MAM18_e].values[~np.isnan(hcho_d[MAM18_s:MAM18_e].values)]


#green triangle indicate mean value, black line meadian value, The box shows the quartiles of the dataset.
#Maximum length of the plot whiskers is set to 1.5 times the interquartile range. the remaining data points are shown as outliers.

fig, axes = plt.subplots(nrows=2, ncols=2, sharey='row') #sharex='col', figsize=(6, 6))
#fig.set_size_inches(3.39,2.54)
axes[0, 0].boxplot(filtered_hcho18,showmeans=True)
axes[0, 0].set_title('MAM18_ref', fontsize=fs)
#axes[0, 0].set_ylabel(u'HCHO [ppb]', fontsize=fs)
#axes[0, 0].set_xticklabels('MAM18_dry')
axes[0, 0].set(xticklabels=(''))

axes[0, 1].boxplot(filtered_hcho20,showmeans=True)
axes[0, 1].set_title('MAM20_dry', fontsize=fs)
axes[0, 0].set_ylabel(u'OBS: HCHO [ppb]', fontsize=fs)
axes[0, 1].set(xticklabels=(''))
#axes[0, 0].set_xticks(1,labels=['MAM20_dry'])
#axes[0, 0].set(xticklabels=('DRY','REF'))

axes[1, 0].boxplot(ISO_MAM18,showmeans=True)
#axes[1, 0].set_title('MOD_MAM18_ref', fontsize=fs)
axes[1, 0].set(xticklabels=(''))
#axes[1, 0].set_ylabel(u'isoprene [mol s-1 m-2]', fontsize=fs)
#axes[1, 0].set(xticklabels=('REF'))

axes[1, 1].boxplot(ISO_MAM20,showmeans=True)
#axes[1, 1].set_title('MAM20_dry', fontsize=fs)
axes[1, 0].set_ylabel(u'MOD: isoprene [mol s-1 m-2]', fontsize=fs)
#axes[1, 1].set(xticklabels=('DRY'))
axes[1, 1].set(xticklabels=(''))

#fig.subplots_adjust(hspace=0.4)
#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure3_total_5days_vegcomp.tiff')
plt.show()
exit()
