# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import numpy as np
import csv
import pandas as pd
from datetime import datetime
import matplotlib.dates
import matplotlib.pyplot as plt
from scipy import stats
import sys
import os
import ReadinVINDOBONA

outpath ='/media/lnx/Norskehavet/EMEPData/OUTPUT/2020_4'
#file = '/media/lnx/Norskehavet/EMEPData/OUTPUT/2020_4/JanBASESIM_4b_day.nc'
#file2 = '/media/lnx/Norskehavet/EMEPData/OUTPUT/2020_4/wrfout_d01_2020-03-31_01:00:00'
file3 = '/media/lnx/Norskehavet/EMEPData/OUTPUT/emep-ctm-2020_3/JanBASESIM_3_hourInst.nc'
fh3 = Dataset(file3, mode='r')
o3 = fh3.variables['SURF_ppb_O3']
o3_units = fh3.variables['SURF_ppb_O3'].units
#no2 = fh3.variables['SURF_ppb_NO2']
#no2_units = fh3.variables['SURF_ppb_NO2'].units

'''
file2 = '/media/lnx/Norskehavet/EMEPData/OUTPUT/2020_3CAMS/wrfout_d02_2020-03-01_01:00:00'
file3CAMS = '/media/lnx/Norskehavet/EMEPData/OUTPUT/2020_3CAMS/JanBASESIM_3_CAMS_day.nc'
file4CAMS = '/media/lnx/Norskehavet/EMEPData/OUTPUT/2020_4CAMS/JanBASESIM_4_CAMS_day.nc'

#fh = Dataset(file, mode='r')
fh2 = Dataset(file2, mode='r')
CAMS3 = Dataset(file3CAMS, mode='r')
CAMS4 = Dataset(file4CAMS, mode='r')
hcho = Dataset(hcho, mode='r')

lons = CAMS3.variables['lon'][1]
lats = CAMS3.variables['lat'][1]
c5h8 = CAMS3.variables['SURF_ppb_C5H8']
c5h8_units = CAMS3.variables['SURF_ppb_C5H8'].units
o3 = CAMS3.variables['SURF_ppb_O3']
o3_units = CAMS3.variables['SURF_ppb_O3'].units
no2 = CAMS3.variables['SURF_ppb_NO2']
no2_units = CAMS3.variables['SURF_ppb_NO2'].units

LON = fh2.variables['XLONG'][1]
LAT = fh2.variables['XLAT'][1]
T2 = fh2.variables['T2']
SM = fh2.variables['SMOIS'][:,:,:,:]  #SMOIS, SH20
SM_units = fh2.variables['SMOIS'].units
EBIO_ISO = fh2.variables['EBIO_ISO']
EBIO_ISO_units = fh2.variables['EBIO_ISO'].units
EBIO_API = fh2.variables['EBIO_API']
'''

'''read in air pollution csv data'''


#A23	A23 S�dosttangente-Wehlistra�e
#AKC	AKH
#BELG	Belgradplatz
#FLO	Floridsdorf
#GAUD	Gaudenzdorf
#24   JAEG	Hermannskogel
#MBA	Hietzinger Kai
#25   ZA	Hohe Warte
#KE	Kaiser-Ebersdorf
#KEND	Kendlerstra�e
#LIES	Liesing - Gewerbegebiet
#26   LOB	Lobau
#SCHA	Schafberg
#STAD	Stadlau
#27     STEF	Stephansplatz
#TAB	Taborstra�e
#35 LAA

no2_meas = pd.read_csv('/home/lnx/DATACHEM/Luftmessnetz/NO2_HMW_2017-19.4.2020.csv')
no2_meas_ppb = no2_meas*1.88 #for 1atm, 25degC! Exact it would be: ppb*12.187*(molar mass)/(273.15+degC)
#print no2_pd['STEF']
#print no2_meas.head()
#pd.to_datetime(no2_pd)
#no2_meas['timestamp.MEZ'] = no2_meas[(no2_meas['timestamp.MEZ'] >= datetime(2020,02,29))]   #&(no2_pd.Timestamp <= datetime(2020,04,30))
no2_meas2 = no2_meas_ppb[54048:55439]
no2_meas2b = no2_meas2[0::2]

no2_meas3 = no2_meas_ppb[55440:56928]
no2_meas3b = no2_meas3[0::2]

no2_meas4 = no2_meas_ppb[56928:]
no2_meas4b = no2_meas4[0::2]

no_meas = pd.read_csv('/home/lnx/DATACHEM/Luftmessnetz/NO_HMW_2017-19.4.2020.csv')
no_meas_ppb = no2_meas*1.25
no_meas2 = no_meas_ppb[54048:55439]
no_meas2b = no_meas2[0::2]

no_meas3 = no_meas_ppb[55440:56928]
no_meas3b = no_meas3[0::2]

no_meas4 = no_meas_ppb[56928:]
no_meas4b = no_meas4[0::2]


o3_meas = pd.read_csv('/home/lnx/DATACHEM/Luftmessnetz/O3_HMW_1.1.2015_19.4.2020.csv')
o3_meas_ppb = o3_meas * 2.0
o3_meas3 = o3_meas_ppb[90528:92018]
o3_meas3b = o3_meas3[0::2]

#print o3_meas3['HMW.O3.0101.03.ug.m3..'].values

#o3_meas4 = o3_meas[92016:]
#o3_meas4b = o3_meas4[0::2]

#print o3_meas["STEF"]
#print o3_meas["HMW.O3.0101.03.ug.m3.."]

#list(o3_meas.columns.values)

"read in VINDOBONA"

foldername = "/home/lnx/DATACHEM/StefanSchreier/2001_2004_DQ_91_HCHO_mixing_ratio/"
files = os.listdir(foldername)
# print files
julianday = 0
hcho = []
for i in files:
    julianday += 1
    # filename = "200101DQ_91_HCHO_mixing_ratio.asc"
    thedata = ReadinVINDOBONA.loadfile(foldername=foldername, filename=i, julianday=julianday)
    # print 'loaded: '
    for d in thedata:
        hcho.append = d

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
    fig0 = plt.figure()
    plt.plot(hcho)
    plt.show()

    exit()

    fig1 = plt.figure()
    #ax1 = plt.gca()
    #ax2 = ax1.twinx()
    plt.plot(o3_meas3b['HMW.O3.0101.03.ug.m3..'].values, color='violet', label = "O3_obs")
    #plt.plot(o3_meas4b['HMW.O3.0101.03.ug.m3..'].values, color='violet')
    plt.plot(o3[:,150,79], color='violet', label="O3_sim", linestyle="dotted")
    #plt.plot(no2[:,150,79], color='blue', label="NO2_sim", linestyle="dotted")
    #ax2.plot(c5h8[:240,173,79], color='orange', label="C5H8_sim", linestyle="dotted")
    plt.plot(no2_meas3b['STEF'].values, color='blue', label = "no2_obs" )
    #ax1.plot(no2_meas4b['STEF'].values, color='blue')
    plt.plot(no_meas3b['STEF'].values, color='green', label = "no_obs" )
    #ax1.plot(no_meas4b['STEF'].values, color='green' )
    plt.xlabel("days")
    plt.ylabel("ug m3", size="medium")
    #ax2.set_ylabel("ppb", size="medium")
    plt.legend(loc='upper left')
    #ax2.legend(loc='upper right')
    #ax1.set_xlim(0, 240)
    #ax1.set_ylim(0, 50)
    plt.title("EMEP, March 2020")#, Vienna region", size="large")#+"2m air temperature"))
    #myFmt = matplotlib.dates.DateFormatter("%d")
    #ax1.xaxis.set_major_formatter(myFmt)
    #fig1.autofmt_xdate()
    plt.show()
except:
    print("Oops!", sys.exc_info()[0], "occured.")
    pass
'''
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
'''


exit()

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



