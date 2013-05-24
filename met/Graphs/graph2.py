import csv
#import datetime as dt
import matplotlib.pyplot as plt
x,y1,y2 = [],[],[]
csv_reader = csv.reader(open('gs_rs2.csv'))
for line in csv_reader:
	x.append(int(line[0]))
	y1.append(int(line[1]))
	y2.append(int(line[2]))
	# y3.append(int(line[3]))
	# other option: y.append(dt.datetime.strptime(line[1],'%M:%S.%f'))
fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(x,y1, 'b-', x,y2, 'g-')
ax.plot(x,y1,color='yellow',lw=0.5) # Globalstrahlung
ax.plot(x,y2,color='orange', lw=0.5)
# add 'o-' in the brackets behind x,y, if you want dots for each value
# fig.autofmt_xdate()
plt.ylim(0,800)
plt.ylim(0,800)
plt.xlabel('time')
plt.ylabel('radiation')
plt.grid(True)

fig.savefig('test1.png')
plt.show()


