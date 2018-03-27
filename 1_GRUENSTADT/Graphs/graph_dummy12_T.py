# -*- coding: cp1252 -*-
import csv
import datetime as dt
import matplotlib.pyplot as plt

x,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12 = [],[],[],[],[],[],[],[],[],[],[],[],[]
csv_reader = csv.reader(open('csv_input/ESLF_ltS10_11_ltF1_10_wt1_4.csv'))
for line in csv_reader:
	x.append(dt.datetime.strptime(line[0],"%D/%M/%Y %H:%M"))
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
     
fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x,y1, 'b-', x,y2, 'g-')
ax.plot(x,y1,color='orange',lw=0.5, label='TC1_Gruenwand_50cm') 
ax.plot(x,y3,color='red',lw=0.5, label='TC2_Gruenwand_10cm')
ax.plot(x,y5,color='pink',lw=0.5, label='TC3_Referenz_50cm')
ax.plot(x,y7,color='violet',lw=0.5, label='T4_Referenz_10cm')
ax.plot(x,y9,color='blue',lw=0.5, label='T5_hinter_Trog')
#ax.plot(x,y2,color='turquoise',lw=0.5, label='RH1_Gruenwand_50cm')
#ax.plot(x,y4,color='green',lw=0.5, label='RH2_Gruenwand_10cm')
#ax.plot(x,y6,color='darkgreen',lw=0.5, label='RH3_Referenz_50cm')
#ax.plot(x,y8,color='black',lw=0.5, label='RH4_Referenz_10cm')
#ax.plot(x,y10,color='darkblue',lw=0.5, label='RH5_hinter_Trog')
#ax.plot(x,y11,color='darkgreen',lw=0.5, label='Bodenfeuchte')
ax.plot(x,y12,color='darkred',lw=0.5, label='Bodentemperatur')
#ax.plot(x,y13,color='lightblue',lw=0.5, label='13')
#ax.plot(x,y14,color='lightgreen',lw=0.5, label='14')
#ax.plot(x,y15,color='yellow',lw=0.5, label='15')
#ax.plot(x,y16,color='brown',lw=0.5, label='16')
#ax.plot(x,y17,color='brown',lw=0.5, label='17')
#ax.plot(x,y18,color='green',lw=0.5, label='18')
#ax.plot(x,y19,color='blue',lw=0.5, label='19')
#ax.plot(x,y20,color='brown',lw=0.5, label='20')


# add 'o-' in the brackets behind x,y, if you want dots for each value
# fig.autofmt_xdate()
plt.ylim(-20,100)
#plt.xlabel('time')
plt.ylabel('temperature (degC)')
plt.grid(True)

#plt.legend(('label1', 'label2'))
plt.legend()

#fig.savefig('test1.png')
plt.show()


