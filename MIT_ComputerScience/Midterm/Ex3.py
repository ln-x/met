__author__ = 'lnx'
"""
stuff = ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
for thing in stuff:
        if thing == 'iQ':
           print("Found it")
"""
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

Square(-2)