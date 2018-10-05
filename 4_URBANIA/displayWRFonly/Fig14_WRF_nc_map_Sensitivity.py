# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import sys

outpath ='/media/lnx/Norskehavet/WRF-TEB-NC_Files/201708/Sensitivity_Runs/'
file = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201708/Sensitivity_Runs/Ref-run/wrfout_d03_2017-07-31_18_00_00.nc'
file2 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201708/Sensitivity_Runs/3b-Sensitivity-run-2/wrfout_d03_2017-07-31_18_00_00.nc'
file3 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201708/Sensitivity_Runs/3c-Sensitivity-run-3/wrfout_d03_2017-07-31_18_00_00.nc'

fh = Dataset(file, mode='r')
fh2 = Dataset(file2, mode='r')
fh3 = Dataset(file3, mode='r')

'''time + 2dvariables'''
lons = fh.variables['XLONG'][1]  #lon (147x)135x174 #print len(lons), len(lons[1])
lats = fh.variables['XLAT'][1]  #lat (147x)135x174  #print len(lats), len(lats[1])

tair = fh.variables['T2'][:] #147x135x174
tair2 = fh2.variables['T2'][:] #147x135x174
tair3 = fh3.variables['T2'][:] #147x135x174

swup = fh.variables['SWUPB'][:]
swup2 = fh2.variables['SWUPB'][:]
swup3 = fh3.variables['SWUPB'][:]
swdown = fh.variables['SWDOWN'][:]
swdown2 = fh2.variables['SWDOWN'][:]
alb = fh.variables['ALBEDO'][:]
alb2 = fh2.variables['ALBEDO'][:]
alb3 = fh3.variables['ALBEDO'][:]
H = fh.variables['HFX'][:] #upward heat flux= sensible heat flux?
H2 = fh2.variables['HFX'][:] #upward heat flux= sensible heat flux?
H3 = fh3.variables['HFX'][:] #upward heat flux= sensible heat flux?


LE = fh.variables['LH'][:]
LE3 = fh3.variables['LH'][:]

lwup = fh.variables['LWUPB'][:]
lwup2 = fh2.variables['LWUPB'][:]
lwdown = fh.variables['LWDNB'][:]

tair_units = fh.variables['T2'].units
lwup_units = fh.variables['LWUPB'].units
swup_units = fh.variables['SWUPB'].units
LE_units = fh.variables['LH'].units
pblh_units = fh.variables['PBLH'].units
swdown_units = fh.variables['SWDOWN'].units

fh.close()
fh2.close()

'''>>>!!! CHECK CORRECT UNITS, TITLE, RANGE and FIGNAME'''
timestep=18
tair_diff = tair2[timestep] - tair[timestep]
m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
xi, yi = m(lons, lats)
cmap=plt.cm.get_cmap('bwr',11)  #RdBu: Red to Blue, bwr: blue white red
cs = m.pcolor(xi, yi, np.squeeze(tair_diff),cmap=cmap)
#day = int(round(timestep-6 / 24, 0))
plt.title("TC-Ref: Tair 1 Aug 2017 12 UTC")
cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
cbar.set_label(tair_units)
# plt.title(r'$\delta$ sw rad balance $\alpha_{r}:0.30-0.15$ day %s UTC %s' %(str(day), str(hour)))
#plt.clim(-2, 2)

figname = outpath + "Tair_Ref_" + str(timestep) + "_WRFTEB_Ref_2017_tair.png"
#plt.savefig(figname)
#plt.show()

#exit()

timeslices = 37
"""
for i in range(timeslices):
  tair_diff = tair2[i]-tair[i]
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(tair_diff), cmap=cmap)
  plt.title((r'$\delta$ tair TC-Ref %d') %i) #day %s UTC %s' %(str(day), str(hour)))
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(tair_units)
  plt.clim(-2,2)
  figname = outpath + "Tair_" + str(i) + "_WRFTEB_TC-Ref.png"
  plt.show()
  #plt.savefig(figname)
"""
"""
for i in range(timeslices):
  tair_diff = tair3[i]-tair[i]
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(tair_diff), cmap=cmap)
  plt.title((r'$\delta$ tair Unseal-Ref %d') %i)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(tair_units)
  plt.clim(-2,2)
  figname = outpath + "Tair_" + str(i) + "_WRFTEB_Unseal-Ref.png"
  plt.show()
"""

for i in range(timeslices):
  LE_diff = LE3[i]-LE[i]
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(LE_diff), cmap=cmap)
  plt.title((r'$\delta$ LE Unseal-Ref %d') %i)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(lwup_units)
  plt.clim(-150,150)
  figname = outpath + "LWup_" + str(i) + "_WRFTEB_Iso-Ref.png"
  plt.show()

exit()
for i in range(timeslices):
  lwup_diff = lwup2[i] -lwup[i]
  #Q_diff = (swdown2-swup2[i])-(swdown[i]-swup[i])
  m = Basemap(width=57943,height=44955,\
            rsphere=(6378137.00,6356752.3142),\
            projection='lcc',\
            lat_1=30.,lat_2=60.,\
            lat_0=48.24166,\
            lon_0=16.37247,\
            resolution='l')
  xi, yi = m(lons, lats)
  cmap = plt.cm.get_cmap('bwr', 11)  # RdBu: Red to Blue, bwr: blue white red
  cs = m.pcolor(xi,yi,np.squeeze(lwup_diff), cmap=cmap)
  plt.title((r'$\delta$ lwup Iso-Ref %d') %i)
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(swup_units)
  plt.clim(-15,15)
  #figname = outpath + "swup_" + str(i) + "_WRFTEB_Unseal-Ref.png"
  plt.show()




