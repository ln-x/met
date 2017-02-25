__author__ = 'lnx'

#Write a generator, genPrimes, that returns the sequence of prime numbers
# on successive calls to its next() method: 2, 3, 5, 7, 11, ...

def genPrimes():
    prim0 = 2
    prim1 = 2
    while True:
        while prim1%prim0 != 0:
            prim0 += 1
        if prim0 == prim1:
            pass
        next = prim1
        yield next
        prim1 +=1
        prim0 = 2

def genPrimes2():
    prim0 = 1
    prim1 = 2
    while True:
        while prim0 != prim1:
            while prim1%prim0 != 0:
                prim0 += 1
            prim1 +=1
        next = prim1
        yield next
        prim1 +=1
        prim0 = 2


def genPrimes3():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last

genPrimes3().__next__()
#genPrimes().__next__()
#genPrimes().__next__()
#genPrimes().__next__()

"""
def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
"""