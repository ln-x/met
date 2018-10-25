# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from pylab import *

outpath_sens ='/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/'
ref = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/Ref-run/wrfout_d03_2017-07-31_18_00_00.nc'

outpath ='/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/'
file = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/Ref_Heidi_Lu_2015_1stRun/wrfout_d03_2015-08-05_18_00_00.nc'
file1 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/Sprawl_2050_2ndRun/wrfout_d03_2015-08-05_18_00_00.nc'

f = Dataset(file, mode='r')
lon = f.variables['XLONG'][1]  #lon (147x)135x174
lat = f.variables['XLAT'][1]  #lat (147x)135x174
tair_units = f.variables['T2'].units
f.close()

CE, NO, SA, RU, SE, SX, SI, VW, WE = [],[],[],[],[],[],[],[],[]
CE1, NO1, SA1, RU1, SE1, SX1, SI1, VW1, WE1 = [],[],[],[],[],[],[],[],[]

for i in range(6,199,1):
 f = nc.Dataset(file)
 f1 = nc.Dataset(file1)
 tair = f.variables['T2'][i]
 tair1 = f1.variables['T2'][i]
 f.close()
 f1.close()

 tair_CE, tair_RU, tair_SA,tair_SE, tair_SX, tair_SI, tair_VW, tair_WE, tair_NO = [],[],[],[],[],[],[],[],[]
 tair_CE.append(tair[50:59][:,80:89]) #left upper corner: 80-58 ... right lower 88-50
 tair_RU.append(tair[56:66][:,128:137])
 tair_SA.append(tair[58:67][:,109:118])
 tair_SE.append(tair[37:46][:,99:108])
 tair_SX.append(tair[24:33][:,75:84])
 tair_SI.append(tair[31:40][:,68:77])
 tair_VW.append(tair[47:56][:,64:73])
 tair_WE.append(tair[62:71][:,73:82])
 tair_NO.append(tair[73:82][:,89:98])

 CE.append(np.average(np.hstack(tair_CE)))
 NO.append(np.average(np.hstack(tair_NO)))
 SA.append(np.average(np.hstack(tair_SA)))
 SE.append(np.average(np.hstack(tair_SE)))
 SX.append(np.average(np.hstack(tair_SX)))
 SI.append(np.average(np.hstack(tair_SI)))
 VW.append(np.average(np.hstack(tair_VW)))
 WE.append(np.average(np.hstack(tair_WE)))
 RU.append(np.average(np.hstack(tair_RU)))

 tair1_CE, tair1_RU, tair1_SA, tair1_SE, tair1_SX, tair1_SI, tair1_VW, tair1_WE, tair1_NO = [], [], [], [], [], [], [], [], []
 tair1_CE.append(tair1[50:59][:, 80:89])  # left upper corner: 80-58 ... right lower 88-50
 tair1_RU.append(tair1[56:66][:, 128:137])
 tair1_SA.append(tair1[58:67][:, 109:118])
 tair1_SE.append(tair1[37:46][:, 99:108])
 tair1_SX.append(tair1[24:33][:, 75:84])
 tair1_SI.append(tair1[31:40][:, 68:77])
 tair1_VW.append(tair1[47:56][:, 64:73])
 tair1_WE.append(tair1[62:71][:, 73:82])
 tair1_NO.append(tair1[73:82][:,89:98])

 CE1.append(np.average(np.hstack(tair1_CE)))
 NO1.append(np.average(np.hstack(tair1_NO)))
 SA1.append(np.average(np.hstack(tair1_SA)))
 SE1.append(np.average(np.hstack(tair1_SE)))
 SX1.append(np.average(np.hstack(tair1_SX)))
 SI1.append(np.average(np.hstack(tair1_SI)))
 VW1.append(np.average(np.hstack(tair1_VW)))
 WE1.append(np.average(np.hstack(tair1_WE)))
 RU1.append(np.average(np.hstack(tair1_RU)))

"""
time = range(0,31,1)
fig, axs = plt.subplots(2,2)
major_ticks = np.arange(0, 31, 6)
minor_ticks = np.arange(0, 31, 3)
axs[0,0].set_xticks(major_ticks)
axs[0,0].set_xticks(minor_ticks, minor=True)
axs[0,0].plot(time,CE, color="red", label="Center")
axs[0,0].plot(time,SA, color="blue", label="Seestadt Aspern")
axs[0,0].plot(time,RU, color="green", label="Rural")
axs[0,0].set_ylabel(r"$T_{air_2m}$"u'[°C]')
#axs[0,0].legend(loc='upper center')

axs[1,0].set_xticks(major_ticks)
axs[1,0].set_xticks(minor_ticks, minor=True)
axs[1,0].plot(time, CE1, color="red", label="Innere Stadt")
axs[1,0].plot(time, SA1, color="blue", label="Innere Stadt")
axs[1,0].plot(time, RU1, color="green", label="Wiental")
axs[1,0].set_xlabel("hours [UTC]")
axs[1,0].set_ylabel('$albedo [0-1]$')
#axs[1,0].legend(loc='upper left')

axs[0,1].set_xticks(major_ticks)
axs[0,1].set_xticks(minor_ticks, minor=True)
axs[0,1].plot(time, CE_H, color="red", label="Innere Stadt")
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

Tair= transpose(np.array([CE,SA,RU,SE,SX,SI,VW,WE,NO]))
Tair1= transpose(np.array([CE1,SA1,RU1,SE1,SX1,SI1,VW1,WE1,NO1]))
#print len(ALB), ALB.shape
labels = ["CE","SA","RU","SE","SX","SI","VW","WE","NO"]

fig2, axs = plt.subplots(nrows=1, ncols=3)#, figsize=(9, 4))
fig2.suptitle("Region Averages Mean ")
axs[0].boxplot(Tair, notch=True, labels=labels, showfliers=True, showmeans=True)
axs[0].set_ylabel(r"$T_{air_2m}$"u'[°C]')
axs[0].set_xlabel("REF")

axs[1].boxplot(Tair1,  notch=True, labels=labels, showfliers=True, showmeans=True)
axs[1].set_ylabel(r"$T_{air_2m}$"u'[°C]')
axs[1].set_xlabel("SPRAWL")

#axs[1].boxplot(Tair2,  notch=True, labels=labels, showfliers=True, showmeans=True)
axs[2].set_ylabel(r"$T_{air_2m}$"u'[°C]')
axs[2].set_xlabel("OPT")

plt.show()



