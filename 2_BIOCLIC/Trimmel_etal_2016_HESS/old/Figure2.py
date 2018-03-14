__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

C_2013_0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/inputfiles/Climate_04inca.csv', sep=',', parse_dates=['DateTime'])
stats= C_2013_0.describe()
print 'C_2013=', stats
C_2013 = C_2013_0.set_index('DateTime')
#print C_2013
C_2013_glorad_sum = C_2013['GloRad (W/m2)'].resample('D', how='sum')/1000
C_2013_glorad_sum_1 = C_2013_glorad_sum.reset_index()

stats= C_2013_glorad_sum.describe()
print 'C_2013_gloR=', stats
#print C_2013_glorad_sum_1

C_1a_2030_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/1jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
#stats= C_1a_2030_0.describe()
#print 'C_2030=', stats
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
C_2030_wi = pd.concat([C_1a_2030_0['Wspd'], C_5a_2030_0['Wspd'],C_max_2030_0['Wspd']],axis=1)
C_2030_rh = pd.concat([C_1a_2030_0['Rhum'], C_5a_2030_0['Rhum'],C_max_2030_0['Rhum']],axis=1)

stats= C_2030.describe()
print 'C_2030_airt=', stats
stats= C_2030_rh.describe()
print 'C_2030_relh=', stats
stats= C_2030_wi.describe()
print 'C_2030_wspd=', stats

#print C_2030
C_2030 = np.array(C_2030.values)
C_2030_glorad = pd.concat([C_1a_2030_glorad_sum_1['Rad'], C_5a_2030_glorad_sum_1['Rad'], C_max_2030_glorad_sum_1['Rad']], axis=1)
stats= C_2030_glorad.describe()
print 'C_2030_gloR=', stats
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
C_2050_wi = pd.concat([C_1a_2050_0['Wspd'], C_5a_2050_0['Wspd'],C_max_2050_0['Wspd']],axis=1)
C_2050_rh = pd.concat([C_1a_2050_0['Rhum'], C_5a_2050_0['Rhum'],C_max_2050_0['Rhum']],axis=1)
stats= C_2050.describe()
print 'C_2050_airt=', stats
stats= C_2050_rh.describe()
print 'C_2050_relh=', stats
stats= C_2050_wi.describe()
print 'C_2050_wdsp=', stats

C_2050 = np.array(C_2050.values)
C_2050_glorad = pd.concat([C_1a_2050_glorad_sum_1['Rad'], C_5a_2050_glorad_sum_1['Rad'], C_max_2050_glorad_sum_1['Rad']], axis=1)
stats= C_2050_glorad.describe()
print 'C_2050_gloR=', stats
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
C_2085_wi = pd.concat([C_1a_2085_0['Wspd'], C_5a_2085_0['Wspd'],C_max_2085_0['Wspd']],axis=1)
C_2085_rh = pd.concat([C_1a_2085_0['Rhum'], C_5a_2085_0['Rhum'],C_max_2085_0['Rhum']],axis=1)

stats= C_2085.describe()
print 'C_2085_airT=', stats
stats= C_2085_rh.describe()
print 'C_2085_relH=', stats
stats= C_2085_wi.describe()
print 'C_2085_wind=', stats

C_2085 = np.array(C_2085.values)
C_2085_glorad = pd.concat([C_1a_2085_glorad_sum_1['Rad'], C_5a_2085_glorad_sum_1['Rad'], C_max_2085_glorad_sum_1['Rad']], axis=1)
stats= C_2085_glorad.describe()
print 'C_2085_gloR=', stats

C_2085_glorad = np.array(C_2085_glorad.values)


fs = 10  # fontsize

fig, axes = plt.subplots(nrows=3, ncols=3, sharey='row') #, figsize=(6, 6))
#fig.set_size_inches(3.39,2.54)

axes[0, 0].boxplot(C_2030)
axes[0, 0].set_title('2030', fontsize=fs)
axes[0, 0].set_ylabel('air temperature [degC]', fontsize=fs)
axes[0, 0].set(xticklabels=('1a','5a','max'))
#plt.xticks(fontsize='small')

axes[0, 1].boxplot(C_2050)
axes[0, 1].set_title('2050', fontsize=fs)
axes[0, 1].set(xticklabels=('1a','5a','max'))

axes[0, 2].boxplot(C_2085)
axes[0, 2].set_title('2085', fontsize=fs)
axes[0, 2].set(xticklabels=('1a','5a','max'))
#axisrange = [1,3,5,40]
#axes[0,0].axis(axisrange)

axes[1, 0].boxplot(C_2030_glorad)
axes[1, 0].set_ylabel('radiation sum [MJ d-1]', fontsize=fs)
axes[1, 0].set(xticklabels=('1a','5a','max'))

axes[1, 1].boxplot(C_2050_glorad)
axes[1, 1].set(xticklabels=('1a','5a','max'))

axes[1, 2].boxplot(C_2085_glorad)
axes[1, 2].set(xticklabels=('1a','5a','max'))


#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure2.tiff')
plt.show()

# #
# # ax = fig.add_subplot(221)
# #
# # plt.ylabel('air temperature [degC]')
# # #axes2.axhline(linestyle=':', color='black') #draw x axis as default value 0
# # ax.margins(0.2)
# # ax.set(xticklabels=('','2030','','2050','','2085'))  #fontsize=18
# # #axes2.set(title='B')
# # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#
# #ax = fig.add_subplot(222)
#
# # plt.text(20, 18, 'II', fontsize=20)
# # plt.setp(plt.gca(), xticklabels=[6, 12, 18], yticks=(10, 15, 20), xticks=(6, 12, 18))
# # plt.axis([1, 23, 5, 20])
#
# # ax = fig.add_subplot(223)
# #
# # ax = fig.add_subplot(224)
#
#

#
#
# quit()
#
#
#
# x = [1,2,3]
#
# Ta_1a_mean = [20.5847645429,23.0731301939,24.7293628809] #2030,2050,285
# Ta_1a_min = [9,12.6,25.2]
# Ta_1a_max = [31.4,32.6,35.5]
#
# Ta_5a_mean = [22.6595567867,22.6847645429,29.2368421053]
# Ta_5a_min = [12,8.3,18.7]
# Ta_5a_max = [35.7,34.2,38.9]
#
# Ta_max_mean = [26.232132964,27.1432132964,30.5614958449]
# Ta_max_min = [14.7,16.7,19.4]
# Ta_max_max = [38.8,39.1,40.9]
#
# fig = plt.figure()
#
# fig.set_size_inches(3.39,2.54)
#
#
#
# ax.plot(x, Ta_1a_mean, marker='x', linestyle='none', color='lightgrey', label='1a_mean')
# ax.plot(x, Ta_1a_min, marker='x', linestyle='none', color='grey', label='1a_min')
# ax.plot(x, Ta_1a_max, marker='x', linestyle='none', color='black', label='1a_max')
# ax.plot(x, Ta_5a_mean, marker='.', linestyle='none', color='lightgrey', label='5a_mean')
# ax.plot(x, Ta_5a_min, marker='.', linestyle='none', color='grey', label='5a_min')
# ax.plot(x, Ta_5a_max, marker='.', linestyle='none', color='black', label='5a_max')
# ax.plot(x, Ta_max_mean, marker='o',linestyle='none', color='lightgrey', label='max_mean')
# ax.plot(x, Ta_max_min, marker='o', linestyle='none', color='grey', label='max_min')
# ax.plot(x, Ta_max_max, marker='o', linestyle='none', color='black', label='max_max')