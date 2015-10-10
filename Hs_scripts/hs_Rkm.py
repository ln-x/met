from Hs_scripts import hs_loader
from pylab import *

__author__ = 'lnx'
import matplotlib.pyplot as plt
filename = "/home/lnx/PycharmProjects/HS/049/outputfiles_newConv_elevcorr_incacloud_start89_masstransfer/Heat_Conv.txt"
name, header. thedata = hs_loader.loadfile(filename=filename)
print 'loaded: ', name


fig = plt.figure()
plt.plot(thedata[6][1:], color='red', lw=0.5, label="6h")
plt.plot(thedata[9][1:], color='orange', lw=0.5, label="9h")
plt.plot(thedata[12][1:], color='yellow', lw=0.5, label="12h")
plt.plot(thedata[15][1:], color='green', lw=0.5, label="15h")
plt.plot(thedata[18][1:], color='blue', lw=0.5, label="18h")
plt.plot(thedata[21][1:], color='violet', lw=0.5, label="21h")
plt.plot(thedata[24][1:], color='black', lw=0.5, label="24h")
plt.title("1 July 2013, Pinka")
plt.ylabel('convective heat flux [W/m2]')
plt.xlabel('distance from source')
plt.legend()
fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2014Paper/newC_m_Conv_Fkm.png')

plt.show()




