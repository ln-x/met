# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import numpy as np
import pandas as pd
from scipy import stats
import sys
from metpy.calc import *
from metpy.units import units
from datetime import datetime, timedelta
from pylab import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime

outpath ='/home/lnx'
file = '/media/lnx/Norskehavet/WRF-TEB-NC_Files/FINAL/WRF-2019-Runs/Ref-Run-2017/wrfout_d03_2017-07-26_18_00_00'

fh = Dataset(file, mode='r')
#fh2 = Dataset(file2, mode='r')

'''time + 2dvariables'''
lons = fh.variables['XLONG'][1]  #lon (147x)135x174
lats = fh.variables['XLAT'][1]  #lat (147x)135x174
SM_WRFTEB = fh.variables['SMOIS'] #229 timesteps x 4 soil layers x 135 x 174  [kg]
print SM_WRFTEB.shape
depths = fh.variables['ZS'] #center of layer

SM_WRFTEB_units = fh.variables['SMOIS'].units

#a1,a2,b1,b2= 51,60,81,90 #50,59,80,89   #CE
#a1,a2,b1,b2=73,82,89,98   #NO
a1,a2,b1,b2=57,66,128,137 #RU
#a1,a2,b1,b2=58,67,109,118 #SA
#a1,a2,b1,b2=37,46,99,108  #SE
#a1,a2,b1,b2=24,33,75,84   #SX
#a1,a2,b1,b2=31,40,68,77   #SI
#a1,a2,b1,b2=47,56,64,73   #VW
#a1,a2,b1,b2=62,71,73,82   #WE

SM_layer005 = SM_WRFTEB[:,0,a1:a2,b1:b2]
print SM_layer005.shape
SM_layer005= SM_layer005.reshape(229,81)
SM_layer005 = SM_layer005.mean(axis=1)

SM_layer025 = SM_WRFTEB[:,1,57:66,128:137]
SM_layer025= SM_layer025.reshape(229,81)
SM_layer025 = SM_layer025.mean(axis=1)

SM_layer07 = SM_WRFTEB[:,2,57:66,128:137]
SM_layer07= SM_layer07.reshape(229,81)
SM_layer07 = SM_layer07.mean(axis=1)

SM_layer15 = SM_WRFTEB[:,3,57:66,128:137]
SM_layer15= SM_layer15.reshape(229,81)
SM_layer15 = SM_layer15.mean(axis=1)

start = datetime.datetime(2069,7,1,19,0)  #1...229
stop = datetime.datetime(2069,7,9,0,0)
#stop = datetime.datetime(2069,7,11,7,0)
delta = datetime.timedelta(hours=1)
dates = mpl.dates.drange(start,stop,delta)
print dates.shape

#date_format = mpl.dates.DateFormatter('%d %B %Y')
date_format = mpl.dates.DateFormatter('      %H') #Meteorol. Z. Format:  %H%M UTC %d %B %Y

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(dates, SM_layer005[1:175], color='black', label="0.05 m")  #31
ax1.plot(dates, SM_layer025[1:175], color='black', linestyle="--", label="0.25 m")  #31
ax1.plot(dates, SM_layer07[1:175], color='grey', linestyle="--", label="0.7 m")  #31
ax1.plot(dates, SM_layer15[1:175], color='grey', linestyle=":",  label="1.5 m")  #31

#ax1.plot(WRFdata2_heatdays, color='blue', label="WRF(C)")  #31
ax1.set_xlabel("Time [UTC]")
ax1.set_ylabel(r"soil moisture "'$[kg/kg]$', size="medium")
ax1.legend(loc='upper right')
#ax1.set_xlim(0, 180)
#ax1.set_ylim(15, 40)
ax1 = gca()
days = DayLocator(range(2, 9), interval=1)
hours = HourLocator(range(0, 23), interval=6)
ax1.xaxis.set_major_locator(hours)
ax1.xaxis.set_major_formatter(date_format)
ax1.grid(linestyle=":")
plt.xticks(rotation='vertical', fontsize='small')
plt.subplots_adjust(bottom=.3)
plt.show()

fh.close()



