# -*- coding: utf-8 -*-
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import numpy as np
import pandas as pd
import os
import wrf
from wrf import to_np, getvar, get_basemap, latlon_coords
#%%
"""
WICHTIG! Bilder mit Qt5 speichern da sonst Abstönde etc nicht passen!

Erstellt einen AREA 1x3 subplot för OPT & SPR mit:
    + DIFF LU index
    + DIFF median of MAX temp
    + DIFF median of MIN temp
"""


""" START Variable definition """

date = '2015-08-05' # Startdate of the WRF run / the time was in this ase always 18:00:00
domain = 'd03' # WRF domain
run = 'Ref_run_2017' # reference run
run1 = 'SPR_Run_2017' # sprawl run 
run2 = 'OPT_Run_2017' # optimized city run
path = '/hp4/Urbania/WRF-2019-Runs/' # runPATH
filepath = path + run + '/'
filepath1 = path + run1 + '/'
filepath2 = path + run2 + '/'
para = 'T2' # WRF Variable which shall be plotted
res = 'i' # resolution of basemap elements c = cruel, l = low, i = intermediate, h = high, f = full

spinup = pd.to_datetime(('2015-08-05', '2015-08-06', '2015-08-07', '2015-08-08')) # spinup time 
cuttime = pd.to_datetime(('2015-08-11', '2015-08-14')) # day with not usable data, will be cut out from calculation data
cuttime = spinup.append(cuttime)

filenam = 'wrfout_' + domain + '_' + date + '_18_00_00.nc'
plot_dir ='/hp4/Urbania/plots/' + date + '/'

if not os.path.exists(plot_dir): # creates directory if not existing
    os.makedirs(plot_dir)

 
""" END Variable definition """

""" START defining FUNCTIONS """

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
    
    
    heights = np.arange(100, 800, 75)
    categ = np.arange(1,34, 1)
    
    # Draw the contours and filled contours
    hgt_cont = bm.contour(x,y,to_np(hgt), levels=heights, colors="magenta", linewidths=0.4, alpha=1)
    var_contf = bm.pcolormesh(x,y,to_np(var), cmap=get_cmap("viridis"), alpha=0.9)
    cb_var = fig.colorbar(var_contf, ticks=categ[::3], ax=ax, shrink=0.4)
    cb_var.ax.tick_params(labelsize=8)
    return


def var_subplot(var, pos, res, title, hgt, par=True, mer=True):
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
    
#    levels=np.arange(-1.0, 1.0+steps, steps)
#    levels=np.insert(levels,0, np.arange((maxdiff_spr.min()*10).round()/10,-1,steps*6))
#    levels=np.append(levels, np.arange(1,(maxdiff_spr.max()*10).round()/10,steps*6))
#    
#    contour_levels=np.arange(-1.0, 1.0+steps, steps*2)
#    contour_levels=np.insert(contour_levels,0, (var.min()*10).round()/10)
#    contour_levels=np.append(contour_levels, (var.max()*10).round()/10)
    
    heights = np.arange(100, 800, 75)

    # Draw the contours and filled contours
    hgt_cont = bm.contour(x,y,to_np(hgt), levels=heights, colors="magenta", linewidths=0.4, alpha=1)
    var_cont = bm.contour(x,y,to_np(var), colors="black", linewidths=0.4, alpha=0.5)
    var_contf = bm.contourf(x,y,to_np(var), cmap=get_cmap("RdBu_r"), extend='both', alpha=0.9)
    cb_var = fig.colorbar(var_contf, ax=ax, shrink=0.4)
    cb_var.ax.tick_params(labelsize=8)
    return

def var_diff_subplot(var, pos, res, title, hgt, steps, par=True, mer=True):
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
    
    levels=np.arange(-1.0, 1.0+steps, steps)
    heights = np.arange(100, 800, 75)

    # Draw the contours and filled contours
    hgt_cont = bm.contour(x,y,to_np(hgt), levels=heights, colors="magenta", linewidths=0.4, alpha=1)
    var_cont = bm.contour(x,y,to_np(var), colors="black", levels=levels[::3], linewidths=0.4, alpha=0.5)
    var_contf = bm.contourf(x,y,to_np(var), levels=levels, cmap=get_cmap("RdBu_r"), extend='both', alpha=0.9)
    cb_var = fig.colorbar(var_contf, ax=ax, shrink=0.4)
    cb_var.ax.tick_params(labelsize=8)
    return

""" END defining FUNCTIONS """


ncfile = Dataset(filepath + filenam)
ncfile1 = Dataset(filepath1 + filenam)
ncfile2 = Dataset(filepath2 + filenam)

#Dimension of domain
data = getvar(ncfile, para, timeidx=wrf.ALL_TIMES)
data_max = (data.max()/10).round()*10
data_min = (data.min()/10).round()*10
data1 = getvar(ncfile1, para, timeidx=wrf.ALL_TIMES)
data2 = getvar(ncfile2, para, timeidx=wrf.ALL_TIMES)

times = getvar(ncfile, "Times", timeidx=wrf.ALL_TIMES, meta=False) # FC times in np.datetime64 format - very ugly
init = pd.to_datetime(times[0]) # converts the numpy datetime to datetime datetime format
init = str(init) # initial time of wrf dataset

ref = data     # data is a safetyvariable for attributes
spr = data1
opt = data2


#%%
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

ref_med_max = ref_med_max.assign_attrs({'projection': data.projection,
                                        'description': 'REF Median of MAX '+data.description,
                                        'units': 'degree Celsius'})
ref_med_min = ref_med_min.assign_attrs({'projection': data.projection,
                                        'description': 'REF Median of MIN '+data.description,
                                        'units': 'degree Celsius'})

    
    
opt_daily_max = opt.groupby(opt.Time.dt.day).max(axis=0)
opt_daily_min = opt.groupby(opt.Time.dt.day).min(axis=0)

opt_med_max = opt_daily_max.median(axis=0) - 273.15
opt_med_min = opt_daily_min.median(axis=0) - 273.15

opt_med_max = opt_med_max.assign_attrs({'projection': data.projection,
                                        'description': 'OPT Median of MAX '+data.description,
                                        'units': 'degree Celsius'})
opt_med_min = opt_med_min.assign_attrs({'projection': data.projection,
                                        'description': 'OPT Median of MIN '+data.description,
                                        'units': 'degree Celsius'})

    
    
spr_daily_max = spr.groupby(spr.Time.dt.day).max(axis=0)
spr_daily_min = spr.groupby(spr.Time.dt.day).min(axis=0)

spr_med_max = spr_daily_max.median(axis=0) - 273.15
spr_med_min = spr_daily_min.median(axis=0) - 273.15

spr_med_max = spr_med_max.assign_attrs({'projection': data.projection,
                                        'description': 'SPR Median of MAX '+data.description,
                                        'units': 'degree Celsius'})
spr_med_min = spr_med_min.assign_attrs({'projection': data.projection,
                                        'description': 'SPR Median of MIN '+data.description,
                                        'units': 'degree Celsius'})

""" END Calculation of areal median of MIN & MAX """

    
""" START Calculation of Differences between REF SPR OPT """   

spr_max_diff = spr_med_max - ref_med_max
spr_min_diff = spr_med_min - ref_med_min

opt_max_diff = opt_med_max - ref_med_max
opt_min_diff = opt_med_min - ref_med_min

spr_max_diff = spr_max_diff.assign_attrs({'projection': data.projection,
                                        'description': 'Difference SPR - REF of Median of MAX '+data.description,
                                        'units': 'degree Celsius'})
spr_min_diff = spr_min_diff.assign_attrs({'projection': data.projection,
                                        'description': 'Difference SPR - REF Median of MIN '+data.description,
                                        'units': data.units})

opt_max_diff = opt_max_diff.assign_attrs({'projection': data.projection,
                                        'description': 'Difference OPT - REF of Median of MAX '+data.description,
                                        'units': 'degree Celsius'})
opt_min_diff = opt_min_diff.assign_attrs({'projection': data.projection,
                                        'description': 'Difference OPT - REF Median of MIN '+data.description,
                                        'units': 'degree Celsius'})

""" END Calculation of Differences between REF SPR OPT """


""" START getting LU_INDEX/HGT and create DIFFS """

hgt = getvar(ncfile, 'HGT')
ref_lu = getvar(ncfile, 'LU_INDEX').rename('REF Landuse Category\'s')
spr_lu = getvar(ncfile1, 'LU_INDEX').rename('SPR Landuse Category\'s')
opt_lu = getvar(ncfile2, 'LU_INDEX').rename('OPT Landuse Category\'s')

spr_lu_diff = spr_lu.where(ref_lu.data != spr_lu.data)
opt_lu_diff = opt_lu.where(ref_lu.data != opt_lu.data)

""" END getting LU_INDEX and create DIFFS """


#%%
""" START Plotting routine for SPR """

# Create a figure for MAX PLOTS
fig, ax = plt.subplots(figsize=(20,9))

# Get the latitude and longitude points
lats, lons = latlon_coords(spr_med_max)


""" DIFF LU_INDEX Plot """
spr_lu_diff_plt = lu_subplot(spr_lu_diff, 131, res, 'Difference ' + spr_lu_diff.name, hgt, par=True, mer=True)

""" DIFF CASE - REF MAX plot """
spr_maxdiff_plt = var_diff_subplot(spr_max_diff, 132, res, spr_max_diff.description, hgt, 0.1, par=False, mer=True)

""" DIFF CASE - REF MIN plot """
spr_mindiff_plt = var_diff_subplot(spr_min_diff, 133, res, spr_min_diff.description, hgt, 0.1, par=False, mer=True)


plt.subplots_adjust(top=0.996,
                    bottom=0.014,
                    left=0.033,
                    right=1.0,
                    hspace=0.01,
                    wspace=0.01)

filename = domain + '_medMINMAX_LU_Comp' + '_SPR_onlyDIFF.png'
plt.savefig(plot_dir + filename)

""" END Plotting routine for SPR """




""" START Plotting routine for OPT """

# Create a figure for MAX PLOTS
fig, ax = plt.subplots(figsize=(20,9))

# Get the latitude and longitude points
lats, lons = latlon_coords(opt_med_max)


""" DIFF LU_INDEX Plot """
opt_lu_diff_plt = lu_subplot(opt_lu_diff, 131, res, 'Difference ' + opt_lu_diff.name, hgt, par=True, mer=True)

""" DIFF CASE - REF MAX plot """
opt_maxdiff_plt = var_diff_subplot(opt_max_diff, 132, res, opt_max_diff.description, hgt, 0.1, par=False, mer=True)

""" DIFF CASE - REF MIN plot """
opt_mindiff_plt = var_diff_subplot(opt_min_diff, 133, res, opt_min_diff.description, hgt, 0.1, par=False, mer=True)


plt.subplots_adjust(top=0.996,
                    bottom=0.014,
                    left=0.033,
                    right=1.0,
                    hspace=0.01,
                    wspace=0.01)

filename = domain + '_medMINMAX_LU_Comp' + '_OPT_onlyDIFF.png'
plt.savefig(plot_dir + filename)

""" END Plotting routine for OPT """