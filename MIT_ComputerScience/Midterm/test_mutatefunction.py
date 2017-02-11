__author__ = 'lnx'

l = ['a', 'b', 'c'] # your list of strings

def add_something(x):
    x.append('d')

add_something(l)

#['a', 'b', 'c', 'd']
print (l)


x = []
def changevalue(v):
    v.append(5)
    v[0] = 6
    #v = [7] #Doesnt work!

changevalue(x)
print(x)