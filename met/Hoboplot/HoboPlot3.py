#!usr/bin/python2
#Special thanks to David Leidinger who gave me this code to work on.
#import pylab as pl

import scipy as sp
import glob

import matplotlib.pyplot as pl


def read_UA(fname):
    from datetime import datetime as dt

    X = sp.genfromtxt(fname, skip_header=2, delimiter=';', usecols=(1, 2), dtype="S20,f8", names=["f0", "f1"])
    print X

    dates = [dt.strptime(dts, '%m.%d.%y %I:%M:%S %p') for dts in X["f0"]]

    T = X["f1"]
    return dates, T


path = '/media/Backup/_BioClic/_Messungen/_WT/WT/'
filenames = glob.glob(path + "*[2,7].txt")
filenames.sort()

lege = []

#cnt=0
for cnt, fn in enumerate(filenames):
    print fn
    dates, T = read_UA(fn)
    pl.plot(dates, T, color=cols[cnt][:])
    #lege.append(fn.split('/')[-1].strip('.txt'))
    #cnt+=1
    #raw_input("Press ENTER to continue..."

#pl.legend(lege,loc=(1.03,0.0))
#pl.grid()

pl.show()