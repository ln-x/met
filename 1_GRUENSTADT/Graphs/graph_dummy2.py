import csv
import datetime as dt
import matplotlib.pyplot as plt

x,y1,y2 = [],[],[]
csv_reader = csv.reader(open('csv_input/JHS_vergleichDach_EKO.csv'))
for line in csv_reader:
	x.append(dt.datetime.strptime(line[0],"%m/%d/%Y %H:%M"))
	y1.append(float(line[1]))
	y2.append(float(line[2]))
	

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x,y1, 'b-', x,y2, 'g-')
ax.plot(x,y1,color='orange',lw=0.5, label='1 Kriwan Pyranometer 13S374') 
ax.plot(x,y2,color='red',lw=0.5, label='2 EKO MS-802F')

# add 'o-' in the brackets behind x,y, if you want dots for each value
# fig.autofmt_xdate()
plt.ylim(0,800)
# plt.xlabel('time')
plt.ylabel('radiation [W/m2]')
plt.grid(True)

#plt.legend(('label1', 'label2'))
plt.legend()

fig.savefig('test1.png')
plt.show()


