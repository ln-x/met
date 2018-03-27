import csv
import datetime as dt
import matplotlib.pyplot as plt

x,y1,y2,y3,y4 = [],[],[],[],[]
csv_reader = csv.reader(open('gs_rs2_7_10_time.csv'))
for line in csv_reader:
	x.append(dt.datetime.strptime(line[0],"%Y/%d/%m %H:%M:%S"))
	y1.append(float(line[1]))
	y2.append(float(line[2]))
	y3.append(float(line[3]))
	y4.append(float(line[4]))

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x,y1, 'b-', x,y2, 'g-')
ax.plot(x,y1,color='orange',lw=0.5, label='Globalstrahlung') # Globalstrahlung
ax.plot(x,y2,color='grey',lw=0.5, label='Rueckstrahlung2 Blech')
ax.plot(x,y3,color='black',lw=0.5, label='Rueckstrahlung3 Folie')
ax.plot(x,y4,color='blue',lw=0.5, label='Rueckstrahlung4 Kies')
# add 'o-' in the brackets behind x,y, if you want dots for each value
# fig.autofmt_xdate()
plt.ylim(0,1)
plt.xlabel('time')
plt.ylabel('radiation')
plt.grid(True)

#plt.legend(('label1', 'label2'))
plt.legend()

fig.savefig('test1.png')
plt.show()


