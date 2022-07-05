# -*- coding: utf-8 -*-
__author__ = 'lnx'

import numpy as np
import pandas as pd
from datetime import datetime
from scipy import stats
import cftime
import nc_time_axis
import monthdelta
import matplotlib.pyplot as plt
import met.library.BOKUMet_Data
from met.library.Datetime_recipies import datestdtojd
from met.library.conversions import *
from met.library import ReadinVindobona_Filter_fullperiod
from met.library import ReadinCAMX_2
from met.library import ReadinPROBAV_LAI_300m
from netCDF4 import Dataset
import netCDF4

"read in VINDOBONA"
foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1, 0, 0, 0))
hcho_w = hcho_dmax.resample("W").mean()

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
BOKUMetData_weekly = BOKUMetData_dailysum.resample('W').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                      'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

vp_sat = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3))  #kPa sh. Dingman
vp_air = 0.611 * np.exp((17.3 * BOKUMetData_hourlymean["AT"])/(BOKUMetData_hourlymean["AT"]+237.3)) * (BOKUMetData_hourlymean["RH"]/100)
vpd = vp_sat - vp_air
#print(vp_sat,vp_air, vpd)
#vpd.plot()
#plt.show()
vpd_d = vpd.resample('D').mean()
vpd_dmax = vpd.resample('D').max()
vpd_dmax_w = vpd_dmax.resample('W').max()

'''READ IN EMEP data'''
##Jans indexes for Vienna gridpoint:
#wrf_vie_i=109 #TODO Double check! i=x=long
#wrf_vie_j=58  #TODO Double check! j=y=lat
wrf_vie_i=63  #16.40278
wrf_vie_j=60  #48.20032

#see manual check in script FinNearest_EMEP_gridpoints.py
wrf_STE_i = 60 #16.3742 48.2086
wrf_STE_j = 62
wrf_LOB_i = 59 #16.5269 48.1625
wrf_LOB_j = 66
wrf_HER_i = 63 #16.2983 48.2708
wrf_HER_j = 60


path = '/windata/DATA/models/boku/EMEP/output/UOZONE/'

#EMISSIONS
fh_E = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/uozone_month_20180206_20201231.nc", mode='r') #TODO: join all files

#CONCENTRATIONS
#file1 = path + 'uozone_hourInst.nc'
#fh_o3 = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ppb_O3_uozone.nc", mode='r') #TODO: update join all files
#fh_o3 = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ug_O3_uozone.nc", mode='r') #TODO: update join all files
#fh_hcho = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ppb_HCHO_uozone.nc", mode='r') #TODO: update join all files
#fh_c5h8 = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ppb_C5H8_uozone.nc", mode='r') #TODO: update join all files
fh_o3 = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ug_O3_uozone_new2.nc", mode='r') #TODO: update join all files
fh_hcho = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ppb_HCHO_uozone_new.nc", mode='r') #TODO: update join all files
fh_c5h8 = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ppb_C5H8_uozone_new.nc", mode='r') #TODO: update join all files
##DDEPOSTION
fh_ddp = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/DDEP_O3_m2Grid_new2.nc", mode='r')

lons = fh_ddp.variables['lon'][1]
lats = fh_ddp.variables['lat'][1]
emep_time_o3 = fh_o3.variables['time']
print(emep_time_o3[:]) #[43135.75  43136.75  43137.75 44192.75 44193.75 44194.45833333]
jd_o3 = netCDF4.num2date(emep_time_o3[:],emep_time_o3.units, only_use_cftime_datetimes=False)
print(jd_o3)

#emep_time = fh_c5h8.variables['time']
#emep_time_ddp = fh_ddp.variables['time']
#emep_time_month = fh_E.variables['time']
#jd_part = netCDF4.num2date(emep_time[:],emep_time.units)
#jd_ddp = netCDF4.num2date(emep_time_ddp[:],emep_time_ddp.units)
#jd_month = netCDF4.num2date(emep_time_month[:],emep_time_month.units)

"""
emep_E_c5h8_m = fh_E.variables['Emis_mgm2_BioNatC5H8'][:,wrf_vie_j, wrf_vie_i]
emep_E_c5h8_m = pd.Series(emep_E_c5h8_m[:],index=jd_month)
emep_E_terp_m = fh_E.variables['Emis_mgm2_BioNatTERP'][:,wrf_vie_j, wrf_vie_i]
emep_E_terp_m = pd.Series(emep_E_terp_m[:],index=jd_month)
#print(emep_E_c5h8_m)

emep_c5h8_d = fh_c5h8.variables['SURF_ppb_C5H8'][:,wrf_vie_j, wrf_vie_i]
emep_c5h8_d = pd.Series(emep_c5h8_d[:],index=jd_part)
emep_hcho_d = fh_hcho.variables['SURF_ppb_HCHO'][:,wrf_vie_j, wrf_vie_i]
emep_hcho_d = pd.Series(emep_hcho_d[:],index=jd_part)
"""
emep_o3_d_STE = fh_o3.variables['SURF_ug_O3'][:, wrf_STE_i,wrf_STE_j] #(time, j, i)
emep_o3_d_STE = pd.Series(emep_o3_d_STE[:],index=jd_o3)
emep_o3_d_STE_w = emep_o3_d_STE.resample('W').mean()
emep_o3_d_LOB = fh_o3.variables['SURF_ug_O3'][:, wrf_LOB_i,wrf_LOB_j] #(time, j, i)
emep_o3_d_LOB = pd.Series(emep_o3_d_LOB[:],index=jd_o3)
emep_o3_d_LOB_w = emep_o3_d_LOB.resample('W').mean()
emep_o3_d_HER = fh_o3.variables['SURF_ug_O3'][:, wrf_HER_i,wrf_HER_j] #(time, j, i)
emep_o3_d_HER = pd.Series(emep_o3_d_HER[:],index=jd_o3)
emep_o3_d_HER_w = emep_o3_d_HER.resample('W').mean()
emep_o3_d_area = fh_o3.variables['SURF_ug_O3'][:,:,:]
#print(emep_o3_d_area)
emep_o3_d_area = emep_o3_d_area.mean(axis=(1, 2))
emep_o3_d_area = pd.Series(emep_o3_d_area[:],index=jd_o3)
emep_o3_d_area_w = emep_o3_d_area.resample('W').mean()
print(emep_o3_d_area)

#print(emep_o3_d)
#emep_o3_d = emep_o3_d.resample('D').mean()
#print(emep_o3_d[datetime(2020,3,2,0,0)])

#emep_ddep_d = fh_ddp.variables['DDEP_O3_m2Grid'][:,wrf_vie_j,wrf_vie_i] #(time, j, i)
#emep_ddep_d = pd.Series(emep_ddep_d[:],index=jd_ddp)

'''READ IN EEA air pollution data'''
pathbase2 = "/windata/DATA/obs_point/chem/EEA/"
#"AT"+compound+"stationsname"+"year"+_"timeseries.csv"
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
o3_1990_2020_mda1 = o3_1990_2020_mda1[datetime(2018,1,1):datetime(2020,12,31)] #TODO: Attention! Timeserie is filtered#

#o3_1990_2020_mda1.plot()
#plt.show()
#exit()
#print(o3_1990_2020_mda1["AT9JAEG"].index)

o3_2020_mda8 = o3_2020_mda1.resample('8H', label='right').mean()
o3_2020_mda8 = o3_2020_mda8.resample('D').mean()
o3_1990_2020_mda8 = pd.concat([o3_1990_2019_mda8, o3_2020_mda8], axis=0)
o3_1990_2020_mda8 = o3_1990_2020_mda8#*ugm3toppb_o3 #MUG->PPB
o3_1990_2020_da = o3_1990_2020_mda8.resample('D').mean()
o3_1990_2020_m = o3_1990_2020_mda8.resample('M').mean()
o3_1990_2020_mda1_w = o3_1990_2020_mda1.resample('W').mean()
o3_1990_2020_mda8_w = o3_1990_2020_mda8.resample('W').mean()
#o3_1990_2020_mda1_w.plot()
#plt.show()
#exit()

"read in VINDOBONA"
foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1))
#print(hcho_d.index)

'''READ IN PROBAV_LAI300m'''
LAI_df = ReadinPROBAV_LAI_300m.LAI()

'''
Plotting
'''
#start = datetime(2018, 2, 6, 00, 00)
start = datetime(2020, 3, 1, 00, 00)
end = datetime(2020, 12, 31, 00, 00)
#print(len(emep_o3_d[start:end]), len(o3_1990_2020_mda1_w['AT9JAEG'][start:end]))


fig = plt.figure()
#ax1 = fig.add_subplot(2, 1, (1, 1))#, sharex=True)
ax1 = fig.add_subplot(1, 1, (1, 1))#, sharex=True)
plt.suptitle("1 validation")
ax1.plot(o3_1990_2020_mda1_w['AT9JAEG'],linewidth="1", color='darkgreen', label="JAEG", linestyle="-") #TODO mda1 vs da (mda8)
ax1.plot(o3_1990_2020_mda1_w['AT9STEF'],linewidth="1", color='violet', label="STEF", linestyle="-") #mda1 vs da (mda8)
ax1.plot(o3_1990_2020_mda1_w['AT90LOB'],linewidth="1", color='chartreuse', label="LOB", linestyle="-") #mda1 vs da (mda8)
ax1.plot(emep_o3_d_HER_w,color='darkgreen', linestyle=":")#, marker=".") #(time, j, i)
ax1.plot(emep_o3_d_STE_w,color='violet', linestyle=":")#, marker=".") #(time, j, i)
ax1.plot(emep_o3_d_LOB_w,color='chartreuse', linestyle=":")#, marker=".") #(time, j, i)
ax1.plot(emep_o3_d_area_w,color="grey",linestyle=":", linewidth="5", label="area mean")
ax1.legend(loc='upper right')
#ax3 = fig.add_subplot(2, 1, (2, 2))#, sharex=True)
#ax3.plot(emep_o3_d_HER_w,color='purple', linestyle=":")#, marker=".") #(time, j, i)
#ax3.plot(emep_o3_d_STE_w,color='violet', linestyle=":")#, marker=".") #(time, j, i)
#ax3.plot(emep_o3_d_LOB_w,color='blue', linestyle=":")#, marker=".") #(time, j, i)
#ax3.plot(emep_o3_d_HER,color='purple', linestyle=" ", marker=".") #(time, j, i)
#ax3.plot(emep_o3_d_STE,color='violet', linestyle=" ", marker=".") #(time, j, i)
#ax3.plot(emep_o3_d_LOB,color='blue', linestyle=" ", marker=".") #(time, j, i)
ax1.set_ylim(0, 150)
#ax3.set_ylim(0, 150)
ax1.set_ylabel("[ug/m2]", size="medium")
#ax3.set_ylabel("[ug/m2]", size="medium")
plt.show()
exit()


data = pd.concat([o3_1990_2019_mda1['AT9JAEG'].resample("D").mean(), o3_1990_2019_mda1['AT9STEF'].resample("D").mean(),
                  o3_1990_2019_mda1['AT90LOB'].resample("D").mean(), emep_o3_d_HER.resample("D").mean(), emep_o3_d_STE.resample("D").mean(),
                  emep_o3_d_LOB.resample("D").mean()], axis=1)
data.columns = ['obs_her', 'obs_ste', 'obs_lob', 'mod_her', 'mod_ste', 'mod_lob']
data = data.dropna()  #subset=['GRhigh'])
print(data)
#pff_clear2 = pff_clear.loc[pff_clear["GR"] >= 4500]

SRho_her, Sp_her = stats.spearmanr(data['obs_her'], data['mod_her'])
SRho_ste, Sp_ste = stats.spearmanr(data['obs_ste'], data['mod_ste'])
SRho_lob, Sp_lob = stats.spearmanr(data['obs_her'], data['mod_lob'])

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
#fig.suptitle('Horizontally stacked subplots')
ax1.set_title('(a) JAE: \n R={:.2f} \n p={:.2f}'.format(SRho_her, Sp_her), fontsize='small')
ax2.set_title('(b) STE: \n R={:.2f} \n p={:.2f}'.format(SRho_ste, Sp_ste), fontsize='small')
ax3.set_title('(c) LOB: \n R={:.2f} \n p={:.2f}'.format(SRho_lob, Sp_lob), fontsize='small')
ax1.scatter(data['obs_her'], data['mod_her'],label="JAEG", s=1)
ax2.scatter(data['obs_ste'], data['mod_ste'],label="STEF", s=1)
ax3.scatter(data['obs_lob'], data['mod_lob'],label="LOB", s=1)
ax1.plot(range(180),range(180),linewidth=0.5)
ax2.plot(range(180),range(180),linewidth=0.5)
ax3.plot(range(180),range(180),linewidth=0.5)
ax1.set_ylim(0,180)
ax2.set_ylim(0,180)
ax3.set_ylim(0,180)
ax1.set_xlim(0,180)
ax2.set_xlim(0,180)
ax3.set_xlim(0,180)
ax1.set_ylabel("[ug/m³]", size="medium")
plt.show()
exit()




















fig = plt.figure()
plt.suptitle("2b deposition/EMEP")
ax1 = fig.add_subplot(3, 1, (1, 2))#, sharex=True)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(emep_ddep_d.index, emep_ddep_d.values, linewidth="1", color='blue', label="DDEP_O3", linestyle="solid")
ax2.plot(emep_o3_d.index, emep_o3_d.values, linewidth="1", color='violet', label="O3_mod", linestyle="solid")
#ax1.set_ylim(0, 8)
ax1.set_xlabel("days")
#ax1.set_xlim(start,end)
#ax3.set_ylabel("[μg/m³]", size="medium")
#ax2.set_ylabel("[μg/m³]", size="medium")
ax1.set_ylabel("[mg/m2]", size="medium")
ax1.grid()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3 = fig.add_subplot(3, 1, (3, 3))#, sharex=True)
ax4 = ax3.twinx()
ax3.grid()
ax3.plot(LAI_df[start:end].index, LAI_df[start:end].LAI, linewidth="3",color="green", alpha=0.3, label="LAI")
ax4.plot(BOKUMetData_dailysum["AT"][start:end].index,BOKUMetData_dailysum["AT"][start:end].values,linewidth="2",color="red", alpha=0.2, label="T_air DA")
ax3.set_ylabel("LAI [-]")
ax4.set_ylabel("AT [°C]") #average daily temperature
plt.show()

exit()



fig = plt.figure()
#gridspec_kw={'height_ratios': [1, 2]
plt.suptitle("1b biogenic VOC emission/EMEP")
ax1 = fig.add_subplot(3, 1, (1, 2))#, sharex=True)
ax1 = plt.gca()
ax2 = ax1.twinx()
#ax3 = ax2.twinx()
ax1.plot(hcho_w[start:end], linewidth="1", color='black', label="HCHO", linestyle=":")
ax1.plot(emep_hcho_d[start:end].index, emep_hcho_d[start:end].values, linewidth="1", color='black', label="HCHO_emep", linestyle=":")
ax1.plot(emep_c5h8_d[start:end].index, emep_c5h8_d[start:end].values, linewidth="1", color='red', label="C5H8_emep", linestyle=":")
#ax2.plot(emep_E_c5h8_m[start:end].index,emep_E_c5h8_m[start:end].values,linewidth="1", color='red', label="E_C5H8_emep", linestyle=" ", marker="o")
#ax2.plot(emep_E_terp_m[start:end].index,emep_E_terp_m[start:end].values,linewidth="1", color='orange', label="E_TERP_emep", linestyle=" ", marker="o")

#ax2.plot(emep_eISO_d[start:end], linewidth="1", color='black', label="ISO", linestyle="solid")
#ax2.plot(emep_eTERP_d[start:end], linewidth="1", color='black', label="TERP", linestyle="solid")
#TODO CAMX ISO, MT, METH
#ax1.set_ylim(0, 8)
ax1.set_xlabel("days")
#ax1.set_xlim(start,end)
ax1.set_ylabel("[ppb]", size="medium")
ax2.set_ylabel("[mg/m2]", size="medium")
#ax3.set_ylabel("[]", size="medium")
ax1.grid()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3 = fig.add_subplot(3, 1, (3, 3))#, sharex=True)
ax4 = ax3.twinx()
ax3.plot(LAI_df[datetime(2018,2,6):datetime(2020,12,31)].index, LAI_df[datetime(2018,2,6):datetime(2020,12,31)].LAI, linewidth="3",color="green", alpha=0.3, label="LAI")
ax4.plot(BOKUMetData_dailysum["AT"][datetime(2018,2,6):datetime(2020,12,31)].index,BOKUMetData_dailysum["AT"][datetime(2018,2,6):datetime(2020,12,31)].values,linewidth="2",color="red", alpha=0.2, label="T_air DA")
ax3.set_ylabel("LAI[-]")
ax4.set_ylabel("AT[°C]") #average daily temperature
plt.show()
