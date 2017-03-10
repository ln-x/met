__author__ = 'lnx'
#DFS20 - STQ1998 - STQ2085 - V02085
#DFS61 - STQ1998 - STQ2085 - V02085

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

Sw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_SR6.txt', skiprows=6, sep='\s+')#, index_col='Datetime') #, parse_dates="Datetime"
Lw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_TR.txt', skiprows=6, sep='\s+')#, index_col='Datetime') #, parse_dates="Datetime"
Cv = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_Conv.txt', skiprows=6, sep='\s+')#, index_col='Datetime') #, parse_dates="Datetime"
Ev = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_Evap.txt', skiprows=6, sep='\s+')#, index_col='Datetime') #, parse_dates="Datetime"
Cd = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_Cond.txt', skiprows=6, sep='\s+')#, index_col='Datetime') #, parse_dates="Datetime"
Bilanz = Sw + Lw + Cv + Cd + Ev
#Bilanz_mt = Sw + Lw + Cv_mt + Cd + Ev_mt

WT_20a_2085_Sw_V100_test = pd.read_csv('/home/lnx/PycharmProjects/HS/S300_P_V100_2085_20a_MLF_TESTrun_264/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_Sw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')

WT_20a_2085_Sw = pd.read_csv('/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw = pd.read_csv('/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv = pd.read_csv('/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev = pd.read_csv('/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd = pd.read_csv('/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')

WT_20a_2085_Sw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')

WT_20a_2085_Sw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')

WT_20a_2085_Sw_V100_VD07 = pd.read_csv('/home/lnx/PycharmProjects/HS/S300_P_V100_VD07_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')


"""
WT_20a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V0 = WT_20a_2085_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2085_V0 = np.array(WT_20a_2085_V0['61.000'])
WT_20a_2085_V0 = WT_20a_2085_V0.ravel()
WT_20a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V100 = WT_20a_2085_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2085_V100 = np.array(WT_20a_2085_V100['61.000'])
WT_20a_2085_V100 = WT_20a_2085_V100.ravel()
WT_2085_20a = transpose(np.array([WT_20a_2085_V0,WT_20a_2085,WT_20a_2085_V100]))
WT_2085_20a_stats = pd.DataFrame(WT_2085_20a).describe()
"""

print len(Bilanz)
print len(WT_20a_2085_Sw) #TODO - not same length!

fig = plt.figure()#sharex= True, sharey= True)

ax = fig.add_subplot(231)
ax.set_title('DFS20, STQ, 1995/20a')
ax.plot(Bilanz['80.000'][-24:], linestyle='-', color = 'black', lw=0.5)
ax.plot(Sw['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(Lw['80.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(Cv['80.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(Ev['80.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(Cd['80.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])
#plt.ylabel('W m-2', fontsize='small')
#plt.ylabel('W m-2', fontsize='small')
#plt.xlabel('time from episode start [h]', fontsize='small')
#plt.legend(loc=4, ncol=3, fontsize='small')
#plt.show()

ax = fig.add_subplot(232)

#plt.ylim([-750,750])
ax.set_title('DFS20, STQ, 2085/20a')
ax.plot(WT_20a_2085_Sw['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw['80.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv['80.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev['80.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd['80.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])

#plt.xlabel('time from episode start [h]', fontsize='small')
#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(233)
ax.set_title('DFS20, V0, 2085/20a')
ax.plot(WT_20a_2085_Sw_V0['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.set_ylim([-750,750])


ax = fig.add_subplot(234)
ax.set_title('DFS61, STQ, 1995/20a')
ax.plot(Sw['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(Lw['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(Cv['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(Ev['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(Cd['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])

ax = fig.add_subplot(235)
ax.set_title('DFS61, STQ, 2085/20a')
ax.plot(WT_20a_2085_Sw['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])

ax = fig.add_subplot(236)
ax.set_title('DFS61, V0, 2085/20a')
ax.plot(WT_20a_2085_Sw_V0['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.set_ylim([-750,750])

plt.show()
