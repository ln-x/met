from __future__ import print_function  # Only needed for Python 2
# -*- coding: utf-8 -*-
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
from scipy.stats import *
import scipy.stats as ss
from urllib2 import urlopen
import pandas
from statsmodels.formula.api import ols
from statsmodels.graphics.api import interaction_plot, abline_plot
from statsmodels.stats.anova import anova_lm
#import operator
import itertools

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
WT_dailymean = range(x)

for i in range(len(path)):
    WT_max[i] =  pd.read_csv(path[i], skiprows=6, sep='\s+')
    WT_max[i]['realdate'] = pd.TimedeltaIndex(WT_max[i]['Datetime'], unit='d') +  datetime.datetime(1900,1,1,0,0,0)
    WT_max[i] = WT_max[i].set_index('realdate')
    WT_dailymax[i] = WT_max[i]['61.000'].resample('D').max()
    WT_dailymin[i] = WT_max[i]['61.000'].resample('D').min()
    WT_dailymean[i] = WT_max[i]['61.000'].resample('D').mean()
    #print WT_dailymax[i].head()

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
TA_dailymean = range(y)
TA_dailymax = range(y)
TA_dailymin = range(y)
#print y

for i in range(len(C_path)):
    #print i
    C[i] = pd.read_csv(C_path[i], sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
    C[i] = C[i].set_index('datetime')
    TA_dailymean[i] = C[i]['AirT'].resample('D').mean()
    TA_dailymax[i] = C[i]['AirT'].resample('D').max()
    TA_dailymin[i] = C[i]['AirT'].resample('D').min()
    #print WT_dailymax[i].head()


fig, (ax, ax1, ax2) = plt.subplots(3,1, sharex= True)
# fig.set_size_inches(3.39,2.54)
watertemp_STQ = [WT_dailymean[i] for i in range (0,60,5)]
watertemp_V0 = [WT_dailymean[i] for i in range(1,61,5)]
watertemp_V100 = [WT_dailymean[i] for i in range(2,62,5)]
watertemp_V50 = [WT_dailymean[i] for i in range(3,62,5)]
watertemp_V100VD70 = [WT_dailymean[i] for i in range(4,62,5)]
airtemp = [TA_dailymean[i] for i in range(12)]
#print len(airtemp[1]), len(watertemp_STQ[1])

watertemp_STQall = []
watertemp_V0all = []
watertemp_V100all = []
watertemp_V50all = []
watertemp_V100VD70all = []
airtemp_all = []

for i in range(len(watertemp_STQ)):
    watertemp_STQall.append(watertemp_STQ[i])
    watertemp_V0all.append(watertemp_V0[i])
    watertemp_V100all.append(watertemp_V100[i])
    watertemp_V50all.append(watertemp_V50[i])
    watertemp_V100VD70all.append(watertemp_V100VD70[i])
    airtemp_all.append(airtemp[i])

#print len(airtemp_all), len(watertemp_V0all)
#print type(watertemp_STQall)
ax.scatter(airtemp_all,watertemp_STQall,color='lightgrey', s=3, label=u"STQ,  R²=0.92")
ax.scatter(airtemp_all,watertemp_V0all,color='#d95f02',  s=3,label=u"V0,     R²=0.89")
ax.scatter(airtemp_all,watertemp_V50all, color='orange',  s=3,label=u"V50,   R²=0.91")
ax.scatter(airtemp_all,watertemp_V100VD70all, color='green',  s=3,label=u"V70,   R²=0.91")
ax.scatter(airtemp_all,watertemp_V100all, color='blue',  s=3,label=u"V100, R²=0.90")
#data_df = 1
#data_sd = np.std(watertemp_STQall,axis=0)
#print data_sd
#ax.errorbar(airtemp_all,watertemp_STQall, yerr=ss.t.ppf(0.95, data_df)*data_sd)

ax.axis([10,40,10,40])
ax.set_ylabel(u'water temperature [°C]',fontsize="large")
#ax.set_xlabel(u'air temperature [°C]',fontsize="large")
ax.legend(loc="upper left", title="DAILY MEAN")

airtemp_all = np.array(airtemp_all,dtype=pd.Series)
watertemp_STQall = np.array(watertemp_STQall,dtype=pd.Series)
watertemp_V0all = np.array(watertemp_V0all,dtype=pd.Series)
watertemp_V50all = np.array(watertemp_V50all,dtype=pd.Series)
watertemp_V100all = np.array(watertemp_V100all,dtype=pd.Series)
watertemp_V100VD70all = np.array(watertemp_V100VD70all,dtype=pd.Series)
#airtemp_all2 = reduce(operator.add, airtemp_all1) #Version1
#airtemp_all2 = reduce(lambda x,y: x+y,airtemp_all1) #Version2
airtemp_all1 = list(itertools.chain(*airtemp_all)) #Version3
watertemp_STQall1 = list(itertools.chain(*watertemp_STQall))
watertemp_V0all1 = list(itertools.chain(*watertemp_V0all))
watertemp_V50all1 = list(itertools.chain(*watertemp_V50all))
watertemp_V100all1 = list(itertools.chain(*watertemp_V100all))
watertemp_V100VD70all1 = list(itertools.chain(*watertemp_V100VD70all))

all = pd.DataFrame({'air':airtemp_all1,'STQ':watertemp_STQall1, 'V0':watertemp_V0all1,'V50': watertemp_V50all1, 'V70':watertemp_V100VD70all1, 'V100':watertemp_V100all1})
#print (all.head())
all.to_csv("/home/lnx/dailymeans.csv", index=False, cols=('air','STQ','V0','V50','V70','V100'))


covariance = np.cov(airtemp_all1,watertemp_STQall1,bias=True)[0][1]
print (covariance)


#factor_groups

formula = ''

axes = plt.gca()
STQpoly = np.polyfit(airtemp_all1, watertemp_V0all1, 1, full=False, cov=True)
m1, b1 = np.polyfit(airtemp_all1, watertemp_V0all1, 1)

#print STQpoly
#print m1,b1

m2, b2 = np.polyfit(airtemp_all1, watertemp_STQall1, 1)
m3, b3 = np.polyfit(airtemp_all1, watertemp_V100all1, 1)
m4, b4 = np.polyfit(airtemp_all1, watertemp_V50all1, 1)
m5, b5 = np.polyfit(airtemp_all1, watertemp_V100VD70all1, 1)
X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)


ax = gca()
ax.spines['top'].set_color('none')
#ax.set_xticks([])
ax.margins(0.2)
#plt.show()

#fig = plt.figure()
# fig.set_size_inches(3.39,2.54)
watertemp_STQ = [WT_dailymin[i] for i in range (0,60,5)]
watertemp_V0 = [WT_dailymin[i] for i in range(1,61,5)]
watertemp_V100 = [WT_dailymin[i] for i in range(2,62,5)]
watertemp_V50 = [WT_dailymin[i] for i in range(3,62,5)]
watertemp_V100VD70 = [WT_dailymin[i] for i in range(4,62,5)]
airtemp = [TA_dailymean[i] for i in range(12)]

watertemp_STQall = []
watertemp_V0all = []
watertemp_V100all = []
watertemp_V50all = []
watertemp_V100VD70all = []
airtemp_all = []

for i in range(len(watertemp_STQ)):
    watertemp_STQall.append(watertemp_STQ[i])
    watertemp_V0all.append(watertemp_V0[i])
    watertemp_V100all.append(watertemp_V100[i])
    watertemp_V50all.append(watertemp_V50[i])
    watertemp_V100VD70all.append(watertemp_V100VD70[i])
    airtemp_all.append(airtemp[i])

ax1.axis([5,35,5,35])
#axisrange = [16,26,16,26]
ax1.scatter(airtemp_all,watertemp_STQall,color='lightgrey',  s=3,label=u"STQ,  R²=0.88")
ax1.scatter(airtemp_all,watertemp_V0all,color='#d95f02', s=3, label=u"V0,     R²=0.86")
ax1.scatter(airtemp_all,watertemp_V50all, color='orange', s=3, label=u"V50,   R²=0.87")
ax1.scatter(airtemp_all,watertemp_V100VD70all, color='green', s=3, label=u"V70,   R²=0.87")
ax1.scatter(airtemp_all,watertemp_V100all, color='blue', s=3, label=u"V100, R²=0.86")

airtemp_all = np.array(airtemp_all,dtype=pd.Series)
watertemp_STQall = np.array(watertemp_STQall,dtype=pd.Series)
watertemp_V0all = np.array(watertemp_V0all,dtype=pd.Series)
watertemp_V50all = np.array(watertemp_V50all,dtype=pd.Series)
watertemp_V100all = np.array(watertemp_V100all,dtype=pd.Series)
watertemp_V100VD70all = np.array(watertemp_V100VD70all,dtype=pd.Series)

airtemp_all1 = list(itertools.chain(*airtemp_all))
watertemp_STQall1 = list(itertools.chain(*watertemp_STQall))
watertemp_V0all1 = list(itertools.chain(*watertemp_V0all))
watertemp_V50all1 = list(itertools.chain(*watertemp_V50all))
watertemp_V100all1 = list(itertools.chain(*watertemp_V100all))
watertemp_V100VD70all1 = list(itertools.chain(*watertemp_V100VD70all))

allmin = pd.DataFrame({'air':airtemp_all1,'STQ':watertemp_STQall1, 'V0':watertemp_V0all1,'V50': watertemp_V50all1, 'V70':watertemp_V100VD70all1, 'V100':watertemp_V100all1})
#print (all.head())
allmin.to_csv("/home/lnx/dailymin.csv", index=False, cols=('air','STQ','V0','V50','V70','V100'))


axes = plt.gca()
m1, b1 = np.polyfit(airtemp_all1, watertemp_V0all1, 1)
m2, b2 = np.polyfit(airtemp_all1, watertemp_STQall1, 1)
m3, b3 = np.polyfit(airtemp_all1, watertemp_V100all1, 1)
m4, b4 = np.polyfit(airtemp_all1, watertemp_V50all1, 1)
m5, b5 = np.polyfit(airtemp_all1, watertemp_V100VD70all1, 1)

ax1.set_ylabel(u'water temperature [°C]',fontsize="large")
#ax1.set_xlabel(u'air temperature [°C]',fontsize="large")
plt.setp(ax.get_xticklabels(), visible=False)

ax1.legend(loc="upper left", title="DAILY MINIMA")
ax1.text(32,32,"b", horizontalalignment='center', verticalalignment='center',fontsize=20,
         bbox=dict(facecolor='none', edgecolor='black', pad=10.0))
ax1 = gca()
ax1.spines['top'].set_color('none')


#plt.margins(0.2)


#plt.show()


#fig = plt.figure()
# fig.set_size_inches(3.39,2.54)
watertemp_STQ = [WT_dailymax[i] for i in range (0,60,5)]
watertemp_V0 = [WT_dailymax[i] for i in range(1,61,5)]
watertemp_V100 = [WT_dailymax[i] for i in range(2,62,5)]
watertemp_V50 = [WT_dailymax[i] for i in range(3,62,5)]
watertemp_V100VD70 = [WT_dailymax[i] for i in range(4,62,5)]
airtemp = [TA_dailymax[i] for i in range(12)]

watertemp_STQall = []
watertemp_V0all = []
watertemp_V100all = []
watertemp_V50all = []
watertemp_V100VD70all = []
airtemp_all = []

for i in range(len(watertemp_STQ)):
    watertemp_STQall.append(watertemp_STQ[i])
    watertemp_V0all.append(watertemp_V0[i])
    watertemp_V100all.append(watertemp_V100[i])
    watertemp_V50all.append(watertemp_V50[i])
    watertemp_V100VD70all.append(watertemp_V100VD70[i])
    airtemp_all.append(airtemp[i])

ax2.axis([10,45,10,45])
ax2.scatter(airtemp,watertemp_STQall,color='lightgrey', s=3, label=u"STQ,  R²=0.93")
ax2.scatter(airtemp,watertemp_V0all,color='#d95f02', s=3, label=u"V0,     R²=0.88")
ax2.scatter(airtemp,watertemp_V50all, color='orange', s=3, label=u"V50,   R²=0.90")
ax2.scatter(airtemp,watertemp_V100VD70all, color='green', s=3, label=u"V70,   R²=0.90")
ax2.scatter(airtemp,watertemp_V100all, color='blue', s=3, label=u"V100, R²=0.78")

airtemp_all = np.array(airtemp_all,dtype=pd.Series)
watertemp_STQall = np.array(watertemp_STQall,dtype=pd.Series)
watertemp_V0all = np.array(watertemp_V0all,dtype=pd.Series)
watertemp_V50all = np.array(watertemp_V50all,dtype=pd.Series)
watertemp_V100all = np.array(watertemp_V100all,dtype=pd.Series)
watertemp_V100VD70all = np.array(watertemp_V100VD70all,dtype=pd.Series)

airtemp_all1 = list(itertools.chain(*airtemp_all))
watertemp_STQall1 = list(itertools.chain(*watertemp_STQall))
watertemp_V0all1 = list(itertools.chain(*watertemp_V0all))
watertemp_V50all1 = list(itertools.chain(*watertemp_V50all))
watertemp_V100all1 = list(itertools.chain(*watertemp_V100all))
watertemp_V100VD70all1 = list(itertools.chain(*watertemp_V100VD70all))

allmax = pd.DataFrame({'air':airtemp_all1,'STQ':watertemp_STQall1, 'V0':watertemp_V0all1,'V50': watertemp_V50all1, 'V70':watertemp_V100VD70all1, 'V100':watertemp_V100all1})
#print (all.head())
allmax.to_csv("/home/lnx/dailymax.csv", index=False, cols=('air','STQ','V0','V50','V70','V100'))

axes = plt.gca()
m1, b1 = np.polyfit(airtemp_all1, watertemp_V0all1, 1)
m2, b2 = np.polyfit(airtemp_all1, watertemp_STQall1, 1)
m3, b3 = np.polyfit(airtemp_all1, watertemp_V100all1, 1)
m4, b4 = np.polyfit(airtemp_all1, watertemp_V50all1, 1)
m5, b5 = np.polyfit(airtemp_all1, watertemp_V100VD70all1, 1)


ax2.set_ylabel(u'water temperature [°C]',fontsize="large")
ax2.set_xlabel(u'air temperature [°C]',fontsize="large")
ax2.legend(loc="upper left", title="DAILY MAXIMA")
ax2.text(42,42,"c", horizontalalignment='center', verticalalignment='center',fontsize=20,
         bbox=dict(facecolor='none', edgecolor='black', pad=10.0))
ax2 = gca()
ax2.spines['top'].set_color('none')
ax2.margins(0.2)
plt.show()

