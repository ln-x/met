__author__ = 'lnx'

from Hs_scripts import hs_loader
from pylab import *
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd

#filename = "/home/lnx/PycharmProjects/HS/049/outputfiles_newConv_elevcorr_incacloud_start89_masstransfer/Heat_Conv.txt"
#name, header, thedata = hs_loader.loadfile(filename=filename)
#print 'loaded: ', name

VTS = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS = VTS.mean()

Sw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Sw_mean = Sw.mean()

Lw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw_mean = Lw.mean()

Cv = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_mean = Cv.mean()

Ev = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_mean = Ev.mean()*(-1)

WT = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_mean = WT.mean()

#Rkm = WT.columns
Rkm = np.arange(13,64.5,0.5)
print len(Rkm)

meas = {13:15.6400807292,17.5: 17.78446875,	22:19.3895416667,33: 21.17528125,37:21.3037604167,39.5:22.0474713542,41:22.3981354167,
47.5:22.6211927083,	50.5:22.2223671875,61:22.5628932292,64:22.5950885417} #mean 20130725-0809


#meas_index = {stationcode:(DFM,DRS),HB:(89,13),TB:(84.5:17.5), SD:(80,22), RD:(69,33), OO:(65,37),UO:(62.5,39.5),
#            UW:(61,41),J1:(55.5,46.5),J2:(55,47),J3:(54.5,47.5), J4:(51.5,50.5), Z1:(47,55),BD:(45,57),WD:(41,61),BG:(38,64)}

print meas.keys()

fig = plt.figure()
plt.title("1 July  - 29. Aug 2013, Pinka")

ax = fig.add_subplot(311)
ax.plot(Rkm, VTS, color='black', lw=0.5)
plt.ylabel('view to sky')

ax = fig.add_subplot(312)
ax.plot(Rkm, Sw_mean, color='orange', lw=0.5, label="short wave heat flux")
ax.plot(Rkm, Lw_mean, color='violet', lw=0.5, label="long wave heat flux")
ax.plot(Rkm, Ev_mean, color='green', lw=0.5, label="latent heat flux * (-1)")
ax.plot(Rkm, Cv_mean, color='red', lw=0.5, label="sensible heat flux")
plt.legend()
plt.ylabel('heat flux [W/m2]')

ax = fig.add_subplot(313)
ax.plot(Rkm, WT_mean, color='blue', lw=0.5)
ax.scatter(meas.keys, meas, marker='o',color='blue', lw=0.5)
plt.ylabel('water temperature [degC]')

plt.xlabel('distance from source')
fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure1_298p1.png')

plt.show()
