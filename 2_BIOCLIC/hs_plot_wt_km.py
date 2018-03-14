from BIOCLIC import hs_loader

__author__ = 'lnx'
import matplotlib.pyplot as plt
from pylab import *

filename = "/home/lnx/PycharmProjects/Messdatenauswertung/HStest/v808_20130429_c00_v01_f30/Temp_H2O.txt"
thedata = hs_loader.loadfile(filename=filename)

date_time = [i[0] for i in thedata]
a1 = [i[1] for i in thedata]
a2 = [i[2] for i in thedata]
a3 = [i[3] for i in thedata]
a4 = [i[4] for i in thedata]

Y6 = [a1[6],a2[6],a3[6],a4[6]] # WT jeweils um 6h 1ter Tag
Y12 = [a1[12],a2[12],a3[12],a4[12]]  # WT jeweils um 12h 1ter Tag
Y18 = [a1[18],a2[18],a3[18],a4[18]] # WT jeweils um 18h 1ter Tag
Y24 = [a1[24],a2[24],a3[24],a4[24]] # WT jeweils um 24h 1ter Tag
X = [0.65,0.40,0.15,0.0]

# def fit(x):
#     return 3+0.5*x
#
# xfit = array( [amin(Y6), amax(Y6) ] )

fig = plt.figure()

plt.corr(X)
plt.scatter(X, Y6, color='red', lw=0.5, label="6h")
plt.scatter(X, Y12, color='darkred', lw=0.5, label="12h")
plt.scatter(X, Y18,color='violet', lw=0.5, label="18h")
plt.scatter(X, Y24, color='darkblue', lw=0.5, label="24h")
plt.setp(plt.gca(), xticks=(0.65,0.40,0.15,0.0), xticklabels=(0.65,0.40,0.15,0.0))
plt.ylabel('water temperature [degC]')
plt.xlabel('river distance from model outflow [km]')
plt.gca().invert_xaxis()

pairs = (X,Y6), (X,Y12), (X,Y18), (X,Y24)
for x,y in pairs:
    print mean(y), std(y), corrcoef(x,y)[0][1]


plt.legend()
plt.show()