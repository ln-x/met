# -*- coding: utf-8 -*-
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
import xarray
import os
import wrf
import matplotlib.dates as mdates
from wrf import to_np, getvar, get_basemap, latlon_coords



"""
 Diurnal Plot of median VAR with BOXPLOT of MIN & MAX VAR 
 
"""



def DataArray_to_dataframe(array1, array2, array3):
    """
    Converts 3 DataArrays with metadata to an pandas DataFrame
    & drops XTIME so it can calculate the temporal means betweens he columns
    
    Input: 3 DataArray
    Output: 1 Dataframe, Mean of Columns
    """
    frame = array1.to_dataframe()
    frame[str(array2.name)] = array2.to_series()
    frame[str(array3.name)] = array3.to_series()
    #frame = frame.drop(columns=['XTIME'])
    #mean = frame.mean(axis=1)
    return frame #, mean

def DataArray_drop_to_Frame(array1, array2, array3):
    """
    Converts 3 DataArrays with metadata to an pandas DataFrame
    & drops XTIME so it can calculate the temporal means betweens he columns
    
    Input: 3 DataArray
    Output: 1 Dataframe, Mean of Columns
    """
    frame = array1.to_dataframe()
    frame[str(array2.name)] = array2.to_series()
    frame[str(array3.name)] = array3.to_series()
    #frame = frame.drop(columns=['XTIME'])
    frame = frame.drop(columns=['XLONG'])
    frame = frame.drop(columns=['XLAT'])
    #mean = frame.mean(axis=1)
    return frame #, mean

def arr_rename(liste, atts, text):
    for idx, val in enumerate(liste):
        ar = val.rename(str(atts[idx].name) + ' ' + str(text))
        liste[idx] = ar
    return liste

# EXAMPLE
# plot 30-year mean of precipitation dataset
# load data as xarray dataset
date = '2069-07-01'
domain = 'd03'
run = 'REF_Run_2069'
run1 = 'SPR_Run_2069'
run2 = 'OPT_Run_2069'
path = '/hp4/Urbania/WRF-2019-Runs/' # runPATH
filepath = path + run + '/'
filepath1 = path + run1 + '/'
filepath2 = path + run2 + '/'
para = 'T2'

cuttime = pd.to_datetime(['2069-7-1','2069-7-2','2069-7-3','2069-7-4','2069-7-5', '2069-7-6','2069-7-9']) # day with not usable data


filenam = 'wrfout_' + domain + '_' + date + '_18_00_00.nc'
plot_dir ='/hp4/Urbania/plots/' + date + '/'
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)

ncfile = Dataset(filepath + filenam)
ncfile1 = Dataset(filepath1 + filenam)
ncfile2 = Dataset(filepath2 + filenam)
#ncfile2 = Dataset(filepath2 + filenam)
#Dimension of domain
data = getvar(ncfile, para, timeidx=wrf.ALL_TIMES)
data_max = (data.max()/10).round()*10
data_min = (data.min()/10).round()*10
data1 = getvar(ncfile1, para, timeidx=wrf.ALL_TIMES)
data2 = getvar(ncfile2, para, timeidx=wrf.ALL_TIMES)

times = getvar(ncfile1, "Times", timeidx=wrf.ALL_TIMES, meta=False) # FC times in np.datetime64 format - very ugly
init = pd.to_datetime(times[0]) # converts the numpy datetime to datetime datetime format
init = str(init) # initial time of wrf dataset
spinup = pd.Timedelta('3 days') # spinup time for wrf and espacially TEB Canopy Temperatures
currtime = pd.to_datetime(times[0]) + spinup # starttime of period which is used

#%%
# Spacial and temporal selection of reference AREAS
NO = data.isel(south_north=slice(73,82), west_east=slice(89,98))
CE = data.isel(south_north=slice(50,59), west_east=slice(80,89))
RU = data.isel(south_north=slice(57,66), west_east=slice(128,137))
SA = data.isel(south_north=slice(58,67), west_east=slice(109,118))
SE = data.isel(south_north=slice(37,46), west_east=slice(99,108))
SX = data.isel(south_north=slice(24,33), west_east=slice(75,84))
SI = data.isel(south_north=slice(31,40), west_east=slice(68,77))
VW = data.isel(south_north=slice(47,56), west_east=slice(64,73))
WE = data.isel(south_north=slice(62,71), west_east=slice(73,82))

NO1 = data1.isel(south_north=slice(73,82), west_east=slice(89,98))
CE1 = data1.isel(south_north=slice(50,59), west_east=slice(80,89))
RU1 = data1.isel(south_north=slice(57,66), west_east=slice(128,137))
SA1 = data1.isel(south_north=slice(58,67), west_east=slice(109,118))
SE1 = data1.isel(south_north=slice(37,46), west_east=slice(99,108))
SX1 = data1.isel(south_north=slice(24,33), west_east=slice(75,84))
SI1 = data1.isel(south_north=slice(31,40), west_east=slice(68,77))
VW1 = data1.isel(south_north=slice(47,56), west_east=slice(64,73))
WE1 = data1.isel(south_north=slice(62,71), west_east=slice(73,82))

NO2 = data2.isel(south_north=slice(73,82), west_east=slice(89,98))
CE2 = data2.isel(south_north=slice(50,59), west_east=slice(80,89))
RU2 = data2.isel(south_north=slice(57,66), west_east=slice(128,137))
SA2 = data2.isel(south_north=slice(58,67), west_east=slice(109,118))
SE2 = data2.isel(south_north=slice(37,46), west_east=slice(99,108))
SX2 = data2.isel(south_north=slice(24,33), west_east=slice(75,84))
SI2 = data2.isel(south_north=slice(31,40), west_east=slice(68,77))
VW2 = data2.isel(south_north=slice(47,56), west_east=slice(64,73))
WE2 = data2.isel(south_north=slice(62,71), west_east=slice(73,82))


#%%
# remove not usable data
for i in cuttime:
    NO = NO.where(NO['Time'].dt.day != i.day, drop=True).rename('NO ref')
    CE = CE.where(CE['Time'].dt.day != i.day, drop=True).rename('CE ref')
    RU = RU.where(RU['Time'].dt.day != i.day, drop=True).rename('RU ref')
    SA = SA.where(SA['Time'].dt.day != i.day, drop=True).rename('SA ref')
    SE = SE.where(SE['Time'].dt.day != i.day, drop=True).rename('SE ref')
    SX = SX.where(SX['Time'].dt.day != i.day, drop=True).rename('SX ref')
    SI = SI.where(SI['Time'].dt.day != i.day, drop=True).rename('SI ref')
    VW = VW.where(VW['Time'].dt.day != i.day, drop=True).rename('VW ref')
    WE = WE.where(WE['Time'].dt.day != i.day, drop=True).rename('WE ref')
    
    NO1 = NO1.where(NO1['Time'].dt.day != i.day, drop=True).rename('NO spr')
    CE1 = CE1.where(CE1['Time'].dt.day != i.day, drop=True).rename('CE spr')
    RU1 = RU1.where(RU1['Time'].dt.day != i.day, drop=True).rename('RU spr')
    SA1 = SA1.where(SA1['Time'].dt.day != i.day, drop=True).rename('SA spr')
    SE1 = SE1.where(SE1['Time'].dt.day != i.day, drop=True).rename('SE spr')
    SX1 = SX1.where(SX1['Time'].dt.day != i.day, drop=True).rename('SX spr')
    SI1 = SI1.where(SI1['Time'].dt.day != i.day, drop=True).rename('SI spr')
    VW1 = VW1.where(VW1['Time'].dt.day != i.day, drop=True).rename('VW spr')
    WE1 = WE1.where(WE1['Time'].dt.day != i.day, drop=True).rename('WE spr')
    
    NO2 = NO2.where(NO2['Time'].dt.day != i.day, drop=True).rename('NO opt')
    CE2 = CE2.where(CE2['Time'].dt.day != i.day, drop=True).rename('CE opt')
    RU2 = RU2.where(RU2['Time'].dt.day != i.day, drop=True).rename('RU opt')
    SA2 = SA2.where(SA2['Time'].dt.day != i.day, drop=True).rename('SA opt')
    SE2 = SE2.where(SE2['Time'].dt.day != i.day, drop=True).rename('SE opt')
    SX2 = SX2.where(SX2['Time'].dt.day != i.day, drop=True).rename('SX opt')
    SI2 = SI2.where(SI2['Time'].dt.day != i.day, drop=True).rename('SI opt')
    VW2 = VW2.where(VW2['Time'].dt.day != i.day, drop=True).rename('VW opt')
    WE2 = WE2.where(WE2['Time'].dt.day != i.day, drop=True).rename('WE opt')

#%%
#calculation of TAGESGANG mean & std
NO_diurnal_mean = NO.groupby(NO.Time.dt.hour).median()
CE_diurnal_mean = CE.groupby(CE.Time.dt.hour).median()
RU_diurnal_mean = RU.groupby(RU.Time.dt.hour).median()
SA_diurnal_mean = SA.groupby(SA.Time.dt.hour).median()
SE_diurnal_mean = SE.groupby(SE.Time.dt.hour).median()
SX_diurnal_mean = SX.groupby(SX.Time.dt.hour).median()
SI_diurnal_mean = SI.groupby(SI.Time.dt.hour).median()
VW_diurnal_mean = VW.groupby(VW.Time.dt.hour).median()
WE_diurnal_mean = WE.groupby(WE.Time.dt.hour).median()

NO_diurnal_min = NO.groupby(NO.Time.dt.day).min(axis=0)
CE_diurnal_min = CE.groupby(CE.Time.dt.day).min(axis=0)
RU_diurnal_min = RU.groupby(RU.Time.dt.day).min(axis=0)
SA_diurnal_min = SA.groupby(SA.Time.dt.day).min(axis=0)
SE_diurnal_min = SE.groupby(SE.Time.dt.day).min(axis=0)
SX_diurnal_min = SX.groupby(SX.Time.dt.day).min(axis=0)
SI_diurnal_min = SI.groupby(SI.Time.dt.day).min(axis=0)
VW_diurnal_min = VW.groupby(VW.Time.dt.day).min(axis=0)
WE_diurnal_min = WE.groupby(WE.Time.dt.day).min(axis=0)

NO_diurnal_max = NO.groupby(NO.Time.dt.day).max(axis=0)
CE_diurnal_max = CE.groupby(CE.Time.dt.day).max(axis=0)
RU_diurnal_max = RU.groupby(RU.Time.dt.day).max(axis=0)
SA_diurnal_max = SA.groupby(SA.Time.dt.day).max(axis=0)
SE_diurnal_max = SE.groupby(SE.Time.dt.day).max(axis=0)
SX_diurnal_max = SX.groupby(SX.Time.dt.day).max(axis=0)
SI_diurnal_max = SI.groupby(SI.Time.dt.day).max(axis=0)
VW_diurnal_max = VW.groupby(VW.Time.dt.day).max(axis=0)
WE_diurnal_max = WE.groupby(WE.Time.dt.day).max(axis=0)

#times = NO_diurnal_mean.hour
times = pd.date_range('08/08/2015 00:00:00', '08/08/2015 23:00:00', freq='H')


NO1_diurnal_mean = NO1.groupby(NO1.Time.dt.hour).median()
CE1_diurnal_mean = CE1.groupby(CE1.Time.dt.hour).median()
RU1_diurnal_mean = RU1.groupby(RU1.Time.dt.hour).median()
SA1_diurnal_mean = SA1.groupby(SA1.Time.dt.hour).median()
SE1_diurnal_mean = SE1.groupby(SE1.Time.dt.hour).median()
SX1_diurnal_mean = SX1.groupby(SX1.Time.dt.hour).median()
SI1_diurnal_mean = SI1.groupby(SI1.Time.dt.hour).median()
VW1_diurnal_mean = VW1.groupby(VW1.Time.dt.hour).median()
WE1_diurnal_mean = WE1.groupby(WE1.Time.dt.hour).median()

NO1_diurnal_min = NO1.groupby(NO1.Time.dt.day).min(axis=0)
CE1_diurnal_min = CE1.groupby(CE1.Time.dt.day).min(axis=0)
RU1_diurnal_min = RU1.groupby(RU1.Time.dt.day).min(axis=0)
SA1_diurnal_min = SA1.groupby(SA1.Time.dt.day).min(axis=0)
SE1_diurnal_min = SE1.groupby(SE1.Time.dt.day).min(axis=0)
SX1_diurnal_min = SX1.groupby(SX1.Time.dt.day).min(axis=0)
SI1_diurnal_min = SI1.groupby(SI1.Time.dt.day).min(axis=0)
VW1_diurnal_min = VW1.groupby(VW1.Time.dt.day).min(axis=0)
WE1_diurnal_min = WE1.groupby(WE1.Time.dt.day).min(axis=0)

NO1_diurnal_max = NO1.groupby(NO1.Time.dt.day).max(axis=0)
CE1_diurnal_max = CE1.groupby(CE1.Time.dt.day).max(axis=0)
RU1_diurnal_max = RU1.groupby(RU1.Time.dt.day).max(axis=0)
SA1_diurnal_max = SA1.groupby(SA1.Time.dt.day).max(axis=0)
SE1_diurnal_max = SE1.groupby(SE1.Time.dt.day).max(axis=0)
SX1_diurnal_max = SX1.groupby(SX1.Time.dt.day).max(axis=0)
SI1_diurnal_max = SI1.groupby(SI1.Time.dt.day).max(axis=0)
VW1_diurnal_max = VW1.groupby(VW1.Time.dt.day).max(axis=0)
WE1_diurnal_max = WE1.groupby(WE1.Time.dt.day).max(axis=0)



NO2_diurnal_mean = NO2.groupby(NO2.Time.dt.hour).median()
CE2_diurnal_mean = CE2.groupby(CE2.Time.dt.hour).median()
RU2_diurnal_mean = RU2.groupby(RU2.Time.dt.hour).median()
SA2_diurnal_mean = SA2.groupby(SA2.Time.dt.hour).median()
SE2_diurnal_mean = SE2.groupby(SE2.Time.dt.hour).median()
SX2_diurnal_mean = SX2.groupby(SX2.Time.dt.hour).median()
SI2_diurnal_mean = SI2.groupby(SI2.Time.dt.hour).median()
VW2_diurnal_mean = VW2.groupby(VW2.Time.dt.hour).median()
WE2_diurnal_mean = WE2.groupby(WE2.Time.dt.hour).median()

NO2_diurnal_min = NO2.groupby(NO2.Time.dt.day).min(axis=0)
CE2_diurnal_min = CE2.groupby(CE2.Time.dt.day).min(axis=0)
RU2_diurnal_min = RU2.groupby(RU2.Time.dt.day).min(axis=0)
SA2_diurnal_min = SA2.groupby(SA2.Time.dt.day).min(axis=0)
SE2_diurnal_min = SE2.groupby(SE2.Time.dt.day).min(axis=0)
SX2_diurnal_min = SX2.groupby(SX2.Time.dt.day).min(axis=0)
SI2_diurnal_min = SI2.groupby(SI2.Time.dt.day).min(axis=0)
VW2_diurnal_min = VW2.groupby(VW2.Time.dt.day).min(axis=0)
WE2_diurnal_min = WE2.groupby(WE2.Time.dt.day).min(axis=0)

NO2_diurnal_max = NO2.groupby(NO2.Time.dt.day).max(axis=0)
CE2_diurnal_max = CE2.groupby(CE2.Time.dt.day).max(axis=0)
RU2_diurnal_max = RU2.groupby(RU2.Time.dt.day).max(axis=0)
SA2_diurnal_max = SA2.groupby(SA2.Time.dt.day).max(axis=0)
SE2_diurnal_max = SE2.groupby(SE2.Time.dt.day).max(axis=0)
SX2_diurnal_max = SX2.groupby(SX2.Time.dt.day).max(axis=0)
SI2_diurnal_max = SI2.groupby(SI2.Time.dt.day).max(axis=0)
VW2_diurnal_max = VW2.groupby(VW2.Time.dt.day).max(axis=0)
WE2_diurnal_max = WE2.groupby(WE2.Time.dt.day).max(axis=0)


NO_diurnal_std = NO.groupby(NO.Time.dt.hour).std()
CE_diurnal_std = CE.groupby(CE.Time.dt.hour).std()
RU_diurnal_std = RU.groupby(RU.Time.dt.hour).std()
SA_diurnal_std = SA.groupby(SA.Time.dt.hour).std()
SE_diurnal_std = SE.groupby(SE.Time.dt.hour).std()
SX_diurnal_std = SX.groupby(SX.Time.dt.hour).std()
SI_diurnal_std = SI.groupby(SI.Time.dt.hour).std()
VW_diurnal_std = VW.groupby(VW.Time.dt.hour).std()
WE_diurnal_std = WE.groupby(WE.Time.dt.hour).std()

NO1_diurnal_std = NO1.groupby(NO1.Time.dt.hour).std()
CE1_diurnal_std = CE1.groupby(CE1.Time.dt.hour).std()
RU1_diurnal_std = RU1.groupby(RU1.Time.dt.hour).std()
SA1_diurnal_std = SA1.groupby(SA1.Time.dt.hour).std()
SE1_diurnal_std = SE1.groupby(SE1.Time.dt.hour).std()
SX1_diurnal_std = SX1.groupby(SX1.Time.dt.hour).std()
SI1_diurnal_std = SI1.groupby(SI1.Time.dt.hour).std()
VW1_diurnal_std = VW1.groupby(VW1.Time.dt.hour).std()
WE1_diurnal_std = WE1.groupby(WE1.Time.dt.hour).std()

NO2_diurnal_std = NO2.groupby(NO2.Time.dt.hour).std()
CE2_diurnal_std = CE2.groupby(CE2.Time.dt.hour).std()
RU2_diurnal_std = RU2.groupby(RU2.Time.dt.hour).std()
SA2_diurnal_std = SA2.groupby(SA2.Time.dt.hour).std()
SE2_diurnal_std = SE2.groupby(SE2.Time.dt.hour).std()
SX2_diurnal_std = SX2.groupby(SX2.Time.dt.hour).std()
SI2_diurnal_std = SI2.groupby(SI2.Time.dt.hour).std()
VW2_diurnal_std = VW2.groupby(VW2.Time.dt.hour).std()
WE2_diurnal_std = WE2.groupby(WE2.Time.dt.hour).std()




NO_diurnal_mean = DataArray_to_dataframe(NO_diurnal_mean, NO1_diurnal_mean, NO2_diurnal_mean)
CE_diurnal_mean = DataArray_to_dataframe(CE_diurnal_mean, CE1_diurnal_mean, CE2_diurnal_mean)
RU_diurnal_mean = DataArray_to_dataframe(RU_diurnal_mean, RU1_diurnal_mean, RU2_diurnal_mean)
SA_diurnal_mean = DataArray_to_dataframe(SA_diurnal_mean, SA1_diurnal_mean, SA2_diurnal_mean)
SE_diurnal_mean = DataArray_to_dataframe(SE_diurnal_mean, SE1_diurnal_mean, SE2_diurnal_mean)
SX_diurnal_mean = DataArray_to_dataframe(SX_diurnal_mean, SX1_diurnal_mean, SX2_diurnal_mean)
SI_diurnal_mean = DataArray_to_dataframe(SI_diurnal_mean, SI1_diurnal_mean, SI2_diurnal_mean)
VW_diurnal_mean = DataArray_to_dataframe(VW_diurnal_mean, VW1_diurnal_mean, VW2_diurnal_mean)
WE_diurnal_mean = DataArray_to_dataframe(WE_diurnal_mean, WE1_diurnal_mean, WE2_diurnal_mean)

NO_diurnal_min = DataArray_drop_to_Frame(NO_diurnal_min, NO1_diurnal_min, NO2_diurnal_min) - 273.15
CE_diurnal_min = DataArray_drop_to_Frame(CE_diurnal_min, CE1_diurnal_min, CE2_diurnal_min) - 273.15
RU_diurnal_min = DataArray_drop_to_Frame(RU_diurnal_min, RU1_diurnal_min, RU2_diurnal_min) - 273.15
SA_diurnal_min = DataArray_drop_to_Frame(SA_diurnal_min, SA1_diurnal_min, SA2_diurnal_min) - 273.15
SE_diurnal_min = DataArray_drop_to_Frame(SE_diurnal_min, SE1_diurnal_min, SE2_diurnal_min) - 273.15
SX_diurnal_min = DataArray_drop_to_Frame(SX_diurnal_min, SX1_diurnal_min, SX2_diurnal_min) - 273.15
SI_diurnal_min = DataArray_drop_to_Frame(SI_diurnal_min, SI1_diurnal_min, SI2_diurnal_min) - 273.15
VW_diurnal_min = DataArray_drop_to_Frame(VW_diurnal_min, VW1_diurnal_min, VW2_diurnal_min) - 273.15
WE_diurnal_min = DataArray_drop_to_Frame(WE_diurnal_min, WE1_diurnal_min, WE2_diurnal_min) - 273.15

NO_diurnal_max = DataArray_drop_to_Frame(NO_diurnal_max, NO1_diurnal_max, NO2_diurnal_max) - 273.15
CE_diurnal_max = DataArray_drop_to_Frame(CE_diurnal_max, CE1_diurnal_max, CE2_diurnal_max) - 273.15
RU_diurnal_max = DataArray_drop_to_Frame(RU_diurnal_max, RU1_diurnal_max, RU2_diurnal_max) - 273.15
SA_diurnal_max = DataArray_drop_to_Frame(SA_diurnal_max, SA1_diurnal_max, SA2_diurnal_max) - 273.15
SE_diurnal_max = DataArray_drop_to_Frame(SE_diurnal_max, SE1_diurnal_max, SE2_diurnal_max) - 273.15
SX_diurnal_max = DataArray_drop_to_Frame(SX_diurnal_max, SX1_diurnal_max, SX2_diurnal_max) - 273.15
SI_diurnal_max = DataArray_drop_to_Frame(SI_diurnal_max, SI1_diurnal_max, SI2_diurnal_max) - 273.15
VW_diurnal_max = DataArray_drop_to_Frame(VW_diurnal_max, VW1_diurnal_max, VW2_diurnal_max) - 273.15
WE_diurnal_max = DataArray_drop_to_Frame(WE_diurnal_max, WE1_diurnal_max, WE2_diurnal_max) - 273.15

NO_diurnal_std = DataArray_to_dataframe(NO_diurnal_std, NO1_diurnal_std, NO2_diurnal_std)
CE_diurnal_std = DataArray_to_dataframe(CE_diurnal_std, CE1_diurnal_std, CE2_diurnal_std)
RU_diurnal_std = DataArray_to_dataframe(RU_diurnal_std, RU1_diurnal_std, RU2_diurnal_std)
SA_diurnal_std = DataArray_to_dataframe(SA_diurnal_std, SA1_diurnal_std, SA2_diurnal_std)
SE_diurnal_std = DataArray_to_dataframe(SE_diurnal_std, SE1_diurnal_std, SE2_diurnal_std)
SX_diurnal_std = DataArray_to_dataframe(SX_diurnal_std, SX1_diurnal_std, SX2_diurnal_std)
SI_diurnal_std = DataArray_to_dataframe(SI_diurnal_std, SI1_diurnal_std, SI2_diurnal_std)
VW_diurnal_std = DataArray_to_dataframe(VW_diurnal_std, VW1_diurnal_std, VW2_diurnal_std)
WE_diurnal_std = DataArray_to_dataframe(WE_diurnal_std, WE1_diurnal_std, WE2_diurnal_std)

#define title und descriptions for plotting
varnam = str(data.name)
vardesc = str(data.description)
var1nam = str(data1.name)
var1desc = str(data1.description)
var2nam = str(data2.name)
var2desc = str(data2.description)
title = ' --- Diurnal Comparison ---'

#data collecting for automated plotting routine
diurnal_mean = [NO_diurnal_mean, CE_diurnal_mean, RU_diurnal_mean, SA_diurnal_mean, SE_diurnal_mean, SX_diurnal_mean, SI_diurnal_mean, VW_diurnal_mean, WE_diurnal_mean]
diurnal_std = [NO_diurnal_std, CE_diurnal_std, RU_diurnal_std, SA_diurnal_std, SE_diurnal_std, SX_diurnal_std, SI_diurnal_std, VW_diurnal_std, WE_diurnal_std]
diurnal_min = [NO_diurnal_min, CE_diurnal_min, RU_diurnal_min, SA_diurnal_min, SE_diurnal_min, SX_diurnal_min, SI_diurnal_min, VW_diurnal_min, WE_diurnal_min]
diurnal_max = [NO_diurnal_max, CE_diurnal_max, RU_diurnal_max, SA_diurnal_max, SE_diurnal_max, SX_diurnal_max, SI_diurnal_max, VW_diurnal_max, WE_diurnal_max]


#sprawl_diurnal_mean = [NO1_diurnal_mean, CE1_diurnal_mean, RU1_diurnal_mean, SA1_diurnal_mean, SE1_diurnal_mean, SX1_diurnal_mean, SI1_diurnal_mean, VW1_diurnal_mean, WE1_diurnal_mean]
#sprawl_diurnal_std = [NO1_diurnal_std, CE1_diurnal_std, RU1_diurnal_std, SA1_diurnal_std, SE1_diurnal_std, SX1_diurnal_std, SI1_diurnal_std, VW1_diurnal_std, WE1_diurnal_std]
#
#dense_diurnal_mean = [NO2_diurnal_mean, CE2_diurnal_mean, RU2_diurnal_mean, SA2_diurnal_mean, SE2_diurnal_mean, SX2_diurnal_mean, SI2_diurnal_mean, VW2_diurnal_mean, WE2_diurnal_mean]
#dense_diurnal_std = [NO2_diurnal_std, CE2_diurnal_std, RU2_diurnal_std, SA2_diurnal_std, SE2_diurnal_std, SX2_diurnal_std, SI2_diurnal_std, VW2_diurnal_std, WE2_diurnal_std]

#ref_diurnal_mean = arr_rename(ref_diurnal_mean, ref_area, 'mean')
#ref_diurnal_std = arr_rename(ref_diurnal_std, ref_area, 'std')
#
#sprawl_diurnal_mean = arr_rename(sprawl_diurnal_mean, sprawl_area, 'mean')
#sprawl_diurnal_std = arr_rename(sprawl_diurnal_std, sprawl_area, 'std')
#
#dense_diurnal_mean = arr_rename(dense_diurnal_mean, dense_area, 'mean')
#dense_diurnal_std = arr_rename(dense_diurnal_std, dense_area, 'std')

#%%
""" PLOTTING ROUTUNE """

boxminrange = 5
boxmaxrange = 5
boxminstart = 24
boxmaxstart = 39


for idx, var in enumerate(diurnal_mean):
    
    fig, ax = plt.subplots(figsize=(16,9))
    gs = gridspec.GridSpec(2, 2,
                       width_ratios=[5, 1]
                       )


    ax1 = plt.subplot(gs[0])
    
    ax1.plot(times, diurnal_mean[idx].iloc[:,0], c='k', label=str(diurnal_mean[idx].iloc[:,0].name[3:])+ ' median')
    ax1.plot(times, diurnal_mean[idx].iloc[:,1], c='C3', label=str(diurnal_mean[idx].iloc[:,1].name[3:])+ ' median')
    ax1.plot(times, diurnal_mean[idx].iloc[:,2], c='C2', label=str(diurnal_mean[idx].iloc[:,2].name[3:])+ ' median')
    ax1.tick_params(axis='x', rotation=90)
    ax1.set_xlabel('Times')
    ax1.set_ylabel(str(data.name) + ' mittlerer Tagesgang ' + '['+str(data.units)+']')
    ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))   #to get a tick every 15 minutes

    #if data.name == 'GLW':
    #    ax1.set_ylim(330, 430)
    ax1.legend(fontsize='small', loc='upper left')
    ax1.grid(True)
    ax1ylim = ax1.get_ylim()
    
#    ax2 = ax1.twinx()
#    ax2.plot(times, diurnal_std[idx].iloc[:,0], c='k', ls=':', label=str(diurnal_std[idx].iloc[:,0].name[3:])+ ' std')
#    ax2.plot(times, diurnal_std[idx].iloc[:,1], c='C3', ls=':', label=str(diurnal_std[idx].iloc[:,1].name[3:])+ ' std')
#    ax2.plot(times, diurnal_std[idx].iloc[:,2], c='C2', ls=':', label=str(diurnal_std[idx].iloc[:,2].name[3:])+ ' std')
#    ax2.set_ylabel(str(data.name) + ' Std ' + '['+str(data.units)+']')
#    #ax2.set_ylim(0,20)
#    ax2.xaxis.set_major_locator(mdates.HourLocator(interval=2))   #to get a tick every 15 minutes
#    #ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))     #optional formatting 
#
#    ax2.legend(fontsize='small', loc='upper right')
    
    
    # Correlation zwischen den Laeufen
    cor_sprawl = np.array([diurnal_mean[idx].iloc[:,0].corr(diurnal_mean[idx].iloc[:,1]) for i in range(diurnal_mean[idx].iloc[:,0].size)])
    cor_dense = np.array([diurnal_mean[idx].iloc[:,0].corr(diurnal_mean[idx].iloc[:,2]) for i in range(diurnal_mean[idx].iloc[:,0].size)])

    # Differenzen zwischen den mittleren tagesgaengen
#    diff_sprawl = np.array(sprawl_diurnal_mean[idx]) - np.array(ref_diurnal_mean[idx])
#    diff_dense = np.array(dense_diurnal_mean[idx]) - np.array(ref_diurnal_mean[idx])
    diurnal_mean[idx][diurnal_mean[idx].iloc[:,0].name[:2]+' diff_sprawl-Ref'] =  diurnal_mean[idx].iloc[:,1] - diurnal_mean[idx].iloc[:,0]
    diurnal_mean[idx][diurnal_mean[idx].iloc[:,0].name[:2]+' diff_dense-Ref'] =  diurnal_mean[idx].iloc[:,2] - diurnal_mean[idx].iloc[:,0]
    
    
    ax3 = plt.subplot(gs[2])
    
    ax3.plot(times, diurnal_mean[idx].iloc[:,3], c='C3', label='Diff spr - Ref')
    ax3.plot(times, diurnal_mean[idx].iloc[:,4], c='C2', label='Diff opt - Ref')
    ax3.set_xlabel('Times')
    ax3.set_ylabel('Difference ' + '['+str(data.units)+']')
    ax3.legend(fontsize='small', loc='lower left')
    ax3.grid(True)
    ax3.xaxis.set_major_locator(mdates.HourLocator(interval=2))   #to get a tick every 15 minutes
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))     #optional formatting 
    
    ax5 = plt.subplot(gs[1])
    boxprops = dict( linewidth=1.5, color='b')
    flierprops = dict(marker='x', linestyle='none')
    medianprops = dict(linestyle='-', linewidth=2.5, color='firebrick')
    meanpointprops = dict(marker='D', markeredgecolor='black',
                      markerfacecolor='g')
    whiskerprops = dict( linestyle='--', color='k')

    ax5.boxplot([diurnal_max[idx].iloc[:,0], diurnal_max[idx].iloc[:,1],diurnal_max[idx].iloc[:,2]],
                notch=True, labels=['REF','SPR', 'OPT'], whis='range', boxprops=boxprops, showfliers=True, flierprops=flierprops, 
                medianprops=medianprops, showmeans=True, meanprops=meanpointprops, 
                whiskerprops=whiskerprops)
    ax5.tick_params(axis='y', labelleft='off', labelright='on')
    ax5.set_ylabel('Daily MAX')
#    ax5.set_ylim(boxmaxstart, boxmaxstart + boxmaxrange)
    ax5.grid(True)

    ax4 = plt.subplot(gs[3])
    
    ax4.boxplot([diurnal_min[idx].iloc[:,0], diurnal_min[idx].iloc[:,1],diurnal_min[idx].iloc[:,2]],
                notch=True, labels=['REF','SPR', 'OPT'], whis='range', boxprops=boxprops, showfliers=True, flierprops=flierprops, 
                medianprops=medianprops, showmeans=True, meanprops=meanpointprops, 
                whiskerprops=whiskerprops)
    ax4.tick_params(axis='y', labelleft='off', labelright='on')
#    ax4.set_ylim(boxminstart, boxminstart + boxminrange)

    ax4.set_ylabel('Daily MIN')
    ax4.grid(True)
    #ax4.set_ylim(ax1ylim)
    
    
    #ax5.set_ylim(ax1ylim)



#    ax4.plot(times, cor_sprawl, c='C2',  ls=':', label='Corr Ref - sprawl')
#    ax4.plot(times, cor_dense, c='C3', ls=':', label='Corr Ref - dense')
#    ax4.set_ylabel('Correlation')
#    ax4 = ax3.twinx()
#    ax3.plot(times, cor2, c='C4', ls=':', label='Ref-'+ list_sp_mean[idx].iloc[:,2].name[:2]+' Corr')
#    ax3.set_ylabel('Correlation')
#    ax3.set_ylim()
    
    plt.subplots_adjust(hspace=0.)
    
    ax1 = plt.gca()
    ax1.text(0,1.04,run , fontsize=14, transform=ax.transAxes)
    ax1.text(0,1.07,'reference Area: ' + diurnal_mean[idx].iloc[:,0].name[:2]+ '   ' + title, fontsize=16, transform=ax.transAxes)
    ax1.text(0.7,1.07,'CORR Spr: ' + np.array2string(cor_sprawl[-1:], precision=5), fontsize=12, transform=ax.transAxes)
    ax1.text(0.7,1.04,'CORR Opt: ' + np.array2string(cor_dense[-1:], precision=5), fontsize=12, transform=ax.transAxes)
    ax1.text(0,1.01,varnam + ' - ' + vardesc, fontsize=12, transform=ax.transAxes)
    ax1.text(0.7,1.01,'Init: ' + init, fontsize=14, transform=ax.transAxes)
    
    #fig.autofmt_xdate()
    #fig.legend(fontsize='small', loc='upper right')
    
    filename = domain + '_' + data.name + '_' + diurnal_mean[idx].iloc[:,0].name[:2] + '_TAGESGANG_BOX_MINMAX'  +".png"
    plt.savefig(plot_dir + filename)