__author__ = 'lnx'
#DFS20 - V02085 - V702085 - V1002085
#DFS61 - V02085 - V702085 - V1002085

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

WT_20a_2085_Sw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')

WT_20a_2085_Sw_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')

#rint len(Bilanz)
#rint len(WT_20a_2085_Sw) #TODO - not same length!

fig = plt.figure()#sharex= True, sharey= True)

ax = fig.add_subplot(231)
ax.set_title('DFS20, V0, 2085/20a')
ax.plot(WT_20a_2085_Sw_V0['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V0['80.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V0['80.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V0['80.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V0['80.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])
#plt.ylabel('W m-2', fontsize='small')
#plt.ylabel('W m-2', fontsize='small')
#plt.xlabel('time from episode start [h]', fontsize='small')
#plt.legend(loc=4, ncol=3, fontsize='small')
#plt.show()

ax = fig.add_subplot(232)

#plt.ylim([-750,750])
ax.set_title('DFS20, V70, 2085/20a')
ax.plot(WT_20a_2085_Sw_V70['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V70['80.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V70['80.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V70['80.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V70['80.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])

#plt.xlabel('time from episode start [h]', fontsize='small')
#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(233)
ax.set_title('DFS20, V100, 2085/20a')
ax.plot(WT_20a_2085_Sw_V100['80.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V100['80.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V100['80.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V100['80.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V100['80.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])


ax = fig.add_subplot(234)
ax.set_title('DFS61, V0, 2085/20a')
ax.plot(WT_20a_2085_Sw_V0['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V0['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V0['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V0['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V0['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])

ax = fig.add_subplot(235)
ax.set_title('DFS61, V70, 2085/20a')
ax.plot(WT_20a_2085_Sw_V70['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V70['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V70['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V70['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V70['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])

ax = fig.add_subplot(236)
ax.set_title('DFS61, V100, 2085/20a')
ax.plot(WT_20a_2085_Sw_V100['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V100['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V100['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V100['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V100['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])

plt.show()
