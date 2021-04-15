# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset, num2date
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sys
from datetime import datetime
from datetime import timedelta
import numpy as np
from matplotlib import dates as d
import datetime as dt
import BOKUMet_Data
from scipy import stats


#Time: all available data for 2020
start = datetime(2020, 4,  1,  0, 0)
end   = datetime(2020, 4, 30, 23, 0)
#Time resolution: hourly
#TODO: Vindobona
#   -HCHO
#   -CHOCHO
#   -ratio
#TODO: WRF-Chem insert new data
#   -hcho, gly, hcho/gly ratio
#   -ho2,

#HCHO DATA
Vindobona = "/windata/Google Drive/DATA/remote/ground/maxdoas/Monika/"  # in DSCD
tframe = '60T'
AxisA = pd.read_csv(Vindobona + "hcho_A_1.6.2017-31.5.2020.csv")#, parse_dates=["date"])
#print(AxisA.date)  #0        2017-06-01 04:39:34
#AxisA.date = pd.to_datetime(AxisA.date)
#print(type(AxisA.date)) #<class 'pandas.core.series.Series'>
#print(AxisA.index, AxisA.columns, AxisA.info, type(AxisA))
AxisA = AxisA.set_index(pd.to_datetime(AxisA['date']))
AxisA_drop = AxisA.drop(columns=['date'])

AxisA_hr_mean = AxisA_drop.resample(tframe).nearest()
AxisA_April2020h = AxisA_hr_mean[start:end]
AxisA_d_mean = AxisA_hr_mean.resample('D').mean()
AxisA_April2020d = AxisA_d_mean[start:end]
#print(len(AxisA_April2020))

#MODEL DATA
path = '/media/heidit/'  # '/media/lnx'
outpath = path + 'Norskehavet/EMEPData/OUTPUT/2020_4'
file = path + 'Norskehavet/EMEPData/OUTPUT/2020_4/JanBASESIM_4b_day.nc'

fh = Dataset(file, mode='r')
#EMEP:
lons = fh.variables['lon'][1]
lats = fh.variables['lat'][1]
emep_o3 = fh.variables['SURF_ppb_O3']
emep_no2 = fh.variables['SURF_ppb_NO2']
emep_c5h8 = fh.variables['SURF_ppb_C5H8']
emep_hcho = fh.variables['SURF_ppb_HCHO']
#print(len(emep_hcho[:,1,1]))
#emep_gly = fh.variables['SURF_ppb_']
c5h8_units = fh.variables['SURF_ppb_C5H8'].units
no2_units = fh.variables['SURF_ppb_NO2'].units
o3_units = fh.variables['SURF_ppb_O3'].units
#TODO emep_forgly_ratio = emep_hcho/emep_gly

#WRF_Chem:
file2 = path + 'Norskehavet/EMEPData/OUTPUT/2020_4/wrfout_d01_2020-03-31_01:00:00'
fh2 = Dataset(file2, mode='r')

LON = fh2.variables['XLONG'][1]
LAT = fh2.variables['XLAT'][1]
times = fh2.variables['XTIME']
T2 = fh2.variables['T2']
SM = fh2.variables['SMOIS'][:,:,:,:]  #SMOIS, SH20
SM_units = fh2.variables['SMOIS'].units
EBIO_ISO = fh2.variables['EBIO_ISO']
EBIO_ISO_units = fh2.variables['EBIO_ISO'].units
EBIO_API = fh2.variables['EBIO_API']
wrfc_hcho = fh2.variables['hcho'] # (Time=720, Bottom-Top, South-North, West-East)
wrfc_hcho_units = fh2.variables['hcho'].units
#wrfc_gly = fh2.variable['gly']
#wrfc_iso = fh2.variable['iso']
#wrfc_ho2 = fh2.variable['ho2']
#wrfc_tol = fh2.variable['tol']
#wrfc_o3 = fh2.variable['o3']
#wrfc_no2 = fh2.variable['no2']
#print(len(wrfc_hcho[:,1,1])) #len720 = 30*24
#print(wrfc_hcho[:,1,1])
#TODO convert to daily values!

jd = num2date(times[:],times.units)
#hs = pd.Series(wrfc_hcho[:,1,1,1],index=jd)

hs = pd.DataFrame(wrfc_hcho[:,1,1,1],index=jd)
hs = hs.set_index(pd.to_datetime(times[:]))
print(hs)
exit()
hs_d = hs.resample('D').mean()

fig = plt.figure(figsize=(12,4))
ax = fig.add_subplot(111)
hs_d.plot(ax=ax)#,title='%s at %s' % (wrfc_hcho.long_name,nc.id))
ax.set_ylabel(wrfc_hcho.units)
plt.show()

exit()

#TODO wrfc_forgly_ratio = wrfc_hcho/wrfc_gly

#print(wrfc_hcho[:,1,1,1])
#exit()

'''calculation of Regression coefficients'''
# print stats.spearmanr(ZAMG_heatdays, WRFdata_heatdays, axis=0)
print(stats.spearmanr(emep_hcho[:,173,79],AxisA_April2020d.values[:26]))

R2_hcho = (stats.spearmanr(AxisA_April2020d.values[:26],emep_hcho[:,173,79])[0] ** 2)
R_hcho = (stats.spearmanr(AxisA_April2020d.values[:26],emep_hcho[:,173,79])[0])
R_hcho2 = (stats.spearmanr(AxisA_April2020h.values[:], wrfc_hcho[:,1,1,1])[0])
#R2_Forc_NO2concentr = (stats.spearmanr(o3, no2))[0] ** 2
#R2_Forc_c5h8concentr = (stats.spearmanr(o3, c5h8))[0] ** 2

print(R_hcho, R_hcho2)
#exit()


'''
Plotting
'''

try:
    fig1 = plt.figure()
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    #ax1.plot(emep_o3[:,173,79], color='violet', label="O3") #emep_o3[:240,173,79]
    #ax1.plot(emep_no2[:,173,79], color='blue', label="NO2")
    #ax2.plot(emep_c5h8[:,173,79], color='orange', label="C5H8")
    ax2.plot(emep_hcho[:,1,1], color='orange', label="emep_hcho")
    ax2.plot(1000*wrfc_hcho[:,1,1,1], color='violet', label="wrfchem_hcho")

    #ax2.plot(AxisA_April2020.values, color='black', label="AxisK")
    ax1.set_xlabel("days")
    ax1.set_ylabel("ppb", size="medium")
    ax2.set_ylabel("ppb", size="medium")
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    #ax1.set_xlim(0, 240)
    ax1.set_ylim(0, 50)
    plt.suptitle("daily HCHO sim")#, Vienna region", size="large")#+"2m air temperature"))
    #myFmt = matplotlib.dates.DateFormatter("%d")
    #ax1.xaxis.set_major_formatter(myFmt)
    #fig1.autofmt_xdate()
    #plt.show()

    x=emep_hcho[:,173,79]
    y=AxisA_April2020d.values[:26]

    fig2a = plt.figure()
    plt.scatter(x,y, color='orange',label=r"$r$=%.2f" % (R_hcho))
    plt.ylabel("emep_hcho [ppb]", size="medium")
    plt.xlabel("maxd_hcho [DSCD]", size="medium")
    m,b = np.polyfit(x,y,1)
    plt.plot(x, m * x+b)
    ax2.legend(loc='upper right')
    plt.suptitle("HCHO mod vs. obs (daily values)")
    plt.show()

    x1 = wrfchem_hcho[:, 1, 1, 1]
    y1 = AxisA_April2020h.values[:]

    #fig2b = plt.figure()
    #plt.scatter(x1, y1, color='orange')#, label=r"$r$=%.2f" % (R_hcho2))
    #plt.ylabel("wrfc_hcho [ppb]", size="medium")
    #plt.xlabel("maxd_hcho [DSCD]", size="medium")
    #m, b = np.polyfit(x1, y1, 1)
    #plt.plot(x1, m * x1 + b)
    #ax2.legend(loc='upper right')
    #plt.suptitle("HCHO mod vs. obs (hourly values)")
    #plt.show()

except:
    print("Oops!", sys.exc_info()[0], "occured.")
    pass
