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

 Diurnal Plot of WIND 
     + diurnal plot of windspeed
     + diurnal plot of winddirection
     
"""

""" startdate of run - uncomment used run """
#date = '2069-07-01'
date = '2015-08-05'

domain = 'd03'
run = 'REF_Run_2015'
run1 = 'SPR_Run_2015'
run2 = 'OPT_Run_2015'
path = '/hp4/Urbania/WRF-2019-Runs/' # runPATH
filepath = path + run + '/'
filepath1 = path + run1 + '/'
filepath2 = path + run2 + '/'
u10 = 'U10'
v10 = 'V10'

""" not usable days - uncomment used run """
#cuttime = pd.to_datetime(['2069-7-1','2069-7-2','2069-7-3','2069-7-4','2069-7-5', '2069-7-6','2069-7-9']) # day with not usable data
cuttime = pd.to_datetime(['2015-08-05', '2015-08-06', '2015-08-07', '2015-08-08','2015-08-11', '2015-08-14']) # 2015 run


filenam = 'wrfout_' + domain + '_' + date + '_18_00_00.nc'
plot_dir ='/hp4/Urbania/plots/' + date + '/'
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)
    
def winddir(u, v):
    wdir = (np.pi/2 - np.arctan2(-v, -u)) * 180/np.pi
    wdir %= 360
    return wdir

def DataArray_to_dataframe(array1, array2, array3):
    """
    Converts 3 DataArrays with metadata to an pandas DataFrame
    & drops XTIME so it can calculate the temporal means betweens he columns
    
    Input: 3 DataArray
    Output: 1 Dataframe, Mean of Columns
    """
    frame = array1.to_dataframe()
    frame[str(array2.description[7:13])] = array2.to_series()
    frame[str(array3.description[7:13])] = array3.to_series()
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
    frame[str(array2.description[7:13])] = array2.to_series()
    frame[str(array2.description[7:13])] = array3.to_series()
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


def area_diurnal_param(data, south_north, west_east, cuttime, name ):
    
    """ START Areal & Temporal Selection """
    area = data.isel(south_north=slice(south_north[0],south_north[1]), west_east=slice(west_east[0],west_east[1]))
    for i in cuttime:
        area = area.where(area['Time'].dt.day != i.day, drop=True).rename(name)

    """ START Calc of MEDIAN, MIN, MAX """
    area_diurnal_mean = area.groupby(area.Time.dt.hour).median()
    area_diurnal_min = area.groupby(area.Time.dt.day).min(axis=0)
    area_diurnal_max = area.groupby(area.Time.dt.day).max(axis=0)
    
    """ START RENAMING """
    area_diurnal_max = area_diurnal_max.assign_attrs({'projection': data.projection,
                                        'description': 'MAX '+ name + data.description,
                                        'units': data.units})
    area_diurnal_min = area_diurnal_min.assign_attrs({'projection': data.projection,
                                    'description': 'MIN '+ name + data.description,
                                    'units': data.units})
    area_diurnal_mean= area_diurnal_mean.assign_attrs({'projection': data.projection,
                                        'description': 'MEDIAN ' + name + data.description,
                                        'units': data.units})
    return area_diurnal_mean, area_diurnal_min, area_diurnal_max

def area_diurnal_dir(u, v, south_north, west_east, cuttime, name ):
    """
    Calcs the mean winddir by calculatin g the mean of u and v and 
    with the resulting vector the mean DIR
    """
    
    
    """ START Areal & Temporal Selection """
    u = u.isel(south_north=slice(south_north[0],south_north[1]), west_east=slice(west_east[0],west_east[1]))
    v = v.isel(south_north=slice(south_north[0],south_north[1]), west_east=slice(west_east[0],west_east[1]))

    for i in cuttime:
        u = u.where(u['Time'].dt.day != i.day, drop=True).rename(name)
        v = v.where(v['Time'].dt.day != i.day, drop=True).rename(name)

    """ START Calc of MEDIAN of windcomponents and calc of winddir"""
    u_diurnal_mean = u.groupby(u.Time.dt.hour).median()
    v_diurnal_mean = v.groupby(v.Time.dt.hour).median()
    
    dd = winddir(u_diurnal_mean, v_diurnal_mean)
    
    """ START RENAMING """
    dd = dd.assign_attrs({'projection': u.projection,
                                        'description': 'MEDIAN ' + name + 'winddirection in 10m',
                                        'units': 'degrees'})
    return dd




ncfile = Dataset(filepath + filenam)
ncfile1 = Dataset(filepath1 + filenam)
ncfile2 = Dataset(filepath2 + filenam)
#ncfile2 = Dataset(filepath2 + filenam)
#Dimension of domain
ref_u10 = getvar(ncfile, u10, timeidx=wrf.ALL_TIMES)
ref_v10 = getvar(ncfile, v10, timeidx=wrf.ALL_TIMES)
spr_u10 = getvar(ncfile1, u10, timeidx=wrf.ALL_TIMES)
spr_v10 = getvar(ncfile1, v10, timeidx=wrf.ALL_TIMES)
opt_u10 = getvar(ncfile2, u10, timeidx=wrf.ALL_TIMES)
opt_v10 = getvar(ncfile2, v10, timeidx=wrf.ALL_TIMES)

times = getvar(ncfile1, "Times", timeidx=wrf.ALL_TIMES, meta=False) # FC times in np.datetime64 format - very ugly
init = pd.to_datetime(times[0]) # converts the numpy datetime to datetime datetime format
init = str(init) # initial time of wrf dataset


""" START Calculation of resulting windvector """

ref_v = np.sqrt(ref_u10**2 + ref_v10**2)
spr_v = np.sqrt(spr_u10**2 + spr_v10**2)
opt_v = np.sqrt(opt_u10**2 + opt_v10**2)

ref_v = ref_v.assign_attrs({'projection': ref_u10.projection,
                                    'description': 'Ref windspeed in 10m',
                                    'units': ref_u10.units})
spr_v = spr_v.assign_attrs({'projection': spr_u10.projection,
                                    'description': 'Spr windspeed in 10m',
                                    'units': spr_u10.units})
opt_v = opt_v.assign_attrs({'projection': opt_u10.projection,
                                    'description': 'Opt windspeed in 10m',
                                    'units': opt_u10.units})



""" END Calculation of resulting windvector """




""" START areal and temporal selection + calculation of MEDIAN / MIN / MAX """


region = {'NO_sn': (73,82), 'NO_we': (89,98),
          'CE_sn': (50,59), 'CE_we': (80,89),
          'RU_sn': (57,66), 'RU_we': (128,137),
          'SA_sn': (58,67), 'SA_we': (109,118),
          'SE_sn': (37,46), 'SE_we': (99,108),
          'SX_sn': (24,33), 'SX_we': (75,84),
          'SI_sn': (31,40), 'SI_we': (68,77),
          'VW_sn': (47,56), 'VW_we': (64,73),
          'WE_sn': (62,71), 'WE_we': (73,82)
          }



ref_NO_v_mean, ref_NO_v_min, ref_NO_v_max = area_diurnal_param(ref_v, region['NO_sn'], region['NO_we'],  cuttime, 'NO ')
spr_NO_v_mean, spr_NO_v_min, spr_NO_v_max = area_diurnal_param(spr_v, region['NO_sn'], region['NO_we'],  cuttime, 'NO ')
opt_NO_v_mean, opt_NO_v_min, opt_NO_v_max = area_diurnal_param(opt_v, region['NO_sn'], region['NO_we'],  cuttime, 'NO ')

ref_CE_v_mean, ref_CE_v_min, ref_CE_v_max = area_diurnal_param(ref_v, region['CE_sn'], region['CE_we'],  cuttime, 'CE ')
spr_CE_v_mean, spr_CE_v_min, spr_CE_v_max = area_diurnal_param(spr_v, region['CE_sn'], region['CE_we'],  cuttime, 'CE ')
opt_CE_v_mean, opt_CE_v_min, opt_CE_v_max = area_diurnal_param(opt_v, region['CE_sn'], region['CE_we'],  cuttime, 'CE ')

ref_RU_v_mean, ref_RU_v_min, ref_RU_v_max = area_diurnal_param(ref_v, region['RU_sn'], region['RU_we'],  cuttime, 'RU ')
spr_RU_v_mean, spr_RU_v_min, spr_RU_v_max = area_diurnal_param(spr_v, region['RU_sn'], region['RU_we'],  cuttime, 'RU ')
opt_RU_v_mean, opt_RU_v_min, opt_RU_v_max = area_diurnal_param(opt_v, region['RU_sn'], region['RU_we'],  cuttime, 'RU ')

ref_SA_v_mean, ref_SA_v_min, ref_SA_v_max = area_diurnal_param(ref_v, region['SA_sn'], region['SA_we'],  cuttime, 'SA ')
spr_SA_v_mean, spr_SA_v_min, spr_SA_v_max = area_diurnal_param(spr_v, region['SA_sn'], region['SA_we'],  cuttime, 'SA ')
opt_SA_v_mean, opt_SA_v_min, opt_SA_v_max = area_diurnal_param(opt_v, region['SA_sn'], region['SA_we'],  cuttime, 'SA ')

ref_SE_v_mean, ref_SE_v_min, ref_SE_v_max = area_diurnal_param(ref_v, region['SE_sn'], region['SE_we'],  cuttime, 'SE ')
spr_SE_v_mean, spr_SE_v_min, spr_SE_v_max = area_diurnal_param(spr_v, region['SE_sn'], region['SE_we'],  cuttime, 'SE ')
opt_SE_v_mean, opt_SE_v_min, opt_SE_v_max = area_diurnal_param(opt_v, region['SE_sn'], region['SE_we'],  cuttime, 'SE ')

ref_SX_v_mean, ref_SX_v_min, ref_SX_v_max = area_diurnal_param(ref_v, region['SX_sn'], region['SX_we'],  cuttime, 'SX ')
spr_SX_v_mean, spr_SX_v_min, spr_SX_v_max = area_diurnal_param(spr_v, region['SX_sn'], region['SX_we'],  cuttime, 'SX ')
opt_SX_v_mean, opt_SX_v_min, opt_SX_v_max = area_diurnal_param(opt_v, region['SX_sn'], region['SX_we'],  cuttime, 'SX ')

ref_SI_v_mean, ref_SI_v_min, ref_SI_v_max = area_diurnal_param(ref_v, region['SI_sn'], region['SI_we'],  cuttime, 'SI ')
spr_SI_v_mean, spr_SI_v_min, spr_SI_v_max = area_diurnal_param(spr_v, region['SI_sn'], region['SI_we'],  cuttime, 'SI ')
opt_SI_v_mean, opt_SI_v_min, opt_SI_v_max = area_diurnal_param(opt_v, region['SI_sn'], region['SI_we'],  cuttime, 'SI ')

ref_VW_v_mean, ref_VW_v_min, ref_VW_v_max = area_diurnal_param(ref_v, region['VW_sn'], region['VW_we'],  cuttime, 'VW ')
spr_VW_v_mean, spr_VW_v_min, spr_VW_v_max = area_diurnal_param(spr_v, region['VW_sn'], region['VW_we'],  cuttime, 'VW ')
opt_VW_v_mean, opt_VW_v_min, opt_VW_v_max = area_diurnal_param(opt_v, region['VW_sn'], region['VW_we'],  cuttime, 'VW ')

ref_WE_v_mean, ref_WE_v_min, ref_WE_v_max = area_diurnal_param(ref_v, region['WE_sn'], region['WE_we'],  cuttime, 'WE ')
spr_WE_v_mean, spr_WE_v_min, spr_WE_v_max = area_diurnal_param(spr_v, region['WE_sn'], region['WE_we'],  cuttime, 'WE ')
opt_WE_v_mean, opt_WE_v_min, opt_WE_v_max = area_diurnal_param(opt_v, region['WE_sn'], region['WE_we'],  cuttime, 'WE ')


ref_NO_dd_mean = area_diurnal_dir(ref_u10, ref_v10, region['NO_sn'], region['NO_we'],  cuttime, 'NO Ref')
spr_NO_dd_mean = area_diurnal_dir(spr_u10, spr_v10, region['NO_sn'], region['NO_we'],  cuttime, 'NO Spr')
opt_NO_dd_mean = area_diurnal_dir(opt_u10, opt_v10, region['NO_sn'], region['NO_we'],  cuttime, 'NO opt')

ref_CE_dd_mean = area_diurnal_dir(ref_u10, ref_v10, region['CE_sn'], region['CE_we'],  cuttime, 'CE Ref')
spr_CE_dd_mean = area_diurnal_dir(spr_u10, spr_v10, region['CE_sn'], region['CE_we'],  cuttime, 'CE Spr')
opt_CE_dd_mean = area_diurnal_dir(opt_u10, opt_v10, region['CE_sn'], region['CE_we'],  cuttime, 'CE opt')

ref_RU_dd_mean = area_diurnal_dir(ref_u10, ref_v10, region['RU_sn'], region['RU_we'],  cuttime, 'RU Ref')
spr_RU_dd_mean = area_diurnal_dir(spr_u10, spr_v10, region['RU_sn'], region['RU_we'],  cuttime, 'RU Spr')
opt_RU_dd_mean = area_diurnal_dir(opt_u10, opt_v10, region['RU_sn'], region['RU_we'],  cuttime, 'RU opt')

ref_SA_dd_mean = area_diurnal_dir(ref_u10, ref_v10, region['SA_sn'], region['SA_we'],  cuttime, 'SA Ref')
spr_SA_dd_mean = area_diurnal_dir(spr_u10, spr_v10, region['SA_sn'], region['SA_we'],  cuttime, 'SA Spr')
opt_SA_dd_mean = area_diurnal_dir(opt_u10, opt_v10, region['SA_sn'], region['SA_we'],  cuttime, 'SA opt')

ref_SE_dd_mean = area_diurnal_dir(ref_u10, ref_v10, region['SE_sn'], region['SE_we'],  cuttime, 'SE Ref')
spr_SE_dd_mean = area_diurnal_dir(spr_u10, spr_v10, region['SE_sn'], region['SE_we'],  cuttime, 'SE Spr')
opt_SE_dd_mean = area_diurnal_dir(opt_u10, opt_v10, region['SE_sn'], region['SE_we'],  cuttime, 'SE opt')

ref_SX_dd_mean = area_diurnal_dir(ref_u10, ref_v10, region['SX_sn'], region['SX_we'],  cuttime, 'SX Ref')
spr_SX_dd_mean = area_diurnal_dir(spr_u10, spr_v10, region['SX_sn'], region['SX_we'],  cuttime, 'SX Spr')
opt_SX_dd_mean = area_diurnal_dir(opt_u10, opt_v10, region['SX_sn'], region['SX_we'],  cuttime, 'SX opt')

ref_SI_dd_mean = area_diurnal_dir(ref_u10, ref_v10, region['SI_sn'], region['SI_we'],  cuttime, 'SI Ref')
spr_SI_dd_mean = area_diurnal_dir(spr_u10, spr_v10, region['SI_sn'], region['SI_we'],  cuttime, 'SI Spr')
opt_SI_dd_mean = area_diurnal_dir(opt_u10, opt_v10, region['SI_sn'], region['SI_we'],  cuttime, 'SI opt')

ref_VW_dd_mean = area_diurnal_dir(ref_u10, ref_v10, region['VW_sn'], region['VW_we'],  cuttime, 'VW Ref')
spr_VW_dd_mean = area_diurnal_dir(spr_u10, spr_v10, region['VW_sn'], region['VW_we'],  cuttime, 'VW Spr')
opt_VW_dd_mean = area_diurnal_dir(opt_u10, opt_v10, region['VW_sn'], region['VW_we'],  cuttime, 'VW opt')

ref_WE_dd_mean = area_diurnal_dir(ref_u10, ref_v10, region['WE_sn'], region['WE_we'],  cuttime, 'WE Ref')
spr_WE_dd_mean = area_diurnal_dir(spr_u10, spr_v10, region['WE_sn'], region['WE_we'],  cuttime, 'WE Spr')
opt_WE_dd_mean = area_diurnal_dir(opt_u10, opt_v10, region['WE_sn'], region['WE_we'],  cuttime, 'WE opt')


""" END areal and temporal selection + calculation of MEDIAN / MIN / MAX """

NO_v_mean = DataArray_to_dataframe(ref_NO_v_mean, spr_NO_v_mean, opt_NO_v_mean)
CE_v_mean = DataArray_to_dataframe(ref_CE_v_mean, spr_CE_v_mean, opt_CE_v_mean)
RU_v_mean = DataArray_to_dataframe(ref_RU_v_mean, spr_RU_v_mean, opt_RU_v_mean)
SA_v_mean = DataArray_to_dataframe(ref_SA_v_mean, spr_SA_v_mean, opt_SA_v_mean)
SE_v_mean = DataArray_to_dataframe(ref_SE_v_mean, spr_SE_v_mean, opt_SE_v_mean)
SX_v_mean = DataArray_to_dataframe(ref_SX_v_mean, spr_SX_v_mean, opt_SX_v_mean)
SI_v_mean = DataArray_to_dataframe(ref_SI_v_mean, spr_SI_v_mean, opt_SI_v_mean)
VW_v_mean = DataArray_to_dataframe(ref_VW_v_mean, spr_VW_v_mean, opt_VW_v_mean)
WE_v_mean = DataArray_to_dataframe(ref_WE_v_mean, spr_WE_v_mean, opt_WE_v_mean)

NO_dd_mean = DataArray_to_dataframe(ref_NO_dd_mean, spr_NO_dd_mean, opt_NO_dd_mean)
CE_dd_mean = DataArray_to_dataframe(ref_CE_dd_mean, spr_CE_dd_mean, opt_CE_dd_mean)
RU_dd_mean = DataArray_to_dataframe(ref_RU_dd_mean, spr_RU_dd_mean, opt_RU_dd_mean)
SA_dd_mean = DataArray_to_dataframe(ref_SA_dd_mean, spr_SA_dd_mean, opt_SA_dd_mean)
SE_dd_mean = DataArray_to_dataframe(ref_SE_dd_mean, spr_SE_dd_mean, opt_SE_dd_mean)
SX_dd_mean = DataArray_to_dataframe(ref_SX_dd_mean, spr_SX_dd_mean, opt_SX_dd_mean)
SI_dd_mean = DataArray_to_dataframe(ref_SI_dd_mean, spr_SI_dd_mean, opt_SI_dd_mean)
VW_dd_mean = DataArray_to_dataframe(ref_VW_dd_mean, spr_VW_dd_mean, opt_VW_dd_mean)
WE_dd_mean = DataArray_to_dataframe(ref_WE_dd_mean, spr_WE_dd_mean, opt_WE_dd_mean)

NO_v_min = DataArray_drop_to_Frame(ref_NO_v_min, spr_NO_v_min, opt_NO_v_min)
CE_v_min = DataArray_drop_to_Frame(ref_CE_v_min, spr_CE_v_min, opt_CE_v_min)
RU_v_min = DataArray_drop_to_Frame(ref_RU_v_min, spr_RU_v_min, opt_RU_v_min)
SA_v_min = DataArray_drop_to_Frame(ref_SA_v_min, spr_SA_v_min, opt_SA_v_min)
SE_v_min = DataArray_drop_to_Frame(ref_SE_v_min, spr_SE_v_min, opt_SE_v_min)
SX_v_min = DataArray_drop_to_Frame(ref_SX_v_min, spr_SX_v_min, opt_SX_v_min)
SI_v_min = DataArray_drop_to_Frame(ref_SI_v_min, spr_SI_v_min, opt_SI_v_min)
VW_v_min = DataArray_drop_to_Frame(ref_VW_v_min, spr_VW_v_min, opt_VW_v_min)
WE_v_min = DataArray_drop_to_Frame(ref_WE_v_min, spr_WE_v_min, opt_WE_v_min)


NO_v_max = DataArray_drop_to_Frame(ref_NO_v_max, spr_NO_v_max, opt_NO_v_max)
CE_v_max = DataArray_drop_to_Frame(ref_CE_v_max, spr_CE_v_max, opt_CE_v_max)
RU_v_max = DataArray_drop_to_Frame(ref_RU_v_max, spr_RU_v_max, opt_RU_v_max)
SA_v_max = DataArray_drop_to_Frame(ref_SA_v_max, spr_SA_v_max, opt_SA_v_max)
SE_v_max = DataArray_drop_to_Frame(ref_SE_v_max, spr_SE_v_max, opt_SE_v_max)
SX_v_max = DataArray_drop_to_Frame(ref_SX_v_max, spr_SX_v_max, opt_SX_v_max)
SI_v_max = DataArray_drop_to_Frame(ref_SI_v_max, spr_SI_v_max, opt_SI_v_max)
VW_v_max = DataArray_drop_to_Frame(ref_VW_v_max, spr_VW_v_max, opt_VW_v_max)
WE_v_max = DataArray_drop_to_Frame(ref_WE_v_max, spr_WE_v_max, opt_WE_v_max)




""" data collecting for automated plotting routine """
v_mean = [NO_v_mean, CE_v_mean, RU_v_mean, SA_v_mean, SE_v_mean, SX_v_mean, SI_v_mean, VW_v_mean, WE_v_mean]
v_min = [NO_v_min, CE_v_min, RU_v_min, SA_v_min, SE_v_min, SX_v_min, SI_v_min, VW_v_min, WE_v_min]
v_max = [NO_v_max, CE_v_max, RU_v_max, SA_v_max, SE_v_max, SX_v_max, SI_v_max, VW_v_max, WE_v_max]

dd_mean = [NO_dd_mean, CE_dd_mean, RU_dd_mean, SA_dd_mean, SE_dd_mean, SX_dd_mean, SI_dd_mean, VW_dd_mean, WE_dd_mean]


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
""" Plotting Routine """


title = '10m diurnal wind'

times = pd.date_range('08/08/2015 00:00:00', '08/08/2015 23:00:00', freq='H')

for idx, var in enumerate(v_mean):
    
    fig, ax = plt.subplots(figsize=(16,9))
    gs = gridspec.GridSpec(2, 1)


    ax1 = plt.subplot(gs[0])
    
    ax1.plot(times, v_mean[idx].iloc[:,0], c='k', label=str(v_mean[idx].iloc[:,0].name[3:])+ 'Ref median')
    ax1.plot(times, v_mean[idx].iloc[:,1], c='C3', label=str(v_mean[idx].iloc[:,1].name[3:])+ ' median')
    ax1.plot(times, v_mean[idx].iloc[:,2], c='C2', label=str(v_mean[idx].iloc[:,2].name[3:])+ ' median')
    ax1.tick_params(axis='x', rotation=90)
    ax1.set_xlabel('Times')
    ax1.set_ylabel(str(ref_NO_v_mean.description[14:]) + '\nmittlerer Tagesgang ' + '['+str(ref_NO_v_mean.units)+']')
       
    #if data.name == 'GLW':
    #    ax1.set_ylim(330, 430)
    ax1.legend(fontsize='small', loc='upper left')
    ax1.grid(True)
    ax1ylim = ax1.get_ylim()
    ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))   #to get a tick every 15 minutes
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))     #optional formatting 

#    ax2 = ax1.twinx()
#    ax2.plot(times, v_std[idx].iloc[:,0], c='k', ls=':', label=str(v_std[idx].iloc[:,0].name[3:])+ ' std')
#    ax2.plot(times, v_std[idx].iloc[:,1], c='C3', ls=':', label=str(v_std[idx].iloc[:,1].name[3:])+ ' std')
#    ax2.plot(times, v_std[idx].iloc[:,2], c='C2', ls=':', label=str(v_std[idx].iloc[:,2].name[3:])+ ' std')
#    ax2.set_ylabel(str(data.name) + ' Std ' + '['+str(data.units)+']')
#    #ax2.set_ylim(0,20)
#    ax2.xaxis.set_major_locator(mdates.HourLocator(interval=2))   #to get a tick every 15 minutes
#    #ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))     #optional formatting 
#
#    ax2.legend(fontsize='small', loc='upper right')
    
    
    # Correlation zwischen den Laeufen
    
    
    ax3 = plt.subplot(gs[1])
    
    ax3.plot(times, dd_mean[idx].iloc[:,0], c='k', linewidth=0, marker='X', label='Dir Ref')
    ax3.plot(times, dd_mean[idx].iloc[:,1], c='C3', linewidth=0, marker='o', label='Dir Spr')
    ax3.plot(times, dd_mean[idx].iloc[:,2], c='C2', linewidth=0, marker='<', label='Dir Opt')
    ax3.set_xlabel('Times')
    ax3.set_ylabel(str(ref_NO_dd_mean.description[14:]) + '\nmittlerer Tagesgang ' + '['+str(ref_NO_dd_mean.units)+']')
    ax3.legend(fontsize='small', loc='lower left')
    ax3.set_ylim(0, 360)
    yticks = [0, 90, 180 , 270, 360]
    ylabels = ['N', 'E', 'S', 'W', 'N']
    ax3.set_yticks(yticks)
    ax3.set_yticklabels(ylabels)
    
    ax3.grid(True)
    ax3.xaxis.set_major_locator(mdates.HourLocator(interval=2))   #to get a tick every 15 minutes
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))     #optional formatting 
    
#    ax5 = plt.subplot(gs[1])
#    boxprops = dict( linewidth=1.5, color='b')
#    flierprops = dict(marker='x', linestyle='none')
#    medianprops = dict(linestyle='-', linewidth=2.5, color='firebrick')
#    meanpointprops = dict(marker='D', markeredgecolor='black',
#                      markerfacecolor='g')
#    whiskerprops = dict( linestyle='--', color='k')
#
#    ax5.boxplot([v_max[idx].iloc[:,0], v_max[idx].iloc[:,1],v_max[idx].iloc[:,2]],
#                notch=True, labels=['REF','SPR', 'OPT'], boxprops=boxprops, showfliers=True, flierprops=flierprops, 
#                medianprops=medianprops, showmeans=True, meanprops=meanpointprops, 
#                whiskerprops=whiskerprops)
#    ax5.tick_params(axis='y', labelleft='off', labelright='on')
#    ax5.set_ylabel('Daily MAX')
#    ax5.grid(True)
#
#    ax4 = plt.subplot(gs[3])
#    
#    ax4.boxplot([v_min[idx].iloc[:,0], v_min[idx].iloc[:,1],v_min[idx].iloc[:,2]],
#                notch=True, labels=['REF','SPR', 'OPT'], boxprops=boxprops, showfliers=True, flierprops=flierprops, 
#                medianprops=medianprops, showmeans=True, meanprops=meanpointprops, 
#                whiskerprops=whiskerprops)
#    ax4.tick_params(axis='y', labelleft='off', labelright='on')
#    ax4.set_ylabel('Daily MIN')
#    ax4.grid(True)
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
#    ax1.text(0,1.04,run , fontsize=14, transform=ax.transAxes)
    ax1.text(0.,1.07,title, fontsize=16, transform=ax.transAxes)
    ax1.text(0.,1.02, 'reference area: ' + v_mean[idx].iloc[:,0].name[:2], fontsize=12, transform=ax.transAxes)
    ax1.text(0.7,1.01,'init: ' + init, fontsize=10, transform=ax.transAxes)
    
    #fig.autofmt_xdate()
    #fig.legend(fontsize='small', loc='upper right')
    
    filename = domain + '_' + '_' + v_mean[idx].iloc[:,0].name[:2] + '_WIND'  +".png"
    plt.savefig(plot_dir + filename)