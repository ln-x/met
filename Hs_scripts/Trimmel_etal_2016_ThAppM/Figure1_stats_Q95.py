__author__ = 'lnx'

from pylab import *
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame

WT = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_Q95_p/outputfiles/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_mean = WT.mean()
WT_max = WT.max()
WT = np.array(WT)
WT = WT.ravel()

print 'WT_p_Q95_mean=', WT_mean.describe()
print 'WT_p_Q95_max=', WT_max.describe()
print 'WT_p_Q95_total=', pd.DataFrame(WT).describe()

meas_mean = [15.6400807292,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	17.78446875,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	19.3895416667,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.17528125,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.3037604167,	nan,	nan,	nan,	nan,	22.0474713542,	nan,	nan,	22.3981354167,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	20.5911901042,	nan,	22.6211927083,	nan,	nan,	nan,	nan,	nan,	22.2223671875,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.80021875,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.5628932292,	nan,	nan,	nan,	nan,	nan,	22.59508854170]
meas_mean = pd.Series(meas_mean)

print 'WT_meas_mean=', meas_mean.describe()

