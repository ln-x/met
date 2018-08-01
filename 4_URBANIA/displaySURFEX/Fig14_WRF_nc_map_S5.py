# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import sys

outpath ='/home/lnx/'
file = '/media/lnx/98C4EEA4C4EE83BA/WRF-TEB-NC_Files/2017_Teb/wrfout_d03_2017-07-27_00_00_00_joined.nc'
file2 = '/media/lnx/Norskehavet/2050_S5/wrfout_d03_2017-07-27_00_00_00_2050LU'

fh = Dataset(file, mode='r')
fh2 = Dataset(file2, mode='r')

'''time + 2dvariables'''
lons = fh.variables['XLONG'][1]  #lon (147x)135x174
lats = fh.variables['XLAT'][1]  #lat (147x)135x174
tair = fh.variables['T2'][:] #147x135x174
tair2 = fh2.variables['T2'][:] #147x135x174

swup = fh.variables['SWUPB']
swup2 = fh2.variables['SWUPB']
swdown = fh.variables['SWDOWN']
swdown2 = fh2.variables['SWDOWN']

tair_units = fh.variables['T2'].units
swfx_units = fh.variables['SWUPB'].units
pblh_units = fh.variables['PBLH'].units
swdown_units = fh.variables['SWDOWN'].units

fh.close()
fh2.close()

#diff = (swup1[12]-swdown1[12]) - (swdown2[12]-swup2[12])
#print len(diff[1])

#print tair4[36]-tair5[36]
#print tair5[36][40][30:40]

#exit()

'''>>>!!! CHECK CORRECT UNITS, TITLE, RANGE and FIGNAME'''

timeslices = 72
UTC=0
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
  cs = m.pcolor(xi,yi,np.squeeze(tair_diff))
  hour = UTC % 24
  day = int(round(UTC/24, 0))
  UTC += 1
  plt.title(r'$\delta$ tair sprawl day %s UTC %s' %(str(day), str(hour)))
  #cs = m.pcolor(xi,yi,np.squeeze(rad_diff))
  cbar = m.colorbar(cs, location='bottom', pad="10%", extend="both")
  cbar.set_label(tair_units)
  #cbar.set_label(swfx_units)
  #cbar.set_label(pblh_units)

  #plt.title(r'$\delta$ sw rad balance $\alpha_{r}:0.30-0.15$ day %s UTC %s' %(str(day), str(hour)))
  plt.clim(-2,2)
  #plt.clim(-2,80)
  figname = outpath + "S5_dTair/" + str(i) + "WRFTEB_S5_2017_dtair.png"
  plt.savefig(figname)
  #plt.show()






