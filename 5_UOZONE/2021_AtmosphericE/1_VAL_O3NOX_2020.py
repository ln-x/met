# -*- coding: utf-8 -*-
__author__ = 'lnx'
from netCDF4 import Dataset
import netCDF4
import numpy as np
import csv
import pandas as pd
from datetime import datetime, timedelta
import monthdelta
import matplotlib.dates
import matplotlib.pyplot as plt
from scipy import stats
import sys
import os
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVINDOBONA
from met.library import ReadinVindobona_DA
from met.library import ReadinVindobona_Filter
from functools import reduce

"read in VINDOBONA"

foldername = "/windata/Google Drive/DATA/remote/ground/maxdoas/MAXDOAS2020/DQ/"
foldername_A = "/windata/Google Drive/DATA/remote/ground/maxdoas/MAXDOAS2020/AQ/"
foldername_K = "/windata/Google Drive/DATA/remote/ground/maxdoas/MAXDOAS2020/KQ/"


hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter.loadfileALL(foldername)
hcho_d_A, hcho_dmax_A, hcho_m_A = ReadinVindobona_Filter.loadfileALL(foldername_A)
hcho_d_K, hcho_dmax_K, hcho_m_K = ReadinVindobona_Filter.loadfileALL(foldername_K)

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

#MONTHLY MEANS
BOKUMetData_monthly = BOKUMetData.resample('M').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                      'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

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
nox_1990_2020_da = pd.concat([nox_1990_2019_da, nox_2020_da], axis=0)

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
jd = netCDF4.num2date(emep_time[:],emep_time.units)

emep_c5h8_d = fh.variables['SURF_ppb_C5H8'][:,wrf_vie_j, wrf_vie_i]
emep_c5h8_d = pd.Series(emep_c5h8_d[:],index=jd)
emep_hcho_d = fh.variables['SURF_ppb_HCHO'][:,wrf_vie_j, wrf_vie_i]
emep_hcho_d = pd.Series(emep_hcho_d[:],index=jd)
emep_o3_d = fh.variables['SURF_ppb_O3'][:,wrf_vie_j,wrf_vie_i] #(time, j, i)
emep_o3_d = pd.Series(emep_o3_d[:],index=jd)
emep_o3_h = fh1.variables['SURF_ppb_O3']

emep_no_d = fh.variables['SURF_ppb_NO'][:,wrf_vie_j,wrf_vie_i]
emep_no_d = pd.Series(emep_no_d[:], index=jd)
emep_no2_d = fh.variables['SURF_ppb_NO2'][:,wrf_vie_j,wrf_vie_i]
emep_no2_d = pd.Series(emep_no2_d[:], index=jd)
emep_nox_d = emep_no_d.add(emep_no2_d)

'''READ IN WRFChem data'''
file2 = path + 'Norskehavet/EMEPData/OUTPUT/2020_4/wrfout_d01_2020-03-31_01:00:00'
fh2 = Dataset(file2, mode='r')
LON = fh2.variables['XLONG'][1]
LAT = fh2.variables['XLAT'][1]

'''READ IN WRFChem data 2020'''
file2020 = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era5/wrfout_d01_2020Jan_Sep.nc'
file2020B = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era5/wrfout_d01_2020Jan_Sep_LAI_DDEP.nc'
file2020tas = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era5/zprac_wrfout/BOKU2020_BASE_WRFchem9_202001-09_tas.nc'
file2020o3 = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era5/zprac_wrfout/BOKU2020_BASE_WRFchem9_202001-09_=3.nc'
#file2020hcho = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era5/wrfout_d01_2020-03-31_01_hcho.nc'
#starttime = datetime(2020, 3, 31, 1, 00)
#wrfc_time_construct_april = np.array([starttime + timedelta(hours=i) for i in range(720)])
file2020hcho = '/windata/Google Drive/DATA/models/boku/wrf_chem/reanalysis/era5/wrfout_d01_2020Jan_Sep_HCHO.nc'

fh2020 = Dataset(file2020, mode='r')
fh2020B = Dataset(file2020B, mode='r')
fh2020hcho = Dataset(file2020hcho, mode='r')
starttime = datetime(2020, 1, 1, 0, 00)
wrfc_time_construct = np.array([starttime + timedelta(hours=i) for i in range(6481)])
wrfc2020_hchov = fh2020hcho.variables["hcho"][:,:,:,:]  #print(type(wrfc_jd)) #<class 'numpy.ma.core.MaskedArray'>
wrfc2020_hchov0 = pd.DataFrame(wrfc2020_hchov[:,0,1,1],index=wrfc_time_construct)
wrfc2020_hcho0_d =wrfc2020_hchov0.resample('D').mean()
wrfc2020_hcho0_dmax =wrfc2020_hchov0.resample('D').max()
wrfc2020_hchov1 = pd.DataFrame(wrfc2020_hchov[:,1,2,2],index=wrfc_time_construct)
wrfc2020_hcho1_d =wrfc2020_hchov1.resample('D').mean()
wrfc2020_hcho1_dmax =wrfc2020_hchov1.resample('D').max()
wrfc2020_hcho1_mmax =wrfc2020_hchov1.resample('M').mean()
wrfc2020_hchov2 = pd.DataFrame(wrfc2020_hchov[:,2,1,1],index=wrfc_time_construct)
wrfc2020_hcho2_d =wrfc2020_hchov2.resample('D').mean()
wrfc2020_hcho2_dmax =wrfc2020_hchov2.resample('D').max()
wrfc2020_hchov3 = pd.DataFrame(wrfc2020_hchov[:,3,1,1],index=wrfc_time_construct)
wrfc2020_hcho3_d =wrfc2020_hchov3.resample('D').mean()
wrfc2020_hcho3_dmax =wrfc2020_hchov3.resample('D').max()
wrfc2020_hchov4 = pd.DataFrame(wrfc2020_hchov[:,4,1,1],index=wrfc_time_construct)
wrfc2020_hcho4_d =wrfc2020_hchov4.resample('D').mean()
wrfc2020_hcho4_dmax =wrfc2020_hchov4.resample('D').max()

wrfc2020_o3 = fh2020.variables["o3"][:,0,0,0]  #print(type(wrfc_jd)) #<class 'numpy.ma.core.MaskedArray'>
wrfc2020_o3 = pd.Series(wrfc2020_o3[:],index=wrfc_time_construct)
wrfc2020_o3_d =wrfc2020_o3.resample('D').mean()

wrfc2020_no = fh2020.variables["no"][:,0,0,0]  #print(type(wrfc_jd)) #<class 'numpy.ma.core.MaskedArray'>
wrfc2020_no = pd.Series(wrfc2020_no[:],index=wrfc_time_construct)
wrfc2020_no_d =wrfc2020_no.resample('D').mean()

wrfc2020_no2 = fh2020.variables["no2"][:,0,0,0]  #print(type(wrfc_jd)) #<class 'numpy.ma.core.MaskedArray'>
wrfc2020_no2 = pd.Series(wrfc2020_no2[:],index=wrfc_time_construct)
wrfc2020_no2_d =wrfc2020_no2.resample('D').mean()

wrfc2020_nox_d = wrfc2020_no2_d.add(wrfc2020_no_d)

wrfc2020_tas = fh2020.variables["T2"][:,0,0]
wrfc2020_tas = pd.Series(wrfc2020_tas[:],index=wrfc_time_construct)
wrfc2020_tas_dmax =wrfc2020_tas.resample('D').max()

wrfc2020_sw = fh2020.variables["SWDOWN"][:,0,0]
wrfc2020_sw = pd.Series(wrfc2020_sw[:],index=wrfc_time_construct)
wrfc2020_sw_d =wrfc2020_sw.resample('D').mean()
wrfc2020_sw_m =wrfc2020_sw_d.resample('M').mean()

wrfc2020_sm = fh2020.variables["SMOIS"][:,0,0,0]
wrfc2020_sm = pd.Series(wrfc2020_sm[:],index=wrfc_time_construct)
wrfc2020_sm_d =wrfc2020_sm.resample('D').mean()

wrfc2020_dv = fh2020B.variables["DRY_DEP_LEN"][:,0,0,0]
wrfc2020_dv = pd.Series(wrfc2020_dv[:],index=wrfc_time_construct)
wrfc2020_dv_d =wrfc2020_dv.resample('D').mean()

#wrfc2020_lai = fh2020B.variables["LAI"][:,0,0]
#wrfc2020_lai = pd.Series(wrfc2020_lai[:],index=wrfc_time_construct)
#wrfc2020_lai =wrfc2020_dv.resample('D').mean()

wrfc2020_hcho = fh2020.variables["hcho"][:,0,0,0]
wrfc2020_hcho = pd.Series(wrfc2020_hcho[:],index=wrfc_time_construct)
wrfc2020_hcho_d =wrfc2020_hcho.resample('D').mean()
wrfc2020_hcho_dmax =wrfc2020_hcho.resample('D').max()
wrfc2020_hcho_mmax =wrfc2020_hcho_dmax.resample('M').mean()


wrfc2020_c5h8 = fh2020.variables["iso"][:,0,0,0]
wrfc2020_c5h8 = pd.Series(wrfc2020_c5h8[:],index=wrfc_time_construct)
wrfc2020_c5h8_d =wrfc2020_c5h8.resample('D').mean()
wrfc2020_c5h8_dmax =wrfc2020_c5h8.resample('D').max()

starttime = datetime(2020, 1, 1, 0, 00)
wrfc_time_construct_months = np.array([starttime + monthdelta.monthdelta(i) for i in range(12)])
wrflai_megan = [471,540,562,1278,2367,2456,2047,1718,1685,1335,807,1003]
wrflai_megan = pd.Series(wrflai_megan[:],index=wrfc_time_construct_months)
#print(wrflai_megan)
#exit()

#print(hcho.index[starttime])



'''
Plotting
'''

#fig = plt.figure()
start = datetime(2020, 1, 1, 00, 00)
end = datetime(2020, 9, 27, 00, 00)


end2 = datetime(2020, 10, 30, 00, 00)
plt.suptitle(f"OBS/MOD {start} - {end}")
#ZOOM IN VERTICAL LAYERS
#ax1 = fig.add_subplot(111)
#ax1 = plt.gca()
#ax2 = ax1.twinx()
#ax1.plot(wrfc2020_hcho_d[start:end]*1000,linewidth="0.5", color='green', label="hcho wrfc d", linestyle=":")
#ax1.plot(wrfc2020_hcho_dmax[start:end]*1000,linewidth="1", color='green', label="hcho wrfc dmax", linestyle="solid")
#ax1.plot(wrfc2020_hcho_mmax[start:end]*1000,linewidth="0.5", color='green', label="hcho wrfc mmax", linestyle="-")
#ax2.plot(wrfc2020_c5h8_dmax[start:end]*1000,linewidth="0.5", color='red', label="c5h8 wrfc dmax", linestyle="dashed")#
#ax1.plot(wrfc2020_hcho0_d[start:end]*1000, linewidth="0.5", color='darkblue', label="hcho wrfc d lev0", linestyle=":") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho1_d[start:end]*1000, linewidth="0.5", color='slateblue', label="hcho wrfc d lev1", linestyle=":") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho2_d[start:end]*1000, linewidth="0.5", color='rebeccapurple', label="hcho wrfc d lev2", linestyle=":") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho3_d[start:end]*1000, linewidth="0.5", color='darkviolet', label="hcho wrfc d lev3", linestyle=":") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho4_d[start:end]*1000, linewidth="0.5", color='fuchsia', label="hcho wrfc d lev4", linestyle=":") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho0_dmax[start:end]*1000, linewidth="0.5", color='darkblue', label="hcho wrfc dmax lev0", linestyle="solid") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho1_dmax[start:end]*1000, linewidth="0.5", color='slateblue', label="hcho wrfc dmax lev1", linestyle="solid") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho2_dmax[start:end]*1000, linewidth="0.5", color='rebeccapurple', label="hcho wrfc dmax lev2", linestyle="solid") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho3_dmax[start:end]*1000, linewidth="0.5", color='darkviolet', label="hcho wrfc dmax lev3", linestyle="solid") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho4_dmax[start:end]*1000, linewidth="0.5", color='fuchsia', label="hcho wrfc dmax lev4", linestyle="solid") #274 = Julian Day 30.Sept2020
#ax1.plot(hcho_d[start:end], linewidth="0.5", color='black', label="hcho OBS d", linestyle=":") #274 = Julian Day 30.Sept2020
#ax1.plot(hcho_dmax[start:end], linewidth="1", color='black', label="hcho OBS dmax", linestyle="solid") #274 = Julian Day 30.Sept2020
#ax1.plot(hcho_m[start:end], linewidth="0.5", color='black', label="hcho OBS mmax", linestyle="-") #274 = Julian Day 30.Sept2020
#ax1.plot(emep_hcho_d[start:end],linewidth="1", color='darkgreen', label="hcho_emep", linestyle=":")
#ax2.plot(emep_c5h8_d[start:end],linewidth="1", color='darkred', label="c5h8_emep", linestyle=":")
#ax1.set_ylim(0, 8)
#ax1.set_xlabel("days")
#ax1.set_ylabel("hcho [ppb]", size="medium")
#ax2.set_ylabel("c5h8 [ppb]", size="medium")
#ax1.legend(loc='upper left')
#ax2.legend(loc='upper right')
#plt.show()

fig = plt.figure()
plt.suptitle(f"OBS/MOD {start} - {end}")
#NOX
ax1 = fig.add_subplot(611)
ax1 = plt.gca()
#ax1.plot(nox_1990_2020_da['AT9JAEG'][start:end], color='violet',  linewidth="0.1", label = "nox_obs_d_jaeg" )
#ax1.plot(nox_1990_2020_da['AT900ZA'][start:end], color='blue',  linewidth="0.1", label = "nox_obs_d_za" )
#ax1.plot(nox_1990_2020_da['AT90LOB'][start:end], color='green',  linewidth="0.1", label = "nox_obs_d_lob" )
#ax1.plot(nox_1990_2020_da['AT9STEF'][start:end], color='grey',  linewidth="0.1", label = "nox_obs_d_stef" )
#ax1.plot(wrfc2020_nox_d*1000, color='blue', label="nox_wrfc_d", linestyle="dashed")
ax1.plot(wrfc2020_nox_d*1000 - nox_1990_2020_da['AT9STEF'][start:end], color='grey',  linewidth="0.1", label = "nox d wrfc - obs_stef" )
#ax1.plot(emep_nox_d, color='green', label="nox_emep_d", linestyle="dashed")
ax1.plot(emep_nox_d - nox_1990_2020_da['AT9STEF'][start:end], color='green', label="nox d emep - obs_stef", linestyle="dashed")
#ax1.plot((emep_no[:,109,58]) + (emep_no2[:,109,58]), color='green', label="nox_emep_d", linestyle="dashed")
ax1.set_xlabel("days")
ax1.set_ylabel("ppb", size="medium")
ax1.set_ylabel("mg m-2 h-1", size="medium")
ax1.legend(loc='upper left')
#ax1.set_ylim(0, 5)

ax1 = fig.add_subplot(612)
#ax1 = fig.add_subplot(512)
#ax1.plot((o3_1990_2020_da['AT9JAEG'][start:end])*ugm3toppb_o3, color='black', linewidth="0.1", label="o3_obs_da_JAEG")
#ax1.plot((o3_1990_2020_m['AT9JAEG'][start:end])*ugm3toppb_o3, color='black',linewidth="1", label="o3_obs_m_JAEG")
#ax1.plot((o3_1990_2020_da['AT900ZA'][start:end])*ugm3toppb_o3, color='grey',linewidth="0.1", label="o3_obs_da_00ZA")
#ax1.plot((o3_1990_2020_da['AT90LOB'][start:end])*ugm3toppb_o3, color='green', linewidth="0.5", label="o3_obs_da_0LOB")
#ax1.plot((o3_1990_2020_da['AT9STEF'][start:end])*ugm3toppb_o3, color='darkgrey', linewidth="0.1", label="o3_obs_da_STEF")
#ax1.plot((o3_1990_2020_m['AT9STEF'][start:end])*ugm3toppb_o3, color='darkgrey',linewidth="1", label="o3_obs_m_STEF")
#ax1.plot(wrfc2020_o3_d[start:end]*1000,color='violet', label="o3_wrfc_d", linewidth="1", linestyle="dashed")
ax1.plot(wrfc2020_o3_d[start:end]*1000-((o3_1990_2020_m['AT9STEF'][start:end])*ugm3toppb_o3),color='violet', label="o3 d wrfc - obs_stef", linewidth="1", linestyle="dashed")
ax1.plot(emep_o3_d[start:end],color='darkgreen', label="o3_emep_d", linewidth="1", linestyle="dashed")
ax1.plot(wrfc2020_o3_d[start:end]*1000 - emep_o3_d[start:end],color='darkgreen', label="o3 d emep - obs_stef", linewidth="1", linestyle="dashed")
ax1.set_xlabel("days")
ax1.set_ylabel("ground level ozone [ppb]", size="medium")
ax1.legend(loc='upper right')

ax1 = fig.add_subplot(613)
ax1.plot(wrfc2020_sw_d[start:end]-BOKUMetData_dailysum["GR"][start:end], color='orange', linewidth="0.1", label="swdown wrfc- obs_BOKUR_d")
ax1.plot(wrfc2020_sw_m[start:end]-BOKUMetData_monthly["GR"][start:end], color='orange', linewidth="1", label="swdown wrfc- obs_BOKUR_m")
#ax1.plot(wrfc2020_sw_d[start:end], color='darkorange', label="swdown_wrfc_d", linewidth="0.1")
#ax1.plot(wrfc2020_sw_m[start:end], color='darkorange', label="swdown_wrfc_m", linewidth="1")
ax1.set_xlabel("days")
ax1.set_ylabel("global radiation means differences [W m-2]", size="medium")
ax1.legend(loc='upper left')


ax1 = fig.add_subplot(614)
ax1 = plt.gca()
ax2 = ax1.twinx()
#ax1.plot(wrfc2020_hcho_d[start:end]*1000,linewidth="0.5", color='violet', label="hcho wrfc d", linestyle=":")
#ax1.plot(wrfc2020_hcho_dmax[start:end]*1000,linewidth="1", color='violet', label="hcho wrfc dmax", linestyle="solid")
#ax1.plot(wrfc2020_hcho_mmax[start:end]*1000,linewidth="0.5", color='violet', label="hcho wrfc mmax", linestyle="-")

#ax1.plot(wrfc2020_hcho0_d[start:end]*1000, linewidth="0.5", color='darkblue', label="hcho wrfc d lev0", linestyle=":") #274 = Julian Day 30.Sept2020
ax1.plot(wrfc2020_hcho1_d[start:end]*1000, linewidth="0.5", color='violet', label="hcho wrfc d lev1", linestyle=":") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho2_d[start:end]*1000, linewidth="0.5", color='rebeccapurple', label="hcho wrfc d lev2", linestyle=":") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho3_d[start:end]*1000, linewidth="0.5", color='darkviolet', label="hcho wrfc d lev3", linestyle=":") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho4_d[start:end]*1000, linewidth="0.5", color='fuchsia', label="hcho wrfc d lev4", linestyle=":") #274 = Julian Day 30.Sept2020

#ax1.plot(wrfc2020_hcho0_dmax[start:end]*1000, linewidth="0.5", color='darkblue', label="hcho wrfc dmax lev0", linestyle="solid") #274 = Julian Day 30.Sept2020
ax1.plot(wrfc2020_hcho1_dmax[start:end]*1000, linewidth="0.5", color='violet', label="hcho wrfc dmax lev1", linestyle="solid") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho2_dmax[start:end]*1000, linewidth="0.5", color='rebeccapurple', label="hcho wrfc dmax lev2", linestyle="solid") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho3_dmax[start:end]*1000, linewidth="0.5", color='darkviolet', label="hcho wrfc dmax lev3", linestyle="solid") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho4_dmax[start:end]*1000, linewidth="0.5", color='fuchsia', label="hcho wrfc dmax lev4", linestyle="solid") #274 = Julian Day 30.Sept2020

ax1.plot(wrfc2020_hcho1_mmax[start:end]*1000, linewidth="0.5", color='violet', label="hcho wrfc dmax lev1", linestyle="solid") #274 = Julian Day 30.Sept2020

ax1.plot(emep_hcho_d[start:end],linewidth="0.5", color='green', label="hcho EMEP d", linestyle=":")

ax1.plot(hcho_d[start:end], linewidth="0.5", color='black', label="hcho OBS d", linestyle=":") #274 = Julian Day 30.Sept2020
ax1.plot(hcho_dmax[start:end], linewidth="1", color='black', label="hcho OBS dmax", linestyle="solid") #274 = Julian Day 30.Sept2020
ax1.plot(hcho_m[start:end], linewidth="0.5", color='black', label="hcho D OBS mmax", linestyle="-") #274 = Julian Day 30.Sept2020
ax1.plot(hcho_m_A[start:end], linewidth="0.5", color='grey', label="hcho A OBS mmax", linestyle="-") #274 = Julian Day 30.Sept2020
ax1.plot(hcho_m_K[start:end], linewidth="0.5", color='darkgrey', label="hcho K OBS mmax", linestyle="-") #274 = Julian Day 30.Sept2020

#ax1.plot(emep_hcho_d[start:end],linewidth="1", color='darkgreen', label="hcho_emep", linestyle=":")
#ax2.plot(emep_c5h8_d[start:end],linewidth="1", color='darkred', label="c5h8_emep", linestyle=":")
#ax1.set_ylim(0, 8)
ax1.set_xlabel("days")
ax1.set_ylabel("hcho [ppb]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

ax1 = fig.add_subplot(615)
ax1 = plt.gca()
ax2 = ax1.twinx()
#ax1.plot(wrfc2020_lai[start:end],linewidth="0.5", color='blue', label="lai_wrfc", linestyle="dashed")
ax1.plot(wrflai_megan[start:end2], linewidth="0.5", color='blue', label="lai_wrf_megan", linestyle="dashed")
#ax2.plot(wrfc2020_dv_d[start:end],linewidth="0.5", color='darkred', label="dv_wrfc", linestyle="dashed") #TODO layer 6 not 1!!
ax2.plot(wrfc2020_c5h8_dmax[start:end]*1000,linewidth="0.5", color='red', label="c5h8 wrfc dmax", linestyle="dashed")
#ax1.set_ylim(-5, 35)
ax1.set_xlabel("days")
ax1.set_ylabel("LAI [degree]", size="medium")
ax2.set_ylabel("c5h8 [ppb]", size="medium")
#ax1.set_ylabel("LAI [m2 m-2]", size="medium") #TODO convert degree to m2 m-2
#ax2.set_ylabel("dry deposition velocity [cm s-1]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')


ax1 = fig.add_subplot(616)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.plot(wrfc2020_sm_d[start:end],linewidth="0.5", color='blue', label="sm_wrfc", linestyle="dashed")
ax1.plot(BOKUMetData_dailymax["AT"][start:end], linewidth="0.3", color='lightsalmon', label="t2_obs_BOKUR")
ax1.plot(BOKUMetData_monthly["AT"][start:end], linewidth="1", color='lightsalmon', label="t2_obs_BOKUR_m")
ax1.plot(wrfc2020_tas_dmax[start:end]-273.15,linewidth="0.5", color='darkred', label="t2_wrfc", linestyle="dashed")
#ax1.plot(tas_m[start:end]-273.15,linewidth="1", color='darkred', label="t2_wrfc_m", linestyle="dashed")
ax1.set_ylim(-5, 35)
ax1.set_xlabel("days")
ax1.set_ylabel("2 m T [degC]", size="medium")
ax2.set_ylabel("soil moisture [m3 m-3]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()


pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,wrfc2020_hcho1_dmax],axis=1, keys=['1','2','3','4'])
pff = pff.dropna()
print(pff)

#print(wrfc2020_hcho1_dmax.values.shape)
x_i = pff['4'].values.flatten()
#print(x_i.shape)
x= x_i*1000
y = pff['1'].values.flatten()
yA = pff['2'].values.flatten()
yK = pff['3'].values.flatten()

fig=plt.figure()
m, b = np.polyfit(x, y , 1)
mA, bA = np.polyfit(x, yA, 1)
mK, bK = np.polyfit(x, yK, 1)
print(m,mA,mK,b,bA,bK)

#R2_Forc_NO2concentr = (stats.spearmanr(o3, no2))[0] ** 2

fig2 = plt.figure()
plt.scatter(x, y, color='red',label='Axis D') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
plt.scatter(x, yA, color='violet',label='Axis A') #label=r"$r$=%.2f" % (R_hcho))
plt.scatter(x, yK, color='green',label='Axis K')
plt.plot(x, b*x+m, color='red')
plt.plot(x, bA*x+mA, color='violet')
plt.plot(x, mK*x+bK, color='green')
#m, b = np.polyfit(x, y, 1)
#plt.plot(x, m * x + b)
plt.legend(loc='upper right')
plt.ylabel("WRF [ppb]", size="medium")
plt.xlabel("MAXDOAS [ppb]", size="medium")
plt.suptitle("HCHO dmax 2020 Jan-Sep")
plt.show()