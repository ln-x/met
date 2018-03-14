__author__ = 'lnx'

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

WT_2013 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_MLF_p/inputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')#, index_col='Datetime', parse_dates='Datetime')

WT_1a_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S190_P_STQ_2030_1a_MLF/inputfiles/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
WT_5a_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S196_P_STQ_2030_5a_MLF/inputfiles/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
WT_20a_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S202_P_STQ_2030_20a_MLF/inputfiles/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
WT_max_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S214_P_STQ_2030_Max_MLF/inputfiles/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})

WT_1a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S220_P_STQ_2050_1a_MLF/inputfiles/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
WT_5a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S226_P_STQ_2050_5a_MLF/inputfiles/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
WT_20a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S232_P_STQ_2050_20a_MLF/inputfiles/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
WT_max_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S244_P_STQ_2050_Max_MLF/inputfiles/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})

WT_1a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/inputfiles/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
WT_5a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S256_P_STQ_2085_5a_MLF/inputfiles/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
WT_20a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/inputfiles/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
WT_max_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S274_P_STQ_2085_Max_MLF/inputfiles/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})

Boundary_Conditions.csv', sep=',', parse_dates=['DateTime'])

fig = plt.figure()
plt.plot(WT_2013['61.000'], linestyle='-', color = 'blue', label='2013')
plt.plot(WT_1a_2030['61.000'], linestyle='dotted', color = 'green', label='1a_2030')
plt.plot(WT_5a_2030['61.000'], linestyle='--', color = 'green', label='5a_2030')
plt.plot(WT_20a_2030['61.000'], linestyle='-', color = 'green', label='20a_2030')
plt.plot(WT_max_2030['61.000'], color = 'green', linewidth=2.0, label='max_2030')
plt.plot(WT_1a_2050['61.000'], linestyle='dotted', color = 'violet', label='1a_2050')
plt.plot(WT_5a_2050['61.000'], linestyle='--', color = 'violet', label='5a_2050')
plt.plot(WT_20a_2050['61.000'], linestyle='-', color = 'violet', label='20a_2050')
plt.plot(WT_max_2050['61.000'], linestyle='-', linewidth=2.0, color = 'violet', label='max_2050')
plt.plot(WT_1a_2085['61.000'], linestyle='dotted', color = 'red', label='1a_2085')
plt.plot(WT_5a_2085['61.000'], linestyle='--', color = 'red', label='5a_2085')
plt.plot(WT_20a_2085['61.000'], linestyle='-', color = 'red', label='20a_2085')
plt.plot(WT_max_2085['61.000'], linestyle='-', linewidth=2.0,color = 'red', label='max_2085')

plt.ylabel('water temperature [degC]', fontsize='small')
plt.xlabel('time from episode start [h]', fontsize='small')

plt.legend(loc=4, ncol=3, fontsize='small')

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure3_total_timeline.tiff')

plt.show()



