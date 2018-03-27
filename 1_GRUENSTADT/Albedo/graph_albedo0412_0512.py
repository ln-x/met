import csv
import datetime as dt
import matplotlib.pyplot as plt

x,gs,r1,r2,r3,r4,r5,r6,r7,r9,r10,r11 = ([] for i in range(12))
r12,r14,r15,r16,r17,r18,a1,a2,a3,a4 = ([] for i in range(10))
a5,a6,a7,a9,a10,a11,a12,a14,a15,a16,a17,a18 = ([] for i in range(12))

startdate = dt.date(2012,4,1)
enddate = dt.date(2012,5,31) 
starttime = dt.time(6,45,0)
endtime = dt.time(17,5,0)
#print startdate, enddate, starttime, endtime

csv_reader = csv.reader(open('old/JHS_Albedo_20111005_20130102_a.csv'))

for line in csv_reader:
	
	actualtimestamp = dt.datetime.strptime(line[0],"%d.%m.%Y %H:%M")
	#startdt = dt.datetime.combine(startdate, starttime)
	#enddt = dt.datetime.combine(enddate, endtime)
	#print startdt, enddt, actualtimestamp
	#print 'datum',actualtimestamp.date()
	#print 'zeit', actualtimestamp.time()
	
	if actualtimestamp.date() >= startdate and actualtimestamp.date() <= enddate \
		and actualtimestamp.time() >= starttime and actualtimestamp.time() <= endtime:
			x.append(dt.datetime.strptime(line[0],"%d.%m.%Y %H:%M"))
	
			#print 'ich bin da'
			#print line[1]
			gs.append(float(line[1]))
			r3.append(float(line[5]))
			a3.append(float(line[20]))
			
			'''
			r2.append(float(line[3]))
			r3.append(float(line[4]))
			r4.append(float(line[5]))
			r5.append(float(line[6]))
			r6.append(float(line[7]))
			r7.append(float(line[8]))
			r9.append(float(line[9]))
			r10.append(float(line[10]))
			r11.append(float(line[11]))
			r12.append(float(line[12]))
			r14.append(float(line[13]))
			r15.append(float(line[14]))
			r16.append(float(line[15]))
			r17.append(float(line[16]))
			r18.append(float(line[17]))
			a1.append(float(line[18]))
			a2.append(float(line[19]))
			a3.append(float(line[20]))
			a4.append(float(line[21]))
			a5.append(float(line[22]))
			a6.append(float(line[23]))
			a7.append(float(line[24]))
			a9.append(float(line[25]))
			a10.append(float(line[26]))
			a11.append(float(line[27]))
			a12.append(float(line[28]))
			a14.append(float(line[29]))
			a15.append(float(line[30]))
			a16.append(float(line[31]))
			a17.append(float(line[32]))
			a18.append(float(line[33]))
'''
print x
print gs
#print a1



fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x,y1, 'b-', x,y2, 'g-')
ax.plot(x,gs,color='orange',marker = '.', lw=0.0, label='gs') 
#ax.plot(x,r3,color='red',lw=0.5, label='r3')
ax.plot(x,a3,color='blue',marker = '.',lw=0.0, label='a3')

'''
ax.plot(x,a2,color='pink',lw=0.5, label='2 tar paper')
ax.plot(x,a3,color='violet',lw=0.5, label='3')
ax.plot(x,a4,color='blue',lw=0.5, label='4')
ax.plot(x,a5,color='turquoise',lw=0.5, label='5')
ax.plot(x,a6,color='green',lw=0.5, label='6')
ax.plot(x,a7,color='darkgreen',lw=0.5, label='7 metal foil')
ax.plot(x,a9,color='black',lw=0.5, label='9')
ax.plot(x,a10,color='brown',lw=0.5, label='10 cobble stone')
ax.plot(x,a11,color='brown',lw=0.5, label='11')
ax.plot(x,a12,color='brown',lw=0.5, label='12')
ax.plot(x,a14,color='brown',lw=0.5, label='14')
ax.plot(x,a15,color='brown',lw=0.5, label='15')
ax.plot(x,a16,color='brown',lw=0.5, label='16')
ax.plot(x,a17,color='brown',lw=0.5, label='17')
ax.plot(x,a18,color='brown',lw=0.5, label='18')
'''

# add 'o-' in the brackets behind x,y, if you want dots for each value
# fig.autofmt_xdate()
plt.ylim(0,1.0)
plt.xlabel('time')
plt.ylabel('albedo')
plt.grid(True)

#plt.legend(('label1', 'label2'))
plt.legend()

fig.savefig('albedo.png')
plt.show()


