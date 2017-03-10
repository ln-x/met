__author__ = 'lnx'
#DFS20 - V01995 - V701995 - V1001995 - MLF
#DFS20 - V02085 - V702085 - V1002085 - MLF
#DFS20 - V02085 - V702085 - V1002085 - MLF*0.85

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
WT_20a_1995_Sw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_1995_Lw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_1995_Cv_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_1995_Ev_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_1995_Cd_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')
WT_20a_1995_ER_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles/Rate_Evap.txt', skiprows=6, sep='\s+')
WT_20a_1995_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_1995_V0_Flow = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles/Hyd_Flow.txt', skiprows=6, sep='\s+')

#last day : [-24:], last 5days: [-120:]
V0_now_balance = WT_20a_1995_Sw_V0['39.000'][-120:].mean() + WT_20a_1995_Lw_V0['39.000'][-120:].mean()+ WT_20a_1995_Cv_V0['39.000'][-120:].mean()+ \
             WT_20a_1995_Ev_V0['39.000'][-120:].mean()+ WT_20a_1995_Cd_V0['39.000'][-120:].mean()
V0_now_balance_s = "bal = %1.2f W m-2" %V0_now_balance
V0_now_WT = "WT = %1.2f degC" %WT_20a_1995_V0['39.000'][-120:].mean()
V0_now_Ev = "evap = %1.2f W m-2" %WT_20a_1995_Ev_V0['39.000'][-120:].mean()
V0_now_evap = "ev_sum = %1.2f mm" %WT_20a_1995_ER_V0['39.000'][-120:].sum()
#V0_now_evap = "ev_sum = %1.2f mm" %WT_20a_1995_ER_V0['39.000'][-120:].sum()



WT_20a_1995_Sw_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V70_2013_MLF_p/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_1995_Lw_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V70_2013_MLF_p/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_1995_Cv_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V70_2013_MLF_p/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_1995_Ev_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V70_2013_MLF_p/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_1995_Cd_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V70_2013_MLF_p/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')
WT_20a_1995_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V70_2013_MLF_p/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')

V70_now_balance = WT_20a_1995_Sw_V70['39.000'][-120:].mean() + WT_20a_1995_Lw_V70['39.000'][-120:].mean()+ WT_20a_1995_Cv_V70['39.000'][-120:].mean()+ \
             WT_20a_1995_Ev_V70['39.000'][-120:].mean()+ WT_20a_1995_Cd_V70['39.000'][-120:].mean()
V70_now_balance_s = "bal = %1.2f W m-2" %V70_now_balance

WT_20a_1995_Sw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_1995_Lw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_1995_Cv_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_1995_Ev_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_1995_Cd_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')
WT_20a_1995_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')

V100_now_balance = WT_20a_1995_Sw_V100['39.000'][-120:].mean() + WT_20a_1995_Lw_V100['39.000'][-120:].mean()+ WT_20a_1995_Cv_V100['39.000'][-120:].mean()+ \
             WT_20a_1995_Ev_V100['39.000'][-120:].mean()+ WT_20a_1995_Cd_V100['39.000'][-120:].mean()
V100_now_balance_s = "bal = %1.2f W m-2" %V100_now_balance

WT_20a_2085_Sw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')
WT_20a_2085_ER_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Rate_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V0_Flow = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Hyd_Flow.txt', skiprows=6, sep='\s+')

V0_balance = WT_20a_2085_Sw_V0['39.000'][-120:].mean() + WT_20a_2085_Lw_V0['39.000'][-120:].mean()+ WT_20a_2085_Cv_V0['39.000'][-120:].mean()+ \
             WT_20a_2085_Ev_V0['39.000'][-120:].mean()+ WT_20a_2085_Cd_V0['39.000'][-120:].mean()
V0_balance_s = "bal = %1.2f W m-2" %V0_balance
V0_WT = "WT = %1.2f degC" %WT_20a_2085_V0['39.000'][-120:].mean()
V0_Ev = "evap = %1.2f W m-2" %WT_20a_2085_Ev_V0['39.000'][-120:].mean()
V0_evap = "ev_sum = %1.2f mm" %WT_20a_2085_ER_V0['39.000'][-120:].sum()
V0_Flow = "discharge = %1.4f m2 s-1" %WT_20a_2085_V0_Flow['39.000'][-120:].mean()


WT_20a_2085_Sw_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')
WT_20a_2085_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')

V70_balance = WT_20a_2085_Sw_V70['39.000'][-120:].mean() + WT_20a_2085_Lw_V70['39.000'][-120:].mean()+ WT_20a_2085_Cv_V70['39.000'][-120:].mean()+ \
             WT_20a_2085_Ev_V70['39.000'][-120:].mean()+ WT_20a_2085_Cd_V70['39.000'][-120:].mean()
V70_balance_s = "bal = %1.2f W m-2" %V70_balance
V70_WT = "WT = %1.2f,%1.2f degC" %(WT_20a_2085_V70['39.000'][-120:].mean(),WT_20a_2085_V70['39.000'][-120:].max())


WT_20a_2085_Sw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')
WT_20a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V100_Flow = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Hyd_Flow.txt', skiprows=6, sep='\s+')

V100_balance = WT_20a_2085_Sw_V100['39.000'][-120:].mean() + WT_20a_2085_Lw_V100['39.000'][-120:].mean()+ WT_20a_2085_Cv_V100['39.000'][-120:].mean()+ \
             WT_20a_2085_Ev_V100['39.000'][-120:].mean()+ WT_20a_2085_Cd_V100['39.000'][-120:].mean()
V100_balance_s = "bal = %1.2f W m-2" %V100_balance
V100_WT = "WT = %1.2f,%1.2f degC" %(WT_20a_2085_V100['39.000'][-120:].mean(), WT_20a_2085_V100['39.000'][-120:].max())
V100_Flow = "discharge = %1.4f m2 s-1" %WT_20a_2085_V100_Flow['39.000'][-120:].mean()

WT_20a_2085_Sw_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')
WT_20a_2085_ER_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Rate_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_V0_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V0_085MLF_Flow = pd.read_csv('/home/lnx/PycharmProjects/HS/S323_P_V0_2085_20a_085MLF/outputfiles/Hyd_Flow.txt', skiprows=6, sep='\s+')

V0_085MLF_balance = WT_20a_2085_Sw_V0_085MLF['39.000'][-120:].mean() + WT_20a_2085_Lw_V0_085MLF['39.000'][-120:].mean()+ WT_20a_2085_Cv_V0_085MLF['39.000'][-120:].mean()+ \
             WT_20a_2085_Ev_V0_085MLF['39.000'][-120:].mean()+ WT_20a_2085_Cd_V0_085MLF['39.000'][-120:].mean()
V0_085MLF_balance_s = "bal = %1.2f W m-2" %V0_085MLF_balance

V0_085MLF_WT = "WT = %1.2f, %1.2f degC" %(WT_20a_2085_V0_085MLF['39.000'][-120:].mean(), WT_20a_2085_V0_085MLF['39.000'][-120:].max())
V0_085MLF_Ev = "evap = %1.2f W m-2" %WT_20a_2085_Ev_V0_085MLF['39.000'][-120:].mean()
V0_085MLF_evap = "ev_sum = %1.2f mm" %WT_20a_2085_ER_V0_085MLF['39.000'][-120:].sum()
V0_085MLF_Flow = "discharge = %1.4f m3 s-1" %WT_20a_2085_V0_085MLF_Flow['39.000'][-120:].mean()


WT_20a_2085_Sw_V70_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S321_P_V100_VD07_2085_20a_085MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V70_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S321_P_V100_VD07_2085_20a_085MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V70_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S321_P_V100_VD07_2085_20a_085MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V70_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S321_P_V100_VD07_2085_20a_085MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V70_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S321_P_V100_VD07_2085_20a_085MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')
WT_20a_2085_V70_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S321_P_V100_VD07_2085_20a_085MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')

V70_085MLF_balance = WT_20a_2085_Sw_V70_085MLF['39.000'][-120:].mean() + WT_20a_2085_Lw_V70_085MLF['39.000'][-120:].mean()+ WT_20a_2085_Cv_V70_085MLF['39.000'][-120:].mean()+ \
             WT_20a_2085_Ev_V70_085MLF['39.000'][-120:].mean()+ WT_20a_2085_Cd_V70_085MLF['39.000'][-120:].mean()
V70_085MLF_balance_s = "bal = %1.2f W m-2" %V70_085MLF_balance
V70_085MLF_WT = "WT = %1.2f, %1.2f degC" %(WT_20a_2085_V70_085MLF['39.000'][-120:].mean(), WT_20a_2085_V70_085MLF['39.000'][-120:].max())


WT_20a_2085_Sw_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_SR6.txt', skiprows=6, sep='\s+')
WT_20a_2085_Lw_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_TR.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cv_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_Conv.txt', skiprows=6, sep='\s+')
WT_20a_2085_Ev_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_Evap.txt', skiprows=6, sep='\s+')
WT_20a_2085_Cd_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Heat_Cond.txt', skiprows=6, sep='\s+')
WT_20a_2085_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V100_085MLF_Flow = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Hyd_Flow.txt', skiprows=6, sep='\s+')

V100_085MLF_balance = WT_20a_2085_Sw_V100_085MLF['39.000'][-120:].mean() + WT_20a_2085_Lw_V100_085MLF['39.000'][-120:].mean()+ WT_20a_2085_Cv_V100_085MLF['39.000'][-120:].mean()+ \
             WT_20a_2085_Ev_V100_085MLF['39.000'][-120:].mean()+ WT_20a_2085_Cd_V100_085MLF['39.000'][-120:].mean()
V100_085MLF_balance_s = "bal = %1.2f W m-2" %V100_085MLF_balance
V100_085MLF_WT = "WT = %1.2f, %1.2f degC" %(WT_20a_2085_V100_085MLF['39.000'][-120:].mean(), WT_20a_2085_V100_085MLF['39.000'][-120:].max())
V100_085MLF_Flow = "discharge = %1.4f m2 s-1" %WT_20a_2085_V100_085MLF_Flow['39.000'][-120:].mean()


fig = plt.figure()#sharex= True, sharey= True)

ax = fig.add_subplot(331)
ax.set_title('1995/20a,V0,MLF')
ax.text(5, 500, V0_now_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
ax.text(5,400, V0_now_evap)
ax.text(5,300,V0_now_WT)
ax.plot(WT_20a_1995_Sw_V0['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_1995_Lw_V0['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_1995_Cv_V0['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_1995_Ev_V0['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_1995_Cd_V0['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])
ax.set_ylabel('W m-2', fontsize='small')
ax2 = ax.twinx()
ax2.plot(WT_20a_1995_V0['39.000'][-24:], linestyle='-', color = 'blue', label='WT')
ax2.set_ylim([18,29])

ax = fig.add_subplot(332)
ax.set_title('1995/20a,V70,MLF')
ax.text(5, 500, V70_now_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
ax.plot(WT_20a_1995_Sw_V70['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_1995_Lw_V70['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_1995_Cv_V70['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_1995_Ev_V70['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_1995_Cd_V70['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])
ax2 = ax.twinx()
ax2.plot(WT_20a_1995_V70['39.000'][-24:], linestyle='-', color = 'blue', label='WT')
ax2.set_ylim([18,29])

ax = fig.add_subplot(333)
ax.set_title('1995/20a,V100,MLF')
ax.text(5, 500, V100_now_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
ax.plot(WT_20a_1995_Sw_V100['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_1995_Lw_V100['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_1995_Cv_V100['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_1995_Ev_V100['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_1995_Cd_V100['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])
ax2 = ax.twinx()
ax2.plot(WT_20a_1995_V100['39.000'][-24:], linestyle='-', color = 'blue', label='WT')
ax2.set_ylim([18,29])


ax = fig.add_subplot(334)
ax.set_title('2085/20a,V0,MLF')
ax.text(5, 500, V0_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
#ax.text(5,400, V0_evap)
ax.text(5,300,V0_WT)
ax.text(5, 400, V0_Flow)
ax.plot(WT_20a_2085_Sw_V0['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V0['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V0['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V0['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V0['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])
ax.set_ylabel('W m-2', fontsize='small')
ax2 = ax.twinx()
ax2.plot(WT_20a_2085_V0['39.000'][-24:], linestyle='-', color = 'blue', label='WT')
ax2.set_ylim([18,29])
#plt.xlabel('time from episode start [h]', fontsize='small')
#plt.legend(loc=4, ncol=3, fontsize='small')
#plt.show()

ax = fig.add_subplot(335)

##ALL SUBGRAPHS: DFS20, 2085/20a, last day of the episode!
#plt.ylim([-750,750])
ax.set_title('2085/20a,V70,MLF')
ax.text(5, 500, V70_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
ax.text(5,300,V70_WT)
ax.plot(WT_20a_2085_Sw_V70['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V70['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V70['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V70['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V70['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylim([-750,750])
ax2 = ax.twinx()
ax2.plot(WT_20a_2085_V70['39.000'][-24:], linestyle='-', color = 'blue', label='WT')
ax2.set_ylim([18,29])
#plt.legend(loc=4, ncol=3, fontsize='small')

ax = fig.add_subplot(336)
ax.set_title('2085/20a,V100,MLF')
ax.text(5, 500, V100_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
ax.text(5,300,V100_WT)
ax.text(5, 400, V100_Flow)
ax.plot(WT_20a_2085_Sw_V100['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V100['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V100['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V100['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V100['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax2 = ax.twinx()
ax2.plot(WT_20a_2085_V100['39.000'][-24:], linestyle='-', color = 'blue', label='WT')
ax2.set_ylim([18,29])
ax.set_ylim([-750,750])


ax = fig.add_subplot(337)
ax.set_title('2085/20a,V0,MLF -15')
ax.text(5, 500, V0_085MLF_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
#ax.text(5,400, V0_085MLF_evap)
ax.text(5,300,V0_085MLF_WT)
ax.text(5, 400, V0_085MLF_Flow)
ax.plot(WT_20a_2085_Sw_V0_085MLF['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V0_085MLF['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V0_085MLF['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V0_085MLF['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V0_085MLF['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_ylabel('W m-2', fontsize='small')
ax.set_xlabel('time [h]', fontsize='small')
ax.set_ylim([-750,750])
ax2 = ax.twinx()
ax2.plot(WT_20a_2085_V0_085MLF['39.000'][-24:], linestyle='-', color = 'blue', label='WT')
ax2.set_ylim([18,29])

ax = fig.add_subplot(338)
ax.set_title('2085/20a,V70,MLF -15')
ax.text(5, 500, V70_085MLF_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
ax.text(5,300,V70_085MLF_WT)
ax.plot(WT_20a_2085_Sw_V70_085MLF['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V70_085MLF['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V70_085MLF['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V70_085MLF['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V70_085MLF['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_xlabel('time [h]', fontsize='small')
ax.set_ylim([-750,750])
ax2 = ax.twinx()
ax2.plot(WT_20a_2085_V70_085MLF['39.000'][-24:], linestyle='-', color = 'blue', label='WT')
ax2.set_ylim([18,29])

ax = fig.add_subplot(339)
ax.set_title('2085/20a,V100,MLF -15')
ax.text(5, 500, V100_085MLF_balance_s)#, horizontalalignment='right', verticalalignment='top')#, fontdict=None, withdash=False)
ax.text(5,300,V100_085MLF_WT)
ax.text(5, 400, V100_085MLF_Flow)
ax.plot(WT_20a_2085_Sw_V100_085MLF['39.000'][-24:], linestyle='-', color = 'yellow', label='Sw')
ax.plot(WT_20a_2085_Lw_V100_085MLF['39.000'][-24:], linestyle='-', color = 'orange', label='Lw')
ax.plot(WT_20a_2085_Cv_V100_085MLF['39.000'][-24:], linestyle='-', color = 'red', label='Cv')
ax.plot(WT_20a_2085_Ev_V100_085MLF['39.000'][-24:], linestyle='-', color = 'green', label='Ev')
ax.plot(WT_20a_2085_Cd_V100_085MLF['39.000'][-24:], linestyle='-', color = 'violet', label='Cd')
ax.set_xlabel('time [h]', fontsize='small')
ax.set_ylim([-750,750])
ax2 = ax.twinx()
ax2.plot(WT_20a_2085_V100_085MLF['39.000'][-24:], linestyle='-', color = 'blue', label='WT')
ax2.set_ylim([18,29])

plt.show()
