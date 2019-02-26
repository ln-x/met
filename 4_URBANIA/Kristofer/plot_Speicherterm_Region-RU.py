# -*- coding: utf-8 -*-
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import os
import wrf
from wrf import to_np, getvar, get_basemap, latlon_coords
import statsmodels.api as sm
from functions import collect_data_speicherterm


"""
Creates Speicherterm plots
Dabei werden von allen Regionen die Region RU abgezogen und ein Trend ermittelt
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
    mean = frame.mean(axis=1) # DO NOT USE !!!! mean over 3 runs
    return frame, mean

def arr_rename(array1, text1, text2):
    array1 = array1.rename(str(text1) + ' ' + str(text2))
    return array1

def lm(data):
    """ Linear Modell
    Args:
    data (pd.Series) : Zeitreihe
    Returns:
    model : lin. Modell
    """
    Y = data.values
    X = sm.add_constant(data.index)#.to_julian_date()) # Konstante hinzufügen
    model = sm.OLS(Y,X, missing='drop').fit()
    return model

date_2015 = '2015-08-05'
date_2069 = '2069-07-01'

domain = 'd03'
#run = 'REF_Run_2015' # reference run
#run1 = 'SPR_Run_2015' # sprawl run 
#run2 = 'OPT_Run_2015' # optimized city run
path = '/hp4/Urbania/WRF-2019-Runs/' # runPATH
#filepath = path + run + '/'
#filepath1 = path + run1 + '/'
#filepath2 = path + run2 + '/'
para = 'T2'




""" not usable days - uncomment used run """
cuttime_2069 = pd.to_datetime(['2069-7-1','2069-7-2','2069-7-3','2069-7-4','2069-7-5', '2069-7-6','2069-7-9']) # day with not usable data
cuttime_2015 = pd.to_datetime(['2015-08-05', '2015-08-06', '2015-08-07', '2015-08-08', '2015-08-14']) # 2015 run

plotdir_2015 ='/hp4/Urbania/plots/' + date_2015 + '/'
plotdir_2069 ='/hp4/Urbania/plots/' + date_2069 + '/'
plotdir_sens ='/hp4/Urbania/plots/'


if not os.path.exists(plotdir_2015):
    os.makedirs(plotdir_2015)
if not os.path.exists(plotdir_2069):
    os.makedirs(plotdir_2069)
if not os.path.exists(plotdir_sens):
    os.makedirs(plotdir_sens)



region = ['NO', 'CE', 'RU', 'SA', 'SE', 'SX', 'SI', 'VW', 'WE', 'WW']


region_sn = {'NO': (73,82), 
          'CE': (50,59),
          'RU': (57,66),
          'SA': (58,67),
          'SE': (37,46),
          'SX': (24,33),
          'SI': (31,40),
          'VW': (47,56),
          'WE': (62,71),
          'WW': (72,81)
          }

region_we = {'NO': (89,98),
          'CE': (80,89),
          'RU': (128,137),
          'SA': (109,118),
          'SE': (99,108),
          'SX': (75,84),
          'SI': (68,77),
          'VW': (64,73),
          'WE': (73,82),
          'WW': (37,46)
          }


#date = '2015-08-05'
#domain = 'd03'
#run = 'Ref_Run_2015' # reference run
#run1 = 'SPR_Run_2015' # sprawl run 
#run2 = 'OPT_Run_2015' # optimized city run
#path = '/hp4/Urbania/WRF-2019-Runs/' # runPATH
#filepath = path + run + '/'
#filepath1 = path + run1 + '/'
#filepath2 = path + run2 + '/'
#para = 'T2'
#startdate = '08/08/2015 18:00:00'
#enddate = '14/08/2015'
#cuttime = pd.to_datetime('2015-08-11') # day with not usable data
#
#filenam = 'wrfout_' + domain + '_' + date + '_18_00_00.nc'
#plot_dir ='/hp4/Urbania/plots/' + date + '/'
#if not os.path.exists(plot_dir):
#    os.makedirs(plot_dir)
#
#
#ncfile = Dataset(filepath + filenam)
#ncfile1 = Dataset(filepath1 + filenam)
#ncfile2 = Dataset(filepath2 + filenam)
##ncfile2 = Dataset(filepath2 + filenam)
##Dimension of domain
#data = getvar(ncfile, para, timeidx=wrf.ALL_TIMES)
#data_max = (data.max()/10).round()*10
#data_min = (data.min()/10).round()*10
#data1 = getvar(ncfile1, para, timeidx=wrf.ALL_TIMES)
#data2 = getvar(ncfile2, para, timeidx=wrf.ALL_TIMES)
#
times = getvar(ncfile1, "Times", timeidx=wrf.ALL_TIMES, meta=False) # FC times in np.datetime64 format - very ugly
#init = pd.to_datetime(times[0]) # converts the numpy datetime to datetime datetime format
#init = str(init) # initial time of wrf dataset
#spinup = pd.Timedelta('3 days') # spinup time for wrf and espacially TEB Canopy Temperatures
times = times[72:]
# Spacial selection of reference AREAS
#
#NO = data.isel(south_north=slice(73,82), west_east=slice(89,98))
#CE = data.isel(south_north=slice(50,59), west_east=slice(80,89))
#RU = data.isel(south_north=slice(57,66), west_east=slice(128,137))
#SA = data.isel(south_north=slice(58,67), west_east=slice(109,118))
#SE = data.isel(south_north=slice(37,46), west_east=slice(99,108))
#SX = data.isel(south_north=slice(24,33), west_east=slice(75,84))
#SI = data.isel(south_north=slice(31,40), west_east=slice(68,77))
#VW = data.isel(south_north=slice(47,56), west_east=slice(64,73))
#WE = data.isel(south_north=slice(62,71), west_east=slice(73,82))
#WW = data.isel(south_north=slice(72,81), west_east=slice(37,46)) # Wienerwald Vergleichsgebiet
#
#
#NO = NO.sel(Time=slice(startdate,enddate)).rename('NO_ref')
#CE = CE.sel(Time=slice(startdate,enddate)).rename('CE_ref')
#RU = RU.sel(Time=slice(startdate,enddate)).rename('RU_ref')
#SA = SA.sel(Time=slice(startdate,enddate)).rename('SA_ref')
#SE = SE.sel(Time=slice(startdate,enddate)).rename('SE_ref')
#SX = SX.sel(Time=slice(startdate,enddate)).rename('SX_ref')
#SI = SI.sel(Time=slice(startdate,enddate)).rename('SI_ref')
#VW = VW.sel(Time=slice(startdate,enddate)).rename('VW_ref')
#WE = WE.sel(Time=slice(startdate,enddate)).rename('WE_ref')
#WW = WW.sel(Time=slice(startdate,enddate)).rename('WW_ref')
#
#
#NO1 = data1.isel(south_north=slice(73,82), west_east=slice(89,98))
#CE1 = data1.isel(south_north=slice(50,59), west_east=slice(80,89))
#RU1 = data1.isel(south_north=slice(57,66), west_east=slice(128,137))
#SA1 = data1.isel(south_north=slice(58,67), west_east=slice(109,118))
#SE1 = data1.isel(south_north=slice(37,46), west_east=slice(99,108))
#SX1 = data1.isel(south_north=slice(24,33), west_east=slice(75,84))
#SI1 = data1.isel(south_north=slice(31,40), west_east=slice(68,77))
#VW1 = data1.isel(south_north=slice(47,56), west_east=slice(64,73))
#WE1 = data1.isel(south_north=slice(62,71), west_east=slice(73,82))
#WW1 = data1.isel(south_north=slice(72,81), west_east=slice(46,55)) # Wienerwald Vergleichsgebiet
#
#
#NO1 = NO1.sel(Time=slice(startdate,enddate)).rename('NO_spr')
#CE1 = CE1.sel(Time=slice(startdate,enddate)).rename('CE_spr')
#RU1 = RU1.sel(Time=slice(startdate,enddate)).rename('RU_spr')
#SA1 = SA1.sel(Time=slice(startdate,enddate)).rename('SA_spr')
#SE1 = SE1.sel(Time=slice(startdate,enddate)).rename('SE_spr')
#SX1 = SX1.sel(Time=slice(startdate,enddate)).rename('SX_spr')
#SI1 = SI1.sel(Time=slice(startdate,enddate)).rename('SI_spr')
#VW1 = VW1.sel(Time=slice(startdate,enddate)).rename('VW_spr')
#WE1 = WE1.sel(Time=slice(startdate,enddate)).rename('WE_spr')
#WW1 = WW1.sel(Time=slice(startdate,enddate)).rename('WW_spr')
#
#
#NO2 = data2.isel(south_north=slice(73,82), west_east=slice(89,98))
#CE2 = data2.isel(south_north=slice(50,59), west_east=slice(80,89))
#RU2 = data2.isel(south_north=slice(57,66), west_east=slice(128,137))
#SA2 = data2.isel(south_north=slice(58,67), west_east=slice(109,118))
#SE2 = data2.isel(south_north=slice(37,46), west_east=slice(99,108))
#SX2 = data2.isel(south_north=slice(24,33), west_east=slice(75,84))
#SI2 = data2.isel(south_north=slice(31,40), west_east=slice(68,77))
#VW2 = data2.isel(south_north=slice(47,56), west_east=slice(64,73))
#WE2 = data2.isel(south_north=slice(62,71), west_east=slice(73,82))
#WW2 = data2.isel(south_north=slice(72,81), west_east=slice(46,55)) # Wienerwald Vergleichsgebiet
#
#
#NO2 = NO2.sel(Time=slice(startdate,enddate)).rename('NO_opt')
#CE2 = CE2.sel(Time=slice(startdate,enddate)).rename('CE_opt')
#RU2 = RU2.sel(Time=slice(startdate,enddate)).rename('RU_opt')
#SA2 = SA2.sel(Time=slice(startdate,enddate)).rename('SA_opt')
#SE2 = SE2.sel(Time=slice(startdate,enddate)).rename('SE_opt')
#SX2 = SX2.sel(Time=slice(startdate,enddate)).rename('SX_opt')
#SI2 = SI2.sel(Time=slice(startdate,enddate)).rename('SI_opt')
#VW2 = VW2.sel(Time=slice(startdate,enddate)).rename('VW_opt')
#WE2 = WE2.sel(Time=slice(startdate,enddate)).rename('WE_opt')
#WW2 = WW2.sel(Time=slice(startdate,enddate)).rename('WW_opt')
#
#
#NO_mean = NO.median(dim={'south_north','west_east'})
#CE_mean = CE.median(dim={'south_north','west_east'})
#RU_mean = RU.median(dim={'south_north','west_east'})
#SA_mean = SA.median(dim={'south_north','west_east'})
#SE_mean = SE.median(dim={'south_north','west_east'})
#SX_mean = SX.median(dim={'south_north','west_east'})
#SI_mean = SI.median(dim={'south_north','west_east'})
#VW_mean = VW.median(dim={'south_north','west_east'})
#WE_mean = WE.median(dim={'south_north','west_east'})
#WW_mean = WW.median(dim={'south_north','west_east'})
#
#
#NO_mean = NO_mean.rename('NO_mean_ref')
#CE_mean = CE_mean.rename('CE_mean_ref')
#RU_mean = RU_mean.rename('RU_mean_ref')
#SA_mean = SA_mean.rename('SA_mean_ref')
#SE_mean = SE_mean.rename('SE_mean_ref')
#SX_mean = SX_mean.rename('SX_mean_ref')
#SI_mean = SI_mean.rename('SI_mean_ref')
#VW_mean = VW_mean.rename('VW_mean_ref')
#WE_mean = WE_mean.rename('WE_mean_ref')
#WW_mean = WW_mean.rename('WW_mean_ref')
#
#
#NO1_mean = NO1.median(dim={'south_north','west_east'})
#CE1_mean = CE1.median(dim={'south_north','west_east'})
#RU1_mean = RU1.median(dim={'south_north','west_east'})
#SA1_mean = SA1.median(dim={'south_north','west_east'})
#SE1_mean = SE1.median(dim={'south_north','west_east'})
#SX1_mean = SX1.median(dim={'south_north','west_east'})
#SI1_mean = SI1.median(dim={'south_north','west_east'})
#VW1_mean = VW1.median(dim={'south_north','west_east'})
#WE1_mean = WE1.median(dim={'south_north','west_east'})
#WW1_mean = WW1.median(dim={'south_north','west_east'})
#
#
#NO1_mean = NO1_mean.rename('NO_mean_spr')
#CE1_mean = CE1_mean.rename('CE_mean_spr')
#RU1_mean = RU1_mean.rename('RU_mean_spr')
#SA1_mean = SA1_mean.rename('SA_mean_spr')
#SE1_mean = SE1_mean.rename('SE_mean_spr')
#SX1_mean = SX1_mean.rename('SX_mean_spr')
#SI1_mean = SI1_mean.rename('SI_mean_spr')
#VW1_mean = VW1_mean.rename('VW_mean_spr')
#WE1_mean = WE1_mean.rename('WE_mean_spr')
#WW1_mean = WW1_mean.rename('WW_mean_spr')
#
#
#NO2_mean = NO2.median(dim={'south_north','west_east'})
#CE2_mean = CE2.median(dim={'south_north','west_east'})
#RU2_mean = RU2.median(dim={'south_north','west_east'})
#SA2_mean = SA2.median(dim={'south_north','west_east'})
#SE2_mean = SE2.median(dim={'south_north','west_east'})
#SX2_mean = SX2.median(dim={'south_north','west_east'})
#SI2_mean = SI2.median(dim={'south_north','west_east'})
#VW2_mean = VW2.median(dim={'south_north','west_east'})
#WE2_mean = WE2.median(dim={'south_north','west_east'})
#WW2_mean = WW2.median(dim={'south_north','west_east'})
#
#
#NO2_mean = NO2_mean.rename('NO_mean_opt')
#CE2_mean = CE2_mean.rename('CE_mean_opt')
#RU2_mean = RU2_mean.rename('RU_mean_opt')
#SA2_mean = SA2_mean.rename('SA_mean_opt')
#SE2_mean = SE2_mean.rename('SE_mean_opt')
#SX2_mean = SX2_mean.rename('SX_mean_opt')
#SI2_mean = SI2_mean.rename('SI_mean_opt')
#VW2_mean = VW2_mean.rename('VW_mean_opt')
#WE2_mean = WE2_mean.rename('WE_mean_opt')
#WW2_mean = WW2_mean.rename('WW_mean_opt')
#
#
#NO_std = NO.std(dim={'south_north','west_east'})
#CE_std = CE.std(dim={'south_north','west_east'})
#RU_std = RU.std(dim={'south_north','west_east'})
#SA_std = SA.std(dim={'south_north','west_east'})
#SE_std = SE.std(dim={'south_north','west_east'})
#SX_std = SX.std(dim={'south_north','west_east'})
#SI_std = SI.std(dim={'south_north','west_east'})
#VW_std = VW.std(dim={'south_north','west_east'})
#WE_std = WE.std(dim={'south_north','west_east'})
#
#NO1_std = NO1.std(dim={'south_north','west_east'})
#CE1_std = CE1.std(dim={'south_north','west_east'})
#RU1_std = RU1.std(dim={'south_north','west_east'})
#SA1_std = SA1.std(dim={'south_north','west_east'})
#SE1_std = SE1.std(dim={'south_north','west_east'})
#SX1_std = SX1.std(dim={'south_north','west_east'})
#SI1_std = SI1.std(dim={'south_north','west_east'})
#VW1_std = VW1.std(dim={'south_north','west_east'})
#WE1_std = WE1.std(dim={'south_north','west_east'})
#
#NO2_std = NO2.std(dim={'south_north','west_east'})
#CE2_std = CE2.std(dim={'south_north','west_east'})
#RU2_std = RU2.std(dim={'south_north','west_east'})
#SA2_std = SA2.std(dim={'south_north','west_east'})
#SE2_std = SE2.std(dim={'south_north','west_east'})
#SX2_std = SX2.std(dim={'south_north','west_east'})
#SI2_std = SI2.std(dim={'south_north','west_east'})
#VW2_std = VW2.std(dim={'south_north','west_east'})
#WE2_std = WE2.std(dim={'south_north','west_east'})
#
#NO_std = NO_std.rename('NO_std_ref')
#CE_std = CE_std.rename('CE_std_ref')
#RU_std = RU_std.rename('RU_std_ref')
#SA_std = SA_std.rename('SA_std_ref')
#SE_std = SE_std.rename('SE_std_ref')
#SX_std = SX_std.rename('SX_std_ref')
#SI_std = SI_std.rename('SI_std_ref')
#VW_std = VW_std.rename('VW_std_ref')
#WE_std = WE_std.rename('WE_std_ref')
#
#NO1_std = NO1_std.rename('NO_std_sprawl')
#CE1_std = CE1_std.rename('CE_std_sprawl')
#RU1_std = RU1_std.rename('RU_std_sprawl')
#SA1_std = SA1_std.rename('SA_std_sprawl')
#SE1_std = SE1_std.rename('SE_std_sprawl')
#SX1_std = SX1_std.rename('SX_std_sprawl')
#SI1_std = SI1_std.rename('SI_std_sprawl')
#VW1_std = VW1_std.rename('VW_std_sprawl')
#WE1_std = WE1_std.rename('WE_std_sprawl')
#
#NO2_std = NO2_std.rename('NO_std_dense')
#CE2_std = CE2_std.rename('CE_std_dense')
#RU2_std = RU2_std.rename('RU_std_dense')
#SA2_std = SA2_std.rename('SA_std_dense')
#SE2_std = SE2_std.rename('SE_std_dense')
#SX2_std = SX2_std.rename('SX_std_dense')
#SI2_std = SI2_std.rename('SI_std_dense')
#VW2_std = VW2_std.rename('VW_std_dense')
#WE2_std = WE2_std.rename('WE_std_dense')
#
#
#NO_sp_mean, NO_t_mean = DataArray_to_dataframe(NO_mean, NO1_mean, NO2_mean)
#CE_sp_mean, CE_t_mean = DataArray_to_dataframe(CE_mean, CE1_mean, CE2_mean)
#RU_sp_mean, RU_t_mean = DataArray_to_dataframe(RU_mean, RU1_mean, RU2_mean)
#SA_sp_mean, SA_t_mean = DataArray_to_dataframe(SA_mean, SA1_mean, SA2_mean)
#SE_sp_mean, SE_t_mean = DataArray_to_dataframe(SE_mean, SE1_mean, SE2_mean)
#SX_sp_mean, SX_t_mean = DataArray_to_dataframe(SX_mean, SX1_mean, SX2_mean)
#SI_sp_mean, SI_t_mean = DataArray_to_dataframe(SI_mean, SI1_mean, SI2_mean)
#VW_sp_mean, VW_t_mean = DataArray_to_dataframe(VW_mean, VW1_mean, VW2_mean)
#WE_sp_mean, WE_t_mean = DataArray_to_dataframe(WE_mean, WE1_mean, WE2_mean)
#WW_sp_mean, WW_t_mean = DataArray_to_dataframe(WW_mean, WW1_mean, WW2_mean)
#
#
#NO_sp_std, NO_t_std = DataArray_to_dataframe(NO_std, NO1_std, NO2_std)
#CE_sp_std, CE_t_std = DataArray_to_dataframe(CE_std, CE1_std, CE2_std)
#RU_sp_std, RU_t_std = DataArray_to_dataframe(RU_std, RU1_std, RU2_std)
#SA_sp_std, SA_t_std = DataArray_to_dataframe(SA_std, SA1_std, SA2_std)
#SE_sp_std, SE_t_std = DataArray_to_dataframe(SE_std, SE1_std, SE2_std)
#SX_sp_std, SX_t_std = DataArray_to_dataframe(SX_std, SX1_std, SX2_std)
#SI_sp_std, SI_t_std = DataArray_to_dataframe(SI_std, SI1_std, SI2_std)
#VW_sp_std, VW_t_std = DataArray_to_dataframe(VW_std, VW1_std, VW2_std)
#WE_sp_std, WE_t_std = DataArray_to_dataframe(WE_std, WE1_std, WE2_std)
#
#list_sp_mean = [NO_sp_mean, CE_sp_mean, RU_sp_mean, SA_sp_mean, SE_sp_mean, SX_sp_mean, SI_sp_mean, VW_sp_mean, WE_sp_mean, WW_sp_mean]
#list_t_mean = [NO_t_mean, CE_t_mean, RU_t_mean, SA_t_mean, SE_t_mean, SX_t_mean, SI_t_mean, VW_t_mean, WE_t_mean, WW_t_mean]
#list_sp_std = [NO_sp_std, CE_sp_std, RU_sp_std, SA_sp_std, SE_sp_std, SX_sp_std, SI_sp_std, VW_sp_std, WE_sp_std]
#list_t_std = [NO_t_std, CE_t_std, RU_t_std, SA_t_std, SE_t_std, SX_t_std, SI_t_std, VW_t_std, WE_t_std]

min_2015, init_2015 = collect_data_speicherterm(date_2015, para, cuttime_2015, region=region, region_sn=region_sn, region_we=region_we, path=path)


#%%
"""
START

Create delta T Speicherterm between Wienerwald WW and other reference areas 
to verify if the waermeinseleffekt strengthens
"""
def speicherterm(data, case):
    ww = data[9][1]['WW_REF']
    deltaT_ref = []
    for i in data:
        T = i[1].iloc[:,case] - ww
        T = T.rename(i[1].iloc[:,case].name)
        deltaT_ref.append(T)
    deltaT_ref.pop(-1)
    return deltaT_ref

deltaT_ref = speicherterm(min_2015, 0)
deltaT_spr = speicherterm(min_2015, 1)
deltaT_opt = speicherterm(min_2015, 2)

 
#%%  
    
    
# sprawl run
ww = WW_sp_mean.iloc[:,1]
deltaT_spr = []
for i in list_sp_mean:
    T = i.iloc[:,1] - ww
    T = T.rename(i.iloc[:,1].name[:2]+'_spr')
    deltaT_spr.append(T)

# optimized city run
ww = WW_sp_mean.iloc[:,2]
deltaT_opt = []
for i in list_sp_mean:
    T = i.iloc[:,2] - ww
    T = T.rename(i.iloc[:,2].name[:2]+'_opt')
    deltaT_opt.append(T)

# drop RURAL comparison ... makes no sense 
deltaT_opt.pop(9)
deltaT_ref.pop(9)
deltaT_spr.pop(9)

"""
END
"""


varnam = str(data.name)
vardesc = str(data.description)
var1nam = str(data1.name)
var1desc = str(data1.description)
var2nam = str(data2.name)
var2desc = str(data2.description)

#%%
for idx, var in enumerate(deltaT_ref):
    
    title = '     --- Speicherterm: '+ str(deltaT_ref[idx].name[:2])+ ' - WW Wienerwald ---'
    
    """ START Trend creation with lin Regr model """
    
    trend_opt = deltaT_opt[idx]
    trend_opt = trend_opt.reset_index()
    trend_opt = trend_opt.set_index(trend_opt['day'])
    trend_opt = trend_opt.drop(columns='day')
    opt_model = lm(trend_opt)
    trend_opt = opt_model.predict()
    
    trend_spr = deltaT_spr[idx]
    trend_spr = trend_spr.reset_index()
    trend_spr = trend_spr.set_index(trend_spr['day'])
    trend_spr = trend_spr.drop(columns='day')
    spr_model = lm(trend_spr)
    trend_spr = spr_model.predict()
    
    trend_ref = deltaT_ref[idx]
    trend_ref = trend_ref.reset_index()
    trend_ref = trend_ref.set_index(trend_ref['day'])
    trend_ref = trend_ref.drop(columns='day')
    ref_model = lm(trend_ref)
    trend_ref = ref_model.predict()
    
    times = pd.date_range('2015-08-'+str(deltaT_ref[idx].index.levels[0][0]), '2015-08-'+str(deltaT_ref[idx].index.levels[0][-1]))
    """ END Trend creation with lin Regr model """

    
    fig, ax = plt.subplots(figsize=(16,9), sharex=True)
    
    ax1 = plt.subplot(211)
    ax1.plot(times, deltaT_ref[idx], c='k')#, label=str(deltaT_ref[idx].name[3:]))
    ax1.plot(times, deltaT_spr[idx], c='C3', label=str(deltaT_spr[idx].name[3:]))
    ax1.plot(times, deltaT_opt[idx], c='C2', label=str(deltaT_opt[idx].name[3:]))
#    ax1.plot(times, trend_spr, c='C3', ls='-.', label=str(deltaT_spr[idx].name[3:]+' Trend'))
    ax1.tick_params(axis='x', rotation=90)
    ax1.axhline(0, color='r')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('\nSPR Speicherterm')
    ax1.grid(True)
    ax1.set_ylim(-4,6)
    ax1limits = ax1.get_ylim()
    ax1.xaxis.set_major_locator(mdates.DayLocator())   #to get a tick every 15 minutes
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))     #optional formatting 
    
#    ax2 = ax1.twinx()
#    ax2.plot(times, deltaT_spr[idx]-deltaT_ref[idx], c='C3', ls=':', label=' Diff spr-ref')
#    ax2.set_ylabel(str(data.name) + ' run differences ' + '['+ str(data.units)+']')
#    #ax2.set_ylim(0,20)
#    #ax2.grid(True)
#    ax2.xaxis.set_major_locator(mdates.HourLocator(interval=6))   #to get a tick every 15 minutes
#    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))     #optional formatting 
#    ax2.set_ylim(-1,2)

    
    ax5 = plt.subplot(212)
    
    ax5.plot(times, trend_ref, c='k', ls='-.')
    ax5.plot(times, trend_spr, c='C3', ls='-.')
    ax5.plot(times, trend_opt, c='C2', ls='-.')
    ax5.tick_params(axis='x', rotation=90)
    ax5.set_xlabel('Time')
    ax5.set_ylabel('\ntrend comparison ')
    ax5.grid(True)
    
    ax5.xaxis.set_major_locator(mdates.DayLocator())   #to get a tick every 15 minutes
    ax5.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))     #optional formatting 

    
#    ax3 = plt.subplot(313)
#    
#    ax3.plot(times, deltaT_ref[idx], c='k', label=str(deltaT_ref[idx].name[3:]))
#    ax3.plot(times, deltaT_opt[idx], c='C2', label=str(deltaT_opt[idx].name[3:]))
#    ax3.plot(times, trend_opt, c='C2', ls='-.', label=str(deltaT_opt[idx].name[3:]+' Trend'))
#    ax3.tick_params(axis='x', rotation=90)
#    ax3.set_xlabel('Time')
#    ax3.set_ylabel('\nOPT Speicherterm ')
#    ax3.axhline(0, color='r')
#    ax3.grid(True)
#    ax3.set_ylim(ax1limits)
#    ax3.xaxis.set_major_locator(mdates.DayLocator())   #to get a tick every 15 minutes
#    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))     #optional formatting 

#    ax4 = ax3.twinx()
#    ax4.plot(times, deltaT_opt[idx]-deltaT_ref[idx], c='C2', ls=':', label=' Diff opt-ref')
#    ax4.set_ylabel(str(data.name) + ' run differences ' + '['+ str(data.units)+']')
#    #ax2.set_ylim(0,20)
#    #ax2.grid(True)
#    ax4.xaxis.set_major_locator(mdates.HourLocator(interval=6))   #to get a tick every 15 minutes
#    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))     #optional formatting 
#    ax4.set_ylim(ax1limits)

    
    plt.subplots_adjust(hspace=0.)
    
    ax1 = plt.gca()
    #ax1.text(0,1.04,run , fontsize=14, transform=ax.transAxes)
    ax1.text(0,1.04,'reference Area: ' + deltaT_ref[idx].name[:2]+ '   ' + title, fontsize=16, transform=ax.transAxes)
#    ax1.text(0,1.01,varnam + ' - ' + vardesc, fontsize=12, transform=ax.transAxes)
    ax1.text(0.7,1.01,'Init: ' + init_2015, fontsize=14, transform=ax.transAxes)
    
    fig.legend(fontsize='small', loc='right')
    fig.autofmt_xdate()
    
    filename = domain + '_' + str(para) + '_' + deltaT_ref[idx].name[:2] + '_Speicherterm'  +".png"
    plt.savefig(plotdir_2015 + filename)