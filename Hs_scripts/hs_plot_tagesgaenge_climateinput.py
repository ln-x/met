# coding=utf-8
from Hs_scripts import hs9_loader
from Hs_scripts import hs_cdataloader

__author__ = 'lnx'
import matplotlib.pyplot as plt

filename = "C:\heatsource900b5_339\win32\Test\inputfiles\Climate_04.csv"
mdata = hs_cdataloader.loadfile(filename=filename)
print 'loaded: ', mdata

date_time = [i[0] for i in mdata]
m1 = [i[1] for i in mdata] #Cloudiness (0-1)
m2 = [i[2] for i in mdata] #Windspeed (m/s)
m3 = [i[3] for i in mdata] #rel Humidity (0-1)
m4 = [i[4] for i in mdata] #air temp (degC)

fig = plt.figure()

ax = fig.add_subplot(221)
ax.set_title('Cloudiness')
ax.plot(date_time, x1, color='red', lw=0.3)

plt.ylabel('cloudiness[0-1]')
fig.autofmt_xdate()

ax = fig.add_subplot(222)
ax.set_title('windspeed')
ax.plot(date_time, x2, color='red', lw=0.3)
plt.ylabel('windspeed[m/s]')

fig.autofmt_xdate()

ax = fig.add_subplot(223)
ax.set_title('air humidity')
ax.plot(date_time, x3, color='red', lw=0.3)
plt.xlabel('time[h]')
plt.ylabel('air humidity[0-1]')

ax = fig.add_subplot(224)
ax.set_title('air temperature')
ax.plot(date_time, x4, color='red', lw=0.3)
fig.autofmt_xdate()
plt.xlabel('time[h]')
plt.ylabel('air temperature[degC]')

plt.show()
fig.savefig('climate_input.png')
