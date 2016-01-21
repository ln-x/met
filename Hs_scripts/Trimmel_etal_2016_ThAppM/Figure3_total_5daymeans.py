__author__ = 'lnx'

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

WT_1a_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S190_P_STQ_2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')#, index_col='Datetime', parse_dates='Datetime')
WT_1a_2030 = WT_1a_2030.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2030 = np.array(WT_1a_2030['61.000']) #select only reference station Unterwart DFM 61km
WT_1a_2030 = WT_1a_2030.ravel()
WT_1a_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S191_P_V0_2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2030_V0 = WT_1a_2030_V0.ix[240:].drop(['Datetime'],axis=1)
WT_1a_2030_V0 = np.array(WT_1a_2030_V0['61.000'])
WT_1a_2030_V0 = WT_1a_2030_V0.ravel()
WT_1a_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S192_P_V100_2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2030_V100 = WT_1a_2030_V100.ix[240:].drop(['Datetime'],axis=1)
WT_1a_2030_V100 = np.array(WT_1a_2030_V100['61.000'])
WT_1a_2030_V100 = WT_1a_2030_V100.ravel()
WT_2030_1a = transpose(np.array([WT_1a_2030_V0,WT_1a_2030,WT_1a_2030_V100]))
print pd.DataFrame(WT_2030_1a).describe()

WT_5a_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S196_P_STQ_2030_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2030 = WT_5a_2030.ix[240:].drop(['Datetime'],axis=1)
WT_5a_2030 = np.array(WT_5a_2030['61.000'])
WT_5a_2030 = WT_5a_2030.ravel()
WT_5a_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S197_P_V0_2030_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2030_V0 = WT_5a_2030_V0.ix[240:].drop(['Datetime'],axis=1)
WT_5a_2030_V0 = np.array(WT_5a_2030_V0['61.000'])
WT_5a_2030_V0 = WT_5a_2030_V0.ravel()
WT_5a_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S198_P_V100_2030_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2030_V100 = WT_5a_2030_V100.ix[240:].drop(['Datetime'],axis=1)
WT_5a_2030_V100 = np.array(WT_5a_2030_V100['61.000'])
WT_5a_2030_V100 = WT_5a_2030_V100.ravel()
WT_2030_5a = transpose(np.array([WT_5a_2030_V0,WT_5a_2030,WT_5a_2030_V100]))
print pd.DataFrame(WT_2030_5a).describe()

WT_20a_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S202_P_STQ_2030_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2030 = WT_20a_2030.ix[240:].drop(['Datetime'],axis=1)
WT_20a_2030 = np.array(WT_20a_2030['61.000'])
WT_20a_2030 = WT_20a_2030.ravel()
WT_20a_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S203_P_V0_2030_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2030_V0 = WT_20a_2030_V0.ix[240:].drop(['Datetime'],axis=1)
WT_20a_2030_V0 = np.array(WT_20a_2030_V0['61.000'])
WT_20a_2030_V0 = WT_20a_2030_V0.ravel()
WT_20a_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S204_P_V100_2030_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2030_V100 = WT_20a_2030_V100.ix[240:].drop(['Datetime'],axis=1)
WT_20a_2030_V100 = np.array(WT_20a_2030_V100['61.000'])
WT_20a_2030_V100 = WT_20a_2030_V100.ravel()
WT_2030_20a = transpose(np.array([WT_20a_2030_V0,WT_20a_2030,WT_20a_2030_V100]))
print pd.DataFrame(WT_2030_20a).describe()

WT_1a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S220_P_STQ_2050_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2050 = WT_1a_2050.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2050 = np.array(WT_1a_2050['61.000'])
WT_1a_2050 = WT_1a_2050.ravel()
WT_1a_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S221_P_V0_2050_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2050_V0 = WT_1a_2050_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2050_V0 = np.array(WT_1a_2050_V0['61.000'])
WT_1a_2050_V0 = WT_1a_2050_V0.ravel()
WT_1a_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S222_P_V100_2050_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2050_V100 = WT_1a_2050_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2050_V100 = np.array(WT_1a_2050_V100['61.000'])
WT_1a_2050_V100 = WT_1a_2050_V100.ravel()
WT_2050_1a = transpose(np.array([WT_1a_2050_V0,WT_1a_2050,WT_1a_2050_V100]))
print pd.DataFrame(WT_2050_1a).describe()

WT_5a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S226_P_STQ_2050_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2050 = WT_5a_2050.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2050 = np.array(WT_5a_2050['61.000'])
WT_5a_2050 = WT_5a_2050.ravel()
WT_5a_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S227_P_V0_2050_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2050_V0 = WT_5a_2050_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2050_V0 = np.array(WT_5a_2050_V0['61.000'])
WT_5a_2050_V0 = WT_5a_2050_V0.ravel()
WT_5a_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S228_P_V100_2050_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2050_V100 = WT_5a_2050_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2050_V100 = np.array(WT_5a_2050_V100['61.000'])
WT_5a_2050_V100 = WT_5a_2050_V100.ravel()
WT_2050_5a = transpose(np.array([WT_5a_2050_V0,WT_5a_2050,WT_5a_2050_V100]))
print pd.DataFrame(WT_2050_5a).describe()


WT_20a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S232_P_STQ_2050_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2050 = WT_20a_2050.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2050 = np.array(WT_20a_2050['61.000'])
WT_20a_2050 = WT_20a_2050.ravel()
WT_20a_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S233_P_V0_2050_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2050_V0 = WT_20a_2050_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2050_V0 = np.array(WT_20a_2050_V0['61.000'])
WT_20a_2050_V0 = WT_20a_2050_V0.ravel()
WT_20a_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S234_P_V100_2050_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2050_V100 = WT_20a_2050_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2050_V100 = np.array(WT_20a_2050_V100['61.000'])
WT_20a_2050_V100 = WT_20a_2050_V100.ravel()
WT_2050_20a = transpose(np.array([WT_20a_2050_V0,WT_20a_2050,WT_20a_2050_V100]))
print pd.DataFrame(WT_2050_20a).describe()

WT_1a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2085 = WT_1a_2085.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2085 = np.array(WT_1a_2085['61.000'])
WT_1a_2085 = WT_1a_2085.ravel()
WT_1a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2085_V0 = WT_1a_2085_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2085_V0 = np.array(WT_1a_2085_V0['61.000'])
WT_1a_2085_V0 = WT_1a_2085_V0.ravel()
WT_1a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2085_V100 = WT_1a_2085_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2085_V100 = np.array(WT_1a_2085_V100['61.000'])
WT_1a_2085_V100 = WT_1a_2085_V100.ravel()
WT_2085_1a = transpose(np.array([WT_1a_2085_V0,WT_1a_2085,WT_1a_2085_V100]))
print pd.DataFrame(WT_2085_1a).describe()


WT_5a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S256_P_STQ_2085_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2085 = WT_5a_2085.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2085 = np.array(WT_5a_2085['61.000'])
WT_5a_2085 = WT_5a_2085.ravel()
WT_5a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S257_P_V0_2085_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2085_V0 = WT_5a_2085_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2085_V0 = np.array(WT_5a_2085_V0['61.000'])
WT_5a_2085_V0 = WT_5a_2085_V0.ravel()
WT_5a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S258_P_V100_2085_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2085_V100 = WT_5a_2085_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2085_V100 = np.array(WT_5a_2085_V100['61.000'])
WT_5a_2085_V100 = WT_5a_2085_V100.ravel()
WT_2085_5a = transpose(np.array([WT_5a_2085_V0,WT_5a_2085,WT_5a_2085_V100]))
print pd.DataFrame(WT_2085_5a).describe()

WT_20a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085 = WT_20a_2085.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2085 = np.array(WT_20a_2085['61.000'])
WT_20a_2085 = WT_20a_2085.ravel()
WT_20a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V0 = WT_20a_2085_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2085_V0 = np.array(WT_20a_2085_V0['61.000'])
WT_20a_2085_V0 = WT_20a_2085_V0.ravel()
WT_20a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V100 = WT_20a_2085_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2085_V100 = np.array(WT_20a_2085_V100['61.000'])
WT_20a_2085_V100 = WT_20a_2085_V100.ravel()
WT_2085_20a = transpose(np.array([WT_20a_2085_V0,WT_20a_2085,WT_20a_2085_V100]))
print pd.DataFrame(WT_2085_20a).describe()

#f = open('/home/lnx/2_Documents/_BioClic/_Simulationen/Figure3_stats.txt','w')
#f.write(stats)

#labels = list['1a','5a','max']
fs = 10  # fontsize

fig, axes = plt.subplots(nrows=3, ncols=3, sharex='col', sharey='row') #, figsize=(6, 6))
#fig.set_size_inches(3.39,2.54)

axes[0, 0].boxplot(WT_2030_1a) # labels=labels) #, showfliers=False)
axes[0, 0].set_title('2030_1a', fontsize=fs)
axes[0, 0].set_ylabel('water temperature [degC]', fontsize=fs)
axes[0, 0].set(xticklabels=('V0','STQ','V100'))

axes[1, 0].boxplot(WT_2030_5a)
axes[1, 0].set_title('2030_5a', fontsize=fs)
axes[1, 0].set_ylabel('water temperature [degC]', fontsize=fs)

axes[2, 0].boxplot(WT_2030_20a)
axes[2, 0].set_title('2030_20a', fontsize=fs)
axes[2, 0].set_ylabel('water temperature [degC]', fontsize=fs)

axes[0, 1].boxplot(WT_2050_1a)
axes[0, 1].set_title('2050_1a', fontsize=fs)
axes[0, 1].set(xticklabels=('V0','STQ','V100'))

axes[1, 1].boxplot(WT_2050_5a)
axes[1, 1].set_title('2050_5a', fontsize=fs)

axes[2, 1].boxplot(WT_2050_20a)
axes[2, 1].set_title('2050_20a', fontsize=fs)

axes[0, 2].boxplot(WT_2085_1a)
axes[0, 2].set_title('2085_1a', fontsize=fs)
axes[0, 2].set(xticklabels=('V0','STQ','V100'))

axes[1, 2].boxplot(WT_2085_5a)
axes[1, 2].set_title('2085_5a', fontsize=fs)
#axes[1, 0].set(xticklabels=('1a','5a','max'))

axes[2, 2].boxplot(WT_2085_20a)
axes[2, 2].set_title('2085_20a', fontsize=fs)
#axes[1, 2].set(xticklabels=('1a','5a','max'))

#fig.subplots_adjust(hspace=0.4)

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure3_total_5days_vegcomp.tiff')
plt.show()



