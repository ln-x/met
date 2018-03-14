__author__ = 'lnx'

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
from scipy.stats import *


#path = ['/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_MLF_p/outputfiles_orig/Temp_H2O.txt',
#        '/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles/Temp_H2O.txt',
#        '/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles/Temp_H2O.txt']
#
#WT_max = []
#for i in range(len(path)):
#    WT_max[i] =  pd.read_csv(path[i-1], skiprows=6, sep='\s+')
#    WT_max[i] = WT_2013[i].ix[240:359].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column  1.July-3.Aug: 744+72=816h
#    WT_max[i] = np.array(WT_2013[i]['61.000']) #select only reference station Unterwart DFM 61km ~ DFS 39
#    WT_max[i] = WT_2013[i].ravel()

path = ['/home/lnx/PycharmProjects/HS/S190_P_STQ_2030_1a_MLF/outputfiles/Temp_H2O.txt',
       '/home/lnx/PycharmProjects/HS/S191_P_V0_2030_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S192_P_V100_2030_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS192_P_V50_2030_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS192_P_V100_VD70_2030_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S196_P_STQ_2030_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S197_P_V0_2030_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S198_P_V100_2030_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS198_P_V50_2030_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS198_P_V100_VD70_2030_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S202_P_STQ_2030_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S203_P_V0_2030_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S204_P_V100_2030_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS204_P_V50_2030_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS204_P_V100_VD70_2030_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S214_P_STQ_2030_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S215_P_V0_2030_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S216_P_V100_2030_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS216_P_V50_2030_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS216_P_V100_VD70_2030_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S220_P_STQ_2050_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S221_P_V0_2050_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S222_P_V100_2050_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS222_P_V50_2050_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS222_P_V100_VD70_2050_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S226_P_STQ_2050_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S227_P_V0_2050_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S228_P_V100_2050_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS228_P_V50_2050_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS228_P_V100_VD70_2050_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S232_P_STQ_2050_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S233_P_V0_2050_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S234_P_V100_2050_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS234_P_V50_2050_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS234_P_V100_VD70_2050_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S244_P_STQ_2050_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S245_P_V0_2050_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S246_P_V100_2050_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS246_P_V50_2050_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS246_P_V100_VD70_2050_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS252_P_V50_2085_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS252_P_V100_VD70_2085_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S256_P_STQ_2085_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S257_P_V0_2085_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S258_P_V100_2085_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS258_P_V50_2085_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS258_P_V100_VD70_2085_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S303_P_V50_VD09_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S274_P_STQ_2085_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S275_P_V0_2085_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S276_P_V100_2085_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS276_P_V50_2085_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/XS276_P_V100_VD70_2085_Max_MLF/outputfiles/Temp_H2O.txt'
        ]

x = len(path)
WT_max = range(x)
WT_dailymax = range(x)
WT_dailymin = range(x)

for i in range(len(path)):
    WT_max[i] =  pd.read_csv(path[i], skiprows=6, sep='\s+')
    WT_max[i]['realdate'] = pd.TimedeltaIndex(WT_max[i]['Datetime'], unit='d') +  datetime.datetime(1900,1,1,0,0,0)
    WT_max[i] = WT_max[i].set_index('realdate')
    #print WT_max[i].head()
    WT_dailymax[i] = WT_max[i]['61.000'].resample('D', how='max').mean()
    WT_dailymin[i] = WT_max[i]['61.000'].resample('D', how='min').mean()
    WT_max[i] = WT_max[i].ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column  1.July-3.Aug: 744+72=816h
    WT_max[i] = np.array(WT_max[i]['61.000']) #select only reference station Unterwart DFM 61km ~ DFS 39
    WT_max[i] = WT_max[i].ravel()
    #shapiro_results = scipy.stats.shapiro(WT_dailymax[i])
    #print shapiro_results[0], shapiro_results[1]

#C_2013 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/inputfiles/Climate_04inca.csv', index_col=['DateTime'], sep=',', parse_dates=['DateTime'])
#C_2013_max5days = C_2013['2013-08-04 00:00:00':'2013-08-08 23:50:00']
#C_2013_max5days_glorad_sum = C_2013_max5days['GloRad (W/m2)'].resample('D', how='sum') * 0.0036
#C_2013_max5days_mean = C_2013_max5days.mean()
#C_2013_max5days_glorad_sum_mean = C_2013_max5days_glorad_sum.mean()
#print '2013 max: \n', C_2013_max5days_mean, '\nGloRadSum[MJ/d] \t\t\t', C_2013_max5days_glorad_sum_mean


C_path = ['/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/1jaehrl/MLF/Climate_04.csv',
        '/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/5jaehrl/MLF/Climate_04.csv',
        '/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/20jaehrl/MLF/Climate_04.csv',
        '/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/Max/MLF/Climate_04.csv',
        '/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/1jaehrl/MLF/Climate_04.csv',
        '/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/5jaehrl/MLF/Climate_04.csv',
        '/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/20jaehrl/MLF/Climate_04.csv',
        '/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/Max/MLF/Climate_04.csv',
        '/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/1jaehrl/MLF/Climate_04.csv',
        '/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/5jaehrl/MLF/Climate_04.csv',
        '/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/20jaehrl/MLF/Climate_04.csv',
        '/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/Max/MLF/Climate_04.csv'
         ]

y = len(C_path)
C = range(y)
TA = range(y)
TA_max = range(y)
TA_dailymax = range(y)
TA_min = range(y)
TA_dailymin = range(y)
print y


for i in range(len(C_path)):
    #print i
    C[i] = pd.read_csv(C_path[i], sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
    C[i] = C[i].set_index('datetime')
    C[i] = C[i].ix[240:]  #last five days
    #C[i]['Rad'] = C[i]['Rad'].resample('D', how='sum') * 0.0036
    TA[i] = C[i]['AirT'].mean()
    TA_max[i] = C[i]['AirT'].max()
    TA_min[i] = C[i]['AirT'].min()
    TA_dailymax[i] = C[i]['AirT'].resample('D', how='max').mean()
    TA_dailymin[i] = C[i]['AirT'].resample('D', how='min').mean()

fs = 10  # fontsize

fig = plt.figure()
# fig.set_size_inches(3.39,2.54)

watertemp_STQ = [WT_max[i].max() for i in range (0,60,5)]
watertemp_V0 = [WT_max[i].max() for i in range(1,61,5)]
watertemp_V100 = [WT_max[i].max() for i in range(2,62,5)]
watertemp_V50 = [WT_max[i].max() for i in range(3,62,5)]
watertemp_V100VD70 = [WT_max[i].max() for i in range(4,62,5)]
airtemp = [TA_max[i] for i in range(12)]

print len(watertemp_V0)
#print watertemp_STQ
print len(airtemp)
#print airtemp
#plt.axis([25,45,15,35])
plt.axis([16,45,15,35])
plt.scatter(airtemp,watertemp_STQ,color='lightgrey', label="STQ, max")
plt.scatter(airtemp,watertemp_V0,color='#d95f02', label="V0, max")
plt.scatter(airtemp,watertemp_V50, color='orange', label="V50, max")
plt.scatter(airtemp,watertemp_V100VD70, color='green', label="V100 VD70, max")
plt.scatter(airtemp,watertemp_V100, color='blue', label="V100, max")

plt.legend(loc="4")

axes = plt.gca()
m1, b1 = np.polyfit(airtemp, watertemp_V0, 1)
m2, b2 = np.polyfit(airtemp, watertemp_STQ, 1)
m3, b3 = np.polyfit(airtemp, watertemp_V100, 1)
m4, b4 = np.polyfit(airtemp, watertemp_V50, 1)
m5, b5 = np.polyfit(airtemp, watertemp_V100VD70, 1)
s1 =  "V0:", m1, "*x + ", b1
s2 = "STQ:", m2, "*x + ", b2
s3 = "V100:", m3, "*x + ", b3
s4 = "V50:", m4, "*x + ", b4
s5 = "V100VD70:", m5, "*x + ", b5

X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m1*X_plot + b1, '-', color="#d95f02")
plt.plot(X_plot, m2*X_plot + b2, '-', color="lightgrey")
plt.plot(X_plot, m3*X_plot + b3, '-', color="blue")
plt.plot(X_plot, m4*X_plot + b4, '-', color="orange")
plt.plot(X_plot, m5*X_plot + b5, '-', color="green")
plt.text(1,1,s1)

print "Spearmann STQ", (scipy.stats.spearmanr(airtemp,watertemp_STQ)[0])**2, scipy.stats.spearmanr(airtemp,watertemp_STQ)
print "Spearmann V0", (scipy.stats.spearmanr(airtemp,watertemp_V0)[0])**2
print "Spearmann V100", (scipy.stats.spearmanr(airtemp,watertemp_V100)[0])**2

r_STQ = linregress(airtemp,watertemp_STQ)[2] #r-value  coefficient of correlation
r_V0 = linregress(airtemp,watertemp_V0)[2] #r-value  coefficient of correlation
r_V100 = linregress(airtemp,watertemp_V100)[2] #r-value  coefficient of correlation

print r_STQ, r_V0, r_V100
print s1
print s2
print s3
print s4
print s5
print (m3-m1)/m3
print "p= %.2E" %(ttest_rel(m1*X_plot + b1, m3*X_plot + b3)[1])


plt.ylabel('water temperature [degC]',fontsize="large")
plt.xlabel('air temperature [degC]',fontsize="large")

ax = gca()
ax.spines['top'].set_color('none')
#ax.set_xticks([])


plt.margins(0.2)


plt.show()

fig = plt.figure()
# fig.set_size_inches(3.39,2.54)

watertemp_STQ = [WT_max[i].mean() for i in range (0,60,5)]
watertemp_V0 = [WT_max[i].mean() for i in range(1,61,5)]
watertemp_V100 = [WT_max[i].mean() for i in range(2,62,5)]
watertemp_V50 = [WT_max[i].mean() for i in range(3,62,5)]
watertemp_V100VD70 = [WT_max[i].mean() for i in range(4,62,5)]
airtemp = [TA[i] for i in range(12)]

plt.axis([16,45,15,35])
plt.scatter(airtemp,watertemp_STQ,color='lightgrey', label="STQ, mean")
plt.scatter(airtemp,watertemp_V0,color='#d95f02', label="V0, mean")
plt.scatter(airtemp,watertemp_V50, color='orange', label="V50, mean")
plt.scatter(airtemp,watertemp_V100VD70, color='green', label="V100 VD70, mean")
plt.scatter(airtemp,watertemp_V100, color='blue', label="V100, mean")


axes = plt.gca()
m1, b1 = np.polyfit(airtemp, watertemp_V0, 1)
m2, b2 = np.polyfit(airtemp, watertemp_STQ, 1)
m3, b3 = np.polyfit(airtemp, watertemp_V100, 1)
m4, b4 = np.polyfit(airtemp, watertemp_V50, 1)
m5, b5 = np.polyfit(airtemp, watertemp_V100VD70, 1)
s1 =  "V0:", m1, "*x + ", b1
s2 = "STQ:", m2, "*x + ", b2
s3 = "V100:", m3, "*x + ", b3
s4 = "V50:", m4, "*x + ", b4
s5 = "V100VD70:", m5, "*x + ", b5

X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m1*X_plot + b1, '-', color="#d95f02")
plt.plot(X_plot, m2*X_plot + b2, '-', color="lightgrey")
plt.plot(X_plot, m3*X_plot + b3, '-', color="blue") ##1b9e77
plt.plot(X_plot, m4*X_plot + b4, '-', color="orange")
plt.plot(X_plot, m5*X_plot + b5, '-', color="green")
plt.text(1,1,s1)
r_STQ = linregress(airtemp,watertemp_STQ)[2] #r-value  coefficient of correlation
r_V0 = linregress(airtemp,watertemp_V0)[2] #r-value  coefficient of correlation
r_V100 = linregress(airtemp,watertemp_V100)[2] #r-value  coefficient of correlation
print "MEAN"
print "Spearmann STQ", (scipy.stats.spearmanr(airtemp,watertemp_STQ)[0])**2, scipy.stats.spearmanr(airtemp,watertemp_STQ)
print "Spearmann V0", (scipy.stats.spearmanr(airtemp,watertemp_V0)[0])**2
print "Spearmann V100", (scipy.stats.spearmanr(airtemp,watertemp_V100)[0])**2
print "Spearmann V50", (scipy.stats.spearmanr(airtemp,watertemp_V50)[0])**2
print "Spearmann V100VD70", (scipy.stats.spearmanr(airtemp,watertemp_V100VD70)[0])**2

print r_STQ, r_V0, r_V100
print s1
print s2
print s3
print s4
print s5
print (m3-m1)/m3
print "p= %.2E" %(ttest_rel(m1*X_plot + b1, m3*X_plot + b3)[1])

plt.ylabel('water temperature [degC]',fontsize="large")
plt.xlabel('air temperature [degC]',fontsize="large")
plt.legend(loc="4")

ax = gca()
ax.spines['top'].set_color('none')
#ax.set_xticks([])
plt.margins(0.2)


plt.show()


fig = plt.figure()
# fig.set_size_inches(3.39,2.54)
watertemp_STQ = [WT_max[i].min() for i in range (0,60,5)]
watertemp_V0 = [WT_max[i].min() for i in range(1,61,5)]
watertemp_V100 = [WT_max[i].min() for i in range(2,62,5)]
watertemp_V50 = [WT_max[i].min() for i in range(3,62,5)]
watertemp_V100VD70 = [WT_max[i].min() for i in range(4,62,5)]
airtemp = [TA_min[i] for i in range(12)]

plt.axis([16,45,15,35])
#axisrange = [16,26,16,26]
plt.scatter(airtemp,watertemp_STQ,color='lightgrey', label="STQ, min")
plt.scatter(airtemp,watertemp_V0,color='#d95f02', label="V0, min")
plt.scatter(airtemp,watertemp_V50, color='orange', label="V50, min")
plt.scatter(airtemp,watertemp_V100VD70, color='green', label="V100 VD70, min")
plt.scatter(airtemp,watertemp_V100, color='blue', label="V100, min")


axes = plt.gca()
m1, b1 = np.polyfit(airtemp, watertemp_V0, 1)
m2, b2 = np.polyfit(airtemp, watertemp_STQ, 1)
m3, b3 = np.polyfit(airtemp, watertemp_V100, 1)
m4, b4 = np.polyfit(airtemp, watertemp_V50, 1)
m5, b5 = np.polyfit(airtemp, watertemp_V100VD70, 1)
s1 =  "V0:", m1, "*x + ", b1
s2 = "STQ:", m2, "*x + ", b2
s3 = "V100:", m3, "*x + ", b3
s4 = "V50:", m4, "*x + ", b4
s5 = "V100VD70:", m5, "*x + ", b5

print "MIN"
print "Spearmann STQ", (scipy.stats.spearmanr(airtemp,watertemp_STQ)[0])**2, scipy.stats.spearmanr(airtemp,watertemp_STQ)
print "Spearmann V0", (scipy.stats.spearmanr(airtemp,watertemp_V0)[0])**2
print "Spearmann V100", (scipy.stats.spearmanr(airtemp,watertemp_V100)[0])**2
print "Spearmann V50", (scipy.stats.spearmanr(airtemp,watertemp_V50)[0])**2
print "Spearmann V100VD70", (scipy.stats.spearmanr(airtemp,watertemp_V100VD70)[0])**2


X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m1*X_plot + b1, '-', color="#d95f02")
plt.plot(X_plot, m2*X_plot + b2, '-', color="lightgrey")
plt.plot(X_plot, m3*X_plot + b3, '-', color="blue")
plt.plot(X_plot, m4*X_plot + b4, '-', color="orange")
plt.plot(X_plot, m5*X_plot + b5, '-', color="green")
plt.text(1,1,s1)
r_STQ = linregress(airtemp,watertemp_STQ)[2] #r-value  coefficient of correlation
r_V0 = linregress(airtemp,watertemp_V0)[2] #r-value  coefficient of correlation
r_V100 = linregress(airtemp,watertemp_V100)[2] #r-value  coefficient of correlation

print r_STQ, r_V0, r_V100
print s1
print s2
print s3
print s4
print s5
print (m3-m1)/m3
print "p= %.2E" %(ttest_rel(m1*X_plot + b1, m3*X_plot + b3)[1])


plt.ylabel('water temperature [degC]',fontsize="large")
plt.xlabel('air temperature [degC]',fontsize="large")
plt.legend(loc="4")

ax = gca()
ax.spines['top'].set_color('none')


plt.margins(0.2)


plt.show()


fig = plt.figure()
# fig.set_size_inches(3.39,2.54)
watertemp_STQ = [WT_dailymax[i] for i in range (0,60,5)]
watertemp_V0 = [WT_dailymax[i] for i in range(1,61,5)]
watertemp_V100 = [WT_dailymin[i] for i in range(2,62,5)]
watertemp_V50 = [WT_dailymax[i] for i in range(3,62,5)]
watertemp_V100VD70 = [WT_dailymax[i] for i in range(4,62,5)]
airtemp = [TA_dailymax[i] for i in range(12)]

plt.axis([16,45,15,35])
plt.scatter(airtemp,watertemp_STQ,color='lightgrey', label="STQ, dailymax")
plt.scatter(airtemp,watertemp_V0,color='#d95f02', label="V0, dailymax")
plt.scatter(airtemp,watertemp_V50, color='orange', label="V50, dailymax")
plt.scatter(airtemp,watertemp_V100VD70, color='green', label="V100 VD70, dailymax")
plt.scatter(airtemp,watertemp_V100, color='blue', label="V100, dailymax")

axes = plt.gca()
m1, b1 = np.polyfit(airtemp, watertemp_V0, 1)
m2, b2 = np.polyfit(airtemp, watertemp_STQ, 1)
m3, b3 = np.polyfit(airtemp, watertemp_V100, 1)
m4, b4 = np.polyfit(airtemp, watertemp_V50, 1)
m5, b5 = np.polyfit(airtemp, watertemp_V100VD70, 1)
s1 =  "V0:", m1, "*x + ", b1
s2 = "STQ:", m2, "*x + ", b2
s3 = "V100:", m3, "*x + ", b3
s4 = "V50:", m4, "*x + ", b4
s5 = "V100VD70:", m5, "*x + ", b5

print "DAILYMAX"
print "Spearmann STQ", (scipy.stats.spearmanr(airtemp,watertemp_STQ)[0])**2, scipy.stats.spearmanr(airtemp,watertemp_STQ)
print "Spearmann V0", (scipy.stats.spearmanr(airtemp,watertemp_V0)[0])**2
print "Spearmann V100", (scipy.stats.spearmanr(airtemp,watertemp_V100)[0])**2
print "Spearmann V50", (scipy.stats.spearmanr(airtemp,watertemp_V50)[0])**2
print "Spearmann V100VD70", (scipy.stats.spearmanr(airtemp,watertemp_V100VD70)[0])**2

X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m1*X_plot + b1, '-', color="#d95f02")
plt.plot(X_plot, m2*X_plot + b2, '-', color="lightgrey")
plt.plot(X_plot, m3*X_plot + b3, '-', color="blue")
plt.plot(X_plot, m4*X_plot + b4, '-', color="orange")
plt.plot(X_plot, m5*X_plot + b5, '-', color="green")
plt.text(1,1,s1)
r_STQ = linregress(airtemp,watertemp_STQ)[2] #r-value  coefficient of correlation
r_V0 = linregress(airtemp,watertemp_V0)[2] #r-value  coefficient of correlation
r_V100 = linregress(airtemp,watertemp_V100)[2] #r-value  coefficient of correlation

print r_STQ, r_V0, r_V100
print s1
print s2
print s3
print s4
print s5
print (m3-m1)/m3
print "p= %.2E" %(ttest_rel(m1*X_plot + b1, m3*X_plot + b3)[1])

plt.ylabel('water temperature [degC]',fontsize="large")
plt.xlabel('air temperature [degC]',fontsize="large")
plt.legend(loc="2")
ax = gca()
ax.spines['top'].set_color('none')
plt.margins(0.2)
plt.show()


fig = plt.figure()
# fig.set_size_inches(3.39,2.54)
watertemp_STQ = [WT_dailymin[i] for i in range (0,60,5)]
watertemp_V0 = [WT_dailymin[i] for i in range(1,61,5)]
watertemp_V100 = [WT_dailymin[i] for i in range(2,62,5)]
watertemp_V50 = [WT_dailymin[i] for i in range(3,62,5)]
watertemp_V100VD70 = [WT_dailymin[i] for i in range(4,62,5)]
airtemp = [TA_dailymin[i] for i in range(12)]


plt.axis([16,45,15,35])
#axisrange = [16,26,16,26]
plt.scatter(airtemp,watertemp_STQ,color='lightgrey', label="STQ, dailymin")
plt.scatter(airtemp,watertemp_V0,color='#d95f02', label="V0, dailymin")
plt.scatter(airtemp,watertemp_V50, color='orange', label="V50, dailymin")
plt.scatter(airtemp,watertemp_V100VD70, color='green', label="V100 VD70, dailymin")
plt.scatter(airtemp,watertemp_V100, color='blue', label="V100, dailymin")

axes = plt.gca()
m1, b1 = np.polyfit(airtemp, watertemp_V0, 1)
m2, b2 = np.polyfit(airtemp, watertemp_STQ, 1)
m3, b3 = np.polyfit(airtemp, watertemp_V100, 1)
m4, b4 = np.polyfit(airtemp, watertemp_V50, 1)
m5, b5 = np.polyfit(airtemp, watertemp_V100VD70, 1)
s1 =  "V0:", m1, "*x + ", b1
s2 = "STQ:", m2, "*x + ", b2
s3 = "V100:", m3, "*x + ", b3
s4 = "V50:", m4, "*x + ", b4
s5 = "V100VD70:", m5, "*x + ", b5

print "DAILYMIN"
print "Spearmann STQ", (scipy.stats.spearmanr(airtemp,watertemp_STQ)[0])**2, scipy.stats.spearmanr(airtemp,watertemp_STQ)
print "Spearmann V0", (scipy.stats.spearmanr(airtemp,watertemp_V0)[0])**2
print "Spearmann V100", (scipy.stats.spearmanr(airtemp,watertemp_V100)[0])**2
print "Spearmann V50", (scipy.stats.spearmanr(airtemp,watertemp_V50)[0])**2
print "Spearmann V100VD70", (scipy.stats.spearmanr(airtemp,watertemp_V100VD70)[0])**2
X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m1*X_plot + b1, '-', color="#d95f02")
plt.plot(X_plot, m2*X_plot + b2, '-', color="lightgrey")
plt.plot(X_plot, m3*X_plot + b3, '-', color="blue")
plt.plot(X_plot, m4*X_plot + b4, '-', color="orange")
plt.plot(X_plot, m5*X_plot + b5, '-', color="green")
plt.text(1,1,s1)
r_STQ = linregress(airtemp,watertemp_STQ)[2] #r-value  coefficient of correlation
r_V0 = linregress(airtemp,watertemp_V0)[2] #r-value  coefficient of correlation
r_V100 = linregress(airtemp,watertemp_V100)[2] #r-value  coefficient of correlation

print r_STQ, r_V0, r_V100
print s1
print s2
print s3
print s4
print s5
print (m3-m1)/m3
print "daily min",(m5-m4)/m5
print "p= %.2E" %(ttest_rel(m1*X_plot + b1, m3*X_plot + b3)[1])

plt.ylabel('water temperature [degC]',fontsize="large")
plt.xlabel('air temperature [degC]',fontsize="large")
#plt.legend(loc="1")
ax = gca()
ax.spines['top'].set_color('none')
plt.margins(0.2)
plt.show()