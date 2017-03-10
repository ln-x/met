

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #[0]*n**[len(L)]
    res = L[0]*(10**3) + L[1]*(10**2) + L[2]*(10**1) + L[3]*(10**0)
    #res = L[0]*(10**len(L)) + L[1]*(10**(len(L-1))) + L[2]*(10**(len(L-2))) + L[3]*(10**0)
    return res

def general_poly_rec(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #[0]*n**[len(L)]
    #print L[-1]
    res = 0
    if len(L) == 0:
        return res
    else:
       x = L[0] * (10 ** (len(L)-1))
       print (x)
       res += x
       print (res)
       L = L[1:]
       res += general_poly_rec(L)
        #res = L[-1] * (10 ** 0) * general_poly_rec(L[:-1])
       return res

def general_poly_iter(L):
        """ L, a list of numbers (n0, n1, n2, ... nk)
        Returns a function, which when applied to a value x, returns the value
        n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
        # [0]*n**[len(L)]
        # print L[-1]
        res = 0
        if len(L) == 0:
            return res
        else:
            for i in range(len(L)):
                x = L[-1] * (10 ** (i))
                #print x
                res += x
                L = L[:-1]
            return res

#print general_poly([1, 2, 3, 4])(10) #1234
#print general_poly([1, 2, 3, 4])
print general_poly_iter([1, 2, 3, 4])



def general_poly_iter2(L,n):
        """ L, a list of numbers (n0, n1, n2, ... nk)
        Returns a function, which when applied to a value x, returns the value
        n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
        # [0]*n**[len(L)]
        # print L[-1]
        res = 0
        if len(L) == 0:
            return res
        else:
            for i in range(len(L)):
                x = L[-1] * (n ** (i))
                #print x
                res += x
                L = L[:-1]
            return res

print general_poly_iter2([1, 2, 3, 4],10)


