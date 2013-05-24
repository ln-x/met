import csv
import datetime as dt
import matplotlib.pyplot as plt
import numpy

x,lt,rh,gs,lw = ([] for i in range(4))

csv_reader = csv.reader(open('LRef_20120522_20121102.csv'))

for line in csv_reader:
	
	actualtimestamp = dt.datetime.strptime(line[0],"%m/%d/%Y %H:%M")
	
	if actualtimestamp.date() >= startdate and actualtimestamp.date() <= enddate \
		and actualtimestamp.time() >= starttime and actualtimestamp.time() <= endtime:
			x.append(dt.datetime.strptime(line[0],"%m/%d/%Y %H:%M"))
	
			#print 'ich bin da'
			#print line[1]
			lt.append(float(line[1]))
			rh.append(float(line[2]))
			gs.append(float(line[3]))
			lw.append(float(line[4]))
			
			
			if actualtimestamp.date() == sundays:
				avsun_a3 = numpy.mean(a3)
				print avsun_a3
			#elif actualtimestamp.date() == clouddays:
			#	avcloud_a3 = numpy.mean(a3)
			



fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x,y1, 'b-', x,y2, 'g-')
ax.plot(x,lt,color='orange',marker = '.', lw=0.0, label='lt') 
#ax.plot(x,r3,color='red',lw=0.5, label='r3')
ax.plot(x,rh,color='blue',marker = '.',lw=0.0, label='rh')

plt.ylim(0,50)
plt.xlabel('time')
plt.ylabel('°C, %')
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


