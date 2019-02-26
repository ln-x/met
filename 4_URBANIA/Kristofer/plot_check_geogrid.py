# -*- coding: utf-8 -*-
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.cm import get_cmap
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
#import cartopy.feature as cfeature
import cartopy as cpy
import numpy as np
import datetime
import pandas as pd
import sys
import os
import wrf
from wrf import to_np, getvar, smooth2d, get_basemap, latlon_coords

""" 
Erstellt einen KONTROLL plot für geo_em - files mit:
    + LU REF / SPR / OPT
    + DIFF SPR - REF
    + DIFF OPT - REF
"""

# EXAMPLE
# plot 30-year mean of precipitation dataset
# load data as xarray dataset
date = '2015-08-05'
domain = 'd03'
run = 'REF_geo_files'
#run1 = 'SPR_geo_files'
#run2 = 'OPT_geo_files'
path = '/hp4/Urbania/WRF-TEB/WPS/'
param = 'LU_INDEX'

res = 'h'

filepath = path + '/'
#filepath1 = path + run1 + '/'
#filepath2 = path + run2 + '/'

filenam = 'geo_em.d03.nc'

plot_dir ='/home/kristofh/projects/Urbania/plots/' + date + '/' + run + '/'
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)


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
    
    
    heights = np.arange(100, 800, 5)
    categ = np.arange(1,34, 1)
    
    # Draw the contours and filled contours
    hgt_cont = bm.contour(x,y,to_np(hgt), levels=heights, colors="magenta", linewidths=0.4, alpha=1)
    var_contf = bm.pcolormesh(x,y,to_np(var), cmap=get_cmap("viridis"), alpha=0.9)
    cb_var = fig.colorbar(var_contf, ticks=categ[::3], ax=ax, shrink=0.4)
    cb_var.ax.tick_params(labelsize=8)
    return




ncfile = Dataset(filepath + filenam)
ncfile1 = Dataset(filepath1 + filenam)
ncfile2 = Dataset(filepath2 + filenam)

#var = getvar(ncfile, param, timeidx=wrf.ALL_TIMES)
#var.plot(cmap='tab20')

hgt = getvar(ncfile, 'HGT_M')
ref_lu = getvar(ncfile, 'LU_INDEX').rename('REF Landuse Category\'s')
#spr_lu = getvar(ncfile1, 'LU_INDEX').rename('SPR Landuse Category\'s')
#opt_lu = getvar(ncfile2, 'LU_INDEX').rename('OPT Landuse Category\'s')

#spr_lu_diff = spr_lu.where(ref_lu.data != spr_lu.data)
#opt_lu_diff = opt_lu.where(ref_lu.data != opt_lu.data)


""" START Plotting routine for SPR """


fig, ax = plt.subplots(figsize=(20,9))

# Get the latitude and longitude points
lats, lons = latlon_coords(spr_lu_diff)

""" REF LU_INDEX Plot """
ref_lu_plt = lu_subplot(ref_lu, 231, res, ref_lu.name, hgt, par=True, mer=False)

""" SPR LU_INDEX Plot """
#spr_lu_plt = lu_subplot(spr_lu, 232, res, spr_lu.name, hgt, par=False, mer=False)
#
#""" opt LU_INDEX Plot """
#opt_lu_plt = lu_subplot(opt_lu, 233, res, opt_lu.name, hgt, par=False, mer=False)
#
#
#""" DIFF LU_INDEX Plot """
#spr_lu_diff_plt = lu_subplot(spr_lu_diff, 235, res, 'Difference ' + spr_lu_diff.name, hgt, par=True, mer=True)
#
#""" DIFF LU_INDEX Plot """
#opt_lu_diff_plt = lu_subplot(opt_lu_diff, 236, res, 'Difference ' + opt_lu_diff.name, hgt, par=True, mer=True)

plt.subplots_adjust(top=0.996,
                    bottom=0.014,
                    left=0.033,
                    right=1.0,
                    hspace=0.01,
                    wspace=0.01)

filename = 'LU_DIFF.png'
plt.savefig(plot_dir + filename)


#%%


#plt.contourf(var, cmap='rainbow')
#plt.contour(hgt)

var = getvar(ncfile, param, timeidx=wrf.ALL_TIMES)
var = var[0]
title = var.description
title1 = var.name + ' [' + var.units + ']' + ' - ' + run 
#currtime = str(pd.to_datetime(time))
var_mean = var.mean(dim={'south_north','west_east'})
var_std = var.std(dim={'south_north','west_east'})
# Smooth the sea level pressure since it tends to be noisy near the mountains
# smooth_slp = smooth2d(slp, 3)

# Get the latitude and longitude points
lats, lons = latlon_coords(var)

# Get the basemap object
bm = get_basemap(var, resolution='h', projection='lcc')

# Define gridlines
parallels = np.arange(-90,90,0.2)
meridians = np.arange(0,360,0.2)

# Create a figure
fig = plt.figure(figsize=(12,9))

# Add geographic outlines
bm.drawcoastlines(linewidth=1)
bm.drawstates(linewidth=1)
bm.drawcountries(linewidth=1)
bm.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
bm.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)
bm.drawrivers(linewidth=0.75,color='blue') #only for high resolution plots
#bm.shadedrelief() #beautiful for bigger areas with mountains
bm.readshapefile('/home/kristofh/projects/shp_files/BEZIRKSGRENZEOGDPolygon', 'BEZIRKSGRENZEOGDPolygon', linewidth=1.2)
#bm.readshapefile('/home/kristofh/projects/shp_files/STATISTIK_AUSTRIA_NUTS2_20160101', 'STATISTIK_AUSTRIA_NUTS2_20160101', linewidth=1)

# Convert the lats and lons to x and y.  Make sure you convert the lats and lons to
# numpy arrays via to_np, or basemap crashes with an undefined RuntimeError.
x, y = bm(to_np(lons), to_np(lats))
steps = 1
levels=np.arange(1, 34, steps)
heights = np.arange(100, 800, 75)
# Draw the contours and filled contours
bm.contour(x, y, to_np(hgt), levels=heights, colors="magenta", linewidths=1.2, alpha=1.)
var_cont = bm.pcolormesh(x, y, to_np(var), cmap=get_cmap("viridis"), alpha=0.9)

cb = bm.colorbar(var_cont, spacing='uniform', ticks=levels, location='right', pad=0.2)

# setting colorbar with fixed limits
#m = plt.cm.ScalarMappable(cmap=get_cmap("jet"))
#m.set_array(to_np(t2))
#m.set_clim(int(data_min), int(data_max))
#plt.colorbar(t2_cont)
#cbar.set_ticks(clevs)
ax = plt.gca()
ax.text(0,1.08,title1,fontsize=14,transform=ax.transAxes)
#ax.text(0,1.01,title+'\nValid:'+currtime,fontsize=14,transform=ax.transAxes)
#ax.text(0.7,1.01,'Init: '+init, fontsize=12,transform=ax.transAxes)
ax.text(0.7,1.07,'MEAN: '+str(var_mean.values), fontsize=12,transform=ax.transAxes)
ax.text(0.7,1.04,'STD: '+str(var_std.values), fontsize=12,transform=ax.transAxes)
filename = domain + '_' + var.name + '_REF' +".png"
plt.savefig(plot_dir + filename)


#%%
#Dimension of domain
data = getvar(ncfile, param, timeidx=wrf.ALL_TIMES)
data_max = (data.max()/10).round()*10
data_min = (data.min()/10).round()*10

times = getvar(ncfile, "Times", timeidx=wrf.ALL_TIMES, meta=False) # FC times in np.datetime64 format - very ugly
init = pd.to_datetime(times[0]) # converts the numpy datetime to datetime datetime format
init = str(init) # initial time of wrf dataset




for idx, time in enumerate(times):
    
    #get vavriable from netCDF file
    var = getvar(ncfile, param, timeidx=idx)
    title = var.description
    title1 = var.name + ' [' + var.units + ']' + ' - ' + run 
    currtime = str(pd.to_datetime(time))
    var_mean = var.mean(dim={'south_north','west_east'})
    var_std = var.std(dim={'south_north','west_east'})
    # Smooth the sea level pressure since it tends to be noisy near the mountains
    # smooth_slp = smooth2d(slp, 3)
    
    # Get the latitude and longitude points
    lats, lons = latlon_coords(var)

    # Get the basemap object
    bm = get_basemap(var, resolution='h', projection='lcc')

    # Define gridlines
    parallels = np.arange(-90,90,0.2)
    meridians = np.arange(0,360,0.2)

    # Create a figure
    fig = plt.figure(idx, figsize=(12,9))

    # Add geographic outlines
    bm.drawcoastlines(linewidth=1)
    bm.drawstates(linewidth=1)
    bm.drawcountries(linewidth=1)
    bm.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
    bm.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)
    bm.drawrivers(linewidth=0.75,color='blue') #only for high resolution plots
    #bm.shadedrelief() #beautiful for bigger areas with mountains
    bm.readshapefile('/home/kristofh/projects/shp_files/BEZIRKSGRENZEOGDPolygon', 'BEZIRKSGRENZEOGDPolygon', linewidth=1.2)
    #bm.readshapefile('/home/kristofh/projects/shp_files/STATISTIK_AUSTRIA_NUTS2_20160101', 'STATISTIK_AUSTRIA_NUTS2_20160101', linewidth=1)

    # Convert the lats and lons to x and y.  Make sure you convert the lats and lons to
    # numpy arrays via to_np, or basemap crashes with an undefined RuntimeError.
    x, y = bm(to_np(lons), to_np(lats))
    steps = 1
    levels=np.arange(1, 25, steps)
    # Draw the contours and filled contours
    bm.contour(x, y, to_np(var), colors="black", levels=levels, linewidths=0.4, alpha=0.5)
    var_cont = bm.contourf(x, y, to_np(var), levels=levels, cmap=get_cmap("Paired"), alpha=0.9)
    
    cb = bm.colorbar(var_cont, location='right', pad=0.2)
    
    # setting colorbar with fixed limits
    #m = plt.cm.ScalarMappable(cmap=get_cmap("jet"))
    #m.set_array(to_np(t2))
    #m.set_clim(int(data_min), int(data_max))
    #plt.colorbar(t2_cont)
    #cbar.set_ticks(clevs)
    ax = plt.gca()
    ax.text(0,1.08,title1,fontsize=14,transform=ax.transAxes)
    ax.text(0,1.01,title+'\nValid:'+currtime,fontsize=14,transform=ax.transAxes)
    ax.text(0.7,1.01,'Init: '+init, fontsize=12,transform=ax.transAxes)
    ax.text(0.7,1.07,'MEAN: '+str(var_mean.values), fontsize=12,transform=ax.transAxes)
    ax.text(0.7,1.04,'STD: '+str(var_std.values), fontsize=12,transform=ax.transAxes)
    filename = domain + '_' + var.name + '_' + currtime +".png"
    plt.savefig(plot_dir + filename)
