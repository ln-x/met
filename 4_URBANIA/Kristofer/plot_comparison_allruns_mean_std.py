# -*- coding: utf-8 -*-
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import os
import wrf
from wrf import to_np, getvar, get_basemap, latlon_coords

"""
erstellt einen Zeitreihenplot aller AREAS und vergleicht die einzelnen runs der geplotteten variable
    + Zeitreihenplot SPACIAL MEAN + Stdabweichung
    + Differenz SPR/OPT - REF
    + CORRELATION SPR/OPT mit REF
"""



def DataArray_to_dataframe(array1, array2, array3):
    """
    Converts 3 DataArrays with metadata to an pandas DataFrame
    & drops XTIME so it can calculate the means
    
    Input: 3 DataArray
    Output: 1 Dataframe, Mean of Columns
    """
    
    frame = array1.to_dataframe()
    frame[str(array2.name)] = array2.to_series()
    frame[str(array3.name)] = array3.to_series()
    frame = frame.drop(columns=['XTIME'])
    mean = frame.mean(axis=1)
    return frame, mean

def arr_rename(array1, text1, text2):
    array1 = array1.rename(str(text1) + ' ' + str(text2))
    return array1

# EXAMPLE
# plot 30-year mean of precipitation dataset
# load data as xarray dataset
date = '2069-07-01'
domain = 'd03'
run = 'REF_Run_2069'
run1 = 'SPR_Run_2069'
run2 = 'OPT_Run_2069'
path = '/hp4/Urbania/WRF-2019-Runs/'
filepath = path + run + '/'
filepath1 = path + run1 + '/'
filepath2 = path + run2 + '/'
para = 'T2'
startdate = '01/07/2069 18:00:00'
enddate = '08/07/2069'


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
currtime = pd.to_datetime(times[0]) + spinup
startdate = pd.to_datetime(startdate) + spinup
# Spacial selection of reference AREAS
times = getvar(ncfile1, "Times", timeidx=wrf.ALL_TIMES)
NO = data.isel(south_north=slice(73,82), west_east=slice(89,98))
CE = data.isel(south_north=slice(50,59), west_east=slice(80,89))
RU = data.isel(south_north=slice(57,66), west_east=slice(128,137))
SA = data.isel(south_north=slice(58,67), west_east=slice(109,118))
SE = data.isel(south_north=slice(37,46), west_east=slice(99,108))
SX = data.isel(south_north=slice(24,33), west_east=slice(75,84))
SI = data.isel(south_north=slice(31,40), west_east=slice(68,77))
VW = data.isel(south_north=slice(47,56), west_east=slice(64,73))
WE = data.isel(south_north=slice(62,71), west_east=slice(73,82))

NO = NO.sel(Time=slice(startdate,enddate)).rename('NO_ref')
CE = CE.sel(Time=slice(startdate,enddate)).rename('CE_ref')
RU = RU.sel(Time=slice(startdate,enddate)).rename('RU_ref')
SA = SA.sel(Time=slice(startdate,enddate)).rename('SA_ref')
SE = SE.sel(Time=slice(startdate,enddate)).rename('SE_ref')
SX = SX.sel(Time=slice(startdate,enddate)).rename('SX_ref')
SI = SI.sel(Time=slice(startdate,enddate)).rename('SI_ref')
VW = VW.sel(Time=slice(startdate,enddate)).rename('VW_ref')
WE = WE.sel(Time=slice(startdate,enddate)).rename('WE_ref')

times = times.to_series()

NO1 = data1.isel(south_north=slice(73,82), west_east=slice(89,98))
CE1 = data1.isel(south_north=slice(50,59), west_east=slice(80,89))
RU1 = data1.isel(south_north=slice(57,66), west_east=slice(128,137))
SA1 = data1.isel(south_north=slice(58,67), west_east=slice(109,118))
SE1 = data1.isel(south_north=slice(37,46), west_east=slice(99,108))
SX1 = data1.isel(south_north=slice(24,33), west_east=slice(75,84))
SI1 = data1.isel(south_north=slice(31,40), west_east=slice(68,77))
VW1 = data1.isel(south_north=slice(47,56), west_east=slice(64,73))
WE1 = data1.isel(south_north=slice(62,71), west_east=slice(73,82))

NO1 = NO1.sel(Time=slice(startdate,enddate)).rename('NO_spr')
CE1 = CE1.sel(Time=slice(startdate,enddate)).rename('CE_spr')
RU1 = RU1.sel(Time=slice(startdate,enddate)).rename('RU_spr')
SA1 = SA1.sel(Time=slice(startdate,enddate)).rename('SA_spr')
SE1 = SE1.sel(Time=slice(startdate,enddate)).rename('SE_spr')
SX1 = SX1.sel(Time=slice(startdate,enddate)).rename('SX_spr')
SI1 = SI1.sel(Time=slice(startdate,enddate)).rename('SI_spr')
VW1 = VW1.sel(Time=slice(startdate,enddate)).rename('VW_spr')
WE1 = WE1.sel(Time=slice(startdate,enddate)).rename('WE_spr')

NO2 = data2.isel(south_north=slice(73,82), west_east=slice(89,98))
CE2 = data2.isel(south_north=slice(50,59), west_east=slice(80,89))
RU2 = data2.isel(south_north=slice(57,66), west_east=slice(128,137))
SA2 = data2.isel(south_north=slice(58,67), west_east=slice(109,118))
SE2 = data2.isel(south_north=slice(37,46), west_east=slice(99,108))
SX2 = data2.isel(south_north=slice(24,33), west_east=slice(75,84))
SI2 = data2.isel(south_north=slice(31,40), west_east=slice(68,77))
VW2 = data2.isel(south_north=slice(47,56), west_east=slice(64,73))
WE2 = data2.isel(south_north=slice(62,71), west_east=slice(73,82))

NO2 = NO2.sel(Time=slice(startdate,enddate)).rename('NO_opt')
CE2 = CE2.sel(Time=slice(startdate,enddate)).rename('CE_opt')
RU2 = RU2.sel(Time=slice(startdate,enddate)).rename('RU_opt')
SA2 = SA2.sel(Time=slice(startdate,enddate)).rename('SA_opt')
SE2 = SE2.sel(Time=slice(startdate,enddate)).rename('SE_opt')
SX2 = SX2.sel(Time=slice(startdate,enddate)).rename('SX_opt')
SI2 = SI2.sel(Time=slice(startdate,enddate)).rename('SI_opt')
VW2 = VW2.sel(Time=slice(startdate,enddate)).rename('VW_opt')
WE2 = WE2.sel(Time=slice(startdate,enddate)).rename('WE_opt')

NO_mean = NO.median(dim={'south_north','west_east'})
CE_mean = CE.median(dim={'south_north','west_east'})
RU_mean = RU.median(dim={'south_north','west_east'})
SA_mean = SA.median(dim={'south_north','west_east'})
SE_mean = SE.median(dim={'south_north','west_east'})
SX_mean = SX.median(dim={'south_north','west_east'})
SI_mean = SI.median(dim={'south_north','west_east'})
VW_mean = VW.median(dim={'south_north','west_east'})
WE_mean = WE.median(dim={'south_north','west_east'})

NO_mean = NO_mean.rename('NO_mean_ref')
CE_mean = CE_mean.rename('CE_mean_ref')
RU_mean = RU_mean.rename('RU_mean_ref')
SA_mean = SA_mean.rename('SA_mean_ref')
SE_mean = SE_mean.rename('SE_mean_ref')
SX_mean = SX_mean.rename('SX_mean_ref')
SI_mean = SI_mean.rename('SI_mean_ref')
VW_mean = VW_mean.rename('VW_mean_ref')
WE_mean = WE_mean.rename('WE_mean_ref')

NO1_mean = NO1.median(dim={'south_north','west_east'})
CE1_mean = CE1.median(dim={'south_north','west_east'})
RU1_mean = RU1.median(dim={'south_north','west_east'})
SA1_mean = SA1.median(dim={'south_north','west_east'})
SE1_mean = SE1.median(dim={'south_north','west_east'})
SX1_mean = SX1.median(dim={'south_north','west_east'})
SI1_mean = SI1.median(dim={'south_north','west_east'})
VW1_mean = VW1.median(dim={'south_north','west_east'})
WE1_mean = WE1.median(dim={'south_north','west_east'})

NO1_mean = NO1_mean.rename('NO_mean_spr')
CE1_mean = CE1_mean.rename('CE_mean_spr')
RU1_mean = RU1_mean.rename('RU_mean_spr')
SA1_mean = SA1_mean.rename('SA_mean_spr')
SE1_mean = SE1_mean.rename('SE_mean_spr')
SX1_mean = SX1_mean.rename('SX_mean_spr')
SI1_mean = SI1_mean.rename('SI_mean_spr')
VW1_mean = VW1_mean.rename('VW_mean_spr')
WE1_mean = WE1_mean.rename('WE_mean_spr')

NO2_mean = NO2.median(dim={'south_north','west_east'})
CE2_mean = CE2.median(dim={'south_north','west_east'})
RU2_mean = RU2.median(dim={'south_north','west_east'})
SA2_mean = SA2.median(dim={'south_north','west_east'})
SE2_mean = SE2.median(dim={'south_north','west_east'})
SX2_mean = SX2.median(dim={'south_north','west_east'})
SI2_mean = SI2.median(dim={'south_north','west_east'})
VW2_mean = VW2.median(dim={'south_north','west_east'})
WE2_mean = WE2.median(dim={'south_north','west_east'})

NO2_mean = NO2_mean.rename('NO_mean_opt')
CE2_mean = CE2_mean.rename('CE_mean_opt')
RU2_mean = RU2_mean.rename('RU_mean_opt')
SA2_mean = SA2_mean.rename('SA_mean_opt')
SE2_mean = SE2_mean.rename('SE_mean_opt')
SX2_mean = SX2_mean.rename('SX_mean_opt')
SI2_mean = SI2_mean.rename('SI_mean_opt')
VW2_mean = VW2_mean.rename('VW_mean_opt')
WE2_mean = WE2_mean.rename('WE_mean_opt')

NO_std = NO.std(dim={'south_north','west_east'})
CE_std = CE.std(dim={'south_north','west_east'})
RU_std = RU.std(dim={'south_north','west_east'})
SA_std = SA.std(dim={'south_north','west_east'})
SE_std = SE.std(dim={'south_north','west_east'})
SX_std = SX.std(dim={'south_north','west_east'})
SI_std = SI.std(dim={'south_north','west_east'})
VW_std = VW.std(dim={'south_north','west_east'})
WE_std = WE.std(dim={'south_north','west_east'})

NO1_std = NO1.std(dim={'south_north','west_east'})
CE1_std = CE1.std(dim={'south_north','west_east'})
RU1_std = RU1.std(dim={'south_north','west_east'})
SA1_std = SA1.std(dim={'south_north','west_east'})
SE1_std = SE1.std(dim={'south_north','west_east'})
SX1_std = SX1.std(dim={'south_north','west_east'})
SI1_std = SI1.std(dim={'south_north','west_east'})
VW1_std = VW1.std(dim={'south_north','west_east'})
WE1_std = WE1.std(dim={'south_north','west_east'})

NO2_std = NO2.std(dim={'south_north','west_east'})
CE2_std = CE2.std(dim={'south_north','west_east'})
RU2_std = RU2.std(dim={'south_north','west_east'})
SA2_std = SA2.std(dim={'south_north','west_east'})
SE2_std = SE2.std(dim={'south_north','west_east'})
SX2_std = SX2.std(dim={'south_north','west_east'})
SI2_std = SI2.std(dim={'south_north','west_east'})
VW2_std = VW2.std(dim={'south_north','west_east'})
WE2_std = WE2.std(dim={'south_north','west_east'})

NO_std = NO_std.rename('NO_std_ref')
CE_std = CE_std.rename('CE_std_ref')
RU_std = RU_std.rename('RU_std_ref')
SA_std = SA_std.rename('SA_std_ref')
SE_std = SE_std.rename('SE_std_ref')
SX_std = SX_std.rename('SX_std_ref')
SI_std = SI_std.rename('SI_std_ref')
VW_std = VW_std.rename('VW_std_ref')
WE_std = WE_std.rename('WE_std_ref')

NO1_std = NO1_std.rename('NO_std_spr')
CE1_std = CE1_std.rename('CE_std_spr')
RU1_std = RU1_std.rename('RU_std_spr')
SA1_std = SA1_std.rename('SA_std_spr')
SE1_std = SE1_std.rename('SE_std_spr')
SX1_std = SX1_std.rename('SX_std_spr')
SI1_std = SI1_std.rename('SI_std_spr')
VW1_std = VW1_std.rename('VW_std_spr')
WE1_std = WE1_std.rename('WE_std_spr')

NO2_std = NO2_std.rename('NO_std_opt')
CE2_std = CE2_std.rename('CE_std_opt')
RU2_std = RU2_std.rename('RU_std_opt')
SA2_std = SA2_std.rename('SA_std_opt')
SE2_std = SE2_std.rename('SE_std_opt')
SX2_std = SX2_std.rename('SX_std_opt')
SI2_std = SI2_std.rename('SI_std_opt')
VW2_std = VW2_std.rename('VW_std_opt')
WE2_std = WE2_std.rename('WE_std_opt')

NO_sp_mean, NO_t_mean = DataArray_to_dataframe(NO_mean, NO1_mean, NO2_mean)
CE_sp_mean, CE_t_mean = DataArray_to_dataframe(CE_mean, CE1_mean, CE2_mean)
RU_sp_mean, RU_t_mean = DataArray_to_dataframe(RU_mean, RU1_mean, RU2_mean)
SA_sp_mean, SA_t_mean = DataArray_to_dataframe(SA_mean, SA1_mean, SA2_mean)
SE_sp_mean, SE_t_mean = DataArray_to_dataframe(SE_mean, SE1_mean, SE2_mean)
SX_sp_mean, SX_t_mean = DataArray_to_dataframe(SX_mean, SX1_mean, SX2_mean)
SI_sp_mean, SI_t_mean = DataArray_to_dataframe(SI_mean, SI1_mean, SI2_mean)
VW_sp_mean, VW_t_mean = DataArray_to_dataframe(VW_mean, VW1_mean, VW2_mean)
WE_sp_mean, WE_t_mean = DataArray_to_dataframe(WE_mean, WE1_mean, WE2_mean)

NO_sp_std, NO_t_std = DataArray_to_dataframe(NO_std, NO1_std, NO2_std)
CE_sp_std, CE_t_std = DataArray_to_dataframe(CE_std, CE1_std, CE2_std)
RU_sp_std, RU_t_std = DataArray_to_dataframe(RU_std, RU1_std, RU2_std)
SA_sp_std, SA_t_std = DataArray_to_dataframe(SA_std, SA1_std, SA2_std)
SE_sp_std, SE_t_std = DataArray_to_dataframe(SE_std, SE1_std, SE2_std)
SX_sp_std, SX_t_std = DataArray_to_dataframe(SX_std, SX1_std, SX2_std)
SI_sp_std, SI_t_std = DataArray_to_dataframe(SI_std, SI1_std, SI2_std)
VW_sp_std, VW_t_std = DataArray_to_dataframe(VW_std, VW1_std, VW2_std)
WE_sp_std, WE_t_std = DataArray_to_dataframe(WE_std, WE1_std, WE2_std)

varnam = str(data.name)
vardesc = str(data.description)
var1nam = str(data1.name)
var1desc = str(data1.description)
var2nam = str(data2.name)
var2desc = str(data2.description)
title = ' --- Spacial and Temporal Medians and Stds ---'

list_sp_mean = [NO_sp_mean, CE_sp_mean, RU_sp_mean, SA_sp_mean, SE_sp_mean, SX_sp_mean, SI_sp_mean, VW_sp_mean, WE_sp_mean]
list_t_mean = [NO_t_mean, CE_t_mean, RU_t_mean, SA_t_mean, SE_t_mean, SX_t_mean, SI_t_mean, VW_t_mean, WE_t_mean]
list_sp_std = [NO_sp_std, CE_sp_std, RU_sp_std, SA_sp_std, SE_sp_std, SX_sp_std, SI_sp_std, VW_sp_std, WE_sp_std]
list_t_std = [NO_t_std, CE_t_std, RU_t_std, SA_t_std, SE_t_std, SX_t_std, SI_t_std, VW_t_std, WE_t_std]
    
#%%
for idx, var in enumerate(list_sp_mean):
    
    fig, ax = plt.subplots(figsize=(16,9), sharex=True)
    
    ax1 = plt.subplot(211)
    ax1.plot(times, list_sp_mean[idx].iloc[:,0], c='k', label=str(list_sp_mean[idx].iloc[:,0].name[3:]))
    ax1.plot(times, list_sp_mean[idx].iloc[:,1], c='C3', label=str(list_sp_mean[idx].iloc[:,1].name[3:]))
    ax1.plot(times, list_sp_mean[idx].iloc[:,2], c='C2', label=str(list_sp_mean[idx].iloc[:,2].name[3:]))
    ax1.tick_params(axis='x', rotation=90)
    ax1.set_xlabel('Times')
    ax1.set_ylabel(str(data.name) + ' spacial Median ' +'['+ str(data.units)+']')
    if data.name == 'GLW':
        ax1.set_ylim(330, 430)
    ax1.grid(True)

    
    ax2 = ax1.twinx()
    ax2.plot(times, list_sp_std[idx].iloc[:,0], c='k', ls=':', label=str(list_sp_std[idx].iloc[:,0].name[3:]))
    ax2.plot(times, list_sp_std[idx].iloc[:,1], c='C3', ls=':', label=str(list_sp_std[idx].iloc[:,1].name[3:]))
    ax2.plot(times, list_sp_std[idx].iloc[:,2], c='C2', ls=':', label=str(list_sp_std[idx].iloc[:,2].name[3:]))
    ax2.set_ylabel(str(data.name) + ' Std ' + '['+ str(data.units)+']')
    #ax2.set_ylim(0,20)
    #ax2.grid(True)
    ax2.xaxis.set_major_locator(mdates.HourLocator(interval=6))   #to get a tick every 15 minutes
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))     #optional formatting 

    
    cor_sprawl = np.array([ list_sp_mean[idx].iloc[:i,0].corr(list_sp_mean[idx].iloc[:i,1]) for i in range(list_sp_mean[idx].iloc[:,0].size)])
    cor_dense = np.array([ list_sp_mean[idx].iloc[:i,0].corr(list_sp_mean[idx].iloc[:i,2]) for i in range(list_sp_mean[idx].iloc[:,0].size)])
    
    
    
    list_sp_mean[idx][list_sp_mean[idx].iloc[:,0].name[:2]+'corr_Ref_sprawl'] = cor_sprawl
    list_sp_mean[idx][list_sp_mean[idx].iloc[:,0].name[:2]+'corr_Ref_dense'] = cor_dense
    
    list_sp_mean[idx][list_sp_mean[idx].iloc[:,0].name[:2]+'diff_sprawl-Ref'] =  list_sp_mean[idx].iloc[:,1] - list_sp_mean[idx].iloc[:,0]
    list_sp_mean[idx][list_sp_mean[idx].iloc[:,0].name[:2]+'diff_dense-Ref'] =  list_sp_mean[idx].iloc[:,2] - list_sp_mean[idx].iloc[:,0]
    
    ax3 = plt.subplot(212)
    
    ax3.plot(times, list_sp_mean[idx][list_sp_mean[idx].iloc[:,0].name[:2]+'diff_sprawl-Ref'], c='C3', label='Diff spr - Ref')
    ax3.plot(times, list_sp_mean[idx][list_sp_mean[idx].iloc[:,0].name[:2]+'diff_dense-Ref'], c='C2', label='Diff opt - Ref')
    ax3.set_xlabel('Times')
    ax3.set_ylabel('Difference ' + '['+ str(data.units)+']')
    ax3.grid(True)
    
    ax4 = ax3.twinx()
    ax4.plot(times, list_sp_mean[idx][list_sp_mean[idx].iloc[:,0].name[:2]+'corr_Ref_sprawl'], c='C3',  ls=':', label='Corr Ref - spr')
    ax4.plot(times, list_sp_mean[idx][list_sp_mean[idx].iloc[:,0].name[:2]+'corr_Ref_dense'], c='C2', ls=':', label='Corr Ref- opt')
    ax4.set_ylabel('Correlation')
    ax4.xaxis.set_major_locator(mdates.HourLocator(interval=6))   #to get a tick every 15 minutes
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))     #optional formatting 
    #ax4 = ax3.twinx()
    #ax3.plot(times, cor2, c='C4', ls=':', label='Ref-'+ list_sp_mean[idx].iloc[:,2].name[:2]+' Corr')
    #ax3.set_ylabel('Correlation')
    #ax3.set_ylim()
    
    plt.subplots_adjust(hspace=0.)
    
    ax1 = plt.gca()
    ax1.text(0,1.04,run , fontsize=14, transform=ax.transAxes)
    ax1.text(0,1.07,'reference Area: ' + list_sp_mean[idx].iloc[:,1].name[:2]+ '   ' + title, fontsize=16, transform=ax.transAxes)
    ax1.text(0.7,1.07,'CORR Spr: ' + np.array2string(cor_sprawl[-1:], precision=5), fontsize=12, transform=ax.transAxes)
    ax1.text(0.7,1.04,'CORR Opt: ' + np.array2string(cor_dense[-1:], precision=5), fontsize=12, transform=ax.transAxes)
    ax1.text(0,1.01,varnam + ' - ' + vardesc, fontsize=12, transform=ax.transAxes)
    ax1.text(0.7,1.01,'Init: ' + init, fontsize=14, transform=ax.transAxes)
    
    fig.legend(fontsize='small', loc='upper right')
    fig.autofmt_xdate()
    
    filename = domain + '_' + data.name + '_' + list_sp_mean[idx].iloc[:,0].name[:2] + '_RunCOMPARISON-MEDIAN-STD_'  +".png"
    plt.savefig(plot_dir + filename)