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

#tair_max = tair[18::24].mean(axis=0)
#tair1_max = tair1[18::24].mean(axis=0)
#tair2_max = tair2[18::24].mean(axis=0)

#1) Only selected heat wave: 199 timesteps: 6+(3*24) = 78h spinn up time.
# or last 5 days: [:-120]
#2) remove days with clouds:
#10:4UTC, 18:12UTC, 30:24UTC, 34:4UTC
print "tair.shape=", tair.shape

print len(tair[174:198])
exit()

tair_max1 = tair[78:102].min(axis=0)
tair_max2 = tair[102:126].min(axis=0)
tair_max3 = tair[150:174].min(axis=0)
tair_max4 = tair[174:198].min(axis=0)
tair_max = np.array([tair_max1,tair_max2,tair_max3,tair_max4])
print "tair_max1.shape=", tair_max1.shape
print "tair_max.shape=", tair_max.shape
tair_max = tair_max.mean(axis=0)
print "tair_max.mean.shape=", tair_max.shape

#exit()

tair1_max1 = tair1[78:102].min(axis=0)  #9.8.2015
tair1_max2 = tair1[102:126].min(axis=0) #10.8.2015
tair1_max3 = tair1[150:174].min(axis=0) #12.8.2015
tair1_max4 = tair1[174:198].min(axis=0) #13.8.2015
tair1_max = np.array([tair1_max1,tair1_max2,tair1_max3,tair1_max4])
tair1_max = tair1_max.mean(axis=0)

tair2_max1 = tair2[78:102].min(axis=0)
tair2_max2 = tair2[102:126].min(axis=0)
tair2_max3 = tair2[150:174].min(axis=0)
tair2_max4 = tair2[174:198].min(axis=0)
tair2_max = np.array([tair2_max1,tair2_max2,tair2_max3,tair2_max4])
tair2_max = tair2_max.mean(axis=0)

#print "tair.shape=", tair.shape, "tair_max.shape=", tair_max.shape
#exit()
f.close()
f1.close()
f2.close()

CE, NO, SA, RU, SE, SX, SI, VW, WE = [],[],[],[],[],[],[],[],[]
CE1, NO1, SA1, RU1, SE1, SX1, SI1, VW1, WE1 = [],[],[],[],[],[],[],[],[]
CE2, NO2, SA2, RU2, SE2, SX2, SI2, VW2, WE2 = [],[],[],[],[],[],[],[],[]

NO = tair_max[73:82][:,89:98]
CE = tair_max[50:59][:,80:89]
RU = tair_max[57:66][:,128:137]
SA = tair_max[58:67][:,109:118]
SE = tair_max[37:46][:,99:108]
SX = tair_max[24:33][:,75:84]
SI = tair_max[31:40][:,68:77]
VW = tair_max[47:56][:,64:73]
WE = tair_max[62:71][:,73:82]

NO1 = tair1_max[73:82][:,89:98]
CE1 = tair1_max[50:59][:,80:89]
RU1 = tair1_max[57:66][:,128:137]
SA1 = tair1_max[58:67][:,109:118]
SE1 = tair1_max[37:46][:,99:108]
SX1 = tair1_max[24:33][:,75:84]
SI1 = tair1_max[31:40][:,68:77]
VW1 = tair1_max[47:56][:,64:73]
WE1 = tair1_max[62:71][:,73:82]

NO2 = tair2_max[73:82][:,89:98]
CE2 = tair2_max[50:59][:,80:89]
RU2 = tair2_max[57:66][:,128:137]
SA2 = tair2_max[58:67][:,109:118]
SE2 = tair2_max[37:46][:,99:108]
SX2 = tair2_max[24:33][:,75:84]
SI2 = tair2_max[31:40][:,68:77]
VW2 = tair2_max[47:56][:,64:73]
WE2 = tair2_max[62:71][:,73:82]

print "CE.shape=", CE.shape, CE1.shape, CE2.shape
print "RU.shape=", RU.shape, RU1.shape, RU2.shape
print "SA.shape=", SA.shape, SA1.shape, SA2.shape
print "SE.shape=", SE.shape, SE1.shape, SE2.shape
print "SX.shape=", SX.shape, SX1.shape, SX2.shape
print "SI.shape=", SI.shape, SI1.shape, SI2.shape
print "VW.shape=", VW.shape, VW1.shape, VW2.shape
print "WE.shape=", WE.shape, WE1.shape, WE2.shape
print "NO.shape=", NO.shape, NO1.shape, NO2.shape
#print CE, CE1
#exit()

#Tair= transpose(np.array([CE,SA,RU,SE,SX,SI,VW,WE,NO]))
TairCE= transpose(np.array([CE.flatten(),CE1.flatten(),CE2.flatten()]))
TairSA= transpose(np.array([SA.flatten(),SA1.flatten(),SA2.flatten()]))
TairRU= transpose(np.array([RU.flatten(),RU1.flatten(),RU2.flatten()]))
TairSE= transpose(np.array([SE.flatten(),SE1.flatten(),SE2.flatten()]))
TairSX= transpose(np.array([SX.flatten(),SX1.flatten(),SX2.flatten()]))
TairSI= transpose(np.array([SI.flatten(),SI1.flatten(),SI2.flatten()]))
TairVW= transpose(np.array([VW.flatten(),VW1.flatten(),VW2.flatten()]))
TairWE= transpose(np.array([WE.flatten(),WE1.flatten(),WE2.flatten()]))
TairNO= transpose(np.array([NO.flatten(),NO1.flatten(),NO2.flatten()]))
#print "TairCE.shape=", TairCE.shape
#print "TairRU.shape=", TairRU.shape
#print "Tair.shape=", Tair.shape

labels = ["REF","SPR","OPT"]

#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.boxplot.html
#The box extends from the lower (Q1) to the upper (Q3) quartile values of data, with a line at the median
#The whiskers extend from the box to show the range of data, default=1.5 ->   Q1-whis*IQR, Q3+whis*IQR (interquartiles range)
#whis=[5,95]  Set whiskers to percentiles


fig2, axs = plt.subplots(nrows=1, ncols=10)#, figsize=(9, 4))
fig2.suptitle("mean daily minima, averaged over regions for 9,10,12,13 Aug 2015")
axs[0].boxplot(TairCE, notch=True, labels=labels, showfliers=True, whis=[5,95])
axs[0].set_ylabel(r"$T_{air_2m}$"u'[°C]')
axs[0].set_xlabel("Center")
axs[0].set_ylim([294,299.5])

axs[1].boxplot(TairSA,  notch=True, labels=labels, showfliers=True, whis=[5,95])
axs[1].set_xlabel("Seestadt")
axs[1].set_ylim([294,299.5])
axs[1].set_yticklabels([])

axs[2].boxplot(TairRU,  notch=True, labels=labels, showfliers=True,  whis=[5,95])
axs[2].set_xlabel("Rural")
axs[2].set_ylim([294,299.5])
axs[2].set_yticklabels([])

axs[3].boxplot(TairSE,  notch=True, labels=labels, showfliers=True,  whis=[5,95])
axs[3].set_xlabel("SouthEast")
axs[3].set_ylim([294,299.5])
axs[3].set_yticklabels([])

axs[4].boxplot(TairSX,  notch=True, labels=labels, showfliers=True,  whis=[5,95])
axs[4].set_xlabel("SouthExpansion")
axs[4].set_ylim([294,299.5])
axs[4].set_yticklabels([])

axs[5].boxplot(TairSI,  notch=True, labels=labels, showfliers=True,  whis=[5,95])
axs[5].set_xlabel("SouthIndustry")
axs[5].set_ylim([294,299.5])
axs[5].set_yticklabels([])

axs[6].boxplot(TairVW,  notch=True, labels=labels, showfliers=True,  whis=[5,95])
axs[6].set_xlabel("WienValley")
axs[6].set_ylim([294,299.5])
axs[6].set_yticklabels([])

axs[7].boxplot(TairWE,  notch=True, labels=labels, showfliers=True,  whis=[5,95])
axs[7].set_ylim([294,299.5])
axs[7].set_xlabel("WestElevated")
axs[7].set_yticklabels([])

axs[8].boxplot(TairNO,  notch=True, labels=labels, showfliers=True,  whis=[5,95])
axs[8].set_ylim([294,299.5])
axs[8].set_xlabel("NorthRim")
axs[8].set_yticklabels([])

axs[9].boxplot(TairNO,  notch=True, labels=labels, showfliers=True,  whis=[5,95], bootstrap=100000, autorange=False)
axs[9].set_ylim([294,299.5])
axs[9].set_xlabel("NorthRim")
axs[9].set_yticklabels([])

plt.show()


