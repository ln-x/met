# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset


outpath ='/home/lnx/'
file = '/media/lnx/98C4EEA4C4EE83BA/WRF-TEB-NC_Files/2015_Teb_nonTeb/wrfout_d03_2015-07-13_12_00_00_nest_teb.nc'
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

IS, SA, WI = [],[],[]
IS_alb, SA_alb, WI_alb =[],[],[]
IS_H, SA_H, WI_H = [],[],[]
IS_LE, SA_LE, WI_LE = [],[],[]

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

 tair_IS = tair[53:60][:,83:90]   #7x7=49 -> 5 444 443m2 -> 544ha -> 5.4km2 (actual: 5.7km2)
 alb_IS = alb[53:60][:, 83:90]
 H_IS = H[53:60][:, 83:90]
 LE_IS = LE[53:60][:, 83:90]

 tair_SA = tair[61:65][:,114:120] #4x6=24 -> 2 666 666m2 -> 266ha -> 2.7kmw (actual: 240ha)
 alb_SA = alb[61:65][:, 114:120]
 H_SA = H[61:65][:, 114:120]
 LE_SA = LE[61:65][:, 114:120]

 tair_WI = tair[51:56][:,65:70]   #4x6=24 -> 2 666 666m2 -> 266ha -> 2.7kmw (actual: 240ha)
 alb_WI = alb[51:56][:, 65:70]
 H_WI = H[51:56][:,65:70]
 LE_WI = LE[51:56][:,65:70]

 IS_mn = np.average(np.hstack(tair_IS))
 SA_mn = np.average(np.hstack(tair_SA))
 WI_mn = np.average(np.hstack(tair_WI))
 IS_alb_mn = np.average(np.hstack(alb_IS))
 IS_H_mn = np.average(np.hstack(H_IS))
 IS_LE_mn = np.average(np.hstack(LE_IS))
 SA_alb_mn = np.average(np.hstack(alb_SA))
 SA_H_mn = np.average(np.hstack(H_SA))
 SA_LE_mn = np.average(np.hstack(LE_SA))
 WI_alb_mn = np.average(np.hstack(alb_WI))
 WI_H_mn = np.average(np.hstack(H_WI))
 WI_LE_mn = np.average(np.hstack(LE_WI))

#c_a = np.average(np.hstack(tair_regionC))- np.average(np.hstack(tair_regionAg))
 IS.append(IS_mn)
 SA.append(SA_mn)
 WI.append(WI_mn)
 IS_alb.append(IS_alb_mn)
 IS_H.append(IS_H_mn)
 IS_LE.append(IS_LE_mn)
 SA_alb.append(SA_alb_mn)
 SA_H.append(SA_H_mn)
 SA_LE.append(SA_LE_mn)
 WI_alb.append(WI_alb_mn)
 WI_H.append(WI_H_mn)
 WI_LE.append(WI_LE_mn)

time =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23] #UTC

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

major_ticks = np.arange(0, 23, 6)
minor_ticks = np.arange(0, 23, 3)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.plot(time,IS, color="red", label="Innere Stadt")
ax.plot(time,SA, color="blue", label="Seestadt Aspern")
ax.plot(time,WI, color="green", label="Wiental")
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
ax.plot(time, SA_alb, color="blue", label="Innere Stadt")
ax.plot(time, WI_alb, color="green", label="Wiental")
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
ax.plot(time, IS_H, color="red", label="Innere Stadt")
ax.plot(time, SA_H, color="blue", label="Seestadt Aspern")
ax.plot(time, WI_H, color="green", label="Wiental")
ax.set_ylabel("Sensible Heat flux $W/m2$")
ax.legend(loc='upper left')
#ax.set_xlim(0, 23)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

major_ticks = np.arange(0, 23, 6)
minor_ticks = np.arange(0, 23, 3)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.plot(time, IS_LE, color="red", label="Innere Stadt")
ax.plot(time, SA_LE, color="blue", label="Seestadt Aspern")
ax.plot(time, WI_LE, color="green", label="Wiental")
ax.set_ylabel("Latent Heat Flux $W/m2$")
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