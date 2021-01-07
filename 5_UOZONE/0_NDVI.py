# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.dates
import matplotlib.pyplot as plt
from scipy import stats
import sys
from mpl_toolkits.basemap import Basemap

file = '/media/lnx/Norskehavet/SATELLITE/NDVI/c_gls_NDVI300_201703110000_GLOBE_PROBAV_V1.0.1.nc'
file2 = '/media/lnx/Norskehavet/SATELLITE/NDVI/c_gls_NDVI300_201803110000_GLOBE_PROBAV_V1.0.1.nc'
file3 = '/media/lnx/Norskehavet/SATELLITE/NDVI/c_gls_NDVI300_201903110000_GLOBE_PROBAV_V1.0.1.nc'
file4 = '/media/lnx/Norskehavet/SATELLITE/NDVI/c_gls_NDVI300_202003110000_GLOBE_PROBAV_V1.0.1.nc'

fh = Dataset(file, mode='r')
fh2 = Dataset(file2, mode='r')
fh3 = Dataset(file3, mode='r')
fh4 = Dataset(file4, mode='r')

lons = fh.variables['lon'][1]
lats = fh.variables['lat'][1]
ndvi2017 = fh.variables['NDVI']
ndvi2018 = fh2.variables['NDVI']
ndvi2019 = fh3.variables['NDVI']
ndvi2020 = fh4.variables['NDVI']

#total gridpoints: 47040,120960 # LAT48-LON16 Furth an der Tristing - Wienerwald
WIENLAT = 10753   #from panoply != calculated: 47040 /180*(90-48)  =  10976
WIENLON = 65857   #from panoply != calculated: 120960/360*(180+16) =  65865

print ndvi2017[WIENLAT-2:WIENLAT+2,WIENLON-2:WIENLON+2]#[47040,120960]
print ndvi2018[WIENLAT-2:WIENLAT+2,WIENLON-2:WIENLON+2]#[47040,120960]
print ndvi2019[WIENLAT-2:WIENLAT+2,WIENLON-2:WIENLON+2]#[47040,120960]
print ndvi2020[WIENLAT-2:WIENLAT+2,WIENLON-2:WIENLON+2]#[47040,120960]

#ndvi_diff17 = ndvi2020 - ndvi2017

m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
xi, yi = m(lons, lats)
cmap=plt.cm.get_cmap('bwr',11)  #RdBu: Red to Blue, bwr: blue white red
cs = m.pcolor(xi, yi, np.squeeze(ndvi2017),cmap=cmap)
#day = int(round(timestep-6 / 24, 0))
plt.title("NDVI 11Mar 2020-2017")
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label("NDVI")
# plt.title(r'$\delta$ sw rad balance $\alpha_{r}:0.30-0.15$ day %s UTC %s' %(str(day), str(hour)))
#plt.clim(-2, 2)

#figname = outpath + "Tair_Ref_" + str(timestep) + "_WRFTEB_Ref_2017_tair.png"
#plt.savefig(figname)
plt.show()
#"""
#exit()

fh.close()
fh2.close()
fh3.close()
fh4.close()




