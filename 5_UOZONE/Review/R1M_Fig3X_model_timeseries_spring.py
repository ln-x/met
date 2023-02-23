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

#TODO extract daily timeserie

def EmisSEEDS(foldername,var,lat,lon,dim4, timestep):
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
    VAR = pd.DataFrame({'datetime': dateaxis, 'VAR' : varh_out})
    VAR['datetime'] = pd.to_datetime(VAR['datetime'])
    VAR = VAR.set_index(['datetime'])
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

foldername_laiMAM18 = "/Users/lnx/DATA/models/NILU/LAIas_MAM18/"
foldername_laiMAM20 = "/Users/lnx/DATA/models/NILU/LAIas_MAM20/"
foldername_wgMAM18 = "/Users/lnx/DATA/models/NILU/WGas_MAM18/"
foldername_wgMAM20 = "/Users/lnx/DATA/models/NILU/WGas_MAM20/"
foldername_isoMAM18 ="/Users/lnx/DATA/models/NILU/MEGAN/ISO_MAM18/"
foldername_isoMAM20 ="/Users/lnx/DATA/models/NILU/MEGAN/ISO_MAM20/"

ISOMAM18 = EmisSEEDS(foldername_isoMAM18, 'Emiss',index_lat_ww, index_lon_ww, True, "hourly")
ISOMAM20 = EmisSEEDS(foldername_isoMAM20, 'Emiss',index_lat_ww, index_lon_ww, True,"hourly")
ISOMAM18_lob = EmisSEEDS(foldername_isoMAM18, 'Emiss',index_lat_lob, index_lon_lob, True,"hourly")
ISOMAM20_lob = EmisSEEDS(foldername_isoMAM20, 'Emiss',index_lat_lob, index_lon_lob, True,"hourly")
ISOMAM18_cen = EmisSEEDS(foldername_isoMAM18, 'Emiss',index_lat_city, index_lon_city, True,"hourly")
ISOMAM20_cen = EmisSEEDS(foldername_isoMAM20, 'Emiss',index_lat_city, index_lon_city, True,"hourly")
ISOMAM18_leitha = EmisSEEDS(foldername_isoMAM18, 'Emiss',index_lat_leitha, index_lon_leitha, True,"hourly")
ISOMAM20_leitha = EmisSEEDS(foldername_isoMAM20, 'Emiss',index_lat_leitha, index_lon_leitha, True,"hourly")

LAIMAM18 = EmisSEEDS(foldername_laiMAM18, 'LAI_ISBA',index_lat_ww, index_lon_ww, False, "daily")
LAIMAM20 = EmisSEEDS(foldername_laiMAM20, 'LAI_ISBA',index_lat_ww, index_lon_ww, False, "daily")
LAIMAM18_cen = EmisSEEDS(foldername_laiMAM18, 'LAI_ISBA',index_lat_city, index_lon_city, False,"daily")
LAIMAM20_cen = EmisSEEDS(foldername_laiMAM20, 'LAI_ISBA',index_lat_city, index_lon_city, False,"daily")
LAIMAM18_lob = EmisSEEDS(foldername_laiMAM18, 'LAI_ISBA',index_lat_lob, index_lon_lob, False,"daily")
LAIMAM20_lob = EmisSEEDS(foldername_laiMAM20, 'LAI_ISBA',index_lat_lob, index_lon_lob, False,"daily")
LAIMAM18_leitha = EmisSEEDS(foldername_laiMAM18, 'LAI_ISBA',index_lat_leitha, index_lon_leitha, False,"daily")
LAIMAM20_leitha = EmisSEEDS(foldername_laiMAM20, 'LAI_ISBA',index_lat_leitha, index_lon_leitha, False,"daily")

WGMAM18 = EmisSEEDS(foldername_wgMAM18, 'WG5_ISBA',index_lat_ww, index_lon_ww, False,"hourly")
WGMAM20 = EmisSEEDS(foldername_wgMAM20, 'WG5_ISBA',index_lat_ww, index_lon_ww, False,"hourly")
WGMAM18_cen = EmisSEEDS(foldername_wgMAM18, 'WG5_ISBA',index_lat_city, index_lon_city, False,"hourly")
WGMAM20_cen = EmisSEEDS(foldername_wgMAM20, 'WG5_ISBA',index_lat_city, index_lon_city, False,"hourly")
WGMAM18_lob = EmisSEEDS(foldername_wgMAM18, 'WG5_ISBA',index_lat_lob, index_lon_lob, False,"hourly")
WGMAM20_lob = EmisSEEDS(foldername_wgMAM20, 'WG5_ISBA',index_lat_lob, index_lon_lob, False,"hourly")
WGMAM18_leitha = EmisSEEDS(foldername_wgMAM18, 'WG5_ISBA',index_lat_leitha, index_lon_leitha, False,"hourly")
WGMAM20_leitha = EmisSEEDS(foldername_wgMAM20, 'WG5_ISBA',index_lat_leitha, index_lon_leitha, False,"hourly")

'''TIMESLICES'''
MAM18_s = datetime(2018, 3, 1, 00, 00)
MAM18_e = datetime(2018, 5, 31, 00, 00)
MAM18_e2 = datetime(2018, 6, 7, 00, 00)
MAM20_s = datetime(2020, 3, 1, 00, 00)
MAM20_e = datetime(2020, 5, 31, 00, 00)
MAM20_e2 = datetime(2020, 6, 1, 00, 00)

fig = plt.figure()
#plt.suptitle(f"OBS {start} - {end}")
ax1 = fig.add_subplot(311)
ax1.set_title('(a)', loc='left', size='medium')#, color='green')
ax1.plot(LAIMAM20["VAR"], linewidth="1", color='green', label="LAI") #label="GR,sum,w"
ax1.plot(LAIMAM20["VAR"].index, LAIMAM18["VAR"].values, linewidth="1", color='green', linestyle=":")
ax1.plot(LAIMAM20_cen["VAR"], linewidth="1", color='orange', label="LAI_city")
ax1.plot(LAIMAM20_cen["VAR"].index, LAIMAM18_cen["VAR"].values, linewidth="1", color='orange', linestyle=":")
ax1.plot(LAIMAM20_lob["VAR"], linewidth="1", color='blue', label="LAI_lob") 
ax1.plot(LAIMAM20_lob["VAR"].index, LAIMAM18_lob["VAR"].values, linewidth="1", color='blue', linestyle=":")
ax1.plot(LAIMAM20_leitha["VAR"], linewidth="1", color='black', label="LAI_leitha") 
ax1.plot(LAIMAM20_leitha["VAR"].index, LAIMAM18_leitha["VAR"].values, linewidth="1", color='black', linestyle=":")
#ax1.set_xlim(start,end)
ax1.set_ylabel("LAI [m2 m-2]", size="medium")
#ax1.set_xlim(start,end)
ax1.set_ylabel("[]", size="medium")
ax1.xaxis.set_major_formatter(mdates.DateFormatter(' '))
ax1.grid()
ax1.legend(loc='upper left')

ax1 = fig.add_subplot(312)
ax1.set_title('(b)', loc='left', size='medium')
ax1.plot(WGMAM20["VAR"], linewidth="1", color='green', label="SM_ww") 
ax1.plot(WGMAM20["VAR"].index, WGMAM18["VAR"].values, linewidth="1", color='green', linestyle=":")
ax1.plot(WGMAM20_lob["VAR"], linewidth="1", color='blue', label="SM_lob") 
ax1.plot(WGMAM20_lob["VAR"].index, WGMAM18_lob["VAR"].values, linewidth="1", color='blue', linestyle=":")
ax1.plot(WGMAM20_cen["VAR"], linewidth="1", color='orange', label="SM_ww") 
ax1.plot(WGMAM20_cen["VAR"].index, WGMAM18_cen["VAR"].values, linewidth="1", color='orange', linestyle=":")
ax1.plot(WGMAM20_leitha["VAR"], linewidth="1", color='black', label="SM_leitha") 
ax1.plot(WGMAM20_leitha["VAR"].index, WGMAM18_leitha["VAR"].values, linewidth="1", color='black', linestyle=":")
ax1.set_ylabel("soil liquid water content [m3 m-3]", size="medium")
ax1.legend(loc='upper left')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1.grid()

ax1 = fig.add_subplot(313)
ax1.set_title('(b)', loc='left', size='medium')
ax1.plot(ISOMAM20["VAR"], linewidth="1", color='green', label="ISO_ww") 
ax1.plot(ISOMAM20["VAR"].index, ISOMAM18["VAR"].values, linewidth="1", color='green', linestyle=":")
ax1.plot(ISOMAM20_lob["VAR"], linewidth="1", color='blue', label="ISO_lob") 
ax1.plot(ISOMAM20_lob["VAR"].index, ISOMAM18_lob["VAR"].values, linewidth="1", color='blue', linestyle=":")
ax1.plot(ISOMAM20_cen["VAR"], linewidth="1", color='orange', label="ISO_ww") 
ax1.plot(ISOMAM20_cen["VAR"].index, ISOMAM18_cen["VAR"].values, linewidth="1", color='orange', linestyle=":")
ax1.plot(ISOMAM20_leitha["VAR"], linewidth="1", color='black', label="ISO_leitha") 
ax1.plot(ISOMAM20_leitha["VAR"].index, ISOMAM18_leitha["VAR"].values, linewidth="1", color='black', linestyle=":")
ax1.set_ylabel("isoprene [ppb]", size="medium")
ax1.legend(loc='upper left')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1.grid()
plt.show()

