import csv
import datetime as dt
import matplotlib.pyplot as plt

x,y1,y2,y3,y4 = [],[],[],[],[]
csv_reader = csv.reader(open('/media/WETTER_JHG/MET Radiation/2_Landstationen/P1.csv'))
for line in csv_reader:
    #x.append(dt.datetime.strptime(line[0],"%d.%m.%y %I:%M:%S %p"))
	x.append(line[0])
	y1.append(float(line[2]))
	y2.append(float(line[3]))
	y3.append(float(line[4]))
	y4.append(float(line[5]))


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y1,color='orange',lw=0.5, label='P1_tair')
#ax.plot(x,y2,color='red',lw=0.5, label='2')
#ax.plot(x,y3,color='pink',lw=0.5, label='3')
ax.plot(x,y4,color='violet',lw=0.5, label='P1_ws')


# add 'o-' in the brackets behind x,y, if you want dots for each value
# fig.autofmt_xdate()
plt.ylim(-10,40)
plt.xlabel('time')
plt.ylabel('air temperature C')
plt.grid(True)

#plt.legend(('label1', 'label2'))
plt.legend()

#fig.savefig('test1.png')
plt.show()


