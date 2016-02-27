__author__ = 'lnx'

from pylab import *
import matplotlib.pyplot as plt
import pandas as pd
from Hs_scripts import hs_loader

VTS = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS = VTS.mean()
VTS_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS_V0 = VTS_V0.mean()
VTS_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS_V100 = VTS_V100.mean()

Sw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Sw_mean = Sw.mean()

Lw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw_mean = Lw.mean()

Cv = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_mean = Cv.mean()
Cv_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_20130804_08/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_mt_mean = Cv_mt.mean()

Ev = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_mean = Ev.mean()*(-1)
Ev_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_20130804_08/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_mt_mean = Ev_mt.mean()*(-1)

WT = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_mean = WT.mean()
WT_mt = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_m/outputfiles_20130804_08/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_mt_mean = WT_mt.mean()

filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08_acc/Temp_H2O_orig.txt'
name, header, data = hs_loader.loadfile(filename=filename)
data = pd.DataFrame(data)
data = data.set_index(0)
daily_max = data.resample('D', how ='max')
daily_mean = data.resample('D', how = 'mean')
sun_max = daily_max.iloc[4] #29 July = sunny
sun_mean = daily_mean.iloc[4]
cloud_max = daily_max.iloc[6] # 31.July = cloudy
cloud_mean = daily_mean.iloc[6]

writer_orig = pd.ExcelWriter('/home/lnx/simple.xlsx', engine='xlsxwriter')
daily_max.to_excel(writer_orig, index=False, sheet_name='report')
writer_orig.save()

#out = open('/home/lnx/daily_max_acc1.txt', 'w')
#out.write(daily_max)                               #file written ok, but not unicode characters?
#out.close()



#Rkm = WT.columns
Rkm = np.arange(13,64.5,0.5)
Rkm = pd.DataFrame(Rkm, columns=['Rkm'])
#meas_mean = [16.329,nan,nan,nan,nan,nan,18.604,nan,nan,nan,nan,nan,nan,nan,20.018,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.939,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.992,	nan,	nan,	nan,	nan,	22.596,	nan,	nan,	23.016,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.851,	nan,	nan,	nan,	nan,	nan,	22.494,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.478,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	23.134,	nan,	nan,	nan,	nan,	nan,	23.214, nan, nan, nan, nan] #mean 4. -8.Aug

fig = plt.figure()
#fig.set_size_inches(3.39,2.54)

#ax = fig.add_subplot(311)
#plt.title("4 - 8. Aug 2013, Pinka")
#ax.plot(Rkm, VTS, color='black', lw=0.5, label='STQ')
#ax.plot(Rkm, VTS_V0, color='black', linestyle='dotted', lw=0.5, label='V0')
#ax.plot(Rkm, VTS_V100, color='black', linestyle='dashed', lw=0.5, label='V100')
#plt.ylabel('view to sky')
#plt.legend(fontsize='small')

#ax = fig.add_subplot(312)
#ax.plot(Rkm, Sw_mean, color='orange', lw=0.5, label="Q_sw")
#ax.plot(Rkm, Lw_mean, color='violet', lw=0.5, label="Q_lw")
#ax.plot(Rkm, Ev_mean, color='green', lw=0.5, label="-LE, penman")
#ax.plot(Rkm, Ev_mt_mean, color='green', lw=0.5, linestyle='dashed', label="-LE, mass transfer")
#ax.plot(Rkm, Cv_mean, color='red', lw=0.5, label="H")
#ax.plot(xticks(fontsize='small')
#plt.ylabel('heat flux [W/m2]')
#plt.legend(fontsize='small')

ax = fig.add_subplot(313)
#ax.title("4 - 8. Aug 2013, Pinka")
ax.plot(Rkm, sun_max, color='orange', linestyle="solid", lw=0.5, label='Tmax acc_sun')
ax.plot(Rkm, cloud_max, color='blue', linestyle="solid", lw=0.5, label='Tmax acc_cloud')
ax.plot(Rkm, sun_mean, color='orange', linestyle="dashed", lw=0.5, label='Tmean acc_cloud')
ax.plot(Rkm, cloud_mean, color='blue', linestyle="dashed", lw=0.5, label='Tmean acc_cloud')



#ax.plot(Rkm, meas_mean, marker='x',color='blue', lw=0.5, label='measured')
plt.xlabel('distance from source')
plt.ylabel('water temperature [degC]')
plt.legend(fontsize='small')

#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure1_298.tiff')

plt.show()


