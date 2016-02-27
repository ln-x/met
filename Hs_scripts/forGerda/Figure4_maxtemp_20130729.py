__author__ = 'lnx'
from Hs_scripts import hs_loader
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import pandas as pd

#WT = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Temp_H2O.txt', skiprows=6, sep='\s+')#, index_col='Datetime', parse_dates="Datetime")
filename = '/home/lnx/PycharmProjects/HS/303_P500_STQ_2013_p/outputfiles/Temp_H2O.txt'
filename_I0 = '/home/lnx/PycharmProjects/HS/303_P500_STQ_2013_p_noinflows/outputfiles/Temp_H2O.txt'
filename_V0 = '/home/lnx/PycharmProjects/HS/304_P500_V0_2013_p/outputfiles/Temp_H2O.txt'
filename_V0_I0 = '/home/lnx/PycharmProjects/HS/304_P500_V0_2013_p_noinflows/outputfiles/Temp_H2O.txt'

name, header, thedata = hs_loader.loadfile(filename=filename)
data = pd.DataFrame(thedata)
data = data.set_index(0)
daily_max = data.resample('D',how='max')
daily_max_20130729 = daily_max.ix['2013-07-29']
daily_max_20130731 = daily_max.ix['2013-07-31']
daily_mean = data.resample('D',how='mean')
daily_mean_20130729 = daily_mean.ix['2013-07-29']
daily_mean_20130731 = daily_mean.ix['2013-07-31']

name, header, thedata_I0 = hs_loader.loadfile(filename=filename_I0)
data_I0 = pd.DataFrame(thedata_I0)
data_I0 = data_I0.set_index(0)
daily_max_I0 = data_I0.resample('D',how='max')
daily_max_20130729_I0 = daily_max_I0.ix['2013-07-29']
daily_max_20130731_I0 = daily_max_I0.ix['2013-07-31']
daily_mean_I0 = data_I0.resample('D',how='mean')
daily_mean_20130729_I0 = daily_mean_I0.ix['2013-07-29']
daily_mean_20130731_I0 = daily_mean_I0.ix['2013-07-31']

name, header, thedata_V0 = hs_loader.loadfile(filename=filename_V0)
data_V0 = pd.DataFrame(thedata_V0)
data_V0 = data_V0.set_index(0)
daily_max_V0 = data_V0.resample('D',how='max')
daily_max_20130729_V0 = daily_max_V0.ix['2013-07-29']
daily_max_20130731_V0 = daily_max_V0.ix['2013-07-31']
daily_mean_V0 = data_V0.resample('D',how='mean')
daily_mean_20130729_V0 = daily_mean_V0.ix['2013-07-29']
daily_mean_20130731_V0 = daily_mean_V0.ix['2013-07-31']

name, header, thedata_V0_I0 = hs_loader.loadfile(filename=filename_V0_I0)
data_V0_I0 = pd.DataFrame(thedata_V0_I0)
data_V0_I0 = data_V0_I0.set_index(0)
daily_max_V0_I0 = data_V0_I0.resample('D',how='max')
daily_max_20130729_V0_I0 = daily_max_V0_I0.ix['2013-07-29']
daily_max_20130731_V0_I0 = daily_max_V0_I0.ix['2013-07-31']
daily_mean_V0_I0 = data_V0_I0.resample('D',how='mean')
daily_mean_20130729_V0_I0 = daily_mean_V0_I0.ix['2013-07-29']
daily_mean_20130731_V0_I0 = daily_mean_V0_I0.ix['2013-07-31']

Rkm = np.arange(13,64.5,0.5)

fig = plt.figure()

#ax = fig.add_subplot(211)

#ax.set_title('1a 2085')
#axisrange = [12,60,12,33]
#ax.axis(axisrange)

plt.plot(Rkm, daily_max_20130729, color='green', lw=0.5, label='max, STQ, sunny (2013 07 29)')
plt.plot(Rkm, daily_max_20130731, color='green', linestyle='dashed', lw=0.5, label='max, STQ, cloudy (2013 07 31)')
#plt.plot(Rkm, daily_mean_20130729, color='green', lw=1,  linestyle='dotted', label='mean, STQ, sunny (2013 07 29)')
#plt.plot(Rkm, daily_mean_20130731, color='green', linestyle='dashed', lw=1, label='mean, STQ, cloudy (2013 07 31)')

#plt.plot(Rkm, daily_max_20130729_I0, color='blue', lw=0.5, label='max, STQ, no inflows, sunny')
#plt.plot(Rkm, daily_max_20130731_I0, color='blue', linestyle='dotted', lw=1, label='max, I0, cloudy')
#plt.plot(Rkm, daily_mean_20130729_I0, color='turquoise', lw=0.5, linestyle='solid', label='mean, STQ, no inflows, sunny')
#plt.plot(Rkm, daily_mean_20130731_I0, color='turquoise', linestyle='dotted', lw=1, label='mean, I0, cloudy')

plt.plot(Rkm, daily_max_20130729_V0, color='orange', lw=0.5, label='max, V0, sunny')
plt.plot(Rkm, daily_max_20130731_V0, color='orange', linestyle='dashed', lw=0.5, label='max, V0, cloudy')
#plt.plot(Rkm, daily_mean_20130729_V0, color='orange', lw=1, linestyle='dotted',label='mean, V0 ,sunny')
#plt.plot(Rkm, daily_mean_20130731_V0, color='orange', linestyle='dashed', lw=1, label='mean, V0, cloudy')

#plt.plot(Rkm, daily_max_20130729_V0_I0, color='violet', lw=0.5, label='max, V0, no inflows sunny')
#plt.plot(Rkm, daily_max_20130731_V0_I0, color='violet', linestyle='dotted', lw=1, label='max, V0, cloudy')
#plt.plot(Rkm, daily_mean_20130729_V0_I0, color='red', lw=0.5, linestyle='solid', label='mean, V0, no inflows sunny')
#plt.plot(Rkm, daily_mean_20130731_V0_I0, color='red', linestyle='dotted', lw=1, label='mean, V0, cloudy')
plt.grid(True)
plt.legend(loc=3, ncol=2, fontsize='small')
plt.ylabel('water temperature [degC]')


#ax = fig.add_subplot(212)

#ax.set_title('max 2085')
# axisrange = [12,60,12,33]
# ax.axis(axisrange)
# ax.plot(Rkm, WT_max, color='black', lw=0.5)
# # ax.plot(Rkm, WT_max, color='black', lw=0.3,  linestyle='dotted')
# # ax.plot(Rkm, WT_max_2085_mean, color='orange', lw=0.5)
# # ax.plot(Rkm, WT_max_2085_V0_mean, color='red', lw=0.5)
# # ax.plot(Rkm, WT_max_2085_V100_mean, color='green', lw=0.5)
# # ax.plot(Rkm, WT_max_2085_max, color='orange', lw=0.3, linestyle='dotted')
# # ax.plot(Rkm, WT_max_2085_V0_max, color='red', lw=0.3, linestyle='dotted')
# # ax.plot(Rkm, WT_max_2085_V100_max, color='green', lw=0.3, linestyle='dotted')
# plt.ylabel('water temperature [degC]')
# plt.xlabel('distance from source [km]')

#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title="km")


#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure4a.tiff')
plt.show()

quit()

#WT['Datetime'] = (mod(WT['Datetime'],1)*1000000/41667).round(2)
#WT['Datetime'] = WT['Datetime'].round(0)
days = WT['Datetime'].round(0)
#begin = datetime(1900,1,1,0,0,0) # Startddatum
#date = begin + timedelta(days-2)
               #+ timedelta(hours=zeit)


print datetime

#Datetime_old = str(WT['Datetime'])
#Datetime_old = np.array(Datetime_old)
#print Datetime_old
#starttime = '41480.000000'

#Datetime = []
#begin = datetime(1900,1,1,0,0,0) # Startdatum
#for i in Datetime_old:
#    tage, frac = Datetime_old[i].split('.')  # split bei '.'
#    zeit = round((float(frac) * 24) / 1000000)   # 500000 = 12h, 250000 = 6h, 041667 = 1h
#    date_time = begin + timedelta(days=float(tage)-2) \
#               + timedelta(hours=zeit)
#    Datetime.append(date_time)

#print Datetime

#print starttime.strftime('%Y-%m-%d %H')
#print WT['Datetime']
#datetime = np.array(WT['Datetime']).strftime('%Y-%m-%d %H')
#datetime = pd.to_datetime(WT['Datetime'])
#print datetime

#WT = WT.resample('D', how='max')

# WT_mean = WT.mean()
# WT_max = WT.max()
# WT_1a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
# WT_1a_2085_mean = WT_1a_2085.mean()
# WT_1a_2085_max = WT_1a_2085.max()
# WT_1a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
# WT_1a_2085_V0_mean = WT_1a_2085_V0.mean()
# WT_1a_2085_V0_max = WT_1a_2085_V0.max()
# WT_1a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
# WT_1a_2085_V100_mean = WT_1a_2085_V100.mean()
# WT_1a_2085_V100_max = WT_1a_2085_V100.max()