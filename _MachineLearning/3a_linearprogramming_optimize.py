# -*- coding: utf8 -*-
__author__ = 'Heidelinde'
#from scipy.optimize import linprog
import scipy.optimize

#Minimize: f = -1*x[0] + 4*x[1]
#Subject to: -3*x[0] + 1*x[1] <= 6
#    1*x[0] + 2*x[1] <= 4
#       x[1] >= -3
#where: -inf <= x[0] <= inf
#This problem deviates from the standard linear programming problem. In standard form, linear programming problems assume the variables x are non-negative.
# Since the variables don’t have standard bounds where 0 <= x <= inf, the bounds of the variables must be explicitly set.
#There are two upper bound constraints, which can be expressed as
#dot(A_ub, x) <= b_ub
"""
>>c = [-1, 4]
A = [[-3, 1], [1, 2]]
>>> b = [6, 4]
>>> x0_bounds = (None, None)
>>> x1_bounds = (-3, None)
>>> from scipy.optimize import linprog
>>> res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds),
...               options={"disp": True})
Optimization terminated successfully.
     Current function value: -22.000000
     Iterations: 1
>>> print(res)
     fun: -22.0
 message: 'Optimization terminated successfully.'
     nit: 1
   slack: array([ 39.,   0.])
  status: 0
 success: True
       x: array([ 10.,  -3.])
"""

#minimize: f= 20x + 30y
#0 < x < 400
#0 < y < 200

x_bounds = (0,400)
y_bounds = (0,200)
c = [20,30]
#x*1/60 + y*1/50 < 8
A = [[1/60],[1/50]]
b = [8]

res = scipy.optimize.linprog(c,A_ub=A, b_ub=b, bounds=(x_bounds, y_bounds), options={"disp":True})

print (res)