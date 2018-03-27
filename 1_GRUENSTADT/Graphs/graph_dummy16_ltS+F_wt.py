import csv
import datetime as dt
import matplotlib.pyplot as plt

x,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16 = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
csv_reader = csv.reader(open('csv_input/ESLF_ltS10_11_ltF1_10.csv'))
for line in csv_reader:
	x.append(dt.datetime.strptime(line[0],"%d/%m/%Y %H:%M"))
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
	y11.append(float(line[11]))
	y12.append(float(line[12]))
	y13.append(float(line[13]))
	y14.append(float(line[14]))
	y15.append(float(line[15]))
	y16.append(float(line[16]))


fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x,y1, 'b-', x,y2, 'g-')
ax.plot(x,y1,color='orange',lw=0.5, label='LT10_Station') 
ax.plot(x,y2,color='red',lw=0.5, label='LT11_Station')
ax.plot(x,y3,color='pink',lw=0.5, label='LT1_Fassade')
ax.plot(x,y4,color='violet',lw=0.5, label='LT2_Fassade')
ax.plot(x,y5,color='blue',lw=0.5, label='LT3_Fassade')
ax.plot(x,y6,color='turquoise',lw=0.5, label='LT4_Fassade')
ax.plot(x,y7,color='green',lw=0.5, label='LT5_Fassade')
ax.plot(x,y8,color='darkgreen',lw=0.5, label='LT6_Fassade')
ax.plot(x,y9,color='black',lw=0.5, label='LT7_Fassade')
ax.plot(x,y10,color='darkblue',lw=0.5, label='LT8_Fassade')
ax.plot(x,y11,color='darkgreen',lw=0.5, label='LT9_Fassade')
ax.plot(x,y12,color='darkred',lw=0.5, label='LT10_Fassade')
ax.plot(x,y13,color='lightblue',lw=0.5, label='WT1_Fassade')
ax.plot(x,y14,color='lightgreen',lw=0.5, label='WT2_Fassade')
ax.plot(x,y15,color='yellow',lw=0.5, label='WT3_Fassade')
ax.plot(x,y16,color='brown',lw=0.5, label='WT4_Fassade')
#ax.plot(x,y17,color='brown',lw=0.5, label='17')
#ax.plot(x,y18,color='green',lw=0.5, label='18')
#ax.plot(x,y19,color='blue',lw=0.5, label='19')
#ax.plot(x,y20,color='brown',lw=0.5, label='20')


# add 'o-' in the brackets behind x,y, if you want dots for each value
# fig.autofmt_xdate()
plt.ylim(-10,40)
plt.xlabel('time')
plt.ylabel('temperature')
plt.grid(True)

#plt.legend(('label1', 'label2'))
plt.legend()

fig.savefig('test1.png')
plt.show()


