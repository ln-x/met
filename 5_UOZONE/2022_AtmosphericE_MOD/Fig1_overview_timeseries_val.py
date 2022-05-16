# -*- coding: utf-8 -*-
__author__ = 'lnx'

import numpy as np
import pandas as pd
from datetime import datetime
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
path = '/windata/DATA/models/boku/EMEP/output/UOZONE/'
#path = '/windata/DATA/models/boku/EMEP/output/UOZONE/'+folder
#2018-02-06 #DDEP_03 missing
#"2018-12-27" #not run because over 2 years raises error
#folder = ["2018-03-20", "2018-05-01", "2018-07-23", \
#"2018-09-03","2018-10-14", "2018-11-25", \
#"2019-02-06", "2019-03-20","2019-05-01", \
#"2019-06-11","2019-07-23","2019-09-03", \
#"2019-10-14", "2019-11-25"]

#EMISSIONS
#fh_E = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/uozone_month_20180320_20200202.nc", mode='r') #TODO: join all files
fh_E = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/uozone_month_20180320_20201226.nc", mode='r') #TODO: join all files

#CONCENTRATIONS
#file1 = path + 'uozone_hourInst.nc'
#fh_o3 = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ppb_O3_uozone.nc", mode='r') #TODO: update join all files
fh_o3 = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ug_O3_uozone.nc", mode='r') #TODO: update join all files
fh_hcho = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ppb_HCHO_uozone.nc", mode='r') #TODO: update join all files
fh_c5h8 = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/SURF_ppb_C5H8_uozone.nc", mode='r') #TODO: update join all files

##DDEPOSTION
fh_ddp = Dataset("/windata/DATA/models/boku/EMEP/output/UOZONE/DDEP_O3_m2Grid_uozone.nc", mode='r') #TODO: update join all files

##fh1 = Dataset(file1, mode='r')
lons = fh_ddp.variables['lon'][1]
lats = fh_ddp.variables['lat'][1]
emep_time = fh_c5h8.variables['time']
emep_time_full = fh_ddp.variables['time']

emep_time_month = fh_E.variables['time']
jd_part = netCDF4.num2date(emep_time[:],emep_time.units)
jd = netCDF4.num2date(emep_time_full[:],emep_time_full.units)
jd_month = netCDF4.num2date(emep_time_month[:],emep_time_month.units)
##print(jd)
emep_E_c5h8_m = fh_E.variables['Emis_mgm2_BioNatC5H8'][:,wrf_vie_j, wrf_vie_i]
emep_E_c5h8_m = pd.Series(emep_E_c5h8_m[:],index=jd_month)
emep_E_terp_m = fh_E.variables['Emis_mgm2_BioNatTERP'][:,wrf_vie_j, wrf_vie_i]
emep_E_terp_m = pd.Series(emep_E_terp_m[:],index=jd_month)

emep_c5h8_d = fh_c5h8.variables['SURF_ppb_C5H8'][:,wrf_vie_j, wrf_vie_i]
emep_c5h8_d = pd.Series(emep_c5h8_d[:],index=jd_part)
emep_hcho_d = fh_hcho.variables['SURF_ppb_HCHO'][:,wrf_vie_j, wrf_vie_i]
emep_hcho_d = pd.Series(emep_hcho_d[:],index=jd_part)
emep_o3_d = fh_o3.variables['SURF_ug_O3'][:,wrf_vie_j,wrf_vie_i] #(time, j, i)
emep_o3_d = pd.Series(emep_o3_d[:],index=jd)

emep_ddep_d = fh_ddp.variables['DDEP_O3_m2Grid'][:,wrf_vie_j,wrf_vie_i] #(time, j, i)
emep_ddep_d = pd.Series(emep_ddep_d[:],index=jd)


'''READ IN CAMX DATA'''
pathbase_camx_1819 = "/windata/DATA/models/boku/CAMX/2018-2019"
pathbase_camx_2020 = "/windata/DATA/models/boku/CAMX/BOKU2020"
camx3_y_vie_isBOKU20 = 76  #for Wien Innere Stadt 1,76,181
camx3_x_vie_isBOKU20 = 178 #179: father west...  181: Wien Innere Stadt
camx3_y_vie_is1819 = 53  #53 LAT Gersthof
camx3_x_vie_is1819 = 100 #102 #100: WienerWald west of Vienna

#EMISSIONS
BioEmis_1819 = ReadinCAMX_2.loadCAMXALL(pathbase_camx_1819,camx3_x_vie_is1819,camx3_y_vie_is1819)
print(BioEmis_1819)
BioEmis_20 = ReadinCAMX_2.loadCAMXALL(pathbase_camx_2020,camx3_x_vie_isBOKU20,camx3_y_vie_isBOKU20)
#print(BioEmis)

#CONCENTRATIONS
#for i in ["HCHO","O3", "NO", "NO2"]:
file_o3 = pathbase_camx_2020 + '/4_CAMXoutput/BOKU2020_BASE_WRFchem3_202001-09_O3.nc'
file_hcho = pathbase_camx_2020 + '/4_CAMXoutput/BOKU2020_BASE_WRFchem3_202001-09_HCHO.nc'
#file = '/windata/DATA/models/boku/CAMX/BOKU2020_BASE_WRFchem9_202001-03_'+ i + '.nc'
f_o3 = Dataset(file_o3, mode='r')
f_hcho = Dataset(file_hcho, mode='r')
hcho = f_hcho.variables["HCHO"][:, 76, 181] #TODO 181 vs 178
o3 = f_o3.variables["O3"][:, 76, 181]  #TODO 181 vs 178
xtime = f_o3.variables["XTIME"][:]  #TODO 181 vs 178
#print(xtime) #6481 currently; hourly values
#exit()

    #par1 = pd.DataFrame(par[:, 76, 181], index=wrfc_time_construct)
    #globals()[f"camx3_2020_{i}_d"] = par1.resample('D').mean()
    #globals()[f"camx3_2020_{i}_dmax"] = par1.resample('D').max()

#DEPOSITION
DDepO3_1819 = ReadinCAMX_2.loadCAMXALL_DD(pathbase_camx_1819,camx3_x_vie_is1819,camx3_y_vie_is1819)

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
o3_1990_2020_mda1 = o3_1990_2020_mda1[datetime(2018,1,1):datetime(2020,12,31)] #TODO: Attention! Timeserie is filtered
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

"read in VINDOBONA"
foldername_D = "/windata/DATA/remote/ground/maxdoas/MAXDOAS_DQ"
hcho_d, hcho_dmax, hcho_m = ReadinVindobona_Filter_fullperiod.loadfileALL(foldername_D,"D", begin= datetime(2017, 5, 1))
#print(hcho_d.index)

'''READ IN PROBAV_LAI300m'''
LAI_df = ReadinPROBAV_LAI_300m.LAI()

#print("MAM18:", LAI_df[MAM18_s:MAM18_e].mean())
#print("MAM20:", LAI_df[MAM20_s:MAM20_e].mean())
#print("JJA20:", LAI_df[JJA20_s:JJA20_e].mean())
#print("JJA19:", LAI_df[JJA19_s:JJA19_e].mean())

print("May18:", LAI_df[datetime(2018, 5, 1, 00, 00):datetime(2018, 5, 31, 00, 00)].mean())
print("May20:", LAI_df[datetime(2020, 5, 1, 00, 00):datetime(2020, 5, 31, 00, 00)].mean())
#print("Aug20:", LAI_df[datetime(2020, 8, 1, 00, 00):JJA20_e].mean())
#print("Aug19:", LAI_df[datetime(2019, 8, 1, 00, 00):JJA19_e].mean())
exit()


'''
Plotting
'''
#start = datetime(2017, 5, 1, 00, 00)
start = datetime(2018, 2, 6, 00, 00)
#start = datetime(2017, 1, 1, 00, 00)
#end = datetime(2021, 8, 31, 00, 00)
#end = datetime(2019, 11, 25, 00, 00)
end = datetime(2020, 12, 31, 00, 00)
#end2 = datetime(2020, 10, 30, 00, 00)

#print(emep_hcho_d.index)
#print(emep_hcho_d.values)


fig = plt.figure()
#gridspec_kw={'height_ratios': [1, 2]
plt.suptitle("1a biogenic VOC emission/CAMX")
ax1 = fig.add_subplot(3, 1, (1, 2))#, sharex=True)
ax1 = plt.gca()
ax1.plot(BioEmis_20.index,BioEmis_20["Isop"].values,linewidth="1", color='red', label="E_C5H8_camx", linestyle=" ", marker="x")
ax1.plot(BioEmis_20.index,BioEmis_20["Terp"].values,linewidth="1", color='orange', label="E_TERP_camx", linestyle=" ", marker="x")
ax1.plot(BioEmis_20.index,BioEmis_20["Meth"].values,linewidth="1", color='green', label="E_METH_camx", linestyle=" ", marker="x")
ax1.plot(BioEmis_1819.index,BioEmis_1819["Isop"].values,linewidth="1", color='red',linestyle=" ", marker="x") # label="E_C5H8_camx",
ax1.plot(BioEmis_1819.index,BioEmis_1819["Terp"].values,linewidth="1", color='orange', linestyle=" ", marker="x") #label="E_TERP_camx",
ax1.plot(BioEmis_1819.index,BioEmis_1819["Meth"].values,linewidth="1", color='green', linestyle=" ", marker="x") #label="E_METH_camx",

ax1.plot(BioEmis_1819.index,BioEmis_1819["Par"].values,linewidth="1", color='blue', linestyle=" ", marker="x", label="Par") #label="E_METH_camx",
ax1.plot(BioEmis_1819.index,BioEmis_1819["Xyl"].values,linewidth="1", color='turquoise', linestyle=" ", marker="x", label="Xyl") #label="E_METH_camx",
ax1.plot(BioEmis_1819.index,BioEmis_1819["Ole"].values,linewidth="1", color='yellow', linestyle=" ", marker="x", label="Ole") #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["Nr"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="Nr") #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["Ch4"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="Ch4" #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["Nh3"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="Nh3" #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["NO"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="NO") #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["Alde2"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="Alde2") #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["Etoh"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="Etoh") #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["Form"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="Form") #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["Aldex"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="Aldex") #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["Tol"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="Tol") #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["Iole"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="Iole") #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["Co"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="Co") #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["Ehta"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="Ehta") #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["Eth"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="Eth") #label="E_METH_camx",
#ax1.plot(BioEmis_1819.index,BioEmis_1819["Gday"].values,linewidth="1", color='green', linestyle=" ", marker="x", label="Gday") #label="E_METH_camx",


ax1.set_ylabel("[mol/s]", size="medium")
ax1.grid()
ax1.legend(loc='upper left')
ax3 = fig.add_subplot(3, 1, (3, 3))#, sharex=True)
ax4 = ax3.twinx()
ax3.plot(LAI_df[datetime(2018,1,1):datetime(2020,4,30)].index, LAI_df[datetime(2018,1,1):datetime(2020,4,30)].LAI, linewidth="3",color="green", alpha=0.3, label="LAI")
ax4.plot(BOKUMetData_dailysum["AT"][datetime(2018,1,1):datetime(2020,4,30)].index,BOKUMetData_dailysum["AT"][datetime(2018,1,1):datetime(2020,4,30)].values,linewidth="2",color="red", alpha=0.2, label="T_air DA")
ax3.set_ylabel("LAI[-]")
ax4.set_ylabel("AT[°C]") #average daily temperature
#ax3.set_xlabel("days")
plt.show()

exit()
"""
fig = plt.figure()
#gridspec_kw={'height_ratios': [1, 2]
plt.suptitle("1b biogenic VOC emission/EMEP")
ax1 = fig.add_subplot(3, 1, (1, 2))#, sharex=True)
ax1 = plt.gca()
ax2 = ax1.twinx()
#ax3 = ax2.twinx()
ax1.plot(hcho_w[start:end], linewidth="1", color='black', label="HCHO", linestyle=":")
ax1.plot(emep_hcho_d.index, emep_hcho_d.values, linewidth="1", color='black', label="HCHO_emep", linestyle=":")
ax1.plot(emep_c5h8_d.index, emep_c5h8_d.values, linewidth="1", color='red', label="C5H8_emep", linestyle=":")
ax2.plot(emep_E_c5h8_m.index,emep_E_c5h8_m.values,linewidth="1", color='red', label="E_C5H8_emep", linestyle=" ", marker="o")
ax2.plot(emep_E_terp_m.index,emep_E_terp_m.values,linewidth="1", color='orange', label="E_TERP_emep", linestyle=" ", marker="o")

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
"""
"""
fig = plt.figure()
plt.suptitle("2a deposition/CAMX")
ax1 = fig.add_subplot(3, 1, (1, 2))#, sharex=True)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(DDepO3_1819.index, DDepO3_1819["DD"].values, linewidth="1", color='blue', label="DDEP", linestyle="solid")
ax2.plot(DDepO3_1819.index, DDepO3_1819["DV"].values, linewidth="1", color='turquoise', label="DVEL", linestyle="solid")
ax1.set_xlabel("days")
ax2.set_ylabel("dry deposition velocity [m s-1]", size="medium")
ax1.set_ylabel("O3 dry deposited mass [mol ha-1]", size="medium")
ax1.grid()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3 = fig.add_subplot(3, 1, (3, 3))#, sharex=True)
ax4 = ax3.twinx()
ax3.grid()
ax3.plot(LAI_df[datetime(2018,1,1):datetime(2019,12,31)].index, LAI_df[datetime(2018,1,1):datetime(2019,12,31)].LAI, linewidth="3",color="green", alpha=0.3, label="LAI")
ax4.plot(BOKUMetData_dailysum["AT"][datetime(2018,1,1):datetime(2019,12,31)].index,BOKUMetData_dailysum["AT"][datetime(2018,1,1):datetime(2019,12,31)].values,linewidth="2",color="red", alpha=0.2, label="T_air DA")
ax3.set_ylabel("LAI[-]")
ax4.set_ylabel("AT[°C]") #average daily temperature
plt.show()
"""
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
ax3.set_ylabel("LAI[-]")
ax4.set_ylabel("AT[°C]") #average daily temperature
plt.show()

exit()

start2020 = datetime(2020, 1, 1, 00, 00)
end202009 = datetime(2020, 9, 30, 00, 00)

fig = plt.figure()
plt.suptitle("3 validation")
ax1 = fig.add_subplot(2, 1, (1, 1))#, sharex=True)
ax2 = ax1.twinx()
#ax3 = ax1.twinx()
ax1.plot(hcho_d[start2020:end202009].index,hcho_d[start2020:end202009].values, linewidth="1", color='black', label="HCHO_obs", linestyle=":")
ax2.plot(o3_1990_2020_mda1['AT9JAEG'][start2020:end202009].index, o3_1990_2020_mda1['AT9JAEG'][start2020:end202009].values,linewidth="1", color='violet', label="O3_obs", linestyle=":") #mda1 vs da (mda8)
#ax2.plot(o3_1990_2020_mda8_w['AT9STEF'][start:end],linewidth="1", color='violet', linestyle=":")  #JAEG
#ax1.set_ylim(0, 8)
#ax1.set_xlabel("days")
#ax1.set_xlim(start,end)
ax1.set_ylabel("[ppb]", size="medium")
ax2.set_ylabel("[ug/m2]", size="medium")
ax1.grid()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

ax3 = fig.add_subplot(2, 1, (2, 2))#, sharex=True)
ax4 = ax3.twinx()
#ax3.plot(emep_hcho_d.index, emep_hcho_d.values, linewidth="1", color='black', label="HCHO_mod", linestyle="solid")
ax3.plot(range(len(hcho)), hcho, linewidth="1", color='black', label="HCHO_camx", linestyle="--")
#ax4.plot(emep_o3_d.index, emep_o3_d.values, linewidth="1", color='violet', label="O3_emep", linestyle="solid")
ax3.plot(range(len(o3)), o3, linewidth="1", color='violet', label="O3_camx", linestyle="--")
ax3.set_ylabel("[ppb]", size="medium")
ax4.set_ylabel("[ug/m2]", size="medium")
ax3.legend(loc='upper left')
ax4.legend(loc='upper right')

plt.show()

exit()

fig = plt.figure()
plt.suptitle(f"OBS {start} - {end}")
ax1 = fig.add_subplot(411)
#ax1 = fig.add_subplot(211)
x1 = plt.gca()
ax2 = ax1.twinx()
#ax2.plot(o3_1990_2020_da['AT9STEF'][start:end]*ugm3toppb_o3,linewidth="1", color='violet', label="o3 OBS da", linestyle="solid")
ax2.plot(o3_1990_2020_mda8_w['AT9STEF'][start:end],linewidth="1", color='violet', linestyle="solid") #label="o3 OBS mda8",
#ax2.plot(o3_1990_2020_mda1_w['AT9STEF'][start:end]*ugm3toppb_o3,linewidth="1", color='violet', label="o3 OBS mda1", linestyle=":")
#ax1.plot(BOKUMetData_dailysum["GR"][start:end], linewidth="1", color='orange', label="gr dmax BOKUR OBS")
ax1.plot(BOKUMetData_weekly["GR"][start:end], linewidth="2", color='yellow')#, label="GR sum BOKUR")
#ax2.plot(nox_1990_2020_da['AT9STEF'][start:end],linewidth="1", color='blue', label="nox OBS da", linestyle="solid")
#ax1.set_ylim(0, 8)
ax1.set_xlabel("days")
ax1.set_xlim(start,end)
ax1.set_ylabel("GR[kWh/m²]", size="medium")
ax2.set_ylabel("O3[μg/m³]", size="medium")
ax1.grid()
ax1.axvspan(MAM18_s, MAM18_e, color='orange', alpha=0.2)
ax1.axvspan(MAM20_s, MAM20_e, color='orange', alpha=0.4)
ax1.axvspan(JJA19_s, JJA19_e, color='red', alpha=0.4)
ax1.axvspan(JJA20_s, JJA20_e, color='red', alpha=0.2)
#ax1.legend(loc='upper left')
#ax2.legend(loc='upper right')

ax1 = fig.add_subplot(412)
ax1 = plt.gca()
#ax2 = ax1.twinx()
ax3 = ax1.twinx()
#ax2.plot(tsif, color='violet', label="Tropomi SIF 743nm", marker="x", linestyle=" ")
#ax2.plot(tsif_m,color='violet')
ax1.plot(tsif_w,color='violet', label="TROP")
#ax2.plot(osif_757, color='red', label="OCO2 SIF 757nm", marker="x", linestyle=" ")
#ax2.plot(osif_757_m,color='red')
ax1.plot(osif_757_w,color='red',label="OCO-2")
ax1.set_ylabel("SIF[mW/m2/sr/nm]", size="medium")
#ax2.plot(fAPAR,color='green', label="fAPAR anomaly")
#ax2.set_ylabel("f[-]", size="medium")
#ax1.plot(wrfc2020_lai[start:end],linewidth="0.5", color='blue', label="lai_wrfc", linestyle="dashed")
#ax1.plot(wrflai_megan[start:end], linewidth="0.5", color='blue', label="lai_wrf_megan", linestyle="solid")
#ax1.set_ylim(-5, 35)
ax1.axvspan(MAM18_s, MAM18_e, color='orange', alpha=0.2)
ax1.axvspan(MAM20_s, MAM20_e, color='orange', alpha=0.4)
ax1.axvspan(JJA19_s, JJA19_e, color='red', alpha=0.4)
ax1.axvspan(JJA20_s, JJA20_e, color='red', alpha=0.2)
ax1.set_xlabel("days")
#ax1.set_ylabel("[degree]", size="medium")
#ax1.set_ylim(0, 3500)
#ax2.set_ylabel("[ppb]", size="medium")
#ax1.set_ylabel("LAI [m2 m-2]", size="medium") #TODO convert degree to m2 m-2
#ax2.set_ylabel("dry deposition velocity [cm s-1]", size="medium")
ax1.grid()
ax1.set_xlim(start,end)
#ax1.legend(loc='upper left')
ax1.legend(loc='upper left')
#ax2.legend(loc='upper right')

ax1 = fig.add_subplot(413)
ax1 = plt.gca()
ax2 = ax1.twinx()
#ax1.plot(sm['VWC1 min[%]'][start:end],linewidth="1", color='black', label="sm_rutz1 min 0-30 cm OBS ", linestyle="solid")
#ax1.plot(sm['VWC2 min[%]'][start:end],linewidth="1", color='darkgrey', label="sm_rutz2 min 0-30 cm  OBS ", linestyle="solid")
#ax1.plot(sm['VWC3 min[%]'][start:end],linewidth="1", color='lightgrey', label="sm_rutz3 min 0-30 cm OBS ", linestyle="solid")
#ax1.plot(sm['VWC1 max[%]'][start:end],linewidth="0.5", color='black', label="sm_rutz1 max 0-30 cm OBS ", linestyle="solid")
#ax1.plot(sm['VWC2 max[%]'][start:end],linewidth="0.5", color='darkgrey', label="sm_rutz2 max 0-30 cm OBS ", linestyle="solid")
#ax1.plot(sm['VWC3 max[%]'][start:end],linewidth="0.5", color='lightgrey', label="sm_rutz3 max 0-30 cm OBS ", linestyle="solid")
#ax1.plot(rss['RSS_top_wWheat'][start:end],linewidth="1", color='darkred', label="rss rutz2 0-40 cm ARIS", linestyle="solid")
#ax1.plot(vwc['RSS_top_wWheat'][start:end],linewidth="1", color='red', label="sm rutz2 0-40 cm ARIS wWheat", linestyle="solid")
ax1.plot(vwc['RSS_sub_wWheat'][start:end],linewidth="1", color='orange', label="wWheat", linestyle="solid") #label="rss 40-100 cm ARIS wWheat"
ax1.plot(vwc['RSS_sub_grass'][start:end],linewidth="1", color='green', label="grass", linestyle="solid")  #label="rss 40-100 cm ARIS grass"
#ax1.plot(vwc['RSS_top_maize'][start:end],linewidth="1", color='orange', label="sm rutz2 0-40 cm ARIS maize", linestyle="solid")
#ax1.plot(vwc['RSS_top_sBarley'][start:end],linewidth="1", color='brown', label="sm rutz2 0-40 cm ARIS sBarley", linestyle="solid")
#ax1.plot(vwc['RSS_top_sugBeet'][start:end],linewidth="1", color='purple', label="sm rutz2 0-40 cm ARIS sugBeet", linestyle="solid")
#ax1.plot(vwc_grass['RSS_top_grass'][start:end],linewidth="1", color='green', label="sm rutz2 0-40 cm ARIS grass", linestyle="solid")
ax2.plot((BOKUMetData_dailysum["PC"]*0.1)[start:end], linewidth="1", color='blue')#, label="prec BOKUR OBS")
ax2.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
ax1.set_xlabel("days")
ax2.set_ylabel("PC[mm]", size="medium")
ax1.set_ylabel("RSS[-]", size="medium")
ax1.set_xlim(start,end)
#ax1.legend(loc='upper left',fontsize="small")
#ax2.legend(loc='upper right',fontsize="small")
ax1.grid()
ax1.axvspan(MAM18_s, MAM18_e, color='orange', alpha=0.2)
ax1.axvspan(MAM20_s, MAM20_e, color='orange', alpha=0.4)
ax1.axvspan(JJA19_s, JJA19_e, color='red', alpha=0.4)
ax1.axvspan(JJA20_s, JJA20_e, color='red', alpha=0.2)

ax1 = fig.add_subplot(414)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.axhline(0, color='grey',linestyle="dashed",linewidth="0.3")
#ax2.plot(BOKUMetData_dailymax["AT"][start:end], linewidth="1", color='lightsalmon', label="t2dmax BOKUR OBS")
ax2.plot(vpd_dmax_w[start:end], linewidth="1", color='green')#, label="vpd dmax")
#ax2.plot(BOKUMetData_weekly["AT"][start:end], linewidth="1", color='lightsalmon', label="t2dmax BOKUR OBS")
#ax1.plot(hcho_d[start:end], linewidth="1", color='black', label="hcho D OBS d", linestyle="solid") #274 = Julian Day 30.Sept2020
ax1.plot(hcho_w[start:end], linewidth="1", color='black', linestyle="solid") #274 = Julian Day 30.Sept2020 #label="hcho D OBS d",
#ax1.plot(hcho_dmax[start:end], linewidth="1", color='black', label="hcho OBS dmax", linestyle="solid") #274 = Julian Day 30.Sept2020
#ax1.plot(hcho_m[start:end], linewidth="0.5", color='black', label="hcho D OBS mmax", linestyle="-") #274 = Julian Day 30.Sept2020
#ax1.plot(hcho_m_A[start:end], linewidth="0.5", color='grey', label="hcho A OBS mmax", linestyle="-") #274 = Julian Day 30.Sept2020
#ax1.plot(hcho_m_K[start:end], linewidth="0.5", color='darkgrey', label="hcho K OBS mmax", linestyle="-") #274 = Julian Day 30.Sept2020
#ax1.plot(BOKUMetData_monthly["AT"][start:end], linewidth="1", color='lightsalmon', label="t2_obs_BOKUR_m")
#ax2.plot(BOKUMetData_monthly["GR"][start:end], linewidth="1", color='orange', label="gr_obs_BOKUR_m")
#ax1.plot(tas_m[start:end]-273.15,linewidth="1", color='darkred', label="t2_wrfc_m", linestyle="dashed")
#ax1.set_ylim(-5, 35)
ax1.set_xlim(start,end)
ax1.set_xlabel("days")
ax2.set_ylabel("VDP[kPa]", size="medium")
ax1.set_ylabel("HCHO[ppb]", size="medium")
#ax1.legend(loc='upper left')
#ax2.legend(loc='upper right')
ax1.grid()
ax1.axvspan(MAM18_s, MAM18_e, color='orange', alpha=0.2)
ax1.axvspan(MAM20_s, MAM20_e, color='orange', alpha=0.4)
ax1.axvspan(JJA19_s, JJA19_e, color='red', alpha=0.4)
ax1.axvspan(JJA20_s, JJA20_e, color='red', alpha=0.2)
plt.show()

