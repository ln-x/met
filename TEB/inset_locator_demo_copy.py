import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar

def add_sizebar(ax, size):
    asb = AnchoredSizeBar(ax.transData,
                          size,
                          str(size),
                          loc=8,
                          pad=0.1, borderpad=0.5, sep=5,
                          frameon=False)
    ax.add_artist(asb)

fig, ax = plt.subplots(figsize=[5.5, 3])

# first subplot
ax.set_aspect(1.)
x = np.random.rand(7)
y = np.random.rand(7)
ax.plot(x,y)

#X1, X2, Y1, Y2 = 10.5, 0.9, 12.5, 1.9
#ax.set_xlim(X1, X2)
#ax.set_ylim(Y1, Y2)

axins = inset_axes(ax,
                   width="30%",  # width = 30% of parent_bbox
                   height=1.,  # height : 1 inch
                   loc=1)

axins.plot(x[:3],y[:3])

#axins = zoomed_inset_axes(ax, 6, loc=1)  # zoom = 6
#axins.imshow(Z2, extent=extent, interpolation="nearest",
#             origin="lower")

## sub region of the original image
#x1, x2, y1, y2 = 1.5, 0.9, 2.5, 1.9
#axins.set_xlim(x1, x2)
#axins.set_ylim(y1, y2)

plt.xticks(visible=False)
plt.yticks(visible=False)

add_sizebar(ax, 0.5)
add_sizebar(axins, 0.5)

plt.draw()
plt.show()
