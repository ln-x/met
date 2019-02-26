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
Erstellt AREA plots von allen Zeitpunkten der eingegebenen Variable
"""

# EXAMPLE
# plot 30-year mean of precipitation dataset
# load data as xarray dataset
date = '2015-08-05'
domain = 'd03'
run = '/hasel_test/'
path = '/hp4/Urbania/WRF-TEB/WPS'
param = 'LU_INDEX'

filepath1 = path + '/'
filenam = 'geo_em.d03.nc'

plot_dir ='/home/kristofh/projects/Urbania/plots/' + date + '/' + run + '/'
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)

ncfile = Dataset(filepath1 + filenam)


#%%
#Dimension of domain
data = getvar(ncfile, param, timeidx=wrf.ALL_TIMES)
data_max = (data.max()/10).round()*10
data_min = (data.min()/10).round()*10

times = getvar(ncfile, "Times", timeidx=wrf.ALL_TIMES, meta=False) # FC times in np.datetime64 format - very ugly
init = pd.to_datetime(times[0]) # converts the numpy datetime to datetime datetime format
init = str(init) # initial time of wrf dataset


#%%

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
