__author__ = 'lnx'
from Hs_scripts import hs_loader
import numpy as np

filename1 = '/home/lnx/PycharmProjects/HS/303_P500_STQ_2013_p/outputfiles/Temp_H2O.txt'
name, header, thedata = hs_loader.loadfile(filename=filename1)
WT = [i[1:] for i in thedata]
WT = np.array(WT)
#print WT[0][0]

filename2 = '/home/lnx/PycharmProjects/HS/303_P500_STQ_2013_p/outputfiles/Hyd_Vel.txt'
name, header, thedata = hs_loader.loadfile(filename=filename2)
Vel = [i[1:] for i in thedata]
Vel = np.array(Vel)
#print Vel[1][1]

timesteps = np.arange(0,384,1)          # 384 #timesteps delta 1h, t_i, 384 hours from 25 July 0h - 09 August 2013 23h
spacesteps = np.arange(0,103,1)         # spacesteps delta 500, s_i, DFM: 89,38, len=103
#date_time = np.arange('2013-07-25 00:00','2013-08-10 00:00', dtype='datetime64[h]')

s = 0 # 0 = DFM 89
water_path = []

for i in timesteps:
    for j in spacesteps:
        t = 0
        while t < 1:                     #iterate until 1 hour passed
            t = t + Vel[s][i]*(5/36)
            s = s+1      #-500m
            i = i+1
    water_path.append(WT[s][i])

Rkm = np.arange(13,64.5,0.5)
fig = plt.figure()
plt.plot(Rkm, water_path) # , color='green', lw=0.5, label='max, STQ, sunny (2013 07 29)')
show()