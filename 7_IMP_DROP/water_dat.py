# -*- coding: utf-8 -*-
__author__ = 'lnx'

import numpy as np
import pandas as pd
from datetime import datetime
import monthdelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.stats import linregress
import BOKUMet_Data
from Datetime_recipies import datestdtojd
#from conversions import *

Present1_start = '2004-7-15'
Present2_end = '2004-7-26'
Messperiode_start = '2022-8-10'
Messperiode_end = '2022-8-20'
RCP85_start = '2021-6-9'
RCP85_end = '2021-6-20'
RCP26_start = '2018-8-6'
RCP26_end = '2018-8-17'

'''READ in DRINKING WATER FED [m³]'''
file_MA31_04 = "/Users/lnx/DATA/obs_point/land/MA31_WienerWasser/Systemeinspeisung_Wien_2004.txt"
dwf_2004 = pd.read_csv(file_MA31_04, skiprows=2, sep='\t', names=["date","2004"])#, converters={'A': pd.to_datetime})
#print(dwf_2004)
dwf_2004 = dwf_2004.set_index(pd.to_datetime(dwf_2004['date'], dayfirst=True)) 
dwf_2004 = dwf_2004.drop(columns=['date']) 
dwf_2004_wd = dwf_2004.loc[dwf_2004.index.weekday <= 4] #Mo-Fr
dwf_2004_we = dwf_2004.loc[dwf_2004.index.weekday >= 5] #Sa,So
dwf_2004_we_w = dwf_2004_we.resample("W").sum()
#print(dwf_2004_we_w)
dwf_2004_wd_w = dwf_2004_wd.resample("W").sum()
dwf_2004_we_m = dwf_2004_we.resample("M").sum()
dwf_2004_wd_m = dwf_2004_we.resample("M").sum()
#dwf_2004.plot()

file_MA31_18 = "/Users/lnx/DATA/obs_point/land/MA31_WienerWasser/Systemeinspeisung_Wien_2018.txt"
dwf_2018 = pd.read_csv(file_MA31_18, skiprows=2, sep='\t', names=["date","2018"])
dwf_2018 = dwf_2018.set_index(pd.to_datetime(dwf_2018['date'], dayfirst=True)) 
dwf_2018 = dwf_2018.drop(columns=['date']) 

file_MA31_21 = "/Users/lnx/DATA/obs_point/land/MA31_WienerWasser/Systemeinspeisung_Wien_2021.txt"
dwf_2021 = pd.read_csv(file_MA31_21, skiprows=2, sep='\t', names=["date","2021"])
dwf_2021 = dwf_2021.set_index(pd.to_datetime(dwf_2021['date'], dayfirst=True)) 
dwf_2021 = dwf_2021.drop(columns=['date']) 

file_MA31_22 = "/Users/lnx/DATA/obs_point/land/MA31_WienerWasser/Systemeinspeisung_Wien_2022.txt"
dwf_2022 = pd.read_csv(file_MA31_22, skiprows=2, sep='\t', names=["date","2022"])
dwf_2022 = dwf_2022.set_index(pd.to_datetime(dwf_2022['date'], dayfirst=True)) 
dwf_2022 = dwf_2022.drop(columns=['date']) 

'''READ in MA42 sum[m³]'''
ma42_2006 = 722000 
ma42_2009 = 788000
ma42_2012 = 790000 
ma42_2015 = 707000 
ma42_2018 = 711000
ma42_2021 = 1012000 
ma42_2022 = 1129000 

'''READ in EBS'''
#hourly data 1h = Q from 1-2h!
#6.-17.8.2018 
file_ebs_hw2018 = "/Users/lnx/DATA/obs_point/land/EBS_Klaeranlage_Wandel/ebs_hw2018.txt"
ebs_hw2018 = pd.read_csv(file_ebs_hw2018, skiprows=1, sep='\t', names=["datetime","hw2018"]) #, converters={'A': pd.to_datetime})
ebs_hw2018 = ebs_hw2018.set_index(pd.to_datetime(ebs_hw2018['datetime'], dayfirst=True)) #format ='%d.%m.%Y' 
ebs_hw2018 = ebs_hw2018.drop(columns=['datetime']) 
ebs_hw2018_d = ebs_hw2018.resample("D").sum()  
#print(ebs_hw2018.index)

#9.-20.6.2021
file_ebs_hw2021 = "/Users/lnx/DATA/obs_point/land/EBS_Klaeranlage_Wandel/ebs_hw2021.txt"
ebs_hw2021 = pd.read_csv(file_ebs_hw2021, skiprows=1, sep='\t', names=["datetime","hw2021"])
ebs_hw2021 = ebs_hw2021.set_index(pd.to_datetime(ebs_hw2021['datetime'], dayfirst=True)) 
ebs_hw2021 = ebs_hw2021.drop(columns=['datetime'])  
ebs_hw2021_d = ebs_hw2021.resample("D").sum()  

#10.-20.8.2022
file_ebs_hw2022 = "/Users/lnx/DATA/obs_point/land/EBS_Klaeranlage_Wandel/ebs_hw2022.txt"
ebs_hw2022 = pd.read_csv(file_ebs_hw2022, skiprows=1, sep='\t', names=["datetime","hw2022"])
ebs_hw2022 = ebs_hw2022.set_index(pd.to_datetime(ebs_hw2022['datetime'], dayfirst=True)) 
ebs_hw2022 = ebs_hw2022.drop(columns=['datetime']) 
ebs_hw2022_d = ebs_hw2022.resample("D").sum()  

#ebs_2022_full
file_ebs_2022full = "/Users/lnx/DATA/obs_point/land/EBS_Klaeranlage_Wandel/ebs_2022full.txt"
ebs_2022 = pd.read_csv(file_ebs_2022full, skiprows=1, sep='\t', names=["datetime","2022"])
ebs_2022 = ebs_2022.set_index(pd.to_datetime(ebs_2022['datetime'], dayfirst=True)) 
ebs_2022 = ebs_2022.drop(columns=['datetime']) 
ebs_2022_d = ebs_2022.resample("D").sum()  

'''READ IN BOKU Metdata'''
# DT = 'dewpoint temperature (degree C)'
# AT = 'air temperature (degree C)'
# RH = 'relative humidity (%)'
# GR = 'global radiation (W m^(-2))'
# WS = 'wind speed (km/h)'
# WD = 'wind direction (degree)'
# WS = 'wind speed - gust (km/h)'
# PS = 'precipitation (10^(-1) mm)'
# AP = 'air pressure (hPa)'
BOKUMetData = BOKUMet_Data.BOKUMet()
#print(BOKUMetData) #10min values
#DAILY MEANS
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})
BOKUMetData_dailysum = BOKUMetData_hourlymean.resample('D').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.sum, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})

#print(BOKUMetData_dailysum['PC'])
#timeslice
BOKUMetData_dailysum18 = BOKUMetData_dailysum['2018-1-1':'2018-12-31']
BOKUMetData_dailysum21 = BOKUMetData_dailysum['2021-1-1':'2021-12-31']
BOKUMetData_dailysum22 = BOKUMetData_dailysum['2022-1-1':'2022-12-31']

'''READ in GEOSPHERE SYNOP'''
file_path = '/Users/lnx/DATA/obs_point/met/ZAMG/DataHub/ViennaStations_SYNOP Datensatz_20170101T0000_20221231T2300.csv'

# Define custom date parsing function
dateparse = lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M+00:00')

# Read CSV into DataFrame
df = pd.read_csv(file_path, 
                 parse_dates=['time'],            # Parse 'time' column as datetime
                 date_parser=dateparse,           # Use custom date parsing function
                 na_values=[''],                  # Treat empty strings as NaN
                 index_col=None)                  # Don't use any column as index

# Display the DataFrame
print(df["time"])

df = df.set_index(pd.to_datetime(df['time']))
df = df.drop(columns=['time']) 
print(df)

# Filter rows where 'station' column is '11035' and extract 'RRR' column
#RRR,Niederschlagsmenge im Beobachtungszeitraum tr,"Niederschlagsmenge im Beobachtungszeitraum tr (0 = Spuren von Nied., -1 = kein Nied.)",mm
rrr_for_station_11035 = df[df['station'] == 11035]['RRR']

# Display the extracted RRR values for station 11035

pd.set_option('display.max_rows', None)

print(rrr_for_station_11035[Messperiode_start:Messperiode_end]) #max=1.0  (0.2, 0.2, 1,1) -> 2.4mm
print(rrr_for_station_11035[RCP26_start:RCP26_end]) #max=2.0 (0.3, 1, 2, 0.2, 0.3)  #2018  -> 3.8 mm
print(rrr_for_station_11035[RCP85_start:RCP85_end]) #max=2.0 (0.4, 2, 0.8, 0.8, ) #2021  -> 4 mm 
pd.reset_option('display.max_rows')

"""
fig, (ax1,ax2,ax3) = plt.subplots(3,1)
ax1.set(title="precipitation [mm]")
#ax1.plot(dwf_2004, color="grey", label = "all")  
ax1.plot(rrr_for_station_11035['2018-1-1':'2018-12-31', color="red", label = 2018")
ax1.plot(dwf_2004_we_m, color="blue", label = "weekend")
ax2.plot(dwf_2018)#linestyle=" ", marker="."
ax3.plot(dwf_2021)
plt.show()
"""

exit()
'''READ IN MA45 Q'''

file_qkennedy_wien_full = "/Users/lnx/DATA/obs_point/land/MA45_WienerGewaesser/QKennedybruecke.dat"
file_qmauerbach_full = "/Users/lnx/DATA/obs_point/land/MA45_WienerGewaesser/QMauerbachstrasse.dat"
file_qoberlaa_liesingb_full = "/Users/lnx/DATA/obs_point/land/MA45_WienerGewaesser/QOberlaa.dat"

qken = pd.read_csv(file_qkennedy_wien_full, skiprows=27, sep='\s+', names=["date","hour","qken"], encoding='latin-1')

#data['Datetime'] = pd.to_datetime(data['Date']+ ' ' + data['Time'], format='%d.%m.%Y %H:%M:%S')


qken['datetime'] = qken['date']+ ' ' + qken['hour']
#print(qken['datetime'])
qken = qken.set_index(pd.to_datetime(qken['datetime'], format='%d.%m.%Y %H:%M:%S')) #, dayfirst=True) 
qken = qken.drop(columns=['date', 'hour', 'datetime']) 
"""
#print(qken)
#print(qken['qken'].mean())
#exit()
print("Q Wienerwald Creeks")
qken_pres = qken[Present1_start:Present2_end]
qken_pres_sum = qken.mean()
qken_meas = qken[Messperiode_start:Messperiode_end]
qken_meas_sum = qken_meas.sum()
qken_rcp85 = qken[RCP85_start:RCP85_end]
qken_rcp85_sum = qken_rcp85.sum()
qken_rcp26 = qken[RCP26_start:RCP26_end]
qken_rcp26_sum = qken_rcp26.sum()

#print("\n Present1=", qken_pres_sum)
#print("\n Messperiode=", qken_meas_sum)
#print("\n RCP26=", qken_rcp26_sum)
#print("\n RCP85=", qken_rcp85_sum)

exit()
"""
print("Precipitation at BOKU-Met \n")
x_pres = BOKUMetData_dailysum[Present1_start:Present2_end]['PC']*0.1
x_pres_sum = x_pres.sum()
x_meas = BOKUMetData_dailysum[Messperiode_start:Messperiode_end]['PC']*0.1
x_meas_sum = x_meas.sum()
x_rcp85 = BOKUMetData_dailysum[RCP85_start:RCP85_end]['PC']*0.1
x_rcp85_sum = x_rcp85.sum()
x_rcp26 = BOKUMetData_dailysum[RCP26_start:RCP26_end]['PC']*0.1
x_rcp26_sum = x_rcp26.sum()

print("\n Present1=", x_pres_sum)
print("\n Messperiode=", x_meas_sum)
print("\n RCP26=", x_rcp26_sum)
print("\n RCP85=", x_rcp85_sum)

print("\n\n Discharge, main sewage")
print("\n Messperiode=", ebs_hw2022.sum())
print("\n RCP26=", ebs_hw2018.sum())
print("\n RCP85=", ebs_hw2021.sum())

exit()

"""
fig, (ax1,ax2,ax3) = plt.subplots(3,1)
ax1.set(title="sewage water leaving the system [m3]")
ax1.plot(ebs_hw2018)#, linestyle=" ", marker="."
ax2.plot(ebs_hw2021)
ax3.plot(ebs_hw2022)
ax3.set(xlabel="time [h]",ylabel="[m3]")
ax1.set_ylim([8000,30000])
ax2.set_ylim([8000,30000])
ax3.set_ylim([8000,30000])
plt.show()

fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1)
ax1.set(title="drinking water fed into system [m3]")
#ax1.plot(dwf_2004, color="grey", label = "all")  
ax1.plot(dwf_2004_wd_m, color="red", label = "weekdays")
ax1.plot(dwf_2004_we_m, color="blue", label = "weekend")
ax2.plot(dwf_2018)#linestyle=" ", marker="."
ax3.plot(dwf_2021)
ax4.plot(dwf_2022)
ax4.set(xlabel="time [d]",ylabel="[m3]")
#ax1.set_ylim([280000,550000])
ax2.set_ylim([280000,550000])
ax3.set_ylim([280000,550000])
ax4.set_ylim([280000,550000])
plt.show()
"""

x18 = BOKUMetData_dailysum18['PC']*0.1
x21 = BOKUMetData_dailysum21['PC']*0.1
x22 = BOKUMetData_dailysum22['PC']*0.1

#print(len(dwf_2022), len(BOKUMetData_dailysum22['PC']))

fs = 10  #fontsize
fig, axs = plt.subplots(nrows=1,ncols=3,sharey='row', sharex='col')#, figsize=(6, 6))

axes = plt.gca()
m1, b1 = np.polyfit(x18['2018-6-1':'2018-8-31'], dwf_2018['2018-6-1':'2018-8-31'], 1)
m2, b2 = np.polyfit(x21['2021-6-1':'2021-8-31'], dwf_2021['2021-6-1':'2021-8-31'], 1)
m3, b3 = np.polyfit(x22['2022-6-1':'2022-8-31'], dwf_2022['2022-6-1':'2022-8-31'], 1)
s1 = "2018:", m1, "*x + ", b1
s2 = "2021:", m2, "*x + ", b2
s3 = "2022:", m3, "*x + ", b3

X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
#plt.text(1,1,s1)

r1 = linregress(x18['2018-6-1':'2018-8-31'],dwf_2018["2018"]['2018-6-1':'2018-8-31'])[2] #r-value  coefficient of correlation
r2 = linregress(x21['2021-6-1':'2021-8-31'],dwf_2021["2021"]['2021-6-1':'2021-8-31'])[2] #r-value  coefficient of correlation
r3 = linregress(x22['2022-6-1':'2022-8-31'],dwf_2022["2022"]['2022-6-1':'2022-8-31'])[2] #r-value  coefficient of correlation
print(type(r1),r2,r3)

axs[0].set_title(f'2018, R= {r1:.2f}')
axs[1].set_title(f'2021, R= {r2:.2f}')
axs[2].set_title(f'2022, R= {r3:.2f}')
axs[0].scatter(x18['2018-6-1':'2018-8-31'], dwf_2018['2018-6-1':'2018-8-31']) #, label="2018") 
axs[1].scatter(x21['2021-6-1':'2021-8-31'], dwf_2021['2021-6-1':'2021-8-31']) 
axs[2].scatter(x22['2022-6-1':'2022-8-31'], dwf_2022['2022-6-1':'2022-8-31']) 
#axs[0].plot(X_plot, m1*X_plot + b1, '-')
#axs[1].plot(X_plot, m2*X_plot + b2, '-')
#axs[2].plot(X_plot, m3*X_plot + b3, '-')
axs[0].set_ylabel("daily drinking water fed into system [m³]")
axs[0].set_xlabel("daily precipitation [mm]")
axs[1].set_xlabel("daily precipitation [mm]")
axs[2].set_xlabel("daily precipitation [mm]")
#axs[0].legend(loc="upper right") #axs[1, 0].set_title('NE')
#axs[1].legend(loc="upper right") #axs[1, 0].set_title('NE')
#axs[2].legend(loc="upper right") #axs[1, 0].set_title('NE')

for ax in fig.get_axes():
    print(ax)
    ax.set_xlim(0,85)
    ax.set_ylim(300000,600000)
#plt.colorbar(pl1, ax=axs[:, 1], shrink=0.6, label="WD [°]")

for i, ax in enumerate(axs):
    x_values = BOKUMetData_dailysum_values[i]['PC'] * 0.1  # Replace with your actual data
    dwf_values = dwf_values_list[i]  # Replace with your actual data

    m, b = np.polyfit(x_values['2018-6-1':'2018-8-31'], dwf_values['2018-6-1':'2018-8-31'], 1)
    regression_line = m * X_plot + b

    ax.plot(X_plot, regression_line, '-')

# Other code...


plt.show()

"""
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
"""





