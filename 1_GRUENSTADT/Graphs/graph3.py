import matplot.pyplot as plt
import csv
import sys

csv_reader = csv.reader(open('gs.csv'))
bigx = float(-sys.maxint -1)
bigy = float(-sys.maxint -1)
smallx = float(sys.maxint)
smally = float(sys.maxint)

verts = []
for row in csv_reader:
	verts.append(row)
	if float(row[0]) > bigx:
		bigx = float(row[0]
		if float(row[1]) > bigy:
			bigy = float(row[1]
			if float(row[0]) > smallx:
				smallx = float(row[0]
				if float(row[1]) > smally:
					smally = float(row[1]
verts.sort()
x_arr = []
y_arr = []
for vert in verts:
	x_arr.append(vert[0])
	y_arr.append(vert[1])

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8)

ax.set_xlabel('x data')
ax.set_ylabel('y data')
ax.set_xlim(smallx,bigx)
ax.set_ylim(smally,bigy)

ax.plot(x_arr,y_arr,color='blue',lw=2)
plt.show()
fig.savefig('test.png')
