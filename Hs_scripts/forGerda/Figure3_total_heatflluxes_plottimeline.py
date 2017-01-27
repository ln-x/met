__author__ = 'lnx'

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

Sw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_fricvelWindVTS_sed1m/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
#Ev = Ev*(-1)
Ev_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_fricvelWindVTS_sed1m/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
#Ev_mt = Ev_mt*(-1)
Cd = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_Cond.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Bilanz = Sw + Lw + Cv + Cd + Ev
#Bilanz_mt = Sw + Lw + Cv_mt + Cd + Ev_mt

fig = plt.figure()
plt.ylim([-750,750])
plt.plot(Bilanz['65.500'], linestyle='-', color = 'black', label='Bal')
#plt.plot(Bilanz_mt['51.000'], linestyle='--', color = 'black', label='Bal_mt')
plt.plot(Lw['65.500'], linestyle='-', color = 'orange', label='Lw')
plt.plot(Sw['65.500'], linestyle='-', color = 'yellow', label='Sw')
plt.plot(Cv['65.500'], linestyle='-', color = 'red', label='Cv')
#plt.plot(Cv_mt['61.000'], linestyle='--', color = 'red', label='Cv_mt')
plt.plot(Ev['65.500'], linestyle='-', color = 'green', label='Ev')
#plt.plot(Ev_mt['61.000'], linestyle='--', color = 'green', linewidth=2.0, label='Ev_mt')
plt.plot(Cd['65.500'], linestyle='-', color = 'violet', label='Cd')

plt.ylabel('W m-2', fontsize='small')
plt.xlabel('time from episode start [h]', fontsize='small')

plt.legend(loc=4, ncol=3, fontsize='small')

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Heatfluxes_DFM65_5.tiff')

plt.show()



