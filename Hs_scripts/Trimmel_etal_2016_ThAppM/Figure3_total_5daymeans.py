__author__ = 'lnx'

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

WT_2013_0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_MLF_p/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')#, index_col='Datetime', parse_dates='Datetime')
WT_2013_1 = WT_2013_0.ix[240:359].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column  1.July-3.Aug: 744+72=816h
WT_2013 = np.array(WT_2013_1['61.000']) #select only reference station Unterwart DFM 61km
WT_2013 = WT_2013.ravel()
#print pd.DataFrame(WT_2013).describe()
WT_2013_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_2013_V0 = WT_2013_V0.ix[240:].drop(['Datetime'],axis=1)
WT_2013_V0 = np.array(WT_2013_V0['61.000'])
WT_2013_V0 = WT_2013_V0.ravel()
WT_2013_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_2013_V100 = WT_2013_V100.ix[240:].drop(['Datetime'],axis=1)
WT_2013_V100 = np.array(WT_2013_V100['61.000'])
WT_2013_V100 = WT_2013_V100.ravel()
WT_2013 = transpose(np.array([WT_2013_V0,WT_2013,WT_2013_V100]))
WT_2013_stats = pd.DataFrame(WT_2013).describe()
print WT_2013_stats
dWT_2013 = WT_2013_stats.ix['mean'][0]-WT_2013_stats.ix['mean'][2]
print dWT_2013

# WT_1a_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/303_P500__2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
# WT_1a_2030_V0 = WT_1a_2030_V0.ix[240:].drop(['Datetime'],axis=1)
# WT_1a_2030_V0 = np.array(WT_1a_2030_V0['61.000'])
# WT_1a_2030_V0 = WT_1a_2030_V0.ravel()
# WT_1a_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S192_P_V100_2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
# WT_1a_2030_V100 = WT_1a_2030_V100.ix[240:].drop(['Datetime'],axis=1)
# WT_1a_2030_V100 = np.array(WT_1a_2030_V100['61.000'])
# WT_1a_2030_V100 = WT_1a_2030_V100.ravel()
# WT_2030_1a = transpose(np.array([WT_1a_2030_V0,WT_1a_2030,WT_1a_2030_V100]))
# print pd.DataFrame(WT_2030_1a).describe()


WT_1a_2030_0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S190_P_STQ_2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')#, index_col='Datetime', parse_dates='Datetime')
WT_1a_2030_1 = WT_1a_2030_0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2030 = np.array(WT_1a_2030_1['61.000']) #select only reference station Unterwart DFM 61km
WT_1a_2030 = WT_1a_2030.ravel()
WT_1a_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S191_P_V0_2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2030_V0 = WT_1a_2030_V0.ix[240:].drop(['Datetime'],axis=1)
WT_1a_2030_V0 = np.array(WT_1a_2030_V0['61.000'])
WT_1a_2030_V0 = WT_1a_2030_V0.ravel()
WT_1a_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S192_P_V100_2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2030_V100 = WT_1a_2030_V100.ix[240:].drop(['Datetime'],axis=1)
WT_1a_2030_V100 = np.array(WT_1a_2030_V100['61.000'])
WT_1a_2030_V100 = WT_1a_2030_V100.ravel()
WT_2030_1a = transpose(np.array([WT_1a_2030_V0,WT_1a_2030,WT_1a_2030_V100]))
WT_2030_1a_stats = pd.DataFrame(WT_2030_1a).describe()
print WT_2030_1a_stats
dWT_2030_1a = WT_2030_1a_stats.ix['mean'][0]-WT_2030_1a_stats.ix['mean'][2]
print dWT_2030_1a

WT_5a_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S196_P_STQ_2030_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2030_1 = WT_5a_2030.ix[240:].drop(['Datetime'],axis=1)
WT_5a_2030 = np.array(WT_5a_2030_1['61.000'])
WT_5a_2030 = WT_5a_2030.ravel()
WT_5a_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S197_P_V0_2030_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2030_V0 = WT_5a_2030_V0.ix[240:].drop(['Datetime'],axis=1)
WT_5a_2030_V0 = np.array(WT_5a_2030_V0['61.000'])
WT_5a_2030_V0 = WT_5a_2030_V0.ravel()
WT_5a_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S198_P_V100_2030_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2030_V100 = WT_5a_2030_V100.ix[240:].drop(['Datetime'],axis=1)
WT_5a_2030_V100 = np.array(WT_5a_2030_V100['61.000'])
WT_5a_2030_V100 = WT_5a_2030_V100.ravel()
WT_2030_5a = transpose(np.array([WT_5a_2030_V0,WT_5a_2030,WT_5a_2030_V100]))
WT_2030_5a_stats = pd.DataFrame(WT_2030_5a).describe()
print WT_2030_5a_stats
dWT_2030_5a = WT_2030_5a_stats.ix['mean'][0]-WT_2030_5a_stats.ix['mean'][2]


WT_20a_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S202_P_STQ_2030_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2030 = WT_20a_2030.ix[240:].drop(['Datetime'],axis=1)
WT_20a_2030 = np.array(WT_20a_2030['61.000'])
WT_20a_2030 = WT_20a_2030.ravel()
WT_20a_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S203_P_V0_2030_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2030_V0 = WT_20a_2030_V0.ix[240:].drop(['Datetime'],axis=1)
WT_20a_2030_V0 = np.array(WT_20a_2030_V0['61.000'])
WT_20a_2030_V0 = WT_20a_2030_V0.ravel()
WT_20a_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S204_P_V100_2030_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2030_V100 = WT_20a_2030_V100.ix[240:].drop(['Datetime'],axis=1)
WT_20a_2030_V100 = np.array(WT_20a_2030_V100['61.000'])
WT_20a_2030_V100 = WT_20a_2030_V100.ravel()
WT_2030_20a = transpose(np.array([WT_20a_2030_V0,WT_20a_2030,WT_20a_2030_V100]))
WT_2030_20a_stats = pd.DataFrame(WT_2030_20a).describe()
print WT_2030_20a_stats
dWT_2030_20a = WT_2030_20a_stats.ix['mean'][0]-WT_2030_20a_stats.ix['mean'][2]

WT_max_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S214_P_STQ_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2030 = WT_max_2030.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2030 = np.array(WT_max_2030['61.000'])
WT_max_2030 = WT_max_2030.ravel()
WT_max_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S215_P_V0_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2030_V0 = WT_max_2030_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2030_V0 = np.array(WT_max_2030_V0['61.000'])
WT_max_2030_V0 = WT_max_2030_V0.ravel()
WT_max_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S146_P_V100_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2030_V100 = WT_max_2030_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2030_V100 = np.array(WT_max_2030_V100['61.000'])
WT_max_2030_V100 = WT_max_2030_V100.ravel()
WT_2030_max = transpose(np.array([WT_max_2030_V0,WT_max_2030,WT_max_2030_V100]))
WT_2030_max_stats = pd.DataFrame(WT_2030_max).describe()
print WT_2030_max_stats
dWT_2030_max = WT_2030_max_stats.ix['mean'][0]-WT_2030_max_stats.ix['mean'][2]
print dWT_2030_max

WT_1a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S220_P_STQ_2050_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2050 = WT_1a_2050.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2050 = np.array(WT_1a_2050['61.000'])
WT_1a_2050 = WT_1a_2050.ravel()
WT_1a_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S221_P_V0_2050_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2050_V0 = WT_1a_2050_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2050_V0 = np.array(WT_1a_2050_V0['61.000'])
WT_1a_2050_V0 = WT_1a_2050_V0.ravel()
WT_1a_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S222_P_V100_2050_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2050_V100 = WT_1a_2050_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2050_V100 = np.array(WT_1a_2050_V100['61.000'])
WT_1a_2050_V100 = WT_1a_2050_V100.ravel()
WT_2050_1a = transpose(np.array([WT_1a_2050_V0,WT_1a_2050,WT_1a_2050_V100]))
WT_2050_1a_stats = pd.DataFrame(WT_2050_1a).describe()
print WT_2050_1a_stats
dWT_2050_1a = WT_2050_1a_stats.ix['mean'][0]-WT_2050_1a_stats.ix['mean'][2]
print dWT_2050_1a



WT_5a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S226_P_STQ_2050_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2050 = WT_5a_2050.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2050 = np.array(WT_5a_2050['61.000'])
WT_5a_2050 = WT_5a_2050.ravel()
WT_5a_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S227_P_V0_2050_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2050_V0 = WT_5a_2050_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2050_V0 = np.array(WT_5a_2050_V0['61.000'])
WT_5a_2050_V0 = WT_5a_2050_V0.ravel()
WT_5a_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S228_P_V100_2050_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2050_V100 = WT_5a_2050_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2050_V100 = np.array(WT_5a_2050_V100['61.000'])
WT_5a_2050_V100 = WT_5a_2050_V100.ravel()
WT_2050_5a = transpose(np.array([WT_5a_2050_V0,WT_5a_2050,WT_5a_2050_V100]))
WT_2050_5a_stats = pd.DataFrame(WT_2050_5a).describe()
print WT_2050_5a_stats
dWT_2050_5a = WT_2050_5a_stats.ix['mean'][0]-WT_2050_5a_stats.ix['mean'][2]
print dWT_2050_5a

WT_20a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S232_P_STQ_2050_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2050 = WT_20a_2050.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2050 = np.array(WT_20a_2050['61.000'])
WT_20a_2050 = WT_20a_2050.ravel()
WT_20a_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S233_P_V0_2050_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2050_V0 = WT_20a_2050_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2050_V0 = np.array(WT_20a_2050_V0['61.000'])
WT_20a_2050_V0 = WT_20a_2050_V0.ravel()
WT_20a_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S234_P_V100_2050_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2050_V100 = WT_20a_2050_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2050_V100 = np.array(WT_20a_2050_V100['61.000'])
WT_20a_2050_V100 = WT_20a_2050_V100.ravel()
WT_2050_20a = transpose(np.array([WT_20a_2050_V0,WT_20a_2050,WT_20a_2050_V100]))
WT_2050_20a_stats = pd.DataFrame(WT_2050_20a).describe()
print WT_2050_20a_stats
dWT_2050_20a = WT_2050_20a_stats.ix['mean'][0]-WT_2050_20a_stats.ix['mean'][2]
print dWT_2050_20a

WT_max_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S244_P_STQ_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2050 = WT_max_2050.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2050 = np.array(WT_max_2050['61.000'])
WT_max_2050 = WT_max_2050.ravel()
WT_max_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S245_P_V0_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2050_V0 = WT_max_2050_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2050_V0 = np.array(WT_max_2050_V0['61.000'])
WT_max_2050_V0 = WT_max_2050_V0.ravel()
WT_max_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S246_P_V100_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2050_V100 = WT_max_2050_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2050_V100 = np.array(WT_max_2050_V100['61.000'])
WT_max_2050_V100 = WT_max_2050_V100.ravel()
WT_2050_max = transpose(np.array([WT_max_2050_V0,WT_max_2050,WT_max_2050_V100]))
WT_2050_max_stats = pd.DataFrame(WT_2050_max).describe()
print WT_2050_max_stats
dWT_2050_max = WT_2050_max_stats.ix['mean'][0]-WT_2050_max_stats.ix['mean'][2]
print dWT_2050_max

WT_1a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2085 = WT_1a_2085.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2085 = np.array(WT_1a_2085['61.000'])
WT_1a_2085 = WT_1a_2085.ravel()
WT_1a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2085_V0 = WT_1a_2085_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2085_V0 = np.array(WT_1a_2085_V0['61.000'])
WT_1a_2085_V0 = WT_1a_2085_V0.ravel()
WT_1a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2085_V100 = WT_1a_2085_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2085_V100 = np.array(WT_1a_2085_V100['61.000'])
WT_1a_2085_V100 = WT_1a_2085_V100.ravel()
WT_2085_1a = transpose(np.array([WT_1a_2085_V0,WT_1a_2085,WT_1a_2085_V100]))
WT_2085_1a_stats = pd.DataFrame(WT_2085_1a).describe()
print WT_2085_1a_stats
dWT_2085_1a = WT_2085_1a_stats.ix['mean'][0]-WT_2085_1a_stats.ix['mean'][2]
print dWT_2085_1a


WT_5a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S256_P_STQ_2085_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2085 = WT_5a_2085.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2085 = np.array(WT_5a_2085['61.000'])
WT_5a_2085 = WT_5a_2085.ravel()
WT_5a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S257_P_V0_2085_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2085_V0 = WT_5a_2085_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2085_V0 = np.array(WT_5a_2085_V0['61.000'])
WT_5a_2085_V0 = WT_5a_2085_V0.ravel()
WT_5a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S258_P_V100_2085_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2085_V100 = WT_5a_2085_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2085_V100 = np.array(WT_5a_2085_V100['61.000'])
WT_5a_2085_V100 = WT_5a_2085_V100.ravel()
WT_2085_5a = transpose(np.array([WT_5a_2085_V0,WT_5a_2085,WT_5a_2085_V100]))
WT_2085_5a_stats = pd.DataFrame(WT_2085_5a).describe()
print WT_2085_5a_stats
dWT_2085_5a = WT_2085_5a_stats.ix['mean'][0]-WT_2085_5a_stats.ix['mean'][2]
print dWT_2085_5a

WT_20a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085 = WT_20a_2085.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2085 = np.array(WT_20a_2085['61.000'])
WT_20a_2085 = WT_20a_2085.ravel()
WT_20a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V0 = WT_20a_2085_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2085_V0 = np.array(WT_20a_2085_V0['61.000'])
WT_20a_2085_V0 = WT_20a_2085_V0.ravel()
WT_20a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V100 = WT_20a_2085_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2085_V100 = np.array(WT_20a_2085_V100['61.000'])
WT_20a_2085_V100 = WT_20a_2085_V100.ravel()
WT_2085_20a = transpose(np.array([WT_20a_2085_V0,WT_20a_2085,WT_20a_2085_V100]))
WT_2085_20a_stats = pd.DataFrame(WT_2085_20a).describe()
print WT_2085_20a_stats
dWT_2085_20a = WT_2085_20a_stats.ix['mean'][0]-WT_2085_20a_stats.ix['mean'][2]
print dWT_2085_20a

WT_max_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S274_P_STQ_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2085 = WT_max_2085.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2085 = np.array(WT_max_2085['61.000'])
WT_max_2085 = WT_max_2085.ravel()
WT_max_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S275_P_V0_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2085_V0 = WT_max_2085_V0.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2085_V0 = np.array(WT_max_2085_V0['61.000'])
WT_max_2085_V0 = WT_max_2085_V0.ravel()
WT_max_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S276_P_V100_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2085_V100 = WT_max_2085_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2085_V100 = np.array(WT_max_2085_V100['61.000'])
WT_max_2085_V100 = WT_max_2085_V100.ravel()
WT_2085_max = transpose(np.array([WT_max_2085_V0,WT_max_2085,WT_max_2085_V100]))
WT_2085_max_stats = pd.DataFrame(WT_2085_max).describe()
print WT_2085_max_stats
dWT_2085_max = WT_2085_max_stats.ix['mean'][0]-WT_2085_max_stats.ix['mean'][2]
print dWT_2085_max


#f = open('/home/lnx/2_Documents/_BioClic/_Simulationen/Figure3_stats.txt','w')
#f.write(stats)

#labels = list['1a','5a','max']
fs = 10  # fontsize

fig, axes = plt.subplots(nrows=3, ncols=3, sharex='col', sharey='row') #, figsize=(6, 6))
#fig.set_size_inches(3.39,2.54)

axes[0, 0].boxplot(WT_2030_1a) # labels=labels) #, showfliers=False)
axes[0, 0].set_title('2030_1a', fontsize=fs)
axes[0, 0].set_ylabel('water temperature [degC]', fontsize=fs)
axes[0, 0].set(xticklabels=('V0','STQ','V100'))

axes[1, 0].boxplot(WT_2030_5a)
axes[1, 0].set_title('2030_5a', fontsize=fs)
axes[1, 0].set_ylabel('water temperature [degC]', fontsize=fs)

axes[2, 0].boxplot(WT_2030_20a)
axes[2, 0].set_title('2030_20a', fontsize=fs)
axes[2, 0].set_ylabel('water temperature [degC]', fontsize=fs)

axes[0, 1].boxplot(WT_2050_1a)
axes[0, 1].set_title('2050_1a', fontsize=fs)
axes[0, 1].set(xticklabels=('V0','STQ','V100'))

axes[1, 1].boxplot(WT_2050_5a)
axes[1, 1].set_title('2050_5a', fontsize=fs)

axes[2, 1].boxplot(WT_2050_20a)
axes[2, 1].set_title('2050_20a', fontsize=fs)

axes[0, 2].boxplot(WT_2085_1a)
axes[0, 2].set_title('2085_1a', fontsize=fs)
axes[0, 2].set(xticklabels=('V0','STQ','V100'))

axes[1, 2].boxplot(WT_2085_5a)
axes[1, 2].set_title('2085_5a', fontsize=fs)
#axes[1, 0].set(xticklabels=('1a','5a','max'))

axes[2, 2].boxplot(WT_2085_20a)
axes[2, 2].set_title('2085_20a', fontsize=fs)
#axes[1, 2].set(xticklabels=('1a','5a','max'))

#fig.subplots_adjust(hspace=0.4)

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure3_total_5days_vegcomp.tiff')
plt.show()


fig = plt.figure()
#
# fig.set_size_inches(3.39,2.54)
#

plt.plot(1, dWT_2030_1a, marker='s', linestyle='none', color='black', label='1a')
plt.plot(2, dWT_2030_5a, marker='s', linestyle='none', color='grey', label='5a')
plt.plot(3, dWT_2030_20a, marker='s', linestyle='none', color='darkgrey', label='20a')
plt.plot(4, dWT_2050_1a, marker='s', linestyle='none', color='black')#, label='1a')
plt.plot(5, dWT_2050_5a, marker='s', linestyle='none', color='grey')#, label='1a_min')
plt.plot(6, dWT_2050_20a, marker='s', linestyle='none', color='darkgrey')#, label='1a_max')
plt.plot(7, dWT_2085_1a, marker='s', linestyle='none', color='black')#, label='1a')
plt.plot(8, dWT_2085_5a, marker='s', linestyle='none', color='grey')#, label='1a_min')
plt.plot(9, dWT_2085_20a, marker='s', linestyle='none', color='darkgrey')#, label='1a_max')
plt.ylabel('water temperature difference [degC]')#,fontsize='small')
plt.legend()

ax = gca()

#ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#ax.spines['bottom'].set_color('none')
ax.set_xticks([])
#ax.set_yticks([])
#ax.set(xticklabels=('','','','','','','','',''))
ax.set(title='2030               2050               2085')

ax.axvline(3.5,linestyle=':', color='black')
ax.axvline(6.5,linestyle=':', color='black')

plt.margins(0.2)

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure5_5days_veg_diff.tiff')

plt.show()

