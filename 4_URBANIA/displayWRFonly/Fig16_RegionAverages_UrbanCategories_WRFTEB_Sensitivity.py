# -*- coding: utf-8 -*-
import csv
import netCDF4 as nc
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from pylab import *
#import regionmask
#regionmask.__version__

diff_tair_ldr1a_1, diff_tair_ldr1_ref, diff_tair_ldr1a_ref = [],[],[]
diff_tair_com1a_1, diff_tair_com1_ref, diff_tair_com1a_ref = [],[],[]

outpath ='/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/'
file = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/Ref-run/wrfout_d03_2017-07-31_18_00_00.nc'
file1 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/03a-Sensitivity-run-1/wrfout_d03_2017-07-31_18_00_00.nc'
file1a = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/03a-rerun/wrfout_d03_2017-07-31_18_00_00.nc'
file2 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/3b-Sensitivity-run-2/wrfout_d03_2017-07-31_18_00_00.nc'
file3 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/3c-Sensitivity-run-3/wrfout_d03_2017-07-31_18_00_00.nc'
file4 = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/201707/Sensitivity_Runs/3d-Sensitivity-run-4/wrfout_d03_2017-07-31_18_00_00.nc'

for i in range(0,37,1):
 f = nc.Dataset(file)
 f1 = Dataset(file1, mode='r')
 f1a = Dataset(file1a, mode='r')
 f2 = Dataset(file2, mode='r')
 f3 = Dataset(file3, mode='r')
 f4 = Dataset(file4, mode='r')
 tair_units = f.variables['T2'].units
 LU = f.variables['LU_INDEX'][i]  #31 low density residential, 32 high density residential, 33 commercial
 tair = f.variables['T2'][i]   #T2 because TC_URB is equal for all timesteps
 tair1 = f1.variables['T2'][i]
 tair1a = f1a.variables['T2'][i]
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

 LU_ldr = LU == 31
 LU_hdr = LU == 32
 LU_com = LU == 33

 tair_ldr = ma.masked_array(tair, mask=LU_ldr)
 tair1_ldr = ma.masked_array(tair1, mask=LU_ldr)
 tair1a_ldr = ma.masked_array(tair1a, mask=LU_ldr)
 tair_hdr = ma.masked_array(tair, mask=LU_hdr)
 tair_com = ma.masked_array(tair, mask=LU_com)
 tair1_com = ma.masked_array(tair1, mask=LU_com)
 tair1a_com = ma.masked_array(tair1a, mask=LU_com)
 tair_ldr_m = tair_ldr.mean()
 tair1_ldr_m = tair1_ldr.mean()
 tair1a_ldr_m = tair1a_ldr.mean()

 tair_hdr_m = tair_hdr.mean()

 tair_com_m = tair_com.mean()
 tair1_com_m = tair1_com.mean()
 tair1a_com_m = tair1a_com.mean()

 diff_tair_ldr1a_1.append(tair1a_ldr_m - tair1_ldr_m)
 diff_tair_ldr1a_ref.append(tair1a_ldr_m - tair_ldr_m)
 diff_tair_ldr1_ref.append(tair1_ldr_m - tair_ldr_m)

 diff_tair_com1a_1.append(tair1a_com_m - tair1_com_m)
 diff_tair_com1a_ref.append(tair1a_com_m - tair_com_m)
 diff_tair_com1_ref.append(tair1_com_m - tair_com_m)

#print np.max(diff_tair_com1a_1),np.min(diff_tair_com1a_1)
#exit()

time = range(0,37,1)

#"""
fig_tair = plt.figure()
major_ticks = np.arange(0, 37, 6)
minor_ticks = np.arange(0, 37, 3)
plt.xticks(major_ticks)

#plt.xticks(minor_ticks)
plt.plot(time,diff_tair_com1a_1, color="red", label="COM 3a rerun - 3a")
plt.plot(time,diff_tair_com1a_ref, color="blue", label="COM 3a rerun - Ref")
plt.plot(time,diff_tair_com1_ref, color="green", label="COM 3a - Ref")
plt.plot(time,diff_tair_ldr1a_1, color="red", linestyle=':',label="LDR 3a rerun - 3a")
plt.plot(time,diff_tair_ldr1a_ref, color="blue", linestyle=':', label="LDR 3a rerun - Ref")
plt.plot(time,diff_tair_ldr1_ref, color="green", linestyle=':', label="LDR 3a - Ref")
plt.axhline(y=0.000, color="black")#, xmin=0, xmax=1, hold=None, linewidth=2)
plt.axvline(x=10.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=17.500, color="yellow", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=25.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.axvline(x=34.000, color="red", linestyle=':')#, xmin=0, xmax=1, hold=None)
plt.ylabel(r"$\delta T_{air_2m}$"u'[°C]')
plt.legend(loc='upper right')
plt.show()
#"""
exit()


def difference(param):
 diff = []
 param_ldr = ma.masked_array(param, mask=LU_ldr)
 param_hdr = ma.masked_array(param, mask=LU_hdr)
 param_com = ma.masked_array(param, mask=LU_com)

 for i in range(len(param)):
    diff.append(x[i] - y[i])
 return diff

