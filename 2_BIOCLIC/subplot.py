from pylab import *
__author__ = 'lnx'
import matplotlib.pyplot as plt

fig = plt.figure()

#fig(dpi = 300, figsize = (3.39,2.53)) #tupel in inches - > 86 x 64,5mm -> 4:3

ax = fig.add_subplot(221)
#subplot(121)
#boxplot(listeddata)

ax2 = fig.add_subplot(224)
#subplot(122)
#hist(listeddata)
x = [1, 2, 3, 4]
WTdiff = [0.8158, 0.1484, -0.0085, -0.617664]
labels = ['Sw*1.1','Cv*1.1','Lw*1.1','Ev*1.1']

ax2.plot(x,WTdiff, color='black', lw='0', marker='s')
#ax.set(ylabel=('water temperature difference [degC]'))
# You can specify a rotation for the tick labels in degrees or with keywords.
ax2.set(xticks=x, rotation='vertical')  #plt.xticks(x, labels, rotation='vertical')
#ax.set(xticklabels=('Sw*1.1','Cv*1.1','Lw*1.1','Ev*1.1'))
#ax2.set_xticks(rotation=70)

plt.title('Evaporation[W/m2], 1Jul-29Aug2013, Pinka,(submitted, origC, penman)')
plt.text(70,110000, 'min=',fontsize=12)

show()
