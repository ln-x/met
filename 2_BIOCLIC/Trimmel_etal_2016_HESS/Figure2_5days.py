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
#print len(Sw)
#Sw = Sw_1.ix[240:359] #.drop(['Datetime'],axis=1)  #cut only 5 max days
#Sw = Sw.ix[:120]
#print len(Sw)
#print Sw.tail()
Sw_mean = Sw.mean()
#print len(Sw_mean)

print 'Sw=', Sw_mean.describe()


Lw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
#Lw = Lw.ix[240:] #cut only 5 max days
Lw_mean = Lw.mean()

print 'Lw=', Lw_mean.describe()


Cv = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
#Cv = Cv.ix[240:] #cut only 5 max days
Cv_mean = Cv.mean()
Cv_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_20130804_08/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
#Cv_mt = Cv_mt.ix[240:] #cut only 5 max days
Cv_mt_mean = Cv_mt.mean()

print 'Cv_p=', Cv_mean.describe()


Ev = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
#Ev = Ev.ix[240:] #cut only 5 max days
Ev_mean = Ev.mean()*(-1)
Ev_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_20130804_08/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
#Ev_mt = Ev_mt.ix[240:] #cut only 5 max days
Ev_mt_mean = Ev_mt.mean()*(-1)

print 'Ev_p=', Ev_mean.describe()
print 'Ev_mt=', Ev_mt_mean.describe()


WT = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
#WT = WT.ix[240:] #cut only 5 max days
WT_mean = WT.mean()
WT_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_20130804_08/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
#WT_mt = WT_mt.ix[240:] #cut only 5 max days
WT_mt_mean = WT_mt.mean()

print 'WT_p=', WT_mean.describe()
print 'WT_p_total=', pd.DataFrame(WT).describe()

print 'WT_mt=', WT_mt_mean.describe()

#WT_new = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08_heatwaveoffset/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime')
#WT_new_mean = WT_new.mean()

#WT_newBW = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08_heatwaveoffset/Temp_H2O_corrBW.txt', skiprows=6, sep='\s+', index_col='Datetime')
#WT_newBW_mean = WT_newBW.mean()

#WT_newBW2 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08_heatwaveoffset2_corrBW/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime')
#WT_newBW2_mean = WT_newBW2.mean()

#WT_acc = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08_acc/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime')
#WT_acc_mean = WT_acc.mean()



#Rkm = WT.columns
Rkm = np.arange(13,64.5,0.5)
#print len(Rkm)
Rkm = pd.DataFrame(Rkm, columns=['Rkm'])
#print Rkm
print len(Rkm)


#meas_min = [12.787,	nan	,nan,	nan,	nan,	nan,	nan,	nan,	nan,	13.558,	nan,	nan,	nan,	nan,	nan,	nan,	nan	nan	14.325	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	16.332	nan	nan	nan	nan	nan	nan	nan	16.808	nan	nan	nan	nan	17.284	nan	nan	17.189	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	17.284	nan	nan	nan	nan	nan	18.426	nan	nan	nan	nan	nan	nan	nan	nan	nan	18.996	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	18.331	nan	nan	nan	nan	nan	18.426
#meas_mean = [15.6400807292,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	17.78446875,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	19.3895416667,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.17528125,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.3037604167,	nan,	nan,	nan,	nan,	22.0474713542,	nan,	nan,	22.3981354167,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	20.5911901042,	nan,	22.6211927083,	nan,	nan,	nan,	nan,	nan,	22.2223671875,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.80021875,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.5628932292,	nan,	nan,	nan,	nan,	nan,	22.59508854170] #mean 14day period
#orig 5 days:  meas_mean = [16.329,nan,nan,nan,nan,18.604,nan,nan,nan,nan,nan,nan,nan,nan,20.018,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.939,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.992,	nan,	nan,	nan,	nan,	22.596,	nan,	nan,	23.057,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.7914,	nan,	23.251,	nan,	nan,	nan,	nan,	nan,	22.494,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.478,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	23.134,	nan,	nan,	nan,	nan,	nan,	23.214, nan, nan, nan, nan] #mean 4. -8.Aug
meas_mean = [16.329,nan,nan,nan,nan,nan,18.604,nan,nan,nan,nan,nan,nan,nan,20.018,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.939,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.992,	nan,	nan,	nan,	nan,	22.596,	nan,	nan,	23.016,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.851,	nan,	nan,	nan,	nan,	nan,	22.494,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.478,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	23.134,	nan,	nan,	nan,	nan,	nan,	23.214, nan, nan, nan, nan] #mean 4. -8.Aug

#meas_mean = [16.329,nan,nan,nan,nan,nan,nan,nan,nan,18.604,nan,nan,nan,nan,nan,nan,nan,nan,20.018,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.939,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.992,	nan,	nan,	nan,	nan,	22.596,	nan,	nan,	23.057,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.7914,	nan,	23.251,	nan,	nan,	nan,	nan,	nan,	22.494,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.478,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	23.134,	nan,	nan,	nan,	nan,	nan,	23.134] #mean 4. -9.Aug
print len(meas_mean)
#meas_max = [19.472	nan	nan	nan	nan	nan	nan	nan	nan	24.158	nan	nan	nan	nan	nan	nan	nan	nan	26.683	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	25.805	nan	nan	nan	nan	nan	nan	nan	24.835	nan	nan	nan	nan	29.252	nan	nan	28.754	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	26.781	nan	27.272	nan	nan	nan	nan	nan	25.416	nan	nan	nan	nan	nan	nan	nan	nan	nan	23.966	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	27.075	nan	nan	nan	nan	nan	27.075

meas_mean = pd.Series(meas_mean)

print 'WT_meas=', meas_mean.describe()

fig = plt.figure()
#fig.set_size_inches(3.39,2.54)

ax = fig.add_subplot(311)
plt.title("4-8 August 2013, Pinka")
ax.plot(Rkm, VTS, color='black', lw=0.5, label='STQ')
ax.plot(Rkm, VTS_V0, color='black', linestyle='dotted', lw=0.5, label='V0')
ax.plot(Rkm, VTS_V100, color='black', linestyle='dashed', lw=0.5, label='V100')
plt.ylabel('view to sky')
plt.legend(fontsize='small')

ax = fig.add_subplot(312)
ax.plot(Rkm, Sw_mean, color='orange', lw=0.5, label="Q_sw")
ax.plot(Rkm, Lw_mean, color='violet', lw=0.5, label="Q_lw")
ax.plot(Rkm, Ev_mean, color='#1b9e77', lw=0.5, label="-LE, penman")
ax.plot(Rkm, Ev_mt_mean, color='#1b9e77', lw=0.5, linestyle='dashed', label="-LE, mass transfer")
ax.plot(Rkm, Cv_mean, color='#d95f02', lw=0.5, label="H")
#ax.plot(xticks(fontsize='small')
#ax.plot(Rkm, Cv_mean, color='black',linestyle='dashed', lw=0.5, label="H, mass transfer") #same as penman
plt.ylabel('energy flux [W m-2]')
plt.legend(fontsize='small')

ax = fig.add_subplot(313)
ax.plot(Rkm, WT_mean, color='blue', lw=0.5, label='penman')
ax.plot(Rkm, WT_mt_mean, color='blue', linestyle="dashed", lw=0.5, label='mass transfer')
#ax.plot(Rkm, WT_new_mean, color='green', linestyle="dashed", lw=0.5, label='new')
#ax.plot(Rkm, WT_newBW_mean, color='red', linestyle="dashed", lw=0.5, label='newBW')
#ax.plot(Rkm, WT_newBW2_mean, color='red', linestyle="dashed", lw=0.5, label='newBW')
#ax.plot(Rkm, WT_acc_mean, color='orange', linestyle="dashed", lw=0.5, label='acc')


ax.plot(Rkm, meas_mean, marker='x',color='blue', lw=0.5, label='measured')
plt.xlabel('distance from source')
plt.ylabel('water temperature [degC]')
plt.legend(fontsize='small')

#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure1_298p1.tiff')

plt.show()


