# -*- coding: utf-8 -*-
__author__ = 'lnx'

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import csv

'''This file plots 2D maps of SURFEX.nc files.  
This is the cleaned version of the script, for all comments see Fig4_plotSURFFEXDIFF_nc1.py
For hourly loop look at Fig5_plotSURFEX_nc1_hourly.py'''

file = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S12/TEB_DIAGNOSTICS.OUT.nc'
file2 = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S13/TEB_DIAGNOSTICS.OUT.nc'
fileREF = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S15_XUNIF/TEB_DIAGNOSTICS.OUT.nc'
fileS2 = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S16_XUNIF/TEB_DIAGNOSTICS.OUT.nc'
fileS3 = '/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/S17_XUNIF/TEB_DIAGNOSTICS.OUT.nc'

#file = '/home/lnx/MODELS/SURFEX/3_input/met_forcing/FORCING_new.nc'
fh = Dataset(file, mode='r')
fh2 = Dataset(file2, mode='r')
fhref= Dataset(fileREF, mode='r')
fhs2 = Dataset(fileS2, mode='r')
fhs3 = Dataset(fileS3, mode='r')

lons = fh.variables['xx'][:]  #lon
lats = fh.variables['yy'][:]  #lat
RN = fh.variables['RN_TEB'][73]
H = fh.variables['H_TEB'][73]
LE = fh.variables['LE_TEB'][73]
GFLUX = fh.variables['GFLUX_TEB'][73]
UTCIsun = fh.variables['UTCI_OUTSUN'][121]
UTCIshade = fh.variables['UTCI_OUTSHAD'][121]
UTCIsun2 = fh2.variables['UTCI_OUTSUN'][121]
UTCIshade2 = fh2.variables['UTCI_OUTSHAD'][121]

UTCIsunREF = fhref.variables['UTCI_OUTSUN'][115]
UTCIsunS2 = fhs2.variables['UTCI_OUTSUN'][115]
UTCIsunS3 = fhs3.variables['UTCI_OUTSUN'][115]
UTCIshadeREF = fhref.variables['UTCI_OUTSHAD'][121]
UTCIshadeS2 = fhs2.variables['UTCI_OUTSHAD'][121]
UTCIshadeS3 = fhs3.variables['UTCI_OUTSHAD'][121]
#starts at 17.7.18hUTC [0], hourly ->
# 18.7.0h [7],6h[13], 12h [19], 14h [21], 18h [42], 6h [54]
# 20.7.  0h[55], 5h[60], 6h[61], 12h [67], 14h[69], HOTTEST 15h[70], 18h [73]
# 22.7.  0h[103], 6h[109], 12h [115], 18h [121]
heatflux_units = fh.variables['RN_TEB'].units


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


'''UTCI'''

cs = m.pcolor(xi,yi,np.squeeze(UTCIsunREF))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIsun STQ 2015-07-22 12UTC')
plt.clim(40,50)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(UTCIsunS2))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIsun S2 2015-07-22 12UTC')
plt.clim(40,50)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(UTCIsunS3))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIsun S3 2015-07-22 12UTC')
plt.clim(40,50)
plt.show()

exit()

cs = m.pcolor(xi,yi,np.squeeze(UTCIshadeREF))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIshade STQ 2015-07-22 18UTC')
plt.clim(20,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(UTCIshadeS2))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIshade S2 2015-07-22 18UTC')
plt.clim(20,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(UTCIshadeS3))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIshade S3 2015-07-22 18UTC')
plt.clim(20,35)
plt.show()

exit()


dUTCIsun = UTCIsun2-UTCIsun
dUTCIshade = UTCIshade2-UTCIshade

cs = m.pcolor(xi,yi,np.squeeze(UTCIsun))#,cmap=cmap)
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIsun STQ 2015-07-22 18UTC')
plt.clim(20,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(UTCIshade))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIshade STQ 2015-07-22 18UTC')
plt.clim(20,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dUTCIsun))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIsun S1-STQ 2015-07-22 18UTC')
plt.clim(-0.5,0.5)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(dUTCIshade))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(u"°C")
plt.title('UTCIshade S1-STQ 2015-07-22 18UTC')
plt.clim(-0.5,0.5)
plt.show()

exit()

'''Heat fluxes'''

cs = m.pcolor(xi,yi,np.squeeze(RN))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Radiation Balance STQ 2015-07-20 18UTC')
#plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(GFLUX))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Ground Heat Flux STQ 2015-07-20 18UTC')
#plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(H))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Sensible Heat Flux STQ 2015-07-20 18UTC')
#plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(LE))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(heatflux_units)
plt.title('Latent Heat Flux STQ 2015-07-20 18 UTC')
#plt.clim(21,35)
plt.show()

'''Air temperature'''

#cs = m.pcolor(xi,yi,np.squeeze(tairC))
cs = m.pcolor(xi,yi,np.squeeze(tair0UTC_C))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
#cbar.set_label(tair_units)
cbar.set_label(tairC_units)
#cbar.set_label(wind10m_units)
plt.title('2m Air Temperature STQ 2015-07-20 0UTC')
#plt.title('10m Wind Speed - 2015-07-20 18UTC')
plt.clim(21,35)
plt.show()


cs = m.pcolor(xi,yi,np.squeeze(tair6UTC_C))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(tairC_units)
plt.title('2m Air Temperature STQ 2015-07-20 6UTC')
plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(tair12UTC_C))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(tairC_units)
plt.title('2m Air Temperature STQ 2015-07-20 12UTC')
plt.clim(21,35)
plt.show()

cs = m.pcolor(xi,yi,np.squeeze(tair18UTC_C))
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(tairC_units)
plt.title('2m Air Temperature STQ 2015-07-20 18UTC')
plt.clim(21,35)
plt.show()


