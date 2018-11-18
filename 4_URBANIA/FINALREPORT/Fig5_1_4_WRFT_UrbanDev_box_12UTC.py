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
file2 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/Dense_2050_3rdRun_Optimized_city/wrfout_d03_2015-08-05_18_00_00.nc'

f = Dataset(file, mode='r')
f1 = Dataset(file1, mode='r')
f2 = Dataset(file2, mode='r')
lon = f.variables['XLONG'][1]  #lon (199x)135x174
lat = f.variables['XLAT'][1]   #lat (199x)135x174
tair_units = f.variables['T2'].units
tair = f.variables['T2'][:]
tair1 = f1.variables['T2'][:]
tair2 = f2.variables['T2'][:]

#10:4UTC, 18:12UTC, 30:24UTC, 34:4UTC
tair_max = tair[18::24].mean(axis=0)   #mean over every 24th element (12UTC timestep)
tair1_max = tair1[18::24].mean(axis=0)
tair2_max = tair2[18::24].mean(axis=0)
#print tair.shape, tair_max.shape
#exit()
f.close()
f1.close()
f2.close()

CE, NO, SA, RU, SE, SX, SI, VW, WE = [],[],[],[],[],[],[],[],[]
CE1, NO1, SA1, RU1, SE1, SX1, SI1, VW1, WE1 = [],[],[],[],[],[],[],[],[]
CE2, NO2, SA2, RU2, SE2, SX2, SI2, VW2, WE2 = [],[],[],[],[],[],[],[],[]

NO = tair_max[89:98][:,73:82]
CE = tair_max[80:89][:,50:59]
RU = tair_max[128:137][:,56:66]
SA = tair_max[109:118][:,58:67]
SE = tair_max[99:108][:,37:46]
SX = tair_max[75:84][:,24:33]
SI = tair_max[68:77][:,31:40]
VW = tair_max[64:73][:,47:56]
WE = tair_max[73:82][:,62:71]

NO1 = tair1_max[89:98][:,73:82]
CE1 = tair1_max[80:89][:,50:59]
RU1 = tair1_max[128:137][:,56:66]
SA1 = tair1_max[109:118][:,58:67]
SE1 = tair1_max[99:108][:,37:46]
SX1 = tair1_max[75:84][:,24:33]
SI1 = tair1_max[68:77][:,31:40]
VW1 = tair1_max[64:73][:,47:56]
WE1 = tair1_max[73:82][:,62:71]

NO2 = tair2_max[89:98][:,73:82]
CE2 = tair2_max[80:89][:,50:59]
RU2 = tair2_max[128:137][:,56:66]
SA2 = tair2_max[109:118][:,58:67]
SE2 = tair2_max[99:108][:,37:46]
SX2 = tair2_max[75:84][:,24:33]
SI2 = tair2_max[68:77][:,31:40]
VW2 = tair2_max[64:73][:,47:56]
WE2 = tair2_max[73:82][:,62:71]
print "CE.shape", CE.shape
Tair= transpose(np.array([CE,SA,RU,SE,SX,SI,VW,WE,NO]))
Tair1= transpose(np.array([CE1,SA1,RU1,SE1,SX1,SI1,VW1,WE1,NO1]))
Tair2= transpose(np.array([CE2,SA2,RU2,SE2,SX2,SI2,VW2,WE2,NO2]))
TairCE= transpose(np.array([CE,CE1,CE2]))
print "TairCE.shape=", TairCE.shape

print "Tair.shape=", Tair.shape
labels = ["CE","SA","RU","SE","SX","SI","VW","WE","NO"]

fig2, axs = plt.subplots(nrows=1, ncols=3)#, figsize=(9, 4))
fig2.suptitle("Region Averages 12UTC")
axs[0].boxplot(Tair, notch=True, labels=labels, showfliers=True, showmeans=True)
axs[0].set_ylabel(r"$T_{air_2m}$"u'[°C]')
axs[0].set_xlabel("REF")

axs[1].boxplot(Tair1,  notch=True, labels=labels, showfliers=True, showmeans=True)
axs[1].set_ylabel(r"$T_{air_2m}$"u'[°C]')
axs[1].set_xlabel("SPRAWL")

axs[2].boxplot(Tair2,  notch=True, labels=labels, showfliers=True, showmeans=True)
axs[2].set_ylabel(r"$T_{air_2m}$"u'[°C]')
axs[2].set_xlabel("OPT")

plt.show()


