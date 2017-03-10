from Hs_scripts import hs_loader
from pylab import *
__author__ = 'lnx'
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#WT_2013 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_MLF_p/outputfiles_orig/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime')#, parse_dates='Datetime')
WT_20a_1995_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime')
WT_20a_1995_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V70_2013_MLF_p/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime')

WT_20a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime')
WT_20a_2085_V70 = pd.read_csv('/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime')

WT_20a_2085_V100_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S320_P_V100_2085_20a_085MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime')
WT_20a_2085_V70_085MLF = pd.read_csv('/home/lnx/PycharmProjects/HS/S321_P_V100_VD07_2085_20a_085MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime')


#print WT_20a_1995_V100.head()
#fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, sharex= True)

""""
fig = plt.figure()

ax = fig.add_subplot(231)
X = WT_20a_1995_V100.columns.values
Y = WT_20a_1995_V100.index.values
Z = WT_20a_1995_V100.values
Xi,Yi = np.meshgrid(X, Y)
CS = plt.contourf(Yi, Xi, Z, alpha=0.7, cmap=plt.cm.jet);
ax.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)
ax.colorbar(CS)
ax.title('Water temperature [degC, 1995/20a)')
ax.xlabel('time [days]')
ax.ylabel('distance from upstream model boundary [km]')

ax = fig.add_subplot(232)
X = WT_20a_2085_V100.columns.values
Y = WT_20a_2085_V100.index.values
Z = WT_20a_2085_V100.values
Xi,Yi = np.meshgrid(X, Y)
ax.contourf(Yi, Xi, Z, alpha=0.7, cmap=plt.cm.jet);
"""

contour_levels = arange(10, 30, 0.5)

#fig, ax = subplots(subplot_kw=dict(projection='polar'))
#cax = ax.contourf(thetas, r, values, contour_levels)
#cb1 = fig.colorbar(cax)

X = WT_20a_1995_V100.columns.values
Y = WT_20a_1995_V100.index.values
Z = WT_20a_1995_V100.values
Xi,Yi = np.meshgrid(X, Y)
CS = plt.contourf(Yi, Xi, Z, contour_levels, alpha=0.7, cmap=plt.cm.jet)
plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)
plt.colorbar(CS)
plt.title('Water temperature [degC] 1995/20a, V100, MLF')
plt.xlabel('time [days]')
plt.ylabel('distance from mouth [km]')
show()

X = WT_20a_2085_V100.columns.values
Y = WT_20a_2085_V100.index.values
Z = WT_20a_2085_V100.values
Xi,Yi = np.meshgrid(X, Y)
CS = plt.contourf(Yi, Xi, Z, contour_levels, alpha=0.7, cmap=plt.cm.jet);
plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)
plt.colorbar(CS)
plt.title('Water temperature [degC] 2085/20a, V100, MLF')
plt.xlabel('time [days]')
plt.ylabel('distance from mouth [km]')
show()

X = WT_20a_1995_V70.columns.values
Y = WT_20a_1995_V70.index.values
Z = WT_20a_1995_V70.values
Xi,Yi = np.meshgrid(X, Y)
CS = plt.contourf(Yi, Xi, Z, contour_levels, alpha=0.7, cmap=plt.cm.jet);
plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)
plt.colorbar(CS)
plt.title('Water temperature [degC] 1995/20a, V70, MLF')
plt.xlabel('time [days]')
plt.ylabel('distance from mouth [km]')
show()

X = WT_20a_2085_V70.columns.values
Y = WT_20a_2085_V70.index.values
Z = WT_20a_2085_V70.values
Xi,Yi = np.meshgrid(X, Y)
CS = plt.contourf(Yi, Xi, Z, contour_levels, alpha=0.7, cmap=plt.cm.jet);
plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)
plt.colorbar(CS)
plt.title('Water temperature [degC] 2085/20a, V70, MLF')
plt.xlabel('time [days]')
plt.ylabel('distance from mouth [km]')
show()

X = WT_20a_2085_V100_085MLF.columns.values
Y = WT_20a_2085_V100_085MLF.index.values
Z = WT_20a_2085_V100_085MLF.values
Xi,Yi = np.meshgrid(X, Y)
CS = plt.contourf(Yi, Xi, Z, contour_levels, alpha=0.7, cmap=plt.cm.jet);
plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)
plt.colorbar(CS)
plt.title('Water temperature [degC] 2085/20a, V100, MLF-15%')
plt.xlabel('time [days]')
plt.ylabel('distance from mouth [km]')
show()

X = WT_20a_2085_V70_085MLF.columns.values
Y = WT_20a_2085_V70_085MLF.index.values
Z = WT_20a_2085_V70_085MLF.values
Xi,Yi = np.meshgrid(X, Y)
CS = plt.contourf(Yi, Xi, Z, contour_levels, alpha=0.7, cmap=plt.cm.jet);
plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)
plt.colorbar(CS)
plt.title('Water temperature [degC] 2085/20a, V70, MLF-15%')
plt.xlabel('time [days]')
plt.ylabel('distance from mouth [km]')
show()