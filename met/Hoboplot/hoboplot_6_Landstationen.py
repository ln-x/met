#!usr/bin/python2
#Special thanks to David Leidinger who gave me this code to work on.
#import pylab as pl
import os
import scipy as sp
from numpy.random import rand

import matplotlib.pyplot as pl

#from matplotlib.dates import DateFormatter, MonthLocator, HourLocator, \
#DayLocator


def read_UA(fname):
    """

    :param fname:
    :rtype : object
    """
    from datetime import datetime as dt

    X = sp.genfromtxt(fname, skip_header=1, delimiter=',', usecols=(0, 1, 2, 3, 4), dtype="S20,f8,f8,f8,f8",
                      names=["f0", "f1", "f2", "f3", "f4"])
    print X

    list = X.tolist()

    dates = []
    for dts in X["f0"]:
        dates.append(dt.strptime(dts, '%d.%m.%y %I:%M:%S %p'))

    T = X["f1"]
    RH = X["f2"]
    SW = X["f3"]
    WD = X["f4"]

    return dates, T, RH, SW, WD


path = "/media/WETTER_JHG/MET Radiation/2_Landstationen/"
ext = "txt"


def listExt(path, ext):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith("." + ext) and f.startswith("L")]:
            files.append(os.path.join(dirpath, filename))
    return files

#path = "WT\Lafnitz_Profil"
#print listExt(path, ext)
filenames = listExt(path, ext)
filenames.sort()

lege = []
cols = rand(len(filenames), 50000)

#month = MonthLocator()        # major ticks each month
#alldays = DayLocator()              # minor ticks on the days
#weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
#dayFormatter = DateFormatter('%d')      # e.g., 12

fig, ax = pl.subplots()

#cnt=0
for cnt, fn in enumerate(filenames):
    print fn
    dates, T, RH, SW, WD = read_UA(fn)

    #ax.xaxis.set_major_locator(month)
    #ax.xaxis.set_minor_locator(alldays)
    #ax.xaxis.set_major_formatter(weekFormatter)

    pl.subplot(211)
    pl.plot(dates, T)
    #pl.plot(dates, T, color = cols[cnt])
    fig.autofmt_xdate()

    pl.subplot(212)
    pl.plot(dates, RH)
    fig.autofmt_xdate()

    lege.append(fn.split('/')[-1].strip('.txt'))
    #cnt+=1
    #raw_input("Press ENTER to continue..."

    ax.xaxis_date()
    ax.autoscale_view()

pl.legend(lege, bbox_to_anchor=(1.0, 1), loc=2, prop={'size': 6}, borderaxespad=0.)

pl.grid()

pl.show()
