from BIOCLIC import hs_loader

__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import pandas as pd
import math
import csv
from dateutil.parser import parse

#index = pd.date_range('1/7/2013 00', periods= 1440 ) #1440 hours until 29.8.23h
#index = pd.date_range('25/7/2013 0h', periods= 384 ) #1440 hours until 9.8.23h

#WT0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Temp_H2O.txt', skiprows=6, sep='\s+')
               # index_col='Datetime', parse_dates="Datetime")
WT0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130701_0829/Temp_H2O.txt', skiprows=6, sep='\s+')
WT0['Datetime'] = pd.date_range('1/7/2013 00', periods= 1440, freq='1h')
WT = WT0.set_index(['Datetime'])
print WT['47.000'].head()
WT_daily_mean = WT.resample('D', how='mean')
WT_daily_min = WT.resample('D', how='min')
WT_daily_max = WT.resample('D', how='max')

#WTm0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/Measurements_20130725_0809_corr.csv', skiprows=6, sep='\s+')
WTm0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/Measurements_corr.csv', skiprows=6, sep='\s+',  na_values=['0.000'])
WTm0['Datetime'] = pd.date_range('1/7/2013 00', periods= 1440, freq='1h')
WTm = WTm0.set_index(['Datetime'])
WTm.drop(['datetime'], axis=1)
print WTm
WTm_daily_mean = WTm.resample('D', how='mean')
WTm_daily_min = WTm.resample('D', how='min')
WTm_daily_max = WTm.resample('D', how='max')

R2_RD = WTm['69'].corr(WT['69.000'])
R2_RD_min = WTm_daily_min['69'].corr(WT_daily_min['69.000'])
R2_RD_mean = WTm_daily_mean['69'].corr(WT_daily_mean['69.000'])
R2_RD_max = WTm_daily_max['69'].corr(WT_daily_max['69.000'])

R2_OO = WTm['65'].corr(WT['65.000'])
R2_OO_min = WTm_daily_min['65'].corr(WT_daily_min['65.000'])
R2_OO_mean = WTm_daily_mean['65'].corr(WT_daily_mean['65.000'])
R2_OO_max = WTm_daily_max['65'].corr(WT_daily_max['65.000'])

R2_UO = WTm['69'].corr(WT['62.500'])
R2_UO_min = WTm_daily_min['62.5'].corr(WT_daily_min['62.500'])
R2_UO_mean = WTm_daily_mean['62.5'].corr(WT_daily_mean['62.500'])
R2_UO_max = WTm_daily_max['62.5'].corr(WT_daily_max['62.500'])

R2_UW = WTm['61'].corr(WT['61.000'])
R2_UW_min = WTm_daily_min['61'].corr(WT_daily_min['61.000'])
R2_UW_mean = WTm_daily_mean['61'].corr(WT_daily_mean['61.000'])
R2_UW_max = WTm_daily_max['61'].corr(WT_daily_max['61.000'])

R2_J3 = WTm['51.5'].corr(WT['51.500'])
R2_J3_min = WTm_daily_min['51.5'].corr(WT_daily_min['51.500'])
R2_J3_mean = WTm_daily_mean['51.5'].corr(WT_daily_mean['51.500'])
R2_J3_max = WTm_daily_max['51.5'].corr(WT_daily_max['51.500'])

print 'RD: R2=', R2_RD, 'R2_min=', R2_RD_min, 'R2_mean=' , R2_RD_mean, 'R2_max=', R2_RD_max
print 'OO: R2=', R2_OO, 'R2_min=', R2_OO_min, 'R2_mean=' , R2_OO_mean, 'R2_max=', R2_OO_max
print 'UO: R2=', R2_UO, 'R2_min=', R2_UO_min, 'R2_mean=' , R2_UO_mean, 'R2_max=', R2_UO_max
print 'UW: R2=', R2_UW, 'R2_min=', R2_UW_min, 'R2_mean=' , R2_UW_mean, 'R2_max=', R2_UW_max
print 'J3: R2=', R2_J3, 'R2_min=', R2_J3_min, 'R2_mean=' , R2_J3_mean, 'R2_max=', R2_J3_max

quit()

results = np.array()

RD: R2= 0.980510404486 R2_min= 0.97928107736 R2_mean= 0.986728679309 R2_max= 0.96099739861
OO: R2= 0.97844988591 R2_min= 0.964975884613 R2_mean= 0.990697465707 R2_max= 0.975776578411
UO: R2= 0.967714213343 R2_min= 0.961714734289 R2_mean= 0.980434864687 R2_max= 0.955377459447
UW: R2= 0.848087203786 R2_min= 0.959993342821 R2_mean= 0.979487784863 R2_max= 0.95344534338
J3: R2= 0.939901246484 R2_min= 0.95858128585 R2_mean= 0.958071146274 R2_max= 0.938299045843

results = results.append([R2_RD,R2_RD_min,R2_RD_mean,R2_RD_max])
results = results.append([R2_OO,R2_OO_min,R2_OO_mean,R2_OO_max])
results = results.append([R2_OO,R2_OO_min,R2_OO_mean,R2_OO_max])
results = results.append([R2_UW,R2_UW_min,R2_UW_mean,R2_UW_max])
results = results.append([R2_J3,R2_J3_min,R2_J3_mean,R2_J3_max])

results = DataFrame(results, index=['RD','OO', 'UO', 'UW', 'J3'], column=['min','mean','max'])
results.to_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/R2_daily_298_sed1m_fricvWindVTS_penman_20130725_0809.csv')

f = open("/home/lnx/2_Documents/_BioClic/_Simulationen/R2_daily_298_sed1m_fricvWindVTS_penman_20130725_0809.txt",'w')

f.write('RD: R2=', R2_RD, 'R2_min=', R2_RD_min, 'R2_mean=' , R2_RD_mean, 'R2_max=', R2_RD_max)
f.write('OO: R2=', R2_OO, 'R2_min=', R2_OO_min, 'R2_mean=' , R2_OO_mean, 'R2_max=', R2_OO_max)
f.write('UO: R2=', R2_UO, 'R2_min=', R2_UO_min, 'R2_mean=' , R2_UO_mean, 'R2_max=', R2_UO_max)
f.write('UW: R2=', R2_UW, 'R2_min=', R2_UW_min, 'R2_mean=' , R2_UW_mean, 'R2_max=', R2_UW_max)
f.write('J3: R2=', R2_J3, 'R2_min=', R2_J3_min, 'R2_mean=' , R2_J3_mean, 'R2_max=', R2_J3_max)




#meas_index = {stationcode:(DFM,DRS),RD:(69,33), OO:(65,37),UO:(62.5,39.5),UW:(61,41),J3:(54.5,47.5??48)}


for i in y:

    rmse = []
    for j in x:
        rmse.append(((stations[i][0][j]-stations[i][1][j])**2)**0.5)
        #print 'i=', i, 'j=', j, 'rmse=', rmse
    rmse_m = 0
    for j in x:
        rmse_m = rmse_m + rmse[j]
    rmse_m = rmse_m/(len(rmse))
    print stations_names[i]
    print 'rmse:', rmse_m
    f.write('\n')
    f.write(str(stations_names[i]))
    f.write('\nrmse:')
    f.write(str(rmse_m))

    slope, intercept, r_value, p_value, std_err = linregress(stations[i][0],stations[i][1])
    print 'r_value:', r_value       # correlation coefficient
    print 'r-squared:', r_value**2  #coefficient of determination
    f.write('\nr_value:')
    f.write(str(r_value))       # correlation coefficient
    f.write('\nr-squared:')
    f.write(str(r_value**2))  #coefficient of determination
    f.write('\n')

    #min/max/amplitude/mean of whole period
    #min_m = min(stations[i][0])
    min_s = min(stations[i][1])
    max_m = max(stations[i][0])
    max_s = max(stations[i][0])
    #amp_m = max_m - min_m
    amp_s = max_s - min_s
    mean_m = np.mean(stations[i][0])
    mean_s = np.mean(stations[i][1])

    #if abs(amp_m - amp_s) > 1: print "amplitudes m, s:", amp_m, amp_s
    #if abs(min_m - min_s) > 1: print "min m, s:", min_m, min_s
    if abs(max_m - max_s) > 1: print "max m, s:", max_m, max_s
    if abs(mean_m - mean_s) > 1: print "mean m, s:", mean_m, mean_s
    print "\n"

    #"gleitendes" min/max?
    for j in x:
        min_m = min(stations[i][0][j:j+23])
        print min_m

    #daily mean

    # x ...number of hours, d = x/24 ... days

    #d = np.arange(0,len(date_time)/24,1)

    #for j in x:
    #    for k in d:
    #        min_m = min(stations[i][0][k])



# slope, intercept, r_value, p_value, std_err = linregress(uws,uw)
# print 'r_value:', r_value       # correlation coefficient
# print "r-squared:", r_value**2  #coefficient of determination

#slope : float   - slope of the regression line
#intercept : float - intercept of the regression line
#r-value : float -correlation coefficient
#p-value : float -two-sided p-value for a hypothesis test whose null hypothesis is that the slope is zero
#stderr : float -Standard error of the estimate

fig = plt.figure()
plt.title(simname)
plt.plot(date_time, uos, color='red', lw=0.5, label='uo_s')
plt.plot(date_time, uo, color='blue', lw=0.5, label='uo_m')
#plt.plot(date_time, rmse_uw, color='black', lw=0.5, label='rmse_uw')


fig.autofmt_xdate()
plt.xlabel('time[h]')
plt.ylabel('water temperature [degC]')
plt.legend()

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/UO_Validation_OrigConv_m_298_sed1m_FricvelWindVTS_penman_20130701_0829.png')
plt.show()