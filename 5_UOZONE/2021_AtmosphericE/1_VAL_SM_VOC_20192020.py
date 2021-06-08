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
from met.library import ReadinVindobona_Filter2019

from functools import reduce

"read in VINDOBONA"

foldername = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2020/DQ/"
foldername2019 = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2019/"
foldername_A = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2020/AQ/"
foldername_K = "/windata/DATA/remote/ground/maxdoas/MAXDOAS2020/KQ/"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter.loadfileALL(foldername)
hcho19_d, hcho19_dmax, hcho19_m = ReadinVindobona_Filter2019.loadfileALL(foldername2019)
hcho_d_A, hcho_dmax_A, hcho_m_A = ReadinVindobona_Filter.loadfileALL(foldername_A)
hcho_d_K, hcho_dmax_K, hcho_m_K = ReadinVindobona_Filter.loadfileALL(foldername_K)


'''READ IN BOKU Metdata'''
BOKUMetData = met.library.BOKUMet_Data.BOKUMet()
#print(BOKUMetData) #10min values
#DAILY MEANS
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
#DAILY MAX
BOKUMetData_dailymax = BOKUMetData_hourlymean.resample('D').agg({'DT': np.max, 'AT': np.max, 'RH': np.max, 'GR': np.max, 'WS': np.max,
                                                      'WD': np.max, 'WSG': np.max, 'PC': np.sum, 'AP': np.max})
#JULIAN DAY
BOKUMetData_dailysum['JD'] = (BOKUMetData_dailysum.index)
f = lambda x: datestdtojd(str(x)[:-9])
BOKUMetData_dailysum['JD'] = BOKUMetData_dailysum['JD'].apply(f)

#MONTHLY MEANS
BOKUMetData_monthly = BOKUMetData.resample('M').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                      'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

'''READ in SOIL MOISTURE DATA'''
#file_sm_2019_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/2019_Parrots_Rutzendorf_4_Heidi.xls"
#sm = pd.read_excel(file_sm_2019_rutz, sheet_name="Data", usecols="A,B", skiprows=11)#, converters={'A': pd.to_datetime})
#sm.columns = ['datetime', 'Parrot mean [VWC%]']  #TODO: local time!
#sm = sm.set_index(pd.to_datetime(sm['datetime']))
#sm = sm.drop(columns=['datetime'])

file_sm_2019_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/RUT_10_min.xls"
sm = pd.read_excel(file_sm_2019_rutz, sheet_name="RUT_d", usecols="D,K,L,M,N,O,P", skiprows=11)#, converters={'A': pd.to_datetime})
sm.columns = ['datetime', 'VWC1 min[%]', 'VWC2 min[%]','VWC3 min[%]','VWC1 max[%]', 'VWC2 max[%]','VWC3 max[%]']  #TODO: local time!
sm = sm.set_index(pd.to_datetime(sm['datetime']))
sm = sm.drop(columns=['datetime'])

file_rss_rutz = "/windata/DATA/obs_point/land/Bodenfeuchte_Rutzendorf/2008_2020_Rutzendorf_ARIS_results_sepp.xlsx"
rss = pd.read_excel(file_rss_rutz, sheet_name="RSS_top", usecols="A,B,C,D,E,F", skiprows=11)#, converters={'A': pd.to_datetime})
rss.columns = ['datetime', 'RSS_top_maize', 'RSS_top_sBarley','RSS_top_sugBeet','RSS_top_wWheat', 'RSS_top_grass']  #TODO: local time!
rss = rss.set_index(pd.to_datetime(rss['datetime']))
rss = rss.drop(columns=['datetime'])


'''READ IN EMEP data'''
#Jans indexes for Vienna gridpoint:
wrf_vie_i=109 #TODO Double check! i=x=long
wrf_vie_j=58  #TODO Double check! j=y=lat

path = '/media/heidit/'  # '/media/lnx'
file = path + 'Norskehavet/EMEPData/OUTPUT/file_MarApr.nc'
#file = path + 'Norskehavet/EMEPData/OUTPUT/2020_4/JanBASESIM_4b_day.nc'
#file1 = path + 'Norskehavet/EMEPData/OUTPUT/2020_4/JanBASESIM_4b_hourInst.nc'
file = '/windata/DATA/models/boku/EMEP/Base20_day.nc'
file1 = '/windata/DATA/models/boku/EMEP/Base20_hourInst.nc'
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
#file2 = path + 'Norskehavet/EMEPData/OUTPUT/2020_4/wrfout_d01_2020-03-31_01:00:00'
#fh2 = Dataset(file2, mode='r')
#LON = fh2.variables['XLONG'][1]
#LAT = fh2.variables['XLAT'][1]

'''READ IN WRFChem data 2020'''
file2020 = '/windata/DATA/models/boku/wrf_chem/reanalysis/era5/wrfout_d01_2020Jan_Sep.nc'
file2020B = '/windata/DATA/models/boku/wrf_chem/reanalysis/era5/wrfout_d01_2020Jan_Sep_LAI_DDEP.nc'
file2020tas = '/windata/DATA/models/boku/wrf_chem/reanalysis/era5/zprac_wrfout/BOKU2020_BASE_WRFchem9_202001-09_tas.nc'
file2020o3 = '/windata/DATA/models/boku/wrf_chem/reanalysis/era5/zprac_wrfout/BOKU2020_BASE_WRFchem9_202001-09_o3.nc'
#file2020hcho = '/windata/DATA/models/boku/wrf_chem/reanalysis/era5/wrfout_d01_2020-03-31_01_hcho.nc'
#starttime = datetime(2020, 3, 31, 1, 00)
#wrfc_time_construct_april = np.array([starttime + timedelta(hours=i) for i in range(720)])
file2020hcho = '/windata/DATA/models/boku/wrf_chem/reanalysis/era5/wrfout_d01_2020Jan_Sep_HCHO.nc'

fh2020 = Dataset(file2020, mode='r')
fh2020B = Dataset(file2020B, mode='r')
fh2020hcho = Dataset(file2020hcho, mode='r')
starttime = datetime(2020, 1, 1, 0, 00)
wrfc_time_construct = np.array([starttime + timedelta(hours=i) for i in range(6481)])
wrfc2020_hchov = fh2020hcho.variables["hcho"][:,:,:,:]  #print(type(wrfc_jd)) #<class 'numpy.ma.core.MaskedArray'>
wrfc2020_hchov0 = pd.DataFrame(wrfc2020_hchov[:,0,1,1],index=wrfc_time_construct)
wrfc2020_hcho0_d =wrfc2020_hchov0.resample('D').mean()
wrfc2020_hcho0_dmax =wrfc2020_hchov0.resample('D').max()
wrfc2020_hchov1 = pd.DataFrame(wrfc2020_hchov[:,1,1,1],index=wrfc_time_construct)
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

starttime = datetime(2019, 1, 1, 0, 00)
wrfc_time_construct_months = np.array([starttime + monthdelta.monthdelta(i) for i in range(24)])
wrflai_megan = [471,540,562,1278,2367,2456,2047,1718,1685,1335,807,1003,471,540,562,1278,2367,2456,2047,1718,1685,1335,807,1003]
wrflai_megan = pd.Series(wrflai_megan[:],index=wrfc_time_construct_months)
#print(hcho.index[starttime])

'''READ IN WRFChem data 2019 - Christian''' #RUTZ: [1,69,101] VIE CENTER: [1,69,99]
file2019 = '/windata/DATA/models/boku/wrf/120521/9km_3km_2domain/wrfout_d01_2019-07-01_00:00:00'
fh2019 = Dataset(file2019, mode='r')
starttime = datetime(2019, 7, 1, 0, 00)
wrf_time_construct = np.array([starttime + timedelta(hours=i) for i in range(248)])
wrf2019_sm = fh2019.variables["SMOIS"][:,1,69,101]
#print(len(wrfc2019_sm))
wrf2019_sm = pd.Series(wrf2019_sm[:],index=wrf_time_construct)
wrf2019_sm_d =wrf2019_sm.resample('D').mean()

wrf2019_rain = fh2019.variables["RAINC"][:,69,101]
#print(len(wrfc2019_sm))
wrf2019_rain = pd.Series(wrf2019_rain[:],index=wrf_time_construct)
wrf2019_rain_d =wrf2019_rain.resample('D').sum()

wrf2019_tas = fh2019.variables["T2"][:,69,99]
#wrf2019_tas = fh2019.variables["T2"][:,69,101]
wrf2019_tas = pd.Series(wrf2019_tas[:],index=wrf_time_construct)
wrf2019_tas_dmax =wrf2019_tas.resample('D').max()

'''READ IN CAMX'''
camx3_y_vie_is = 76  #for Wien Innere Stadt 1,76,181
camx3_x_vie_is = 181 #for Wien Innere Stadt

for i in ["HCHO","O3", "NO", "NO2"]:
    file = '/windata/DATA/models/boku/CAMX/BOKU2020_BASE_WRFchem3_202001-09_'+ i + '.nc'
    f = Dataset(file, mode='r')
    par = f.variables[i][:, :, :]
    par1 = pd.DataFrame(par[:, 76, 181], index=wrfc_time_construct)
    globals()[f"camx3_2020_{i}_d"] = par1.resample('D').mean()
    globals()[f"camx3_2020_{i}_dmax"] = par1.resample('D').max()

#cams3_2020_NOx_dmax = cams3_2020_NO2_dmax.add(cams3_2020_NO_dmax)

#TSIF_743
tsif_r = pd.read_csv("/windata/DATA/remote/satellite/TROPOMI/TSIF_743.csv", sep=",")
tsif = tsif_r.set_index(pd.to_datetime(tsif_r['time']))
tsif = tsif.drop(columns=['time'])
#print(tsif)

'''READ IN Vinzenz's classification'''
#metclass_r = pd.read_csv("/windata/DATA/metclass_vienna.csv", sep=";")
#print(metclass)
#metclass_x = metclass_r.set_index(pd.to_datetime(metclass_r['time']))
#metclass = metclass_x.drop(columns=['time'])
#print(metclass_x)

'''TIMESLICES'''
March = datetime(2020, 3, 1, 00, 00) #JD 2020=92
April = datetime(2020, 4, 1, 00, 00) #JD 2020=92
June = datetime(2020, 6, 1, 00, 00)  #JD 2020=183
July = datetime(2020, 7, 1, 00, 00)  #JD 2020=183
Sept = datetime(2020, 9, 1, 00, 00)  #JD 2020=183
DP1_s = datetime(2019, 3, 17, 00, 00) #drought period1 start
DP1_e = datetime(2019, 4, 29, 00, 00) #drought period1 end
DP2_s = datetime(2019, 6, 8, 00, 00) #drought period2 start
DP2_e = datetime(2019, 6, 30, 00, 00) #drought period2 end
DP3_s = datetime(2019, 8, 13, 00, 00) #drought period3 start
DP3_e = datetime(2019, 8, 31, 00, 00) #drought period3 end
DP4_s = datetime(2020, 3, 22, 00, 00) #drought period4 start
DP4_e = datetime(2020, 4, 11, 00, 00) #drought period4 end


'''
Plotting
'''

#fig = plt.figure()
#start = datetime(2020, 1, 1, 00, 00)
start = datetime(2019, 1, 1, 00, 00)
end = datetime(2020, 9, 27, 00, 00)
end2 = datetime(2020, 10, 30, 00, 00)
plt.suptitle(f"OBS/MOD {start} - {end}")

"""
fig = plt.figure()
plt.suptitle(f"OBS/MOD {start} - {end}")

ax1 = fig.add_subplot(411)
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(wrfc2020_hcho0_d[start:end]*1000, linewidth="0.5", color='darkblue', label="hcho wrfc d lev0", linestyle=":") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho0_dmax[start:end]*1000, linewidth="0.5", color='darkblue', label="hcho wrfc dmax lev0", linestyle="solid") #274 = Julian Day 30.Sept2020
#ax1.plot(wrfc2020_hcho1_dmax[start:end]*1000, linewidth="0.5", color='violet', label="hcho wrfc dmax lev1", linestyle="solid") #274 = Julian Day 30.Sept2020
ax1.plot(camx3_2020_HCHO_d[start:end]*1000, linewidth="0.5", color='red', label="hcho camx d lev0", linestyle=":") #274 = Julian Day 30.Sept2020
#ax1.plot(camx3_2020_HCHO_dmax[start:end]*1000, linewidth="0.5", color='red', label="hcho camx dmax lev0", linestyle="solid") #274 = Julian Day 30.Sept2020
ax1.plot(emep_hcho_d[start:end],linewidth="0.5", color='green', label="hcho EMEP d", linestyle=":")
ax1.plot(hcho_d[start:end], linewidth="1", color='black', label="hcho D OBS d", linestyle="solid") #274 = Julian Day 30.Sept2020
ax1.plot(hcho19_d[start:end], linewidth="1", color='black', label="hcho D OBS d", linestyle="solid")
#ax1.plot(hcho_dmax[start:end], linewidth="1", color='black', label="hcho OBS dmax", linestyle="solid") #274 = Julian Day 30.Sept2020
#ax1.plot(hcho_m[start:end], linewidth="0.5", color='black', label="hcho D OBS mmax", linestyle="-") #274 = Julian Day 30.Sept2020
#ax1.plot(hcho_m_A[start:end], linewidth="0.5", color='grey', label="hcho A OBS mmax", linestyle="-") #274 = Julian Day 30.Sept2020
#ax1.plot(hcho_m_K[start:end], linewidth="0.5", color='darkgrey', label="hcho K OBS mmax", linestyle="-") #274 = Julian Day 30.Sept2020

#ax1.plot(emep_hcho_d[start:end],linewidth="1", color='darkgreen', label="hcho_emep", linestyle=":")
#ax2.plot(emep_c5h8_d[start:end],linewidth="1", color='darkred', label="c5h8_emep", linestyle=":")
#ax1.set_ylim(0, 8)
ax1.axvspan(DP1_s, DP1_e, color='red', alpha=0.2)
ax1.axvspan(DP2_s, DP2_e, color='red', alpha=0.2)
ax1.axvspan(DP3_s, DP3_e, color='red', alpha=0.2)
ax1.axvspan(DP4_s, DP4_e, color='red', alpha=0.2)
ax1.set_xlabel("days")
ax1.set_ylabel("[ppb]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

ax1 = fig.add_subplot(412)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.plot(tsif[start:end], color='violet', label="Tropomi SIF 743nm", linewidth="1", linestyle="solid")
ax2.set_ylabel("[mW/m2/sr/nm]", size="medium")
#ax1.plot(wrfc2020_lai[start:end],linewidth="0.5", color='blue', label="lai_wrfc", linestyle="dashed")
ax1.plot(wrflai_megan[start:end], linewidth="0.5", color='blue', label="lai_wrf_megan", linestyle="solid")
#ax2.plot(wrfc2020_dv_d[start:end],linewidth="0.5", color='darkred', label="dv_wrfc", linestyle="dashed") #TODO layer 6 not 1!!
#ax2.plot(wrfc2020_c5h8_dmax[start:end]*1000,linewidth="0.5", color='red', label="c5h8 wrfc dmax", linestyle="dashed")
#ax1.set_ylim(-5, 35)
ax1.axvspan(DP1_s, DP1_e, color='red', alpha=0.2)
ax1.axvspan(DP2_s, DP2_e, color='red', alpha=0.2)
ax1.axvspan(DP3_s, DP3_e, color='red', alpha=0.2)
ax1.axvspan(DP4_s, DP4_e, color='red', alpha=0.2)
ax1.set_xlabel("days")
ax1.set_ylabel("[degree]", size="medium")
ax1.set_ylim(0, 3500)
#ax2.set_ylabel("[ppb]", size="medium")
#ax1.set_ylabel("LAI [m2 m-2]", size="medium") #TODO convert degree to m2 m-2
#ax2.set_ylabel("dry deposition velocity [cm s-1]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

ax1 = fig.add_subplot(413)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(sm['VWC1 min[%]'],linewidth="1", color='black', label="sm_rutz1 min 0-30 cm OBS ", linestyle="solid")
ax1.plot(sm['VWC2 min[%]'],linewidth="1", color='darkgrey', label="sm_rutz2 min 0-30 cm  OBS ", linestyle="solid")
ax1.plot(sm['VWC3 min[%]'],linewidth="1", color='lightgrey', label="sm_rutz3 min 0-30 cm OBS ", linestyle="solid")
ax1.plot(sm['VWC1 max[%]'],linewidth="0.5", color='black', label="sm_rutz1 max 0-30 cm OBS ", linestyle="solid")
ax1.plot(sm['VWC2 max[%]'],linewidth="0.5", color='darkgrey', label="sm_rutz2 max 0-30 cm OBS ", linestyle="solid")
ax1.plot(sm['VWC3 max[%]'],linewidth="0.5", color='lightgrey', label="sm_rutz3 max 0-30 cm OBS ", linestyle="solid")
ax1.plot(wrf2019_sm_d[start:end], linewidth="0.5", color='green', label="sm_wrfc 1st layer, RUT", linestyle="dashed")
ax1.plot(wrfc2020_sm_d[start:end],linewidth="0.5", color='darkgreen', label="sm_wrfc 1st layer, CEN", linestyle="dashed")
ax1.plot(rss['RSS_top_wWheat'][start:end],linewidth="1", color='darkred', label="rss rutz2 0-40 cm ARIS", linestyle="solid")
ax2.plot((BOKUMetData_dailysum["PC"]*0.1)[start:end], linewidth="1", color='turquoise', label="prec BOKUR OBS")
#ax2.plot(wrf2019_rain_d, linewidth="0.5", color='blue', label="wrf precip, RUT", linestyle="dashed")
ax1.axvspan(DP1_s, DP1_e, color='red', alpha=0.2)
ax1.axvspan(DP2_s, DP2_e, color='red', alpha=0.2)
ax1.axvspan(DP3_s, DP3_e, color='red', alpha=0.2)
ax1.axvspan(DP4_s, DP4_e, color='red', alpha=0.2)
ax2.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
ax1.set_xlabel("days")
ax2.set_ylabel("[mm]", size="medium")
ax1.set_ylabel("[m3 m-3]", size="medium")
ax1.legend(loc='upper left',fontsize="small")
ax2.legend(loc='upper right',fontsize="small")


ax1 = fig.add_subplot(414)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(wrf2019_tas_dmax[start:end]-273.15,linewidth="0.5", color='red', label="t2dmax_wrf  CEN", linestyle="dashed")
ax1.plot(wrfc2020_tas_dmax[start:end]-273.15,linewidth="0.5", color='darkred', label="t2dmax_wrfc CEN", linestyle="dashed")
ax1.plot(BOKUMetData_dailymax["AT"][start:end], linewidth="1", color='lightsalmon', label="t2dmax BOKUR OBS")
#ax1.plot(wrfc2020_tas_dmax[start:end]-273.15-(BOKUMetData_dailymax["AT"][start:end]) ,linewidth="0.5", color='darkred', label="t2 dmax wrfc - obs_boku", linestyle="dashed")
ax1.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
#ax1.plot(BOKUMetData_monthly["AT"][start:end], linewidth="1", color='lightsalmon', label="t2_obs_BOKUR_m")
#ax1.plot(tas_m[start:end]-273.15,linewidth="1", color='darkred', label="t2_wrfc_m", linestyle="dashed")
#ax1.set_ylim(-5, 35)
ax1.axvspan(DP1_s, DP1_e, color='red', alpha=0.2)
ax1.axvspan(DP2_s, DP2_e, color='red', alpha=0.2)
ax1.axvspan(DP3_s, DP3_e, color='red', alpha=0.2)
ax1.axvspan(DP4_s, DP4_e, color='red', alpha=0.2)
ax1.set_xlabel("days")
ax1.set_ylabel("[degC]", size="medium")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()

#metclass['WLK]'


pff = pd.concat([hcho19_dmax,tsif,BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
pff1 = pff[DP1_s:DP1_e].dropna()
pff1.columns = pff1.columns.droplevel(-1)
#isHighGRall = pff1["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff1[isHighGRall]
x_i = pff1['4'].values.flatten()
x1= x_i       #FOR SIF
y1 = pff1['1'].values.flatten()
a=0#92*24
m1, b1 = np.polyfit(x1[a:], y1[a:], 1)

pff2 = pff[DP2_s:DP2_e].dropna()
pff2.columns = pff2.columns.droplevel(-1)
#isHighGRall = pff2["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff2[isHighGRall]
x_i = pff2['4'].values.flatten()
x2= x_i       #FOR SIF
y2 = pff2['1'].values.flatten()
a=0#92*24
m2, b2 = np.polyfit(x2[a:], y2[a:], 1)

pff3 = pff[DP3_s:DP3_e].dropna()
pff3.columns = pff3.columns.droplevel(-1)
#isHighGRall = pff3["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff3[isHighGRall]
x_i = pff3['4'].values.flatten()
x3= x_i       #FOR SIF
y3 = pff3['1'].values.flatten()
a=0#92*24
m3, b3 = np.polyfit(x3[a:], y3[a:], 1)

pff = pd.concat([hcho_d,hcho_dmax_A,hcho_dmax_K,tsif,BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff4 = pff[DP4_s:DP4_e].dropna()
pff4.columns = pff4.columns.droplevel(-1)
#isHighGRall = pff4["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff4[isHighGRall]
x_i = pff4['4'].values.flatten()
x4= x_i       #FOR SIF
y4 = pff4['1'].values.flatten()
yA4 = pff4['2'].values.flatten()
yK4 = pff4['3'].values.flatten()
a=0#92*24
m4, b4 = np.polyfit(x4[a:], y4[a:], 1)
#mA4, bA4 = np.polyfit(x4[a:], yA4[a:], 1)
#mK4, bK4 = np.polyfit(x4[a:], yK4[a:], 1)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.set_title(f"{DP1_s.date()} - {DP1_e.date()}")
ax0.scatter(x1[a:], y1[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x1, m1*x1+b1, color='red')
#ax0.legend(loc='upper right')
ax0.set_ylabel("MAXDOAS [ppb]", size="medium")

ax1.set_title(f"{DP2_s.date()} - {DP2_e.date()}")
ax1.scatter(x2[a:], y2[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x2, m2*x2+b2, color='red')

ax2.set_title(f"{DP3_s.date()} - {DP3_e.date()}")
ax2.scatter(x3[a:], y3[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.set_ylabel("MAXDOAS [ppb]", size="medium")
ax2.set_xlabel("TROPOMI SIF [mW m-2 sr-1 nm-1]", size="medium")
ax2.plot(x3, m3*x3+b3, color='red')

ax3.set_title(f"{DP4_s.date()} - {DP4_e.date()}")
ax3.scatter(x4[a:], y4[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.set_xlabel("TROPOMI SIF [mW m-2 sr-1 nm-1]", size="medium")
ax3.plot(x4, m4*x4+b4, color='red')

fig.tight_layout()
plt.show()

"""#HCHO - VWC/SM
"""
pff = pd.concat([hcho19_dmax,sm['VWC1 max[%]'],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
pff1 = pff[DP1_s:DP1_e].dropna()
#pff1.columns = pff1.columns.droplevel(-1)
#isHighGRall = pff1["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff1[isHighGRall]
x_i = pff1['4'].values.flatten()
x1= x_i       #FOR SIF
y1 = pff1['1'].values.flatten()
a=0#92*24
m1, b1 = np.polyfit(x1[a:], y1[a:], 1)

pff2 = pff[DP2_s:DP2_e].dropna()
#pff2.columns = pff2.columns.droplevel(-1)
#isHighGRall = pff2["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff2[isHighGRall]
x_i = pff2['4'].values.flatten()
x2= x_i       #FOR SIF
y2 = pff2['1'].values.flatten()
a=0#92*24
m2, b2 = np.polyfit(x2[a:], y2[a:], 1)

pff3 = pff[DP3_s:DP3_e].dropna()
#pff3.columns = pff3.columns.droplevel(-1)
#isHighGRall = pff3["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff3[isHighGRall]
x_i = pff3['4'].values.flatten()
x3= x_i       #FOR SIF
y3 = pff3['1'].values.flatten()
a=0#92*24
m3, b3 = np.polyfit(x3[a:], y3[a:], 1)

pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,tsif,BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff4 = pff[DP4_s:DP4_e].dropna()
#pff4.columns = pff4.columns.droplevel(-1)
#isHighGRall = pff4["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff4[isHighGRall]
x_i = pff4['4'].values.flatten()
x4= x_i       #FOR SIF
y4 = pff4['1'].values.flatten()
yA4 = pff4['2'].values.flatten()
yK4 = pff4['3'].values.flatten()
a=0#92*24
m4, b4 = np.polyfit(x4[a:], y4[a:], 1)
#mA4, bA4 = np.polyfit(x4[a:], yA4[a:], 1)
#mK4, bK4 = np.polyfit(x4[a:], yK4[a:], 1)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.set_title(f"SPRING 1: {DP1_s.date()} - {DP1_e.date()}")
ax0.scatter(x1[a:], y1[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x1, m1*x1+b1, color='red')
#ax0.legend(loc='upper right')
ax0.set_ylabel("HCHO [ppb]", size="medium")

ax1.set_title(f"SUMMER 1: {DP2_s.date()} - {DP2_e.date()}")
ax1.scatter(x2[a:], y2[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x2, m2*x2+b2, color='red')

ax2.set_title(f"SPRING 2: {DP4_s.date()} - {DP4_e.date()}")
ax2.scatter(x4[a:], y4[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.set_ylabel("HCHO [ppb]", size="medium")
ax2.set_xlabel("VWC [%]", size="medium")
ax2.plot(x4, m4*x4+b4, color='red')

ax3.set_title(f"SUMMER 2: {DP3_s.date()} - {DP3_e.date()}")
ax3.scatter(x3[a:], y3[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.set_xlabel("VWC [%]", size="medium")
ax3.plot(x3, m3*x3+b3, color='red')

fig.tight_layout()
plt.show()

"""
#HCHO - RSS
"""
pff = pd.concat([hcho19_dmax,rss['RSS_top_wWheat'],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
pff1 = pff[DP1_s:DP1_e].dropna()
#pff1.columns = pff1.columns.droplevel(-1)
#isHighGRall = pff1["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff1[isHighGRall]
x_i = pff1['4'].values.flatten()
x1= x_i       #FOR SIF
y1 = pff1['1'].values.flatten()
a=0#92*24
m1, b1 = np.polyfit(x1[a:], y1[a:], 1)

pff2 = pff[DP2_s:DP2_e].dropna()
#pff2.columns = pff2.columns.droplevel(-1)
#isHighGRall = pff2["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff2[isHighGRall]
x_i = pff2['4'].values.flatten()
x2= x_i       #FOR SIF
y2 = pff2['1'].values.flatten()
a=0#92*24
m2, b2 = np.polyfit(x2[a:], y2[a:], 1)

pff3 = pff[DP3_s:DP3_e].dropna()
#pff3.columns = pff3.columns.droplevel(-1)
#isHighGRall = pff3["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff3[isHighGRall]
x_i = pff3['4'].values.flatten()
x3= x_i       #FOR SIF
y3 = pff3['1'].values.flatten()
a=0#92*24
m3, b3 = np.polyfit(x3[a:], y3[a:], 1)

pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,tsif,BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff4 = pff[DP4_s:DP4_e].dropna()
#pff4.columns = pff4.columns.droplevel(-1)
#isHighGRall = pff4["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff4[isHighGRall]
x_i = pff4['4'].values.flatten()
x4= x_i       #FOR SIF
y4 = pff4['1'].values.flatten()
yA4 = pff4['2'].values.flatten()
yK4 = pff4['3'].values.flatten()
a=0#92*24
m4, b4 = np.polyfit(x4[a:], y4[a:], 1)
#mA4, bA4 = np.polyfit(x4[a:], yA4[a:], 1)
#mK4, bK4 = np.polyfit(x4[a:], yK4[a:], 1)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.set_title(f"SPRING 1: {DP1_s.date()} - {DP1_e.date()}")
ax0.scatter(x1[a:], y1[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x1, m1*x1+b1, color='red')
#ax0.legend(loc='upper right')
ax0.set_ylabel("HCHO [ppb]", size="medium")

ax1.set_title(f"SUMMER 1: {DP2_s.date()} - {DP2_e.date()}")
ax1.scatter(x2[a:], y2[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x2, m2*x2+b2, color='red')

ax2.set_title(f"SPRING 2: {DP4_s.date()} - {DP4_e.date()}")
ax2.scatter(x4[a:], y4[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.set_ylabel("HCHO [ppb]", size="medium")
ax2.set_xlabel("RSS [%]", size="medium")
ax2.plot(x4, m4*x4+b4, color='red')

ax3.set_title(f"SUMMER 2: {DP3_s.date()} - {DP3_e.date()}")
ax3.scatter(x3[a:], y3[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.set_xlabel("RSS [%]", size="medium")
ax3.plot(x3, m3*x3+b3, color='red')

fig.tight_layout()
plt.show()
"""

"""HCHO - TMAX"""
pff = pd.concat([hcho19_dmax,BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
pff1 = pff[DP1_s:DP1_e].dropna()
#pff1.columns = pff1.columns.droplevel(-1)
#isHighGRall = pff1["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff1[isHighGRall]
x_i = pff1['4'].values.flatten()
x1= x_i       #FOR SIF
y1 = pff1['1'].values.flatten()
a=0#92*24
m1, b1 = np.polyfit(x1[a:], y1[a:], 1)

pff2 = pff[DP2_s:DP2_e].dropna()
#pff2.columns = pff2.columns.droplevel(-1)
#isHighGRall = pff2["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff2[isHighGRall]
x_i = pff2['4'].values.flatten()
x2= x_i       #FOR SIF
y2 = pff2['1'].values.flatten()
a=0#92*24
m2, b2 = np.polyfit(x2[a:], y2[a:], 1)

pff3 = pff[DP3_s:DP3_e].dropna()
#pff3.columns = pff3.columns.droplevel(-1)
#isHighGRall = pff3["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff3[isHighGRall]
x_i = pff3['4'].values.flatten()
x3= x_i       #FOR SIF
y3 = pff3['1'].values.flatten()
a=0#92*24
m3, b3 = np.polyfit(x3[a:], y3[a:], 1)

pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff4 = pff[DP4_s:DP4_e].dropna()
#pff4.columns = pff4.columns.droplevel(-1)
#isHighGRall = pff4["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff4[isHighGRall]
x_i = pff4['4'].values.flatten()
x4= x_i       #FOR SIF
y4 = pff4['1'].values.flatten()
yA4 = pff4['2'].values.flatten()
yK4 = pff4['3'].values.flatten()
a=0#92*24
m4, b4 = np.polyfit(x4[a:], y4[a:], 1)
#mA4, bA4 = np.polyfit(x4[a:], yA4[a:], 1)
#mK4, bK4 = np.polyfit(x4[a:], yK4[a:], 1)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.set_title(f"SPRING 1: {DP1_s.date()} - {DP1_e.date()}")
ax0.scatter(x1[a:], y1[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x1, m1*x1+b1, color='red')
#ax0.legend(loc='upper right')
ax0.set_ylabel("HCHO [ppb]", size="medium")

ax1.set_title(f"SUMMER 1: {DP2_s.date()} - {DP2_e.date()}")
ax1.scatter(x2[a:], y2[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x2, m2*x2+b2, color='red')

ax2.set_title(f"SPRING 2: {DP4_s.date()} - {DP4_e.date()}")
ax2.scatter(x4[a:], y4[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.set_ylabel("HCHO [ppb]", size="medium")
ax2.set_xlabel("Tmax [degC]", size="medium")
ax2.plot(x4, m4*x4+b4, color='red')

ax3.set_title(f"SUMMER 2: {DP3_s.date()} - {DP3_e.date()}")
ax3.scatter(x3[a:], y3[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.set_xlabel("Tmax [degC]", size="medium")
ax3.plot(x3, m3*x3+b3, color='red')

fig.tight_layout()
plt.show()

"""HCHO - GLOBAL RADIATION"""
pff = pd.concat([hcho19_dmax,BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','4','GR'])
pff1 = pff[DP1_s:DP1_e].dropna()
x_i = pff1['GR'].values.flatten()
x1= x_i
y1 = pff1['1'].values.flatten()
a=0#92*24
m1, b1 = np.polyfit(x1[a:], y1[a:], 1)

pff2 = pff[DP2_s:DP2_e].dropna()
#pff2.columns = pff2.columns.droplevel(-1)
#isHighGRall = pff2["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff2[isHighGRall]
x_i = pff2['GR'].values.flatten()
x2= x_i       #FOR SIF
y2 = pff2['1'].values.flatten()
a=0#92*24
m2, b2 = np.polyfit(x2[a:], y2[a:], 1)

pff3 = pff[DP3_s:DP3_e].dropna()
#pff3.columns = pff3.columns.droplevel(-1)
#isHighGRall = pff3["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff3[isHighGRall]
x_i = pff3['GR'].values.flatten()
x3= x_i       #FOR SIF
y3 = pff3['1'].values.flatten()
a=0#92*24
m3, b3 = np.polyfit(x3[a:], y3[a:], 1)

pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,BOKUMetData_dailymax["AT"],BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff4 = pff[DP4_s:DP4_e].dropna()
#pff4.columns = pff4.columns.droplevel(-1)
#isHighGRall = pff4["GR"] > 15000 #15 KWh (per day) Globalstrahlung
#pff_HighGRdays = pff4[isHighGRall]
x_i = pff4['GR'].values.flatten()
x4= x_i       #FOR SIF
y4 = pff4['1'].values.flatten()
yA4 = pff4['2'].values.flatten()
yK4 = pff4['3'].values.flatten()
a=0#92*24
m4, b4 = np.polyfit(x4[a:], y4[a:], 1)
#mA4, bA4 = np.polyfit(x4[a:], yA4[a:], 1)
#mK4, bK4 = np.polyfit(x4[a:], yK4[a:], 1)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()
ax0.set_title(f"SPRING 1: {DP1_s.date()} - {DP1_e.date()}")
ax0.scatter(x1[a:], y1[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax0.plot(x1, m1*x1+b1, color='red')
#ax0.legend(loc='upper right')
ax0.set_ylabel("HCHO [ppb]", size="medium")

ax1.set_title(f"SUMMER 1: {DP2_s.date()} - {DP2_e.date()}")
ax1.scatter(x2[a:], y2[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax1.plot(x2, m2*x2+b2, color='red')

ax2.set_title(f"SPRING 2: {DP4_s.date()} - {DP4_e.date()}")
ax2.scatter(x4[a:], y4[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax2.set_ylabel("HCHO [ppb]", size="medium")
ax2.set_xlabel("global rad sum [Wh m-2]", size="medium")
ax2.plot(x4, m4*x4+b4, color='red')

ax3.set_title(f"SUMMER 2: {DP3_s.date()} - {DP3_e.date()}")
ax3.scatter(x3[a:], y3[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
ax3.set_xlabel("global rad sum [Wh m-2]", size="medium")
ax3.plot(x3, m3*x3+b3, color='red')

fig.tight_layout()
plt.show()
""""
#BACKUP

#pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,wrfc2020_hcho1_dmax,metclass],axis=1, keys=['1','2','3','4','WLK'])
#pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,camx3_2020_HCHO_dmax,BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff = pd.concat([hcho_dmax,hcho_dmax_A,hcho_dmax_K,tsif,BOKUMetData_dailysum["GR"]],axis=1, keys=['1','2','3','4','GR'])
pff = pff[June:Sept].dropna()
pff.columns = pff.columns.droplevel(-1)
print(pff)
#pff = pff.drop(pff[pff.WLK == "C"].index)
#print(pff)

isHighGRall = pff["GR"] > 15000 #15 KWh (per day) Globalstrahlung
pff_HighGRdays = pff[isHighGRall]
print(pff_HighGRdays)

#pff = pff_HighGRdays

#print(wrfc2020_hcho1_dmax.values.shape)
x_i = pff['4'].values.flatten()
#print(x_i.shape)
#x= x_i*1000 #FOR WRF-CHEM + CAMX
x= x_i       #FOR SIF
y = pff['1'].values.flatten()
yA = pff['2'].values.flatten()
yK = pff['3'].values.flatten()

a=0#92*24
m, b = np.polyfit(x[a:], y[a:], 1)
mA, bA = np.polyfit(x[a:], yA[a:], 1)
mK, bK = np.polyfit(x[a:], yK[a:], 1)
print(m,mA,mK,b,bA,bK)

#R2_Forc_NO2concentr = (stats.spearmanr(o3, no2))[0] ** 2

fig2 = plt.figure()
plt.scatter(x[a:], y[a:], color='red',label='Axis D (Stephansdom)') # , label=(r"$R^2$=%.2f, Bias=%.2f" % (R2_Forc_i, Bias_Forc_i)))#, s=3, label=u"STQ,  R²=0.92")  #squared= u"\u00B2"?
plt.scatter(x[a:], yA[a:], color='violet',label='Axis A (Vetmed)') #label=r"$r$=%.2f" % (R_hcho))
plt.scatter(x[a:], yK[a:], color='green',label='Axis K (Wienerwald)')
plt.plot(x, m*x+b, color='red')
plt.plot(x, mA*x+bA, color='violet')
plt.plot(x, mK*x+bK, color='green')
#m, b = np.polyfit(x, y, 1)
#plt.plot(x, m * x + b)
plt.legend(loc='upper right')
#plt.xlabel("WRF [ppb]", size="medium")
#plt.xlabel("CAMX [ppb]", size="medium")
plt.xlabel("TROPOMI SIF [mW m-2 sr-1 nm-1]", size="medium")
plt.ylabel("MAXDOAS [ppb]", size="medium")
#plt.suptitle("HCHO dmax 2020 summer (JJA)")
plt.show()
"""