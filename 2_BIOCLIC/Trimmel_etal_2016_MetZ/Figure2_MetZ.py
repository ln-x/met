__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np

N = 6
noCh = [11.82,34.49,-201.94, 6.63,198.45,49.46]
Sw11 = [11.78, 25.81, -200.68, 3.85, 218.30, 59.06]
Lw11 = [11.80,24.04,-203.32,7.35,198.45,38.32]
Ev11 = [11.88,45.77,-223.23,10.16,198.45,43.04]
Cv11 = [11.80,35.98,-201.68,5.66,198.45,50.22]

ind = np.arange(N)
width = 0.15
fig = plt.figure(0)
#axes1 = plt.subplot2grid((1,2),(0,0), colspan=1)
axes1 = plt.subplot2grid((2,3),(0,0), rowspan=2, colspan=2)

rects5 = axes1.bar(ind, noCh, width, color='white', label='no changes')
rects1 = axes1.bar(ind + width, Sw11, width, color='lightgrey', label='Sw *1.1')
rects2 = axes1.bar(ind + 2*width, Lw11, width, color='darkgrey', label='Lw *1.1')
rects3 = axes1.bar(ind + 3*width, Ev11, width, color='grey', label='Ev *1.1')
rects4 = axes1.bar(ind + 4*width, Cv11, width, color='black', label='Cv *1.1')

axes1.set(ylabel=('W m-2'))
axes1.set(xticks=(ind+width))
axes1.set(xticklabels=('Cd','Cv','Ev','Lw','Sw','Bal'))
axes1.legend(bbox_to_anchor=(0.63,0.92,1.,.102), loc=1, fontsize=12)
axes1.set(title='A')

#axes2 = plt.subplot2grid((1,2),(0,1), colspan=1)
axes2 = plt.subplot2grid((2,3),(1,2), colspan=1)

x = [1, 2, 3, 4]
#ind = 1
WTdiff = [0.8158, 0.1484, -0.0085, -0.617664]
#labels = ['Sw*1.1','Cv*1.1','Lw*1.1','Ev*1.1']

print WTdiff[0]

axes2.plot(1, WTdiff[0], marker='s', color='lightgrey') #label='Sw *1.1'
axes2.plot(2, WTdiff[1], marker='s', color='black') #label='Lw *1.1'
axes2.plot(3, WTdiff[2], marker='s', color='darkgrey') #label='Ev *1.1'
axes2.plot(4, WTdiff[3], marker='s', color='grey') #label='Cv *1.1'
axes2.set(ylabel=('water temp. diff. [degC]'))
# You can specify a rotation for the tick labels in degrees or with keywords.
axes2.set(xticks=x)  #plt.xticks(x, labels, rotation='vertical')
axes2.axhline(linestyle=':', color='black') #draw x axis as default value 0
# Pad margins so that markers don't get clipped by the axes
axes2.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
axes2.set(xticklabels=('','','',''))  #fontsize=18
axes2.set(title='B')

fig.set_figwidth(6.78)
fig.set_figheight(4.5)
plt.tight_layout()

plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure2.png')
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure2.tiff', dpi=300)
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure2.eps')

plt.show()



