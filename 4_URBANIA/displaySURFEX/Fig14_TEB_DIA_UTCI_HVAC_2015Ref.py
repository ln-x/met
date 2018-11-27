# -*- coding: utf-8 -*-
__author__ = 'lnx'

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
#from pylab import *
import csv

'''This file plots 2D maps of SURFEX.nc files.  
This is the cleaned version of the script, for all comments see Fig4_plotSURFFEXDIFF_nc1.py
For hourly loop look at Fig5_plotSURFEX_nc1_hourly.py'''

forc = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/Ref_Heidi_Lu_2015_1stRun/wrfout_d03_2015-08-05_18_00_00.nc'
file = '/media/lnx/Norskehavet/OFFLINE/20150804_FR_Ref/SURF_ATM_DIAGNOSTICS.OUT.nc'
file1 = '/media/lnx/Norskehavet/OFFLINE/20150804_FR_Ref/TEB_DIAGNOSTICS.OUT.nc'
file2 = '/media/lnx/Norskehavet/OFFLINE/20150804_FR_Spr/TEB_DIAGNOSTICS.OUT.nc'

#f = Dataset(forc, mode='r')
fh = Dataset(file, mode='r')
fh1 = Dataset(file1, mode='r')
fh2 = Dataset(file2, mode='r')
hour = 12
index = 6+(3*24)+hour
#print index

lons = fh.variables['xx'][:]  #shape: (174,)
lats = fh.variables['yy'][:]  #shape: (135,)

Tair = fh.variables['T2M'][index]

UTCIsun = fh1.variables['UTCI_OUTSUN'][index]
UTCIshade = fh1.variables['UTCI_OUTSHAD'][index]
UTCIsun2 = fh2.variables['UTCI_OUTSUN'][index]
UTCIshade2 = fh2.variables['UTCI_OUTSHAD'][index]
HVAC = fh1.variables['HVAC_CL'][index]
HVAC2 = fh2.variables['HVAC_CL'][index]
UTCI_units = fh1.variables['UTCI_OUTSUN'].units
HVAC_units = fh1.variables['HVAC_CL'].units

fh.close()
fh2.close()

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


'''UTCI'''

dUTCIsun = UTCIsun2-UTCIsun
dUTCIshade = UTCIshade2-UTCIshade
cmap = plt.cm.get_cmap('RdBu', 11)    # 11 discrete colors

cs = m.pcolor(xi,yi,np.squeeze(Tair))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('Tair Ref 2015-08-09 12UTC')
#plt.clim(30,50)
plt.show()

#exit()


cs = m.pcolor(xi,yi,np.squeeze(UTCIsun))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIsun Ref 2015-08-09 12UTC')
#plt.clim(30,50)
plt.show()


cs = m.pcolor(xi,yi,np.squeeze(UTCIshade))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIshade Ref 2015-08-09 12UTC')
#plt.clim(30,50)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dUTCIsun))
cbar = m.colorbar(cs, cmap=cmap, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIsun Spr-Ref 2015-08-09 12UTC')
#plt.clim(-0.5,0.5)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dUTCIshade))
cbar = m.colorbar(cs, cmap=cmap, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIshade Spr-Ref 2015-08-09 12UTC')
#plt.clim(-0.5,0.5)
plt.show()
