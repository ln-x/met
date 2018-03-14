from pylab import *

__author__ = 'lnx'
import matplotlib.pyplot as plt
import numpy as np
import csv

filename = '/home/lnx/PycharmProjects/HS/049/outputfiles_origConv_elevcorr_incacloud_start89_masstransfer/Heat_Conv.txt'

data = []

try:
    with open(filename) as f:
        for line in f:
            #print 'DIRTY: ', line.split('\t')
            line = line.strip()
            #print line.split('\t')

        reader = csv.reader(f, dialect=csv.excel_tab)

    header1 = reader.next()
    header2 = reader.next()
    header3 = reader.next()
    header4 = reader.next()
    header5 = reader.next()
    header6 = reader.next()
    header7 = reader.next()

    data = [row for row in reader]

except csv.Error as e:
    print "Error"
    sys.exit(-1)

if header2:
    print header2

for datarow in data:
    print datarow

quit()

data = [y[1:] for x in thedata for y in thedata]

#data = [i[1] for i in thedata]

#data = thedata[1:][1:]

print data[0]
print data[1]

print len(data)

data = list(data)



quit()

min = [min for i in data]
max = max(data)



#quit()

#max = max(rd), max(uw)
#min = min(thedata[1][1:])
#min = min(i[1] for i in thedata)
#mean = np.mean(data)
#median = np.median(data)
#std = np.std(data)
#rmse = rmse(thedata)
print 'max=', max
print 'min=', min
#print 'mean=', mean
#print 'median=', median
#print 'stdev=', std


quit()

print thedata[0]

date_time = [i[0] for i in thedata] # Datum
x1 = [i[1] for i in thedata] # km 89
x2 = [i[2] for i in thedata] # km 88.5
rd = [i[41] for i in thedata] # km 69
oo = [i[49] for i in thedata] # km 65
uo = [i[54] for i in thedata] # km 62.5
uw = [i[57] for i in thedata] # km 61
j4 = [i[76] for i in thedata] # km 51.5

fig = plt.figure()
#ax = fig.add_subplot(221)
#subplot(121)
#boxplot(thedata[1][1:])
#subplot(122)
#hist(thedata[1][1:])
#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/origC_m_Conv.png')
#show()




