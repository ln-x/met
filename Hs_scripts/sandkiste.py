import matplotlib.pyplot as plt
import matplotlib as mpl

list1 = [[1,2.9],[4,5],[6,7.00]]
list2 = (1,2,3,4)

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

