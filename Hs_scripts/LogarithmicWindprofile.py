__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import math

h0 = 30 # Vegetation height
z = 2 # measurement height
d0 = h0 * 0.7 # displacement height , Brutsaert 1982 p. 116  (2/3 ~ 0.7)
z0 = h0 * 0.1 # roughness length , Brutsaert 1982 p. 113 (1/e2 = 0.135)
z0 = 0.1
k = 0.4 # Karman constant , Brustaert 1982 p. 57ff (0.35 - 0.47)
u_mean = np.random.rand(40)
#u_mean = u*/k * ln(z/z0)
#u* = u_mean*k/(log(z-d0)/z0) #Friction velcity
term1 = z/z0
print term1
term2 = math.log(term1)
print term2
uf = u_mean*k/term2 #Friction velcity
uf_1 = 0.3

x = np.arange(1,40,1)  # height z
y = np.arange(0,5,0.1) # velocity u

term1 = x/z0

term2 = []
for i in (x-1):
    term2.append(math.log(term1[i]))

u_mean_1 = []
for i in (x-1):
    u_mean_1.append((u_mean*uf_1/k)*(term2[i]))



plt.plot(x,u_mean_1, label="mean wind velocity")
#plt.plot(x,uf_1, label="friction velocity, fixed at 0.3")
plt.ylabel('wind speed [m s-1]')
plt.xlabel('height [z]')

plt.show()







