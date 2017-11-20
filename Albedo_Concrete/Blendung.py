# -*- coding: utf-8 -*-
##TAGESLICHTBLENDUNGSWAHRSCHEINLICHKEIT: Formel nach Wienold und Christoffersen (2006)
import numpy as np

theta = 0.5         #Blendwinkel 0.5 = worst
EB = 100000         #Beleuchtungsstärke [lx] 100 000=Sun
Pi = 2              #Pigmentierung der Augen (0 ...dunkel, 2...hell=worst)
Ls = 1              #Schleierleuchtdichte [cd/m²]
Alter = 70          #70 = worst

Ev = 100000         #Vertikale Beleuchtungsstärke in der Augenebene (lx)
Ws = 1              #Raumwinkel der Blendquelle
TBW = 1             #Tageslichtblendungswahrscheinlichkeit
alpha = 0           #Winkel zwischen Bildebene und Blickrichtung
beta = 0            #Winkel zwischen Blickrichtung und Blendstrahl
P = 1               #Positionsindex zwischen Blendquelle oberhalb der Augenebene

Ls = EB*( (10/theta**3) + (5/theta**2)+0.1**(Pi/theta) * (1+(Alter/62.5)**4) +0.0025*Pi)
#P= np.exp[(35.2 - 0.31889*alpha - 0.0122*alpha/9)*10-3*beta +(21+0.26667*alpha - 0.002936*alpha**2)*10-5*beta**2]
TBW1 = sum((Ls**2 *Ws)/((Ev**1.87)* P**2))
TBW = 5.87 * 10**-5 * Ev + 0.918 * np.log10(1+TBW1) +0.16

print round(Ls,2), round(P,2), round(TBW1,2)