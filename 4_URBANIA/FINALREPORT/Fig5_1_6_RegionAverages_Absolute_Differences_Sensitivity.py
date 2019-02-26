# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from pylab import *
import matplotlib.gridspec as gridspec

outpath ='/media/lnx/Norskehavet/WRF-TEB-NC_Files/201508/'
file = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/Ref-run/wrfout_d03_2017-07-31_18_00_00.nc'
file1 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/02-sprawl/wrfout_d03_2017-07-31_18_00_00.nc'
file2 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/03-Sensitivity-run-1/wrfout_d03_2017-07-31_18_00_00.nc'
file3 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/03a-rerun/wrfout_d03_2017-07-31_18_00_00.nc'
file4 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/3b-Sensitivity-run-2/wrfout_d03_2017-07-31_18_00_00.nc'
file5 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/3c-Sensitivity-run-3/wrfout_d03_2017-07-31_18_00_00.nc'
file6 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/3d-Sensitivity-run-4/wrfout_d03_2017-07-31_18_00_00.nc'


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

init = datetime.datetime.strptime("2015-08-04 18:00", "%Y-%m-%d %H:%M")
timelist = [init + datetime.timedelta(hours=x) for x in range(0,199)]
print len(timelist)
#exit()

fig = plt.figure()
#ax1 = fig.add_subplot(111)

gs = gridspec.GridSpec(2, 1,height_ratios=[1,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])

#major_ticks = np.arange(0, 199, 6)
#minor_ticks = np.arange(0, 199, 3)
#ax1.set_xticks(major_ticks)
#ax2.set_xticks(major_ticks)

ax1.plot(timelist,CE, color="red", label="Center, Ref")
ax1.plot(timelist,CE1, color="red", linestyle="--", label="Center, Spr")
ax1.plot(timelist,CE2, color="red", linestyle=":", label="Center, Opt")
ax1.plot(timelist,SA, color="blue", label="Center, Ref")
ax1.plot(timelist,SA1, color="blue", linestyle="--", label="Seestadt, Spr")
ax1.plot(timelist,SA2, color="blue", linestyle=":", label="Seestadtr, Opt")
ax1.plot(timelist,RU, color="green", label="Center, Ref")
ax1.plot(timelist,RU1, color="green", linestyle="--", label="Rural, Spr")
ax1.plot(timelist,RU2, color="green", linestyle=":", label="Rural, Opt")
ax1.set_ylabel(r"$\Delta T_{a}$" u"°C")
ax1.legend(loc="lower right",fontsize='small')
ax1.set_ylim([293,309])

ax2.plot(timelist,CEdiff_1, color="red", label="Center, Spr-Ref",linestyle="--")
ax2.plot(timelist,CEdiff_2, color="red", label="Center, Opt-Ref", linestyle=":")
ax2.plot(timelist,RUdiff_1, color="green", label="Rural, Spr-Ref",linestyle="--")
ax2.plot(timelist,RUdiff_2, color="green", label="Rural, Opt-Ref", linestyle=":")
ax2.plot(timelist,SAdiff_1, color="blue", label="Seestadt, Spr-Ref",linestyle="--")
ax2.plot(timelist,SAdiff_2, color="blue", label="Seestadt, Opt-Ref", linestyle=":")
ax2.set_ylim([-2,1])
ax2.set_ylabel(r"$T_{a}$"u'[°C]')
ax2.legend(loc="lower right",fontsize='small')
ax2.set_xlabel('[UTC]')
ax1.grid(True)
ax2.grid(True)
myFmt = DateFormatter("%d")
ax1.xaxis.set_major_formatter(myFmt)
plt.show()

exit()
###
fig_tair, ax1 = plt.subplots()
major_ticks = np.arange(0, 199, 6)
minor_ticks = np.arange(0, 199, 3)
plt.xticks(major_ticks)
ax2 = ax1.twinx()

ax1.axhline(y=0.000, color="black")#, xmin=0, xmax=1, hold=None, linewidth=2)
ax1.axvline(x=10.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
ax1.axvline(x=17.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
ax1.axvline(x=25.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
ax1.axvline(x=34.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
ax1.axvline(x=41.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
ax1.axvline(x=65.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
ax1.axvline(x=89.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
ax1.axvline(x=113.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
ax1.axvline(x=137.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)

plt.ylabel(r"$\delta T_{air_2m}$"u'[°C]')
plt.legend(loc='lower left')
plt.show()
