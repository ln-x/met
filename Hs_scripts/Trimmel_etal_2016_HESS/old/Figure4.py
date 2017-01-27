from pylab import *
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd
__author__ = 'lnx'
import matplotlib.pyplot as plt

WT = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_mean = WT.mean()
WT_max = WT.max()


WT_1a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_1a_2085_mean = WT_1a_2085.mean()
WT_1a_2085_max = WT_1a_2085.max()

WT_1a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_1a_2085_V0_mean = WT_1a_2085_V0.mean()
WT_1a_2085_V0_max = WT_1a_2085_V0.max()

WT_1a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_1a_2085_V100_mean = WT_1a_2085_V100.mean()
WT_1a_2085_V100_max = WT_1a_2085_V100.max()

WT_max_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S274_P_STQ_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2085_mean = WT_max_2085.mean()
WT_max_2085_max = WT_max_2085.max()

WT_max_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S275_P_V0_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2085_V0_mean = WT_max_2085_V0.mean()
WT_max_2085_V0_max = WT_max_2085_V0.max()

WT_max_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S276_P_V100_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2085_V100_mean = WT_max_2085_V100.mean()
WT_max_2085_V100_max = WT_max_2085_V100.max()


Rkm = np.arange(13,64.5,0.5)
#Rkm2 = np.arange(9,60.5,0.5)
#Rkm2 = np.arange(13,64.5,0.5)


fig = plt.figure()
#fig.set_size_inches(3.39,2.54)

#axisrange = [9,60,15,35]
#plt.axis(axisrange)

ax = fig.add_subplot(211)

ax.set_title('1a 2085')

axisrange = [12,60,12,33]
ax.axis(axisrange)
ax.plot(Rkm, WT_mean, color='black', lw=0.5, label='2013_STQ')
ax.plot(Rkm, WT_max, color='black', lw=0.3,  linestyle='dotted', label='2013_STQ_max')
ax.plot(Rkm, WT_1a_2085_mean, color='orange', lw=0.5, label='STQ')
ax.plot(Rkm, WT_1a_2085_max, color='orange', lw=0.3, linestyle='dotted', label='STQ_max')
ax.plot(Rkm, WT_1a_2085_V0_mean, color='red', lw=0.5, label='V0')
ax.plot(Rkm, WT_1a_2085_V0_max, color='red', lw=0.3, linestyle='dotted',  label='V0_max')
ax.plot(Rkm, WT_1a_2085_V100_mean, color='green', lw=0.5, label='V100')
ax.plot(Rkm, WT_1a_2085_V100_max, color='green', lw=0.3, linestyle='dotted', label='V100_max')
plt.legend(loc=9, ncol=4, fontsize='small')
plt.ylabel('water temperature [degC]')

ax = fig.add_subplot(212)

ax.set_title('max 2085')
axisrange = [12,60,12,33]
ax.axis(axisrange)
ax.plot(Rkm, WT_mean, color='black', lw=0.5)
ax.plot(Rkm, WT_max, color='black', lw=0.3,  linestyle='dotted')
ax.plot(Rkm, WT_max_2085_mean, color='orange', lw=0.5)
ax.plot(Rkm, WT_max_2085_V0_mean, color='red', lw=0.5)
ax.plot(Rkm, WT_max_2085_V100_mean, color='green', lw=0.5)
ax.plot(Rkm, WT_max_2085_max, color='orange', lw=0.3, linestyle='dotted')
ax.plot(Rkm, WT_max_2085_V0_max, color='red', lw=0.3, linestyle='dotted')
ax.plot(Rkm, WT_max_2085_V100_max, color='green', lw=0.3, linestyle='dotted')
plt.ylabel('water temperature [degC]')
plt.xlabel('distance from source [km]')

#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title="km")


fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure4_new.tiff')
plt.show()