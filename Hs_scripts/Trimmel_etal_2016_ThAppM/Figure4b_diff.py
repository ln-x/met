from pylab import *
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd
__author__ = 'lnx'
import matplotlib.pyplot as plt

WT = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_mean = WT.mean()
WT_max = WT.max()

WT_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S214_P_STQ_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_2030_mean = WT_2030.mean()
WT_2030_max = WT_2030.max()

WT_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S215_P_V0_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_2030_V0_mean = WT_2030_V0.mean()
WT_2030_V0_max = WT_2030_V0.max()

WT_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S216_P_V100_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_2030_V100_mean = WT_2030_V100.mean()
WT_2030_V100_max = WT_2030_V100.max()

WT_2030_V0_diff = (WT_2030_mean - WT_2030_V0_mean)*-1
WT_2030_V100_diff = WT_2030_mean - WT_2030_V100_mean

print WT_2030_mean.head()
print WT_2030_V0_mean.head()
print WT_2030_V0_diff.head()

WT_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S244_P_STQ_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_2050_mean = WT_2050.mean()
WT_2050_max = WT_2050.max()

WT_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S245_P_V0_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_2050_V0_mean = WT_2050_V0.mean()
WT_2050_V0_max = WT_2050_V0.max()

WT_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S246_P_V100_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_2050_V100_mean = WT_2050_V100.mean()
WT_2050_V100_max = WT_2050_V100.max()

WT_2050_V0_diff = (WT_2050_mean - WT_2050_V0_mean)*-1
WT_2050_V100_diff = WT_2050_mean - WT_2050_V100_mean

WT_max_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S274_P_STQ_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2085_mean = WT_max_2085.mean()
WT_max_2085_max = WT_max_2085.max()

WT_max_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S275_P_V0_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2085_V0_mean = WT_max_2085_V0.mean()
WT_max_2085_V0_max = WT_max_2085_V0.max()

WT_max_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S276_P_V100_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2085_V100_mean = WT_max_2085_V100.mean()
WT_max_2085_V100_max = WT_max_2085_V100.max()

WT_2085_V0_diff = (WT_max_2085_mean - WT_max_2085_V0_mean)*-1
WT_2085_V100_diff = WT_max_2085_mean - WT_max_2085_V100_mean

Rkm = np.arange(13,64.5,0.5)
#Rkm2 = np.arange(9,60.5,0.5)
#Rkm2 = np.arange(13,64.5,0.5)

fig = plt.figure()
#fig.set_size_inches(3.39,2.54)

axisrange = [9,60,-0.1,2.5]
plt.axis(axisrange)

ax = fig.add_subplot(111)
#ax.set_title('  2030 MAX', fontsize='small', loc='left')
#axisrange = [12,60,12,30]
#ax.axis(axisrange)
ax.plot(Rkm, WT_2030_V100_diff, color='green', lw=0.5, label='2030: STQ-V100')
ax.plot(Rkm, WT_2050_V100_diff, color='green', lw=0.5, linestyle='dashed',label='2050: STQ-V100')
ax.plot(Rkm, WT_2085_V100_diff, color='green', lw=0.5,linestyle='dotted', label='2085: STQ-V100')

ax.plot(Rkm, WT_2030_V0_diff, color='red', lw=0.5, label='2030: STQ-V0 *-1')
ax.plot(Rkm, WT_2050_V0_diff, color='red', lw=0.5, linestyle='dashed',label='2050: STQ-V0 *-1')
ax.plot(Rkm, WT_2085_V0_diff, color='red', lw=0.5, linestyle='dotted', label='2085: STQ-V0 *-1')

#ax.set(xticklabels=('','','','',''))
#plt.legend(bbox_to_anchor=(0.577, 1.35), ncol=4, loc=9, borderaxespad=0, fontsize='small')
plt.legend(fontsize='small', loc=4)
plt.ylabel('water temperature difference [degC]')
plt.xlabel('distance from source [km]')

#fig.legend()

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure4b_diff.tiff')
plt.show()