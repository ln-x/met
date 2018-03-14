__author__ = 'lnx'

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

WT_1a_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S190_P_STQ_2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_1a_2030 = np.array(WT_1a_2030)
WT_1a_2030 = WT_1a_2030.ravel()
#print WT_1a_2030
WT_5a_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S196_P_STQ_2030_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_5a_2030 = np.array(WT_5a_2030)
WT_5a_2030 = WT_5a_2030.ravel()
#print WT_5a_2030
WT_max_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S214_P_STQ_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2030 = np.array(WT_max_2030)
WT_max_2030 = WT_max_2030.ravel()
#print WT_max_2030
WT_2030 = transpose(np.array([WT_1a_2030,WT_5a_2030,WT_max_2030]))
#print WT_2030
print pd.DataFrame(WT_2030).describe()

WT_1a_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S191_P_V0_2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_1a_2030_V0 = np.array(WT_1a_2030_V0)
WT_1a_2030_V0 = WT_1a_2030_V0.ravel()
WT_5a_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S197_P_V0_2030_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_5a_2030_V0 = np.array(WT_5a_2030_V0)
WT_5a_2030_V0 = WT_5a_2030_V0.ravel()
WT_max_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S215_P_V0_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2030_V0 = np.array(WT_max_2030_V0)
WT_max_2030_V0 = WT_max_2030_V0.ravel()
WT_2030_V0 = transpose(np.array([WT_1a_2030_V0,WT_5a_2030_V0,WT_max_2030_V0]))
print pd.DataFrame(WT_2030_V0).describe()

WT_1a_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S192_P_V100_2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_1a_2030_V100 = np.array(WT_1a_2030_V100)
WT_1a_2030_V100 = WT_1a_2030_V100.ravel()
WT_5a_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S198_P_V100_2030_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_5a_2030_V100 = np.array(WT_5a_2030_V100)
WT_5a_2030_V100 = WT_5a_2030_V100.ravel()
WT_max_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S216_P_V100_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2030_V100 = np.array(WT_max_2030_V100)
WT_max_2030_V100 = WT_max_2030_V100.ravel()
WT_2030_V100 = transpose(np.array([WT_1a_2030_V100,WT_5a_2030_V0,WT_max_2030_V100]))
print pd.DataFrame(WT_2030_V100).describe()

WT_1a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S220_P_STQ_2050_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_1a_2050 = np.array(WT_1a_2050)
WT_1a_2050 = WT_1a_2050.ravel()
WT_5a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S226_P_STQ_2050_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_5a_2050 = np.array(WT_5a_2050)
WT_5a_2050 = WT_5a_2050.ravel()
#print len(WT_5a_2050)
WT_max_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S244_P_STQ_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2050 = np.array(WT_max_2050)
WT_max_2050 = WT_max_2050.ravel()
#print len(WT_max_2050)
WT_2050 = transpose(np.array([WT_1a_2050,WT_5a_2050,WT_max_2050]))
print pd.DataFrame(WT_2050).describe()

WT_1a_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S221_P_V0_2050_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_1a_2050_V0 = np.array(WT_1a_2050_V0)
WT_1a_2050_V0 = WT_1a_2050_V0.ravel()
WT_5a_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S227_P_V0_2050_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_5a_2050_V0 = np.array(WT_5a_2050_V0)
WT_5a_2050_V0 = WT_5a_2050_V0.ravel()
WT_max_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S245_P_V0_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2050_V0 = np.array(WT_max_2050_V0)
WT_max_2050_V0 = WT_max_2050_V0.ravel()
WT_2050_V0 = transpose(np.array([WT_1a_2050_V0,WT_5a_2050_V0,WT_max_2050_V0]))
print pd.DataFrame(WT_2050_V0).describe()

WT_1a_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S222_P_V100_2050_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_1a_2050_V100 = np.array(WT_1a_2050_V100)
WT_1a_2050_V100 = WT_1a_2050_V100.ravel()
WT_5a_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S228_P_V100_2050_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_5a_2050_V100 = np.array(WT_5a_2050_V100)
WT_5a_2050_V100 = WT_5a_2050_V100.ravel()
WT_max_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S246_P_V100_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2050_V100 = np.array(WT_max_2050_V100)
WT_max_2050_V100 = WT_max_2050_V100.ravel()
WT_2050_V100 = transpose(np.array([WT_1a_2050_V100,WT_5a_2050_V100,WT_max_2050_V100]))
print pd.DataFrame(WT_2050_V100).describe()

WT_1a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_1a_2085 = np.array(WT_1a_2085)
WT_1a_2085 = WT_1a_2085.ravel()
WT_5a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S256_P_STQ_2085_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_5a_2085 = np.array(WT_5a_2085)
WT_5a_2085 = WT_5a_2085.ravel()
WT_max_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S274_P_STQ_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2085 = np.array(WT_max_2085)
WT_max_2085 = WT_max_2085.ravel()
WT_2085 = transpose(np.array([WT_1a_2085,WT_5a_2085,WT_max_2085]))
print pd.DataFrame(WT_2085).describe()

WT_1a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_1a_2085_V0 = np.array(WT_1a_2085_V0)
WT_1a_2085_V0 = WT_1a_2085_V0.ravel()
WT_5a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S257_P_V0_2085_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_5a_2085_V0 = np.array(WT_5a_2085_V0)
WT_5a_2085_V0 = WT_5a_2085_V0.ravel()
WT_max_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S275_P_V0_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2085_V0 = np.array(WT_max_2085_V0)
WT_max_2085_V0 = WT_max_2085_V0.ravel()
WT_2085_V0 = transpose(np.array([WT_1a_2085_V0,WT_5a_2085_V0,WT_max_2085_V0]))
print pd.DataFrame(WT_2085_V0).describe()

WT_1a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_1a_2085_V100 = np.array(WT_1a_2085_V100)
WT_1a_2085_V100 = WT_1a_2085_V100.ravel()
WT_5a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S258_P_V100_2085_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_5a_2085_V100 = np.array(WT_5a_2085_V100)
WT_5a_2085_V100 = WT_5a_2085_V100.ravel()
WT_max_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S276_P_V100_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2085_V100 = np.array(WT_max_2085_V100)
WT_max_2085_V100 = WT_max_2085_V100.ravel()
WT_2085_V100 = transpose(np.array([WT_1a_2085_V100,WT_5a_2085_V100,WT_max_2085_V100]))
print pd.DataFrame(WT_2085_V100).describe()

#f = open('/home/lnx/2_Documents/_BioClic/_Simulationen/Figure3_stats.txt','w')
#f.write(stats)

#labels = list['1a','5a','max']
fs = 10  # fontsize

fig, axes = plt.subplots(nrows=3, ncols=3, sharex='col', sharey='row') #, figsize=(6, 6))
#fig.set_size_inches(3.39,2.54)

axes[0, 0].boxplot(WT_2030) # labels=labels) #, showfliers=False)

#axes[0, 0].boxplot(WT_2030, whis=[5, 95]) #error: operands could not be broadcast together with shapes (37080,) (6,)
#axes[0, 0].set_title('whis=[5, 95]\n#percentiles', fontsize=fs)

axes[0, 0].set_title('2030_STQ', fontsize=fs)
axes[0, 0].set_ylabel('water temperature [degC]', fontsize=fs)
axes[0, 0].set(xticklabels=('1a','5a','max'))

axes[1, 0].boxplot(WT_2030_V0)
axes[1, 0].set_title('2030_V0', fontsize=fs)

axes[2, 0].boxplot(WT_2030_V100)
axes[2, 0].set_title('2030_V100', fontsize=fs)

axes[0, 1].boxplot(WT_2050)
axes[0, 1].set_title('2050_STQ', fontsize=fs)
axes[0, 1].set(xticklabels=('1a','5a','max'))

axes[1, 1].boxplot(WT_2050_V0)
axes[1, 1].set_title('2050_V0', fontsize=fs)

axes[2, 1].boxplot(WT_2050_V100)
axes[2, 1].set_title('2050_V100', fontsize=fs)

axes[0, 2].boxplot(WT_2085)
axes[0, 2].set_title('2085_STQ', fontsize=fs)
axes[0, 2].set(xticklabels=('1a','5a','max'))

axes[1, 2].boxplot(WT_2085_V0)
axes[1, 2].set_title('2085_V0', fontsize=fs)
#axes[1, 0].set(xticklabels=('1a','5a','max'))

axes[2, 2].boxplot(WT_2085_V100)
axes[2, 2].set_title('2085_V100', fontsize=fs)
#axes[1, 2].set(xticklabels=('1a','5a','max'))

#fig.subplots_adjust(hspace=0.4)

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure3_total.tiff')
plt.show()



