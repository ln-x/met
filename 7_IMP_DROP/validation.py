# -*- coding: utf-8 -*-
__author__ = 'lnx'

import netCDF4 as nc
from netCDF4 import Dataset, num2date
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import BOKUMet_Data


labels_dictionary = {
    'label1': 'ARIS_30p_Irrigation',
    'label2': 'ARIS',
    'label3': 'Raw'
}

par_dic = {'glw':['W/m2','DOWNWARD LONG WAVE FLUX AT GROUND SURFACE'], 'prt':['mm', 'total precipitation amount'], 'psfc':['Pa','Surface pressure'], 'q2m':['kg kg-1', 'mixing ratio'], 'rh2m':['%','Relative Humidity',''], 'slp':['pa','Sea level pressure'], 'swdown':['W m-2','DOWNWARD SHORT WAVE FLUX AT GROUND SURFACE'], 't2m':['K', '2m temperature'], 'wdir10':['m s-1', 'grid relative wind direc at mass points'], 'wspd10':['"m s-1','grid relative wind speed at mass points']}
#print(par_dic['prt'][1])

#223 time points
Messperiode_start = '2022-8-10 18:00:00'
Messperiode_end = '2022-8-20 00:00:00 '

ZAMGnames = {'11034': ['Wien-Innere Stadt',85,53], '11035':  ["Wien-Hohe Warte",83,69],
             '11036': ['Schwechat',129,25], '11037':['Gross-Enzersdorf',127,54],
             '11040': ['Wien-Unterlaa',97,29], '11042':['Wien-Stammersdorf',94,88],
             '11077': ['Brunn am Gebirge',65,24], '11080':['Wien-Mariabrunn',56,56]}
  
station_sel = '11080'

x = ZAMGnames[station_sel][1]
y = ZAMGnames[station_sel][2]

print(x, y)

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
BOKUMetData_hourlymean = BOKUMetData.resample('H').agg({'DT': np.mean, 'AT': np.mean, 'RH': np.mean, 'GR': np.mean, 'WS': np.mean,
                                                     'WD': np.mean, 'WSG': np.mean, 'PC': np.sum, 'AP': np.mean})


#TODO read in datetime

'''READ in GEOSPHERE SYNOP'''
#file_path = '/Users/lnx/DATA/obs_point/met/ZAMG/DataHub/ViennaStations_SYNOP Datensatz_20170101T0000_20221231T2300.csv'
file_path = '/Users/lnx/DATA/obs_point/met/ZAMG/DataHub/SYNOP Datensatz_20180101T0000_20231231T2300.csv'

# Define custom date parsing function
dateparse = lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M+00:00')

# Read CSV into DataFrame
df = pd.read_csv(file_path, 
                 parse_dates=['time'],            # Parse 'time' column as datetime
                 date_parser=dateparse,           # Use custom date parsing function
                 na_values=[''],                  # Treat empty strings as NaN
                 index_col=None)                  # Don't use any column as index

# Display the DataFrame
#print(df["time"])
df = df.set_index(pd.to_datetime(df['time']))
df = df.drop(columns=['time']) 
#print(df, df['station']==station_sel)

# Filter rows where 'station' column is '11035' and extract 'T' column
t2m_for_station = df[df['station']==11080]['T']   #Temperature
wdir_for_station = df[df['station']==station_sel]['dd'] #Windrichtung, Windrichtung  in Grad , 990=umlaufender Wind (Code Table 0877)",°
wsp_for_station = df[df['station']==station_sel]['ff']  #Windgeschwindigkeit,"Windgeschwindigkeit in 1/10 m/s (wird umgerechnet, wenn Knoten: *5.14)",m/s
                                                          #w1ffmax,Höchste mittlere Windgeschwindigkeit (W1W2),Höchste mittlere Windgeschwindigkeit (10 Minuten-Mittel) im Zeitraum von W1W2 (siehe Gruppe 7wwW1W2),m/s
prt_for_station = df[df['station']==11080]['RRR'] #RRR,Niederschlagsmenge im Beobachtungszeitraum tr,"Niederschlagsmenge im Beobachtungszeitraum tr (0 = Spuren von Nied., -1 = kein Nied.)",mm
                                                          #tr,Beobachtungszeitraum für Niederschlagsmenge,"Beobachtungszeitraum für Niederschlagsmenge RRR (Code Table 4019), Code 1=6std, 2=12std, 3=18std, 4=24std, 5=1std, 6=2std, 7=3std, 8=9std, 9=15std",Code (Synop)
prt_for_station = prt_for_station.replace(-1.0, 0)

rh_for_station = df[df['station']==11080]['rel']  #Relative Feuchte,"Relative Luftfeuchte (bis 2001/06/19 = 254, nicht gemeldet)",%

#print(prt_for_station.index)


# Display the extracted values for station 11035
#pd.set_option('display.max_rows', None)
#print(t_for_station_11035[Messperiode_start:Messperiode_end]) #max=1.0  (0.2, 0.2, 1,1) -> 2.4mm
#pd.reset_option('display.max_rows')

'''READ IN IMRANS WRFTEB Metdata'''

# Open a NetCDF file to read
path_ARIS = '/Users/lnx/DATA/models/BOKU/WRFTEB/IMP_DROP/OBS/ARIS/D03/' 
path_ARISirr = '/Users/lnx/DATA/models/BOKU/WRFTEB/IMP_DROP/OBS/ARISirr/D03/' 
path_RAW = '/Users/lnx/DATA/models/BOKU/WRFTEB/IMP_DROP/OBS/RAW/D03/' 

file_t2m_ARISirr = path_ARISirr +'D03_t2m_2022-08-10_'+labels_dictionary['label1']+'.nc'  
file_t2m_ARISstq = path_ARIS +'D03_t2m_2022-08-10_'+labels_dictionary['label2']+'.nc'
file_t2m_ARISno = path_RAW +'D03_t2m_2022-08-10_'+labels_dictionary['label3']+'.nc'  
file_rh_ARISirr = path_ARISirr +'D03_rh2m_2022-08-10_'+labels_dictionary['label1']+'.nc'  
file_prt_ARISirr = path_ARISirr +'D03_prt_2022-08-10_'+labels_dictionary['label1']+'.nc'  

# Open the NetCDF file
ds_ARISirr = nc.Dataset(file_t2m_ARISirr, 'r')  # 'r' is for read mode
ds_ARISstq = nc.Dataset(file_t2m_ARISstq, 'r') 
ds_ARISno = nc.Dataset(file_t2m_ARISno, 'r')  
ds_rh_ARISirr = nc.Dataset(file_rh_ARISirr, 'r')  
ds_prt_ARISirr = nc.Dataset(file_prt_ARISirr, 'r')  

# Read the time variable (assuming it's named 'time')
time_var = ds_ARISirr.variables['time']
# Read the time units (e.g., "days since 1900-01-01")
time_units = time_var.units
# Convert numeric time values to datetime objects
datetimes = nc.num2date(time_var[:], units=time_units)

"""TODO 
var = ds_ARISirr.variables['t2m']
#print(f"Variable '{variable_name}' info: {var}")
#print(f"Variable '{variable_name}' data: {var[:]}")
data = np.array(var[:, y, x])
data_variable = data.values[:]

# Create a DataFrame using the datetimes as the index
df = pd.DataFrame(data_variable, index=datetimes, columns=['Data'])

# Convert the index to a pandas DatetimeIndex (if it's not already)
df.index = pd.to_datetime(df.index)

print(df)

#ds_ARISirr = ds_ARISirr.set_index(pd.to_datetime(datetimes, dayfirst=True)) 
#ds_ARISirr = ds_ARISirr.drop(columns=['date'])

exit()
# Print out information about the file
#print(f"Dimensions: {ds.dimensions.keys()}")
#print(f"Variables: {ds.variables.keys()}")
"""
variable_name = 't2m'
if variable_name in ds_ARISirr.variables:
    var = ds_ARISirr.variables[variable_name]
    #print(f"Variable '{variable_name}' info: {var}")
    #print(f"Variable '{variable_name}' data: {var[:]}")
    data = np.array(var[:, y, x])    
    #print(ds_ARISirr.variables['time'])
    #exit()
    var2 = ds_ARISstq.variables[variable_name]
    var3 = ds_ARISno.variables[variable_name]
    data2 = np.array(var2[:, y, x])   
    data3 = np.array(var3[:, y, x])    

variable_name = 'rh2m'
if variable_name in ds_rh_ARISirr.variables:
    var = ds_rh_ARISirr.variables[variable_name]
    data_rh = np.array(var[:, y, x])    
 
variable_name = 'prt'
if variable_name in ds_prt_ARISirr.variables:
    var = ds_prt_ARISirr.variables[variable_name]
    data_prt = np.array(var[:, y, x])   
    
    #print(len(t_for_station_11035[Messperiode_start:Messperiode_end]))
    #print(t_for_station_11035[Messperiode_start:Messperiode_end]) 223
    
    print(rh_for_station.values, data_rh)

    # Plotting
    #plt.figure(figsize=(10, 6))
    fig, (ax1,ax2,ax3) = plt.subplots(3,1)
    ax1.set_title(ZAMGnames[station_sel][0])  #f"Time Series of {variable_name}, 
    #plt.plot(times, data, label=variable_name)
    #ax1.plot(ds.variables[variable_name][:])#, linestyle=" ", marker="."
    ax1.plot(t2m_for_station[Messperiode_start:Messperiode_end], label="T (GeoS)")
    ax1.plot(t2m_for_station[Messperiode_start:Messperiode_end].index, data-273.15, label="T WRFTEB_ARIS_30p_irr")
    ax1.plot(t2m_for_station[Messperiode_start:Messperiode_end].index, data2-273.15, label="T WRFTEB_ARIS_stq")
    ax1.plot(t2m_for_station[Messperiode_start:Messperiode_end].index, data3-273.15, label="T WRFTEB_ARIS_ARIS_no")
    ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

    ax1.legend(loc="upper left")
    ax1.set(ylabel="[°C]")
    ax2.plot(BOKUMetData_hourlymean[Messperiode_start:Messperiode_end]['RH'], label="RH (BOKU)")
    ax2.plot(t2m_for_station[Messperiode_start:Messperiode_end].index, data_rh, label="RH WRFTEB_ARIS_30p_irr")
    #ax2.plot(rh_for_station[Messperiode_start:Messperiode_end].values, label="RH ")
    ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax2.set(ylabel="[%]")
    ax2.legend(loc="upper left")
    ax3.plot(prt_for_station[Messperiode_start:Messperiode_end], label="PRT (GeoS)")
    ax3.plot(t2m_for_station[Messperiode_start:Messperiode_end].index, data_prt, label="PRT WRFTEB_ARIS_30p_irr")
    ax3.set(xlabel="time [h]",ylabel="[mm]")
    ax3.legend(loc="upper left")
    ax3.grid(True, which='both', linestyle='--', linewidth=0.5)

    #ax1.set_ylim([8000,30000])
    #ax2.set_ylim([8000,30000]) 
    #ax3.set_ylim([8000,30000])
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    #plt.imshow(data, cmap='viridis')  # Choose a colormap that fits your data
    #plt.colorbar(label=variable_name)
    #plt.xlabel('X dimension')
    #plt.ylabel('Y dimension')
    plt.show()
else:
    print(f"Variable '{variable_name}' not found in the file.")

# Close the dataset
ds_ARISirr.close()

plt.show()


exit()

#ViennaStations_STD Datensatz
#GSW, GSW_qflag    Globalstrahlung - Mittelwert aus 10 Minuten-Werten der kalibrierten Globalstrahlung, SUMME((hh-1):10 - hh:00)/6   W/m2
#D6X Windrichtung in ° - vektorielles Mittel aus 10 Minuten-Werten über die Stunde ((hh-1):10 - hh:00), °
#RSX Niederschlag - 60 Minuten-Summe ((hh-1):00:01 - hh:00:00) der 1 Minuten-Werte des Niederschlags mm
#TTX Lufttemperatur 2 meter -  letzter 10 Minutenwert der vollen Stunde (01:00, 02:00,…)  °C
#VKM Windgeschwindigkeit km/h

#retrieve: FFX Relative Luftfeuchte - letzter 10 Minutenwert der vollen Stunde (01:00, 02:00,…) %