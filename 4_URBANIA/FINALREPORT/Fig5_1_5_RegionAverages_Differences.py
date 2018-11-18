# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from pylab import *

outpath ='/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/'
file = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/Ref_Heidi_Lu_2015_1stRun/wrfout_d03_2015-08-05_18_00_00.nc'
file1 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/Sprawl_2050_2ndRun/wrfout_d03_2015-08-05_18_00_00.nc'
file2 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/Dense_2050_3rdRun_Optimized_city/wrfout_d03_2015-08-05_18_00_00.nc'

f = Dataset(file, mode='r')
lon = f.variables['XLONG'][1]  # lon (199x)135x174
lat = f.variables['XLAT'][1]  # lat (199x)135x174
f.close()

CE, NO, SA, RU, SE, SX, SI, VW, WE = [],[],[],[],[],[],[],[],[]
CE1, NO1, SA1, RU1, SE1, SX1, SI1, VW1, WE1 = [],[],[],[],[],[],[],[],[]
CE2, NO2, SA2, RU2, SE2, SX2, SI2, VW2, WE2 = [],[],[],[],[],[],[],[],[]

for i in range(0,199,1):
 f = Dataset(file, mode='r')
 f1 = Dataset(file1, mode='r')
 f2 = Dataset(file2, mode='r')
 tair_units = f.variables['T2'].units
 tair = f.variables['T2'][i]
 tair1 = f1.variables['T2'][i]
 tair2 = f2.variables['T2'][i]

 f.close()
 f1.close()
 f2.close()

 #print tair[50:59].shape
 #exit()

 CE.append(np.average(np.hstack(tair[50:59][:, 80:89])))
 RU.append(np.average(np.hstack(tair[57:66][:, 128:137])))
 SA.append(np.average(np.hstack(tair[58:67][:, 109:118])))

 CE1.append(np.average(np.hstack(tair1[50:59][:, 80:89])))
 RU1.append(np.average(np.hstack(tair1[57:66][:, 128:137])))
 SA1.append(np.average(np.hstack(tair1[58:67][:, 109:118])))

 CE2.append(np.average(np.hstack(tair2[50:59][:, 80:89])))
 RU2.append(np.average(np.hstack(tair2[57:66][:, 128:137])))
 SA2.append(np.average(np.hstack(tair2[58:67][:, 109:118])))

#print CE, CE1
#exit()

def difference(x,y):
 diff = []
 for i in range(len(x)):
    diff.append(x[i] - y[i])
 return diff

CEdiff_1 = difference(CE1,CE)
CEdiff_2 = difference(CE2,CE)
RUdiff_1 = difference(RU1,RU)
RUdiff_2 = difference(RU2,RU)
SAdiff_1 = difference(SA1,SA)
SAdiff_2 = difference(SA2,SA)

time = range(0,199,1)
#"""
fig_tair = plt.figure()
major_ticks = np.arange(0, 199, 6)
minor_ticks = np.arange(0, 199, 3)
plt.xticks(major_ticks)

#plt.xticks(minor_ticks)
#plt.plot(time,ISdiff_DenseIso, color="black", label="Dense-Iso")
plt.plot(time,CEdiff_1, color="red", label="Center, Spr-Ref")
plt.plot(time,CEdiff_2, color="red", label="Center, Opt-Ref", linestyle=":")
plt.plot(time,RUdiff_1, color="green", label="Rural, Spr-Ref")
plt.plot(time,RUdiff_2, color="green", label="Rural, Opt-Ref", linestyle=":")
plt.plot(time,SAdiff_1, color="blue", label="Seestadt, Spr-Ref")
plt.plot(time,SAdiff_2, color="blue", label="Seestadt, Opt-Ref", linestyle=":")
plt.axhline(y=0.000, color="black")#, xmin=0, xmax=1, hold=None, linewidth=2)
plt.axvline(x=10.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=17.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=25.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=34.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=41.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=65.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=89.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=113.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=137.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)

plt.ylabel(r"$\delta T_{air_2m}$"u'[°C]')
plt.legend(loc='lower left')
plt.show()
#"""
#exit()
"""
fig_LE = plt.figure()
major_ticks = np.arange(0, 37, 6)
plt.xticks(major_ticks)
plt.plot(time,LE_IS1diff, color="black", label="Dense-Ref")
plt.plot(time,LE_IS2diff, color="blue", label="Iso-Ref")
plt.plot(time,LE_IS3diff, color="green", label="Unseal-Ref")
plt.plot(time,LE_IS4diff, color="vinolet", label="HighAlb-Ref")
plt.axhline(y=0.000, color="black")#, xmin=0, xmax=1, hold=None, linewidth=2)
plt.axvline(x=10.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=17.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=25.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=34.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.ylabel("$Latent Heat Flux [W m-2]$")
plt.legend(loc='upper right')
plt.show()
"""
"""
fig_SW = plt.figure()
major_ticks = np.arange(0, 37, 6)
plt.xticks(major_ticks)
plt.plot(time,SW_IS1diff, color="black", label="Dense-Ref")
plt.plot(time,SW_IS2diff, color="blue", label="Iso-Ref")
plt.plot(time,SW_IS3diff, color="green", label="Unseal-Ref")
plt.plot(time,SW_IS4diff, color="violet", label="HighAlb-Ref")
plt.axhline(y=0.000, color="black")#, xmin=0, xmax=1, hold=None, linewidth=2)
plt.axvline(x=10.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=17.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=25.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=34.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.ylabel("$Upward Shortwave Radiation [W m-2]$")
plt.legend(loc='upper right')
plt.show()

fig_LW = plt.figure()
major_ticks = np.arange(0, 37, 6)
plt.xticks(major_ticks)
plt.plot(time,LW_IS1diff, color="black", label="Dense-Ref")
plt.plot(time,LW_IS2diff, color="blue", label="Iso-Ref")
plt.plot(time,LW_IS3diff, color="green", label="Unseal-Ref")
plt.plot(time,LW_IS4diff, color="violet", label="HighAlb-Ref")
plt.axhline(y=0.000, color="black")#, xmin=0, xmax=1, hold=None, linewidth=2)
plt.axvline(x=10.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=17.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=25.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=34.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.ylabel("$Upward Long Wave Radiation [W m-2]$")
plt.legend(loc='upper right')
plt.show()
#"""
exit()


fig2, axs = plt.subplots(2,2)
major_ticks = np.arange(0, 37, 6)
axs[0,0].set_xticks(major_ticks)
axs[0,0].plot(time,IS, color="red", label="Ref")
axs[0,0].plot(time,IS1, color="blue", label="Dense")
axs[0,0].set_ylabel(r"$T_{air_2m}$"u'[°C]')
axs[0,0].legend(loc='upper right')

axs[1,0].set_xticks(major_ticks)
axs[1,0].plot(time,IS, color="red", label="Ref")
axs[1,0].plot(time,IS2, color="blue", label="Iso")
axs[1,0].set_xlabel("hours [UTC]")
axs[1,0].set_ylabel(r"$T_{air_2m}$"u'[°C]')
axs[1,0].legend(loc='upper right')

axs[0,1].set_xticks(major_ticks)
axs[0,1].plot(time,IS, color="red", label="Ref")
axs[0,1].plot(time,IS3, color="blue", label="Unseal")
axs[0,1].set_ylabel(r"$T_{air_2m}$"u'[°C]')
axs[0,1].legend(loc='upper right')

axs[1,1].set_xticks(major_ticks)
axs[1,1].plot(time,IS, color="red", label="Ref")
axs[1,1].plot(time,IS4, color="blue", label="Alb")
axs[1,1].set_xlabel("hours [UTC]")
axs[1,1].set_ylabel(r"$T_{air_2m}$"u'[°C]')
axs[1,1].legend(loc='upper right')
#axs[1,1].legend(loc='upper left')
plt.show()
#"""

#exit()
#WT_2030_1a = transpose(np.array([WT_1a_2030_V0,WT_1a_2030,WT_1a_2030_V100]))
Tair= transpose(np.array([IS,SA,WI]))
ALB= transpose(np.array([IS_alb,SA_alb,WI_alb]))
SHFX= transpose(np.array([IS_H,SA_H,WI_H]))
LHFX= transpose(np.array([IS_LE,SA_LE,WI_LE]))
#print len(ALB), ALB.shape
#exit()
labels = ["IS","SA","WI"]

fig3, axs = plt.subplots(2,2)

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