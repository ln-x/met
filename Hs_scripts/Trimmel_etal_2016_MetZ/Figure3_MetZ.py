__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import csv

filename = '/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/Figure3_data.csv'

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
noCh = [float(i[1]) for i in data]
glorad11 = [float(i[2]) for i in data]
lwatm11 = [float(i[3]) for i in data]
airtemp11 = [float(i[4]) for i in data]
airhum11 = [float(i[5]) for i in data]
windsp11 = [float(i[6]) for i in data]

ind = np.arange(N)
width = 0.15
fig = plt.figure(0)
axes1 = plt.subplot2grid((2,3),(0,0), rowspan=2, colspan=2)

rects1 = axes1.bar(ind, noCh, width, color='white', label='no changes')
rects4 = axes1.bar(ind + width, airtemp11, width, color='lightgrey', label='airtemp *1.1')
rects3 = axes1.bar(ind + 2*width, lwatm11, width, color='darkgrey', label='lwatm *1.1')
rects2 = axes1.bar(ind + 3*width, glorad11, width, color='grey', label='glorad *1.1')
rects5 = axes1.bar(ind + 4*width, airhum11, width, color='black', label='airhum *1.1')
rects6 = axes1.bar(ind + 5*width, windsp11, width, color='lightgrey', label='windsp *1.1')

axes1.set(ylabel=('W m-2'))
axes1.set(xticks=(ind+width))
axes1.set(xticklabels=('Cd','Cv','Ev','Lw','Sw','Bal'))
axes1.legend(bbox_to_anchor=(0.62,0.92,1.,.102), loc=1, fontsize=12)
axes1.set(title='A')

#axes2 = plt.subplot2grid((1,2),(0,1), colspan=1)
axes2 = plt.subplot2grid((2,3),(1,2), colspan=1)

x = [1, 2, 3, 4, 5]
WTdiff = [1.393, 0.783, 0.693, 0.290, -0.032]
labels = ['airtemp*1.1','lwatm*1.1','glorad*1.1','airhum*1.1', 'windsp*1.1']

axes2.plot(1, WTdiff[0], marker='s', color='lightgrey') #label='airtemp *1.1'
axes2.plot(2, WTdiff[1], marker='s', color='darkgrey') #label='lwatm *1.1'
axes2.plot(3, WTdiff[2], marker='s', color='grey') #label='glorad *1.1'
axes2.plot(4, WTdiff[3], marker='s', color='black') #label='airhum *1.1'
axes2.plot(5, WTdiff[4], marker='s', color='lightgrey') #label='windsp *1.1'
axes2.set(ylabel=('water temp. diff. [degC]'))
axes2.set(xticks=x)  #plt.xticks(x, labels, rotation='vertical')
axes2.set(xticklabels=('','','','',''))
axes2.axhline(linestyle=':', color='black') #draw x axis as default value 0

# Pad margins so that markers don't get clipped by the axes
axes2.margins(0.2)
axes2.set(title='B')

fig.set_figwidth(6.78)
fig.set_figheight(4.5)

plt.tight_layout()

plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure3.png')
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure3.tiff', dpi=300)
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure3.eps')

plt.show()



