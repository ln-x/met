import csv
import datetime as dt
import matplotlib.pyplot as plt
import numpy


startdate = dt.date(2011, 10, 1)
enddate = dt.date(2013, 11, 30)
starttime = dt.time(9, 0, 0)
endtime = dt.time(17, 45, 0)
sundays = [dt.date(2012, 10, 2),dt.date(2012, 10, 7)]
#clouddays = dt.date[(2012,10,3),(2012,10,6)]

#print startdate, enddate, starttime, endtime

#csv_reader = csv.reader(open('/home/hpl/4_buero/github/py_library/heidiplot/JHS_Albedo_20111005_20130102_a.csv'))
# csvdict = csv.DictReader(open('/home/hpl/4_buero/github/py_library/heidiplot/JHS_Albedo_short.csv'))
csvdict = csv.DictReader(open('/home/hpl/4_buero/github/py_library/heidiplot/JHS_Albedo_20111005_20130102_a.csv'))


print csvdict.fieldnames
alldata = {}
for name in csvdict.fieldnames:
    # print name
    alldata[name] = {}

#print [x for x in alldata]

for line in csvdict:
    #try:
    actualtimestamp = dt.datetime.strptime(line['datetime'], "%d.%m.%Y %H:%M")

    #startdt = dt.datetime.combine(startdate, starttime)
    #enddt = dt.datetime.combine(enddate, endtime)
    #print startdt, enddt, actualtimestamp
    #print 'datum',actualtimestamp.date()
    #print 'zeit', actualtimestamp.time()

    for name in csvdict.fieldnames:
        #print name
        if startdate <= actualtimestamp.date() <= enddate and starttime <= actualtimestamp.time() <= endtime:
            if name != 'datetime':
                try:
                    alldata[name][actualtimestamp] = float(line[name])
                except:
                    pass
            else:
                alldata[name][actualtimestamp] = actualtimestamp



fig = plt.figure()
ax = fig.add_subplot(111)

timeaxis = sorted(alldata['gs'].keys())
values = [alldata['gs'][dictio] for dictio in alldata['gs'] if dictio in timeaxis]
ax.plot(timeaxis, values, color='orange', marker='.', lw=0.0, label='gs')

timeaxis = sorted(alldata['a1'].keys())
values = [alldata['a1'][dictio] for dictio in alldata['a1'] if dictio in timeaxis]
ax.plot(timeaxis, values, color='red', marker='.', lw=0.0, label='a1')



#ax.plot(alldata['datetime'][0] ,gs,color='orange',marker = '.', lw=0.0, label='gs')
# ax.plot(x,gs,color='orange',marker = '.', lw=0.0, label='gs')
#ax.plot(x,r3,color='red',lw=0.5, label='r3')
# ax.plot(x,a3,color='blue',marker = '.',lw=0.0, label='a3')

# '''
# ax.plot(x,a2,color='pink',lw=0.5, label='2 tar paper')
# ax.plot(x,a3,color='violet',lw=0.5, label='3')
# ax.plot(x,a4,color='blue',lw=0.5, label='4')
# ax.plot(x,a5,color='turquoise',lw=0.5, label='5')
# ax.plot(x,a6,color='green',lw=0.5, label='6')
# ax.plot(x,a7,color='darkgreen',lw=0.5, label='7 metal foil')
# ax.plot(x,a9,color='black',lw=0.5, label='9')
# ax.plot(x,a10,color='brown',lw=0.5, label='10 cobble stone')
# ax.plot(x,a11,color='brown',lw=0.5, label='11')
# ax.plot(x,a12,color='brown',lw=0.5, label='12')
# ax.plot(x,a14,color='brown',lw=0.5, label='14')
# ax.plot(x,a15,color='brown',lw=0.5, label='15')
# ax.plot(x,a16,color='brown',lw=0.5, label='16')
# ax.plot(x,a17,color='brown',lw=0.5, label='17')
# ax.plot(x,a18,color='brown',lw=0.5, label='18')
# '''

# add 'o-' in the brackets behind x,y, if you want dots for each value
fig.autofmt_xdate()
plt.ylim(0,1.0)
plt.xlabel('time')
plt.ylabel('albedo')
plt.grid(True)

plt.legend(('label1', 'label2'))
plt.legend()

fig.savefig('albedo.png')
plt.show()


