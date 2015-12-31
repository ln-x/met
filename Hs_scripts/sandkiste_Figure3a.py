__author__ = 'lnx'

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

WT_2030 = np.random.random(50)

#labels = list['1a','5a','max']
fs = 10  # fontsize

fig, axes = plt.subplots(nrows=3, ncols=3, sharex='col') #, figsize=(6, 6))
#fig.set_size_inches(3.39,2.54)

axes[0, 0].boxplot(WT_2030) # labels=labels) #, showfliers=False)
axes[0, 0].set_title('2030', fontsize=fs)
axes[0, 0].set_ylabel('water temperature [degC]', fontsize=fs)
axes[0, 0].set(xticklabels=('1a','5a','max'))

axes[0, 1].boxplot(WT_2030)
axes[0, 1].set_title('2050', fontsize=fs)
axes[0, 1].set(xticklabels=('1a','5a','max'))

axes[0, 2].boxplot(WT_2030)
axes[0, 2].set_title('2085', fontsize=fs)
axes[0, 2].set(xticklabels=('1a','5a','max'))

axes[1, 0].boxplot(WT_2030)
axes[1, 0].set_title('2085_V0', fontsize=fs)
#axes[1, 0].set(xticklabels=('1a','5a','max'))

axes[1, 2].boxplot(WT_2030)
axes[1, 2].set_title('2085_V0', fontsize=fs)
#axes[1, 2].set(xticklabels=('1a','5a','max'))

axes[2, 0].boxplot(WT_2030)
axes[2, 0].set_title('2085_V100', fontsize=fs)
#axes[2, 2].set(xticklabels=('1a','5a','max'))

#fig.subplots_adjust(hspace=0.4)

plt.show()
