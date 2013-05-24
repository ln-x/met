import csv
import datetime as dt
import matplotlib.pyplot as plt

x,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17 = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
csv_reader = csv.reader(open('csv_input/ESL_rd1-16_20111106-07_EKOvergleich_min20m.csv'))
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
	y11.append(float(line[11]))
	y12.append(float(line[12]))
	y13.append(float(line[13]))
	y14.append(float(line[14]))
	y15.append(float(line[15]))
	y16.append(float(line[16]))
	y17.append(float(line[17]))

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x,y1, 'b-', x,y2, 'g-')
ax.plot(x,y1,color='orange',lw=0.5, label='EKO Global') 
ax.plot(x,y2,color='red',lw=0.5, label='W1_Rasenpflaster')
ax.plot(x,y3,color='pink',lw=0.5, label='W2_Versickerungsfugen')
ax.plot(x,y4,color='violet',lw=0.5, label='W3')
ax.plot(x,y5,color='blue',lw=0.5, label='W4')
ax.plot(x,y6,color='turquoise',lw=0.5, label='W5')
ax.plot(x,y7,color='green',lw=0.5, label='W6')
ax.plot(x,y8,color='darkgreen',lw=0.5, label='W7')
ax.plot(x,y9,color='black',lw=0.5, label='W8_Terraway')
ax.plot(x,y10,color='darkblue',lw=0.5, label='W9_Asphalt')
ax.plot(x,y11,color='darkgreen',lw=0.5, label='CS300_Global')
ax.plot(x,y12,color='darkred',lw=0.5, label='F1_Referenz')
ax.plot(x,y13,color='lightblue',lw=0.5, label='F2_90degreen')
ax.plot(x,y14,color='lightgreen',lw=0.5, label='F3_Gruenwand')
ax.plot(x,y15,color='yellow',lw=0.5, label='F4_Efeu')
ax.plot(x,y16,color='brown',lw=0.5, label='Global_Halbraum')
ax.plot(x,y17,color='brown',lw=0.5, label='F5_Optigruen')


# add 'o-' in the brackets behind x,y, if you want dots for each value
# fig.autofmt_xdate()
plt.ylim(0,0.6)
plt.xlabel('time')
plt.ylabel('radiation')
plt.grid(True)

#plt.legend(('label1', 'label2'))
plt.legend()

fig.savefig('test1.png')
plt.show()


