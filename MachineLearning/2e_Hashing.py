#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Heidelinde'
#h(x) = x mod 7 (i.e. h(x) is the remainder of the division of x by 7)
#to hash into a table with 7 slots (the slots are numbered 0, 1,…, 6) the following numbers: 32, 57, 43, 20, 28, 67, 41, 62, 91, 54


def hash(L):
    h = [[],[],[],[],[],[],[]]
    for i in L:
        #print i%7
        for j in range(7):
            rem = i%7
            if j == rem:
                h[j].append(rem)

    print h


hash([32, 57, 43, 20, 28, 67, 41, 62, 91, 54])