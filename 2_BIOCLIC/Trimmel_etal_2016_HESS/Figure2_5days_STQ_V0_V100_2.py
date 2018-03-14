__author__ = 'lnx'

from pylab import *
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame

VTS = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS = VTS.mean()
VTS_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS_V0 = VTS_V0.mean()
VTS_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS_V100 = VTS_V100.mean()

Sw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Sw_mean = Sw.mean()
Sw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Sw_V0_mean = Sw_V0.mean()
Sw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Sw_V100_mean = Sw_V100.mean()

print 'Sw=', Sw_mean.describe()


Lw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw_mean = Lw.mean()
Lw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw_V0_mean = Lw_V0.mean()
Lw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw_V100_mean = Lw_V100.mean()

print 'Lw=', Lw_mean.describe()


Cv = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_mean = Cv.mean()
Cv_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_V0_mean = Cv_V0.mean()
Cv_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_V100_mean = Cv_V100.mean()

print 'Cv_p=', Cv_mean.describe()


Ev = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_mean = Ev.mean() #*(-1)
Ev_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_V0_mean = Ev_V0.mean() #*(-1)
Ev_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_V100_mean = Ev_V100.mean() #*(-1)

#print 'Ev_p=', Ev_mean.describe()
#print 'Ev_mt=', Ev_mt_mean.describe()


WT = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_mean = WT.mean()
WT_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_V0_mean = WT_V0.mean()
WT_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_V100_mean = WT_V100.mean()

#print 'WT_p=', WT_mean.describe()
#print 'WT_p_total=', pd.DataFrame(WT).describe()
#print 'WT_V0=', WT_V0_mean.describe()

Rkm = np.arange(13,64.5,0.5)
Rkm = pd.DataFrame(Rkm, columns=['Rkm'])
print len(Rkm)

meas_mean = [16.329,nan,nan,nan,nan,nan,18.604,nan,nan,nan,nan,nan,nan,nan,20.018,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.939,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.992,	nan,	nan,	nan,	nan,	22.596,	nan,	nan,	23.016,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.851,	nan,	nan,	nan,	nan,	nan,	22.494,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.478,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	23.134,	nan,	nan,	nan,	nan,	nan,	23.214, nan, nan, nan, nan] #mean 4. -8.Aug

print len(meas_mean)

meas_mean = pd.Series(meas_mean)

print 'WT_meas=', meas_mean.describe()

fig = plt.figure()
#fig.set_size_inches(3.39,2.54)

ax = fig.add_subplot(411)
plt.title("4-8 August 2013, Pinka")
ax.plot(Rkm, Sw_V0_mean, color='orange', lw=0.5, linestyle="dashed", label="Q_sw, V0")
ax.plot(Rkm, Lw_V0_mean, color='violet', lw=0.5, linestyle="dashed", label="Q_lw, V0")
ax.plot(Rkm, Ev_V0_mean, color='#1b9e77', lw=0.5, linestyle='dashed', label="LE, V0")
ax.plot(Rkm, Cv_V0_mean, color='#d95f02', lw=0.5, linestyle="dashed", label="H, V0")
#plt.ylabel('energy flux [W m-2]')
plt.legend(fontsize='small')

ax = fig.add_subplot(412)
ax.plot(Rkm, Sw_mean, color='orange', lw=0.5, label="Q_sw, STQ")
ax.plot(Rkm, Lw_mean, color='violet', lw=0.5, label="Q_lw, STQ")
ax.plot(Rkm, Ev_mean, color='#1b9e77', lw=0.5, label="LE, STQ")
ax.plot(Rkm, Cv_mean, color='#d95f02', lw=0.5, label="H, STQ")
plt.ylabel('energy flux [W m-2]')
plt.legend(fontsize='small')

ax = fig.add_subplot(413)
ax.plot(Rkm, Sw_V100_mean, color='orange', lw=0.5, label="Q_sw, V100")
ax.plot(Rkm, Lw_V100_mean, color='violet', lw=0.5, label="Q_lw, V100")
ax.plot(Rkm, Ev_V100_mean, color='#1b9e77', lw=0.5, linestyle='solid', label="LE, V100")
ax.plot(Rkm, Cv_V100_mean, color='#d95f02', lw=0.5, label="H, V100")
#plt.ylabel('energy flux [W m-2]')
plt.legend(fontsize='small')

ax = fig.add_subplot(414)
ax.plot(Rkm, WT_mean, color='blue', lw=0.5, label='STQ')
ax.plot(Rkm, WT_V0_mean, color='blue', linestyle="dashed", lw=0.5, label='V0')
ax.plot(Rkm, WT_V100_mean, color='blue', linestyle="solid", lw=1.0, label='V100')

ax.plot(Rkm, meas_mean, marker='x',color='blue', lw=0.5, label='measured')
plt.xlabel('distance from source')
plt.ylabel('water temperature [degC]')
plt.legend(fontsize='small')

#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure1_298p1.tiff')

plt.show()


