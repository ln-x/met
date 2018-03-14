from pylab import *
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd
__author__ = 'lnx'
import matplotlib.pyplot as plt

WT = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_MLF_p_INCA/outputfiles/Temp_H2O_bis8Aug.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
#TODO .ix funktioniert hier aus irgendwelchen Gruenden nicht - entweder raw file bearbeiten oder?
WT = WT.ix[240:]
print len(WT)
#T = WT.ix[:359]
#print len(WT)

WT_forest = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_MLF_p_INCA/outputfiles_forest/Temp_H2O_bis8Aug.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_forest = WT_forest.ix[240:]

WT_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p_INCA/outputfiles/Temp_H2O_bis8Aug.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_V100 = WT_V100.ix[240:]

WT_V100_forest = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p_INCA/outputfiles_forest/Temp_H2O_bis8Aug.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_V100_forest = WT_V100_forest.ix[240:]

#WT = WT.ix[240:359]

WT_mean = WT.mean()
WT_max = WT.max()
WT_mean_forest = WT_forest.mean()
WT_max_forest = WT_forest.max()
WT_mean_V100_forest = WT_V100_forest.mean()
WT_max_V100_forest = WT_V100_forest.max()
WT_mean_V100 = WT_V100.mean()
WT_max_V100 = WT_V100.max()

print "WT_mean['61.000'] - WT_mean_forest['61.000']", WT_mean['61.000'] - WT_mean_forest['61.000']
print "WT_mean_V100['61.000'] - WT_mean_V100_forest['61.000']", WT_mean_V100['61.000'] - WT_mean_V100_forest['61.000']
print "WT_max_V100['61.000'] - WT_max_V100_forest['61.000']", WT_max_V100['61.000'] - WT_max_V100_forest['61.000']
print (WT_mean_forest- WT_mean).mean()
print (WT_mean_V100_forest- WT_mean_V100).mean()




WT_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S214_P_STQ_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_2030 = WT_2030.ix[240:]#.drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
print len(WT_2030)
WT_2030_mean = WT_2030.mean()
WT_2030_max = WT_2030.max()

WT_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S215_P_V0_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_2030_V0 = WT_2030_V0.ix[240:]
WT_2030_V0_mean = WT_2030_V0.mean()
WT_2030_V0_max = WT_2030_V0.max()

WT_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S216_P_V100_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_2030_V100 = WT_2030_V100.ix[240:]
WT_2030_V100_mean = WT_2030_V100.mean()
WT_2030_V100_max = WT_2030_V100.max()

WT_2030_V0_diff = (WT_2030_mean - WT_2030_V0_mean)*-1
WT_2030_V100_diff = (WT_2030_mean - WT_2030_V100_mean)#*-1

WT_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S244_P_STQ_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_2050 = WT_2050.ix[240:]
WT_2050_mean = WT_2050.mean()
WT_2050_max = WT_2050.max()

WT_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S245_P_V0_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_2050_V0 = WT_2050_V0.ix[240:]
WT_2050_V0_mean = WT_2050_V0.mean()
WT_2050_V0_max = WT_2050_V0.max()

WT_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S246_P_V100_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_2050_V100 = WT_2050_V100.ix[240:]
WT_2050_V100_mean = WT_2050_V100.mean()
WT_2050_V100_max = WT_2050_V100.max()

WT_2050_V0_diff = (WT_2050_mean - WT_2050_V0_mean)*-1
WT_2050_V100_diff = (WT_2050_mean - WT_2050_V100_mean)#*-1

WT_max_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S274_P_STQ_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2085 = WT_max_2085.ix[240:]
WT_max_2085_mean = WT_max_2085.mean()
WT_max_2085_max = WT_max_2085.max()

WT_max_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S275_P_V0_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2085_V0 = WT_max_2085_V0.ix[240:]
WT_max_2085_V0_mean = WT_max_2085_V0.mean()
WT_max_2085_V0_max = WT_max_2085_V0.max()

WT_max_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S276_P_V100_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_max_2085_V100 = WT_max_2085_V100.ix[240:]
WT_max_2085_V100_mean = WT_max_2085_V100.mean()
WT_max_2085_V100_max = WT_max_2085_V100.max()

WT_2085_V0_diff = (WT_max_2085_mean - WT_max_2085_V0_mean)*-1
WT_2085_V100_diff = (WT_max_2085_mean - WT_max_2085_V100_mean)#*-1

print WT_2030_V0_diff[19]
print WT_2030_V100_diff[19]

#Rkm = np.arange(13,64.5,0.5)
Rkm = np.arange(10.85,62.35,0.5)

print len(Rkm)

fig = plt.figure()


#fig.set_size_inches(3.39,2.54)

ax = fig.add_subplot(411)
ax.set_title('  2030 MAX', fontsize='small', loc='left')
axisrange = [10,61,12,30]
ax.axis(axisrange)
a= ax.plot(Rkm, WT_mean, color='black', lw=0.9, label='2013_STQ')
a= ax.plot(Rkm, WT_mean_forest, color='black',linestyle='dashed', lw=0.9, label='2013_STQ_forest')
b= ax.plot(Rkm, WT_mean_V100, color='green', lw=0.9, label='2013_V100')
c= ax.plot(Rkm, WT_mean_V100_forest, color='green', linestyle='dashed', lw=0.9, label='2013_V100_forest')
'''
b= ax.plot(Rkm, WT_max, color='black', lw=0.9,  linestyle='dashed', label='2013_STQ_max')
c= ax.plot(Rkm, WT_2030_mean, color='orange', lw=0.9, label='STQ')
d= ax.plot(Rkm, WT_2030_max, color='orange', lw=0.9, linestyle='dotted', label='STQ_max')
e= ax.plot(Rkm, WT_2030_V0_mean, color='#d95f02', lw=0.9, label='V0')
f= ax.plot(Rkm, WT_2030_V0_max, color='#d95f02', lw=0.9, linestyle='dotted',  label='V0_max')
g= ax.plot(Rkm, WT_2030_V100_mean, color='#1b9e77', lw=0.9, label='V100')
h= ax.plot(Rkm, WT_2030_V100_max, color='#1b9e77', lw=0.9, linestyle='dotted', label='V100_max')
'''
plt.ylabel('water temperature [degC]')

ax.set(xticklabels=('','','','',''))
#plt.legend(loc=9, ncol=4, fontsize='small')
#plt.legend(bbox_to_anchor=(0.577, 1.35), ncol=4, loc=9, borderaxespad=0, fontsize='small')
plt.legend(bbox_to_anchor=(0.577, 1.45), ncol=4, loc=9, borderaxespad=0, fontsize='small')

#plt.ylabel('water temperature [degC]')

ax = fig.add_subplot(412)
ax.set_title('  2050 MAX', fontsize='small', loc='left')
axisrange = [10,61,12,30]
ax.axis(axisrange)
ax.plot(Rkm, WT_mean, color='black', lw=0.9, label='2013_STQ')
ax.plot(Rkm, WT_max, color='black', lw=0.9,  linestyle='dashed', label='2013_STQ_max')
ax.plot(Rkm, WT_2050_mean, color='orange', lw=0.9, label='STQ')
ax.plot(Rkm, WT_2050_max, color='orange', lw=0.9, linestyle='dotted', label='STQ_max')
ax.plot(Rkm, WT_2050_V0_mean, color='#d95f02', lw=0.9, label='V0')
ax.plot(Rkm, WT_2050_V0_max, color='#d95f02', lw=0.9, linestyle='dotted',  label='V0_max')
ax.plot(Rkm, WT_2050_V100_mean, color='#1b9e77', lw=0.9, label='V100')
ax.plot(Rkm, WT_2050_V100_max, color='#1b9e77', lw=0.9, linestyle='dotted', label='V100_max')
ax.set(xticklabels=('','','','',''))
#plt.legend(loc=9, ncol=4, fontsize='small')

ax = fig.add_subplot(413)

ax.set_title('  2085 MAX', fontsize='small', loc='left')
axisrange = [10,61,12,30]
ax.axis(axisrange)
#ticks = [10,15,20,25,30]
#ax.set_ticks(ticks, minor = False)
ax.plot(Rkm, WT_mean, color='black', lw=0.9)
ax.plot(Rkm, WT_max, color='black', lw=0.9,  linestyle='dashed')
ax.plot(Rkm, WT_max_2085_mean, color='orange', lw=0.9)
ax.plot(Rkm, WT_max_2085_V0_mean, color='#d95f02', lw=0.9)
ax.plot(Rkm, WT_max_2085_V100_mean, color='#1b9e77', lw=0.9)
ax.plot(Rkm, WT_max_2085_max, color='orange', lw=0.9, linestyle='dotted')
ax.plot(Rkm, WT_max_2085_V0_max, color='#d95f02', lw=0.9, linestyle='dotted')
ax.plot(Rkm, WT_max_2085_V100_max, color='#1b9e77', lw=0.9, linestyle='dotted')
ax.set(xticklabels=('','','','',''))
#plt.ylabel('water temperature [degC]')

ax = fig.add_subplot(414)
ax.set_title('green: V100-STQ, red: V0-STQ', fontsize='small', loc='left') #, color='g'
axisrange = [10,61,-2.5,2.5]
plt.axis(axisrange)
ax.plot(Rkm, WT_2030_V100_diff, color='#1b9e77', lw=0.9, label='2030')#: STQ-V100')
ax.plot(Rkm, WT_2050_V100_diff, color='#1b9e77', lw=0.9, linestyle='dashed',label='2050') #: STQ-V100')
ax.plot(Rkm, WT_2085_V100_diff, color='#1b9e77', lw=0.9,linestyle='dotted', label='2085') #: STQ-V100')
ax.plot(Rkm, WT_2030_V0_diff, color='#d95f02', lw=0.9)#, label='2030: STQ-V0 *-1')
ax.plot(Rkm, WT_2050_V0_diff, color='#d95f02', lw=0.9, linestyle='dashed')#,label='2050: STQ-V0 *-1')
ax.plot(Rkm, WT_2085_V0_diff, color='#d95f02', lw=0.9, linestyle='dotted')#, label='2085: STQ-V0 *-1')
plt.legend(fontsize='small', loc=4, ncol=3)
#plt.ylabel('water temperature difference [degC]')
plt.xlabel('distance from source [km]')

#fig.legend((a,b,c,d,e,f,g,h),('STQ_2013','STQ_2013_max','STQ','STQ_max','V0','V0_max','V100','V100_max'),'upper left')
#fig.legend(a,'STQ_2013','upper left')

#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/fig/Figure4_20160406.tiff')
plt.show()