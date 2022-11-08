# -*- coding: utf-8 -*-
__author__ = 'lnx'
import met.library.BOKUMet_Data
import numpy as np
import pandas as pd
from netCDF4 import Dataset
from netCDF4 import num2date
from datetime import datetime
import matplotlib.pyplot as plt

'''READ IN BOKU Metdata'''
BOKUMetData = met.library.BOKUMet_Data.BOKUMet() #10min values
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean, 'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean, 'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailymax = BOKUMetData_hourlymean.resample('D').agg({'DT': np.max, 'AT': np.max, 'RH': np.max, 'GR': np.max, 'WS': np.max,'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})

synop = "/windata/DATA/obs_point/met/ZAMG/DataHub/synop_UOZONE.csv"
df = pd.read_csv(synop, sep=",", skiprows=1) #47
df.columns = ['station', 'time', 'dd','ff','Tmax','T','N','Ir','Pg','RRR','VV','h','tr']
df = df.set_index(pd.to_datetime(df['time']))
df = df.drop(columns=['time'])
IS = df.loc[df['station'] == 11034]
IS_ws = IS["ff"]
IS_ws = IS_ws.resample('D').mean()

print(IS_ws)

"""HW days
90th percentile of daily mean temperature May-Sept 1990-2019"""

slice_30yr = BOKUMetData_dailysum["AT"][datetime(1990,1,1):]
#o3_2020_mda1 = o3_2020_mda1.set_index(pd.to_datetime(o3_2020_mda1['date']))

#select only May-Sept
slice_hotseason = slice_30yr[(slice_30yr.index.month >= 5) & (slice_30yr.index.month <= 9)]
slice_summer = slice_30yr[(slice_30yr.index.month >= 6) & (slice_30yr.index.month <= 8)]
slice_spring = slice_30yr[(slice_30yr.index.month >= 3) & (slice_30yr.index.month <= 5)]
print(slice_hotseason)
Tdmean_JJA_q90 = slice_summer.quantile(0.9)
Tdmean_MAM_q90 = slice_spring.quantile(0.9)
Tdmeanhot_q90 = slice_hotseason.quantile(0.9)
print(Tdmeanhot_q90)  #24.735375
print(Tdmean_JJA_q90) #25.85034722222222
print(Tdmean_MAM_q90) #25.85034722222222


'''READ in ERA5'''
file_u = "/windata/DATA/obs_grid/met/ERA5/ERA5_Eu_daily_u_component_of_wind_500hPa.nc"
file_v = "/windata/DATA/obs_grid/met/ERA5/ERA5_Eu_daily_v_component_of_wind_500hPa.nc"
era5_vie_lon=16.5
era5_vie_lat=48.25

fh_u = Dataset(file_u, mode='r')
fh_v = Dataset(file_v, mode='r')
lons = fh_u.variables['longitude'][1]
lats = fh_u.variables['latitude'][1]
era5_time = fh_u.variables['time']
#emep_o3_d = fh.variables['SURF_ppb_O3'][:,wrf_vie_j,wrf_vie_i] #(time, j, i)
jd = num2date(era5_time[:],era5_time.units)
u = fh_u.variables['u'][:,era5_vie_lat,era5_vie_lon]
v = fh_v.variables['v'][:,era5_vie_lat,era5_vie_lon]
wind_speed = np.sqrt(u**2 + v**2)
ws_d_500hpa = pd.Series(wind_speed[:],index=jd)
#print(u)
#print(v)
#print(ws_d)
#ws_d.plot()
#plt.show()



#(1)  surface wind speed < 3.2m s-1
#(2)  500mbar wind < 13m s-1
#(3)  no precipitation
#ASI_data = pd.concat([BOKUMetData_dailymax['WS'],BOKUMetData_dailysum["PC"]], axis=1)
#isHighGR = BOKUMetData_dailysum["GR"] > BOKUMetData_dailysum["GRthres"] #boolean (False/True)
#HighGRdays = BOKUMetData_dailysum[isHighGR]

#isLowWS1 = BOKUMetData_dailysum["WS"] < (3.2*3.6)  #because WS in km/h and threshold in m/s
#isLowWS1_andNoPC = (BOKUMetData_dailysum["WS"] < (3.2*3.6)) & (BOKUMetData_dailysum["PC"] == 0)
isLowWS1 = IS_ws < 32.0  #because WS in 1/10 m/s and threshold 3.2 m/s
isASI = (BOKUMetData_dailysum["PC"] == 0) & (ws_d_500hpa < 13) & (IS_ws < 32.0)
#isHW = BOKUMetData_dailysum["AT"] > Tdmeanhot_q90
isHW_MAM = BOKUMetData_dailysum["AT"] > Tdmean_MAM_q90

pd.set_option('display.max_rows', None)
out = pd.concat([isASI,isLowWS1,isHW_MAM], axis=1)
out = out[datetime(2020,6,1):datetime(2020,8,31)]
print(out)

"""
ASIdays (using IS wind), HW days (90% of season)
MAM18:  5  , 26 
MAM20:  0  , 5
JJA19:  32  , 89
JJA20:  9  , 71 
"""

"""
ASIdays (total/in periods > 4days), HW days:  USING BOKU Metwind 
MAM18:  19  / 0  , 0 
MAM19:   7  / 0  , 0
MAM20:  16  / 0  , 0
JJA19:  41  / 26 , 15
JJA20:  33 / 9   , 6
"""


#BOKUMetData_dailysum["WS"].plot()
#plt.show()
exit()

#pff_full = pd.concat([hcho_dmax,vpd_dmax, rss_sub["RSS_sub_grass"], rss_sub["RSS_sub_wWheat"], BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"],HighGRdays["GR"], sif_join,
#                o3_1990_2020_da["AT9STEF"],BOKUMetData_dailysum["WD"],BOKUMetData_dailysum["WS"], BOKUMetData_dailysum["PC"],pbl["PBL"]], axis=1)
#pff_full.columns = ['hcho', 'vpd', 'RSSg', 'RSSw', 'AT', 'GR', 'GRhigh', 'SIF', 'O3','WD','WS','PC','PBL']
#pff_clear = pff_full.dropna(subset=['GRhigh'])
#print(pff_clear)
#pff_clear2 = pff_clear.loc[pff_clear["GR"] >= 4500]
#pff_clear2_o3high = pff_clear2.loc[pff_clear2["O3"] > 100]

exit()

