# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from pylab import *

IS,IS1,IS2,IS3,IS4 = [],[],[],[],[]
IS_LE,IS1_LE,IS2_LE,IS3_LE,IS4_LE = [],[],[],[],[]
IS_SW,IS1_SW,IS2_SW,IS3_SW,IS4_SW = [],[],[],[],[]
IS_LW,IS1_LW,IS2_LW,IS3_LW,IS4_LW = [],[],[],[],[]

outpath ='/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/'
file = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/Ref-run/wrfout_d03_2017-07-31_18_00_00.nc'
file1 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/03a-Sensitivity-run-1/wrfout_d03_2017-07-31_18_00_00.nc'
file2 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/3b-Sensitivity-run-2/wrfout_d03_2017-07-31_18_00_00.nc'
file3 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/3c-Sensitivity-run-3/wrfout_d03_2017-07-31_18_00_00.nc'
file4 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/3d-Sensitivity-run-4/wrfout_d03_2017-07-31_18_00_00.nc'

for i in range(0,37,1):
 f = nc.Dataset(file)
 f1 = Dataset(file1, mode='r')
 f2 = Dataset(file2, mode='r')
 f3 = Dataset(file3, mode='r')
 f4 = Dataset(file4, mode='r')
 tair_units = f.variables['T2'].units
 tair = f.variables['T2'][i]   #T2 because TC_URB is equal for all timesteps
 tair1 = f1.variables['T2'][i]
 tair2 = f2.variables['T2'][i]
 tair3 = f3.variables['T2'][i]
 tair4 = f4.variables['T2'][i]
 #alb = f.variables['ALBEDO'][:]
 #H = f.variables['HFX'][:]  # upward heat flux= sensible heat flux?
 LE = f.variables['LH'][i]
 LE1 = f1.variables['LH'][i]
 LE2 = f2.variables['LH'][i]
 LE3 = f3.variables['LH'][i]
 LE4 = f4.variables['LH'][i]

 SW = f.variables['SWUPB'][i]
 SW1 = f1.variables['SWUPB'][i]
 SW2 = f2.variables['SWUPB'][i]
 SW3 = f3.variables['SWUPB'][i]
 SW4 = f4.variables['SWUPB'][i]

 LW = f.variables['LWUPB'][i]
 LW1 = f1.variables['LWUPB'][i]
 LW2 = f2.variables['LWUPB'][i]
 LW3 = f3.variables['LWUPB'][i]
 LW4 = f4.variables['LWUPB'][i]

 lon = f.variables['XLONG'][:]
 lat = f.variables['XLAT'][:]
 tair_IS = []
 tair_IS.append(tair[31:35][:, 70])
 tair_IS.append(tair[31:35][:, 71])  #y .. x
 tair_IS.append(tair[31:35][:, 72])
 tair_IS.append(tair[32:35][:, 73])
 tair_IS1 = []
 tair_IS1.append(tair1[31:35][:, 70])
 tair_IS1.append(tair1[31:35][:, 71])  #y .. x
 tair_IS1.append(tair1[31:35][:, 72])
 tair_IS1.append(tair1[32:35][:, 73])
 tair_IS2 = []
 tair_IS2.append(tair2[31:35][:, 70])
 tair_IS2.append(tair2[31:35][:, 71])  #y .. x
 tair_IS2.append(tair2[31:35][:, 72])
 tair_IS2.append(tair2[32:35][:, 73])
 tair_IS3 = []
 tair_IS3.append(tair3[31:35][:, 70])
 tair_IS3.append(tair3[31:35][:, 71])  #y .. x
 tair_IS3.append(tair3[31:35][:, 72])
 tair_IS3.append(tair3[32:35][:, 73])
 tair_IS4 = []
 tair_IS4.append(tair4[31:35][:, 70])
 tair_IS4.append(tair4[31:35][:, 71])  #y .. x
 tair_IS4.append(tair4[31:35][:, 72])
 tair_IS4.append(tair4[32:35][:, 73])

 LE_IS = []
 LE_IS.append(LE[31:35][:, 70])
 LE_IS.append(LE[31:35][:, 71])
 LE_IS.append(LE[31:35][:, 72])
 LE_IS.append(LE[32:35][:, 73])

 LE_IS1 = []
 LE_IS1.append(LE1[31:35][:, 70])
 LE_IS1.append(LE1[31:35][:, 71])
 LE_IS1.append(LE1[31:35][:, 72])
 LE_IS1.append(LE1[32:35][:, 73])

 LE_IS2 = []
 LE_IS2.append(LE2[31:35][:, 70])
 LE_IS2.append(LE2[31:35][:, 71])
 LE_IS2.append(LE2[31:35][:, 72])
 LE_IS2.append(LE2[32:35][:, 73])

 LE_IS3 = []
 LE_IS3.append(LE3[31:35][:, 70])
 LE_IS3.append(LE3[31:35][:, 71])
 LE_IS3.append(LE3[31:35][:, 72])
 LE_IS3.append(LE3[31:35][:, 73])
 LE_IS4 = []
 LE_IS4.append(LE4[31:35][:, 70])
 LE_IS4.append(LE4[31:35][:, 71])
 LE_IS4.append(LE4[31:35][:, 72])
 LE_IS4.append(LE4[31:35][:, 73])

 SW_IS = []
 SW_IS.append(SW[31:35][:, 70])
 SW_IS.append(SW[31:35][:, 71])
 SW_IS.append(SW[31:35][:, 72])
 SW_IS.append(SW[31:35][:, 73])

 SW_IS1 = []
 SW_IS1.append(SW1[31:35][:, 70])
 SW_IS1.append(SW1[31:35][:, 71])
 SW_IS1.append(SW1[31:35][:, 72])
 SW_IS1.append(SW1[31:35][:, 73])

 SW_IS2 = []
 SW_IS2.append(SW2[31:35][:, 70])
 SW_IS2.append(SW2[31:35][:, 71])
 SW_IS2.append(SW2[31:35][:, 72])
 SW_IS2.append(SW2[31:35][:, 73])

 SW_IS3 = []
 SW_IS3.append(SW3[31:35][:, 70])
 SW_IS3.append(SW3[31:35][:, 71])
 SW_IS3.append(SW3[31:35][:, 72])
 SW_IS3.append(SW3[31:35][:, 73])

 SW_IS4 = []
 SW_IS4.append(SW4[31:35][:, 70])
 SW_IS4.append(SW4[31:35][:, 71])
 SW_IS4.append(SW4[31:35][:, 72])
 SW_IS4.append(SW4[31:35][:, 73])

 LW_IS = []
 LW_IS.append(LW[31:35][:, 70])
 LW_IS.append(LW[31:35][:, 71])
 LW_IS.append(LW[31:35][:, 72])
 LW_IS.append(LW[31:35][:, 73])

 LW_IS1 = []
 LW_IS1.append(LW1[31:35][:, 70])
 LW_IS1.append(LW1[31:35][:, 71])
 LW_IS1.append(LW1[31:35][:, 72])
 LW_IS1.append(LW1[31:35][:, 73])

 LW_IS2 = []
 LW_IS2.append(LW2[31:35][:, 70])
 LW_IS2.append(LW2[31:35][:, 71])
 LW_IS2.append(LW2[31:35][:, 72])
 LW_IS2.append(LW2[31:35][:, 73])

 LW_IS3 = []
 LW_IS3.append(LW3[31:35][:, 70])
 LW_IS3.append(LW3[31:35][:, 71])
 LW_IS3.append(LW3[31:35][:, 72])
 LW_IS3.append(LW3[31:35][:, 73])

 LW_IS4 = []
 LW_IS4.append(LW4[31:35][:, 70])
 LW_IS4.append(LW4[31:35][:, 71])
 LW_IS4.append(LW4[31:35][:, 72])
 LW_IS4.append(LW4[31:35][:, 73])

 IS_mn = np.average(np.hstack(tair_IS))
 IS1_mn = np.average(np.hstack(tair_IS1))
 IS2_mn = np.average(np.hstack(tair_IS2))
 IS3_mn = np.average(np.hstack(tair_IS3))
 IS4_mn = np.average(np.hstack(tair_IS4))

 IS_LE_mn = np.average(np.hstack(LE_IS))
 IS1_LE_mn = np.average(np.hstack(LE_IS1))
 IS2_LE_mn = np.average(np.hstack(LE_IS2))
 IS3_LE_mn = np.average(np.hstack(LE_IS3))
 IS4_LE_mn = np.average(np.hstack(LE_IS4))

 IS_SW_mn = np.average(np.hstack(SW_IS))
 IS1_SW_mn = np.average(np.hstack(SW_IS1))
 IS2_SW_mn = np.average(np.hstack(SW_IS2))
 IS3_SW_mn = np.average(np.hstack(SW_IS3))
 IS4_SW_mn = np.average(np.hstack(SW_IS4))

 IS_LW_mn = np.average(np.hstack(LW_IS))
 IS1_LW_mn = np.average(np.hstack(LW_IS1))
 IS2_LW_mn = np.average(np.hstack(LW_IS2))
 IS3_LW_mn = np.average(np.hstack(LW_IS3))
 IS4_LW_mn = np.average(np.hstack(LW_IS4))

 #SA_mn = np.average(np.hstack(tair_SA))
 #WI_mn = np.average(np.hstack(tair_WI))

#c_a = np.average(np.hstack(tair_regionC))- np.average(np.hstack(tair_regionAg))

 IS.append(IS_mn)
 IS1.append(IS1_mn)
 IS2.append(IS2_mn)
 IS3.append(IS3_mn)
 IS4.append(IS4_mn)
 #SA.append(SA_mn)

 IS_LE.append(IS_LE_mn)
 IS1_LE.append(IS1_LE_mn)
 IS2_LE.append(IS2_LE_mn)
 IS3_LE.append(IS3_LE_mn)
 IS4_LE.append(IS4_LE_mn)

 IS_SW.append(IS_SW_mn)
 IS1_SW.append(IS1_SW_mn)
 IS2_SW.append(IS2_SW_mn)
 IS3_SW.append(IS3_SW_mn)
 IS4_SW.append(IS4_SW_mn)

 IS_LW.append(IS_LW_mn)
 IS1_LW.append(IS1_LW_mn)
 IS2_LW.append(IS2_LW_mn)
 IS3_LW.append(IS3_LW_mn)
 IS4_LW.append(IS4_LW_mn)

def difference(x,y):
 diff = []
 for i in range(len(x)):
    diff.append(x[i] - y[i])
 return diff

IS1diff = difference(IS1,IS)
IS2diff = difference(IS2,IS)
IS3diff = difference(IS3,IS)
IS4diff = difference(IS4,IS)

LE_IS1diff = difference(IS1_LE,IS_LE)
LE_IS2diff = difference(IS2_LE,IS_LE)
LE_IS3diff = difference(IS3_LE,IS_LE)
LE_IS4diff = difference(IS4_LE,IS_LE)

SW_IS1diff = difference(IS1_SW,IS_SW)
SW_IS2diff = difference(IS2_SW,IS_SW)
SW_IS3diff = difference(IS3_SW,IS_SW)
SW_IS4diff = difference(IS4_SW,IS_SW)

LW_IS1diff = difference(IS1_LW,IS_LW)
LW_IS2diff = difference(IS2_LW,IS_LW)
LW_IS3diff = difference(IS3_LW,IS_LW)
LW_IS4diff = difference(IS4_LW,IS_LW)

time = range(0,37,1)

#"""
fig_tair = plt.figure()
major_ticks = np.arange(0, 37, 6)
minor_ticks = np.arange(0, 37, 3)
plt.xticks(major_ticks)
#plt.xticks(minor_ticks)
plt.plot(time,IS1diff, color="black", label="Dense-Ref")
plt.plot(time,IS2diff, color="blue", label="Iso-Ref")
plt.plot(time,IS3diff, color="green", label="Unseal-Ref")
plt.plot(time,IS4diff, color="violet", label="HighAlb-Ref")
plt.axhline(y=0.000, color="black")#, xmin=0, xmax=1, hold=None, linewidth=2)
plt.axvline(x=10.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=17.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=25.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=34.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.ylabel(r"$\delta T_{air_2m}$"u'[°C]')
plt.legend(loc='upper right')
plt.show()
#"""
#"""
fig_LE = plt.figure()
major_ticks = np.arange(0, 37, 6)
plt.xticks(major_ticks)
plt.plot(time,LE_IS1diff, color="black", label="Dense-Ref")
plt.plot(time,LE_IS2diff, color="blue", label="Iso-Ref")
plt.plot(time,LE_IS3diff, color="green", label="Unseal-Ref")
plt.plot(time,LE_IS4diff, color="violet", label="HighAlb-Ref")
plt.axhline(y=0.000, color="black")#, xmin=0, xmax=1, hold=None, linewidth=2)
plt.axvline(x=10.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=17.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=25.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=34.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.ylabel("$Latent Heat Flux [W m-2]$")
plt.legend(loc='upper right')
plt.show()
#"""
exit()
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
plt.legend(loc='lower right')
plt.show()

#exit()

#"""
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

exit()
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