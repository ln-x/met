__author__ = 'lnx'

from pylab import *
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame

VTS = pd.read_csv('/home/lnx/PycharmProjeprint 'Sw=', Sw_mean.describe()
cts/HS/S250_P_STQ_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS = VTS.mean()
VTS_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS_V0 = VTS_V0.mean()
VTS_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS_V100 = VTS_V100.mean()

print 'VTS=', VTS.describe()
print 'VTS_V0=', VTS_V0.describe()
print 'VTS_V100=', VTS_V100.describe()

Sw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Sw_mean = Sw.mean()

print 'Sw=', Sw_mean.describe()


Lw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw_mean = Lw.mean()

print 'Lw=', Lw_mean.describe()

Cv = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_mean = Cv.mean()
Cv_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_fricvelWindVTS_sed1m/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_mt_mean = Cv_mt.mean()

print 'Cv_p=', Cv_mean.describe()

Ev = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_mean = Ev.mean()*(-1)
Ev_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_fricvelWindVTS_sed1m/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_mt_mean = Ev_mt.mean()*(-1)

print 'Ev_p=', Ev_mean.describe()
print 'Ev_mt=', Ev_mt_mean.describe()

WT = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_mean = WT.mean()
WT = np.array(WT)
WT = WT.ravel()

WT_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_fricvelWindVTS_sed1m/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_mt_mean = WT_mt.mean()

print 'WT_p=', WT_mean.describe()
print 'WT_p_total=', pd.DataFrame(WT).describe()

print 'WT_mt=', WT_mt_mean.describe()


#Rkm = WT.columns
Rkm = np.arange(13,64.5,0.5)
#print len(Rkm)
Rkm = pd.DataFrame(Rkm, columns=['Rkm'])
#print Rkm

#meas_min = [12.787,	nan	,nan,	nan,	nan,	nan,	nan,	nan,	nan,	13.558,	nan,	nan,	nan,	nan,	nan,	nan,	nan	nan	14.325	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	16.332	nan	nan	nan	nan	nan	nan	nan	16.808	nan	nan	nan	nan	17.284	nan	nan	17.189	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	17.284	nan	nan	nan	nan	nan	18.426	nan	nan	nan	nan	nan	nan	nan	nan	nan	18.996	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	18.331	nan	nan	nan	nan	nan	18.426
meas_mean = [15.6400807292,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	17.78446875,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	19.3895416667,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.17528125,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.3037604167,	nan,	nan,	nan,	nan,	22.0474713542,	nan,	nan,	22.3981354167,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	20.5911901042,	nan,	22.6211927083,	nan,	nan,	nan,	nan,	nan,	22.2223671875,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.80021875,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.5628932292,	nan,	nan,	nan,	nan,	nan,	22.59508854170]
#meas_max = [19.472	nan	nan	nan	nan	nan	nan	nan	nan	24.158	nan	nan	nan	nan	nan	nan	nan	nan	26.683	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	25.805	nan	nan	nan	nan	nan	nan	nan	24.835	nan	nan	nan	nan	29.252	nan	nan	28.754	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	26.781	nan	27.272	nan	nan	nan	nan	nan	25.416	nan	nan	nan	nan	nan	nan	nan	nan	nan	23.966	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	27.075	nan	nan	nan	nan	nan	27.075

meas_mean = pd.Series(meas_mean)

print 'WT_meas=', meas_mean.describe()


print
