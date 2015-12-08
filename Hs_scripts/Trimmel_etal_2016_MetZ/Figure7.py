__author__ = 'lnx'
from pylab import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import csv

filename = '/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/Figure7_data.csv'

data = []
try:
    with open(filename) as f:
        for line in f:
            reader = csv.reader(f)
            #header = reader.next()
            data = [row for row in reader]

except csv.Error as e:
    print "Error"
    sys.exit(-1)

rkm = [i[0] for i in data]
M = [i[1] for i in data]
masstransfer = [i[2] for i in data]
penman = [i[3] for i in data]

fig = plt.figure()
fig.set_size_inches(3.39,2.54)

axisrange = [37,90,15,26]
plt.axis(axisrange)

plt.plot(rkm,M, linestyle=' ', marker='o', markersize=3, color = 'black', label='obs. WT')
plt.plot(rkm,masstransfer, linestyle=':', color='black', label='pred. WT, mass transfer')
plt.plot(rkm,penman,  linestyle='--', color='black', label='pred. WT, penman')

plt.ylabel('water temperature [degC]',  fontsize='small')
plt.xlabel('river distance from mouth [km]', fontsize='small')
plt.xticks(fontsize='small')
plt.yticks(fontsize='small')

ax = gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#ax.spines['bottom'].set_position(('data',0))
#ax.spines['left'].set_position(('data',0))

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.legend(loc=3, fontsize='9')
plt.tight_layout()


plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure7.tiff', dpi=300)
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure7.png')
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure7.eps')

plt.show()