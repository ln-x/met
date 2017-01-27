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
print 'Sw_V0=', Sw_V0_mean.describe()
print 'Sw_V100=', Sw_V100_mean.describe()


Lw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw_mean = Lw.mean()
Lw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw_V0_mean = Lw_V0.mean()
Lw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw_V100_mean = Lw_V100.mean()

print 'Lw=', Lw_mean.describe()
print 'Lw_V0=', Lw_V0_mean.describe()
print 'Lw_V100=', Lw_V100_mean.describe()

Cv = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_mean = Cv.mean()
Cv_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_V0_mean = Cv_V0.mean()
Cv_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_V100_mean = Cv_V100.mean()

print 'Cv=', Cv_mean.describe()
print 'Cv_V0=', Cv_V0_mean.describe()
print 'Cv_V100=', Cv_V100_mean.describe()

Ev = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_mean = Ev.mean() #*(-1)
Ev_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_V0_mean = Ev_V0.mean() #*(-1)
Ev_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_V100_mean = Ev_V100.mean() #*(-1)

print 'Ev=', Ev_mean.describe()
print 'Ev_V0=', Ev_V0_mean.describe()
print 'Ev_V100=', Ev_V100_mean.describe()

Cd = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_Cond.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cd_mean = Cd.mean() #*(-1)
Cd_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_Cond.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cd_V0_mean = Cd_V0.mean() #*(-1)
Cd_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_Cond.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cd_V100_mean = Cd_V100.mean() #*(-1)

print 'Cd=', Cd_mean.describe()
print 'Cd_V0=', Cd_V0_mean.describe()
print 'Cd_V100=', Cd_V100_mean.describe()
#print 'Ev_p=', Ev_mean.describe()
#print 'Ev_mt=', Ev_mt_mean.describe()

Bal_V0_mean = Sw_V0_mean + Lw_V0_mean + Cv_V0_mean + Ev_V0_mean + Cd_V0_mean
Bal_mean = Sw_mean + Lw_mean + Cv_mean + Ev_mean + Cd_mean
Bal_V100_mean = Sw_V100_mean + Lw_V100_mean + Cv_V100_mean + Ev_V100_mean + Cd_V100_mean


print 'Bal_mean=', Bal_mean.describe()
print 'Bal_V0=', Bal_V0_mean.describe()
print 'Bal_V100=', Bal_V100_mean.describe()

Sum = Cd_mean.mean()+ Cv_mean.mean()+ Sw_mean.mean()+ Lw_mean.mean()
Sum0 = Cd_V0_mean.mean()+ Cv_V0_mean.mean()+ Sw_V0_mean.mean()+ Lw_V0_mean.mean()
Sum1 = Cd_V100_mean.mean()+ Cv_V100_mean.mean()+ Sw_V100_mean.mean()+ Lw_V100_mean.mean()


print 'percentage of Sw,Lw,Cv,Cd (STQ):', Sw_mean.mean()/Sum,Lw_mean.mean()/Sum,Cv_mean.mean()/Sum,Cd_mean.mean()/Sum
print 'percentage of Sw,Lw,Cv,Cd (V0):', Sw_V0_mean.mean()/Sum0,Lw_V0_mean.mean()/Sum0,Cv_V0_mean.mean()/Sum0,Cd_V0_mean.mean()/Sum0
print 'percentage of Sw,Lw,Cv,Cd (V100):', Sw_V100_mean.mean()/Sum1,Lw_V100_mean.mean()/Sum1,Cv_V100_mean.mean()/Sum1,Cd_V100_mean.mean()/Sum1


WT = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_mean = WT.mean()
WT_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_V0_mean = WT_V0.mean()
WT_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_V100_mean = WT_V100.mean()

print 'WT=', WT_mean.describe()
print 'WT_V0=', WT_V0_mean.describe()
print 'WT_V100=', WT_V100_mean.describe()

#print 'WT_p_total=', pd.DataFrame(WT).describe()
#print 'WT_V0=', WT_V0_mean.describe()


exit()

Rkm = np.arange(13,64.5,0.5)
Rkm = pd.DataFrame(Rkm, columns=['Rkm'])
print len(Rkm)

meas_mean = [16.329,nan,nan,nan,nan,nan,18.604,nan,nan,nan,nan,nan,nan,nan,20.018,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.939,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.992,	nan,	nan,	nan,	nan,	22.596,	nan,	nan,	23.016,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.851,	nan,	nan,	nan,	nan,	nan,	22.494,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.478,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	23.134,	nan,	nan,	nan,	nan,	nan,	23.214, nan, nan, nan, nan] #mean 4. -8.Aug

#print len(meas_mean)
#meas_mean = pd.Series(meas_mean)
#print 'WT_meas=', meas_mean.describe()

fig = plt.figure()
#fig.set_size_inches(3.39,2.54)

ax = fig.add_subplot(711)
plt.title("4-8 August 2013, Pinka")
ax.plot(Rkm, Sw_V0_mean, color='black', lw=0.5, linestyle="dashed", label="Q_sw, V0")
ax.plot(Rkm, Sw_mean, color='black', lw=0.5, label="Q_sw, STQ")
ax.plot(Rkm, Sw_V100_mean, color='black', lw=1.0, label="Q_sw, V100")
#plt.ylabel('energy flux [W m-2]')
plt.legend(fontsize='small')

ax = fig.add_subplot(712)
ax.plot(Rkm, Lw_V0_mean, color='black', lw=0.5, linestyle="dashed", label="Q_lw, V0")
ax.plot(Rkm, Lw_mean, color='black', lw=0.5, label="Q_lw, STQ")
ax.plot(Rkm, Lw_V100_mean, color='black', lw=1.0, label="Q_lw, V100")
plt.ylabel('energy flux [W m-2]')
plt.legend(fontsize='small')

ax = fig.add_subplot(713)
ax.plot(Rkm, Ev_V0_mean, color='black', lw=0.5, linestyle='dashed', label="LE, V0")
ax.plot(Rkm, Ev_mean, color='black', lw=0.5, label="LE, STQ")
ax.plot(Rkm, Ev_V100_mean, color='black', lw=1.0, linestyle='solid', label="LE, V100")
#plt.ylabel('energy flux [W m-2]')
plt.legend(fontsize='small')

ax = fig.add_subplot(714)
ax.plot(Rkm, Cv_V0_mean, color='black', lw=0.5, linestyle="dashed", label="H, V0")
ax.plot(Rkm, Cv_mean, color='black', lw=0.5, label="H, STQ")
ax.plot(Rkm, Cv_V100_mean, color='black', lw=1.0, label="H, V100")
plt.legend(fontsize='small')

ax = fig.add_subplot(715)
ax.plot(Rkm, Cd_V0_mean, color='black', lw=0.5, linestyle="dashed", label="Cd, V0")
ax.plot(Rkm, Cd_mean, color='black', lw=0.5, label="Cd, STQ")
ax.plot(Rkm, Cd_V100_mean, color='black', lw=1.0, label="Cd, V100")
plt.legend(fontsize='small')

ax = fig.add_subplot(716)
ax.plot(Rkm, Bal_V0_mean, color='black', lw=0.5, linestyle="dashed", label="Bal, V0")
ax.plot(Rkm, Bal_mean, color='black', lw=0.5, label="Bal, STQ")
ax.plot(Rkm, Bal_V100_mean, color='black', lw=1.0, label="Bal, V100")

ax = fig.add_subplot(717)
ax.plot(Rkm, WT_mean, color='blue', lw=0.5, label='STQ')
ax.plot(Rkm, WT_V0_mean, color='blue', linestyle="dashed", lw=0.5, label='V0')
ax.plot(Rkm, WT_V100_mean, color='blue', linestyle="solid", lw=1.0, label='V100')
ax.plot(Rkm, meas_mean, marker='x',color='blue', lw=0.5, label='measured')
plt.xlabel('distance from source')
plt.ylabel('water temperature [degC]')
plt.legend(fontsize='small')

plt.xlabel('distance from source')
plt.legend(fontsize='small')

#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure1_298p1.tiff')

plt.show()


