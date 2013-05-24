import csv
import datetime as dt
import matplotlib.pyplot as plt

x,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10 = [],[],[],[],[],[],[],[],[],[],[]
csv_reader = csv.reader(open('csv_input/ESLF_gs_rs1_6_reverse.csv'))
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
	y9.append(float(line[9]))
	y10.append(float(line[10]))

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x,y1, 'b-', x,y2, 'g-')
ax.plot(x,y1,color='orange',lw=0.5, label='1') 
ax.plot(x,y2,color='red',lw=0.5, label='2')
ax.plot(x,y3,color='pink',lw=0.5, label='3')
ax.plot(x,y4,color='violet',lw=0.5, label='4')
ax.plot(x,y5,color='blue',lw=0.5, label='5')
ax.plot(x,y6,color='turquoise',lw=0.5, label='6')
ax.plot(x,y7,color='green',lw=0.5, label='7')
ax.plot(x,y8,color='darkgreen',lw=0.5, label='8')
ax.plot(x,y9,color='black',lw=0.5, label='9')
ax.plot(x,y10,color='brown',lw=0.5, label='10')

# add 'o-' in the brackets behind x,y, if you want dots for each value
# fig.autofmt_xdate()
plt.ylim(0,2)
plt.xlabel('time')
plt.ylabel('radiation')
plt.grid(True)

#plt.legend(('label1', 'label2'))
plt.legend()

fig.savefig('test1.png')
plt.show()


