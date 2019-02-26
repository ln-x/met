# -*- coding: utf-8 -*-
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import numpy as np
import pandas as pd
import os
import wrf
from wrf import to_np, getvar, get_basemap, latlon_coords

"""
WICHTIG! Bilder mit Qt5 speichern da sonst Abstände etc nicht passen!

Erstellt einen AREA 3x3 subplot för OPT & SPR mit:
    + REF LU index
    + CASE LU index
    + DIFF LU index
    + REF median of MAX temp
    + CASE median of MAX temp
    + DIFF median of MAX temp
    + REF median of MIN temp
    + CASE median of MIN temp
    + DIFF median of MIN temp
    
DON'T FORGET TO CHANGE PLOT PREFERENCES FOR DIFFERENT RUNS IN PLOT ROUTINE !!!! 
"""


""" START Variable definition """

date_2015 = '2015-08-05' 
date_2069 = '2069-07-01' # Startdate of the WRF run / the time was in this ase always 18:00:00
domain = 'd03' # WRF domain
#run = 'REF_Run_2015' # reference run
#run1 = 'SPR_Run_2015' # sprawl run 
#run2 = 'OPT_Run_2015' # optimized city run
path = '/hp4/Urbania/WRF-2019-Runs/' # runPATH
#filepath = path + run + '/'
#filepath1 = path + run1 + '/'
#filepath2 = path + run2 + '/'
para = 'T2' # WRF Variable which shall be plotted
res = 'c' # resolution of basemap elements c = low, i = intermediate, h = high, f = full

""" not usable days - uncomment the run """
cuttime_2069 = pd.to_datetime(['2069-7-1','2069-7-2','2069-7-3','2069-7-4','2069-7-5', '2069-7-6','2069-7-9']) # 2069 run
cuttime_2015 = pd.to_datetime(['2015-08-05', '2015-08-06', '2015-08-07', '2015-08-08','2015-08-11', '2015-08-14']) # 2015 run


plotdir ='/hp4/Urbania/plots/'

if not os.path.exists(plotdir): # creates directory if not existing
    os.makedirs(plotdir)

levels = [-0.3, -0.15, -0.1, -0.05, -0.025, -0.01, 0.01, 0.025, 0.05, 0.1, 0.15, 0.5]
blrd = ["#002266", "#003399", "#0055ff","#6699ff", "#ccddff", "#ffffff", "#ffcccc","#ff9999","#ff6666","#ff3333","#cc0000","#b30000", "#990000", "#800000", "#660000"]
rdbl = ["#cc0000","#ff3333","#ff6666","#ff9999", "#ffcccc","#ffffff","#ccddff","#6699ff","#0055ff","#003399","#002266"]

 
""" END Variable definition """

""" START defining FUNCTIONS """

def area_collect_data_opt_spr(date, para, cuttime, path):
    
    import wrf
    import pandas as pd
    import xarray as xr
    import numpy as np
    from netCDF4 import Dataset
    from wrf import getvar

    
    filename = 'wrfout_d03_' + date + '_18_00_00.nc'
    
    ref = 'REF_Run_' + str(pd.to_datetime(date).year) # reference run
    spr = 'SPR_Run_' + str(pd.to_datetime(date).year) # sprawl run 
    opt = 'OPT_Run_' + str(pd.to_datetime(date).year) # optimized city run

    ref_filepath = path + ref + '/'
    spr_filepath = path + spr + '/'
    opt_filepath = path + opt + '/'

    ref_ncfile = Dataset(ref_filepath + filename)
    spr_ncfile = Dataset(spr_filepath + filename)
    opt_ncfile = Dataset(opt_filepath + filename)
    
    times = getvar(ref_ncfile, "Times", timeidx=wrf.ALL_TIMES, meta=False) # FC times in np.datetime64 format - very ugly
    init = pd.to_datetime(times[0]) # converts the numpy datetime to datetime datetime format
    init = str(init) # initial time of wrf dataset

    
    ref = getvar(ref_ncfile, para, timeidx=wrf.ALL_TIMES)
    spr = getvar(spr_ncfile, para, timeidx=wrf.ALL_TIMES)
    opt = getvar(opt_ncfile, para, timeidx=wrf.ALL_TIMES)

    """ START ELIMINATING unsuseable days like spinup & cloudy days """

    for i in cuttime:
        spr = spr.where(spr['Time'].dt.day != i.day, drop=True).rename('SPR')
        ref = ref.where(ref['Time'].dt.day != i.day, drop=True).rename('REF')
        opt = opt.where(opt['Time'].dt.day != i.day, drop=True).rename('OPT')
    
    """ END ELIMINATING unsuseable days like spinup & cloudy days """
    
    
    """ START Calculation of areal median of MIN & MAX for REF SPR OPT """
    
    ref_daily_max = ref.groupby(ref.Time.dt.day).max(axis=0)
    ref_daily_min = ref.groupby(ref.Time.dt.day).min(axis=0)
    
    ref_med_max = ref_daily_max.median(axis=0) - 273.15
    ref_med_min = ref_daily_min.median(axis=0) -273.15
    
    ref_med_max = ref_med_max.assign_attrs({'projection': ref.projection,
                                            'description': 'REF Median of MAX '+ref.description,
                                            'units': 'degree Celsius'})
    ref_med_min = ref_med_min.assign_attrs({'projection': ref.projection,
                                            'description': 'REF Median of MIN '+ref.description,
                                            'units': 'degree Celsius'})
    
        
        
    opt_daily_max = opt.groupby(opt.Time.dt.day).max(axis=0)
    opt_daily_min = opt.groupby(opt.Time.dt.day).min(axis=0)
    
    opt_med_max = opt_daily_max.median(axis=0) - 273.15
    opt_med_min = opt_daily_min.median(axis=0) - 273.15
    
    opt_med_max = opt_med_max.assign_attrs({'projection': ref.projection,
                                            'description': 'OPT Median of MAX '+ref.description,
                                            'units': 'degree Celsius'})
    opt_med_min = opt_med_min.assign_attrs({'projection': ref.projection,
                                            'description': 'OPT Median of MIN '+ref.description,
                                            'units': 'degree Celsius'})
    
        
        
    spr_daily_max = spr.groupby(spr.Time.dt.day).max(axis=0)
    spr_daily_min = spr.groupby(spr.Time.dt.day).min(axis=0)
    
    spr_med_max = spr_daily_max.median(axis=0) - 273.15
    spr_med_min = spr_daily_min.median(axis=0) - 273.15
    
    spr_med_max = spr_med_max.assign_attrs({'projection': ref.projection,
                                            'description': 'SPR Median of MAX '+ref.description,
                                            'units': 'degree Celsius'})
    spr_med_min = spr_med_min.assign_attrs({'projection': ref.projection,
                                            'description': 'SPR Median of MIN '+ref.description,
                                            'units': 'degree Celsius'})
    
    """ END Calculation of areal median of MIN & MAX """
    
        
    """ START Calculation of Differences between REF SPR OPT """   
    
    spr_max_diff = spr_med_max - ref_med_max
    spr_min_diff = spr_med_min - ref_med_min
    
    opt_max_diff = opt_med_max - ref_med_max
    opt_min_diff = opt_med_min - ref_med_min
    
    opt_spr_min_diff = opt_med_min - spr_med_min
    opt_spr_max_diff = opt_med_max - spr_med_max
    
    
    
    
    spr_max_diff = spr_max_diff.assign_attrs({'projection': ref.projection,
                                            'description': 'Difference SPR - REF of Median of MAX '+ref.description,
                                            'units': 'degree Celsius'})
    spr_min_diff = spr_min_diff.assign_attrs({'projection': ref.projection,
                                            'description': 'Difference SPR - REF Median of MIN '+ref.description,
                                            'units': ref.units})
    
    opt_max_diff = opt_max_diff.assign_attrs({'projection': ref.projection,
                                            'description': 'Difference OPT - REF of Median of MAX '+ref.description,
                                            'units': 'degree Celsius'})
    opt_min_diff = opt_min_diff.assign_attrs({'projection': ref.projection,
                                            'description': 'Difference OPT - REF Median of MIN '+ref.description,
                                            'units': 'degree Celsius'})
    
    opt_spr_min_diff = opt_spr_min_diff.assign_attrs({'projection': ref.projection,
                                            'description': str(pd.to_datetime(date).year) + ' Difference OPT - SPR Median of MIN '+ref.description,
                                            'units': 'degree Celsius'})
    opt_spr_max_diff = opt_spr_max_diff.assign_attrs({'projection': ref.projection,
                                            'description': str(pd.to_datetime(date).year) + ' Difference OPT - SPR Median of MAX '+ref.description,
                                            'units': 'degree Celsius'})
    
    """ END Calculation of Differences between REF SPR OPT """
    
    
    """ START getting LU_INDEX/HGT and create DIFFS """
    
    hgt = getvar(ref_ncfile, 'HGT')
    ref_lu = getvar(ref_ncfile, 'LU_INDEX').rename('REF Landuse Category\'s')
    spr_lu = getvar(spr_ncfile, 'LU_INDEX').rename('SPR Landuse Category\'s')
    opt_lu = getvar(opt_ncfile, 'LU_INDEX').rename('OPT Landuse Category\'s')
    
    spr_lu_diff = spr_lu.where(ref_lu.data != spr_lu.data)
    opt_lu_diff = opt_lu.where(ref_lu.data != opt_lu.data)
    opt_spr_lu_diff = spr_lu.where(spr_lu.data != opt_lu.data)
    
    """ END getting LU_INDEX and create DIFFS """

    return opt_spr_min_diff, opt_spr_max_diff, opt_spr_lu_diff, hgt


#def lu_subplot(var, pos, res, title, hgt, par=True, mer=True):
#    ax = plt.subplot(pos)
#    ax.set_title(title, fontsize=10)
#    # Get the basemap object
#    bm = get_basemap(var, projection='lcc', resolution=res, ax=ax)
#    # Convert the lats and lons to x and y.  Make sure you convert the lats and lons to
#    # numpy arrays via to_np, or basemap crashes with an undefined RuntimeError.
#    x, y = bm(to_np(lons), to_np(lats))
#    # Define gridlines
#    parallels = np.arange(-90,90,0.2)
#    meridians = np.arange(0,360,0.2)
#    # Add geographic outlines
#    if par == True:
#        bm.drawparallels(parallels,labels=[1,0,0,0],fontsize=8)
#    else:
#        bm.drawparallels(parallels,fontsize=8)
#    if mer == True:
#        bm.drawmeridians(meridians,labels=[0,0,0,1],fontsize=8)
#    else:
#        bm.drawmeridians(meridians,fontsize=8)
#    bm.drawrivers(linewidth=0.75,color='blue') #only for high resolution plots
#    bm.readshapefile('/home/kristofh/projects/shp_files/BEZIRKSGRENZEOGDPolygon', 'BEZIRKSGRENZEOGDPolygon', linewidth=0.6)
#    
#    
#    heights = np.arange(100, 800, 50)
#    categ = np.arange(1,34, 1)
#    
#    # Draw the contours and filled contours
#    hgt_cont = bm.contour(x,y,to_np(hgt), levels=heights, colors="magenta", linewidths=0.4, alpha=1)
#    var_contf = bm.pcolormesh(x,y,to_np(var), cmap=get_cmap("viridis"), alpha=0.9)
#    cb_var = fig.colorbar(var_contf, ticks=categ[::3], ax=ax, shrink=0.7)
#    cb_var.ax.tick_params(labelsize=8)
#    return


def area_collect_data(date, para, cuttime, path):
    
    import wrf
    import pandas as pd
    import xarray as xr
    import numpy as np
    from netCDF4 import Dataset
    from wrf import getvar

    
    filename = 'wrfout_d03_' + date + '_18_00_00.nc'
    
    ref = 'REF_Run_' + str(pd.to_datetime(date).year) # reference run
    spr = 'SPR_Run_' + str(pd.to_datetime(date).year) # sprawl run 
    opt = 'OPT_Run_' + str(pd.to_datetime(date).year) # optimized city run

    ref_filepath = path + ref + '/'
    spr_filepath = path + spr + '/'
    opt_filepath = path + opt + '/'

    ref_ncfile = Dataset(ref_filepath + filename)
    spr_ncfile = Dataset(spr_filepath + filename)
    opt_ncfile = Dataset(opt_filepath + filename)
    
    times = getvar(ref_ncfile, "Times", timeidx=wrf.ALL_TIMES, meta=False) # FC times in np.datetime64 format - very ugly
    init = pd.to_datetime(times[0]) # converts the numpy datetime to datetime datetime format
    init = str(init) # initial time of wrf dataset

    
    ref = getvar(ref_ncfile, para, timeidx=wrf.ALL_TIMES)
    spr = getvar(spr_ncfile, para, timeidx=wrf.ALL_TIMES)
    opt = getvar(opt_ncfile, para, timeidx=wrf.ALL_TIMES)

    """ START ELIMINATING unsuseable days like spinup & cloudy days """

    for i in cuttime:
        spr = spr.where(spr['Time'].dt.day != i.day, drop=True).rename('SPR')
        ref = ref.where(ref['Time'].dt.day != i.day, drop=True).rename('REF')
        opt = opt.where(opt['Time'].dt.day != i.day, drop=True).rename('OPT')
    
    """ END ELIMINATING unsuseable days like spinup & cloudy days """
    
    
    """ START Calculation of areal median of MIN & MAX for REF SPR OPT """
    
    ref_daily_max = ref.groupby(ref.Time.dt.day).max(axis=0)
    ref_daily_min = ref.groupby(ref.Time.dt.day).min(axis=0)
    
    ref_med_max = ref_daily_max.median(axis=0) - 273.15
    ref_med_min = ref_daily_min.median(axis=0) -273.15
    
    ref_med_max = ref_med_max.assign_attrs({'projection': ref.projection,
                                            'description': 'REF Median of MAX '+ref.description,
                                            'units': 'degree Celsius'})
    ref_med_min = ref_med_min.assign_attrs({'projection': ref.projection,
                                            'description': 'REF Median of MIN '+ref.description,
                                            'units': 'degree Celsius'})
    
        
        
    opt_daily_max = opt.groupby(opt.Time.dt.day).max(axis=0)
    opt_daily_min = opt.groupby(opt.Time.dt.day).min(axis=0)
    
    opt_med_max = opt_daily_max.median(axis=0) - 273.15
    opt_med_min = opt_daily_min.median(axis=0) - 273.15
    
    opt_med_max = opt_med_max.assign_attrs({'projection': ref.projection,
                                            'description': 'OPT Median of MAX '+ref.description,
                                            'units': 'degree Celsius'})
    opt_med_min = opt_med_min.assign_attrs({'projection': ref.projection,
                                            'description': 'OPT Median of MIN '+ref.description,
                                            'units': 'degree Celsius'})
    
        
        
    spr_daily_max = spr.groupby(spr.Time.dt.day).max(axis=0)
    spr_daily_min = spr.groupby(spr.Time.dt.day).min(axis=0)
    
    spr_med_max = spr_daily_max.median(axis=0) - 273.15
    spr_med_min = spr_daily_min.median(axis=0) - 273.15
    
    spr_med_max = spr_med_max.assign_attrs({'projection': ref.projection,
                                            'description': 'SPR Median of MAX '+ref.description,
                                            'units': 'degree Celsius'})
    spr_med_min = spr_med_min.assign_attrs({'projection': ref.projection,
                                            'description': 'SPR Median of MIN '+ref.description,
                                            'units': 'degree Celsius'})
    
    """ END Calculation of areal median of MIN & MAX """
    
        
    """ START Calculation of Differences between REF SPR OPT """   
    
    spr_max_diff = spr_med_max - ref_med_max
    spr_min_diff = spr_med_min - ref_med_min
    
    opt_max_diff = opt_med_max - ref_med_max
    opt_min_diff = opt_med_min - ref_med_min
    
    opt_spr_min_diff = opt_med_min - spr_med_min
    opt_spr_max_diff = opt_med_max - spr_med_max
    
    
    
    
    spr_max_diff = spr_max_diff.assign_attrs({'projection': ref.projection,
                                            'description': 'Difference SPR - REF of Median of MAX '+ref.description,
                                            'units': 'degree Celsius'})
    spr_min_diff = spr_min_diff.assign_attrs({'projection': ref.projection,
                                            'description': 'Difference SPR - REF Median of MIN '+ref.description,
                                            'units': ref.units})
    
    opt_max_diff = opt_max_diff.assign_attrs({'projection': ref.projection,
                                            'description': 'Difference OPT - REF of Median of MAX '+ref.description,
                                            'units': 'degree Celsius'})
    opt_min_diff = opt_min_diff.assign_attrs({'projection': ref.projection,
                                            'description': 'Difference OPT - REF Median of MIN '+ref.description,
                                            'units': 'degree Celsius'})
    
    opt_spr_min_diff = opt_spr_min_diff.assign_attrs({'projection': ref.projection,
                                            'description': str(pd.to_datetime(date).year) + ' Difference OPT - SPR Median of MIN '+ref.description,
                                            'units': 'degree Celsius'})
    opt_spr_max_diff = opt_spr_max_diff.assign_attrs({'projection': ref.projection,
                                            'description': str(pd.to_datetime(date).year) + ' Difference OPT - SPR Median of MAX '+ref.description,
                                            'units': 'degree Celsius'})
    
    """ END Calculation of Differences between REF SPR OPT """
    
    ref_d = {ref_med_max.description[:3] + '_' + ref_med_max.description[14:17]: ref_med_max,
              ref_med_min.description[:3] + '_' + ref_med_min.description[14:17]: ref_med_min,
              }
    spr_d = {spr_med_max.description[:3] + '_' + spr_med_max.description[14:17]: spr_med_max,
          spr_med_min.description[:3] + '_' + spr_med_min.description[14:17]: spr_med_min,
          }
    opt_d = {opt_med_max.description[:3] + '_' + opt_med_max.description[14:17]: opt_med_max,
          opt_med_min.description[:3] + '_' + opt_med_min.description[14:17]: opt_med_min,
          }
    

    
    """ START getting LU_INDEX/HGT and create DIFFS """
    
    hgt = getvar(ref_ncfile, 'HGT')
    ref_lu = getvar(ref_ncfile, 'LU_INDEX').rename('REF Landuse Category\'s')
    spr_lu = getvar(spr_ncfile, 'LU_INDEX').rename('SPR Landuse Category\'s')
    opt_lu = getvar(opt_ncfile, 'LU_INDEX').rename('OPT Landuse Category\'s')
    
    spr_lu_diff = spr_lu.where(ref_lu.data != spr_lu.data)
    opt_lu_diff = opt_lu.where(ref_lu.data != opt_lu.data)
    opt_spr_lu_diff = spr_lu.where(spr_lu.data != opt_lu.data)
    
    """ END getting LU_INDEX and create DIFFS """

    return ref_d, spr_d, opt_d, hgt


def lu_subplot(var, pos, res, title, hgt, par=True, mer=True):
    ax = plt.subplot(pos)
    ax.set_title(title, fontsize=10)
    # Get the basemap object
    bm = get_basemap(var, projection='lcc', resolution=res, ax=ax)
    # Convert the lats and lons to x and y.  Make sure you convert the lats and lons to
    # numpy arrays via to_np, or basemap crashes with an undefined RuntimeError.
    x, y = bm(to_np(lons), to_np(lats))
    # Define gridlines
    parallels = np.arange(-90,90,0.2)
    meridians = np.arange(0,360,0.2)
    # Add geographic outlines
    if par == True:
        bm.drawparallels(parallels,labels=[1,0,0,0],fontsize=8)
    else:
        bm.drawparallels(parallels,fontsize=8)
    if mer == True:
        bm.drawmeridians(meridians,labels=[0,0,0,1],fontsize=8)
    else:
        bm.drawmeridians(meridians,fontsize=8)
    bm.drawrivers(linewidth=0.75,color='blue') #only for high resolution plots
    bm.readshapefile('/home/kristofh/projects/shp_files/BEZIRKSGRENZEOGDPolygon', 'BEZIRKSGRENZEOGDPolygon', linewidth=0.6)
    
    
    heights = np.arange(100, 800, 50)
    categ = np.arange(1,34, 1)
    
    # Draw the contours and filled contours
    hgt_cont = bm.contour(x,y,to_np(hgt), levels=heights, colors="magenta", linewidths=0.4, alpha=1)
    var_contf = bm.pcolormesh(x,y,to_np(var), cmap=get_cmap("viridis"), alpha=0.9)
    cb_var = fig.colorbar(var_contf, ticks=categ[::3], ax=ax, shrink=0.7)
    cb_var.ax.tick_params(labelsize=8)
    return


def var_subplot(var, pos, res, title,  steps, tmin, trange,  cmap=blrd, levels=levels, par=True, mer=True):
    ax = plt.subplot(pos)
    ax.set_title(title, fontsize=10)
    # Get the basemap object
    bm = get_basemap(var, projection='lcc', resolution=res, ax=ax)
    # Convert the lats and lons to x and y.  Make sure you convert the lats and lons to
    # numpy arrays via to_np, or basemap crashes with an undefined RuntimeError.
    x, y = bm(to_np(lons), to_np(lats))
    # Define gridlines
    parallels = np.arange(-90,90,0.2)
    meridians = np.arange(0,360,0.2)
    # Add geographic outlines
    if par == True:
        bm.drawparallels(parallels,labels=[1,0,0,0],fontsize=8)
    else:
        bm.drawparallels(parallels,fontsize=8)
    if mer == True:
        bm.drawmeridians(meridians,labels=[0,0,0,1],fontsize=8)
    else:
        bm.drawmeridians(meridians,fontsize=8)
#    bm.drawrivers(linewidth=0.75,color='blue') #only for high resolution plots
    bm.readshapefile('/home/kristofh/projects/shp_files/BEZIRKSGRENZEOGDPolygon', 'BEZIRKSGRENZEOGDPolygon', linewidth=0.6)
    
#    levels=np.arange(tmin, tmin + trange, steps)
#    levels=np.insert(levels,0, np.arange((maxdiff_spr.min()*10).round()/10,-1,steps*6))
#    levels=np.append(levels, np.arange(1,(maxdiff_spr.max()*10).round()/10,steps*6))
#    
#    contour_levels=np.arange(-1.0, 1.0+steps, steps*2)
#    contour_levels=np.insert(contour_levels,0, (var.min()*10).round()/10)
#    contour_levels=np.append(contour_levels, (var.max()*10).round()/10)
    
#    heights = np.arange(100, 800, 50)

    # Draw the contours and filled contours
#    hgt_cont = bm.contour(x,y,to_np(hgt), levels=heights, colors="magenta", linewidths=0.4, alpha=1)
    var_cont = bm.contour(x,y,to_np(var), levels=levels, colors="black", linewidths=0.4, alpha=0.5)
    var_contf = bm.contourf(x,y,to_np(var), levels=levels, colors=cmap, extend='both', alpha=0.9)
    cb_var = fig.colorbar(var_contf, ax=ax, ticks=levels, shrink=0.4)
    cb_var.ax.tick_params(labelsize=8)
    cbar_var.ax.set_yticklabels(levels)
    return

def var_diff_subplot(var, pos, res, title, tmin, trange,  cmap=blrd, levels=levels, steps=0.25, par=True, mer=True):
    ax = plt.subplot(pos)
    ax.set_title(title, fontsize=16)
    # Get the basemap object
    bm = get_basemap(var, projection='lcc', resolution=res, ax=ax)
    # Convert the lats and lons to x and y.  Make sure you convert the lats and lons to
    # numpy arrays via to_np, or basemap crashes with an undefined RuntimeError.
    x, y = bm(to_np(lons), to_np(lats))
    # Define gridlines
    parallels = np.arange(-90,90,0.2)
    meridians = np.arange(0,360,0.2)
    # Add geographic outlines
    if par == True:
        bm.drawparallels(parallels,labels=[1,0,0,0],fontsize=12)
    else:
        bm.drawparallels(parallels,fontsize=12)
    if mer == True:
        bm.drawmeridians(meridians,labels=[0,0,0,1],fontsize=12)
    else:
        bm.drawmeridians(meridians,fontsize=12)
#    bm.drawrivers(linewidth=0.75,color='blue') #only for high resolution plots
    bm.readshapefile('/home/kristofh/projects/shp_files/BEZIRKSGRENZEOGDPolygon', 'BEZIRKSGRENZEOGDPolygon', linewidth=0.6)
    
#    levels=np.arange(tmin, tmin+trange+steps, steps)
#    heights = np.arange(100, 800, 50)

    # Draw the contours and filled contours
#    hgt_cont = bm.contour(x,y,to_np(hgt), levels=heights, colors="magenta", linewidths=0.4, alpha=1)
    var_cont = bm.contour(x,y,to_np(var), colors="black", levels=levels, linewidths=0.4, alpha=0.5)
    var_contf = bm.contourf(x,y,to_np(var), levels=levels, colors=cmap, extend='both', alpha=0.9)
    cb_var = fig.colorbar(var_contf, ax=ax, ticks=levels, shrink=1.)
    cb_var.ax.tick_params(labelsize=8)
    return

#%%


min_diff_2015, max_diff_2015, lu_diff_2015, hgt = area_collect_data_opt_spr(date_2015, para, cuttime_2015, path)

ref_2015, spr_2015, opt_2015, hgt = area_collect_data(date_2015, para, cuttime_2015, path)


min_diff_2069, max_diff_2069, lu_diff_2069, hgt = area_collect_data_opt_spr(date_2069, para, cuttime_2069, path)
ref_2069, spr_2069, opt_2069, hgt = area_collect_data(date_2069, para, cuttime_2069, path)

ref_min_diff = (ref_2069['REF_MIN'] - ref_2015['REF_MIN']).assign_attrs({'projection': min_diff_2015.projection})
spr_min_diff = (spr_2069['SPR_MIN'] - spr_2015['SPR_MIN']).assign_attrs({'projection': min_diff_2015.projection})
opt_min_diff = (opt_2069['OPT_MIN'] - opt_2015['OPT_MIN']).assign_attrs({'projection': min_diff_2015.projection})

ref_max_diff = (ref_2069['REF_MAX'] - ref_2015['REF_MAX']).assign_attrs({'projection': min_diff_2015.projection})
spr_max_diff = (spr_2069['SPR_MAX'] - spr_2015['SPR_MAX']).assign_attrs({'projection': min_diff_2015.projection})
opt_max_diff = (opt_2069['OPT_MAX'] - opt_2015['OPT_MAX']).assign_attrs({'projection': min_diff_2015.projection})

sens_spr_min_diff = (spr_2069['SPR_MIN'] - ref_2015['REF_MIN']).assign_attrs({'projection': min_diff_2015.projection})
sens_opt_min_diff = (opt_2069['OPT_MIN'] - ref_2015['REF_MIN']).assign_attrs({'projection': min_diff_2015.projection})

sens_opt_spr_min_diff = sens_opt_min_diff - sens_spr_min_diff

min_diff =  min_diff_2069 - min_diff_2015
max_diff =  max_diff_2069 - max_diff_2015
lu_diff =  lu_diff_2015 - lu_diff_2069

min_diff = min_diff.assign_attrs({'projection': min_diff_2015.projection,
                                        'description': 'Difference OPT - SPR of Median of MIN '+min_diff_2015.description,
                                        'units': 'degree Celsius'})
max_diff = max_diff.assign_attrs({'projection': max_diff_2015.projection,
                                        'description': 'Difference OPT - SPR of Median of MAX '+max_diff_2015.description,
                                        'units': 'degree Celsius'})
lu_diff = lu_diff.assign_attrs({'projection': lu_diff_2015.projection,
                                        'description': 'Difference OPT - SPR of Landuse '+lu_diff_2015.description,
                                        'units': 'Category'})

##%%
#
#
#
#""" END defining FUNCTIONS """
#
#
#ncfile = Dataset(filepath + filenam)
#ncfile1 = Dataset(filepath1 + filenam)
#ncfile2 = Dataset(filepath2 + filenam)
#
##Dimension of domain
#data = getvar(ncfile, para, timeidx=wrf.ALL_TIMES)
#data_max = (data.max()/10).round()*10
#data_min = (data.min()/10).round()*10
#data1 = getvar(ncfile1, para, timeidx=wrf.ALL_TIMES)
#data2 = getvar(ncfile2, para, timeidx=wrf.ALL_TIMES)
#
#data.close()
#data1.close()
#data2.close()
#
#times = getvar(ncfile, "Times", timeidx=wrf.ALL_TIMES, meta=False) # FC times in np.datetime64 format - very ugly
#init = pd.to_datetime(times[0]) # converts the numpy datetime to datetime datetime format
#init = str(init) # initial time of wrf dataset
#
#ref = data     # data is a safetyvariable for attributes
#spr = data1
#opt = data2
#
#
##%%
#""" START ELIMINATING unsuseable days like spinup & cloudy days """
#
#for i in cuttime:
#    spr = spr.where(spr['Time'].dt.day != i.day, drop=True).rename('SPR')
#    ref = ref.where(ref['Time'].dt.day != i.day, drop=True).rename('REF')
#    opt = opt.where(opt['Time'].dt.day != i.day, drop=True).rename('OPT')
#
#""" END ELIMINATING unsuseable days like spinup & cloudy days """
#
#
#""" START Calculation of areal median of MIN & MAX for REF SPR OPT """
#
#ref_daily_max = ref.groupby(ref.Time.dt.day).max(axis=0)
#ref_daily_min = ref.groupby(ref.Time.dt.day).min(axis=0)
#
#ref_med_max = ref_daily_max.median(axis=0) - 273.15
#ref_med_min = ref_daily_min.median(axis=0) -273.15
#
#ref_med_max = ref_med_max.assign_attrs({'projection': data.projection,
#                                        'description': 'REF Median of MAX '+data.description,
#                                        'units': 'degree Celsius'})
#ref_med_min = ref_med_min.assign_attrs({'projection': data.projection,
#                                        'description': 'REF Median of MIN '+data.description,
#                                        'units': 'degree Celsius'})
#
#    
#    
#opt_daily_max = opt.groupby(opt.Time.dt.day).max(axis=0)
#opt_daily_min = opt.groupby(opt.Time.dt.day).min(axis=0)
#
#opt_med_max = opt_daily_max.median(axis=0) - 273.15
#opt_med_min = opt_daily_min.median(axis=0) - 273.15
#
#opt_med_max = opt_med_max.assign_attrs({'projection': data.projection,
#                                        'description': 'OPT Median of MAX '+data.description,
#                                        'units': 'degree Celsius'})
#opt_med_min = opt_med_min.assign_attrs({'projection': data.projection,
#                                        'description': 'OPT Median of MIN '+data.description,
#                                        'units': 'degree Celsius'})
#
#    
#    
#spr_daily_max = spr.groupby(spr.Time.dt.day).max(axis=0)
#spr_daily_min = spr.groupby(spr.Time.dt.day).min(axis=0)
#
#spr_med_max = spr_daily_max.median(axis=0) - 273.15
#spr_med_min = spr_daily_min.median(axis=0) - 273.15
#
#spr_med_max = spr_med_max.assign_attrs({'projection': data.projection,
#                                        'description': 'SPR Median of MAX '+data.description,
#                                        'units': 'degree Celsius'})
#spr_med_min = spr_med_min.assign_attrs({'projection': data.projection,
#                                        'description': 'SPR Median of MIN '+data.description,
#                                        'units': 'degree Celsius'})
#
#""" END Calculation of areal median of MIN & MAX """
#
#    
#""" START Calculation of Differences between REF SPR OPT """   
#
#spr_max_diff = spr_med_max - ref_med_max
#spr_min_diff = spr_med_min - ref_med_min
#
#opt_max_diff = opt_med_max - ref_med_max
#opt_min_diff = opt_med_min - ref_med_min
#
#opt_spr_min_diff = opt_med_min - spr_med_min
#opt_spr_max_diff = opt_med_max - spr_med_max
#
#
#
#
#spr_max_diff = spr_max_diff.assign_attrs({'projection': data.projection,
#                                        'description': 'Difference SPR - REF of Median of MAX '+data.description,
#                                        'units': 'degree Celsius'})
#spr_min_diff = spr_min_diff.assign_attrs({'projection': data.projection,
#                                        'description': 'Difference SPR - REF Median of MIN '+data.description,
#                                        'units': data.units})
#
#opt_max_diff = opt_max_diff.assign_attrs({'projection': data.projection,
#                                        'description': 'Difference OPT - REF of Median of MAX '+data.description,
#                                        'units': 'degree Celsius'})
#opt_min_diff = opt_min_diff.assign_attrs({'projection': data.projection,
#                                        'description': 'Difference OPT - REF Median of MIN '+data.description,
#                                        'units': 'degree Celsius'})
#
#opt_spr_min_diff = opt_spr_min_diff.assign_attrs({'projection': data.projection,
#                                        'description': 'Difference OPT - SPR Median of MIN '+data.description,
#                                        'units': 'degree Celsius'})
#opt_spr_max_diff = opt_spr_max_diff.assign_attrs({'projection': data.projection,
#                                        'description': 'Difference OPT - SPR Median of MAX '+data.description,
#                                        'units': 'degree Celsius'})
#
#""" END Calculation of Differences between REF SPR OPT """
#
#
#""" START getting LU_INDEX/HGT and create DIFFS """
#
#hgt = getvar(ncfile, 'HGT')
#ref_lu = getvar(ncfile, 'LU_INDEX').rename('REF Landuse Category\'s')
#spr_lu = getvar(ncfile1, 'LU_INDEX').rename('SPR Landuse Category\'s')
#opt_lu = getvar(ncfile2, 'LU_INDEX').rename('OPT Landuse Category\'s')
#
#spr_lu_diff = spr_lu.where(ref_lu.data != spr_lu.data)
#opt_lu_diff = opt_lu.where(ref_lu.data != opt_lu.data)
#opt_spr_lu_diff = spr_lu.where(spr_lu.data != opt_lu.data)
#
#""" END getting LU_INDEX and create DIFFS """


#%%
""" START Plotting routine for SPR """

""" preferences for 2069 run """
#maxrange = 12.
#minrange = 10.
#maxmintemp = 33.
#minmintemp = 20.
#steps= 1.

""" preferences for 2015 run """
tminmax = -1
trangemax = 7
steps= 0.25
levels = [ -1.5, -1, 1., 5., 6., 6.5, 7., 7.5, 8.]
blrd = [  "#ccddff", "#ffffff", "#ffcccc","#ff9999","#ff6666","#ff3333","#cc0000","#b30000", "#990000", "#800000", "#660000"]
rdbl = ["#cc0000","#ff3333","#ff6666","#ff9999", "#ffcccc","#ffffff","#ccddff","#6699ff","#0055ff","#003399","#002266"]


# Create a figure for MAX PLOTS
fig, ax = plt.subplots(figsize=(16,12))

# Get the latitude and longitude points
lats, lons = latlon_coords(min_diff_2015)

#fig.suptitle('difference 2069 - 2015 of OPT - SPR' )

""" REF LU_INDEX Plot """
ref_max_plt = var_diff_subplot(ref_max_diff, 111, res, 'Difference 2069 - 2015 REF MAX', tminmax, trangemax, levels=levels, cmap=blrd, steps=steps, par=True, mer=True)

#""" SPR LU_INDEX Plot """
#ref_min_plt = var_diff_subplot(min_diff, 122, res, 'MIN OPT - SPR', tminmax, trangemax, steps=steps, par=False, mer=True)


#""" DIFF LU_INDEX Plot """
#spr_lu_diff_plt = lu_subplot(lu_diff, 133, res, 'LU Diff', hgt, par=False, mer=True)


#""" REF MAX Plot """
#ref_max_plt = var_subplot(ref_med_max, 334, res, ref_med_max.description, steps, maxmintemp, maxrange, par=True, mer=False)
#
#""" SPR MAX Plot """
#spr_max_plt = var_subplot(spr_med_max, 335, res, spr_med_max.description, steps, maxmintemp, maxrange, par=False, mer=False)
#
#""" DIFF CASE - REF MAX plot """
#spr_maxdiff_plt = var_diff_subplot(spr_max_diff, 336, res, spr_max_diff.description, par=False, mer=False)
#
#
#""" REF MIN Plot """
#ref_min_plt = var_subplot(ref_med_min, 337, res, ref_med_min.description, steps, minmintemp, minrange, par=True, mer=True)
#
#""" SPR MIN Plot """
#spr_min_plt = var_subplot(spr_med_min, 338, res, spr_med_min.description, steps, minmintemp, minrange, par=False, mer=True)
#
#""" DIFF CASE - REF MIN plot """
#spr_mindiff_plt = var_diff_subplot(spr_min_diff, 339, res, spr_min_diff.description, par=False, mer=True)
#

#plt.tight_layout()
plt.subplots_adjust(left=0.035, right=1)
#                    bottom=0.017,
#                    left=0.012,
#                    right=0.991,
#                    hspace=0.2,
#                    wspace=0.044
#                    )

filename = domain + '_2069-2015_REF_MAX_SENS.png'
plt.savefig(plotdir + filename)

""" END Plotting routine for SPR """

fig, ax = plt.subplots(figsize=(16,12))
lats, lons = latlon_coords(min_diff_2015)

tminmax = -1
trangemax = 7
steps= 0.25
levels = [ -1., -0.5, 0.5, 1.5, 2.5, 3., 3.5, 4., 4.5, 5., 5.5]
blrd = [ "#ccddff", "#ffffff", "#ffcccc","#ff9999","#ff6666","#ff3333","#cc0000","#b30000", "#990000", "#800000", "#660000"]
rdbl = ["#cc0000","#ff3333","#ff6666","#ff9999", "#ffcccc","#ffffff","#ccddff","#6699ff","#0055ff","#003399","#002266"]
#blrd = ["#002266", "#003399", "#0055ff","#6699ff", "#ccddff", "#ffffff", "#ffcccc","#ff9999","#ff6666","#ff3333","#cc0000","#b30000", "#990000", "#800000", $

ref_min_plt = var_diff_subplot(sens_spr_min_diff, 111, res, 'Difference 2069 SPR - 2015 REF MIN', tminmax, trangemax, levels=levels, cmap=blrd, steps=steps, par=True, mer=True)

plt.subplots_adjust(left=0.035, right=1)

filename = domain + '_2069SPR-2015REF_MIN_SENS.png'
plt.savefig(plotdir + filename)


#%%
fig, ax = plt.subplots(figsize=(16,12))
lats, lons = latlon_coords(min_diff_2015)

tminmax = -1
trangemax = 7
steps= 0.25
levels = [ -1., -0.5, 0.5, 1.5, 2.5, 3., 3.5, 4., 4.5, 5., 5.5]
blrd = [ "#ccddff", "#ffffff", "#ffcccc","#ff9999","#ff6666","#ff3333","#cc0000","#b30000", "#990000", "#800000", "#660000"]
rdbl = ["#cc0000","#ff3333","#ff6666","#ff9999", "#ffcccc","#ffffff","#ccddff","#6699ff","#0055ff","#003399","#002266"]
#blrd = ["#002266", "#003399", "#0055ff","#6699ff", "#ccddff", "#ffffff", "#ffcccc","#ff9999","#ff6666","#ff3333","#cc0000","#b30000", "#990000", "#800000", "#660000"]

ref_min_plt = var_diff_subplot(ref_min_diff, 111, res, 'Difference 2069 - 2015 REF MIN', tminmax, trangemax, levels=levels, cmap=blrd, steps=steps, par=True, mer=True)

plt.subplots_adjust(left=0.035, right=1)

filename = domain + '_2069-2015_REF_MIN_SENS.png'
plt.savefig(plotdir + filename)

fig, ax = plt.subplots(figsize=(16,12))
lats, lons = latlon_coords(min_diff_2015)

tminmax = -1
trangemax = 7
steps= 0.25
levels = [ -1., -0.5, 0.5, 1.5, 2.5, 3., 3.5, 4., 4.5, 5., 5.5]
blrd = [ "#ccddff", "#ffffff", "#ffcccc","#ff9999","#ff6666","#ff3333","#cc0000","#b30000", "#990000", "#800000", "#660000"]
rdbl = ["#cc0000","#ff3333","#ff6666","#ff9999", "#ffcccc","#ffffff","#ccddff","#6699ff","#0055ff","#003399","#002266"]
#blrd = ["#002266", "#003399", "#0055ff","#6699ff", "#ccddff", "#ffffff", "#ffcccc","#ff9999","#ff6666","#ff3333","#cc0000","#b30000", "#990000", "#800000", $

ref_min_plt = var_diff_subplot(sens_opt_min_diff, 111, res, 'Difference 2069 OPT - 2015 REF MIN', tminmax, trangemax, levels=levels, cmap=blrd, steps=steps, par=True, mer=True)

plt.subplots_adjust(left=0.035, right=1)

filename = domain + '_2069OPT-2015REF_MIN_SENS.png'
plt.savefig(plotdir + filename)

fig, ax = plt.subplots(figsize=(16,12))
lats, lons = latlon_coords(min_diff_2015)
#%%
tminmax = -1
trangemax = 7
steps= 0.25
levels = [ -4.,-3.5,-3.,-2.5,-1.5, -0.5, 0.5, 1.5, 2.5, 3., 3.5, 4., 4.5, 5., 5.5]
blrd = [ "#002266", "#003399", "#0055ff","#6699ff", "#ccddff", "#ffffff", "#ffcccc","#ff9999","#ff6666","#ff3333","#cc0000","#b30000", "#990000", "#800000", "#660000"]
rdbl = ["#cc0000","#ff3333","#ff6666","#ff9999", "#ffcccc","#ffffff","#ccddff","#6699ff","#0055ff","#003399","#002266"]
#blrd = ["#002266", "#003399", "#0055ff","#6699ff", "#ccddff", "#ffffff", "#ffcccc","#ff9999","#ff6666","#ff3333","#cc0000","#b30000", "#990000", "#800000", $

ref_min_plt = var_diff_subplot(sens_opt-spr_min_diff, 111, res, 'Difference (2069 OPT - 2015 REF) - (2069 SPR - 2015 REF) MIN', tminmax, trangemax, levels=levels, cmap=blrd, steps=steps, par=True, mer=True)

plt.subplots_adjust(left=0.035, right=1)

filename = domain + '_2069OPT-2015REF-2069SPR-2015REF_MIN_SENS.png'
plt.savefig(plotdir + filename)



""" preferences for 2015 run """
"""
steps= 0.5

tminmax = -8.5
tminmin = -6
trangemax = 17
trangemin = 12
# Create a figure for MAX PLOTS
fig, ax = plt.subplots(figsize=(16,10))

# Get the latitude and longitude points
lats, lons = latlon_coords(min_diff_2015)

fig.suptitle('difference 2069 - 2015' )

# REF LU_INDEX Plot
var_diff_subplot(ref_max_diff, 231, res, 'REF MAX', tminmax, trangemax, steps=steps, par=True, mer=True)
var_diff_subplot(spr_max_diff, 232, res, 'SPR MAX', tminmax, trangemax, steps=steps, par=False, mer=True)
var_diff_subplot(opt_max_diff, 233, res, 'OPT MAX', tminmax, trangemax, steps=steps, par=False, mer=True)

var_diff_subplot(ref_min_diff, 234, res, 'REF MIN', tminmin, trangemin, steps=steps, par=True, mer=True)
var_diff_subplot(spr_min_diff, 235, res, 'SPR MIN', tminmin, trangemin, steps=steps, par=False, mer=True)
var_diff_subplot(opt_min_diff, 236, res, 'OPT MIN', tminmin, trangemin, steps=steps, par=False, mer=True)





plt.tight_layout()
#plt.subplots_adjust(top=0.983,
#                    bottom=0.017,
#                    left=0.012,
#                    right=0.991,
#                    hspace=0.2,
#                    wspace=0.044
#                    )

filename = domain + '_RUNs_SENS.png'
plt.savefig(plotdir + filename)
"""
##%%
#
#""" START Plotting routine for OPT """
#
## Create a figure for MAX PLOTS
#fig, ax = plt.subplots(figsize=(16,16))
#
## Get the latitude and longitude points
#lats, lons = latlon_coords(opt_med_max)
#
#
#""" REF LU_INDEX Plot """
#ref_lu_plt = lu_subplot(ref_lu, 331, res, ref_lu.name, hgt, par=True, mer=False)
#
#""" opt LU_INDEX Plot """
#opt_lu_plt = lu_subplot(opt_lu, 332, res, opt_lu.name, hgt, par=False, mer=False)
#
#
#""" DIFF LU_INDEX Plot """
#opt_lu_diff_plt = lu_subplot(opt_lu_diff, 333, res, 'Difference ' + opt_lu_diff.name, hgt, par=False, mer=False)
#
#
#""" REF MAX Plot """
#ref_max_plt = var_subplot(ref_med_max, 334, res, ref_med_max.description, steps, maxmintemp, maxrange, par=True, mer=False)
#
#""" opt MAX Plot """
#opt_max_plt = var_subplot(opt_med_max, 335, res, opt_med_max.description, steps, maxmintemp, maxrange, par=False, mer=False)
#
#""" DIFF CASE - REF MAX plot """
#opt_maxdiff_plt = var_diff_subplot(opt_max_diff, 336, res, opt_max_diff.description, par=False, mer=False)
#
#
#""" REF MIN Plot """
#ref_min_plt = var_subplot(ref_med_min, 337, res, ref_med_min.description, steps, minmintemp, minrange, par=True, mer=True)
#
#""" opt MIN Plot """
#opt_min_plt = var_subplot(opt_med_min, 338, res, opt_med_min.description, steps, minmintemp, minrange, par=False, mer=True)
#
#""" DIFF CASE - REF MIN plot """
#opt_mindiff_plt = var_diff_subplot(opt_min_diff, 339, res, opt_min_diff.description, par=False, mer=True)
#
#
#plt.subplots_adjust(top=0.986,
#                    bottom=0.014,
#                    left=0.033,
#                    right=1.0,
#                    hspace=0.1,
#                    wspace=0.01)
#
#filename = domain + '_3x3_medMINMAX_LU_DIFF_Comp' + '_OPT.png'
#plt.savefig(plot_dir + filename)
#
#""" END Plotting routine for OPT """
#
#
#
#""" START Plotting routine for DIFF OPT - SPR """
#
## Create a figure for MAX PLOTS
#fig, ax = plt.subplots(figsize=(16,16))
#
## Get the latitude and longitude points
#lats, lons = latlon_coords(opt_med_max)
#
#
#""" SPR LU_INDEX Plot """
#spr_lu_plt = lu_subplot(spr_lu, 331, res, spr_lu.name, hgt, par=True, mer=False)
#
#""" OPT LU_INDEX Plot """
#opt_lu_plt = lu_subplot(opt_lu, 332, res, opt_lu.name, hgt, par=False, mer=False)
#
#""" DIFF LU_INDEX Plot """
#opt_spr_lu_diff = lu_subplot(opt_spr_lu_diff, 333, res, 'Difference SPR - OPT Landuse', hgt, par=False, mer=False)
#
#
#""" SPR MAX Plot """
#spr_max_plt = var_subplot(spr_med_max, 334, res, spr_med_max.description, steps, maxmintemp, maxrange, par=False, mer=False)
#
#""" OPT MAX Plot """
#opt_max_plt = var_subplot(opt_med_max, 335, res, opt_med_max.description, steps, maxmintemp, maxrange, par=False, mer=False)
#
#""" DIFF OPT - SPR MAX plot """
#opt_spr_max_diff_plt = var_diff_subplot(opt_spr_max_diff, 336, res, opt_spr_max_diff.description, par=False, mer=False)


#""" SPR MIN Plot """
#spr_min_plt = var_subplot(spr_med_min, 337, res, spr_med_min.description, steps, minmintemp, minrange, par=False, mer=True)
#
#""" OPT MIN Plot """
#opt_min_plt = var_subplot(opt_med_min, 338, res, opt_med_min.description, steps, minmintemp, minrange, par=False, mer=True)
#
#""" DIFF OPT - SPR MIN plot """
#opt_spr_min_diff_plt = var_diff_subplot(opt_spr_min_diff, 339, res, opt_spr_min_diff.description, par=False, mer=False)
#
#
#plt.subplots_adjust(top=0.986,
#                    bottom=0.014,
#                    left=0.033,
#                    right=1.0,
#                    hspace=0.1,
#                    wspace=0.01)
#
#filename = domain + '_3x3_medMINMAX_LU_DIFF_Comp' + '_OPT-SPR.png'
#plt.savefig(plot_dir + filename)
#
#""" END Plotting routine for OPT """
