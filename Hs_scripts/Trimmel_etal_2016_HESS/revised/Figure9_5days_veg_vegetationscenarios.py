__author__ = 'lnx'

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
from scipy.stats import *


path = ['/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S301_P_V100_VD07_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S306_P_V100_VD05_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S303_P_V50_VD09_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S302_P_V50_VD07_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S307_P_V50_VD05_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        '/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Temp_H2O.txt',
        ]

#'/home/lnx/PycharmProjects/HS/S305_P_V100_VD04_2085_20a_MLF/outputfiles/Temp_H2O.txt',
#'/home/lnx/PycharmProjects/HS/S304_P_V50_VD04_2085_20a_MLF/outputfiles/Temp_H2O.txt',

x = len(path)
WT = range(x)
WT_dailymax = range(x)
WT_dailymin = range(x)

for i in range(len(path)):
    WT[i] =  pd.read_csv(path[i], skiprows=6, sep='\s+')
    WT[i]['realdate'] = pd.TimedeltaIndex(WT[i]['Datetime'], unit='d') +  datetime.datetime(1900,1,1,0,0,0)
    #WT[i] = WT[i].set_index('realdate')
    #print WT_max[i].head()
    #WT_dailymax[i] = WT[i]['61.000'].resample('D', how='max').mean()
    #WT_dailymin[i] = WT[i]['61.000'].resample('D', how='min').mean()
    #WT[i] = WT[i].ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column  1.July-3.Aug: 744+72=816h
    #WT[i] = np.array(WT[i]['61.000']) #select only reference station Unterwart DFM 61km ~ DFS 39
    #WT[i] = WT[i].ravel()

"""
(fig, ax) = plt.figure()#sharex= True, sharey= True)

ax = fig.add_subplot(211)
ax.set_title('height = 30m,MLF')
ax.plot(WT[0]['80.000'][-24:], linestyle='-', color = 'blue', label='VD90')
ax.plot(WT[1]['80.000'][-24:], linestyle='-', color = 'green', label='VD70')
ax.plot(WT[2]['80.000'][-24:], linestyle='-', color = 'orange', label='VD50')
ax.plot(WT[3]['80.000'][-24:], linestyle='- -', color = 'blue', label='VD90')
ax.plot(WT[4]['80.000'][-24:], linestyle='- -', color = 'green', label='VD70')
ax.plot(WT[5]['80.000'][-24:], linestyle='- -', color = 'orange', label='VD50')
ax.plot(WT[6]['80.000'][-24:], linestyle='-', color = 'red', label='V0')
plt.setp(ax.get_xticklabels(), visible=False)
ax.set_ylim([10,39])
ax.set_ylabel('water temperature [degC]', fontsize='large')

ax = fig.add_subplot(222)
ax.set_title('height = 15m,MLF')
ax.plot(WT[3]['80.000'][-24:], linestyle='- -', color = 'blue', label='VD90')
ax.plot(WT[4]['80.000'][-24:], linestyle='- -', color = 'green', label='VD70')
ax.plot(WT[5]['80.000'][-24:], linestyle='- -', color = 'orange', label='VD50')
ax.plot(WT[6]['80.000'][-24:], linestyle='- -', color = 'red', label='V0')
plt.setp(ax.get_xticklabels(), visible=False)
ax.set_ylim([10,39])
plt.setp(ax.get_yticklabels(), visible=False)

plt.show()
"""

fig = plt.figure()

plt.title('DFS 20, 2085/20a')
plt.plot(WT[0]['80.000'][-24:], linestyle='-', color = 'blue', label='VD90, VH100')
plt.plot(WT[3]['80.000'][-24:], linestyle='-', color = 'orange', label='VD90, VH50')
plt.plot(WT[7]['80.000'][-24:], linestyle='-', color = 'black', label='STQ')
plt.plot(WT[1]['80.000'][-24:], linestyle='--', color = 'blue', label='VD70, VH100')
plt.plot(WT[4]['80.000'][-24:], linestyle='--', color = 'orange', label='VD70, VH50')
plt.plot(WT[6]['80.000'][-24:], linestyle=':', color = 'red', linewidth='3', label='V0')
plt.plot(WT[2]['80.000'][-24:], linestyle=':', color = 'blue',  linewidth='3',label='VD50, VH100')
plt.plot(WT[5]['80.000'][-24:], linestyle=':', color = 'orange',  linewidth='3',label='VD50, VH50')
#plt.setp(plt.get_xticklabels(), visible=False)
plt.ylim([18,30])
plt.xlim([-1,24])
plt.ylabel('water temperature [degC]', fontsize='large')
plt.legend(loc=3, ncol=3)
plt.grid()
plt.show()

""""
fig = plt.figure()

plt.title('DFS 20, 2085/20a')
plt.plot(WT[0]['80.000'][-24:], linestyle='-', color = 'blue', label='VD90, VH100')
plt.plot(WT[3]['80.000'][-24:], linestyle='--', color = 'blue', label='VD90, VH50')
plt.plot(WT[6]['80.000'][-24:], linestyle='-', color = 'red', label='V0')
plt.plot(WT[1]['80.000'][-24:], linestyle='-', color = 'green', label='VD70, VH100')
plt.plot(WT[4]['80.000'][-24:], linestyle='--', color = 'green', label='VD70, VH50')
plt.plot(WT[7]['80.000'][-24:], linestyle='-', color = 'black', label='STQ')
plt.plot(WT[2]['80.000'][-24:], linestyle='-', color = 'orange', label='VD50, VH100')
plt.plot(WT[5]['80.000'][-24:], linestyle='--', color = 'orange', label='VD50, VH50')
#plt.setp(plt.get_xticklabels(), visible=False)
plt.ylim([18,30])
plt.xlim([-1,24])
plt.ylabel('water temperature [degC]', fontsize='large')
plt.legend(loc=3, ncol=3)
plt.grid()
plt.show()


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

"""