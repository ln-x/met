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

date = '2015-08-05' 
#date = '2069-07-01' # Startdate of the WRF run / the time was in this ase always 18:00:00
domain = 'd03' # WRF domain
run = 'REF_Run_2015' # reference run
run1 = 'SPR_Run_2015' # sprawl run 
run2 = 'OPT_Run_2015' # optimized city run
path = '/hp4/Urbania/WRF-2019-Runs/' # runPATH
filepath = path + run + '/'
filepath1 = path + run1 + '/'
filepath2 = path + run2 + '/'
para = 'T2' # WRF Variable which shall be plotted
res = 'c' # resolution of basemap elements c = low, i = intermediate, h = high, f = full

""" not usable days - uncomment the run """
#cuttime = pd.to_datetime(['2069-7-1','2069-7-2','2069-7-3','2069-7-4','2069-7-5', '2069-7-6','2069-7-9']) # 2069 run
cuttime = pd.to_datetime(['2015-08-05', '2015-08-06', '2015-08-07', '2015-08-08','2015-08-11', '2015-08-14']) # 2015 run


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
    
    
    heights = np.arange(100, 800, 50)
    categ = np.arange(1,34, 1)
    
    # Draw the contours and filled contours
    hgt_cont = bm.contour(x,y,to_np(hgt), levels=heights, colors="magenta", linewidths=0.4, alpha=1)
    var_contf = bm.pcolormesh(x,y,to_np(var), cmap=get_cmap("viridis"), alpha=0.9)
    cb_var = fig.colorbar(var_contf, ticks=categ[::3], ax=ax, shrink=0.7)
    cb_var.ax.tick_params(labelsize=8)
    return


def var_subplot(var, pos, res, title,  steps, tmin, trange, par=True, mer=True):
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
        bm.drawparallels(parallels,labels=[1,0,0,0],fontsize=14)
    else:
        bm.drawparallels(parallels,fontsize=8)
    if mer == True:
        bm.drawmeridians(meridians,labels=[0,0,0,1],fontsize=14)
    else:
        bm.drawmeridians(meridians,fontsize=14)
#    bm.drawrivers(linewidth=0.75,color='blue') #only for high resolution plots
    bm.readshapefile('/home/kristofh/projects/shp_files/BEZIRKSGRENZEOGDPolygon', 'BEZIRKSGRENZEOGDPolygon', linewidth=0.6)
    
    levels=np.arange(tmin, tmin + trange, steps)
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
    var_contf = bm.contourf(x,y,to_np(var), levels=levels, cmap=get_cmap("RdBu_r"), extend='both', alpha=0.9)
    cb_var = fig.colorbar(var_contf, ax=ax, shrink=0.7)
    cb_var.ax.tick_params(labelsize=14)
    return

def var_diff_subplot(var, pos, res, title, steps=0.25, par=True, mer=True):
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
    
    levels=np.arange(-1.5, 1.5+steps, steps)
#    heights = np.arange(100, 800, 50)

    # Draw the contours and filled contours
#    hgt_cont = bm.contour(x,y,to_np(hgt), levels=heights, colors="magenta", linewidths=0.4, alpha=1)
    var_cont = bm.contour(x,y,to_np(var), colors="black", levels=levels, linewidths=0.4, alpha=0.5)
    var_contf = bm.contourf(x,y,to_np(var), levels=levels, cmap=get_cmap("RdBu_r"), extend='both', alpha=0.9)
    cb_var = fig.colorbar(var_contf, ax=ax, shrink=0.7)
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

data.close()
data1.close()
data2.close()

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

opt_spr_min_diff = opt_med_min - spr_med_min
opt_spr_max_diff = opt_med_max - spr_med_max




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

opt_spr_min_diff = opt_spr_min_diff.assign_attrs({'projection': data.projection,
                                        'description': 'Difference OPT - SPR Median of MIN '+data.description,
                                        'units': 'degree Celsius'})
opt_spr_max_diff = opt_spr_max_diff.assign_attrs({'projection': data.projection,
                                        'description': 'Difference OPT - SPR Median of MAX '+data.description,
                                        'units': 'degree Celsius'})

""" END Calculation of Differences between REF SPR OPT """


""" START getting LU_INDEX/HGT and create DIFFS """

hgt = getvar(ncfile, 'HGT')
ref_lu = getvar(ncfile, 'LU_INDEX').rename('REF Landuse Category\'s')
spr_lu = getvar(ncfile1, 'LU_INDEX').rename('SPR Landuse Category\'s')
opt_lu = getvar(ncfile2, 'LU_INDEX').rename('OPT Landuse Category\'s')

spr_lu_diff = spr_lu.where(ref_lu.data != spr_lu.data)
opt_lu_diff = opt_lu.where(ref_lu.data != opt_lu.data)
opt_spr_lu_diff = spr_lu.where(spr_lu.data != opt_lu.data)

""" END getting LU_INDEX and create DIFFS """


#%%
""" START Plotting routine for SPR """

""" preferences for 2069 run """
#maxrange = 12.
#minrange = 10.
#maxmintemp = 33.
#minmintemp = 20.
#steps= 1.

""" preferences for 2015 run """
maxrange = 9.
minrange = 8.
maxmintemp = 28.
minmintemp = 19.
steps= 1.
#%%

# Create a figure for MAX PLOTS
fig, ax = plt.subplots(figsize=(16,16))

# Get the latitude and longitude points
lats, lons = latlon_coords(spr_med_max)


""" REF LU_INDEX Plot """
ref_lu_plt = lu_subplot(ref_lu, 331, res, ref_lu.name, hgt, par=True, mer=False)

""" SPR LU_INDEX Plot """
spr_lu_plt = lu_subplot(spr_lu, 332, res, spr_lu.name, hgt, par=False, mer=False)


""" DIFF LU_INDEX Plot """
spr_lu_diff_plt = lu_subplot(spr_lu_diff, 333, res, 'Difference ' + spr_lu_diff.name, hgt, par=False, mer=False)


""" REF MAX Plot """
ref_max_plt = var_subplot(ref_med_max, 334, res, ref_med_max.description, steps, maxmintemp, maxrange, par=True, mer=False)

""" SPR MAX Plot """
spr_max_plt = var_subplot(spr_med_max, 335, res, spr_med_max.description, steps, maxmintemp, maxrange, par=False, mer=False)

""" DIFF CASE - REF MAX plot """
spr_maxdiff_plt = var_diff_subplot(spr_max_diff, 336, res, spr_max_diff.description, par=False, mer=False)


""" REF MIN Plot """
ref_min_plt = var_subplot(ref_med_min, 337, res, ref_med_min.description, steps, minmintemp, minrange, par=True, mer=True)

""" SPR MIN Plot """
spr_min_plt = var_subplot(spr_med_min, 338, res, spr_med_min.description, steps, minmintemp, minrange, par=False, mer=True)

""" DIFF CASE - REF MIN plot """
spr_mindiff_plt = var_diff_subplot(spr_min_diff, 339, res, spr_min_diff.description, par=False, mer=True)


plt.subplots_adjust(top=0.986,
                    bottom=0.014,
                    left=0.033,
                    right=1.0,
                    hspace=0.1,
                    wspace=0.01)

filename = domain + '_3x3_medMINMAX_LU_DIFF_Comp' + '_SPR.png'
plt.savefig(plot_dir + filename)

""" END Plotting routine for SPR """




""" START Plotting routine for OPT """

# Create a figure for MAX PLOTS
fig, ax = plt.subplots(figsize=(16,16))

# Get the latitude and longitude points
lats, lons = latlon_coords(opt_med_max)


""" REF LU_INDEX Plot """
ref_lu_plt = lu_subplot(ref_lu, 331, res, ref_lu.name, hgt, par=True, mer=False)

""" opt LU_INDEX Plot """
opt_lu_plt = lu_subplot(opt_lu, 332, res, opt_lu.name, hgt, par=False, mer=False)


""" DIFF LU_INDEX Plot """
opt_lu_diff_plt = lu_subplot(opt_lu_diff, 333, res, 'Difference ' + opt_lu_diff.name, hgt, par=False, mer=False)


""" REF MAX Plot """
ref_max_plt = var_subplot(ref_med_max, 334, res, ref_med_max.description, steps, maxmintemp, maxrange, par=True, mer=False)

""" opt MAX Plot """
opt_max_plt = var_subplot(opt_med_max, 335, res, opt_med_max.description, steps, maxmintemp, maxrange, par=False, mer=False)

""" DIFF CASE - REF MAX plot """
opt_maxdiff_plt = var_diff_subplot(opt_max_diff, 336, res, opt_max_diff.description, par=False, mer=False)


""" REF MIN Plot """
ref_min_plt = var_subplot(ref_med_min, 337, res, ref_med_min.description, steps, minmintemp, minrange, par=True, mer=True)

""" opt MIN Plot """
opt_min_plt = var_subplot(opt_med_min, 338, res, opt_med_min.description, steps, minmintemp, minrange, par=False, mer=True)

""" DIFF CASE - REF MIN plot """
opt_mindiff_plt = var_diff_subplot(opt_min_diff, 339, res, opt_min_diff.description, par=False, mer=True)


plt.subplots_adjust(top=0.986,
                    bottom=0.014,
                    left=0.033,
                    right=1.0,
                    hspace=0.1,
                    wspace=0.01)

filename = domain + '_3x3_medMINMAX_LU_DIFF_Comp' + '_OPT.png'
plt.savefig(plot_dir + filename)

""" END Plotting routine for OPT """



""" START Plotting routine for DIFF OPT - SPR """

# Create a figure for MAX PLOTS
fig, ax = plt.subplots(figsize=(16,16))

# Get the latitude and longitude points
lats, lons = latlon_coords(opt_med_max)


""" SPR LU_INDEX Plot """
spr_lu_plt = lu_subplot(spr_lu, 331, res, spr_lu.name, hgt, par=True, mer=False)

""" OPT LU_INDEX Plot """
opt_lu_plt = lu_subplot(opt_lu, 332, res, opt_lu.name, hgt, par=False, mer=False)

""" DIFF LU_INDEX Plot """
opt_spr_lu_diff = lu_subplot(opt_spr_lu_diff, 333, res, 'Difference SPR - OPT Landuse', hgt, par=False, mer=False)


""" SPR MAX Plot """
spr_max_plt = var_subplot(spr_med_max, 334, res, spr_med_max.description, steps, maxmintemp, maxrange, par=False, mer=False)

""" OPT MAX Plot """
opt_max_plt = var_subplot(opt_med_max, 335, res, opt_med_max.description, steps, maxmintemp, maxrange, par=False, mer=False)

""" DIFF OPT - SPR MAX plot """
opt_spr_max_diff_plt = var_diff_subplot(opt_spr_max_diff, 336, res, opt_spr_max_diff.description, par=False, mer=False)


""" SPR MIN Plot """
spr_min_plt = var_subplot(spr_med_min, 337, res, spr_med_min.description, steps, minmintemp, minrange, par=False, mer=True)

""" OPT MIN Plot """
opt_min_plt = var_subplot(opt_med_min, 338, res, opt_med_min.description, steps, minmintemp, minrange, par=False, mer=True)

""" DIFF OPT - SPR MIN plot """
opt_spr_min_diff_plt = var_diff_subplot(opt_spr_min_diff, 339, res, opt_spr_min_diff.description, par=False, mer=False)


plt.subplots_adjust(top=0.986,
                    bottom=0.014,
                    left=0.033,
                    right=1.0,
                    hspace=0.1,
                    wspace=0.01)

filename = domain + '_3x3_medMINMAX_LU_DIFF_Comp' + '_OPT-SPR.png'
plt.savefig(plot_dir + filename)

""" END Plotting routine for OPT """

#%%
""" START Plotting routine for single min plot """

# Create a figure for MAX PLOTS
fig, ax = plt.subplots(figsize=(16,12))

# Get the latitude and longitude points
lats, lons = latlon_coords(opt_med_max)

""" REF MAX Plot """

ref_min_plt = var_subplot(ref_med_min, 111, res, ref_med_min.description, steps, minmintemp, minrange, par=True, mer=True)

plt.tight_layout()
plt.subplots_adjust(top=0.986,
                    bottom=0.014,
                    left=0.06,
                    right=1.0,
                    hspace=0.1,
                    wspace=0.01)

filename = domain + '_REF_min.png'
plt.savefig(plot_dir + filename)