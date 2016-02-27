from Hs_scripts import hs_loader
from pylab import *
__author__ = 'lnx'
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import colorlover as cl
import scipy.stats as st
from datetime import datetime
from mpl_toolkits.axes_grid.anchored_artists import AnchoredText

#1)load file
filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Temp_H2O.txt'
#filename = "/home/lnx/PycharmProjects/HS/303_P500_STQ_2013_p/outputfiles/Temp_H2O.txt"
#filename = '/home/lnx/PycharmProjects/HS/304_P500_V0_2013_p/outputfiles/Temp_H2O.txt'
#WT_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/305_P500_V100_2013_p/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')#, index_col='Datetime', parse_dates="Datetime")

filename = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Temp_H2O.txt', skiprows=6, sep='\s+')#, index_col='Datetime', parse_dates="Datetime")

data = filename.loc[filename.Name == "WT_STQ"]

#2)prepare y axis
#date_time = [i[0] for i in data]
#date_time = np.array(date_time).transpose
y = [i for i in range(1, 385, 1)]                                     #384 hours from 25 July 0h - 09 August 2013 23h

#3)prepare x axis
x = np.arange(13, 64.5, 0.5)               # DFM: 89,38, len=103

X, Y = np.meshgrid(x,y)

#4)prepare z axis
positions = np.vstack([X.ravel(),Y.ravel()])
values = np.stack(WT_STQ)

Z = np.reshape(values(positions).T, X.shape)

print Z


#6)contour

fig = plt.figure()
CS = plt.contourf(X,Y,Z) #, V, cmap=mpl.cm.jet)                               #oder N?
plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10, color='black')
plt.colorbar(CS)
#plt.title('Convection [ ' $W/m2$ ' ], 1 July 2013, Pinka, %s', name)     #TODO: $$ und %s geht leider nicht
plt.title('Water temperature degC, Pinka, penman, V0')
plt.xlabel('distance from upstream model boundary [km]')
plt.ylabel('time[h]')
plt.yticks(date_time)
#plt.legend()

show()



