__author__ = 'lnx'

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
from math import sqrt
from pandas import DataFrame

WT_2013 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_MLF_p/outputfiles_orig/Temp_H2O.txt', skiprows=6, sep='\s+')#, index_col='Datetime', parse_dates='Datetime')
WT_2013 = WT_2013.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column  1.July-3.Aug: 744+72=816h
WT_2013 = np.array(WT_2013['61.000']) #select only reference station Unterwart DFM 61km ~ DFS 39
WT_2013 = WT_2013.ravel()
#print pd.DataFrame(WT_2013).describe()

WT_2013_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_2013_V0 = WT_2013_V0.ix[:240].drop(['Datetime'],axis=1)
WT_2013_V0 = np.array(WT_2013_V0['61.000'])
WT_2013_V0 = WT_2013_V0.ravel()
#print pd.DataFrame(WT_2013_V0).describe()

WT_2013_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_2013_V100 = WT_2013_V100.ix[:240].drop(['Datetime'],axis=1)
WT_2013_V100 = np.array(WT_2013_V100['61.000'])
WT_2013_V100 = WT_2013_V100.ravel()
#print pd.DataFrame(WT_2013_V100).describe()

WT_1a_2030_0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S190_P_STQ_2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')#, index_col='Datetime', parse_dates='Datetime')
WT_1a_2030_1 = WT_1a_2030_0.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2030 = np.array(WT_1a_2030_1['61.000']) #select only reference station Unterwart DFM 61km
WT_1a_2030 = WT_1a_2030.ravel()
WT_1a_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S191_P_V0_2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2030_V0 = WT_1a_2030_V0.ix[:240].drop(['Datetime'],axis=1)
WT_1a_2030_V0 = np.array(WT_1a_2030_V0['61.000'])
WT_1a_2030_V0 = WT_1a_2030_V0.ravel()
WT_1a_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S192_P_V100_2030_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2030_V100 = WT_1a_2030_V100.ix[:240].drop(['Datetime'],axis=1)
WT_1a_2030_V100 = np.array(WT_1a_2030_V100['61.000'])
WT_1a_2030_V100 = WT_1a_2030_V100.ravel()
WT_2030_1a = transpose(np.array([WT_1a_2030_V0,WT_1a_2030,WT_1a_2030_V100]))
WT_2030_1a_stats = pd.DataFrame(WT_2030_1a).describe()
dWT_2030_1a = WT_2030_1a_stats.ix['mean'][0]-WT_2030_1a_stats.ix['mean'][2]

WT_5a_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S196_P_STQ_2030_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2030_1 = WT_5a_2030.ix[:240].drop(['Datetime'],axis=1)
WT_5a_2030 = np.array(WT_5a_2030_1['61.000'])
WT_5a_2030 = WT_5a_2030.ravel()
WT_5a_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S197_P_V0_2030_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2030_V0 = WT_5a_2030_V0.ix[:240].drop(['Datetime'],axis=1)
WT_5a_2030_V0 = np.array(WT_5a_2030_V0['61.000'])
WT_5a_2030_V0 = WT_5a_2030_V0.ravel()
WT_5a_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S198_P_V100_2030_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2030_V100 = WT_5a_2030_V100.ix[:240].drop(['Datetime'],axis=1)
WT_5a_2030_V100 = np.array(WT_5a_2030_V100['61.000'])
WT_5a_2030_V100 = WT_5a_2030_V100.ravel()
WT_2030_5a = transpose(np.array([WT_5a_2030_V0,WT_5a_2030,WT_5a_2030_V100]))
WT_2030_5a_stats = pd.DataFrame(WT_2030_5a).describe()
dWT_2030_5a = WT_2030_5a_stats.ix['mean'][0]-WT_2030_5a_stats.ix['mean'][2]


WT_20a_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S202_P_STQ_2030_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2030 = WT_20a_2030.ix[:240].drop(['Datetime'],axis=1)
WT_20a_2030 = np.array(WT_20a_2030['61.000'])
WT_20a_2030 = WT_20a_2030.ravel()
WT_20a_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S203_P_V0_2030_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2030_V0 = WT_20a_2030_V0.ix[:240].drop(['Datetime'],axis=1)
WT_20a_2030_V0 = np.array(WT_20a_2030_V0['61.000'])
WT_20a_2030_V0 = WT_20a_2030_V0.ravel()
WT_20a_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S204_P_V100_2030_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2030_V100 = WT_20a_2030_V100.ix[:240].drop(['Datetime'],axis=1)
WT_20a_2030_V100 = np.array(WT_20a_2030_V100['61.000'])
WT_20a_2030_V100 = WT_20a_2030_V100.ravel()
WT_2030_20a = transpose(np.array([WT_20a_2030_V0,WT_20a_2030,WT_20a_2030_V100]))
WT_2030_20a_stats = pd.DataFrame(WT_2030_20a).describe()
dWT_2030_20a = WT_2030_20a_stats.ix['mean'][0]-WT_2030_20a_stats.ix['mean'][2]

WT_max_2030 = pd.read_csv('/home/lnx/PycharmProjects/HS/S214_P_STQ_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2030 = WT_max_2030.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2030 = np.array(WT_max_2030['61.000'])
WT_max_2030 = WT_max_2030.ravel()
WT_max_2030_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S215_P_V0_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2030_V0 = WT_max_2030_V0.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2030_V0 = np.array(WT_max_2030_V0['61.000'])
WT_max_2030_V0 = WT_max_2030_V0.ravel()
WT_max_2030_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S216_P_V100_2030_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2030_V100 = WT_max_2030_V100.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2030_V100 = np.array(WT_max_2030_V100['61.000'])
WT_max_2030_V100 = WT_max_2030_V100.ravel()
WT_2030_max = transpose(np.array([WT_max_2030_V0,WT_max_2030,WT_max_2030_V100]))
WT_2030_max_stats = pd.DataFrame(WT_2030_max).describe()
dWT_2030_max = WT_2030_max_stats.ix['mean'][0]-WT_2030_max_stats.ix['mean'][2]

WT_1a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S220_P_STQ_2050_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2050 = WT_1a_2050.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2050 = np.array(WT_1a_2050['61.000'])
WT_1a_2050 = WT_1a_2050.ravel()
WT_1a_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S221_P_V0_2050_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2050_V0 = WT_1a_2050_V0.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2050_V0 = np.array(WT_1a_2050_V0['61.000'])
WT_1a_2050_V0 = WT_1a_2050_V0.ravel()
WT_1a_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S222_P_V100_2050_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2050_V100 = WT_1a_2050_V100.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2050_V100 = np.array(WT_1a_2050_V100['61.000'])
WT_1a_2050_V100 = WT_1a_2050_V100.ravel()
WT_2050_1a = transpose(np.array([WT_1a_2050_V0,WT_1a_2050,WT_1a_2050_V100]))
WT_2050_1a_stats = pd.DataFrame(WT_2050_1a).describe()
dWT_2050_1a = WT_2050_1a_stats.ix['mean'][0]-WT_2050_1a_stats.ix['mean'][2]

WT_5a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S226_P_STQ_2050_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2050 = WT_5a_2050.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2050 = np.array(WT_5a_2050['61.000'])
WT_5a_2050 = WT_5a_2050.ravel()
WT_5a_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S227_P_V0_2050_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2050_V0 = WT_5a_2050_V0.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2050_V0 = np.array(WT_5a_2050_V0['61.000'])
WT_5a_2050_V0 = WT_5a_2050_V0.ravel()
WT_5a_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S228_P_V100_2050_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2050_V100 = WT_5a_2050_V100.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2050_V100 = np.array(WT_5a_2050_V100['61.000'])
WT_5a_2050_V100 = WT_5a_2050_V100.ravel()
WT_2050_5a = transpose(np.array([WT_5a_2050_V0,WT_5a_2050,WT_5a_2050_V100]))
WT_2050_5a_stats = pd.DataFrame(WT_2050_5a).describe()
dWT_2050_5a = WT_2050_5a_stats.ix['mean'][0]-WT_2050_5a_stats.ix['mean'][2]

WT_20a_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S232_P_STQ_2050_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2050 = WT_20a_2050.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2050 = np.array(WT_20a_2050['61.000'])
WT_20a_2050 = WT_20a_2050.ravel()
WT_20a_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S233_P_V0_2050_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2050_V0 = WT_20a_2050_V0.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2050_V0 = np.array(WT_20a_2050_V0['61.000'])
WT_20a_2050_V0 = WT_20a_2050_V0.ravel()
WT_20a_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S234_P_V100_2050_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2050_V100 = WT_20a_2050_V100.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2050_V100 = np.array(WT_20a_2050_V100['61.000'])
WT_20a_2050_V100 = WT_20a_2050_V100.ravel()
WT_2050_20a = transpose(np.array([WT_20a_2050_V0,WT_20a_2050,WT_20a_2050_V100]))
WT_2050_20a_stats = pd.DataFrame(WT_2050_20a).describe()
dWT_2050_20a = WT_2050_20a_stats.ix['mean'][0]-WT_2050_20a_stats.ix['mean'][2]

WT_max_2050 = pd.read_csv('/home/lnx/PycharmProjects/HS/S244_P_STQ_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2050 = WT_max_2050.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2050 = np.array(WT_max_2050['61.000'])
WT_max_2050 = WT_max_2050.ravel()
WT_max_2050_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S245_P_V0_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2050_V0 = WT_max_2050_V0.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2050_V0 = np.array(WT_max_2050_V0['61.000'])
WT_max_2050_V0 = WT_max_2050_V0.ravel()
WT_max_2050_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S246_P_V100_2050_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2050_V100 = WT_max_2050_V100.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2050_V100 = np.array(WT_max_2050_V100['61.000'])
WT_max_2050_V100 = WT_max_2050_V100.ravel()
WT_2050_max = transpose(np.array([WT_max_2050_V0,WT_max_2050,WT_max_2050_V100]))
WT_2050_max_stats = pd.DataFrame(WT_2050_max).describe()
dWT_2050_max = WT_2050_max_stats.ix['mean'][0]-WT_2050_max_stats.ix['mean'][2]

WT_1a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2085 = WT_1a_2085.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2085 = np.array(WT_1a_2085['61.000'])
WT_1a_2085 = WT_1a_2085.ravel()
WT_1a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2085_V0 = WT_1a_2085_V0.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2085_V0 = np.array(WT_1a_2085_V0['61.000'])
WT_1a_2085_V0 = WT_1a_2085_V0.ravel()
WT_1a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_1a_2085_V100 = WT_1a_2085_V100.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_1a_2085_V100 = np.array(WT_1a_2085_V100['61.000'])
WT_1a_2085_V100 = WT_1a_2085_V100.ravel()
WT_2085_1a = transpose(np.array([WT_1a_2085_V0,WT_1a_2085,WT_1a_2085_V100]))
WT_2085_1a_stats = pd.DataFrame(WT_2085_1a).describe()
dWT_2085_1a = WT_2085_1a_stats.ix['mean'][0]-WT_2085_1a_stats.ix['mean'][2]

WT_5a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S256_P_STQ_2085_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2085 = WT_5a_2085.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2085 = np.array(WT_5a_2085['61.000'])
WT_5a_2085 = WT_5a_2085.ravel()
WT_5a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S257_P_V0_2085_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2085_V0 = WT_5a_2085_V0.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2085_V0 = np.array(WT_5a_2085_V0['61.000'])
WT_5a_2085_V0 = WT_5a_2085_V0.ravel()
WT_5a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S258_P_V100_2085_5a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_5a_2085_V100 = WT_5a_2085_V100.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_5a_2085_V100 = np.array(WT_5a_2085_V100['61.000'])
WT_5a_2085_V100 = WT_5a_2085_V100.ravel()
WT_2085_5a = transpose(np.array([WT_5a_2085_V0,WT_5a_2085,WT_5a_2085_V100]))
WT_2085_5a_stats = pd.DataFrame(WT_2085_5a).describe()
dWT_2085_5a = WT_2085_5a_stats.ix['mean'][0]-WT_2085_5a_stats.ix['mean'][2]

WT_20a_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S262_P_STQ_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085 = WT_20a_2085.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2085 = np.array(WT_20a_2085['61.000'])
WT_20a_2085 = WT_20a_2085.ravel()
WT_20a_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S263_P_V0_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V0 = WT_20a_2085_V0.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2085_V0 = np.array(WT_20a_2085_V0['61.000'])
WT_20a_2085_V0 = WT_20a_2085_V0.ravel()
WT_20a_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S264_P_V100_2085_20a_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_20a_2085_V100 = WT_20a_2085_V100.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_20a_2085_V100 = np.array(WT_20a_2085_V100['61.000'])
WT_20a_2085_V100 = WT_20a_2085_V100.ravel()
WT_2085_20a = transpose(np.array([WT_20a_2085_V0,WT_20a_2085,WT_20a_2085_V100]))
WT_2085_20a_stats = pd.DataFrame(WT_2085_20a).describe()
dWT_2085_20a = WT_2085_20a_stats.ix['mean'][0]-WT_2085_20a_stats.ix['mean'][2]

WT_max_2085 = pd.read_csv('/home/lnx/PycharmProjects/HS/S274_P_STQ_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2085 = WT_max_2085.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2085 = np.array(WT_max_2085['61.000'])
WT_max_2085 = WT_max_2085.ravel()
WT_max_2085_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S275_P_V0_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2085_V0 = WT_max_2085_V0.ix[:240].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2085_V0 = np.array(WT_max_2085_V0['61.000'])
WT_max_2085_V0 = WT_max_2085_V0.ravel()
WT_max_2085_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S276_P_V100_2085_Max_MLF/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+')
WT_max_2085_V100 = WT_max_2085_V100.ix[240:].drop(['Datetime'],axis=1)   #only last 5days, drop "Datetime" column
WT_max_2085_V100 = np.array(WT_max_2085_V100['61.000'])
WT_max_2085_V100 = WT_max_2085_V100.ravel()
WT_2085_max = transpose(np.array([WT_max_2085_V0,WT_max_2085,WT_max_2085_V100]))
WT_2085_max_stats = pd.DataFrame(WT_2085_max).describe()
#dWT_2085_max = WT_2085_max_stats.ix['mean'][0]-WT_2085_max_stats.ix['mean'][2]

C_2013 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/inputfiles/Climate_04inca.csv', index_col=['DateTime'], sep=',', parse_dates=['DateTime'])
C_2013_max5days = C_2013['2013-08-04 00:00:00':'2013-08-08 23:50:00']
C_2013_max5days_glorad_sum = C_2013_max5days['GloRad (W/m2)'].resample('D', how='sum') * 0.0036
C_2013_max5days_mean = C_2013_max5days.mean()
C_2013_max5days_glorad_sum_mean = C_2013_max5days_glorad_sum.mean()
#print '2013 max: \n', C_2013_max5days_mean, '\nGloRadSum[MJ/d] \t\t\t', C_2013_max5days_glorad_sum_mean

C_1a_2030_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/1jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_1a_2030 = C_1a_2030_0.set_index('datetime')
C_1a_2030_max5days = C_1a_2030.ix[:240]  #not last five days
C_1a_2030_max5days['Rad'] = C_1a_2030_max5days['Rad'].resample('D', how='sum') * 0.0036
C_1a_2030_max5days_mean = C_1a_2030_max5days.mean()
Ta_1a_2030 = C_1a_2030_max5days_mean.ix['AirT']
print Ta_1a_2030
#print '2030 1a: \n', C_1a_2030_max5days_mean

C_5a_2030_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/5jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_5a_2030 = C_5a_2030_0.set_index('datetime')
C_5a_2030_max5days = C_5a_2030.ix[:240]
C_5a_2030_max5days['Rad'] = C_5a_2030_max5days['Rad'].resample('D', how='sum') * 0.0036
C_5a_2030_max5days_mean = C_5a_2030_max5days.mean()
Ta_5a_2030 = C_5a_2030_max5days_mean.ix['AirT']

#print '2030 5a: \n', C_5a_2030_max5days_mean

C_20a_2030_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/20jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_20a_2030 = C_20a_2030_0.set_index('datetime')
C_20a_2030_max5days = C_20a_2030.ix[:240]
C_20a_2030_max5days['Rad'] = C_20a_2030_max5days['Rad'].resample('D', how='sum') * 0.0036
C_20a_2030_max5days_mean = C_20a_2030_max5days.mean()
Ta_20a_2030 = C_20a_2030_max5days_mean.ix['AirT']

#print '2030 20a: \n', C_20a_2030_max5days_mean

C_max_2030_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2016-2045/Max/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_max_2030 = C_max_2030_0.set_index('datetime')
C_max_2030_max5days = C_max_2030.ix[:240]
C_max_2030_max5days['Rad'] = C_max_2030_max5days['Rad'].resample('D', how='sum') * 0.0036
C_max_2030_max5days_mean = C_max_2030_max5days.mean()
Ta_max_2030 = C_max_2030_max5days_mean.ix['AirT']

#print '2030 Max: \n', C_max_2030_max5days_mean

C_1a_2050_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/1jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_1a_2050 = C_1a_2050_0.set_index('datetime')
C_1a_2050_max5days = C_1a_2050.ix[:240]  #last five days
C_1a_2050_max5days['Rad'] = C_1a_2050_max5days['Rad'].resample('D', how='sum') * 0.0036
C_1a_2050_max5days_mean = C_1a_2050_max5days.mean()
Ta_1a_2050 = C_1a_2050_max5days_mean.ix['AirT']

#print '2050 1a: \n', C_1a_2050_max5days_mean

C_5a_2050_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/5jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_5a_2050 = C_5a_2050_0.set_index('datetime')
C_5a_2050_max5days = C_5a_2050.ix[:240]
C_5a_2050_max5days['Rad'] = C_5a_2050_max5days['Rad'].resample('D', how='sum') * 0.0036
C_5a_2050_max5days_mean = C_5a_2050_max5days.mean()
Ta_5a_2050 = C_5a_2050_max5days_mean.ix['AirT']

#print '2050 5a: \n', C_5a_2050_max5days_mean

C_20a_2050_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/20jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_20a_2050 = C_20a_2050_0.set_index('datetime')
C_20a_2050_max5days = C_20a_2050.ix[:240]
C_20a_2050_max5days['Rad'] = C_20a_2050_max5days['Rad'].resample('D', how='sum') * 0.0036
C_20a_2050_max5days_mean = C_20a_2050_max5days.mean()
Ta_20a_2050 = C_20a_2050_max5days_mean.ix['AirT']

#print '2050 20a: \n', C_20a_2050_max5days_mean

C_max_2050_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2036-2065/Max/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_max_2050 = C_max_2050_0.set_index('datetime')
C_max_2050_max5days = C_max_2050.ix[:240]
C_max_2050_max5days['Rad'] = C_max_2050_max5days['Rad'].resample('D', how='sum') * 0.0036
C_max_2050_max5days_mean = C_max_2050_max5days.mean()
Ta_max_2050 = C_max_2050_max5days_mean.ix['AirT']

#print '2050 Max: \n', C_max_2050_max5days_mean

C_1a_2085_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/1jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_1a_2085 = C_1a_2085_0.set_index('datetime')
C_1a_2085_max5days = C_1a_2085.ix[:240]  #last five days
C_1a_2085_max5days['Rad'] = C_1a_2085_max5days['Rad'].resample('D', how='sum') * 0.0036
C_1a_2085_max5days_mean = C_1a_2085_max5days.mean()
Ta_1a_2085 = C_1a_2085_max5days_mean.ix['AirT']

#print '2085 1a: \n', C_1a_2085_max5days_mean

C_5a_2085_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/5jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_5a_2085 = C_5a_2085_0.set_index('datetime')
C_5a_2085_max5days = C_5a_2085.ix[:240]
C_5a_2085_max5days['Rad'] = C_5a_2085_max5days['Rad'].resample('D', how='sum') * 0.0036
C_5a_2085_max5days_mean = C_5a_2085_max5days.mean()
Ta_5a_2085 = C_5a_2085_max5days_mean.ix['AirT']

#print '2085 5a: \n', C_5a_2085_max5days_mean

C_20a_2085_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/20jaehrl/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_20a_2085 = C_20a_2085_0.set_index('datetime')
C_20a_2085_max5days = C_20a_2085.ix[:240]
C_20a_2085_max5days['Rad'] = C_20a_2085_max5days['Rad'].resample('D', how='sum') * 0.0036
C_20a_2085_max5days_mean = C_20a_2085_max5days.mean()
Ta_20a_2085 = C_20a_2085_max5days_mean.ix['AirT']

#print '2085 20a: \n', C_20a_2085_max5days_mean

C_max_2085_0 = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/Episoden/Pinka/2071-2100/Max/MLF/Climate_04.csv', sep='\s+', parse_dates={'datetime':['YYYY','MM','DD','HH']})
C_max_2085 = C_max_2085_0.set_index('datetime')
C_max_2085_max5days = C_max_2085.ix[:240]
C_max_2085_max5days['Rad'] = C_max_2085_max5days['Rad'].resample('D', how='sum') * 0.0036
C_max_2085_max5days_mean = C_max_2085_max5days.mean()
Ta_max_2085 = C_max_2085_max5days_mean.ix['AirT']

#print '2085 Max: \n', C_max_2085_max5days_mean


#f = open('/home/lnx/2_Documents/_BioClic/_Simulationen/Figure3_stats.txt','w')
#f.write(stats)

#labels = list['1a','5a','max']
fs = 10  # fontsize


fig = plt.figure()
# fig.set_size_inches(3.39,2.54)

watertemp_STQ = [WT_1a_2030.mean(), WT_5a_2030.mean(), WT_20a_2030.mean(), WT_max_2030.mean(), WT_1a_2050.mean(),WT_5a_2050.mean(), WT_20a_2050.mean(), WT_max_2050.mean(), WT_1a_2085.mean(), WT_5a_2085.mean(), WT_20a_2085.mean(), WT_max_2085.mean() ]
watertemp_V100 = [WT_1a_2030_V100.mean(), WT_5a_2030_V100.mean(), WT_20a_2030_V100.mean(), WT_max_2030_V100.mean(), WT_1a_2050_V100.mean(),WT_5a_2050_V100.mean(), WT_20a_2050_V100.mean(), WT_max_2050_V100.mean(), WT_1a_2085_V100.mean(), WT_5a_2085_V100.mean(), WT_20a_2085_V100.mean(), WT_max_2085_V100.mean() ]
airtemp = [Ta_1a_2030, Ta_5a_2030, Ta_20a_2030, Ta_max_2030, Ta_1a_2050,Ta_5a_2050, Ta_20a_2050, Ta_max_2050, Ta_1a_2085, Ta_5a_2085, Ta_20a_2085, Ta_max_2085 ]

print len(watertemp_STQ)
print watertemp_STQ
print len(airtemp)
print airtemp

plt.scatter(airtemp,watertemp_STQ,color='red', label="STQ")
plt.scatter(airtemp,watertemp_V100, color='green', label="full veg")

a,b = np.polyfit(airtemp, watertemp_STQ,1)
print ("STQ:", a,b, "/n")   #slope, intercept (y = a*x + b)
c,d = np.polyfit(airtemp, watertemp_V100,1)
print ("V100:", c,d, "/n")

'''
#linregress(airtemp,watertemp_STQ)[2] #r-value  coefficient of correlation
#r2_STQ =  sqrt(r)
#r2_V100 = sqrt(linregress(airtemp,watertemp_V100)[2])

#print r2_STQ, r2_V100
'''
plt.ylabel('water temperature [degC]')
plt.xlabel('air temperature [degC]')
plt.legend()

ax = gca()

#ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#ax.spines['bottom'].set_color('none')
ax.set_xticks([])
#ax.set_yticks([])
#ax.set(xticklabels=('','','','','','','','',''))
#ax.set(title='2030               2050               2085')

#ax.axvline(4.5,linestyle=':', color='black')
#ax.axvline(8.5,linestyle=':', color='black')

plt.margins(0.2)

fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/fig/Figure5_notlast5days_veg_WT_Ta_correlation.tiff')

plt.show()

