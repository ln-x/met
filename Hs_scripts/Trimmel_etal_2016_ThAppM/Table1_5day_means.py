__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Episode selection criteria: 5day air temperature means of the 14day episodes
#plus other climatic input during this 5days

C_2013 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/inputfiles/Climate_04inca.csv', index_col=['DateTime'], sep=',', parse_dates=['DateTime'])
C_2013_max5days = C_2013['2013-08-04 00:00:00':'2013-08-08 23:50:00']
C_2013_max5days_glorad_sum = C_2013_max5days['GloRad (W/m2)'].resample('D', how='sum')/1000
C_2013_max5days_mean = C_2013_max5days.mean()
C_2013_max5days_glorad_sum_mean = C_2013_max5days_glorad_sum.mean()
print '2013 max: \n', C_2013_max5days_mean, '\nGloRadSum[MJ/d] \t\t\t', C_2013_max5days_glorad_sum_mean

C_1a_2030_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/1jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_1a_2030 = C_1a_2030_0.set_index('datetime')
C_1a_2030_max5days = C_1a_2030.ix[240:]  #last five days
C_1a_2030_max5days['Rad'] = C_1a_2030_max5days['Rad'].resample('D', how='sum')/1000
C_1a_2030_max5days_mean = C_1a_2030_max5days.mean()
print '2030 1a: \n', C_1a_2030_max5days_mean

C_5a_2030_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/5jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_5a_2030 = C_5a_2030_0.set_index('datetime')
C_5a_2030_max5days = C_5a_2030.ix[240:]
C_5a_2030_max5days['Rad'] = C_5a_2030_max5days['Rad'].resample('D', how='sum')/1000
C_5a_2030_max5days_mean = C_5a_2030_max5days.mean()
print '2030 5a: \n', C_5a_2030_max5days_mean

C_20a_2030_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/20jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_20a_2030 = C_20a_2030_0.set_index('datetime')
C_20a_2030_max5days = C_20a_2030.ix[240:]
C_20a_2030_max5days['Rad'] = C_20a_2030_max5days['Rad'].resample('D', how='sum')/1000
C_20a_2030_max5days_mean = C_20a_2030_max5days.mean()
print '2030 20a: \n', C_20a_2030_max5days_mean

C_max_2030_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/Max/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_max_2030 = C_max_2030_0.set_index('datetime')
C_max_2030_max5days = C_max_2030.ix[240:]
C_max_2030_max5days['Rad'] = C_max_2030_max5days['Rad'].resample('D', how='sum')/1000
C_max_2030_max5days_mean = C_max_2030_max5days.mean()
print '2030 Max: \n', C_max_2030_max5days_mean

C_1a_2050_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/1jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_1a_2050 = C_1a_2050_0.set_index('datetime')
C_1a_2050_max5days = C_1a_2050.ix[240:]  #last five days
C_1a_2050_max5days['Rad'] = C_1a_2050_max5days['Rad'].resample('D', how='sum')/1000
C_1a_2050_max5days_mean = C_1a_2050_max5days.mean()
print '2050 1a: \n', C_1a_2050_max5days_mean

C_5a_2050_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/5jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_5a_2050 = C_5a_2050_0.set_index('datetime')
C_5a_2050_max5days = C_5a_2050.ix[240:]
C_5a_2050_max5days['Rad'] = C_5a_2050_max5days['Rad'].resample('D', how='sum')/1000
C_5a_2050_max5days_mean = C_5a_2050_max5days.mean()
print '2050 5a: \n', C_5a_2050_max5days_mean

C_20a_2050_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/20jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_20a_2050 = C_20a_2050_0.set_index('datetime')
C_20a_2050_max5days = C_20a_2050.ix[240:]
C_20a_2050_max5days['Rad'] = C_20a_2050_max5days['Rad'].resample('D', how='sum')/1000
C_20a_2050_max5days_mean = C_20a_2050_max5days.mean()
print '2050 20a: \n', C_20a_2050_max5days_mean

C_max_2050_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/Max/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_max_2050 = C_max_2050_0.set_index('datetime')
C_max_2050_max5days = C_max_2050.ix[240:]
C_max_2050_max5days['Rad'] = C_max_2050_max5days['Rad'].resample('D', how='sum')/1000
C_max_2050_max5days_mean = C_max_2050_max5days.mean()
print '2050 Max: \n', C_max_2050_max5days_mean

C_1a_2085_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/1jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_1a_2085 = C_1a_2085_0.set_index('datetime')
C_1a_2085_max5days = C_1a_2085.ix[240:]  #last five days
C_1a_2085_max5days['Rad'] = C_1a_2085_max5days['Rad'].resample('D', how='sum')/1000
C_1a_2085_max5days_mean = C_1a_2085_max5days.mean()
print '2085 1a: \n', C_1a_2085_max5days_mean

C_5a_2085_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/5jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_5a_2085 = C_5a_2085_0.set_index('datetime')
C_5a_2085_max5days = C_5a_2085.ix[240:]
C_5a_2085_max5days['Rad'] = C_5a_2085_max5days['Rad'].resample('D', how='sum')/1000
C_5a_2085_max5days_mean = C_5a_2085_max5days.mean()
print '2085 5a: \n', C_5a_2085_max5days_mean

C_20a_2085_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/20jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_20a_2085 = C_20a_2085_0.set_index('datetime')
C_20a_2085_max5days = C_20a_2085.ix[240:]
C_20a_2085_max5days['Rad'] = C_20a_2085_max5days['Rad'].resample('D', how='sum')/1000
C_20a_2085_max5days_mean = C_20a_2085_max5days.mean()
print '2085 20a: \n', C_20a_2085_max5days_mean

C_max_2085_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/Max/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_max_2085 = C_max_2085_0.set_index('datetime')
C_max_2085_max5days = C_max_2085.ix[240:]
C_max_2085_max5days['Rad'] = C_max_2085_max5days['Rad'].resample('D', how='sum')/1000
C_max_2085_max5days_mean = C_max_2085_max5days.mean()
print '2085 Max: \n', C_max_2085_max5days_mean

quit()

