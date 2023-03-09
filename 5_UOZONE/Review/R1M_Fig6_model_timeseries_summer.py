# -*- coding: utf-8 -*-
__author__ = 'lnx'

import os
import numpy as np
import pandas as pd
from datetime import datetime
import monthdelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from netCDF4 import Dataset as netcdf_dataset
import BOKUMet_Data
from Datetime_recipies import datestdtojd
from conversions import *
import ReadinVindobona_Filter_fullperiod

def EmisSEEDS(foldername,var,lat,lon,dim4,timestep):
    files = os.listdir(foldername)
    files = sorted(files)
    dateaxis=[]
    varh_out = []
    VAR=[]
    for i in range(len(files)):
        day = str(files[i][-5:-3])
        month = str(files[i][-7:-5])
        year = "20" + str(files[i][-9:-7])
        date = datetime(year=int(year), month=int(month), day=int(day))
        dateaxis.append(date)
        path = foldername+files[i]
        infile = netcdf_dataset(path)
        if dim4 == False and timestep=="hourly":
            varh = infile.variables[var][:,lat,lon]
            varh = np.average(varh[8:14])
            varh_out.append(varh)
        elif dim4 == False and timestep =="daily":
            varh = infile.variables[var][:,lat,lon]
            varh_out.append(varh)
        else:
            varh = infile.variables[var][:,lat,lon,0]
            #print(varh)
            varh = np.average(varh[8:14])
            #print(varh)
            varh_out.append(varh)
    #print(varh_out)
    #exit()
    #print(dateaxis)
    #varh_out = varh.mean(axis=0)
    VAR = pd.DataFrame({'datetime': dateaxis, 'VAR' : varh_out})
    VAR['datetime'] = pd.to_datetime(VAR['datetime'])
    VAR = VAR.set_index(['datetime'])
    print(VAR)
    return VAR

index_lat_city = 201 #202  #LAT 48.25°N     199/426: Leithagebirge! 202/422 city rim to Wienerwald!
index_lon_city = 424 #422 #LON 16.25°E (city rim to Wienerwald) or 421: LON 16.15°E (middle Wienerwald)
index_lat_leitha = 199
index_lon_leitha = 426
index_lat_ww = 202
index_lon_ww = 422
index_lat_lob = 201
index_lon_lob = 425
index_lat_LNeus = 196
index_lon_LNeus = 427
index_lat_Pinus = 200
index_lon_Pinus = 422
index_lat_WW2 = 201
index_lon_WW2 = 420
index_lat_WWnilu = 199
index_lon_WWnilu = 420

#foldername_sm = "/data1/models/nilu/SEEDS/SM_rootlevel_SURFEX/"
foldername_laiJJA19 = "/Users/lnx/DATA/models/NILU/LAIas_JJA19/"
foldername_laiJJA20 = "/Users/lnx/DATA/models/NILU/LAIas_JJA20/"
foldername_wgJJA19 = "/Users/lnx/DATA/models/NILU/WGas_JJA19/"
foldername_wgJJA20 = "/Users/lnx/DATA/models/NILU/WGas_JJA20/"
#foldername_isoJJA19 = "/Volumes/Expansion/data1/data1/models/nilu/SEEDS/MEGAN/2018/assim_LAI/ISOP/"
foldername_isoJJA19 ="/Users/lnx/DATA/models/NILU/MEGAN/ISO_JJA19/"
foldername_isoJJA20 ="/Users/lnx/DATA/models/NILU/MEGAN/ISO_JJA20/"

ISOJJA19_wwnilu = EmisSEEDS(foldername_isoJJA19, 'Emiss',index_lat_WWnilu, index_lon_WWnilu, True, "hourly")
ISOJJA20_wwnilu = EmisSEEDS(foldername_isoJJA20, 'Emiss',index_lat_WWnilu, index_lon_WWnilu, True,"hourly")
ISOJJA19 = EmisSEEDS(foldername_isoJJA19, 'Emiss',index_lat_ww, index_lon_ww, True, "hourly")
ISOJJA20 = EmisSEEDS(foldername_isoJJA20, 'Emiss',index_lat_ww, index_lon_ww, True,"hourly")
ISOJJA19_lob = EmisSEEDS(foldername_isoJJA19, 'Emiss',index_lat_lob, index_lon_lob, True,"hourly")
ISOJJA20_lob = EmisSEEDS(foldername_isoJJA20, 'Emiss',index_lat_lob, index_lon_lob, True,"hourly")
ISOJJA19_cen = EmisSEEDS(foldername_isoJJA19, 'Emiss',index_lat_city, index_lon_city, True,"hourly")
ISOJJA20_cen = EmisSEEDS(foldername_isoJJA20, 'Emiss',index_lat_city, index_lon_city, True,"hourly")
ISOJJA19_leitha = EmisSEEDS(foldername_isoJJA19, 'Emiss',index_lat_leitha, index_lon_leitha, True,"hourly")
ISOJJA20_leitha = EmisSEEDS(foldername_isoJJA20, 'Emiss',index_lat_leitha, index_lon_leitha, True,"hourly")


LAIJJA19_wwnilu = EmisSEEDS(foldername_laiJJA19, 'LAI_ISBA',index_lat_WWnilu, index_lon_WWnilu, False, "daily")
LAIJJA20_wwnilu = EmisSEEDS(foldername_laiJJA20, 'LAI_ISBA',index_lat_WWnilu, index_lon_WWnilu, False, "daily")
LAIJJA19 = EmisSEEDS(foldername_laiJJA19, 'LAI_ISBA',index_lat_ww, index_lon_ww, False,"daily")
LAIJJA20 = EmisSEEDS(foldername_laiJJA20, 'LAI_ISBA',index_lat_ww, index_lon_ww, False,"daily")
LAIJJA19_cen = EmisSEEDS(foldername_laiJJA19, 'LAI_ISBA',index_lat_city, index_lon_city, False,"daily")
LAIJJA20_cen = EmisSEEDS(foldername_laiJJA20, 'LAI_ISBA',index_lat_city, index_lon_city, False,"daily")
LAIJJA19_lob = EmisSEEDS(foldername_laiJJA19, 'LAI_ISBA',index_lat_lob, index_lon_lob, False,"daily")
LAIJJA20_lob = EmisSEEDS(foldername_laiJJA20, 'LAI_ISBA',index_lat_lob, index_lon_lob, False,"daily")
LAIJJA19_leitha = EmisSEEDS(foldername_laiJJA19, 'LAI_ISBA',index_lat_leitha, index_lon_leitha, False,"daily")
LAIJJA20_leitha = EmisSEEDS(foldername_laiJJA20, 'LAI_ISBA',index_lat_leitha, index_lon_leitha, False,"daily")

WGJJA19_wwnilu = EmisSEEDS(foldername_wgJJA19, 'WG5_ISBA',index_lat_WWnilu, index_lon_WWnilu, False,"hourly")
WGJJA20_wwnilu = EmisSEEDS(foldername_wgJJA20, 'WG5_ISBA',index_lat_WWnilu, index_lon_WWnilu, False,"hourly")
WGJJA19 = EmisSEEDS(foldername_wgJJA19, 'WG5_ISBA',index_lat_ww, index_lon_ww, False,"hourly")
WGJJA20 = EmisSEEDS(foldername_wgJJA20, 'WG5_ISBA',index_lat_ww, index_lon_ww, False,"hourly")
WGJJA19_cen = EmisSEEDS(foldername_wgJJA19, 'WG5_ISBA',index_lat_city, index_lon_city, False,"hourly")
WGJJA20_cen = EmisSEEDS(foldername_wgJJA20, 'WG5_ISBA',index_lat_city, index_lon_city, False,"hourly")
WGJJA19_lob = EmisSEEDS(foldername_wgJJA19, 'WG5_ISBA',index_lat_lob, index_lon_lob, False,"hourly")
WGJJA20_lob = EmisSEEDS(foldername_wgJJA20, 'WG5_ISBA',index_lat_lob, index_lon_lob, False,"hourly")
WGJJA19_leitha = EmisSEEDS(foldername_wgJJA19, 'WG5_ISBA',index_lat_leitha, index_lon_leitha, False,"hourly")
WGJJA20_leitha = EmisSEEDS(foldername_wgJJA20, 'WG5_ISBA',index_lat_leitha, index_lon_leitha, False,"hourly")


fig = plt.figure()
#plt.suptitle(f"OBS {start} - {end}")
ax1 = fig.add_subplot(311)
ax1.set_title('(a)', loc='left', size='medium')#, color='green')
ax1.plot(LAIJJA19_wwnilu["VAR"], linewidth="1", color='green', label="LAI_ww") #label="GR,sum,w"
ax1.plot(LAIJJA19_wwnilu["VAR"].index, LAIJJA20_wwnilu["VAR"].values, linewidth="1", color='green', linestyle=":")
ax1.plot(LAIJJA19["VAR"], linewidth="1", color='black', label="LAI_sp")
ax1.plot(LAIJJA19["VAR"].index, LAIJJA20["VAR"].values, linewidth="1", linestyle=":", color='black')
#ax1.plot(LAIJJA19_lob["VAR"], linewidth="1", color='blue', label="LAI_lob") 
#ax1.plot(LAIJJA19_lob["VAR"].index, LAIJJA20_lob["VAR"].values, linewidth="1", color='blue', linestyle=":")
#ax1.plot(LAIJJA19_cen["VAR"], linewidth="1", color='black', label="LAI_city")
#ax1.plot(LAIJJA19_cen["VAR"].index, LAIJJA20_cen["VAR"].values, linewidth="1", color='black', linestyle=":")
#ax1.plot(LAIJJA19_leitha["VAR"], linewidth="1", color='black', label="LAI_leitha") 
#ax1.plot(LAIJJA19_leitha["VAR"].index, LAIJJA20_leitha["VAR"].values, linewidth="1", color='black', linestyle=":")
#ax1.set_xlim(start,end)
ax1.set_ylabel("LAI [m2 m-2]", size="medium")
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1.grid()
ax1.legend(loc='upper left')

ax1 = fig.add_subplot(312)
ax1.set_title('(b)', loc='left', size='medium')
ax1.plot(WGJJA19_wwnilu["VAR"], linewidth="1", color='green', label="SM_ww") 
ax1.plot(WGJJA19_wwnilu["VAR"].index, WGJJA20_wwnilu["VAR"].values, linewidth="1", color='green', linestyle=":")
ax1.plot(WGJJA19["VAR"], linewidth="1", color='black', label="SM_sp") 
ax1.plot(WGJJA19["VAR"].index, WGJJA20["VAR"].values, linewidth="1", color='black', linestyle=":")
#ax1.plot(WGJJA19_lob["VAR"], linewidth="1", color='blue', label="SM_lob") 
#ax1.plot(WGJJA19_lob["VAR"].index, WGJJA20_lob["VAR"].values, linewidth="1", color='blue', linestyle=":")
#ax1.plot(WGJJA19_cen["VAR"], linewidth="1", color='black', label="SM_city") 
#ax1.plot(WGJJA19_cen["VAR"].index, WGJJA20_cen["VAR"].values, linewidth="1", color='black', linestyle=":")
#ax1.plot(WGJJA19_leitha["VAR"], linewidth="1", color='black', label="SM_leitha") 
#ax1.plot(WGJJA19_leitha["VAR"].index, WGJJA20_leitha["VAR"].values, linewidth="1", color='black', linestyle=":")
ax1.set_ylabel("soil liquid water content [m3 m-3]", size="medium")
ax1.legend(loc='upper left')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1.grid()

ax1 = fig.add_subplot(313)
ax1.set_title('(c)', loc='left', size='medium')
ax1.plot(ISOJJA19_wwnilu["VAR"], linewidth="1", color='green', label="ISO_ww") 
ax1.plot(ISOJJA19_wwnilu["VAR"].index, ISOJJA20_wwnilu["VAR"].values, linewidth="1", color='green', linestyle=":")
ax1.plot(ISOJJA19["VAR"], linewidth="1", color='black', label="ISO_sp") 
ax1.plot(ISOJJA19["VAR"].index, ISOJJA20["VAR"].values, linewidth="1", color='black', linestyle=":")
#ax1.plot(ISOJJA19_lob["VAR"], linewidth="1", color='blue', label="ISO_lob") 
#ax1.plot(ISOJJA19_lob["VAR"].index, ISOJJA20_lob["VAR"].values, linewidth="1", color='blue', linestyle=":")
#ax1.plot(ISOJJA19_cen["VAR"], linewidth="1", color='black', label="ISO_city") 
#ax1.plot(ISOJJA19_cen["VAR"].index, ISOJJA20_cen["VAR"].values, linewidth="1", color='black', linestyle=":")
#ax1.plot(ISOJJA19_leitha["VAR"], linewidth="1", color='black', label="ISO_leitha") 
#ax1.plot(ISOJJA19_leitha["VAR"].index, ISOJJA20_leitha["VAR"].values, linewidth="1", color='black', linestyle=":")
ax1.set_ylabel("isoprene [ppb]", size="medium")
ax1.legend(loc='upper left')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1.grid()
plt.show()

