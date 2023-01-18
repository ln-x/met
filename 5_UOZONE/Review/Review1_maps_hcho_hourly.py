# -*- coding: utf-8 -*-
__author__ = 'lnx'
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import datetime
import os
import matplotlib.pyplot as plt
from netCDF4 import Dataset as netcdf_dataset
from cartopy import config
import cartopy.crs as ccrs
import cartopy.feature as cf
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

filename = r'/windata/DATA/DATAGEO/4_Vienna/CityBorderVienna.shp'
filename_as_moc_jun = "/data1/models/mocage/assim/hmmacc01+Jun-2019.nc"
filename_as_moc_jul = "/data1/models/mocage/assim/hmmacc01+Jul-2019.nc"
filename_as_moc_aug = "/data1/models/mocage/assim/hmmacc01+Aug-2019.nc"
dataset = netcdf_dataset(filename_as_moc_jun)
#TODO title=date
#TODO fix color scale, don't overwrite

lat1,lat2,lon1,lon2 = 192,212,413,433
lats = dataset.variables['lat'][lat1:lat2]
lons = dataset.variables['lon'][lon1:lon2]

def ReadinMocage(path, starttime, lat1, lat2, lon1, lon2):
    infile = netcdf_dataset(path)
    HCHO_moc = infile.variables['HCHO_47'][starttime,lat1:lat2,lon1:lon2]
    timestep = infile.variables['time']
    #ISO_moc = infile.variables['ISO_47'][1, lat1:lat2, lon1:lon2]
    #O3_moc = infile.variables['O_x_47'][1, lat1:lat2, lon1:lon2]
    #time = infile.variables['time'][:]
    #timeaxis = pd.date_range(starttime, periods=len(time), freq="H")
    #MOC_out = pd.DataFrame({'datetime': timeaxis, 'ISO': ISO_moc, 'HCHO': HCHO_moc,'O3': O3_moc})
    #MOC_out['datetime'] = pd.to_datetime(MOC_out['datetime'])
    #MOC_out = MOC_out.set_index(['datetime'])
    return HCHO_moc, timestep

date = datetime.datetime(year=int(2019), month=int(7), day=int(1), hour=int(0))
for i in range(24):
    #print(date)
    #i = i+480 #setstart for 20.July (+20 days*24h)
    #i = i+600 #setstart for 25.July (+25 days*24h)
    #i = i+624 #setstart for 25.July (+26 days*24h)
    HCHO_moc, timestep = ReadinMocage(filename_as_moc_jul,i,lat1,lat2,lon1,lon2)
    ax = plt.axes(projection=ccrs.PlateCarree())
    plt.title(date)
    levels = np.linspace(0, 1.25E-8, 50) #for 1july:1.25e-8, for 25-26:1e-8
    #levels = np.linspace(0, 9e-9, 50)
    plt.contourf(lons, lats, HCHO_moc, levels=levels,
             transform=ccrs.PlateCarree(),cmap="rainbow")
    #plt.pcolor(HCHO_moc_1, vmin=0, vmax=2.4E-8)
    plt.clim(0, 1.25e-8)
    #plt.clim(0, 9e-9)
    plt.colorbar(label="HCHO [?]")
    shape_feature = ShapelyFeature(Reader(filename).geometries(), crs=ccrs.PlateCarree(),edgecolor="black",facecolor=(0,0,0,0))
    ax.add_feature(shape_feature)
    ax.add_feature(cf.BORDERS)
    ax.set_xticks([15.5, 16, 16.5, 17], crs=ccrs.PlateCarree())
    ax.set_yticks([47.5, 48, 48.5, 49], crs=ccrs.PlateCarree())
    plt.savefig("/home/heidit/ATMENV/MAPS/HCHO_ts_fixedscale/HCHO"+str(date))
    date = date + datetime.timedelta(hours=1)
    plt.clf()
    #plt.show()

exit()

def EmisSEEDS(foldername):
    files = os.listdir(foldername)
    files = sorted(files)
    dateaxis=[]
    Emis_noontime=[]
    #index_lat = 202  #LAT 48.25°N
    #index_lon = 422 #LON 16.25°E (city rim to Wienerwald) or 421: LON 16.15°E (middle Wienerwald)
    for i in range(len(files)):
        day = str(files[i][-5:-3])  # splitlistcomp[3:4]
        month = str(files[i][-7:-5])  # splitlistcomp[2:3]
        year = "20" + str(files[i][-9:-7])  # splitlistcomp[:2]
        #print(day,month,year)
        date = datetime.datetime(year=int(year), month=int(month), day=int(day))
        #print(date)
        dateaxis.append(date)
        path = foldername+files[i]
        infile = netcdf_dataset(path)  #path.decode('UTF-8')  #OSError: [Errno -51] NetCDF: Unknown file format: b'/windata/DATA/models/nilu/MEGAN3_SURFEX_SEEDS/MEGAN/ol/MGNOUT_CAMS_BIG_20190803.nc'
        Emis = infile.variables['Emiss'][8:14, 192:212, 413:433, 0]#182:222, 402:442, # ,152:252,372:472,0]# ]  #TODO: only first emission layer (ISO) read in
        Emis_noon = Emis.mean(axis=0)
        Emis_noontime.append(Emis_noon)
    Emis_noontime = pd.DataFrame({'datetime': dateaxis, 'ISO': Emis_noontime})
    Emis_noontime['datetime'] = pd.to_datetime(Emis_noontime['datetime'])
    Emis_noontime = Emis_noontime.set_index(['datetime'])
    Emis_June = Emis_noontime[datetime.datetime(2019,6,1):datetime.datetime(2019,6,30)]
    Emis_June = Emis_June.resample("M").mean()
    Emis06 = Emis_June.ISO.values[0]
    Emis_July = Emis_noontime[datetime.datetime(2019, 7, 1):datetime.datetime(2019, 7, 31)].resample("M").mean()
    Emis_Aug = Emis_noontime[datetime.datetime(2019, 8, 1):datetime.datetime(2019, 8, 31)].resample("M").mean()
    Emis07 = Emis_July.ISO.values[0]
    Emis08 = Emis_Aug.ISO.values[0]
    return Emis_noontime, Emis06, Emis07, Emis08

Emis_assim_noontime, Emis06, Emis07, Emis08 = EmisSEEDS(foldername_as)

ax = plt.axes(projection=ccrs.PlateCarree())
plt.title("JUN 2019")
plt.contourf(lons, lats, Emis06, 60,
             transform=ccrs.PlateCarree())
plt.pcolor(lons,lats, Emis06, vmin=0, vmax=1.7E-8) #cmap=cm,
plt.colorbar(label="ISO [mol s-1 m-2]")
#first version: ax.set_xticks([15, 16, 17, 18], crs=ccrs.PlateCarree())
#first version: ax.set_yticks([47, 48, 49, 50], crs=ccrs.PlateCarree())
ax.set_xticks([15.5, 16, 16.5, 17], crs=ccrs.PlateCarree())
ax.set_yticks([47.5, 48, 48.5, 49], crs=ccrs.PlateCarree())
shape_feature = ShapelyFeature(Reader(filename).geometries(), crs=ccrs.PlateCarree(),edgecolor="black",facecolor=(0,0,0,0))
ax.add_feature(shape_feature)
ax.add_feature(cf.BORDERS)
plt.show()

ax = plt.axes(projection=ccrs.PlateCarree())
plt.title("JUL 2019")
plt.contourf(lons, lats, Emis07, 60,
             transform=ccrs.PlateCarree())
plt.pcolor(lons,lats, Emis07, vmin=0, vmax=1.7E-8) #cmap=cm,
plt.colorbar(label="ISO [mol s-1 m-2]")
ax.set_xticks([15.5, 16, 16.5, 17], crs=ccrs.PlateCarree())
ax.set_yticks([47.5, 48, 48.5, 49], crs=ccrs.PlateCarree())
shape_feature = ShapelyFeature(Reader(filename).geometries(), crs=ccrs.PlateCarree(),edgecolor="black",facecolor=(0,0,0,0))
ax.add_feature(shape_feature)
ax.add_feature(cf.BORDERS)
plt.show()

ax = plt.axes(projection=ccrs.PlateCarree())
plt.title("AUG 2019")
plt.contourf(lons, lats, Emis08, 60,
             transform=ccrs.PlateCarree())
plt.pcolor(lons,lats, Emis08, vmin=0, vmax=1.7E-8)
plt.colorbar(label="ISO [mol s-1 m-2]")
ax.set_xticks([15.5, 16, 16.5, 17], crs=ccrs.PlateCarree())
ax.set_yticks([47.5, 48, 48.5, 49], crs=ccrs.PlateCarree())
shape_feature = ShapelyFeature(Reader(filename).geometries(), crs=ccrs.PlateCarree(),edgecolor="black",facecolor=(0,0,0,0))
ax.add_feature(shape_feature)
ax.add_feature(cf.BORDERS)
plt.show()

