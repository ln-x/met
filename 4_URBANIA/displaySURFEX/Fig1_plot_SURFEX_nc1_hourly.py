# -*- coding: utf-8 -*-
__author__ = 'lnx'

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import csv
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S12_FORC_WRF_333_STQ_2DURBPARAM_long_corr/SURF_ATM_DIAGNOSTICS.OUT.nc'
file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S14/SURF_ATM_DIAGNOSTICS.OUT.nc'
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/DIFF_S4_S0_SURF_ATM_D.nc'
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S0_FORC_WRF_333_STQ_long/SURF_ATM_DIAGNOSTICS.OUT.nc'
#file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S3_LNX_WRF_333_nGD/SURF_ATM_DIAGNOSTICS.OUT.nc'
#file = '/home/lnx/MODELS/SURFEX/3_input/met_forcing/FORCING_new.nc'
outputpath = '/home/lnx/Documents/_Urbania/2018_EGU/DIURNALCYCLE/S2/'
fh = Dataset(file, mode='r')
lons = fh.variables['xx'][:]  #lon
lats = fh.variables['yy'][:]  #lat

'''CONVERSTION TO CELSIUS'''
def Kelvin_to_Celsius(tair):
    tairC = tair.copy()
    for i in range(len(tair)):
        for j in range(len(tair[i])):
            tairC[i][j] = tair[i][j] - 273.15
    return tairC

tairC_units = (u"°C")
index = 55
var = []

'''READ DATA AND CONVERT TO CELSIUS'''
for i in range(24):
    print i, index
    name = "tairC"+ str(i)+"UTC"
    #print name
    name = fh.variables['T2M'][index]
    #print name
    name = Kelvin_to_Celsius(name)
    var.append(name)
    index +=1

#print var
fh.close()

'''CONVERSION TO LATLON, SETUP BASEMAP'''
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

m.drawparallels(np.arange(44.0, 50., 0.1), labels=[1,0,0,0], fontsize=10, linewidth=0.)
m.drawmeridians(np.arange(14.0, 17., 0.2), labels=[0,0,0,1], fontsize=10, linewidth=0.)

lon, lat = np.meshgrid(lons2, lats2)
xi, yi = m(lon, lat)

UTC = 0

'''PLOTTING'''
for i in var:
    print i
    cs = m.pcolor(xi,yi,np.squeeze(i))
    cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
    cbar.set_label(tairC_units)
    plt.title('2m Air Temperature STQ 2015-07-20 UTC %s' % str(UTC))
    plt.clim(21,35)
    figname = outputpath + str(UTC)+ ".png"
    plt.savefig(figname)
    UTC +=1
    #plt.show()
