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
from met.library.conversions import *


'''READ IN BOKU Metdata'''
BOKUMetData = met.library.BOKUMet_Data.BOKUMet()


#DAILY MEANS
BOKUMetData_dailysum = BOKUMetData.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                      'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
#DAILY MAX
BOKUMetData_dailymax = BOKUMetData.resample('D').agg({'DT': np.max, 'AT': np.max, 'RH': np.max, 'GR': np.max, 'WS': np.max,
                                                      'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})
#JULIAN DAY
BOKUMetData_dailysum['JD'] = (BOKUMetData_dailysum.index)
f = lambda x: datestdtojd(str(x)[:-9])
BOKUMetData_dailysum['JD'] = BOKUMetData_dailysum['JD'].apply(f)

#MONTHLEY MEANS
BOKUMetData_monthly = BOKUMetData.resample('M').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                      'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

#print(BOKUMetData_dailysum["GR"])
#exit()

'''READ IN UBA air pollution data (HMW)''' #TODO: UBA data in MEZ!
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
o3_1990_2020_m = o3_1990_2020_mda1.resample('M').mean()
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


"READ in WRF-Chem2"
starttime = datetime(2007, 1, 1, 0, 00)
wrfc_time_construct = np.array([starttime + timedelta(hours=i) for i in range(87673)])
path1 = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era-interim/HCera_9km_2007-16_ATTR/model_base_results/'
"""
f_pblh = Dataset(path1 + 'HC2007t16-W-E-Cam-TNO3ATTR_zmla.nc', mode='r') 
PBLH = f_pblh.variables['zmla'][:,wrf_vie_j,wrf_vie_i]
pblh = pd.Series(PBLH[:],index=wrfc_time_construct)
pblh_d = pblh.resample('D').mean()
pblh_m = pblh.resample('M').mean()
start = datetime(2013, 1, 1, 0, 00)
end = datetime(2013, 12, 1, 0, 00)
print(pblh_m[start:end])
"""
f_o3 = Dataset(path1 + 'HC2007t16-W-E-Cam-TNO3ATTR_O3.nc', mode='r')
O3 = f_o3.variables['O3'][:,wrf_vie_j,wrf_vie_i]
o3 = pd.Series(O3[:],index=wrfc_time_construct) #wrfc_o3_d =wrfc_o3.resample('D').mean() #TODO Only valid with DatetimeIndex, TimedeltaIndex or PeriodINdex, but got instance of 'Index'
o3_d =o3.resample('D').mean()
o3_m =o3.resample('M').mean()
f_swdown = Dataset(path1 + 'HC2007t16-W-E-Cam-TNO3ATTR_swdown.nc', mode='r')
SWDOWN = f_swdown.variables['swdown'][:,wrf_vie_j,wrf_vie_i]
swdown = pd.Series(SWDOWN[:],index=wrfc_time_construct) #wrfc_o3_d =wrfc_o3.resample('D').mean() #TODO Only valid with DatetimeIndex, TimedeltaIndex or PeriodINdex, but got instance of 'Index'
swdown_d =swdown.resample('D').mean()
swdown_m =swdown.resample('M').mean()
f_tas = Dataset(path1 + 'HC2007t16-W-E-Cam-TNO3ATTR_tas.nc', mode='r')
TAS = f_tas.variables['tas'][:,wrf_vie_j,wrf_vie_i]
tas = pd.Series(TAS[:],index=wrfc_time_construct)
tas_d =tas.resample('D').mean()
tas_m =tas.resample('M').mean()
f_ddlen = Dataset(path1 + 'HC2007t16-W-E-Cam-TNO3ATTR_ddlenO3m.nc', mode='r') #DRY_DEP_LEN (bio_emissions_dimensions_stag: ozone = 6)
DDLEN = f_ddlen.variables['ddlenO3'][:,wrf_vie_j,wrf_vie_i]
ddlen = pd.Series(DDLEN[:],index=wrfc_time_construct)
ddlen_m = ddlen.resample('D').mean()
ddlen_m = ddlen.resample('M').mean()
f_hcho = Dataset(path1 + 'HC2007t16-W-E-Cam-TNO3ATTR_HCHO.nc', mode='r') #DRY_DEP_LEN (bio_emissions_dimensions_stag: ozone = 6)
HCHO = f_hcho.variables['HCHO'][:,wrf_vie_j,wrf_vie_i]
hcho = pd.Series(HCHO[:],index=wrfc_time_construct)
hcho_d = hcho.resample('D').mean()
hcho_m = hcho.resample('M').mean()

'''READ IN WRFChem data 2020'''
file2020 = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era5/wrfout_d01_2020Jan_Sep.nc'
fh2020 = Dataset(file2020, mode='r')
starttime = datetime(2020, 1, 1, 0, 00)
wrfc_time_construct = np.array([starttime + timedelta(hours=i) for i in range(6481)])
wrfc2020_o3 = fh2020.variables["o3"][:,0,0,0]  #print(type(wrfc_jd)) #<class 'numpy.ma.core.MaskedArray'>

wrfc2020_o3 = pd.Series(wrfc2020_o3[:],index=wrfc_time_construct)
wrfc2020_o3_d =wrfc2020_o3.resample('D').mean()

wrfc2020_tas = fh2020.variables["T2"][:,0,0]
wrfc2020_tas = pd.Series(wrfc2020_tas[:],index=wrfc_time_construct)
wrfc2020_tas_dmax =wrfc2020_tas.resample('D').max()

wrfc2020_sm = fh2020.variables["SMOIS"][:,0,0,0]
wrfc2020_sm = pd.Series(wrfc2020_sm[:],index=wrfc_time_construct)
wrfc2020_sm_d =wrfc2020_sm.resample('D').mean()

wrfc2020_dv = fh2020.variables["dvel_o3"][:,0,0,0]
wrfc2020_dv = pd.Series(wrfc2020_dv[:],index=wrfc_time_construct)
wrfc2020_dv_d =wrfc2020_dv.resample('D').mean()


'''
Plotting
'''
"""
fig = plt.figure()
start = datetime(2020, 1, 1, 00, 00)
end = datetime(2020, 9, 30, 00, 00)
plt.suptitle(f"OBS/MOD {start} - {end}")
#ax1 = fig.add_subplot(511)
#ax1 = plt.gca()
#ax1.plot(nox_1990_2020_da['AT9JAEG'][start:end], color='violet',  linewidth="0.1", label = "nox_obs_d_jaeg" )
#ax1.plot(nox_1990_2020_da['AT900ZA'][start:end], color='blue',  linewidth="0.1", label = "nox_obs_d_za" )
#ax1.plot(nox_1990_2020_da['AT90LOB'][start:end], color='green',  linewidth="0.1", label = "nox_obs_d_lob" )
#ax1.plot(nox_1990_2020_da['AT9STEF'][start:end], color='grey',  linewidth="0.1", label = "nox_obs_d_stef" )
#ax1.plot(wrfc2020_nox_d*1000, color='blue', label="nox_wrfc_d", linestyle="dashed")
#ax1.plot(emep_nox_d, color='green', label="nox_emep_d", linestyle="dashed")
#ax1.plot((emep_no[:,109,58]) + (emep_no2[:,109,58]), color='green', label="nox_emep_d", linestyle="dashed")
#ax1.set_xlabel("days")
#ax1.set_ylabel("ppb", size="medium")
#ax1.set_ylabel("mg m-2 h-1", size="medium")
#ax2.set_ylabel("degC", size="medium")
#ax1.legend(loc='upper left')
#ax2.legend(loc='upper right')
#ax1.set_ylim(0, 5)
#ax2.set_ylim(10, 50)

ax1 = fig.add_subplot(311)
#ax1 = fig.add_subplot(512)
ax1.plot((o3_1990_2020_da['AT9JAEG'][start:end])*ugm3toppb_o3, color='violet', linewidth="0.1", label="o3_obs_da_JAEG")
ax1.plot((o3_1990_2020_m['AT9JAEG'][start:end])*ugm3toppb_o3, color='violet',linewidth="1", label="o3_obs_m_JAEG")
ax1.plot((o3_1990_2020_da['AT900ZA'][start:end])*ugm3toppb_o3, color='blue',linewidth="0.1", label="o3_obs_da_00ZA")
#ax1.plot((o3_1990_2020_da['AT90LOB'][start:end])*ugm3toppb_o3, color='green', linewidth="0.5", label="o3_obs_da_0LOB")
ax1.plot((o3_1990_2020_da['AT9STEF'][start:end])*ugm3toppb_o3, color='darkgrey', linewidth="0.1", label="o3_obs_da_STEF")
ax1.plot((o3_1990_2020_m['AT9STEF'][start:end])*ugm3toppb_o3, color='darkgrey',linewidth="1", label="o3_obs_m_STEF")
ax1.plot(wrfc2020_o3_d[start:end]*1000,color='black', label="o3_wrfc_d", linewidth="1", linestyle="dashed")
ax1.plot(emep_o3_d[start:end],color='darkgreen', label="o3_emep_d", linewidth="1", linestyle="dashed")
ax1.set_xlabel("days")
ax1.set_ylabel("ground level ozone [ppb]", size="medium")
ax1.legend(loc='upper right')

#ax1 = fig.add_subplot(513)
#ax1.plot(hcho_d[start:end]*1000,color='darkblue', label="o3_wrfc_d", linewidth="0.5", linestyle="dashed")
#ax1.plot(o3_m[start:end]*1000,color='darkblue', label="o3_wrfc_m", linewidth="1", linestyle="dashed")
#ax1.plot((emep_no[:,109,58]) + (emep_no2[:,109,58]), color='green', label="nox_emep_d", linestyle="dashed")
#EMEP
#ax1.set_xlabel("days")
#ax1.set_ylabel("hcho [ppb]", size="medium")
#ax1.legend(loc='upper right')

#ax1 = fig.add_subplot(514)
#ax1.plot((o3_1990_2020_da['AT9STEF'][start:end])*2, color='darkgrey', label="o3_obs_da_STEF")
#ax1.plot(BOKUMetData_dailysum["GR"][start:end], color='yellow', linewidth="0.1", label="swdown_obs_BOKUR_d")
#ax1.plot(BOKUMetData_monthly["GR"][start:end], color='yellow', linewidth="1", label="swdown_obs_BOKUR_m")
#ax1.plot(swdown_d[start:end], color='darkorange', label="swdown_wrfc_d", linestyle="dashed", linewidth="0.1")
#ax1.plot(swdown_m[start:end], color='darkorange', label="swdown_wrfc_m", linestyle="dashed", linewidth="1")
#ax1.set_xlabel("days")
#ax1.set_ylabel("global radiation means [W m-2]", size="medium")
#ax1.legend(loc='upper left')

ax1 = fig.add_subplot(312)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(wrfc2020_sm_d[start:end],linewidth="0.5", color='blue', label="sm_wrfc", linestyle="dashed")
ax2.plot(wrfc2020_dv_d[start:end],linewidth="0.5", color='darkred', label="dv_wrfc", linestyle="dashed")
#ax1.set_ylim(-5, 35)
ax1.set_xlabel("days")
ax1.set_ylabel("soil moisture [m3 m-3]", size="medium")
ax2.set_ylabel("deposition velocity [cm s-1]", size="medium")
ax1.legend(loc='upper left')

ax1 = fig.add_subplot(313)
#ax1 = fig.add_subplot(515)
#ax1.plot((o3_1990_2020_da['AT9STEF'][start:end])*2, color='darkgrey', label="o3_obs_da_STEF")
ax1.plot(BOKUMetData_dailymax["AT"][start:end], linewidth="0.3", color='lightsalmon', label="t2_obs_BOKUR")
ax1.plot(BOKUMetData_monthly["AT"][start:end], linewidth="1", color='lightsalmon', label="t2_obs_BOKUR_m")
ax1.plot(wrfc2020_tas_dmax[start:end]-273.15,linewidth="0.5", color='darkred', label="t2_wrfc", linestyle="dashed")
#ax1.plot(tas_m[start:end]-273.15,linewidth="1", color='darkred', label="t2_wrfc_m", linestyle="dashed")
ax1.set_ylim(-5, 35)
ax1.set_xlabel("days")
ax1.set_ylabel("2 m T [degC]", size="medium")
ax1.legend(loc='upper left')
plt.show()


exit()
"""
fig = plt.figure()
start = datetime(2009, 7, 1, 00, 00)
end = datetime(2016, 12, 31, 00, 00)
plt.suptitle(f"OBS/MOD {start} - {end}")
ax1 = fig.add_subplot(511)
ax1 = plt.gca()
ax1.plot(nox_1990_2020_da['AT9JAEG'][start:end], color='violet',  linewidth="0.1", label = "nox_obs_d_jaeg" )
ax1.plot(nox_1990_2020_da['AT900ZA'][start:end], color='blue',  linewidth="0.1", label = "nox_obs_d_za" )
ax1.plot(nox_1990_2020_da['AT90LOB'][start:end], color='green',  linewidth="0.1", label = "nox_obs_d_lob" )
ax1.plot(nox_1990_2020_da['AT9STEF'][start:end], color='grey',  linewidth="0.1", label = "nox_obs_d_stef" )
ax1.plot(wrfc_nox_d*1000, color='blue', label="nox_wrfc_d", linestyle="dashed")
#ax1.plot(emep_nox_d, color='green', label="nox_emep_d", linestyle="dashed")
ax1.set_xlabel("days")
ax1.set_ylabel("ppb", size="medium")
#ax1.set_ylabel("mg m-2 h-1", size="medium")
#ax2.set_ylabel("degC", size="medium")
ax1.legend(loc='upper left')
#ax2.legend(loc='upper right')
#ax1.set_ylim(0, 5)
#ax2.set_ylim(10, 50)

ax1 = fig.add_subplot(512)
ax1.plot((o3_1990_2020_da['AT9JAEG'][start:end])*ugm3toppb_o3, color='violet', linewidth="0.1", label="o3_obs_da_JAEG")
ax1.plot((o3_1990_2020_m['AT9JAEG'][start:end])*ugm3toppb_o3, color='violet',linewidth="1", label="o3_obs_m_JAEG")
#ax1.plot((o3_1990_2020_da['AT900ZA'][start:end])*ugm3toppb_o3, color='blue',linewidth="1", label="o3_obs_da_00ZA")
#ax1.plot((o3_1990_2020_da['AT90LOB'][start:end])*ugm3toppb_o3, color='green', linewidth="0.5", label="o3_obs_da_0LOB")
ax1.plot((o3_1990_2020_da['AT9STEF'][start:end])*ugm3toppb_o3, color='darkgrey', linewidth="0.1", label="o3_obs_da_STEF")
ax1.plot((o3_1990_2020_m['AT9STEF'][start:end])*ugm3toppb_o3, color='darkgrey',linewidth="1", label="o3_obs_m_STEF")
ax1.plot(o3_d[start:end]*1000,color='darkblue', label="o3_wrfc_d", linewidth="0.5", linestyle="dashed")
ax1.plot(o3_m[start:end]*1000,color='darkblue', label="o3_wrfc_m", linewidth="1", linestyle="dashed")
#ax1.plot((emep_no[:,109,58]) + (emep_no2[:,109,58]), color='green', label="nox_emep_d", linestyle="dashed")
#EMEP
ax1.set_xlabel("days")
ax1.set_ylabel("ground level ozone [ppb]", size="medium")
ax1.legend(loc='upper right')

ax1 = fig.add_subplot(513)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(hcho_d[start:end]*1000,color='red', label="hcho_wrfc_d", linewidth="0.5", linestyle="dashed")
ax2.plot(ddlen[start:end],color='darkblue', label="ddep_wrfc", linewidth="1", linestyle="dashed")
ax1.set_xlabel("days")
ax1.set_ylabel("hcho [ppb]", size="medium")
ax2.set_ylabel("ddep [cm -2]", size="medium")
ax2.set_ylim(0, 0.35)
ax1.legend(loc='upper left')
ax2.legend(loc='upper left')

ax1 = fig.add_subplot(514)
#ax1.plot((o3_1990_2020_da['AT9STEF'][start:end])*2, color='darkgrey', label="o3_obs_da_STEF")
ax1.plot(BOKUMetData_dailysum["GR"][start:end], color='yellow', linewidth="0.1", label="swdown_obs_BOKUR_d")
ax1.plot(BOKUMetData_monthly["GR"][start:end], color='yellow', linewidth="1", label="swdown_obs_BOKUR_m")
ax1.plot(swdown_d[start:end], color='darkorange', label="swdown_wrfc_d", linestyle="dashed", linewidth="0.1")
ax1.plot(swdown_m[start:end], color='darkorange', label="swdown_wrfc_m", linestyle="dashed", linewidth="1")
ax1.set_xlabel("days")
ax1.set_ylabel("global radiation means [W m-2]", size="medium")
ax1.legend(loc='upper left')

ax1 = fig.add_subplot(515)
#ax1.plot((o3_1990_2020_da['AT9STEF'][start:end])*2, color='darkgrey', label="o3_obs_da_STEF")
ax1.plot(BOKUMetData_dailysum["AT"][start:end], linewidth="0.3", color='lightsalmon', label="t2_obs_BOKUR")
ax1.plot(BOKUMetData_monthly["AT"][start:end], linewidth="1", color='lightsalmon', label="t2_obs_BOKUR_m")
ax1.plot(tas_d[start:end]-273.15,linewidth="0.5", color='darkred', label="t2_wrfc", linestyle="dashed")
ax1.plot(tas_m[start:end]-273.15,linewidth="1", color='darkred', label="t2_wrfc_m", linestyle="dashed")
ax1.set_ylim(-5, 35)
ax1.set_xlabel("days")
ax1.set_ylabel("2 m T [degC]", size="medium")
ax1.legend(loc='upper left')
plt.show()





exit()

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

ax1.plot((o3_1990_2020_da['AT9JAEG'][start:end])*ugm3toppb_o3, color='violet', label="o3_obs_da_JAEG") #TODO: Umrechnen korrekt ug/m³ -> ppb! (anstelle *2)
ax1.plot((o3_1990_2020_da['AT900ZA'][start:end])*ugm3toppb_o3, color='blue', label="o3_obs_da_00ZA")
ax1.plot((o3_1990_2020_da['AT90LOB'][start:end])*ugm3toppb_o3, color='green', label="o3_obs_da_0LOB")
ax1.plot((o3_1990_2020_da['AT9STEF'][start:end])*ugm3toppb_o3, color='darkgrey', label="o3_obs_da_STEF")
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
ax1.plot(BOKUMetData_dailysum["GR"][start:end], color='orange', linewidth="0.5", label="swdown_obs_BOKUR")
ax1.plot(wrfc_swd_d[start:end], color='orange', linewidth="0.5", label="swdown_wrfc", linestyle="dashed")
ax2.plot(BOKUMetData_dailysum["AT"][start:end], color='red', linewidth="0.5",label="t2_obs_BOKUR")
ax2.plot(wrfc_T2_d[start:end]-273.15, color='red',linewidth="0.5", label="t2_wrfc", linestyle="dashed")
ax2.set_ylim(-10, 35)
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
ax1.plot((o3_1990_2020_da["AT9JAEG"][start:end])*0.5094042909, color='violet', label="O3_obs_d_jaeg")
ax1.plot((o3_1990_2020_da["AT900ZA"][start:end])*0.5094042909, color='blue', label="O3_obs_d_za")
ax1.plot((o3_1990_2020_da["AT90LOB"][start:end])*0.5094042909, color='green', label="O3_obs_d_lob") #TODO: Umrechnen korrekt ug/m³ -> ppb! (anstelle *2)
ax1.plot((o3_1990_2020_da["AT9STEF"][start:end])*0.5094042909, color='grey', label="O3_obs_d_stef")
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

ax1.plot(wrfc_hcho, color='blue', label="wrfc_hcho", linestyle="dotted")
#ax1.plot(wrfc_ho, color='blue', label="wrfc_oh, hydroxide", linestyle="dotted")
#ax2.plot(wrfc_ho2, color='green', label="wrfc_ho2, hydroperoxyl", linestyle="dashed")
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
