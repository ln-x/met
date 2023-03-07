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

# get the path of the file. It can be found in the repo data directory.
#fname = os.path.join(config["repo_data_dir"],
#                     'netcdf', 'HadISST1_SST_update.nc'
#                     )
filename = r'/windata/DATA/DATAGEO/4_Vienna/CityBorderVienna.shp' #_Austria/Verwaltungsgrenzen/2_raw/BEZIRKSGRENZEOGD/BEZIRKSGRENZEOGDPolygon.shp'  #r'./shapefile/ba_cities.shp'
foldername_as = "/data1/models/nilu/SEEDS/MEGAN/2019/ol/ISOP/"
fname = "/data1/models/nilu/SEEDS/MEGAN/2019/ol/ISOP/MGNOUT_CAMS_BIG_ISOP_20190601.nc"
dataset = netcdf_dataset(fname)
#find good region
#mark Vienna
#make daily average
#make monthly average
#TODO make subplot graph
#fix colorbar
#TODO make hourly plots of peak days

#First smaller version:
#lats = dataset.variables['lat'][182:222]#[152:252]#
#lons = dataset.variables['lon'][402:442]#[372:472]

lats = dataset.variables['lat'][192:212]#[152:252]#
lons = dataset.variables['lon'][413:433]#[372:472]


#print(dataset.variables['lat'][196],dataset.variables['lon'][427]) #  202/422 Vienna 198/425 Eisenstadt #200/425 ~20km SE Vienna Schwadorf

#ISO = dataset.variables['Emiss'][8:14,152:252,372:472,0]#[8:14, 182:222, 402:442, 0] #time(0-23), lat, lon, layer0 = ISO
#ISO = ISO.mean(axis=0)
#ax = plt.axes(projection=ccrs.PlateCarree())
#plt.contourf(lons, lats, ISO, 60,
#             transform=ccrs.PlateCarree())
#plt.pcolor(ISO, vmin=0, vmax=2.2E-8)
#plt.colorbar(label="ISO [mol s-1 m-2]")
#ax.coastlines()
#plt.show()

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



def EmisSEEDS(foldername):
    files = os.listdir(foldername)
    files = sorted(files)
    dateaxis=[]
    SM=[]
    for i in range(len(files)):
        day = str(files[i][-5:-3])
        month = str(files[i][-7:-5])
        year = "20" + str(files[i][-9:-7])
        date = datetime.datetime(year=int(year), month=int(month), day=int(day))
        dateaxis.append(date)
        path = foldername+files[i]
        infile = netcdf_dataset(path)
        SM_h = infile.variables['WG5_ISBA'][:,192:212,413:433]# 182:222, 402:442, 0]
        SM_d = SM_h.mean(axis=0)
        SM.append(SM_d)
    SM = pd.DataFrame({'datetime': dateaxis, 'SM': SM})
    SM['datetime'] = pd.to_datetime(SM['datetime'])
    SM = SM.set_index(['datetime'])
    SM_June = SM[datetime.datetime(2019,6,1):datetime.datetime(2019,6,30)]
    SM_June = SM_June.resample("M").mean()
    SM06 = SM_June.SM.values[0]
    SM_July = SM[datetime.datetime(2019, 7, 1):datetime.datetime(2019, 7, 31)].resample("M").mean()
    SM_Aug = SM[datetime.datetime(2019, 8, 1):datetime.datetime(2019, 8, 31)].resample("M").mean()
    SM07 = SM_July.SM.values[0]
    SM08 = SM_Aug.SM.values[0]
    return SM, SM06, SM07, SM08

#lats = dataset.variables['lat'][182:222]#[152:252]
#lons = dataset.variables['lon'][402:442]#[372:472]
foldername_sm = "/data1/models/nilu/SEEDS/SM_rootlevel_SURFEX/"
SM, SM06, SM07, SM08 = EmisSEEDS(foldername_sm)

ax = plt.axes(projection=ccrs.PlateCarree())
plt.title("JUN 2019")
plt.contourf(lons, lats, SM06, 60,
             transform=ccrs.PlateCarree())
plt.pcolor(lons,lats, SM06, vmin=0.1, vmax=0.5, cmap="gist_rainbow") #cmap=cm,
plt.colorbar(label="SM [m3 m-3]")
ax.set_xticks([15.5, 16, 16.5, 17], crs=ccrs.PlateCarree())
ax.set_yticks([47.5, 48, 48.5, 49], crs=ccrs.PlateCarree())

# Add city borders
shape_feature = ShapelyFeature(Reader(filename).geometries(), crs=ccrs.PlateCarree(), edgecolor="black",facecolor=(0,0,0,0))#,
                               #linewidth = 1, facecolor = (1, 1, 1, 0),
                               #edgecolor = (0.5, 0.5, 0.5, 1))
ax.add_feature(shape_feature)
ax.add_feature(cf.BORDERS)
#ax.plot(lons[20], lats[20], marker='x', markersize=9, color='black')
#ax.text(lons[20] - 3, lats[20] - 12, 'Vienna',
#         horizontalalignment='right')#,
         #transform=ccrs.Geodetic())
#index_lat = 202  # CAMS European grid
#index_lon = 422  # CAMS European grid
#ax.coastlines()
plt.show()

ax = plt.axes(projection=ccrs.PlateCarree())
plt.title("JUL 2019")
plt.contourf(lons, lats, SM07, 60,
             transform=ccrs.PlateCarree())
plt.pcolor(lons,lats, SM07, vmin=0.1, vmax=0.5, cmap="gist_rainbow")
plt.colorbar(label="SM [m3 m-3]")
ax.set_xticks([15.5, 16, 16.5, 17], crs=ccrs.PlateCarree())
ax.set_yticks([47.5, 48, 48.5, 49], crs=ccrs.PlateCarree())
shape_feature = ShapelyFeature(Reader(filename).geometries(), crs=ccrs.PlateCarree(),edgecolor="black",facecolor=(0,0,0,0))
ax.add_feature(shape_feature)
ax.add_feature(cf.BORDERS)
plt.show()

ax = plt.axes(projection=ccrs.PlateCarree())
plt.title("AUG 2019")
plt.contourf(lons, lats, SM08, 60,
             transform=ccrs.PlateCarree())
plt.pcolor(lons,lats, SM08, vmin=0.1, vmax=0.5, cmap="gist_rainbow")
plt.colorbar(label="SM [m3 m-3]")
ax.set_xticks([15.5, 16, 16.5, 17], crs=ccrs.PlateCarree())
ax.set_yticks([47.5, 48, 48.5, 49], crs=ccrs.PlateCarree())
shape_feature = ShapelyFeature(Reader(filename).geometries(), crs=ccrs.PlateCarree(),edgecolor="black",facecolor=(0,0,0,0))
ax.add_feature(shape_feature)
ax.add_feature(cf.BORDERS)
plt.show()



exit()

#[[7.66445361e-10 4.55313098e-09 1.34761546e-09 ... 1.62722630e-09
#  2.19621045e-09 3.84281000e-09]
# [2.49007957e-09 2.44786045e-09 0.00000000e+00 ... 1.31786287e-09
#  2.02072936e-09 2.53268954e-09]
# [1.40574632e-09 2.94640475e-09 3.98697016e-09 ... 1.90651350e-09
#  5.91532342e-10 5.91933567e-10]
# ...
# [1.56814284e-09 2.71923310e-09 8.68355499e-09 ... 5.15626935e-10
#  2.02216549e-09 9.57089102e-10]
# [6.85682970e-09 6.28069086e-09 1.84519254e-09 ... 2.18366869e-09
#  2.63462744e-09 5.45618273e-10]
# [2.42327663e-09 4.59725017e-09 9.24283894e-09 ... 3.46558449e-09
#  3.90241423e-10 4.50662596e-09]]
'''This file plots 2D maps of MEGAN isoprene  
This is an adapted version of the script, for all comments see Fig4_plotSURFFEXDIFF_nc1.py
For hourly loop look at Fig5_plotSURFEX_nc1_hourly.py'''
file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/_S13/SURF_ATM_DIAGNOSTICS.OUT.nc'
file2 = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/_S20_ALB/SURF_ATM_DIAGNOSTICS.OUT.nc'
fh = Dataset(file, mode='r')
fh2 = Dataset(file2, mode='r')
# 22.7.0h [103],6h[109], 12h [115],                           18h [121]
hour = 12
index = 103+hour

lons = fh.variables['xx'][:]  #lon
lats = fh.variables['yy'][:]  #lat

RN0 = fh.variables['RN'][:] #270(time)x135(lon)x174(lat)
H0 = fh.variables['H'][:] #270(time)x135(lon)x174(lat)
LE0 = fh.variables['LE'][:] #270(time)x135(lon)x174(lat)
GFLUX0 = fh.variables['GFLUX'][:] #270(time)x135(lon)x174(lat)
tair0 = fh.variables['T2M'][:] #270(time)x135(lon)x174(lat)

RN20 = fh2.variables['RN'][:] #270(time)x135(lon)x174(lat)
H20 = fh2.variables['H'][:] #270(time)x135(lon)x174(lat)
LE20 = fh2.variables['LE'][:] #270(time)x135(lon)x174(lat)
GFLUX20 = fh2.variables['GFLUX'][:] #270(time)x135(lon)x174(lat)
tair20 = fh2.variables['T2M'][:] #270(time)x135(lon)x174(lat)

RN = fh.variables['RN'][index]
H = fh.variables['H'][index]
LE = fh.variables['LE'][index]
GFLUX = fh.variables['GFLUX'][index]

RN2 = fh2.variables['RN'][index]
H2 = fh2.variables['H'][index]
LE2 = fh2.variables['LE'][index]
GFLUX2 = fh2.variables['GFLUX'][index]

dRN0 = RN20 - RN0
dH0 = H20 - H0
dLE0 = LE20 - LE0
dGFLUX0 = GFLUX20 - GFLUX0

dRN = RN2 - RN
dH = H2 - H
dLE = LE2 - LE
dGFLUX = GFLUX2 - GFLUX

tair = fh.variables['T2M'][index]
tair2 = fh2.variables['T2M'][index]

wind10m =fh.variables['W10M'][73]

heatflux_units = fh.variables['RN'].units
tair_units = fh.variables['T2M'].units
wind10m_units = fh.variables['W10M'].units

fh.close()

'''CONVERSION TO LATLON'''
lons2,lats2 =[],[]
for i in lons:
    i2 = i*0.000014038 + 15.969 - (0.000014038*333)
    lons2.append(i2)
for i in lats:
    i2 = i*0.000009355 + 48.0322418 - (0.000009355*333)
    lats2.append(i2)

m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')

lon, lat = np.meshgrid(lons2, lats2)
xi, yi = m(lon, lat)

'''Heat fluxes'''


cs = m.pcolor(xi,yi,np.squeeze(RN))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Radiation Balance Ref 2015-07-22 %s UTC' %(hour))
plt.clim(-300,1050)  #so fit all energy fluxes
plt.show()