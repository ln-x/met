# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.dates
import matplotlib.pyplot as plt
from scipy import stats
import sys

path = '/media/heidit/'  # '/media/lnx'
outpath = path + 'Norskehavet/EMEPData/OUTPUT/2020_4'
file = path + 'Norskehavet/EMEPData/OUTPUT/2020_4/JanBASESIM_4b_day.nc'
file2 = path + 'Norskehavet/EMEPData/OUTPUT/2020_4/wrfout_d01_2020-03-31_01:00:00'

fh = Dataset(file, mode='r')
fh2 = Dataset(file2, mode='r')

lons = fh.variables['lon'][1]
lats = fh.variables['lat'][1]
c5h8 = fh.variables['SURF_ppb_C5H8']
c5h8_units = fh.variables['SURF_ppb_C5H8'].units
o3 = fh.variables['SURF_ppb_O3']
o3_units = fh.variables['SURF_ppb_O3'].units
no2 = fh.variables['SURF_ppb_NO2']
no2_units = fh.variables['SURF_ppb_NO2'].units


LON = fh2.variables['XLONG'][1]
LAT = fh2.variables['XLAT'][1]
T2 = fh2.variables['T2']
SM = fh2.variables['SMOIS'][:,:,:,:]  #SMOIS, SH20
SM_units = fh2.variables['SMOIS'].units
EBIO_ISO = fh2.variables['EBIO_ISO']
EBIO_ISO_units = fh2.variables['EBIO_ISO'].units
EBIO_API = fh2.variables['EBIO_API']

'''calculation of Regression coefficients'''
# print stats.spearmanr(ZAMG_heatdays, WRFdata_heatdays, axis=0)
#R2_Forc_emission = (stats.spearmanr(EBIO_ISO, T2))[0] ** 2
#R2_Forc_NO2concentr = (stats.spearmanr(o3, no2))[0] ** 2
#R2_Forc_c5h8concentr = (stats.spearmanr(o3, c5h8))[0] ** 2

# print i, R2_Forc_i

'''
Plotting
'''

try:
    fig1 = plt.figure()
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    ax1.plot(o3[:240,173,79], color='violet', label="O3")
    ax1.plot(no2[:240,173,79], color='blue', label="NO2")
    ax2.plot(c5h8[:240,173,79], color='orange', label="C5H8")
    ax1.set_xlabel("days")
    ax1.set_ylabel("ppb", size="medium")
    ax2.set_ylabel("ppb", size="medium")
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    #ax1.set_xlim(0, 240)
    ax1.set_ylim(0, 50)
    plt.suptitle("EMEP, 1-10 April 2020")#, Vienna region", size="large")#+"2m air temperature"))
    #myFmt = matplotlib.dates.DateFormatter("%d")
    #ax1.xaxis.set_major_formatter(myFmt)
    #fig1.autofmt_xdate()
    plt.show()

    fig2a = plt.figure()
    plt.scatter(c5h8[:240,173,79], o3[:240,173,79], color='orange', label='c5h5')#, label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
    #ax2.set_xlabel(r"$T_{air_2m}$"u'[°C]', size="large")
    #ax2.set_ylabel("O3 [ppb]", size="large")
    #ax2.set_xlim(0, 10)
    plt.legend(loc='upper right')
    plt.ylabel("O3 [ppb]", size="medium")
    plt.xlabel("C5H8 [ppb]", size="medium")
    ax2.legend(loc='upper right')
    plt.suptitle("EMEP, 1-10 April 2020")#, Vienna region", size="large")#+"2m air temperature"))
    ##figname = outpath + i + "WRFTEBZAMG.png"
    ##plt.savefig(figname)
    plt.show()

    fig2b = plt.figure()
    plt.scatter(no2[:240,173,79], o3[:240,173,79], color='blue', label='no2')#, label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i2, Bias_Forc_i2)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
    #ax2.set_xlabel(r"$T_{air_2m}$"u'[°C]', size="large")
    #ax2.set_ylabel("O3 [ppb]", size="large")
    #ax2.set_xlim(0, 10)
    plt.legend(loc='upper right')
    plt.ylabel("O3 [ppb]", size="medium")
    plt.xlabel("NO2 [ppb]", size="medium")
    ax2.legend(loc='upper right')
    plt.suptitle("EMEP, 1-10 April 2020")#, Vienna region", size="large")#+"2m air temperature"))
    ##figname = outpath + i + "WRFTEBZAMG.png"
    ##plt.savefig(figname)
    plt.show()
except:
    print("Oops!", sys.exc_info()[0], "occured.")
    pass

'''
fig3 = plt.figure()
ax1 = plt.gca()
ax2 = ax1.twinx()
#plt.plot(c5h8[:10,150,79], color='orange', label="C5H8")
ax1.plot(EBIO_ISO[:240,113,63], color='pink', label="EISO")
ax1.plot(EBIO_API[:240,113,63], color='yellow', label="EAPI")
ax1.set_ylabel("[mol km-1 h-1]", size="medium")
ax1.legend(loc='upper left')
#plt.plot(o3[:10, 150, 79], color='violet', label="O3")
#ax2.plot(SM[:10,150,79], color='blue', label="SM")
#ax2.set_ylabel("[m3 m-3]", size="medium")
ax2.plot(T2[:240,113,63]-273.15, color='red', label="T2")
#ax2.set_ylim(0, 5)
ax2.set_ylabel("[degC]", size="medium")
ax2.legend(loc='lower right')
plt.suptitle("WRF-Chem, 1-10 April 2020")  # , Vienna region", size="large")#+"2m air temperature"))
plt.show()

fig4 = plt.figure()

#plt.scatter(EBIO_ISO[:10,150,79], SM[:10,150,79], color='orange', label='SM')
plt.scatter(EBIO_ISO[:240,113,63], (T2[:240,113,63]-273.15), color='blue', label='r(T2)')#, "$R^2$=%.2f")') % (R2_Forc_emission) # , Bias=%.2f" % (R2_Forc_i2, Bias_Forc_i2)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
plt.xlabel("EBIO_ISO [mol km-1 h-1]", size="large")
plt.ylabel(r"$T_{air_2m}$"u'[°C]', size="large")
plt.suptitle("WRF-Chem, 1-10 April 2020")  # , Vienna region", size="large")#+"2m air temperature"))
    ##figname = outpath + i + "WRFTEBZAMG.png"
    ##plt.savefig(figname)
plt.show()


fig3 = plt.figure()
ax1 = plt.gca()
ax2 = ax1.twinx()
#plt.plot(c5h8[:10,150,79], color='orange', label="C5H8")
ax1.plot(EBIO_ISO[:240,113,63], color='pink', label="EISO")
ax1.plot(EBIO_API[:240,113,63], color='yellow', label="EAPI")
ax1.set_ylabel("[mol km-1 h-1]", size="medium")
ax1.legend(loc='upper left')
#plt.plot(o3[:10, 150, 79], color='violet', label="O3")
ax2.plot(SM[:240,3,113,63], color='black', label="SM4")
ax2.plot(SM[:240,2,113,63], color='darkblue', label="SM3")
ax2.plot(SM[:240,1,113,63], color='blue', label="SM2")
ax2.plot(SM[:240,0,113,63], color='lightblue', label="SM1")
ax2.set_ylim(0.10, 0.35)
ax2.set_ylabel("soil moisture [m3 m-3]", size="medium")
ax2.legend(loc='lower right')
plt.suptitle("WRF-Chem, 1-10 April 2020")  # , Vienna region", size="large")#+"2m air temperature"))
plt.show()
'''
fh.close()
fh2.close()



