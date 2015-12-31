__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

C_2013_0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/inputfiles/Climate_04inca.csv', sep=',', parse_dates=['DateTime'])
C_2013 = C_2013_0.set_index('DateTime')
#print C_2013
C_2013_glorad_sum = C_2013['GloRad (W/m2)'].resample('D', how='sum')/1000
#C_2013_glorad_sum_1 = C_2013_glorad_sum.reset_index()
C_2013_glorad = np.array(C_2013_glorad_sum.values)
C_2013 = np.array(C_2013['Air Temp (*C)'].values)

print C_2013

C_1a_2030_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/1jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_1a_2030 = C_1a_2030_0.set_index('datetime')
C_1a_2030_glorad_sum = C_1a_2030['Rad'].resample('D', how='sum')/1000
C_1a_2030_glorad_sum_1 = C_1a_2030_glorad_sum.reset_index()
#print C_1a_2030_glorad_sum_1.head()

C_5a_2030_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/5jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_5a_2030 = C_5a_2030_0.set_index('datetime')
C_5a_2030_glorad_sum = C_5a_2030['Rad'].resample('D', how='sum')/1000
C_5a_2030_glorad_sum_1 = C_5a_2030_glorad_sum.reset_index()

C_max_2030_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/Max/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_max_2030 = C_max_2030_0.set_index('datetime')
C_max_2030_glorad_sum = C_max_2030['Rad'].resample('D', how='sum')/1000
C_max_2030_glorad_sum_1 = C_max_2030_glorad_sum.reset_index()

# #WT_2030 = pd.merge(WT_1a_2030, WT_5a_2030) #doesnt work - because of Series?
C_2030 = pd.concat([C_1a_2030_0['AirT'], C_5a_2030_0['AirT'],C_max_2030_0['AirT']],axis=1)
#print C_2030
C_2030 = np.array(C_2030.values)
C_2030_glorad = pd.concat([C_1a_2030_glorad_sum_1['Rad'], C_5a_2030_glorad_sum_1['Rad'], C_max_2030_glorad_sum_1['Rad']], axis=1)
C_2030_glorad = np.array(C_2030_glorad.values)
print C_2030_glorad

C_1a_2050_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/1jaehrl/MLF/Climate_04.csv',sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_1a_2050 = C_1a_2050_0.set_index('datetime')
C_1a_2050_glorad_sum = C_1a_2050['Rad'].resample('D', how='sum')/1000
C_1a_2050_glorad_sum_1 = C_1a_2050_glorad_sum.reset_index()

C_5a_2050_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/5jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_5a_2050 = C_5a_2050_0.set_index('datetime')
C_5a_2050_glorad_sum = C_5a_2050['Rad'].resample('D', how='sum')/1000
C_5a_2050_glorad_sum_1 = C_5a_2050_glorad_sum.reset_index()

C_max_2050_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/Max/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_max_2050 = C_max_2030_0.set_index('datetime')
C_max_2050_glorad_sum = C_max_2050['Rad'].resample('D', how='sum')/1000
C_max_2050_glorad_sum_1 = C_max_2050_glorad_sum.reset_index()

C_2050 = pd.concat([C_1a_2050_0['AirT'], C_5a_2050_0['AirT'],C_max_2050_0['AirT']],axis=1)
C_2050 = np.array(C_2050.values)
C_2050_glorad = pd.concat([C_1a_2050_glorad_sum_1['Rad'], C_5a_2050_glorad_sum_1['Rad'], C_max_2050_glorad_sum_1['Rad']], axis=1)
C_2050_glorad = np.array(C_2050_glorad.values)

C_1a_2085_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/1jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_1a_2085 = C_1a_2085_0.set_index('datetime')
C_1a_2085_glorad_sum = C_1a_2085['Rad'].resample('D', how='sum')/1000
C_1a_2085_glorad_sum_1 = C_1a_2085_glorad_sum.reset_index()

C_5a_2085_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/5jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_5a_2085 = C_5a_2085_0.set_index('datetime')
C_5a_2085_glorad_sum = C_5a_2085['Rad'].resample('D', how='sum')/1000
C_5a_2085_glorad_sum_1 = C_5a_2085_glorad_sum.reset_index()

C_max_2085_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/Max/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_max_2085 = C_max_2085_0.set_index('datetime')
C_max_2085_glorad_sum = C_max_2085['Rad'].resample('D', how='sum')/1000
C_max_2085_glorad_sum_1 = C_max_2085_glorad_sum.reset_index()

C_2085 = pd.concat([C_1a_2085_0['AirT'], C_5a_2085_0['AirT'],C_max_2085_0['AirT']],axis=1)
C_2085 = np.array(C_2085.values)
C_2085_glorad = pd.concat([C_1a_2085_glorad_sum_1['Rad'], C_5a_2085_glorad_sum_1['Rad'], C_max_2085_glorad_sum_1['Rad']], axis=1)
C_2085_glorad = np.array(C_2085_glorad.values)

fs = 10  # fontsize

fig, axes = plt.subplots(nrows=2, ncols=4, sharey='row') #, figsize=(6, 6))
#fig.set_size_inches(3.39,2.54)

axes[0,0].boxplot(C_2013)
axes[0,0].set_title('2013', fontsize=fs)
axes[0,0].set_ylabel('air temperature [degC]', fontsize=fs)
axes[0,0].set(xticklabels=(' '))

axes[0, 1].boxplot(C_2030)
axes[0, 1].set_title('2030', fontsize=fs)
axes[0, 1].set(xticklabels=('1a','5a','max'))
#plt.xticks(fontsize='small')

axes[0, 2].boxplot(C_2050)
axes[0, 2].set_title('2050', fontsize=fs)
axes[0, 2].set(xticklabels=('1a','5a','max'))

axes[0, 3].boxplot(C_2085)
axes[0, 3].set_title('2085', fontsize=fs)
axes[0, 3].set(xticklabels=('1a','5a','max'))
#axisrange = [1,3,5,40]
#axes[0,0].axis(axisrange)

axes[1, 0].boxplot(C_2013_glorad)
axes[1, 0].set_ylabel('radiation sum [MJ d-1]', fontsize=fs)
axes[1, 0].set(xticklabels=(' '))

axes[1, 1].boxplot(C_2030_glorad)
axes[1, 1].set(xticklabels=('1a','5a','max'))

axes[1, 2].boxplot(C_2050_glorad)
axes[1, 2].set(xticklabels=('1a','5a','max'))

axes[1, 3].boxplot(C_2085_glorad)
axes[1, 3].set(xticklabels=('1a','5a','max'))

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure2.tiff')
plt.show()