__author__ = 'lnx'
from pylab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import csv
import pandas as pd

HB = pd.read_csv('/home/lnx/2_Documents/_BioClic/_Simulationen/ClimateSzenarios/David_20151221/Bioclick/Wassertemp/T_hourly_Bruck_Hundsmuehlbach_1951-2100.txt', sep='\s+', index_col=['Date','Hour'], parse_dates=['Date','Hour'])

TA = np.array(HB['T_Hundsmuehlbach'])

Datetime = np.arange(0,len(TA),1) #1951 1 1 - 2011 12 31 : 783 461.25 days =  18 803 070 hours

regres = polyfit(Datetime, TA, 1)

#slope,intercept=np.polyfit(Datetime,TA,1)

print regres
#
# # Create a list of values in the best fit line
# abline = []
# for i in x:
#   abline.append(slope*i+intercept)
#
# fig = plt.figure()
# fig.set_size_inches(3.39,2.54)
#
# axisrange = [0.2,1,0,-250]
# plt.axis(axisrange)
#
# plt.scatter(x,y, marker='o', color = 'black')
# plt.plot(x,abline, linestyle='-', color='black')
#
# plt.ylabel('evaporation heat flux [W m-2]', fontsize='small')
# plt.xlabel('view to sky [%]',  fontsize='small')
# plt.xticks(fontsize='small')
# plt.yticks(fontsize='small')
# #print intercept, slope
# plt.text(0.3,-220,'$f(x)= -198.3x - 15.9$',  fontsize='small')
# plt.text(0.3,-200, '$R^2=0.908$', fontsize='small' )
#
# plt.tight_layout()
#
#
# plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure4.tiff',
#         dpi=300, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None)
#
# plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure4.png')
# plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure4.eps')
#
# plt.show()