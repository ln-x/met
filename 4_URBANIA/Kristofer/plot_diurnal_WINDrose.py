# -*- coding: utf-8 -*-
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
import xarray as xr
import os
import wrf
import matplotlib.dates as mdates
from wrf import getvar


"""

 Diurnal Plot of WIND 
     + diurnal plot of windspeed
     + diurnal plot of winddirection
     
"""

# EXAMPLE
# plot 30-year mean of precipitation dataset
# load data as xarray dataset
date = '2069-07-01'
#date = '2015-08-05'
domain = 'd03'
run = 'REF_Run_2069'
run1 = 'SPR_Run_2069'
run2 = 'OPT_Run_2069'
path = '/hp4/Urbania/WRF-2019-Runs/' # runPATH
filepath = path + run + '/'
filepath1 = path + run1 + '/'
filepath2 = path + run2 + '/'
u10 = 'U10'
v10 = 'V10'

""" not usable days - uncomment used run """
cuttime = pd.to_datetime(['2069-7-1','2069-7-2','2069-7-3','2069-7-4','2069-7-5', '2069-7-6','2069-7-9']) # day with not usable data
#cuttime = pd.to_datetime(['2015-08-05', '2015-08-06', '2015-08-07', '2015-08-08','2015-08-11', '2015-08-14']) # 2015 run


filenam = 'wrfout_' + domain + '_' + date + '_18_00_00.nc'
plot_dir ='/hp4/Urbania/plots/' + date + '/'
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)

def windrose_subplot(wspd, wdir, subplot, title, rmax=50, rsteps=10, nsector=20, opening=0.8, bins=np.array([0.5, 1., 2., 3., 4., 5., 6.]), normed=True, cmap=cm.viridis, edgecol='white', legendloc='lower left', legendsize='xx-small' ):
    """ 
    Creates a WINDROSE subplot
    you have to install windrose package in your conda env !
    
    https://windrose.readthedocs.io/en/latest/index.html
    
    -----
    Manuell:
        wspd = windspeed
        wdir = winddirection with 0 degree set to NORTH !
                + use function winddir
                + if you want a mean of a field, first create mean of u & v !
        rmax = like ylim, max of r axes
        rsteps = intervall to rmax
        nsector = how many sectors should be created, 
                for example nsector = 36 creates 36 sectors with each 10 degree angle
        opening = distance between sectors, no dist = 1
        bins = windspeed classes
        normed = should windspeed data be normed? if True, output in percent
        cmap = colormap
        edgecol = framecolor of sectors
    -----
    """
    
    ax = plt.subplot(subplot, projection='windrose')
    ax.set_title(title +  '\n')
    ax.bar(wdir, wspd, normed=normed, 
               bins=bins, nsector=nsector, opening=opening, edgecolor=edgecol, cmap=cmap)
    ax.set_legend(loc=legendloc, fontsize=legendsize)
    ax.set_rmax(rmax)
    ax.set_rgrids(np.arange(rsteps, rmax+rsteps, rsteps), labels=tuple(np.arange(rsteps, rmax+rsteps, rsteps)))
    return ax

def winddir(u, v):
    wdir = (np.pi/2 - np.arctan2(- v, - u)) * 180/np.pi
    wdir %= 360
    return wdir


def DataArray_to_dataframe(array1, array2, array3):
    """
    Converts 3 DataArrays with metadata to an pandas DataFrame
    & drops XTIME so it can calculate the temporal means betweens he columns
    
    Input: 3 DataArray
    Output: 1 Dataframe, Mean of Columns
    """
    frame = pd.merge(array1, array2)
    df = pd.merge(frame, array3)
    #frame = frame.drop(columns=['XTIME'])
    #mean = frame.mean(axis=1)
    return df #, mean

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


def area_day_night(data_spd, data_dir, south_north, west_east, cuttime, name ):
    """ START Areal & Temporal Selection """
    spd = data_spd.isel(south_north=slice(south_north[0],south_north[1]), west_east=slice(west_east[0],west_east[1]))
    dire = data_dir.isel(south_north=slice(south_north[0],south_north[1]), west_east=slice(west_east[0],west_east[1]))

    for i in cuttime:
        spd = spd.where(spd['Time'].dt.day != i.day, drop=True).rename(name)
        dire = dire.where(dire['Time'].dt.day != i.day, drop=True).rename(name)
    
    spd = spd.median(dim={'south_north','west_east'})
    dire = dire.median(dim={'south_north','west_east'})
    
    spd_night = spd[(spd.Time.dt.hour <= 6) | (spd.Time.dt.hour > 18)].rename('speed')
    dire_night = dire[(dire.Time.dt.hour <= 6) | (dire.Time.dt.hour > 18)].rename('direction')
    spd_day = spd[(spd.Time.dt.hour <= 18) & (spd.Time.dt.hour > 6)].rename('speed')
    dire_day = dire[(dire.Time.dt.hour <=18) & (dire.Time.dt.hour > 6)].rename('direction')
    
    day = pd.DataFrame(index=spd_day.indexes.values())
    day[str(name[:3]) + '_speed'] = spd_day.data
    day[str(name[:3]) + '_direction'] = dire_day.data
    night = pd.DataFrame(index=spd_night.indexes.values())
    night[str(name[:3]) + '_speed'] = spd_night.data
    night[str(name[:3]) + '_direction'] = dire_night.data
    
    day.name = name + '_day'
    night.name = name + '_night'
#    day = xr.concat(spd_day, dire_day, dim='XTIME')
#    night = xr.concate(spd_night, dire_night, dim='XTIME')
    
    return day, night





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


""" START Calculation of resulting windvector and winddirection """

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
ref_dd = winddir(ref_u10, ref_v10)
spr_dd = winddir(spr_u10, spr_v10)
opt_dd = winddir(opt_u10, opt_v10)

ref_dd = ref_dd.assign_attrs({'projection': ref_u10.projection,
                                    'description': 'Ref winddirection in 10m',
                                    'units': 'Degrees'})
spr_dd = spr_dd.assign_attrs({'projection': spr_u10.projection,
                                    'description': 'Spr winddirection in 10m',
                                    'units': 'Degrees'})
opt_dd = opt_dd.assign_attrs({'projection': opt_u10.projection,
                                    'description': 'Opt winddirection in 10m',
                                    'units': 'Degrees'})


""" END Calculation of resulting windvector and winddirection """

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

""" START areal and temporal selection + Wind selection day 07:00 - 18:00, night 19:00 - 06:00 """

ref_NO_day, ref_NO_night = area_day_night(ref_v, ref_dd, region['NO_sn'], region['NO_we'],   cuttime, 'ref_NO')
spr_NO_day, spr_NO_night = area_day_night(spr_v, spr_dd, region['NO_sn'], region['NO_we'],   cuttime, 'spr_NO')
opt_NO_day, opt_NO_night = area_day_night(opt_v, opt_dd, region['NO_sn'], region['NO_we'],   cuttime, 'opt_NO')
NO_day = pd.concat([ref_NO_day, spr_NO_day, opt_NO_day], axis=1)
NO_day.name = 'NO'
NO_night = pd.concat([ref_NO_night, spr_NO_night, opt_NO_night], axis=1)

ref_CE_day, ref_CE_night = area_day_night(ref_v, ref_dd, region['CE_sn'], region['CE_we'],   cuttime, 'ref_CE')
spr_CE_day, spr_CE_night = area_day_night(spr_v, spr_dd, region['CE_sn'], region['CE_we'],   cuttime, 'spr_CE')
opt_CE_day, opt_CE_night = area_day_night(opt_v, opt_dd, region['CE_sn'], region['CE_we'],   cuttime, 'opt_CE')
CE_day = pd.concat([ref_CE_day, spr_CE_day, opt_CE_day], axis=1)
CE_day.name = 'CE'
CE_night = pd.concat([ref_CE_night, spr_CE_night, opt_CE_night], axis=1)

ref_RU_day, ref_RU_night = area_day_night(ref_v, ref_dd, region['RU_sn'], region['RU_we'],   cuttime, 'ref_RU')
spr_RU_day, spr_RU_night = area_day_night(spr_v, spr_dd, region['RU_sn'], region['RU_we'],   cuttime, 'spr_RU')
opt_RU_day, opt_RU_night = area_day_night(opt_v, opt_dd, region['RU_sn'], region['RU_we'],   cuttime, 'opt_RU')
RU_day = pd.concat([ref_RU_day, spr_RU_day, opt_RU_day], axis=1)
RU_day.name = 'RU'
RU_night = pd.concat([ref_RU_night, spr_RU_night, opt_RU_night], axis=1)

ref_SA_day, ref_SA_night = area_day_night(ref_v, ref_dd, region['SA_sn'], region['SA_we'],   cuttime, 'ref_SA')
spr_SA_day, spr_SA_night = area_day_night(spr_v, spr_dd, region['SA_sn'], region['SA_we'],   cuttime, 'spr_SA')
opt_SA_day, opt_SA_night = area_day_night(opt_v, opt_dd, region['SA_sn'], region['SA_we'],   cuttime, 'opt_SA')
SA_day = pd.concat([ref_SA_day, spr_SA_day, opt_SA_day], axis=1)
SA_day.name = 'SA'
SA_night = pd.concat([ref_SA_night, spr_SA_night, opt_SA_night], axis=1)

ref_SE_day, ref_SE_night = area_day_night(ref_v, ref_dd, region['SE_sn'], region['SE_we'],   cuttime, 'ref_SE')
spr_SE_day, spr_SE_night = area_day_night(spr_v, spr_dd, region['SE_sn'], region['SE_we'],   cuttime, 'spr_SE')
opt_SE_day, opt_SE_night = area_day_night(opt_v, opt_dd, region['SE_sn'], region['SE_we'],   cuttime, 'opt_SE')
SE_day = pd.concat([ref_SE_day, spr_SE_day, opt_SE_day], axis=1)
SE_night = pd.concat([ref_SE_night, spr_SE_night, opt_SE_night], axis=1)
SE_day.name = 'SE'

ref_SX_day, ref_SX_night = area_day_night(ref_v, ref_dd, region['SX_sn'], region['SX_we'],   cuttime, 'ref_SX')
spr_SX_day, spr_SX_night = area_day_night(spr_v, spr_dd, region['SX_sn'], region['SX_we'],   cuttime, 'spr_SX')
opt_SX_day, opt_SX_night = area_day_night(opt_v, opt_dd, region['SX_sn'], region['SX_we'],   cuttime, 'opt_SX')
SX_day = pd.concat([ref_SX_day, spr_SX_day, opt_SX_day], axis=1)
SX_night = pd.concat([ref_SX_night, spr_SX_night, opt_SX_night], axis=1)
SX_day.name = 'SX'


ref_SI_day, ref_SI_night = area_day_night(ref_v, ref_dd, region['SI_sn'], region['SI_we'],   cuttime, 'ref_SI')
spr_SI_day, spr_SI_night = area_day_night(spr_v, spr_dd, region['SI_sn'], region['SI_we'],   cuttime, 'spr_SI')
opt_SI_day, opt_SI_night = area_day_night(opt_v, opt_dd, region['SI_sn'], region['SI_we'],   cuttime, 'opt_SI')
SI_day = pd.concat([ref_SI_day, spr_SI_day, opt_SI_day], axis=1)
SI_night = pd.concat([ref_SI_night, spr_SI_night, opt_SI_night], axis=1)
SI_day.name = 'SI'


ref_VW_day, ref_VW_night = area_day_night(ref_v, ref_dd, region['VW_sn'], region['VW_we'],   cuttime, 'ref_VW')
spr_VW_day, spr_VW_night = area_day_night(spr_v, spr_dd, region['VW_sn'], region['VW_we'],   cuttime, 'spr_VW')
opt_VW_day, opt_VW_night = area_day_night(opt_v, opt_dd, region['VW_sn'], region['VW_we'],   cuttime, 'opt_VW')
VW_day = pd.concat([ref_VW_day, spr_VW_day, opt_VW_day], axis=1)
VW_night = pd.concat([ref_VW_night, spr_VW_night, opt_VW_night], axis=1)
VW_day.name = 'VW'


ref_WE_day, ref_WE_night = area_day_night(ref_v, ref_dd, region['WE_sn'], region['WE_we'],   cuttime, 'ref_WE')
spr_WE_day, spr_WE_night = area_day_night(spr_v, spr_dd, region['WE_sn'], region['WE_we'],   cuttime, 'spr_WE')
opt_WE_day, opt_WE_night = area_day_night(opt_v, opt_dd, region['WE_sn'], region['WE_we'],   cuttime, 'opt_WE')
WE_day = pd.concat([ref_WE_day, spr_WE_day, opt_WE_day], axis=1)
WE_night = pd.concat([ref_WE_night, spr_WE_night, opt_WE_night], axis=1)
WE_day.name = 'WE'


""" END areal and temporal selection + Wind selection day 07:00 - 18:00, night 19:00 - 06:00 """


day = [NO_day, CE_day, RU_day, SA_day, SE_day, SX_day, SI_day, VW_day, WE_day]
night = [NO_night, CE_night, RU_night, SA_night, SE_night, SX_night, SI_night, VW_night, WE_night]



#%%
""" PLOTTING ROUTINE """

""" WINDROSE PLOTS """

title = '10m wind - day 07:00 - 18:00 / night 19:00 - 06:00'



for idx, var in enumerate(day):
    
    fig, ax = plt.subplots(figsize=(16,9))
#    fig.suptitle('windrose plot for region: ' + day[idx].name + '\nInit: ' + init, fontsize=16, ha='left')

    ax_day_ref = windrose_subplot(day[idx]['ref_speed'], day[idx]['ref_direction'], 231, 'REF - DAY' )
    
    ax_day_spr = windrose_subplot(day[idx]['spr_speed'], day[idx]['spr_direction'], 232, 'SPR - DAY' )
    
    ax_day_opt = windrose_subplot(day[idx]['opt_speed'], day[idx]['opt_direction'], 233, 'OPT - DAY' )
    
    ax_night_ref = windrose_subplot(night[idx]['ref_speed'], night[idx]['ref_direction'], 234, 'REF - NIGHT' )

    ax_night_spr = windrose_subplot(night[idx]['spr_speed'], night[idx]['spr_direction'], 235, 'SPR - NIGHT' )

    ax_night_opt = windrose_subplot(night[idx]['opt_speed'], night[idx]['opt_direction'], 236, 'OPT - NIGHT' )
   
    plt.subplots_adjust(hspace=0.3)
    
    ax1 = plt.gca()
    ax1.text(0.01,1.12,title, fontsize=16, transform=ax.transAxes)
    ax1.text(0.01,1.09, 'reference area: ' + day[idx].name, fontsize=12, transform=ax.transAxes)
    ax1.text(0.3,1.09,'init: ' + init, fontsize=12, transform=ax.transAxes)
        
    filename = domain + '_' + '_' + day[idx].name + '_windrose_bar'  +".png"
    plt.savefig(plot_dir + filename)
    plt.close()

#%%

""" SCATTER PLOTS FOR verifikation of windrose plots

for idx, var in enumerate(day):
    
    fig, ax = plt.subplots(figsize=(16,9))
#    fig.suptitle('windrose plot for region: ' + day[idx].name + '\nInit: ' + init, fontsize=16, ha='left')

    ax_day_ref = plt.subplot(231)
    ax_day_ref.set_title('REF - DAY \n')
    ax_day_ref.scatter(day[idx]['ref_direction'], day[idx]['ref_speed'])
    ax_day_ref.set_xticks([0,90,180,270,360])
    ax_day_ref.set_xticklabels(['N', 'E','S','W','N'])
    ax_day_ref.grid()
    
    ax_day_spr = plt.subplot(232)
    ax_day_spr.set_title('SPR - DAY \n')
    ax_day_spr.scatter(day[idx]['spr_direction'], day[idx]['spr_speed'])
    ax_day_spr.set_xticks([0,90,180,270,360])
    ax_day_spr.set_xticklabels(['N', 'E','S','W','N'])
    ax_day_spr.grid()

    ax_day_opt = plt.subplot(233)
    ax_day_opt.set_title('OPT - DAY \n')
    ax_day_opt.scatter(day[idx]['opt_direction'], day[idx]['opt_speed'])
    ax_day_opt.set_xticks([0,90,180,270,360])
    ax_day_opt.set_xticklabels(['N', 'E','S','W','N'])
    ax_day_opt.grid()
    
    ax_night_ref = plt.subplot(234)
    ax_night_ref.set_title('REF - NIGHT \n')
    ax_night_ref.scatter(night[idx]['ref_direction'], night[idx]['ref_speed'])
    ax_night_ref.set_xticks([0,90,180,270,360])
    ax_night_ref.set_xticklabels(['N', 'E','S','W','N'])
    ax_night_ref.grid()
    
    ax_night_spr = plt.subplot(235)
    ax_night_spr.set_title('SPR - NIGHT \n')
    ax_night_spr.scatter(night[idx]['spr_direction'], night[idx]['spr_speed'])
    ax_night_spr.set_xticks([0,90,180,270,360])
    ax_night_spr.set_xticklabels(['N', 'E','S','W','N'])
    ax_night_spr.grid()

    ax_night_opt = plt.subplot(236)
    ax_night_opt.set_title('OPT - NIGHT \n')
    ax_night_opt.scatter(night[idx]['opt_direction'], night[idx]['opt_speed'])
    ax_night_opt.set_xticks([0,90,180,270,360])
    ax_night_opt.set_xticklabels(['N', 'E','S','W','N'])
    ax_night_opt.grid()

    plt.subplots_adjust(hspace=0.3)
    
    ax1 = plt.gca()
#    ax1.text(0,1.04,run , fontsize=14, transform=ax.transAxes)
    ax1.text(0.01,1.12,title, fontsize=16, transform=ax.transAxes)
    ax1.text(0.01,1.09, 'reference area: ' + day[idx].name, fontsize=12, transform=ax.transAxes)
    ax1.text(0.3,1.09,'init: ' + init, fontsize=12, transform=ax.transAxes)
    
    #fig.autofmt_xdate()
    #fig.legend(fontsize='small', loc='upper right')
    
    filename = domain + '_' + '_' + day[idx].name + '_windrose_scatter'  +".png"
    plt.savefig(plot_dir + filename)
    plt.close()

"""