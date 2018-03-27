import csv
import datetime as dt
import matplotlib.pyplot as plt

x,y1,y2,y3,y4,y5 = [],[],[],[],[],[]
csv_reader = csv.reader(open('csv_input/MA48_NS_rd1-4_20110127-1007.csv'))
for line in csv_reader:
	x.append(dt.datetime.strptime(line[0],"%m/%d/%Y %H:%M"))
	y1.append(float(line[1]))
	y2.append(float(line[2]))
	y3.append(float(line[3]))
	y4.append(float(line[4]))
	y5.append(float(line[5]))

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x,y1, 'b-', x,y2, 'g-')
ax.plot(x,y1,color='black',lw=0.5, label='Niederschlag') 
ax.plot(x,y2,color='red',lw=0.5, label='eintreffenden_Strahlung_GW')
ax.plot(x,y3,color='orange',lw=0.5, label='reflektierte_Strahlng_GW')
ax.plot(x,y4,color='violet',lw=0.5, label='eintreffende_Strahlung_Ref')
ax.plot(x,y5,color='yellow',lw=0.5, label='reflektierte_Strahlung_Ref')

plt.ylim(0,1)
#plt.xlabel('time')
#plt.ylabel('radiation')
plt.grid(True)

plt.legend()

fig.savefig('test1.png')
plt.show()


