# -*- coding: utf-8 -*-
__author__ = 'lnx'

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
file = '/home/lnx/MODELS/WRF/3_testdata/Urbania/Tair_d03.nc'
fh = Dataset(file, mode='r')

'''2dvariables'''
lons = fh.variables['lon'][:]  #lon
lats = fh.variables['lat'][:]  #lat
LU =fh.variables['LU']
terrain =fh.variables['HGT']
'''3dvariables'''
tair = fh.variables['Tair']
tair0UTC = fh.variables['Tair'][55]
tair6UTC = fh.variables['Tair'][61]
tair12UTC = fh.variables['Tair'][67]
tair18UTC = fh.variables['Tair'][73]
RH =fh.variables['RH']
Xwind =fh.variables['U']
Ywind =fh.variables['V']
Zwind =fh.variables['W']

height = range(0,39,1) #len 39
height = np.array(height)
width = lats[:,72]   #len 135
terrainvalues = terrain[:,72]   #len 135
print terrainvalues/40

tairvalues = tair[67,:,:,150] #39x135, type: numpy ndarray
rhvalues = RH[67,:,:,150] #39x135, type: numpy ndarray
#print tair[67,:,120,150] #[104 x 39 x 135 x 174] t - z -y - x ; z=0 ...lowest level; x,y=0 -> left lower corner
tair_units = fh.variables['Tair'].units
fh.close()

X, Y = np.meshgrid(width, height)
Z = np.ma.array(tairvalues)  #39x135, numpy.ma.core.MaskedArray
CS = plt.contourf(X, Y, Z, 25,
                  #[-1, -0.1, 0, 0.1],
                  alpha=1)
                  #cmap=plt.cm.bone)
                  #origin=origin)

plt.title(u'air temperature [°C]') #r"$T_{air_2m}$"u'[°C]'
plt.xlabel(u'latitude [°]')
plt.ylabel(r"$\sigma$ -level above ground")
cbar = plt.colorbar(CS)
plt.show()

Z1 = np.ma.array(rhvalues)  #39x135, numpy.ma.core.MaskedArray
CS1 = plt.contourf(X, Y, Z1, 25)
                  #[-1, -0.1, 0, 0.1],
                  #alpha=0.5,
                  #cmap=plt.cm.bone,
                  #origin=origin)

plt.title(u'relative humidity [%]')
plt.xlabel(u'latitude [°]')
plt.ylabel(r"$\sigma$ -level above ground")
cbar = plt.colorbar(CS1)
plt.show()


figure=plt.figure()
plt.plot(terrainvalues/40)
plt.show()
exit()
