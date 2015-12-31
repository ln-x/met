__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import csv

filename = '/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/Figure5_data.csv'

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

N = 6
B0 = [float(i[1]) for i in data]
T0 = [float(i[2]) for i in data]
V0 = [float(i[3]) for i in data]
STQ = [float(i[4]) for i in data]
V100 = [float(i[5]) for i in data]

ind = np.arange(N)
width = 0.15
fig = plt.figure(0)

axes1 = plt.subplot2grid((2,3),(0,0), rowspan=2, colspan=2)

rects1 = axes1.bar(ind, B0, width, color='white', label='B0')
rects2 = axes1.bar(ind + width, T0, width, color='lightgrey', label='T0')
rects3 = axes1.bar(ind + 2*width, V0, width, color='darkgrey', label='V0')
rects4 = axes1.bar(ind + 3*width, STQ, width, color='grey', label='STQ')
rects5 = axes1.bar(ind + 4*width, V100, width, color='black', label='V100')

axes1.set(ylabel=('W m-2'))
axes1.set(xticks=(ind+width))
axes1.set(xticklabels=('Cd','Cv','Ev','Lw','Sw','Bal'))
axes1.legend(bbox_to_anchor=(0.6,0.92,1.,.102), loc=1, fontsize=12)
axes1.set(title='A')

#axes2 = plt.subplot2grid((1,2),(0,1), colspan=1)
axes2 = plt.subplot2grid((2,3),(1,2), colspan=1)

x = [1, 2, 3, 4, 5]
WT = [24.75, 24.45, 24.01, 22.33, 20.19]
#labels = ['B0','T0','V0','STQ', 'V100']

axes2.plot(1, WT[0], marker='s', color='white') #label='B0'
axes2.plot(2, WT[1], marker='s', color='lightgrey') #label='T0'
axes2.plot(3, WT[2], marker='s', color='darkgrey') #label='V0'
axes2.plot(4, WT[3], marker='s', color='grey') #label='STQ'
axes2.plot(5, WT[4], marker='s', color='black') #label='V100'
axes2.set(ylabel=('water temperature [degC]'))

axes2.set(xticks=x)  #plt.xticks(x, labels, rotation='vertical')
axes2.set(xticklabels=('','','','', ''))

# Pad margins so that markers don't get clipped by the axes
axes2.margins(0.2)
axes2.set(title='B')

fig.set_figwidth(6.78)
fig.set_figheight(4.5)
plt.tight_layout()

plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure5.png')
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure5.tiff', dpi=300)
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure5.eps')

plt.show()



