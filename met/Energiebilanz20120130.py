Rdir = 800
Rdif = 100
a = 0.2
Ra = 100  
Re = 100
#H = 
LE = 10
B = 10

#Rdir + Rdif - a*(Rdir + Rdif) + Ra - Re = H + LE + B

H = Rdir + Rdif - a*(Rdir + Rdif) + Ra - Re - LE - B

print H
