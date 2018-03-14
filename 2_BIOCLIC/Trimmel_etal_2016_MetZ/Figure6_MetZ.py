__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import csv

filename = '/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/Figure6_data.csv'

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
exS = [float(i[1]) for i in data]
exR = [float(i[2]) for i in data]
shR = [float(i[3]) for i in data]
shS = [float(i[4]) for i in data]
exR_WT = [float(i[5]) for i in data]
shR_WT = [float(i[6]) for i in data]

ind = np.arange(N)
width = 0.15

fig = plt.figure(0)

axes1 = plt.subplot2grid((1,2),(0,0))

rects1 = axes1.bar(ind, exS, width, color='white', label='exposed site')
rects2 = axes1.bar(ind + width, exR, width, color='lightgrey', label='exposed reach')
rects3 = axes1.bar(ind + 2*width, shR, width, color='grey', label='shaded reach')
rects4 = axes1.bar(ind + 3*width, shS, width, color='black', label='shaded site')

axes1.set(ylabel=('W m-2'))
axes1.set(xticks=(ind+width))
#axes1.set(xticklabels=('Cd','Cv','Ev','Lw','Sw','Bal'))
axes1.set(xticklabels=('Ev','Cv','Cd','Lw','Sw','Bal'))
axes1.legend(loc=4, fontsize=12)
axes1.set(title='A')
axes1.margins(0.1)

axes2 = plt.subplot2grid((1,2),(0,1), rowspan=1, colspan=1)

rects5 = axes2.bar(ind, shR_WT, 2*width, color='grey', label='shaded reach')
rects6 = axes2.bar(ind + 2*width, exR_WT, 2*width, color='lightgrey', label='exposed reach')

axes2.set(ylabel=('water temperature change in reach [degC]'))
axes2.set(xticks=(ind+width))
#axes2.set(xticklabels=('Cd','Cv','Ev','Lw','Sw','Bal'))
axes2.set(xticklabels=('Ev','Cv','Cd','Lw','Sw','Bal'))
axes2.set(title='B')
axes2.margins(0.1)

fig.set_figwidth(6.78)
fig.set_figheight(4)
plt.tight_layout()

#plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure6.png')
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure6_corr.tiff', dpi=300)
#plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure6.eps')

plt.show()



