import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


list1 = [[1,2.9],[4,5],[6,7.00]]
list2 = (1,2,3,4)
x = np.arange(0,9,1) #hours since start
data = [9,3,4,6,6,2,4,5,3,2]

#print data
#print data[1:1+4]

daily_min = []
today_data = []
for i in x:
    #print i
    #print divmod(i,2)
    quotient, remainder = divmod(i,5)
    if remainder == 0:
        print 'TRUE'
        today_data = data[i:i+4]

#        print i
#        print data
#        print data[i:1+4]
        print today_data

        min = np.min(today_data)
        print min

#        daily_min.append(min(data[i:i+4]))
        daily_min.append(min)

print daily_min

quit()

mean = np.mean(list2)

print mean




quit()

min1 = min(min(i) for i in list1)

list3 = []
for i in list1:
    for j in i:
        list3.append(j)

#list3 = [list3.append(j) for j for i in list1] #TODO funkt fuer 2D nicht Bsp.:splitlistcomp = [i.split() for i in data]

min2 = min(list3)

print min1, min2, len(list1), len(list2), len(list3)
print all(list3), any(list3) #TODO include comparison: all(list3 > 5)
print list1
print list3


fig = plt.figure()
mpl.pyplot.text(10,10,'test')

fig.show()

quit()


from mpl_toolkits.axes_grid.anchored_artists import AnchoredText
at = AnchoredText("Figure 1a",
                  prop=dict(size=8), frameon=True,
                  loc=2,
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at)



#DATETIME

#now = datetime.now()
#print now

#start = datetime(2013,7,25,0,0,0)
#end = datetime(2013,8,9,23,0,0)
#y =  end - start
#print start, end, y