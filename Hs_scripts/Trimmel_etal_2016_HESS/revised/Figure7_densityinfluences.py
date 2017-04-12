__author__ = 'lnx'
# -*- coding: utf-8 -*-
#DFS20 - V01995 - V701995 - V1001995 - MLF
#DFS20 - V02085 - V702085 - V1002085 - MLF
#DFS20 - V02085 - V702085 - V1002085 - MLF*0.85

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

#WT_20a_2085_Sw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_STQ = pd.read_csv('/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V10009 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V10007 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V10005 = pd.read_csv('/home/lnx/PycharmProjects/HS/S306_P_V100_VD05_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V5009 = pd.read_csv('/home/lnx/PycharmProjects/HS/S303_P_V50_VD09_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V5007 = pd.read_csv('/home/lnx/PycharmProjects/HS/S302_P_V50_VD07_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V5005 = pd.read_csv('/home/lnx/PycharmProjects/HS/S307_P_V50_VD05_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')

WT_20a_2085_Cv_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_STQ = pd.read_csv('/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V10009 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V10007 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V10005 = pd.read_csv('/home/lnx/PycharmProjects/HS/S306_P_V100_VD05_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V5009 = pd.read_csv('/home/lnx/PycharmProjects/HS/S303_P_V50_VD09_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V5007 = pd.read_csv('/home/lnx/PycharmProjects/HS/S302_P_V50_VD07_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V5005 = pd.read_csv('/home/lnx/PycharmProjects/HS/S307_P_V50_VD05_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')

WT_20a_2085_Ev_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_STQ = pd.read_csv('/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V10009 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V10007 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V10005 = pd.read_csv('/home/lnx/PycharmProjects/HS/S306_P_V100_VD05_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V5009 = pd.read_csv('/home/lnx/PycharmProjects/HS/S303_P_V50_VD09_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V5007 = pd.read_csv('/home/lnx/PycharmProjects/HS/S302_P_V50_VD07_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V5005 = pd.read_csv('/home/lnx/PycharmProjects/HS/S307_P_V50_VD05_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')

WT_20a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_STQ = pd.read_csv('/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V10009 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V10007 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V10005 = pd.read_csv('/home/lnx/PycharmProjects/HS/S306_P_V100_VD05_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V5009 = pd.read_csv('/home/lnx/PycharmProjects/HS/S303_P_V50_VD09_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V5007 = pd.read_csv('/home/lnx/PycharmProjects/HS/S302_P_V50_VD07_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V5005 = pd.read_csv('/home/lnx/PycharmProjects/HS/S307_P_V50_VD05_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')

#Plotting
fig = plt.figure()#sharex= True, sharey= True)

ax = fig.add_subplot(223)
ax.plot(WT_20a_2085_Lw_V0['80.000'][-24:], linestyle=':', color = 'red', label='V0')
ax.plot(WT_20a_2085_Lw_STQ['80.000'][-24:], linestyle=':', color = 'black', label='STQ')
ax.plot(WT_20a_2085_Lw_V10009['80.000'][-24:], linestyle='-', color = 'blue', label='VH100 VD90')
ax.plot(WT_20a_2085_Lw_V10007['80.000'][-24:], linestyle='-', color = 'green', label='VH100 VD70')
ax.plot(WT_20a_2085_Lw_V10005['80.000'][-24:], linestyle='-', color = 'red', label='VH100 VD50')
ax.plot(WT_20a_2085_Lw_V5009['80.000'][-24:], linestyle='--', color = 'orange', label='VH50 VD90')
ax.plot(WT_20a_2085_Lw_V5007['80.000'][-24:], linestyle='--', color = 'green', label='VH50 VD70')
ax.plot(WT_20a_2085_Lw_V5005['80.000'][-24:], linestyle='--', color = 'orange', label='VH50 VD50')
ax.set_ylim([0,80])
ax.set_xlim([0.0,23.0])
ax.set_ylabel(u'long wave energy flux [W/m²]', fontsize='large')
ax.set_xlabel('time [h]', fontsize='large')

ax = fig.add_subplot(224)
ax.plot(WT_20a_2085_Cv_V0['80.000'][-24:], linestyle=':', color = 'red', label='V0')
ax.plot(WT_20a_2085_Cv_STQ['80.000'][-24:], linestyle=':', color = 'black', label='STQ')
ax.plot(WT_20a_2085_Cv_V10009['80.000'][-24:], linestyle='-', color = 'blue', label='VH100 VD90')
ax.plot(WT_20a_2085_Cv_V10007['80.000'][-24:], linestyle='-', color = 'green', label='VH100 VD70') #-48:-24
ax.plot(WT_20a_2085_Cv_V10005['80.000'][-24:], linestyle='-', color = 'orange', label='VH100 VD50')
ax.plot(WT_20a_2085_Cv_V5009['80.000'][-24:], linestyle='--', color = 'blue', label='VH50 VD90')
ax.plot(WT_20a_2085_Cv_V5007['80.000'][-24:], linestyle='--', color = 'green', label='VH50 VD70')
ax.plot(WT_20a_2085_Cv_V5005['80.000'][-24:], linestyle='--', color = 'orange', label='VH50 VD50')
ax.set_ylim([0.0,150.0])
ax.set_xlim([0.0,23.0])
ax.set_ylabel(u'sensible heat flux [W/m²]', fontsize='large')
ax.set_xlabel('time [h]', fontsize='large')

ax = fig.add_subplot(222)
ax.plot(WT_20a_2085_Ev_V10007['80.000'][-24:], linestyle='-', color = 'green', label='VH100 VD70')
ax.plot(WT_20a_2085_Ev_V10005['80.000'][-24:], linestyle='-', color = 'orange', label='VH100 VD50')
ax.plot(WT_20a_2085_Ev_V5009['80.000'][-24:], linestyle='--', color = 'blue', label='VH50 VD90')
ax.plot(WT_20a_2085_Ev_V5007['80.000'][-24:], linestyle='--', color = 'green', label='VH50 VD70')
ax.plot(WT_20a_2085_Ev_V5005['80.000'][-24:], linestyle='--', color = 'orange', label='VH50 VD50')
ax.plot(WT_20a_2085_Ev_V0['80.000'][-24:], linestyle=':', color = 'red', label='V0')
ax.plot(WT_20a_2085_Ev_STQ['80.000'][-24:], linestyle=':', color = 'black', label='STQ')
plt.setp(ax.get_xticklabels(), visible=False)
ax.set_ylabel(u'latent heat flux [W/m²]', fontsize='large')
ax.set_ylim([-600,0])
ax.set_xlim([0.0,23.0])

ax = fig.add_subplot(221)
ax.plot(WT_20a_2085_V0['80.000'][-24:], linestyle=':', color = 'red', label='V0')
ax.plot(WT_20a_2085_STQ['80.000'][-24:], linestyle=':', color = 'black', label='STQ')
ax.plot(WT_20a_2085_V10009['80.000'][-24:], linestyle='-', color = 'blue', label='VH100 VD90')
ax.plot(WT_20a_2085_V10007['80.000'][-24:], linestyle='-', color = 'green', label='VH100 VD70')
ax.plot(WT_20a_2085_V10005['80.000'][-24:], linestyle='-', color = 'orange', label='VH100 VD50')
ax.plot(WT_20a_2085_V5009['80.000'][-24:], linestyle='--', color = 'blue', label='VH50 VD90')
ax.plot(WT_20a_2085_V5007['80.000'][-24:], linestyle='--', color = 'green', label='VH50 VD70')
ax.plot(WT_20a_2085_V5005['80.000'][-24:], linestyle='--', color = 'orange', label='VH50 VD50')
plt.setp(ax.get_xticklabels(), visible=False)
ax.set_ylabel(u'water temperature [°C]', fontsize='large')
ax.set_xlim([0.0,23.0])


#ax = fig.add_subplot(326)
#ax.plot(WT_20a_2085_V10009['80.000'][-24:], linestyle='-', color = 'blue', label='VH100 VD90')
#ax.plot(WT_20a_2085_V10007['80.000'][-24:], linestyle='-', color = 'green', label='VH100 VD70')
#ax.plot(WT_20a_2085_V10005['80.000'][-24:], linestyle='-', color = 'orange', label='VH100 VD50')
#ax.plot(WT_20a_2085_V5009['80.000'][-24:], linestyle='--', color = 'blue', label='VH50 VD90')
#ax.plot(WT_20a_2085_V5007['80.000'][-24:], linestyle='--', color = 'green', label='VH50 VD70')
#ax.plot(WT_20a_2085_V5005['80.000'][-24:], linestyle='--', color = 'orange', label='VH50 VD50')
#ax.plot(WT_20a_2085_V0['80.000'][-24:], linestyle=':', color = 'red', label='V0')

#ax.legend(ncol=3,loc="upper right")
#labels = ["VH100 VD90","VH100 VD70","VH100 VD50","VH50 VD90","VH50 VD70","VH50 VD50", "V0"]
#ax.legend(labels, loc='upper right', ncol=3)#, bbox_to_anchor=(1.0, -0.4), prop={'size':11})

#plt.legend(loc=3, ncol=3)



plt.show()
