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
width = 0.2

fig = plt.figure()

ax = fig.add_subplot(221)
subplot(121)

#plt.figure(0)
#axes1 = plt.subplot2grid((1,2),(0,0), colspan=1)
#axes1 = plt.subplot2grid((2,3),(0,0), rowspan=2, colspan=2)

#rects5 = axes1.bar(ind, noCh, width, color='white', label='no changes')
#rects1 = axes1.bar(ind + width, Sw11, width, color='lightgrey', label='Sw *1.1')
#rects2 = axes1.bar(ind + 2*width, Lw11, width, color='grey', label='Lw *1.1')
#rects3 = axes1.bar(ind + 3*width, Ev11, width, color='darkgrey', label='Ev *1.1')
#rects4 = axes1.bar(ind + 4*width, Cv11, width, color='black', label='Cv *1.1')

#axes1.set(ylabel=('W/m2'))
#axes1.set(xticks=(ind+width))
#axes1.set(xticklabels=('Cd','Cv','Ev','Lw','Sw','Bal'))
#axes1.legend(bbox_to_anchor=(0.4,0.915,1.,.102), loc=1, fontsize=12)
#axes1.set(title='A')

#axes2 = plt.subplot2grid((1,2),(0,1), colspan=1)
#axes2 = plt.subplot2grid((2,3),(1,2), colspan=1)


subplot(122)
#hist(listeddata)
plt.title('Evaporation[W/m2], 1Jul-29Aug2013, Pinka,(submitted, origC, penman)')
plt.text(70,110000, 'min=',fontsize=12)

x = [1, 2, 3, 4]
WTdiff = [0.8158, 0.1484, -0.0085, -0.617664]
labels = ['Sw*1.1','Cv*1.1','Lw*1.1','Ev*1.1']



plt.tight_layout()
plt.show()



