__author__ = 'lnx'
import csv
import datetime as dt
import matplotlib.pyplot as plt
import numpy

x,lt,rh,gs,lw = ([] for i in range(5))

startdate = dt.date(2012,10,1)
enddate = dt.date(2012,11,30)
starttime = dt.time(9,0,0)
endtime = dt.time(14,45,0)
#sundays = [dt.date(2012,10,2),dt.date(2012,10,7)]
dt10 = dt.timedelta(minutes=10)

csv_reader = csv.reader(open('/home/lnx/Documents/_BioCLIC/_Messungen/_Stationen/LRef_20120522_20120911.csv'))

for row in csv_reader:

    actualtimestamp = dt.datetime.strptime(row[0],"%m/%d/%Y %H:%M")

    if actualtimestamp.date() >= startdate and actualtimestamp.date() <= enddate \
        and actualtimestamp.time() >= starttime and actualtimestamp.time() <= endtime:
        try:
            x.append(dt.datetime.strptime(row[0],"%m/%d/%Y %H:%M"))

            #print 'ich bin da'
            #print line[1]
            lt.append(float(row[1]))
            rh.append(float(row[2]))
            gs.append(float(row[3]))
            lw.append(float(row[4]))
        except:
            pass


        #if actualtimestamp.date() in sundays:
        #if actualtimestamp.min() is 50:
         #   float(row['lt'])+ float(row['lf`]'])

average = numpy.mean(lt)
print average


fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x,y1, 'b-', x,y2, 'g-')
ax.plot(x,lt,color='orange',marker = '.', lw=0.0, label='lt')
#ax.plot(x,r3,color='red',lw=0.5, label='r3')
ax.plot(x,rh,color='blue',marker = '.',lw=0.0, label='rh')

plt.ylim(0,50)
plt.xlabel('time')
plt.ylabel('C, %')
plt.grid(True)

ax = fig.add_subplot(112)
# ax.plot(x,y1, 'b-', x,y2, 'g-')
ax.plot(x,gs,color='orange',marker = '.', lw=0.0, label='gs')
#ax.plot(x,r3,color='red',lw=0.5, label='r3')
ax.plot(x,lw,color='blue',marker = '.',lw=0.0, label='lw')

# add 'o-' in the brackets behind x,y, if you want dots for each value
# fig.autofmt_xdate()
plt.ylim(0,1.0)
plt.xlabel('time')
plt.ylabel('W/m^2')
plt.grid(True)

#plt.legend(('label1', 'label2'))
plt.legend()

fig.savefig('albedo.png')
plt.show()


