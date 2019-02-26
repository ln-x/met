# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset

file = '/media/lnx/Norskehavet/OFFLINE/SENSITIVITY/FR_SEN_1_REF/TEB_DIAGNOSTICS.OUT.nc'
#file1 = '/media/lnx/Norskehavet/OFFLINE/SENSITIVITY/FR_SEN_2_SPR/TEB_DIAGNOSTICS.OUT.nc'
file1 = '/media/lnx/Norskehavet/OFFLINE/SENSITIVITY/FR_SEN_3a_DE2/TEB_DIAGNOSTICS.OUT.nc'
file2 = '/media/lnx/Norskehavet/OFFLINE/SENSITIVITY/FR_SEN_3b_ISO/TEB_DIAGNOSTICS.OUT.nc'
file3 = '/media/lnx/Norskehavet/OFFLINE/SENSITIVITY/FR_SEN_3d_ALB/TEB_DIAGNOSTICS.OUT.nc'

#f = Dataset(file, mode='r')
#lon = f.variables['XLONG'][1]  # lon (199x)135x174
#lat = f.variables['XLAT'][1]  # lat (199x)135x174
#f.close()

CE, NO, SA, RU, SE, SX, SI, VW, WE = [],[],[],[],[],[],[],[],[]
CE1, NO1, SA1, RU1, SE1, SX1, SI1, VW1, WE1 = [],[],[],[],[],[],[],[],[]
CE2, NO2, SA2, RU2, SE2, SX2, SI2, VW2, WE2 = [],[],[],[],[],[],[],[],[]
CE3, NO3, SA3, RU3, SE3, SX3, SI3, VW3, WE3 = [],[],[],[],[],[],[],[],[]

for i in range(0,36,1):
 f = Dataset(file, mode='r')
 f1 = Dataset(file1, mode='r')
 f2 = Dataset(file2, mode='r')
 f3 = Dataset(file3, mode='r')
 #var_units = f.variables['UTCI_OUTSHAD'].units
 var = f.variables['UTCI_OUTSHAD'][i]
 var1 = f1.variables['UTCI_OUTSHAD'][i]
 var2 = f2.variables['UTCI_OUTSHAD'][i]
 var3 = f3.variables['UTCI_OUTSHAD'][i]
 print np.average(var[50:58][:, 80:85].flatten())
 print np.hstack(var2[50:58][:, 80:85])
 print np.average(np.hstack(var[50:58][:, 80:85]))
 print np.average(np.hstack(var2[50:58][:, 80:85]))
 exit()
 
 f.close()
 f1.close()
 f2.close()
 f3.close()
 #print tair[50:59].shape
 #exit()

 CE.append(np.average(np.hstack(var[50:59][:, 80:89])))
 RU.append(np.average(np.hstack(var[57:66][:, 128:137])))
 SA.append(np.average(np.hstack(var[58:67][:, 109:118])))

 CE1.append(np.average(np.hstack(var1[50:59][:, 80:89])))
 RU1.append(np.average(np.hstack(var1[57:66][:, 128:137])))
 SA1.append(np.average(np.hstack(var1[58:67][:, 109:118])))

 CE2.append(np.average(np.hstack(var2[50:59][:, 80:89])))
 RU2.append(np.average(np.hstack(var2[57:66][:, 128:137])))
 SA2.append(np.average(np.hstack(var2[58:67][:, 109:118])))

 CE3.append(np.average(np.hstack(var3[50:59][:, 80:89])))
 RU3.append(np.average(np.hstack(var3[57:66][:, 128:137])))
 SA3.append(np.average(np.hstack(var3[58:67][:, 109:118])))

def difference(x,y):
 diff = []
 for i in range(len(x)):
    diff.append(x[i] - y[i])
 return diff

CEdiff_1 = difference(CE1,CE)
CEdiff_2 = difference(CE2,CE)
CEdiff_3 = difference(CE3,CE)
RUdiff_1 = difference(RU1,RU)
RUdiff_2 = difference(RU2,RU)
RUdiff_3 = difference(RU3,RU)
SAdiff_1 = difference(SA1,SA)
SAdiff_2 = difference(SA2,SA)
SAdiff_3 = difference(SA3,SA)

print len(CE), len(CE2)
exit()

time = range(0,36,1)
#"""
fig_tair = plt.figure()
major_ticks = np.arange(0, 36, 6)
minor_ticks = np.arange(0, 36, 3)
plt.xticks(major_ticks)

#plt.xticks(minor_ticks)
#plt.plot(time,ISdiff_DenseIso, color="black", label="Dense-Iso")
plt.plot(time,CEdiff_1, color="red", label="Center, DE2-Ref")
plt.plot(time,CEdiff_2, color="red", label="Center, ISO-Ref", linestyle="--")
plt.plot(time,CEdiff_3, color="red", label="Center, ALB-Ref", linestyle=":")
plt.plot(time,RUdiff_1, color="green", label="Rural, DE2-Ref")
plt.plot(time,RUdiff_2, color="green", label="Rural, ISO-Ref", linestyle="--")
plt.plot(time,RUdiff_3, color="green", label="Rural, ALB-Ref", linestyle=":")
plt.plot(time,SAdiff_1, color="blue", label="Seestadt, DE2-Ref")
plt.plot(time,SAdiff_2, color="blue", label="Seestadt, ISO-Ref", linestyle="--")
plt.plot(time,SAdiff_3, color="blue", label="Seestadt, ALB-Ref", linestyle=":")
plt.axhline(y=0.000, color="black")#, xmin=0, xmax=1, hold=None, linewidth=2)
plt.axvline(x=10.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=17.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=25.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=34.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
#plt.axvline(x=41.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
#plt.axvline(x=65.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
#plt.axvline(x=89.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
#plt.axvline(x=113.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
#plt.axvline(x=137.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)

plt.ylabel(r"$\delta UTCI$"u'[°C]')
plt.legend(loc='lower left')
plt.show()