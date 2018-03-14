from BIOCLIC import hs_loader
from pylab import *
__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

#1)load file
filename = '/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130725_0809/Temp_H2O.txt'
name, header, thedata = hs_loader.loadfile(filename=filename)
print 'loaded: ', name
data = [i[1:] for i in thedata]
data = np.array(data)
#data = pd.DataFrame(thedata)

#2)prepare x and y axis
#date_time = data[0]
y = [i for i in range(1, 385, 1)]   #384 hours from 25 July 0h - 09 August 2013 23h
date_time = np.arange('2013-07-25 00:00','2013-08-10 00:00', dtype='datetime64[h]')
#print date_time

x = np.arange(13, 64.5, 0.5)               # DFM: 89,38, len=103
X, Y = np.meshgrid(x,y)

#3)contour

fig = plt.figure()
CS = plt.contourf(X,Y,data) #, V, cmap=mpl.cm.jet)                               #oder N?
plt.clabel(CS, inline=True, fmt='%1.1f', color='black', fontsize=10)
plt.colorbar(CS)
plt.title('Water temperature degC, Pinka, penman, V0')
plt.xlabel('distance from upstream model boundary [km]')
plt.ylabel('time[h]')
#axes1.set(xticklabels=('Cd','Cv','Ev','Lw','Sw','Bal'))
#plt.set_labels('Cd','Cv','Ev','Lw','Sw','Bal')

#plt.yticks(date_time)

show()



#
#
# listeddata = []       #splitlistcomp = [i.split() for i in data]
# for i in Z:
#     for j in i:
#         listeddata.append(j)
#
# mean = average(listeddata)
# min = min(listeddata)
# max = max(listeddata)
# std = np.std(listeddata)
# delta = (max-min)/15
# V = np.arange(min,max,delta)
#
# print "min(Z)=", min, "max(Z)=", max, "delta=(min-max)/15=", delta
# print "std(Z)=", std
# print "time steps (len(Z)):", len(Z)
# print "longitudinal steps (len(Z[0])):", len(Z[0])
# print "number of data entries (len(listeddata)):",len(listeddata)
#
# fig = plt.figure()
#
# ax = fig.add_subplot(221)
# subplot(121)
# boxplot(listeddata)
#
# subplot(122)
# hist(listeddata)
# plt.title('Water temperature degC, Pinka, penman')
# plt.text(70,110000, 'min=',fontsize=12)
# plt.text(200,110000, min,fontsize=12)
# plt.text(70,100000, 'max=',fontsize=12)
# plt.text(200,100000, max,fontsize=12)
# plt.text(70,90000, 'mean=',fontsize=12)
# plt.text(200,90000, mean,fontsize=12)
# plt.text(70,80000, 'std=',fontsize=12)
# plt.text(200,80000, std,fontsize=12)
#
# show()


# plt.figure()
# plot = rplot.RPlot(data,'')
# plot.add(rplot.GeomDensity2D())
# plot.render(plt.gcf())