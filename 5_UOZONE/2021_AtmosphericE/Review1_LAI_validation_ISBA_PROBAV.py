# -*- coding: utf-8 -*-
__author__ = 'lnx'

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import netCDF4
from met.library import ReadinPROBAV_LAI_300m_2

"""READ IN ISBA LAI_ PROBAV_assim"""

foldername = "/windata/DATA/models/nilu/MEGAN3_SURFEX_SEEDS/assim_LAI/LAI_assim_LAI_2019/"
files = os.listdir(foldername)
files = sorted(files)
dateaxis=[]
LAI=[]
index_lat = 202  #LAT 48.25°N
index_lon = 422 #LON 16.25°E (city rim to Wienerwald) or 421: LON 16.15°E (middle Wienerwald)
for i in range(len(files)):
    day = str(files[i][-5:-3])  # splitlistcomp[3:4]
    month = str(files[i][-7:-5])  # splitlistcomp[2:3]
    year = "20" + str(files[i][-9:-7])  # splitlistcomp[:2]
    #print(day,month,year)
    date = datetime(year=int(year), month=int(month), day=int(day))
    #print(date)
    dateaxis.append(date)
    infile = netCDF4.Dataset(foldername+files[i])
    LAI_dailyvalue = infile.variables['LAI_ISBA'][:, index_lat, index_lon]
    LAI.append(LAI_dailyvalue)

LAI = pd.DataFrame({'datetime': dateaxis, 'LAI': LAI})
LAI['datetime'] = pd.to_datetime(LAI['datetime'])
LAI_ISBA_as = LAI.set_index(['datetime'])
#print(LAI[:])

"""READ IN PROBAV_LAI300m"""
LAI_PROBAV = ReadinPROBAV_LAI_300m_2.LAI()

print(LAI_PROBAV.to_numpy())

fig = plt.figure()
#plt.suptitle(f"OBS {start} - {end}")
ax1 = fig.add_subplot(111)
ax1.plot(LAI_PROBAV,linewidth="1", color='black', label="PROBAV", linestyle="solid")
ax1.plot(LAI_PROBAV+1,linewidth="1", color='grey', label="Uncertainty Threshold", linestyle="solid")
ax1.plot(LAI_PROBAV-1,linewidth="1", color='grey', label="Uncertainty Threshold", linestyle="solid")
#ax1.fill_between(LAI_PROBAV.to_numpy(), 1, 1, alpha=0.3, facecolor="grey")
#ax.fill_between(epochs, meanst - sdt, meanst + sdt, alpha=0.3, facecolor=clrs[i])
ax1.plot(LAI_ISBA_as[:],linewidth="1", color='violet', label="ISBA_as", linestyle="solid")
ax1.set_xlabel("days")
#ax1.set_xlim(start,end)
ax1.set_ylabel("[-]", size="medium")
plt.show()
exit()


LAI_PROBAV.plot()
LAI_ISBA_as.plot()
plt.show()
exit()

infile1 = netCDF4.Dataset("/windata/DATA/models/nilu/MEGAN3_SURFEX_SEEDS/assim_LAI/LAI_assim_LAI_2019/LAI_20190101.nc")
#lat = infile1.variables['lat'][index_lat]
#lon = infile1.variables['lon'][index_lon]
#print(lat,lon)
LAI = infile1.variables['LAI_ISBA'][:,index_lat,index_lon]
print(LAI)
exit()
