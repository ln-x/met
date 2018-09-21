# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset


outpath ='/home/lnx/'
file = '/media/lnx/98C4EEA4C4EE83BA/WRF-TEB-NC_Files/wrfout_d03_2015-07-13_12_00_00_nest_teb.nc'
#file2 = '/media/lnx/Norskehavet/2050_S5/wrfout_d03_2017-07-27_00_00_00_2050LU'

fh = Dataset(file, mode='r')
#fh2 = Dataset(file2, mode='r')

'''time + 2dvariables'''
lons = fh.variables['XLONG'][1]  #lon (147x)135x174
lats = fh.variables['XLAT'][1]  #lat (147x)135x174
tair = fh.variables['T2'][:] #147x135x174
#tair2 = fh2.variables['T2'][:] #147x135x174

alb = fh.variables['ALBEDO'][:]
H = fh.variables['HFX'][:] #upward heat flux= sensible heat flux?
LE = fh.variables['LH'][:]

swup = fh.variables['SWUPB']
lwup = fh.variables['LWUPB']
#swup2 = fh2.variables['SWUPB']
swdown = fh.variables['SWDOWN']
lwdown = fh.variables['LWDNB']
#swdown2 = fh2.variables['SWDOWN']
tair_units = fh.variables['T2'].units
swfx_units = fh.variables['SWUPB'].units
pblh_units = fh.variables['PBLH'].units
swdown_units = fh.variables['SWDOWN'].units

fh.close()

IS, SA = [], []
IS_alb, SA_alb =[],[]
IS_H, SA_H = [],[]
IS_LE, SA_LE = [],[]

for i in range(55,79,1):   #55:0 UTC
#timeslice = 57
 print i
 f = nc.Dataset(file)
 tair = f.variables['T2'][i] #55: 0UTC, ...73:13UTC
 alb  = f.variables['ALBEDO'][i]
 H = f.variables['HFX'][i] #upward heat flux= sensible heat flux?
 LE = f.variables['LH'][i]
 lon = f.variables['XLONG'][:]
 lat = f.variables['XLAT'][:]
 #print lat 333.333 666.666 ...
 #print len(tair[0]) #174 width, 135 length

 tair_IS = tair[40:50][:,90:100]  #lat/y lon/x
 tair_SA = tair[40:50][:,90:100]  #tair_regionC = tair[40:50][:,90:100]
 alb_IS = alb[40:50][:,90:100]
 H_IS = H[40:50][:,90:100]
 LE_IS = LE[40:50][:,90:100]

 #tair_regionC = tair[80:90][:,50:60]
 #print type(tair_regionC)
 #print len(tair_regionC)
 #print "S", np.average(np.hstack(tair_regionS2))- np.average(np.hstack(tair_regionS))
 IS_mn = np.average(np.hstack(tair_IS))
 SA_mn = np.average(np.hstack(tair_SA))
 IS_alb_mn = np.average(np.hstack(alb_IS))
 IS_H_mn = np.average(np.hstack(H_IS))
 IS_LE_mn = np.average(np.hstack(LE_IS))  #cdiff1 = np.average(np.hstack(tair_regionC1)) - np.average(np.hstack(tair_regionC))
 #print "urban-rural"
 #c_a = np.average(np.hstack(tair_regionC))- np.average(np.hstack(tair_regionAg))
 IS.append(IS_mn)
 SA.append(SA_mn)
 IS_alb.append(IS_alb_mn)
 IS_H.append(IS_H_mn)
 IS_LE.append(IS_LE_mn)

time =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23] #UTC

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

major_ticks = np.arange(0, 23, 6)
minor_ticks = np.arange(0, 23, 3)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.plot(time,IS, color="red", label="Innere Stadt")
#ax.plot(time,SA, color="green", label="Seestadt Aspern")
#ax.plot(time,S, color="red", label="South_Ref")
#ax.plot(time,SS1, color="red", linestyle="dashed")
#ax.plot(time,SS2, color="red", linestyle=":")
ax.set_xlabel("hours [UTC]")
ax.set_ylabel(r"$T_{air_2m}$"u'[°C]')
ax.legend(loc='upper center')
#ax.set_xlim(0, 23)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(121)
major_ticks = np.arange(0, 23, 6)
minor_ticks = np.arange(0, 23, 3)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.plot(time, IS_alb, color="red", label="Innere Stadt")
ax.set_xlabel("hours [UTC]")
ax.set_ylabel('albedo')
ax.legend(loc='upper left')
#ax.set_xlim(0, 23)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

major_ticks = np.arange(0, 23, 6)
minor_ticks = np.arange(0, 23, 3)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.plot(time, IS_H, color="red", label="H - Innere Stadt")
ax.plot(time, IS_LE, color="blue", label="LE - Innere Stadt")
ax.set_ylabel("$W/m2$")
ax.legend(loc='upper left')
#ax.set_xlim(0, 23)
plt.show()

exit()



# select two regions
latidx1 = (lat >= (80.*333.333)) & (lat <= (100.*333.333))
lonidx1 = (lon >= (60.*333.333)) & (lon <= (40.*333.333))

# these basically listing the values in an array (2 in this case)
tairX = tair[:]
tair1 = tairX[:, latidx1][..., lonidx1]
tair_1 = tair1

# time to get the mean values
print np.mean(tair_1)
print "............."
#print np.mean(tair_2)
print "............."