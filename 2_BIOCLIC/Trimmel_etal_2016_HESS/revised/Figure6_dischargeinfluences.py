# -*- coding: utf-8 -*-
__author__ = 'lnx'
#DFS20 - V01995 - V701995 - V1001995 - MLF
#DFS20 - V02085 - V702085 - V1002085 - MLF
#DFS20 - V02085 - V702085 - V1002085 - MLF*0.85

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

WT_20a_2085_Sw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')
WT_20a_2085_ER_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Rate_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V0_Flow = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Hyd_Flow.txt', skiprows=6, sep='\s+')

WT_20a_2085_Sw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')
WT_20a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V100_Flow = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Hyd_Flow.txt', skiprows=6, sep='\s+')

WT_20a_2085_Sw_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')
WT_20a_2085_ER_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Rate_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V0_085MLF_Flow = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Hyd_Flow.txt', skiprows=6, sep='\s+')

WT_20a_2085_Sw_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')
WT_20a_2085_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V100_085MLF_Flow = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Hyd_Flow.txt', skiprows=6, sep='\s+')

#Plotting
fig = plt.figure()#sharex= True, sharey= True)

ax = fig.add_subplot(221)
ax.set_title('V0, DFS20')
ax.plot(WT_20a_2085_Sw_V0['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V0['80.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V0['80.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V0['80.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V0['80.000'][-24:], linestyle='-', color = 'violet', label='Cd')
plt.setp(ax.get_xticklabels(), visible=False)
ax.set_ylim([-750,750])
ax.set_ylabel(u'[W/m²]', fontsize='large')
ax2 = ax.twinx()
ax2.plot(WT_20a_2085_V0['80.000'][-24:], linestyle='-', color = 'blue', label='WT')
ax2.plot(WT_20a_2085_V0_085MLF['80.000'][-24:], linestyle='--', color = 'blue', label='WT')
plt.setp(ax2.get_yticklabels(), visible=False)
ax2.set_ylim([20,30])

ax = fig.add_subplot(222)
ax.set_title('V0, DFS61')
ax.plot(WT_20a_2085_Sw_V0_085MLF['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V0_085MLF['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V0_085MLF['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V0_085MLF['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V0_085MLF['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
plt.setp(ax.get_xticklabels(), visible=False)
ax.set_ylim([-750,750])
ax2 = ax.twinx()
ax2.plot(WT_20a_2085_V0['39.000'][-24:], linestyle='-', color = 'blue', label='WT')
ax2.plot(WT_20a_2085_V0_085MLF['39.000'][-24:], linestyle='--', color = 'blue', label='WT')
plt.setp(ax.get_yticklabels(), visible=False)
ax2.set_ylim([20,30])
ax2.set_ylabel(u'Water temperature [°C]', fontsize='large')


ax = fig.add_subplot(223)

##ALL SUBGRAPHS: DFS20, 2085/20a, last day of the episode!
#plt.ylim([-750,750])
ax.set_title('V100, DFS20')
ax.plot(WT_20a_2085_Sw_V100_085MLF['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V100_085MLF['80.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V100_085MLF['80.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V100_085MLF['80.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V100_085MLF['80.000'][-24:], linestyle='-', color = 'violet', label='Cd')
#plt.setp(ax.get_xticklabels(), visible=False)
ax.set_xlabel('Time [h]', fontsize='large')
ax.set_ylabel(u'[W/m²]', fontsize='large')
ax.set_ylim([-750,750])
ax2 = ax.twinx()
ax2.plot(WT_20a_2085_V100['80.000'][-24:], linestyle='-', color = 'blue', label='WT')
ax2.plot(WT_20a_2085_V100_085MLF['80.000'][-24:], linestyle='--', color = 'blue', label='WT')
#ax2.legend()
ax2.set_ylim([20,30])
plt.setp(ax2.get_yticklabels(), visible=False)

#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(224)
ax.set_title('V100, DFS61')
ax.plot(WT_20a_2085_Sw_V100['38.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Sw_V100['38.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V100['38.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V100['38.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V100['38.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V100['38.000'][-24:], linestyle='-', color = 'violet', label='Cd')
#plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)
ax2 = ax.twinx()
ax2.plot(WT_20a_2085_V100['38.000'][-24:], linestyle='-', color = 'blue', label='WT')
ax2.plot(WT_20a_2085_V100_085MLF['38.000'][-24:], linestyle='--', color = 'blue', label='WT')
ax2.set_ylim([20,30])
ax.set_ylim([-750,750])
ax2.set_ylabel(u'Water temperature [°C]', fontsize='large')
ax.set_xlabel('Time [h]', fontsize='large')

plt.show()
