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
f1 = Dataset(file1, mode='r')
lon = f.variables['XLONG'][1]  #lon (199x)135x174
lat = f.variables['XLAT'][1]  #lat (199x)135x174
tair_units = f.variables['T2'].units
tair = f.variables['T2'][:]
tair1 = f1.variables['T2'][:]

tair_max = tair[18::24].mean(axis=0)  #mean over every 24th element (12UTC timestep)
tair1_max = tair1[18::24].mean(axis=0)
#print tair.shape, tair_max.shape

f.close()
f1.close()

CE, NO, SA, RU, SE, SX, SI, VW, WE = [],[],[],[],[],[],[],[],[]
CE1, NO1, SA1, RU1, SE1, SX1, SI1, VW1, WE1 = [],[],[],[],[],[],[],[],[]

NO = tair_max[73:82][:,89:98]
CE = tair_max[50:59][:,80:89]
RU = tair_max[56:66][:,128:137]
SA = tair_max[58:67][:,109:118]
SE = tair_max[37:46][:,99:108]
SX = tair_max[24:33][:,75:84]
SI = tair_max[31:40][:,68:77]
VW = tair_max[47:56][:,64:73]
WE = tair_max[62:71][:,73:82]

NO1 = tair1_max[73:82][:,89:98]
CE1 = tair1_max[50:59][:,80:89]
RU1 = tair1_max[56:66][:,128:137]
SA1 = tair1_max[58:67][:,109:118]
SE1 = tair1_max[37:46][:,99:108]
SX1 = tair1_max[24:33][:,75:84]
SI1 = tair1_max[31:40][:,68:77]
VW1 = tair1_max[47:56][:,64:73]
WE1 = tair1_max[62:71][:,73:82]

Tair= transpose(np.array([CE,SA,RU,SE,SX,SI,VW,WE,NO]))
Tair1= transpose(np.array([CE1,SA1,RU1,SE1,SX1,SI1,VW1,WE1,NO1]))
#print len(ALB), ALB.shape
labels = ["CE","SA","RU","SE","SX","SI","VW","WE","NO"]

fig2, axs = plt.subplots(nrows=1, ncols=3)#, figsize=(9, 4))
fig2.suptitle("Region Averages 12UTC ")
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


