__author__ = 'lnx'

from pylab import *
import matplotlib.pyplot as plt
import pandas as pd
from Hs_scripts import hs_loader

filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809_STQ/Temp_H2O.txt'
name, header, data = hs_loader.loadfile(filename=filename)
data = pd.DataFrame(data)
data = data.set_index(0)
daily_max = data.resample('D', how ='max')
daily_mean = data.resample('D', how = 'mean')
sun_max = daily_max.iloc[4] #29 July = sunny
sun_mean = daily_mean.iloc[4]
cloud_max = daily_max.iloc[6] # 31.July = cloudy
cloud_mean = daily_mean.iloc[6]

filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809_Bal0/Temp_H2O.txt'
name, header, data = hs_loader.loadfile(filename=filename)
data = pd.DataFrame(data)
data = data.set_index(0)
daily_max = data.resample('D', how ='max')
daily_mean = data.resample('D', how = 'mean')
sun_max_Bal0 = daily_max.iloc[4] #29 July = sunny
sun_mean_Bal0 = daily_mean.iloc[4]
cloud_max_Bal0 = daily_max.iloc[6] # 31.July = cloudy
cloud_mean_Bal0 = daily_mean.iloc[6]

#filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809_Bal_noMix/Temp_H2O.txt'
filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809_H0/Temp_H2O.txt'
name, header, data = hs_loader.loadfile(filename=filename)
data = pd.DataFrame(data)
data = data.set_index(0)
daily_max = data.resample('D', how ='max')
daily_mean = data.resample('D', how = 'mean')
sun_max_H0 = daily_max.iloc[4] #29 July = sunny
sun_mean_H0 = daily_mean.iloc[4]
cloud_max_H0 = daily_max.iloc[6] # 31.July = cloudy
cloud_mean_H0 = daily_mean.iloc[6]

filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809_A1/Temp_H2O.txt'
name, header, data = hs_loader.loadfile(filename=filename)
data = pd.DataFrame(data)
data = data.set_index(0)
daily_max = data.resample('D', how ='max')
daily_mean = data.resample('D', how = 'mean')
sun_max_A1 = daily_max.iloc[4] #29 July = sunny
sun_mean_A1 = daily_mean.iloc[4]
cloud_max_A1 = daily_max.iloc[6] # 31.July = cloudy
cloud_mean_A1 = daily_mean.iloc[6]

filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809_I1/Temp_H2O.txt'
name, header, data = hs_loader.loadfile(filename=filename)
data = pd.DataFrame(data)
data = data.set_index(0)
daily_max = data.resample('D', how ='max')
daily_mean = data.resample('D', how = 'mean')
sun_max_I1 = daily_max.iloc[4] #29 July = sunny
sun_mean_I1 = daily_mean.iloc[4]
cloud_max_I1 = daily_max.iloc[6] # 31.July = cloudy
cloud_mean_I1 = daily_mean.iloc[6]

filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809_Disp0/Temp_H2O.txt'
name, header, data = hs_loader.loadfile(filename=filename)
data = pd.DataFrame(data)
data = data.set_index(0)
daily_max = data.resample('D', how ='max')
daily_mean = data.resample('D', how = 'mean')
sun_max_Disp0 = daily_max.iloc[4] #29 July = sunny
sun_mean_Disp0 = daily_mean.iloc[4]
cloud_max_Disp0 = daily_max.iloc[6] # 31.July = cloudy
cloud_mean_Disp0 = daily_mean.iloc[6]

filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809_V0/Temp_H2O.txt'
name, header, data = hs_loader.loadfile(filename=filename)
data = pd.DataFrame(data)
data = data.set_index(0)
daily_max = data.resample('D', how ='max')
daily_mean = data.resample('D', how = 'mean')
sun_max_V0 = daily_max.iloc[4] #29 July = sunny
sun_mean_V0 = daily_mean.iloc[4]
cloud_max_V0 = daily_max.iloc[6] # 31.July = cloudy
cloud_mean_V0 = daily_mean.iloc[6]

filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809_V100/Temp_H2O.txt'
name, header, data = hs_loader.loadfile(filename=filename)
data = pd.DataFrame(data)
data = data.set_index(0)
daily_max = data.resample('D', how ='max')
daily_mean = data.resample('D', how = 'mean')
sun_max_V100 = daily_max.iloc[4] #29 July = sunny
sun_mean_V100 = daily_mean.iloc[4]
cloud_max_V100 = daily_max.iloc[6] # 31.July = cloudy
cloud_mean_V100 = daily_mean.iloc[6]

filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809_STQ/VTS.txt'
name, header, data = hs_loader.loadfile(filename=filename)
data = pd.DataFrame(data)
data = data.set_index(0)
VTS = data.iloc[1]
VTS = VTS[1:21].mean()

start = 1
end = 20

dT_STQ = sun_max[end]-sun_max[start]
dT_V0 = sun_max_V0[end]-sun_max_V0[start] #15 *2 * 500m
dT_V100 = sun_max_V100[end]-sun_max_V100[start] #15 *2 * 500m
dT_H0 = sun_max_H0[end]-sun_max_H0[start]
dT_Bal0 = sun_max_Bal0[end]-sun_max_Bal0[start]
dT_Acc = sun_max_A1[end]-sun_max_A1[start]
dT_Infl = sun_max_I1[end]-sun_max_I1[start]
dT_Disp = sun_max_Disp0[end]-sun_max_Disp0[start]

dT_STQ_mean = sun_mean[end]-sun_mean[start]
dT_V100_mean = sun_mean_V100[end]-sun_mean_V100[start] #15 *2 * 500m
dT_V0_mean = sun_mean_V0[end]-sun_mean_V0[start] #15 *2 * 500m
dT_H0_mean = sun_mean_H0[end]-sun_mean_H0[start]
dT_Bal0_mean = sun_mean_Bal0[end]-sun_mean_Bal0[start]
dT_Acc_mean = sun_mean_A1[end]-sun_mean_A1[start]
dT_Infl_mean = sun_mean_I1[end]-sun_mean_I1[start]
dT_Disp_mean = sun_mean_Disp0[end]-sun_mean_Disp0[start]

print "VTS_STQ = %g" %VTS
print "Delta T_max[degC] from DFS %d to %d (Difference to STQ), 29.7.2013(sun): \n " %((start+78)/2,(end+78)/2)
print "STQ(no inflows, no accr, inkl. hypr. exch., inkl. evaporation losses): %g" %dT_STQ
print "V0: %g  (%g)" %(dT_V0,(dT_V0-dT_STQ))
print "V100: %g  (%g)" %(dT_V100,(dT_V100-dT_STQ))
print "hyporheic exchange = 0: %g  (%g)" %(dT_H0,(dT_H0-dT_STQ))
print "Dispersion = 0: %g  (%g)" %(dT_Disp,(dT_Disp-dT_STQ))
print "incl. accretion 0.001m2/s, 12km: %g (%g)" %(dT_Acc, (dT_Acc-dT_STQ))
print "incl inflows: %g  (%g)" %(dT_Infl,(dT_Infl-dT_STQ))
print "Energy Balance = 0: %g (%g)\n\n" %(dT_Bal0,(dT_Bal0-dT_STQ))

print "Delta T_mean[degC] (Difference to STQ), 29.7.2013(sun): \n "
print "STQ(no inflows, no accr, inkl. hypr. exch., inkl. evaporation losses): %g " %dT_STQ_mean
print "V0: %g  (%g)" %(dT_V0_mean,(dT_V0_mean-dT_STQ_mean))
print "V100: %g  (%g)" %(dT_V100_mean,(dT_V100_mean-dT_STQ_mean))
print "hyporheic exchange = 0: %g  (%g)" %(dT_H0_mean,(dT_H0_mean-dT_STQ_mean))
print "Dispersion = 0: %g (%g)" %(dT_Disp_mean,(dT_Disp_mean-dT_STQ_mean))
print "incl. accrection 0.001m2/s, 12km: %g (%g)" %(dT_Acc_mean,(dT_Acc_mean-dT_STQ_mean))
print "incl. inflows: %g (%g)" %(dT_Infl_mean,(dT_Infl_mean-dT_STQ_mean))
print "Energy Balance = 0: %g (%g)\n\n" %(dT_Bal0_mean,(dT_Bal0_mean-dT_STQ_mean))

dT_STQ = cloud_max[end]-cloud_max[start]
dT_V0 = cloud_max_V0[end]-cloud_max_V0[start] #15 *2 * 500m
dT_H0 = cloud_max_H0[end]-cloud_max_H0[start]
dT_Bal0 = cloud_max_Bal0[end]-cloud_max_Bal0[start]
dT_Acc = cloud_max_A1[end]-cloud_max_A1[start]
dT_Infl = cloud_max_I1[end]-cloud_max_I1[start]
dT_Disp = cloud_max_Disp0[end]-cloud_max_Disp0[start]

dT_STQ_mean = cloud_mean[end]-cloud_mean[start]
dT_V0_mean = cloud_mean_V0[end]-cloud_mean_V0[start]
dT_H0_mean = cloud_mean_H0[end]-cloud_mean_H0[start]
dT_Bal0_mean = cloud_mean_Bal0[end]-cloud_mean_Bal0[start]
dT_Acc_mean = cloud_mean_A1[end]-cloud_mean_A1[start]
dT_Infl_mean = cloud_mean_I1[end]-cloud_mean_I1[start]
dT_Disp_mean = cloud_mean_Disp0[end]-cloud_mean_Disp0[start]

print "Delta T_max[degC] (Difference to STQ), 31.7.2013(cloud): \n "
print "STQ(no inflows, no accr, inkl. hypr. exch., inkl. evaporation losses): %g" %dT_STQ
print "hyporheic exchange = 0: %g  (%g)" %(dT_H0,(dT_H0-dT_STQ))
print "V0: %g  (%g)" %(dT_V0,(dT_V0-dT_STQ))
print "V100: %g  (%g)" %(dT_V100,(dT_V100-dT_STQ))
print "Dispersion = 0: %g  (%g)" %(dT_Disp,(dT_Disp-dT_STQ))
print "incl. accretion 0.001m2/s, 12km: %g (%g)" %(dT_Acc, (dT_Acc-dT_STQ))
print "incl inflows: %g  (%g)" %(dT_Infl,(dT_Infl-dT_STQ))
print "Energy Balance = 0: %g (%g)\n\n" %(dT_Bal0,(dT_Bal0-dT_STQ))

print "Delta T_mean[degC] (Difference to STQ), 31.7.2013(cloud): \n "
print "STQ(no inflows, no accr, inkl. hypr. exch., inkl. evaporation losses): %g " %dT_STQ_mean
print "V0: %g  (%g)" %(dT_V0_mean,(dT_V0_mean-dT_STQ_mean))
print "V100: %g  (%g)" %(dT_V100_mean,(dT_V100_mean-dT_STQ_mean))
print "hyporheic exchange = 0: %g  (%g)" %(dT_H0_mean,(dT_H0_mean-dT_STQ_mean))
print "Dispersion = 0: %g (%g)" %(dT_Disp_mean,(dT_Disp_mean-dT_STQ_mean))
print "incl. accrection 0.001m2/s, 12km: %g (%g)" %(dT_Acc_mean,(dT_Acc_mean-dT_STQ_mean))
print "incl. inflows: %g (%g)" %(dT_Infl_mean,(dT_Infl_mean-dT_STQ_mean))
print "Energy Balance = 0: %g (%g)\n\n" %(dT_Bal0_mean,(dT_Bal0_mean-dT_STQ_mean))

quit()


# writer_orig = pd.ExcelWriter('/home/lnx/simple.xlsx', engine='xlsxwriter')
# daily_max.to_excel(writer_orig, index=False, sheet_name='report')
# writer_orig.save()

#out = open('/home/lnx/daily_max_acc1.txt', 'w')
#out.write(daily_max)                               #file written ok, but not unicode characters?
#out.close()

#Rkm = WT.columns
#Rkm = np.arange(13,64.5,0.5) #
#Rkm = np.arange(1,47,1)
#print Rkm
#Rkm = pd.DataFrame(Rkm, columns=['Rkm'])

#print sun_max[1]
#print sun_max

fig = plt.figure()

ax = fig.add_subplot(211)
ax.set_title('T max, sun (solid line), cloud (dotted line)')
ax.plot(sun_max, color='red', linestyle="solid", lw=1, label='no_inflows_noaccretion_nohypflux')
ax.plot(cloud_max, color='red', linestyle="dotted", lw=1)
ax.plot(sun_max_A1, color='orange', linestyle="solid", lw=1, label='incl. accretion')
ax.plot(cloud_max_A1, color='orange', linestyle="dotted", lw=1)
ax.plot(sun_max_I1, color='blue', linestyle="solid", lw=1, label='incl. inflows')
ax.plot(cloud_max_I1, color='blue', linestyle="dotted", lw=1)
ax.plot(sun_max_Bal0, color='black', linestyle="solid", lw=1, label='Energy Balance = 0')
ax.plot(cloud_max_Bal0, color='black', linestyle="dotted", lw=1)
ax.plot(sun_max_H0, color='green', linestyle="solid", lw=1, label='Hyporheic exchange = 0')
ax.plot(cloud_max_H0, color='green', linestyle="dotted", lw=1)
ax.plot(sun_max_Disp0, color='violet', linestyle="solid", lw=1, label='Dispersion = 0')
ax.plot(cloud_max_Disp0, color='violet', linestyle="dotted", lw=1)
ax.plot(sun_max_S1_0, color='lightgreen', linestyle="solid", lw=1, label='S1_value = 0')
ax.plot(cloud_max_S1_0, color='lightgreen', linestyle="dotted", lw=1)

plt.legend(fontsize='small')
plt.grid()

ax = fig.add_subplot(212)
ax.set_title('T mean')
ax.plot(sun_mean, color='red', linestyle="solid", lw=0.5, label='no_inflows_noaccretion (sun)')
ax.plot(cloud_mean, color='red', linestyle="dotted", lw=0.5, label='Tmean_cloud')
ax.plot(sun_mean_A1, color='orange', linestyle="solid", lw=0.5, label='+acc_sun')
ax.plot(cloud_mean_A1, color='orange', linestyle="dotted", lw=0.5, label='Tmean +acc_cloud')
ax.plot(sun_mean_I1, color='blue', linestyle="solid", lw=0.5, label='+inflows_sun')
ax.plot(cloud_mean_I1, color='blue', linestyle="dotted", lw=0.5, label='Tmean +inflows_cloud')
ax.plot(sun_mean_Bal0, color='black', linestyle="solid", lw=0.5, label='-Bal0_sun')
ax.plot(cloud_mean_Bal0, color='black', linestyle="dotted", lw=0.5, label='Tmean -BalO_cloud')
ax.plot(sun_mean_Mix0, color='green', linestyle="solid", lw=0.5, label='-hyp.exchange_sun')
ax.plot(cloud_mean_Mix0, color='green', linestyle="dotted", lw=0.5, label='Tmean -hyp.exchange_cloud')
ax.plot(sun_mean_Mix0, color='violet', linestyle="solid", lw=0.5, label='Dispersion = 0')
ax.plot(cloud_mean_Mix0, color='violet', linestyle="dotted", lw=0.5)

#ax.plot(Rkm, meas_mean, marker='x',color='blue', lw=0.5, label='measured')
plt.xlabel('distance from DFM61')
plt.ylabel('water temperature [degC]')
#plt.legend(fontsize='small')
plt.grid()

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/Gerda_Paper/Sun_Shade_Tmax_mean_Acc.tiff')

plt.show()




#
# filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08_acc/Temp_H2O.txt'
# name, header, data = hs_loader.loadfile(filename=filename)
# data = pd.DataFrame(data)
# data = data.set_index(0)
# daily_max = data.resample('D', how ='max')
# daily_mean = data.resample('D', how = 'mean')
# sun_max_acc = daily_max.iloc[4] #29 July = sunny
# sun_mean_acc = daily_mean.iloc[4]
# cloud_max_acc = daily_max.iloc[6] # 31.July = cloudy
# cloud_mean_acc = daily_mean.iloc[6]

#	daily_max = daily_max.ix['2013-08-02':'2013-08-08', '12':'83'