import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as ml

ndata = 10
ny, nx = 100, 200
xmin, xmax = 1, 10
ymin, ymax = 1, 10
# x = np.linspace(1, 10, ndata)
# y = np.linspace(1, 10, ndata)

x = np.random.randint(xmin, xmax, ndata)
y = np.random.randint(ymin, ymax, ndata)
z = np.random.random(ndata)

xi = np.linspace(xmin, xmax, nx)
yi = np.linspace(ymin, ymax, ny)
zi = ml.griddata(x, y, z, xi, yi)

plt.contour(xi, yi, zi, 15, linewidths = 0.5, colors = 'k')
plt.pcolormesh(xi, yi, zi, cmap = plt.get_cmap('rainbow'))

plt.colorbar()
plt.scatter(x, y, marker = 'o', c = 'b', s = 5, zorder = 10)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.show()