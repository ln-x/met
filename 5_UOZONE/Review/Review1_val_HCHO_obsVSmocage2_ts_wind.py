# -*- coding: utf-8 -*-
__author__ = 'lnx'

import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
import netCDF4
from met.library import ReadinVindobona_Filter_fullperiod
from scipy import stats
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
from dateutil import rrule
import met.library.BOKUMet_Data
import matplotlib.dates as mdates

"""READ IN """
foldername_ol = "/data1/models/nilu/SEEDS/MEGAN/2019/ol/ISOP/"  #MGNOUT_CAMS_BIG_ISOP_20190102.nc
foldername_as = "/data1/models/nilu/SEEDS/MEGAN/2019/assim_LAI/ISOP/"
foldername_as_moc = "/data1/models/mocage/assim/"  #hmmacc01+Jun-2019.nc, hmmacc01+Jul-2019.nc
filename_as_moc_jun = "/data1/models/mocage/assim/hmmacc01+Jun-2019.nc"
filename_as_moc_jul = "/data1/models/mocage/assim/hmmacc01+Jul-2019.nc"
filename_as_moc_aug = "/data1/models/mocage/assim/hmmacc01+Aug-2019.nc"

def ReadinMocage(path, starttime, index_lat, index_lon):
    infile = netCDF4.Dataset(path)
    HCHO_moc = infile.variables['HCHO_47'][:, index_lat, index_lon]
    ISO_moc = infile.variables['ISO_47'][:, index_lat, index_lon]
    O3_moc = infile.variables['O_x_47'][:, index_lat, index_lon]
    time = infile.variables['time'][:]
    timeaxis = pd.date_range(starttime, periods=len(time), freq="H")
    MOC_out = pd.DataFrame({'datetime': timeaxis, 'ISO': ISO_moc, 'HCHO': HCHO_moc,'O3': O3_moc})
    MOC_out['datetime'] = pd.to_datetime(MOC_out['datetime'])
    MOC_out = MOC_out.set_index(['datetime'])
    return MOC_out

index_lat_city = 201 #202  #LAT 48.25°N     199/426: Leithagebirge! 202/422 city rim to Wienerwald!
index_lon_city = 424 #422 #LON 16.25°E (city rim to Wienerwald) or 421: LON 16.15°E (middle Wienerwald)
index_lat_leitha = 199
index_lon_leitha = 426
index_lat_ww = 202 #default index
index_lon_ww = 422 #default index
index_lat_lob = 201
index_lon_lob = 425
index_lat_LNeus = 196
index_lon_LNeus = 427
index_lat_Pinus = 200
index_lon_Pinus = 422
index_lat_WW2 = 201
index_lon_WW2 = 420

MOC_out_jun19_h = ReadinMocage(filename_as_moc_jun,datetime.datetime(2019,6,1,0,0),index_lat_lob, index_lon_lob)
MOC_out_jul19_h = ReadinMocage(filename_as_moc_jul,datetime.datetime(2019,7,1,0,0),index_lat_lob, index_lon_lob)
MOC_out_aug19_h = ReadinMocage(filename_as_moc_aug,datetime.datetime(2019,8,1,0,0),index_lat_lob, index_lon_lob)
MOC_HCHO_LOB = pd.concat([MOC_out_jun19_h, MOC_out_jul19_h, MOC_out_aug19_h])
MOC_HCHO_LOB_d = MOC_HCHO_LOB.resample("D").mean()

MOC_out_jun19_h_WWw = ReadinMocage(filename_as_moc_jun,datetime.datetime(2019,6,1,0,0),index_lat_WW2, index_lon_WW2)
MOC_out_jul19_h_WWw = ReadinMocage(filename_as_moc_jul,datetime.datetime(2019,7,1,0,0),index_lat_WW2, index_lon_WW2)
MOC_out_aug19_h_WWw = ReadinMocage(filename_as_moc_aug,datetime.datetime(2019,8,1,0,0),index_lat_WW2, index_lon_WW2)
MOC_HCHO_WWw = pd.concat([MOC_out_jun19_h_WWw, MOC_out_jul19_h_WWw, MOC_out_aug19_h_WWw])
#print(MOC_out_aug19_h_WWw.HCHO)
MOC_HCHO_WWw_d = MOC_HCHO_WWw.resample("D").mean()
#print(MOC_HCHO_LOB_d.HCHO, MOC_HCHO_WWw_d.HCHO)


"read in VINDOBONA"
foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_f, hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D",begin = datetime.datetime(2017, 5, 1, 0, 0, 0))
print(hcho_f.hcho)

'''READ IN BOKU Metdata'''
BOKUMetData = met.library.BOKUMet_Data.BOKUMet()
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

#BOKUMetData_hourlymean["WD"] = BOKUMetData_hourlymean["WD"].fillna(-1)
#BOKUMetData_hourlymean["WD"] = BOKUMetData_hourlymean["WD"].astype('int', errors='ignore')
start1,end1 = datetime.datetime(2019, 6, 30, 18, 00), datetime.datetime(2019, 7, 1, 23, 00)
start2,end2 = datetime.datetime(2019, 7, 19, 18, 00), datetime.datetime(2019, 7, 20, 23, 00)
start3,end3 = datetime.datetime(2019, 7, 24, 18, 00), datetime.datetime(2019, 7, 25, 23, 00)
start4,end4 = datetime.datetime(2019, 7, 25, 18, 00), datetime.datetime(2019, 7, 26, 23, 00)

print(BOKUMetData_hourlymean["WD"][start2:end2])
BOKUMetData_hourlymean["WD"] = BOKUMetData_hourlymean["WD"].apply(np.round).astype('Int64')
wd = BOKUMetData_hourlymean["WD"]
print(wd[start2:end2])

exit()
ws = BOKUMetData_hourlymean["WS"]
#print(wd, ws)
print(ws[start2:end2].index.hour)

fig, ax = plt.subplots(nrows=2, ncols=2, sharey=True)#, sharex=True)
ax[0,0].set_title('Jul1')  # \n SRho{:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')
ax[0,1].set_title('Jul20')
ax[1,0].set_title('Jul25')
ax[1,1].set_title('Jul26')
plt1= ax[0,0].scatter(ws[start1:end1].index,ws[start1:end1].values, c=wd[start1:end1], cmap="hsv", label="ws")
plt2 = ax[0,1].scatter(ws[start2:end2].index,ws[start2:end2].values, c=wd[start2:end2],cmap="hsv", label="ws")
plt3 = ax[1,0].scatter(ws[start3:end3].index,ws[start3:end3].values, c=wd[start3:end3],cmap="hsv", label="ws")
plt4 = ax[1,1].scatter(ws[start4:end4].index,ws[start4:end4].values, c=wd[start4:end4],cmap="hsv", label="ws")
legend1 = ax[0,0].legend(*plt1.legend_elements(), loc="upper left", title="WD [°]",ncol=4)
ax[0,0].add_artist(legend1)
legend1b = ax[0,1].legend(*plt2.legend_elements(), loc="upper left", title="WD [°]",ncol=4)
ax[0,1].add_artist(legend1b)
legend1c = ax[1,0].legend(*plt3.legend_elements(), loc="upper left", title="WD [°]",ncol=4)
ax[1,0].add_artist(legend1c)
legend1d = ax[1,1].legend(*plt4.legend_elements(), loc="upper left", title="WD [°]",ncol=4)
ax[1,1].add_artist(legend1d)
#ax[0,0].plot(hcho_f.hcho[start1:end1], color="black", label="HCHO_obs")
#ax[0,0].plot(MOC_out_jul19_h[datetime.datetime(2019, 7, 1, 0, 0):datetime.datetime(2019, 7, 1, 23, 0)], color="violet", label="HCHO_moc")
#ax[0,1].plot(hcho_f.hcho[start2:end2], color="black")
#ax[1,0].plot(hcho_f.hcho[start3:end3], color="black")
#ax[1,1].plot(hcho_f.hcho[start4:end4], color="black")
#ax[0,0].legend(loc="upper right")
ax[0,0].set_ylabel("wind speed [m/s]")
ax[1,0].set_ylabel("wind speed [m/s]")
#fig.tight_layout()
# for ax in fig.get_axes():
#    ax.set_xlim(0, 6)
#    ax.set_ylim(0, 6E-8)
ax[0,0].set_xticks(ws[start1:end1].index)
ax[0,0].set_xticklabels(ws[start1:end1].index.hour, rotation = 90)
ax[0,1].set_xticks(ws[start2:end2].index)
ax[0,1].set_xticklabels(ws[start2:end2].index.hour, rotation = 90)
ax[1,0].set_xticks(ws[start3:end3].index)
ax[1,0].set_xticklabels(ws[start3:end3].index.hour, rotation = 90)
ax[1,1].set_xticks(ws[start4:end4].index)
ax[1,1].set_xticklabels(ws[start4:end4].index.hour, rotation = 90)
ax[0,0].grid(linewidth=0.1)
ax[0,1].grid(linewidth=0.1)
ax[1,0].grid(linewidth=0.1)
ax[1,1].grid(linewidth=0.1)
ax[0,0].axvline(x = datetime.datetime(2019,7,1,0,0,0), color = 'r', linewidth=0.3)#, label = 'axvline - full height')
ax[0,1].axvline(x = datetime.datetime(2019,7,20,0,0,0), color = 'r', linewidth=0.3)#, label = 'axvline - full height')
ax[1,0].axvline(x = datetime.datetime(2019,7,25,0,0,0), color = 'r', linewidth=0.3)#, label = 'axvline - full height')
ax[1,1].axvline(x = datetime.datetime(2019,7,26,0,0,0), color = 'r', linewidth=0.3)#, label = 'axvline - full height')

#hour_locator = mdates.HourLocator(interval=1)
#ax[0,0].xaxis.set_major_locator(hour_locator)
#fig.autofmt_xdate()
#ax[0,0].xaxis.set_major_formatter(mdates.DateFormatter('%h'))
plt.show()
exit()
def Plot6var():
    fig, ax = plt.subplots(nrows=1, ncols=1, sharey=True)
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    ax.set_title('')# \n SRho{:.2f} \n p={:.2f}'.format(SRho05, Sp05), fontsize='small')
    ax1.plot(hcho_d[datetime.datetime(2019,6,1,0,0):datetime.datetime(2019,8,31,0,0)], color="black", label="HCHO_obs") #linestyle="", marker="o",
    ax2.plot(MOC_HCHO_LOB_d.HCHO, color="purple", label="HCHO_mod LOB")
    #ax1.plot(MOC_out_jul19_h.HCHO, color="purple")
    #ax1.plot(MOC_out_aug19_h.HCHO, color="purple")
    ax2.plot(MOC_HCHO_WWw_d.HCHO, color="green", label="HCHO_mod WW_west")
    ax1.set_xlabel("[ppb] ", size="small")
    ax1.set_ylim(0, 5E-9)
    ax2.set_ylim(0, 5E-9)
    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")
    fig.tight_layout()
    #for ax in fig.get_axes():
    #    ax.set_xlim(0, 6)
    #    ax.set_ylim(0, 6E-8)
    plt.show()

Plot6var()

