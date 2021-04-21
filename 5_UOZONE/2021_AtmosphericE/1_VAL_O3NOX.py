# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import netCDF4
import numpy as np
import csv
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.dates
import matplotlib.pyplot as plt
from scipy import stats
import sys
import os
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd


'''READ IN BOKU Metdata'''
BOKUMetData = met.library.BOKUMet_Data.BOKUMet()
#DAILY MEANS
BOKUMetData_dailysum = BOKUMetData.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean,
                                                      'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
#JULIAN DAY
BOKUMetData_dailysum['JD'] = (BOKUMetData_dailysum.index)
f = lambda x: datestdtojd(str(x)[:-9])
BOKUMetData_dailysum['JD'] = BOKUMetData_dailysum['JD'].apply(f)

#print(BOKUMetData_dailysum["AT"])
#exit()

'''READ IN UBA air pollution data (HMW)'''
#pathbase = "/home/lnx/DATACHEM/Luftmessnetz/" #Thinkpad Lenovo
pathbase = "/windata/Google Drive/DATA/obs_point/chem/UBA/" #imph
#no2_meas = pd.read_csv(pathbase + 'NO2 NO HMW 2009.dat')
#no2_meas = pd.read_csv(pathbase + 'NO2 NO HMW 2010.dat')
#no2_meas = pd.read_csv(pathbase + 'NO2 NO HMW 2011.dat')
#no2_meas = pd.read_csv(pathbase + 'NO2 NO HMW 2012.dat')
#no2_meas = pd.read_csv(pathbase + 'NO2 NO HMW 2013.dat')
#no2_meas = pd.read_csv(pathbase + 'NO2 NO HMW 2014.dat')
#no2_meas = pd.read_csv(pathbase + 'NO2_HMW_2015-2016.csv')
no2_meas = pd.read_csv(pathbase + 'NO2_HMW_2017-19.4.2020.csv') #ppb *1.88 ##for 1atm, 25degC! Exact it would be: ppb*12.187*(molar mass)/(273.15+degC)
#no2_Feb = no2_meas[54048:55439::2]
#no2_Mar = no2_meas[55440:56928]
no2_Apr =no2_meas[56927::2]  #1.4. 0h - 19.4. 23h 2020
#no_meas = pd.read_csv(pathbase + 'NO_HMW_2015-2016.csv')
no_meas = pd.read_csv(pathbase + 'NO_HMW_2017-19.4.2020.csv') #ppb= *1.25
no_Apr = no_meas[56928::2]  #1.4. 0h - 19.4. 23h 2020

#o3_meas = pd.read_csv(pathbase + 'O3 HMW 2009.dat')
#o3_meas = pd.read_csv(pathbase + 'O3 HMW 2010.dat')
#o3_meas = pd.read_csv(pathbase + 'O3 HMW 2011.dat')
#o3_meas = pd.read_csv(pathbase + 'O3 HMW 2012.dat')
#o3_meas = pd.read_csv(pathbase + 'O3 HMW 2013.dat')
#o3_meas = pd.read_csv(pathbase + 'O3 HMW 2014.dat')
o3_meas = pd.read_csv(pathbase + 'O3_HMW_1.1.2015_19.4.2020.csv') #ppb = *2.0
o3_Apr = o3_meas[92016::2]
#print(o3_Apr["HMW.O3.0101.03.ug.m3.."])
#list(o3_meas.columns.values)
#print(o3_Apr)

'''READ IN EEA air pollution data'''
pathbase2 = "/windata/Google Drive/DATA/obs_point/chem/EEA/"
#"AT"+compound+"stationsname"+"year"+_"timeseries.csv"
nox_1990_2019_da = pd.read_csv(pathbase2 + "nox_da_1990-2019_AT_ppb.csv")
nox_1990_2019_da = nox_1990_2019_da.set_index(pd.to_datetime(nox_1990_2019_da['date']))
nox_1990_2019_da = nox_1990_2019_da.drop(columns=['date'])
no2_2020_mda1 = pd.read_csv(pathbase2 + "AT_NO2_2020.csv")
no2_2020_mda1 = no2_2020_mda1.set_index(pd.to_datetime(no2_2020_mda1['date']))
no2_2020_da = no2_2020_mda1.resample('D').mean()

no_2020_mda1 = pd.read_csv(pathbase2 + "AT_NO_2020.csv")
no_2020_mda1 = no_2020_mda1.set_index(pd.to_datetime(no_2020_mda1['date']))
no_2020_da = no_2020_mda1.resample('D').mean()

nox_2020_da = no_2020_da.add(no2_2020_da)
#print(nox_2020_da)
#nox_2020_da = nox_2020_mda1.resample('D').mean()
nox_1990_2020_da = pd.concat([nox_1990_2019_da, nox_2020_da], axis=0)
#print(nox_1990_2020_da['AT900ZA'])
#print(nox_1990_2020_da.columns)
#exit()

o3_1990_2019_mda1 = pd.read_csv(pathbase2 + "o3_mda1_1990-2019_AT_mug.csv")
o3_1990_2019_mda1 = o3_1990_2019_mda1.set_index((pd.to_datetime(o3_1990_2019_mda1['date'])))
o3_1990_2019_mda1 = o3_1990_2019_mda1.drop(columns=['date'])
o3_1990_2019_mda8 = pd.read_csv(pathbase2 + "o3_mda8_1990-2019_AT_mug.csv")
o3_1990_2019_mda8 = o3_1990_2019_mda8.set_index(pd.to_datetime(o3_1990_2019_mda8['date']))
o3_1990_2019_mda8 = o3_1990_2019_mda8.drop(columns=['date'])
o3_2020_mda1 = pd.read_csv(pathbase2 + "AT_O3_2020.csv")
o3_2020_mda1 = o3_2020_mda1.set_index(pd.to_datetime(o3_2020_mda1['date']))
o3_2020_mda1 = o3_2020_mda1.drop(columns=['date'])
o3_1990_2020_mda1 = pd.concat([o3_1990_2019_mda1, o3_2020_mda1], axis=0)
o3_1990_2020_da = o3_1990_2020_mda1.resample('D').mean()
#print(o3_1990_2020_da["AT90LOB"])
#o3_1990_2020_da["AT90LOB"].plot()
#plt.show()


'''READ IN EMEP data'''
#Jans indexes for Vienna gridpoint:
wrf_vie_i=109 #TODO Double check! i=x=long
wrf_vie_j=58  #TODO Double check! j=y=lat

path = '/media/heidit/'  # '/media/lnx'
file = path + 'Norskehavet/EMEPData/OUTPUT/file_MarApr.nc'
#file = path + 'Norskehavet/EMEPData/OUTPUT/2020_4/JanBASESIM_4b_day.nc'
file1 = path + 'Norskehavet/EMEPData/OUTPUT/2020_4/JanBASESIM_4b_hourInst.nc'
fh = Dataset(file, mode='r')
fh1 = Dataset(file1, mode='r')
lons = fh.variables['lon'][1]
lats = fh.variables['lat'][1]
emep_time = fh.variables['time']
c5h8 = fh.variables['SURF_ppb_C5H8'][:,wrf_vie_j, wrf_vie_i]
emep_o3_d = fh.variables['SURF_ppb_O3'][:,wrf_vie_j,wrf_vie_i] #(time, j, i)
jd = netCDF4.num2date(emep_time[:],emep_time.units)
emep_o3_d = pd.Series(emep_o3_d[:],index=jd)
emep_o3_h = fh1.variables['SURF_ppb_O3']

emep_no_d = fh.variables['SURF_ppb_NO'][:,wrf_vie_j,wrf_vie_i]
emep_no_d = pd.Series(emep_no_d[:], index=jd)
emep_no2_d = fh.variables['SURF_ppb_NO2'][:,wrf_vie_j,wrf_vie_i]
emep_no2_d = pd.Series(emep_no2_d[:], index=jd)

emep_nox_d = emep_no_d.add(emep_no2_d)

'''READ IN WRFChem data'''
file2 = path + 'Norskehavet/EMEPData/OUTPUT/2020_4/wrfout_d01_2020-03-31_01:00:00'
file3 = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era-interim/HCera_9km_2007-16_ATTR/wrfout_d01_2013-01-09_01_2014-09-01_01_ex.nc'
fh2 = Dataset(file2, mode='r')
fh3 = Dataset(file3, mode='r')
#fh3 = fh2
LON = fh2.variables['XLONG'][1]
LAT = fh2.variables['XLAT'][1]
"""
wrfc_time = fh2.variables['XTIME']
#wrfc_jd = netCDF4.num2date(wrfc_time[:],wrfc_time.units)

T2 = fh2.variables['T2']
wrfc_o3 = fh2.variables["o3"][:,1,wrf_vie_j,wrf_vie_i] #(Time, bottom_top, spith_north, west_east O3 mixing ratio: ppmv!
print(type(wrfc_jd)) #<class 'numpy.ma.core.MaskedArray'>
wrfc_o32020 = pd.Series(wrfc_o3[:],index=wrfc_jd)
#wrfc_o3_d =wrfc_o3.resample('D').mean() #TODO Only valid with DatetimeIndex, TimedeltaIndex or PeriodINdex, but got instance of 'Index'
wrfc_no2 = fh2.variables["no2"][:,1,wrf_vie_j,wrf_vie_i] #(Time, bottom_top, spith_north, west_east O3 mixing ratio: ppmv!
wrfc_no = fh2.variables["no"][:,1,wrf_vie_j,wrf_vie_i] #(Time, bottom_top, spith_north, west_east O3 mixing ratio: ppmv!
wrfc_ho = fh2.variables["ho"][:,1,wrf_vie_j,wrf_vie_i] #(Time, bottom_top, spith_north, west_east O3 mixing ratio: ppmv!
#wrfc_ho = pd.Series(wrfc_ho[:],index=wrfc_jd)
wrfc_ho2 = fh2.variables["ho2"][:,1,wrf_vie_j,wrf_vie_i] #hydroperoxyl
#wrfc_ho2 = pd.Series(wrfc_ho2[:],index=wrfc_jd)
wrfc_hcho = fh2.variables["hcho"][:,1,wrf_vie_j,wrf_vie_i]
wrfc_iso = fh2.variables["iso"][:,1,wrf_vie_j,wrf_vie_i]
SM = fh2.variables['SMOIS'][:,:,:,:]  #SMOIS, SH20
SM_units = fh2.variables['SMOIS'].units
EBIO_ISO = fh2.variables['EBIO_ISO']
EBIO_ISO_units = fh2.variables['EBIO_ISO'].units
EBIO_API = fh2.variables['EBIO_API']
#print(len(wrfc_o3[1,1]))  #shape(39,165,189
"""
starttime = datetime(2013, 1, 9, 1, 00)
wrfc_time_construct = np.array([starttime + timedelta(hours=i) for i in range(14400)])

wrfc_o3 = fh3.variables["o3"][:,0,0,0]  #print(type(wrfc_jd)) #<class 'numpy.ma.core.MaskedArray'>
wrfc_o3 = pd.Series(wrfc_o3[:],index=wrfc_time_construct) #wrfc_o3_d =wrfc_o3.resample('D').mean() #TODO Only valid with DatetimeIndex, TimedeltaIndex or PeriodINdex, but got instance of 'Index'
wrfc_o3_d =wrfc_o3.resample('D').mean()

wrfc_no2 = fh3.variables["no2"][:,0,0,0] #(Time, bottom_top, spith_north, west_east O3 mixing ratio: ppmv!
wrfc_no2 = pd.Series(wrfc_no2[:],index=wrfc_time_construct)
wrfc_no2_d =wrfc_no2.resample('D').mean()

wrfc_no = fh3.variables["no"][:,0,0,0] #(Time, bottom_top, spith_north, west_east O3 mixing ratio: ppmv!
wrfc_no = pd.Series(wrfc_no[:],index=wrfc_time_construct)
wrfc_no_d =wrfc_no.resample('D').mean()

wrfc_nox_d = wrfc_no_d.add(wrfc_no2_d)

wrfc_ho = fh3.variables["ho"][:,0,0,0] #(Time, bottom_top, spith_north, west_east O3 mixing ratio: ppmv!
wrfc_ho = pd.Series(wrfc_ho[:],index=wrfc_time_construct)
wrfc_ho2 = fh3.variables["ho2"][:,0,0,0] #hydroperoxyl
wrfc_ho2 = pd.Series(wrfc_ho2[:],index=wrfc_time_construct)
wrfc_hcho = fh3.variables["hcho"][:,0,0,0]
wrfc_iso = fh3.variables["iso"][:,0,0,0]
EBIO_ISO = fh3.variables["EBIO_ISO"][:,0,0]
T2 = fh3.variables["T2"][:,0,0]
wrfc_T2 = pd.Series(T2[:],index=wrfc_time_construct)
wrfc_T2_d =wrfc_T2.resample('D').mean()

SWDOWN = fh3.variables["SWDOWN"][:,0,0]
wrfc_swd = pd.Series(SWDOWN[:],index=wrfc_time_construct)
wrfc_swd_d =wrfc_swd.resample('D').mean()

V10 = fh3.variables["V10"][:,0,0]
"""
'''calculation of Regression coefficients'''
# print stats.spearmanr(ZAMG_heatdays, WRFdata_heatdays, axis=0)
#R2_Forc_emission = (stats.spearmanr(EBIO_ISO, T2))[0] ** 2
#R2_Forc_NO2concentr = (stats.spearmanr(o3, no2))[0] ** 2
#R2_Forc_c5h8concentr = (stats.spearmanr(o3, c5h8))[0] ** 2
# print i, R2_Forc_i
"""
'''
Plotting
'''
fig = plt.figure()
plt.suptitle("1990-2020, OBS/MOD")
start = datetime(2013, 1, 1, 00, 00)
end = datetime(2014, 12, 1, 00, 00)
ax1 = fig.add_subplot(311)
ax1 = plt.gca()
#date, AT90A23, AT90AKC, AT9BELG, AT90FLO, AT9GAUD, AT9JAEG, AT90MBA, AT900ZA, AT900KE, AT9KEND, AT9LIES, AT90LOB, AT9SCHA, AT9STAD, AT9STEF, AT90TAB
#nox_1990_2019_da["AT9STEF"].plot()
ax1.plot(nox_1990_2020_da['AT9JAEG'][start:end], color='violet', label="nox_obs_da_JAEG")
ax1.plot(nox_1990_2020_da['AT900ZA'][start:end], color='blue', label="nox_obs_da_00ZA")
ax1.plot(nox_1990_2020_da['AT90LOB'][start:end], color='green', label="nox_obs_da_LOB")
ax1.plot(nox_1990_2020_da['AT9STEF'][start:end], color='darkgrey', label="nox_obs_da_STEF")
ax1.plot(wrfc_nox_d*1000, color='blue', label="nox_wrfc_d", linestyle="dashed")
#ax1.plot(emep_o3[:,109,58], color='green', label="O3_emep_d", linestyle="dashed")
ax1.set_xlabel("days")
ax1.set_ylabel("ppb", size="medium")
ax1.legend(loc='upper right')

ax1 = fig.add_subplot(312)
ax1 = plt.gca()
#ax2 = ax1.twinx()
ax1.plot((o3_1990_2020_da['AT9JAEG'][start:end])*2, color='violet', label="o3_obs_da_JAEG") #TODO: Umrechnen korrekt ug/m³ -> ppb! (anstelle *2)
ax1.plot((o3_1990_2020_da['AT900ZA'][start:end])*2, color='blue', label="o3_obs_da_00ZA")
ax1.plot((o3_1990_2020_da['AT90LOB'][start:end])*2, color='green', label="o3_obs_da_0LOB")
ax1.plot((o3_1990_2020_da['AT9STEF'][start:end])*2, color='darkgrey', label="o3_obs_da_STEF")
ax1.plot(wrfc_o3_d*1000,color='blue', label="o3_wrfc_d", linestyle="dashed")
#ax1.plot((emep_no[:,109,58]) + (emep_no2[:,109,58]), color='green', label="nox_emep_d", linestyle="dashed")
#EMEP
ax1.set_xlabel("days")
ax1.set_ylabel("ppb", size="medium")
ax1.legend(loc='upper right')

ax1 = fig.add_subplot(313)
ax1 = plt.gca()
ax2 = ax1.twinx()
#ax1.plot((o3_1990_2020_da['AT9STEF'][start:end])*2, color='darkgrey', label="o3_obs_da_STEF")
ax1.plot(wrfc_swd_d, color='yellow', label="sw_down_wrfc", linestyle="dashed")
ax2.plot(wrfc_T2_d-273.15, color='red', label="T2_wrfc", linestyle="dashed")
ax1.set_xlabel("days")
ax1.set_ylabel("W m-2", size="medium")
ax2.set_ylabel("degC", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()

exit()

fig = plt.figure()
start = datetime(2020, 1, 1, 00, 00)
end = datetime(2020, 4, 30, 00, 00)
plt.suptitle("2020 - OBS, daily value")
ax1 = fig.add_subplot(311)
ax1 = plt.gca()
ax1.plot((o3_1990_2020_da["AT9JAEG"][start:end])*2, color='violet', label="O3_obs_d_jaeg")
ax1.plot((o3_1990_2020_da["AT900ZA"][start:end])*2, color='blue', label="O3_obs_d_za")
ax1.plot((o3_1990_2020_da["AT90LOB"][start:end])*2, color='green', label="O3_obs_d_lob") #TODO: Umrechnen korrekt ug/m³ -> ppb! (anstelle *2)
ax1.plot((o3_1990_2020_da["AT9STEF"][start:end])*2, color='grey', label="O3_obs_d_stef")
ax1.plot(wrfc_o32020*1000, color='blue', label="O3_wrfc_h", linestyle="dashed")
ax1.plot(emep_o3_d, color='green', label="O3_emep_d", linestyle=":")
#ax1.plot(emep_o3[:,109,58], color='green', label="O3_emep_d", linestyle="dashed")
ax1.set_xlabel("days")
ax1.set_ylabel("ppb", size="medium")
ax1.legend(loc='upper left')


ax1 = fig.add_subplot(312)
ax1 = plt.gca()
ax1.plot(nox_1990_2020_da['AT9JAEG'][start:end], color='violet', label = "nox_obs_d_jaeg" )
ax1.plot(nox_1990_2020_da['AT900ZA'][start:end], color='blue', label = "nox_obs_d_za" )
ax1.plot(nox_1990_2020_da['AT90LOB'][start:end], color='green', label = "nox_obs_d_lob" )
ax1.plot(nox_1990_2020_da['AT9STEF'][start:end], color='grey', label = "nox_obs_d_stef" )
ax1.plot(emep_nox_d, color='green', label="nox_emep_d", linestyle="dashed")
ax1.set_xlabel("days")
ax1.set_ylabel("ppb", size="medium")
#ax1.set_ylabel("mg m-2 h-1", size="medium")
#ax2.set_ylabel("degC", size="medium")
ax1.legend(loc='upper left')
#ax2.legend(loc='upper right')
#ax1.set_ylim(0, 5)
#ax2.set_ylim(10, 50)

ax1 = fig.add_subplot(313)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(wrfc_ho, color='blue', label="wrfc_oh, hydroxide", linestyle="dotted")
ax2.plot(wrfc_ho2, color='green', label="wrfc_ho2, hydroperoxyl", linestyle="dashed")
ax1.set_xlabel("days")
ax1.set_ylabel("ppmv", size="medium")
ax2.set_ylabel("ppmv", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()

exit()

fig = plt.figure()
plt.suptitle("Apr2020 - OBS vs MOD, hourly value")
#fig.set_size_inches(3.39,2.54)
ax1 = fig.add_subplot(211)
ax1 = plt.gca()
ax1.plot(o3_Apr['Timestamp..MEZ.'][:456], (o3_Apr['HMW.O3.ZA.09.ug.m3..'].values)*2.0, color='blue', label="O3_obs_h_za")
ax1.plot(o3_Apr['Timestamp..MEZ.'][:456], (o3_Apr['HMW.O3.LOB.09.ug.m3..'].values)*2.0, color='green', label="O3_obs_h_lob")
ax1.plot(o3_Apr['Timestamp..MEZ.'][:456], (o3_Apr['HMW.O3.JAEG.09.ug.m3..'].values)*2.0, color='violet', label="O3_obs_h_jaeg")
ax1.plot(o3_Apr['Timestamp..MEZ.'][:456], (o3_Apr['HMW.O3.STEF.09.ug.m3..'].values)*2.0, color='grey', label="O3_obs_h_stef")
ax1.plot(o3_Apr['Timestamp..MEZ.'][:456],(wrfc_o3[:456,109,58])*1000, color='blue', label="O3_wrfc_h", linestyle="dashed")
ax1.plot(o3_Apr['Timestamp..MEZ.'][:456],emep_o3_h[:456,109,58], color='green', label="O3_emep_h", linestyle=":")
#ax1.plot(emep_o3[:,109,58], color='green', label="O3_emep_d", linestyle="dashed")
ax1.set_xlabel("days")
ax1.set_ylabel("ppb", size="medium")
#ax1.set_ylabel("mg m-2 h-1", size="medium")
ax1.legend(loc='upper center')
#ax1.set_ylim(0, 5)

ax1 = fig.add_subplot(212)
ax1 = plt.gca()
#ax2 = ax1.twinx() #JAEG, LOB, ZA, STEF
ax1.plot(no2_Apr['timestamp.MEZ'][:456],(no_Apr['ZA'][:456].values)*1.25+(no2_Apr['ZA'][:456].values)*1.88, color='blue', label = "nox_obs_h_za" )
ax1.plot(no2_Apr['timestamp.MEZ'][:456],(no_Apr['JAEG'][:456].values)*1.25+(no2_Apr['JAEG'][:456].values)*1.88, color='violet', label = "nox_obs_h_jaeg" )
ax1.plot(no2_Apr['timestamp.MEZ'][:456],(no_Apr['LOB'][:456].values)*1.25+(no2_Apr['LOB'][:456].values)*1.88, color='green', label = "nox_obs_h_lob" )
ax1.plot(no2_Apr['timestamp.MEZ'][:456],(no_Apr['STEF'][:456].values)*1.25+(no2_Apr['STEF'][:456].values)*1.88, color='grey', label = "nox_obs_h_stef" )
ax1.plot(no2_Apr['timestamp.MEZ'][:456],(wrfc_no[:456,109,58])*1000 + (wrfc_no2[:456,109,58])*1000, color='blue', label="nox_wrfc_h", linestyle="dotted")
#ax1.plot((emep_no[:,109,58]) + (emep_no2[:,109,58]), color='green', label="nox_emep_d", linestyle="dashed")
#WRFCHEM
#EMEP
ax1.set_xlabel("days")
ax1.set_ylabel("ppb", size="medium")
#ax1.set_ylabel("mg m-2 h-1", size="medium")
#ax2.set_ylabel("degC", size="medium")
ax1.legend(loc='upper center')
#ax2.legend(loc='upper right')
#ax1.set_ylim(0, 5)
#ax2.set_ylim(10, 50)

plt.show()
