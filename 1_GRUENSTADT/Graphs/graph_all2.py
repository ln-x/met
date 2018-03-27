import csv
import datetime as dt
import matplotlib.pyplot as plt

x,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10 = [],[],[],[],[],[],[],[],[],[],[]
csv_reader = csv.reader(open('csv_input/MA48_all_20110127-1007.csv'))
for line in csv_reader:
	x.append(dt.datetime.strptime(line[0],"%m/%d/%Y %H:%M"))
	y1.append(float(line[1]))
	y2.append(float(line[2]))
	y3.append(float(line[3]))
	y4.append(float(line[4]))
	y5.append(float(line[5]))
	y6.append(float(line[6]))
	y7.append(float(line[7]))
	y8.append(float(line[8]))

plt.subplot(411)
# fig = plt.figure()
# ax.plot(x,y1, 'b-', x,y2, 'g-')
plt.plot(x,y1,'b-', x,y8, 'g-')
#ax.plot(x,y1,color='orange',lw=0.5, label='global radiation') 
#ax.plot(x,y8,color='blue',lw=0.5, label='precipitation')
#ax.plot(x,y6,color='black',lw=0.5, label='windspeed')
plt.ylim(0,2)
plt.xlabel('time')
plt.ylabel('rad., prec.')
plt.grid(True)

plt.subplot(412)
plt.plot(x,y2, 'b-', x,y4, 'g-')
#ax.plot(x,y2,color='pink',lw=0.5, label='airtemp low')
#ax.plot(x,y3,color='turquoise',lw=0.5, label='rel hum low')
#ax.plot(x,y4,color='red',lw=0.5, label='airtemp high')
#ax.plot(x,y5,color='green',lw=0.5, label='rel hum high')
plt.ylim(0,50)
plt.xlabel('time')
plt.ylabel('Tair low + high')
plt.grid(True)

plt.subplot(413)
plt.plot(x,y3, 'b-', x,y5, 'g-')
#ax.plot(x,y2,color='pink',lw=0.5, label='airtemp low')
#ax.plot(x,y3,color='turquoise',lw=0.5, label='rel hum low')
#ax.plot(x,y4,color='red',lw=0.5, label='airtemp high')
#ax.plot(x,y5,color='green',lw=0.5, label='rel hum high')
plt.ylim(0,100)
plt.xlabel('time')
plt.ylabel('RH low + high')
plt.grid(True)

plt.subplot(414)
plt.plot(x,y6, 'b-', label='wind speed')

#ax.plot(x,y7,color='brown',lw=0.5, label='wind direction')
plt.ylim(0,1)
plt.xlabel('time')
plt.ylabel('windspeed')
plt.grid(True)

#plt.legend(('label1', 'label2'))
plt.legend()

#fig.savefig('test1.png')
plt.show()


