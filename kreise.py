__author__ = 'lnx'
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.random.randn(60)
# y = np.random.randn(60)
#
# plt.scatter(x, y, s=80, facecolors='none', edgecolors='r')
# plt.show()

import matplotlib.pyplot as plt
import random

circle = plt.Circle((.5,.55) , .07,color='b')
fig = plt.gcf()
fig.gca().add_artist(circle)

pointx = random.random()
pointy = random.random()
plt.scatter(pointx , pointy)

plt.show()