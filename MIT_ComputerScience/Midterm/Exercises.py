__author__ = 'lnx'
"""
x = "pi"
y = "pie"
x, y = y, x
print (x, y)

x = "pi"
y = "pie"
x = y
y = x
print (x, y)
"""
"""
def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)
        break
    print (a)

f(5)
"""

s = [1,2,3]
r = "1,2,3"
t = (1,2,3)

s[1] = 3
#r[1] = 3
#t[1] = 3

print (r,s,t)