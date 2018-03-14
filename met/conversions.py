# -*- coding: utf-8 -*-
import numpy as np

def feet_to_meter(a):
    return round(a/3.28084,2)


def pressure_height_simple(h):
    #give height in meters
    #returns pressure in hPh
    # https://www.engineeringtoolbox.com/air-altitude-pressure-d_462.html
    p = 101325 *(1 - (2.25577*(10**(-5)))* h)**5.25588 #pa
    return round(p/100,2) #hpa

#better: P_h = P_0*e**(-mgh/kT)

def temp_decrease_lapse(h,t):
    #dry: 9.8 K/km  # Danielson, Levin, and Abrams, Meteorology, McGraw Hill, 2003
    #environmental: 6.49K / km
    #moist: 4-6
    t2 = t - (h/1000)*4
    return round(t2,2)

#def density_height(h):
    #1225 kg/cm3
    #1.1653/kg/m3 for 30degC, sealevel
    #0.7057/kg/m3 for 15degC, 13000ft
    #return d

def speed(h,m):
    #h=0.5*g*t
    cd = 0.47 #drag coeffient for squere
    g = 9.8 #m/s2
    t=h/(0.5*g)
    #s = g*t
    #F = m*g.diff()
    #np.trapez()
    v=g*m/(m*t-cd)
    return v

h = feet_to_meter(13000)
p = pressure_height_simple(h)
t2 =temp_decrease_lapse(h,30)
d = speed(h,160)

print h,"m",p,"hPa", t2,"°C", d