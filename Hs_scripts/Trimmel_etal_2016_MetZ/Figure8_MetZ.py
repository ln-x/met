__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
from pylab import *


x = np.arange(23.8,98.8,5)
x2 = np.arange(23.8,93.8,10)
mea = [925.188, 867.773,829.211,768.923,704.5522,637.661,570.417,486.0337,401.449,308.194,226.78545,145.3766,73.4948,8.5189,0.403]
lib = [995.505, 948.1674,892.168,828.3615,758.8466,681.581,599.7566,512.679,422.3022,329.253,236.33789,146.4905,65.4949,7.2133,0]
hso = [876.3974, 772.0056,664.2976,506.9096,341.415,174.2632, 24.0455]
hsa = [896.3671,804.7094,698.842, 559.1539, 396.7511, 228.9449, 40.7258]

fig = plt.figure()

fig.set_size_inches(3.39,2.54)

plt.plot(x,mea,linestyle='--', color = 'black', label='oberserved')
plt.scatter(x,lib,marker='+', color='black', label='libradtran')
plt.scatter(x2,hso,marker='o', s=3, color='darkgrey', label='HS original')
plt.scatter(x2,hsa,marker='o', s=3, color='grey', label='HS adapted')

plt.xlabel('zenith angle [deg]',fontsize='small')
plt.ylabel('short wave radiation [W m-2]',fontsize='small')
plt.xticks(fontsize='small')
plt.yticks(fontsize='small')

ax = gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#ax.spines['bottom'].set_position(('data',0))
#ax.spines['left'].set_position(('data',0))

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.legend(loc=1, bbox_to_anchor=(0.03,0.94,1.,.102), fontsize='9')

plt.tight_layout()

plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure8.tiff', dpi=300)
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure8.png')
plt.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/3_revisedversion/figure8.eps')

plt.show()