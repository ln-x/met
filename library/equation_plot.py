import numpy as np
import matplotlib.pyplot as plt
def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    plt.show()


#graph('x**3+2*x-4', range(-10, 11))
Q=30 #m3/d
V=100 #m3
Z=0.1 #kg
U=0.01 #kg/d
Cin = 0.01 #kg/m3
#x = t #days
#graph('Cin*Q*x+U*x-(Z*x/V)*Q*x', range (0,20))
#graph('-(Q/V)*Z*x + Cin*Q + U', range(0,20))
graph('-(Q/V)*Zdx + Cin*Q + U', range(0,1000))
