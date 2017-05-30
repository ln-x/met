__author__ = 'lnx'
import numpy as np
import matplotlib.pyplot as plt
##read stq rasters of relevant information
#LCZ = ...
#LCZ_new = .... #LCZ with densificated properties (height + 3m)

import random
print random.sample([[1,2],[3,4],[5,6]], 1)

exit()

##parameters:
BWGF_add = 1000000 #Bruttowohngeschossflaeche


#2) new BWGF is  split in densification and urban expansion
SplitFactor = 0.7
BWGF_dense = BWGF_add*SplitFactor
BWGF_extension = BWGF_add*(1-SplitFactor)
LCZ_builtratio = 0.5
pixelsize = 111
BWGF = pixelsize**2 * LCZ_builtratio
BWFG_Nr = round(BWGF_add / BWGF)
print BWFG_Nr, BWGF

#3) Assumption: random distribution on all built categories
SP = np.random.randint(0, 10, (3,3))

#weighting = ... #raster with development priorities for growth
SP_ran = np.random.randint(0, 2, (3,3))

#import random
#i = random.choice(SP)
#print random.choice(i)

#random.sample(population, k)
#SP_adddensif = np.random.sample(SP,BWFG_Nr)

print SP
print SP_ran
SP_new = SP
for i in range(len(SP)):
    for j in range(len(SP[i])):
        SP_new[i][j] = SP[i][j]+SP_ran[i][j]
print SP_new

plt.matshow(SP_new)
plt.show()





