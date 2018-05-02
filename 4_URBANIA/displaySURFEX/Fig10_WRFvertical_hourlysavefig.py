# -*- coding: utf-8 -*-
__author__ = 'lnx'

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
file = '/home/lnx/MODELS/WRF/3_testdata/Urbania/Tair_d03.nc'
outputpath = '/home/lnx/MODELS/WRF/3_testdata/Urbania/'
fh = Dataset(file, mode='r')

'''2dvariables'''
lons = fh.variables['lon'][:]  #lon
lats = fh.variables['lat'][:]  #lat
LU =fh.variables['LU']
terrain =fh.variables['HGT']
'''3dvariables'''
tair = fh.variables['Tair']
#print tair[67,:,120,150] #[104 x 39 x 135 x 174] t - z -y - x ; z=0 ...lowest level; x,y=0 -> left lower corner
RH =fh.variables['RH']
Xwind =fh.variables['U']
Ywind =fh.variables['V']
Zwind =fh.variables['W']

height = range(0,39,1) #len 39
height = np.array(height)
width = lats[:,87]   #len 135 north/south cut
#width = lons[72,:]   #len 174 east/west cut
terrainvalues = terrain[72,:]   #len 135
#print len(width)
figure=plt.figure()
plt.plot(terrainvalues)
#plt.show()
#tairvalues = tair[55,:,:,150] #39x135, type: numpy ndarray  #67
#rhvalues = RH[55,:,:,150] #39x135, type: numpy ndarray

var = range(31,104,1) #55: 20.July 2016 0h,
#print var
#tairvalues = []
Tlevels = np.arange(-50,37.5,2.5)
RHlevels = range(0,100,5)
'''
plt.ion()
for i in var:
  plt.clf()
  print i
  #tairvalues = tair[i,:,:,87] #39x135, type: numpy ndarray  #67 north-south cut
  tairvalues = tair[i,:,72,:] #39x135, type: numpy ndarray  #67 east-west cut
  X, Y = np.meshgrid(width, height)
  Z = np.ma.array(tairvalues)  #39x135, numpy.ma.core.MaskedArray
  CS = plt.contour(X, Y, Z, Tlevels)#,
                  # colors=('k',))
                  #[-1, -0.1, 0, 0.1],
                  #alpha=1)
                  #cmap=plt.cm.bone)
                  #origin=origin)
  plt.clabel(CS, fmt='%2.1f',colors="b",fontsize=10)
  #plt.xlabel(u'latitude [°]')
  plt.xlabel(u'longitude [°]')
  plt.ylabel(r"$\sigma$ -level above ground")
  extends = ["both"]
  cbar = plt.colorbar(CS)
  cbar.ax.set_ylabel(u'air temperature [°C]') #r"$T_{air_2m}$"u'[°C]'
  #cbar = plt.colorbar(CS)
  cbar.add_lines(CS)
  figname = outputpath + "tair_" + str(i-31) + ".png"
  plt.savefig(figname)
  #plt.show()

exit()
'''
plt.ion()
for i in var:
  print i
  plt.clf()
  rhvalues = RH[i,:,:,87] #39x135, type: numpy ndarray  north-south
  #rhvalues = RH[i,:,72,:] #39x135, type: numpy ndarray east-west
  X, Y = np.meshgrid(width, height)
  Z1 = np.ma.array(rhvalues)  #39x135, numpy.ma.core.MaskedArray
  CS1 = plt.contourf(X, Y, Z1, RHlevels)
                  #[-1, -0.1, 0, 0.1],
                  #alpha=0.5,
                  #cmap=plt.cm.bone,
                  #origin=origin)
  extends = ["both"]
  cbar = plt.colorbar(CS1)
  cbar.ax.set_ylabel(u'relative humidity [%]')
  plt.xlabel(u'latitude [°]')
  #plt.xlabel(u'longitude [°]')
  plt.ylabel(r"$\sigma$ -level above ground")
  #cbar = plt.colorbar(CS1)
  figname = outputpath + "rh_"+ str(i-31) + ".png"
  plt.savefig(figname)
  #plt.show()

fh.close()
exit()