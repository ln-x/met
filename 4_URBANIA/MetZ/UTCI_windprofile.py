import numpy as np
ZR = 10 #m
Z = 1.3#m
z0_UTCI = 0.01
z0_Wien = 2
u_ZR = 2.2 #m/s

#LOGARITHMIC FORMULA
#z0 = z0_UTCI
z0 = z0_UTCI
u_Z = u_ZR*((np.log(Z/z0))/(np.log(ZR/z0)))

print u_Z, u_Z/u_ZR

#HELLMAN's EXPONENTIAL LAW
z0 = z0_Wien
alpha = 0.12 * z0 +0.18 #friction coefficient / Hellmann coefficient, used e.g. in Ketterer et al. 2017
u_Z_h = u_ZR*((Z**alpha)/ZR) # used e.g. in Urban and Kysely 2014, Ketterer et al. 2017)

print u_Z_h, "error:", u_Z*100/u_Z_h

z0 = z0_UTCI
u_ZR_recalc = u_Z_h/((np.log(Z/z0))/(np.log(ZR/z0)))

print u_ZR_recalc, "error:", u_ZR*100/u_ZR_recalc