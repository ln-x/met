import csv
import datetime as dt
import matplotlib.pyplot as plt

x,y = [],[]
csv_reader = csv.reader(open('gs.csv'))
for line in csv_reader:
	x.append(dt.datetime.strptime(line[0],'%M:%S.%f'))
	y.append(int(line[1]))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(y,x,'o-')
fig.autofmt_xdate()

plt.show()

