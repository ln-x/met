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

Sw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Sw_mean = Sw.mean()

Lw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw_mean = Lw.mean()

Cv = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_mean = Cv.mean()
Cv_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_fricvelWindVTS_sed1m/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_mt_mean = Cv_mt.mean()

Ev = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_mean = Ev.mean()*(-1)
Ev_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_fricvelWindVTS_sed1m/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_mt_mean = Ev_mt.mean()*(-1)

WT = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_mean = WT.mean()
WT_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_fricvelWindVTS_sed1m/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_mt_mean = WT_mt.mean()

#Rkm = WT.columns
Rkm = np.arange(13,64.5,0.5)
#print len(Rkm)
Rkm = pd.DataFrame(Rkm, columns=['Rkm'])
print Rkm

#meas_min = [12.787,	nan	,nan,	nan,	nan,	nan,	nan,	nan,	nan,	13.558,	nan,	nan,	nan,	nan,	nan,	nan,	nan	nan	14.325	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	16.332	nan	nan	nan	nan	nan	nan	nan	16.808	nan	nan	nan	nan	17.284	nan	nan	17.189	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	17.284	nan	nan	nan	nan	nan	18.426	nan	nan	nan	nan	nan	nan	nan	nan	nan	18.996	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	18.331	nan	nan	nan	nan	nan	18.426
meas_mean = [15.6400807292,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	17.78446875,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	19.3895416667,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.17528125,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.3037604167,	nan,	nan,	nan,	nan,	22.0474713542,	nan,	nan,	22.3981354167,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	20.5911901042,	nan,	22.6211927083,	nan,	nan,	nan,	nan,	nan,	22.2223671875,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.80021875,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.5628932292,	nan,	nan,	nan,	nan,	nan,	22.59508854170]
#meas_max = [19.472	nan	nan	nan	nan	nan	nan	nan	nan	24.158	nan	nan	nan	nan	nan	nan	nan	nan	26.683	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	25.805	nan	nan	nan	nan	nan	nan	nan	24.835	nan	nan	nan	nan	29.252	nan	nan	28.754	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	26.781	nan	27.272	nan	nan	nan	nan	nan	25.416	nan	nan	nan	nan	nan	nan	nan	nan	nan	23.966	nan	nan	nan	nan	nan	nan	nan	nan	nan	nan	27.075	nan	nan	nan	nan	nan	27.075

print meas_mean

fig = plt.figure()
#fig.set_size_inches(3.39,2.54)


ax = fig.add_subplot(311)
plt.title("1 July  - 29. Aug 2013, Pinka")
ax.plot(Rkm, VTS, color='black', lw=0.5, label='STQ')
ax.plot(Rkm, VTS_V0, color='black', linestyle='dotted', lw=0.5, label='V0')
ax.plot(Rkm, VTS_V100, color='black', linestyle='dashed', lw=0.5, label='V100')
plt.ylabel('view to sky')
plt.legend(fontsize='small')

ax = fig.add_subplot(312)
ax.plot(Rkm, Sw_mean, color='orange', lw=0.5, label="Q_sw")
ax.plot(Rkm, Lw_mean, color='violet', lw=0.5, label="Q_lw")
ax.plot(Rkm, Ev_mean, color='green', lw=0.5, label="-LE, penman")
ax.plot(Rkm, Ev_mt_mean, color='green', lw=0.5, linestyle='dashed', label="-LE, mass transfer")
ax.plot(Rkm, Cv_mean, color='red', lw=0.5, label="H")
#ax.plot(xticks(fontsize='small')
#ax.plot(Rkm, Cv_mean, color='black',linestyle='dashed', lw=0.5, label="H, mass transfer") #same as penman
plt.ylabel('heat flux [W/m2]')
plt.legend(fontsize='small')

ax = fig.add_subplot(313)
ax.plot(Rkm, WT_mean, color='blue', lw=0.5, label='penman')
ax.plot(Rkm, WT_mt_mean, color='blue', linestyle="dashed", lw=0.5, label='mass transfer')
ax.plot(Rkm, meas_mean, marker='x',color='blue', lw=0.5, label='measured')
plt.xlabel('distance from source')
plt.ylabel('water temperature [degC]')
plt.legend(fontsize='small')

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure1_298p1.tiff')

plt.show()


#meas = DataFrame({'Rkm':['13.0','17.5','22.0','33.0','37.0','39.5','41.0','47.5','50.5','61.0','64.0'],'WT_meas':
#    [15.6400807292,17.78446875,19.3895416667,21.17528125,21.3037604167,22.0474713542,22.3981354167,22.6211927083,22.2223671875,22.5628932292,22.5950885417]}) #mean 20130725-0809

#13:15.6400807292,17.5: 17.78446875,	22:19.3895416667,33: 21.17528125,37:21.3037604167,39.5:22.0474713542,41:22.3981354167,
#47.5:22.6211927083,	50.5:22.2223671875,61:22.5628932292,64:22.5950885417}

#meas1= pd.concat([Rkm,meas], axis=1, join='outer', keys=['Rkm'])
#meas1 = pd.merge(Rkm,meas) #,on='Rkm')#, how='outer')

#print meas1

#meas = {15.6400807292, nan, nan, 17.5: 17.78446875,	22:19.3895416667,33: 21.17528125,37:21.3037604167,39.5:22.0474713542,41:22.3981354167,
#47.5:22.6211927083,	50.5:22.2223671875,61:22.5628932292,64:22.5950885417} #mean 20130725-0809

#meas_index = {stationcode:(DFM,DRS),HB:(89,13),TB:(84.5:17.5), SD:(80,22), RD:(69,33), OO:(65,37),UO:(62.5,39.5),
#            UW:(61,41),J1:(55.5,46.5),J2:(55,47),J3:(54.5,47.5), J4:(51.5,50.5), Z1:(47,55),BD:(45,57),WD:(41,61),BG:(38,64)}

#print meas.keys()