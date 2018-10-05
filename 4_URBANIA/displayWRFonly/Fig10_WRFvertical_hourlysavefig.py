# -*- coding: utf-8 -*-
__author__ = 'lnx'

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.basemap import Basemap
file = '/home/lnx/MODELS/WRF/3_testdata/Urbania/Tair_d03.nc'
file2 = '/home/lnx/MODELS/WRF/3_testdata/Urbania/Tair_d03_teb.nc'
eta = '/home/lnx/MODELS/WRF/3_testdata/Urbania/levels'
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
GP = fh.variables['GP'] #geopotential m2 s-2
eth = fh.variables['ETH']

'''self-defined:width,timestep,legendstep'''
width = lats[:,87]   #len 135 north/south cut
#width = lons[72,:]  #len 174 east/west cut
var = range(31,104,1) #55: 20.July 2016 0h,
#Tlevels = np.arange(-50,37.5,2.5)
KTlevels = np.arange(223,310,2.5)

RHlevels = range(0,100,5)

'''read in eta - model levels'''
sigmalevel = range(0,39,1) #len 39
sigmalevel = np.array(sigmalevel)
with open(eta, "r") as f:  # Einlesen des Files in eine Liste
  alldata = f.readlines()
splitdata = []       #splitlistcomp = [i.split() for i in data]
for i in alldata:
    splitdata.append(i.split())
data1 = splitdata[:41]
data2 = splitdata[43:83]
eta_full40 = []
for i in range(1,41,1):
  value = float(data1[i][1])
  eta_full40.append(value)
print eta_full40
eta_half39 = []
for i in range(1,40,1):
  value = float(data2[i][1])
  eta_half39.append(value)


'''absolute height'''
terrainvalues = terrain[72,:] #len 135
#figure=plt.figure()
#plt.plot(terrainvalues)
#plt.show()
#for i in var:
 #Z = GP[i, 38, 72, :]  # 39x135, type: numpy ndarray  #67 east-west cut
 #print np.std(Z)       #np.std: lowest first level:990!, upper level:~30
 #geopot = GP[i, :, 72, 87]  # !!FIXED on one vertical profile!! #Z = GP[i, :, 72, :]
 #print len(geopot)
 #height = geopot / 9.81

#print eth[1,:,1,1]



'''potential temperature/eta '''

for i in var:
  figure=plt.figure()
  plt.xlabel(u'[°C]')
  plt.ylabel(r'model height [$\eta$]')
  plt.plot((eth[i,:,72,87]-273.15),eta_half39, label=r'$\theta_{e}$')
  plt.plot(tair[i,:,72,87],eta_half39[::-1], label=r'T')
  plt.legend()
  plt.show()

exit()

plt.ion()
for i in var:
  plt.clf()
  print i
  vpottair = eth[i,:,:,87] #39x135, type: numpy ndarray  #67 north-south cut
  #tairvalues = tair[i,:,72,:] #39x135, type: numpy ndarray  #67 east-west cut
  X, Y = np.meshgrid(width, eta_half39)
  Z = np.ma.array(vpottair)  #39x135, numpy.ma.core.MaskedArray
  CS = plt.contour(X, Y, Z)#, KTlevels)
  plt.clabel(CS, fmt='%2.1f',colors="b",fontsize=10)
  #plt.xlabel(u'latitude [°]')
  plt.xlabel(u'longitude [°]')
  plt.ylabel(r"$\eta$")
  extends = ["both"]
  cbar = plt.colorbar(CS)
  cbar.ax.set_ylabel(u'virtuel potential air temperature [°C]') #r"$T_{air_2m}$"u'[°C]'
  #cbar = plt.colorbar(CS)
  cbar.add_lines(CS)
  figname = outputpath + "vpotT_" + str(i-31) + ".png"
  plt.savefig(figname)
  #plt.show()

'''plot air temperature/sigma level'''
plt.ion()
for i in var:
  plt.clf()
  print i
  #tairvalues = tair[i,:,:,87] #39x135, type: numpy ndarray  #67 north-south cut
  tairvalues = tair[i,:,72,:] #39x135, type: numpy ndarray  #67 east-west cut
  X, Y = np.meshgrid(width, sigmalevel)
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

'''plot relative humidity/sigma level'''
plt.ion()
for i in var:
  print i
  plt.clf()
  rhvalues = RH[i,:,:,87]  #CHECK!! 9x135, type: numpy ndarray  north-south
  #rhvalues = RH[i,:,72,:] #CHECK!! 39x135, type: numpy ndarray east-west
  X, Y = np.meshgrid(width, sigmalevel)
  Z1 = np.ma.array(rhvalues)  #39x135, numpy.ma.core.MaskedArray
  CS1 = plt.contourf(X, Y, Z1, RHlevels)
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


