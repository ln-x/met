def general_poly(L):
    def iter(x):
        res = 0
        if len(L) == 0:
            return res
        else:
            L_new = L[:]
            for i in range(len(L_new)):
                y = L_new[-1] * (x ** (i))
                res += y
                L_new = L_new[:-1]
        return res
    return iter

#print general_poly([1,2,3])(2)
#print general_poly_iter3([1,2,3])(2)
print general_poly([1, 2, 3, 4])(10) #1234


""""
import math
def make_cylinder_volume_func(r):
    def volume(h):
        return math.pi * r * r * h
    return volume

#volume_radius_10 = make_cylinder_volume_func(10)
#print volume_radius_10(5)
#print make_cylinder_volume_func(10)(5)
#=> 1570.7963267948967
"""