#!usr/bin/python2
#Special thanks to David Leidinger who gave me this code to work on.
#import pylab as pl
import os

import matplotlib.pyplot as pl
import scipy as sp
from datetime import datetime as dt
import glob
from numpy.random import rand

def read_UA(fname):
    from scipy import genfromtxt
    from datetime import datetime as dt

    X = sp.genfromtxt(fname, skip_header=2, delimiter=';', usecols=(0, 1, 2, 3), dtype="i4,S20,f8, f8",
                      names=["fn", "f0", "f1", "f2"])
    print X

    list = X.tolist()

    dates = [dt.strptime(dts, '%m.%d.%y %I:%M:%S %p') for dts in X["f0"]]

    n = X["fn"]
    T = X["f1"]
    L = X["f2"]
    return n, dates, T, L


path = "F:\_BioClic\_Messungen\_WT\WT\Lafnitz_Profil"
ext = "txt"


def listExt(path, ext):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith("." + ext)]:
            files.append(os.path.join(dirpath, filename))
    return files


path = "F:\_BioClic\_Messungen\_WT\WT\Lafnitz_Profil"
#print listExt(path, ext)
filenames = listExt(path, ext)
filenames.sort()

lege = []
cols = rand(len(filenames), 50000)


#cnt=0
for cnt, fn in enumerate(filenames):
    print fn
    n, dates, T, L = read_UA(fn)
#    pl.subplot(311)
#    pl.plot(dates, n, color = cols[cnt])
    pl.subplot(211)
    pl.plot(dates, T)
    #pl.plot(dates, T, color = cols[cnt])
    pl.subplot(212)
    pl.plot(dates, L)
    #pl.plot(dates, L, color = cols[cnt])
    lege.append(fn.split('/')[-1].strip('.txt'))
    #cnt+=1
    #raw_input("Press ENTER to continue..."

#pl.legend(lege, loc=(1.05, 0.0))
pl.legend(bbox_to_anchor=(1.5, 1), loc=4, borderaxespad=1.)

pl.grid()

pl.show()
