__author__ = 'lnx'

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
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
        '/home/lnx/PycharmProjects/HS/S196_P_STQ_2030_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S197_P_V0_2030_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S198_P_V100_2030_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S202_P_STQ_2030_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S203_P_V0_2030_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S204_P_V100_2030_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S214_P_STQ_2030_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S215_P_V0_2030_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S216_P_V100_2030_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S220_P_STQ_2050_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S221_P_V0_2050_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S222_P_V100_2050_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S226_P_STQ_2050_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S227_P_V0_2050_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S228_P_V100_2050_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S232_P_STQ_2050_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S233_P_V0_2050_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S234_P_V100_2050_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S244_P_STQ_2050_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S245_P_V0_2050_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S246_P_V100_2050_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S256_P_STQ_2085_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S257_P_V0_2085_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S258_P_V100_2085_5a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S274_P_STQ_2085_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S275_P_V0_2085_Max_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S276_P_V100_2085_Max_MLF/outputfiles/Temp_H2O.txt'
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

watertemp_STQ = [WT_max[0].max(), WT_max[3].max(), WT_max[6].max(),WT_max[9].max(),  WT_max[12].max(),WT_max[15].max(), WT_max[18].max(), WT_max[21].max(), WT_max[24].max(), WT_max[27].max(), WT_max[30].max(), WT_max[33].max()]
watertemp_V0 = [WT_max[1].max(), WT_max[4].max(),WT_max[7].max(), WT_max[10].max(), WT_max[13].max(),WT_max[16].max(), WT_max[19].max(), WT_max[22].max(), WT_max[25].max(), WT_max[28].max(), WT_max[31].max(), WT_max[34].max()]
watertemp_V100 = [WT_max[2].max(), WT_max[5].max(), WT_max[8].max(), WT_max[11].max(), WT_max[14].max(),WT_max[17].max(), WT_max[20].max(), WT_max[23].max(), WT_max[26].max(), WT_max[29].max(), WT_max[32].max(), WT_max[35].max()]
airtemp = [TA_max[0], TA_max[1], TA_max[2], TA_max[3], TA_max[4],TA_max[5],TA_max[6],TA_max[7],TA_max[8],TA_max[9],TA_max[10],TA_max[11]]

print len(watertemp_V0)
#print watertemp_STQ
print len(airtemp)
#print airtemp
#plt.axis([25,45,15,35])
plt.axis([16,45,15,35])
plt.scatter(airtemp,watertemp_V0,color='#d95f02', label="V0, max")
plt.scatter(airtemp,watertemp_STQ,color='black', label="STQ, max")
plt.scatter(airtemp,watertemp_V100, color='#1b9e77', label="V100, max")
plt.legend(loc="4")

axes = plt.gca()
m1, b1 = np.polyfit(airtemp, watertemp_V0, 1)
m2, b2 = np.polyfit(airtemp, watertemp_STQ, 1)
m3, b3 = np.polyfit(airtemp, watertemp_V100, 1)
s1 =  "V0:", m1, "*x + ", b1
s2 = "STQ:", m2, "*x + ", b2
s3 = "V100:", m3, "*x + ", b3

X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m1*X_plot + b1, '-', color="#d95f02")
plt.plot(X_plot, m2*X_plot + b2, '-', color="black")
plt.plot(X_plot, m3*X_plot + b3, '-', color="#1b9e77")
plt.text(1,1,s1)
r_STQ = linregress(airtemp,watertemp_STQ)[2] #r-value  coefficient of correlation
r_V0 = linregress(airtemp,watertemp_V0)[2] #r-value  coefficient of correlation
r_V100 = linregress(airtemp,watertemp_V100)[2] #r-value  coefficient of correlation

print r_STQ, r_V0, r_V100
print s1
print s2
print s3
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

watertemp_STQ = [WT_max[0].mean(), WT_max[3].mean(), WT_max[6].mean(),WT_max[9].mean(),  WT_max[12].mean(),WT_max[15].mean(), WT_max[18].mean(), WT_max[21].mean(), WT_max[24].mean(), WT_max[27].mean(), WT_max[30].mean(), WT_max[33].mean() ]
watertemp_V0 = [WT_max[1].mean(), WT_max[4].mean(),WT_max[7].mean(), WT_max[10].mean(), WT_max[13].mean(),WT_max[16].mean(), WT_max[19].mean(), WT_max[22].mean(), WT_max[25].mean(), WT_max[28].mean(), WT_max[31].mean(), WT_max[34].mean() ]
watertemp_V100 = [WT_max[2].mean(), WT_max[5].mean(), WT_max[8].mean(), WT_max[11].mean(), WT_max[14].mean(),WT_max[17].mean(), WT_max[20].mean(), WT_max[23].mean(), WT_max[26].mean(), WT_max[29].mean(), WT_max[32].mean(), WT_max[35].mean() ]
airtemp = [TA[0],TA[1],TA[2],TA[3],TA[4],TA[5],TA[6],TA[7],TA[8],TA[9],TA[10],TA[11]]

plt.axis([16,45,15,35])
plt.scatter(airtemp,watertemp_V0,color='#d95f02', label="V0, mean")
plt.scatter(airtemp,watertemp_STQ,color='black', label="STQ, mean")
plt.scatter(airtemp,watertemp_V100, color='#1b9e77', label="V100, mean")

axes = plt.gca()
m1, b1 = np.polyfit(airtemp, watertemp_V0, 1)
m2, b2 = np.polyfit(airtemp, watertemp_STQ, 1)
m3, b3 = np.polyfit(airtemp, watertemp_V100, 1)
s1 =  "V0:", m1, "*x + ", b1
s2 = "STQ:", m2, "*x + ", b2
s3 = "V100:", m3, "*x + ", b3

X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m1*X_plot + b1, '-',color='#d95f02')
plt.plot(X_plot, m2*X_plot + b2, '-', color='black')
plt.plot(X_plot, m3*X_plot + b3, '-', color='#1b9e77')
plt.text(1,1,s1)
r = linregress(airtemp,watertemp_STQ)[2] #r-value  coefficient of correlation

print s1
print s2
print s3
print (m3-m1)/m3

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

watertemp_STQ = [WT_max[0].min(), WT_max[3].min(), WT_max[6].min(),WT_max[9].min(),  WT_max[12].min(),WT_max[15].min(), WT_max[18].min(), WT_max[21].min(), WT_max[24].min(), WT_max[27].min(), WT_max[30].min(), WT_max[33].min() ]
watertemp_V0 = [WT_max[1].min(), WT_max[4].min(),WT_max[7].min(), WT_max[10].min(), WT_max[13].min(),WT_max[16].min(), WT_max[19].min(), WT_max[22].min(), WT_max[25].min(), WT_max[28].min(), WT_max[31].min(), WT_max[34].min() ]
watertemp_V100 = [WT_max[2].min(), WT_max[5].min(), WT_max[8].min(), WT_max[11].min(), WT_max[14].min(),WT_max[17].min(), WT_max[20].min(), WT_max[23].min(), WT_max[26].min(), WT_max[29].min(), WT_max[32].min(), WT_max[35].min() ]
airtemp = [TA_min[0], TA_min[1], TA_min[2], TA_min[3], TA_min[4],TA_min[5],TA_min[6],TA_min[7],TA_min[8],TA_min[9],TA_min[10],TA_min[11]]
plt.axis([16,45,15,35])
#axisrange = [16,26,16,26]
plt.scatter(airtemp,watertemp_V0,color='#d95f02', label="V0, min")
plt.scatter(airtemp,watertemp_STQ,color='black', label="STQ, min")
plt.scatter(airtemp,watertemp_V100, color='#1b9e77', label="V100, min")

axes = plt.gca()
m1, b1 = np.polyfit(airtemp, watertemp_V0, 1)
m2, b2 = np.polyfit(airtemp, watertemp_STQ, 1)
m3, b3 = np.polyfit(airtemp, watertemp_V100, 1)
s1 =  "V0:", m1, "*x + ", b1
s2 = "STQ:", m2, "*x + ", b2
s3 = "V100:", m3, "*x + ", b3

X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m1*X_plot + b1, '-', color="#d95f02")
plt.plot(X_plot, m2*X_plot + b2, '-', color="black")
plt.plot(X_plot, m3*X_plot + b3, '-', color="#1b9e77")
plt.text(1,1,s1)
r_STQ = linregress(airtemp,watertemp_STQ)[2] #r-value  coefficient of correlation
r_V0 = linregress(airtemp,watertemp_V0)[2] #r-value  coefficient of correlation
r_V100 = linregress(airtemp,watertemp_V100)[2] #r-value  coefficient of correlation

print r_STQ, r_V0, r_V100
print s1
print s2
print s3
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
watertemp_STQ = [WT_dailymax[0], WT_dailymax[3], WT_dailymax[6],WT_dailymax[9],  WT_dailymax[12],WT_dailymax[15], WT_dailymax[18], WT_dailymax[21], WT_dailymax[24], WT_dailymax[27], WT_dailymax[30], WT_dailymax[33]]
watertemp_V0 = [WT_dailymax[1], WT_dailymax[4] ,WT_dailymax[7] , WT_dailymax[10], WT_dailymax[13],WT_dailymax[16] , WT_dailymax[19] , WT_dailymax[22] , WT_dailymax[25] , WT_dailymax[28] , WT_dailymax[31] , WT_dailymax[34]]
watertemp_V100 = [WT_dailymax[2] , WT_dailymax[5] , WT_dailymax[8] , WT_dailymax[11], WT_dailymax[14] ,WT_dailymax[17] , WT_dailymax[20] , WT_dailymax[23] , WT_dailymax[26] , WT_dailymax[29] , WT_dailymax[32] , WT_dailymax[35]]
airtemp = [TA_dailymax[0], TA_dailymax[1], TA_dailymax[2], TA_dailymax[3], TA_dailymax[4],TA_dailymax[5],TA_dailymax[6],TA_dailymax[7],TA_dailymax[8],TA_dailymax[9],TA_dailymax[10],TA_dailymax[11]]

plt.axis([16,45,15,35])
plt.scatter(airtemp,watertemp_V0,color='#d95f02', label="V0, dailymax")
plt.scatter(airtemp,watertemp_STQ,color='black', label="STQ, dailymax")
plt.scatter(airtemp,watertemp_V100, color='#1b9e77', label="V100, dailymax")

axes = plt.gca()
m1, b1 = np.polyfit(airtemp, watertemp_V0, 1)
m2, b2 = np.polyfit(airtemp, watertemp_STQ, 1)
m3, b3 = np.polyfit(airtemp, watertemp_V100, 1)
s1 =  "V0:", m1, "*x + ", b1
s2 = "STQ:", m2, "*x + ", b2
s3 = "V100:", m3, "*x + ", b3

X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m1*X_plot + b1, '-', color="#d95f02")
plt.plot(X_plot, m2*X_plot + b2, '-', color="black")
plt.plot(X_plot, m3*X_plot + b3, '-', color="#1b9e77")
plt.text(1,1,s1)
r_STQ = linregress(airtemp,watertemp_STQ)[2] #r-value  coefficient of correlation
r_V0 = linregress(airtemp,watertemp_V0)[2] #r-value  coefficient of correlation
r_V100 = linregress(airtemp,watertemp_V100)[2] #r-value  coefficient of correlation

print r_STQ, r_V0, r_V100
print s1
print s2
print s3
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
watertemp_STQ = [WT_dailymin[i] for i in range (0,36,3)]
watertemp_V0 = [WT_dailymin[i] for i in range(1,37,3)]
watertemp_V100 = [WT_dailymin[i] for i in range(2,38,3)]
airtemp = [TA_dailymin[i] for i in range(12)]

plt.axis([16,45,15,35])
#axisrange = [16,26,16,26]
plt.scatter(airtemp,watertemp_V0,color='#d95f02', label="V0, dailymin")
plt.scatter(airtemp,watertemp_STQ,color='black', label="STQ, dailymin")
plt.scatter(airtemp,watertemp_V100, color='#1b9e77', label="V100, dailymin")

axes = plt.gca()
m1, b1 = np.polyfit(airtemp, watertemp_V0, 1)
m2, b2 = np.polyfit(airtemp, watertemp_STQ, 1)
m3, b3 = np.polyfit(airtemp, watertemp_V100, 1)
s1 =  "V0:", m1, "*x + ", b1
s2 = "STQ:", m2, "*x + ", b2
s3 = "V100:", m3, "*x + ", b3

X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m1*X_plot + b1, '-', color="#d95f02")
plt.plot(X_plot, m2*X_plot + b2, '-', color="black")
plt.plot(X_plot, m3*X_plot + b3, '-', color="#1b9e77")
plt.text(1,1,s1)
r_STQ = linregress(airtemp,watertemp_STQ)[2] #r-value  coefficient of correlation
r_V0 = linregress(airtemp,watertemp_V0)[2] #r-value  coefficient of correlation
r_V100 = linregress(airtemp,watertemp_V100)[2] #r-value  coefficient of correlation

print r_STQ, r_V0, r_V100
print s1
print s2
print s3
print (m3-m1)/m3
print "p= %.2E" %(ttest_rel(m1*X_plot + b1, m3*X_plot + b3)[1])

plt.ylabel('water temperature [degC]',fontsize="large")
plt.xlabel('air temperature [degC]',fontsize="large")
plt.legend(loc="2")
ax = gca()
ax.spines['top'].set_color('none')
plt.margins(0.2)
plt.show()