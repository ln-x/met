import csv
import datetime as dt
import matplotlib.pyplot as plt

x,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16 = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
csv_reader = csv.reader(open('D:/03GrueneHaeuser/Messungen/csv_input/JHS_ak_20110815_19.csv'))
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
    
fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x,y1, 'b-', x,y2, 'g-')

ax.plot(x,y1,color='darkblue',lw=0.5, label='1 Bauder(dgr)') 
ax.plot(x,y2,color='grey',lw=1, label='2 Blech_hell')
ax.plot(x,y3,color='red',lw=0.5, label='3 Dachgruen(r)')
ax.plot(x,y4,color='green',lw=0.5, label='4 Europerl 20(g)')
ax.plot(x,y5,color='darkgreen',lw=0.5, label='5 Europerl 30(g)')
ax.plot(x,y6,color='red',lw=0.5, label='6 ZinCo(r)')
ax.plot(x,y7,color='black',lw=1, label='7 Folie_schwarz')
ax.plot(x,y8,color='pink',lw=0.5, label='9 Halditt(hr)')
ax.plot(x,y9,color='lightgrey',lw=1, label='10 Kies')
ax.plot(x,y10,color='darkred',lw=0.5, label='11 Liapor(r)')
ax.plot(x,y11,color='violet',lw=0.5, label='12 Pauliberg(br)')
ax.plot(x,y12,color='blue',lw=0.5, label='14 Rath 7(gr)')
ax.plot(x,y13,color='brown',lw=0.5, label='15 Sanoway Sanoplant(br)')
ax.plot(x,y14,color='orange',lw=0.5, label='16 Sanoway Sanovit(br)')
ax.plot(x,y15,color='yellow',lw=0.5, label='17 Ref.Ziegel ext.(br)')
ax.plot(x,y16,color='lightgreen',lw=0.5, label='18 Ref.Ziegel red.int.(g)')

##ax.plot(x,y1,color='darkblue',lw=0.5, label='1 7cm_Bauder_ext+5cm_EPS_Drain') 
##ax.plot(x,y2,color='grey',lw=1, label='2 Blech')
##ax.plot(x,y3,color='pink',lw=0.5, label='3 10cm_RE_leicht+2cm_Drain')
##ax.plot(x,y4,color='green',lw=0.5, label='4 10cm_Pauliberg+10cm_Agroperl')
##ax.plot(x,y5,color='darkgreen',lw=0.5, label='5 15cm_Pauliberg+15cm_Agroperl')
##ax.plot(x,y6,color='orange',lw=0.5, label='6 ZinCo')
##ax.plot(x,y7,color='black',lw=1, label='7 Folie_schwarz')
##ax.plot(x,y8,color='darkgreen',lw=0.5, label='9 7cm_Claylith_organ+5cm_Claylith_Drain')
##ax.plot(x,y9,color='lightgrey',lw=1, label='10 Kies')
##ax.plot(x,y10,color='darkred',lw=0.5, label='11 7cm_RE_leicht+5cm_LiaDrain')
##ax.plot(x,y11,color='violet',lw=0.5, label='12 12cm_Pauliberg')
##ax.plot(x,y12,color='blue',lw=0.5, label='14 7cm_Rath')
##ax.plot(x,y13,color='red',lw=0.5, label='15 7cm_Claylith_organ+5cm_Claylith_Drain')
##ax.plot(x,y14,color='lightgreen',lw=0.5, label='16 7cm_Claylith_organ+5cm_Claylith_Drain')
##ax.plot(x,y15,color='yellow',lw=0.5, label='17 7cm_Recycling_Ziegel+5cm_Recycling_Ziegel')
##ax.plot(x,y16,color='brown',lw=0.5, label='18 15cm_Recycling_Ziegel+5cm_Recycling_Ziegel')



# add 'o-' in the brackets behind x,y, if you want dots for each value
# fig.autofmt_xdate()
plt.ylim(-0,2,1)
#plt.xlabel('time')
plt.ylabel('albedo')
plt.grid(True)

#plt.legend(('label1', 'label2'))
plt.legend()

#fig.savefig('test1.png')
plt.show()


