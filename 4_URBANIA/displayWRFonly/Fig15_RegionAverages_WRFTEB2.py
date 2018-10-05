# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from pylab import *


outpath ='/media/lnx/Norskehavet/WRF-TEB-NC_Files/201708/Sensitivity_Runs/'
file = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201708/Sensitivity_Runs/Ref-run/wrfout_d03_2017-07-31_18_00_00.nc'

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

for i in range(6,37,1):
#timeslice = 57
 #print i
 f = nc.Dataset(file)
 tair = f.variables['T2'][i]
 alb  = f.variables['ALBEDO'][i]
 H = f.variables['HFX'][i] #upward heat flux= sensible heat flux?
 LE = f.variables['LH'][i]
 lon = f.variables['XLONG'][:]
 lat = f.variables['XLAT'][:]
 #print lat 333.333 666.666 ...
 #print len(tair[0]) #174 width, 135 length

#ISMASK =

 #tair_IS = np.hstack(tair[56:57][:,83])+ np.hstack(tair[55:57][:,84])+np.hstack(tair[54:58][:,85])+np.hstack(tair[54:59][:,86])+np.hstack(tair[54:57][:,87:88])+np.hstack(tair[57][:,89])

 tair_IS = []
 tair_IS.append(tair[56:58][:, 83])
 tair_IS.append(tair[55:58][:, 84])
 tair_IS.append(tair[54:59][:, 85])
 tair_IS.append(tair[54:60][:, 86])
 tair_IS.append(tair[54:58][:, 87])
 tair_IS.append(tair[54:58][:, 88])
 #tair_IS.append(tair[57][:, 89])

 tair_AS = []
 tair_AS.append(tair[60:62][:, 113])
 tair_AS.append(tair[60:65][:, 114])
 tair_AS.append(tair[60:65][:, 115])
 tair_AS.append(tair[60:65][:, 116])
 tair_AS.append(tair[63:65][:, 117])

 #print tair_IS
 #tair_IS = tair[53:60][:,83:90]   #7x7=49 -> 5 444 443m2 -> 544ha -> 5.4km2 (actual: 5.7km2)
 alb_IS = alb[53:60][:, 83:90]
 H_IS = H[53:60][:, 83:90]
 LE_IS = LE[53:60][:, 83:90]

 #tair_SA = tair[61:65][:,114:120] #4x6=24 -> 2 666 666m2 -> 266ha -> 2.7kmw (actual: 240ha)
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

time = range(0,31,1)

#"""
fig, axs = plt.subplots(2,2)

major_ticks = np.arange(0, 31, 6)
minor_ticks = np.arange(0, 31, 3)
axs[0,0].set_xticks(major_ticks)
axs[0,0].set_xticks(minor_ticks, minor=True)
axs[0,0].plot(time,IS, color="red", label="Innere Stadt")
axs[0,0].plot(time,SA, color="blue", label="Seestadt Aspern")
axs[0,0].plot(time,WI, color="green", label="Wiental")
axs[0,0].set_ylabel(r"$T_{air_2m}$"u'[°C]')
#axs[0,0].legend(loc='upper center')

axs[1,0].set_xticks(major_ticks)
axs[1,0].set_xticks(minor_ticks, minor=True)
axs[1,0].plot(time, IS_alb, color="red", label="Innere Stadt")
axs[1,0].plot(time, SA_alb, color="blue", label="Innere Stadt")
axs[1,0].plot(time, WI_alb, color="green", label="Wiental")
axs[1,0].set_xlabel("hours [UTC]")
axs[1,0].set_ylabel('$albedo [0-1]$')
#axs[1,0].legend(loc='upper left')

axs[0,1].set_xticks(major_ticks)
axs[0,1].set_xticks(minor_ticks, minor=True)
axs[0,1].plot(time, IS_H, color="red", label="Innere Stadt")
axs[0,1].plot(time, SA_H, color="blue", label="Seestadt Aspern")
axs[0,1].plot(time, WI_H, color="green", label="Wiental")
axs[0,1].set_ylabel("$Sensible Heat flux [W m-2]$")
axs[0,1].legend(loc='upper right')

axs[1,1].set_xticks(major_ticks)
axs[1,1].set_xticks(minor_ticks, minor=True)
axs[1,1].plot(time, IS_LE, color="red", label="Innere Stadt")
axs[1,1].plot(time, SA_LE, color="blue", label="Seestadt Aspern")
axs[1,1].plot(time, WI_LE, color="green", label="Wiental")
axs[1,1].set_xlabel("hours [UTC]")
axs[1,1].set_ylabel("$Latent Heat Flux [W m-2]$")
#axs[1,1].legend(loc='upper left')
plt.show()
#"""

exit()
#WT_2030_1a = transpose(np.array([WT_1a_2030_V0,WT_1a_2030,WT_1a_2030_V100]))
Tair= transpose(np.array([IS,SA,WI]))
ALB= transpose(np.array([IS_alb,SA_alb,WI_alb]))
SHFX= transpose(np.array([IS_H,SA_H,WI_H]))
LHFX= transpose(np.array([IS_LE,SA_LE,WI_LE]))
#print len(ALB), ALB.shape
#exit()
labels = ["IS","SA","WI"]

fig2, axs = plt.subplots(2,2)

axs[0,0].boxplot(Tair, notch=True, labels=labels, showfliers=True, showmeans=True)
axs[0,0].set_ylabel(r"$T_{air_2m}$"u'[°C]')

axs[1,0].boxplot(ALB,  notch=False, labels=labels, showfliers=True, showmeans=True)
axs[1,0].set_ylabel('$albedo [0-1]$')

axs[0,1].boxplot(SHFX,  notch=False, labels=labels, showfliers=True, showmeans=True)
axs[0,1].set_ylabel("$Sensible Heat flux [W m-2]$")

axs[1,1].boxplot(LHFX,  notch=False, labels=labels, showfliers=True, showmeans=True)
axs[1,1].set_ylabel("$Latent Heat Flux [W m-2]$")

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