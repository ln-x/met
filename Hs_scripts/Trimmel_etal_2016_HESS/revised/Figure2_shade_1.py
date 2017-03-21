__author__ = 'lnx'

from pylab import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from matplotlib.offsetbox import AnchoredOffsetbox, AuxTransformBox, VPacker,\
    TextArea, DrawingArea

VTS = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS = VTS.mean()
VTS_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS_V0 = VTS_V0.mean()
VTS_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS_V100 = VTS_V100.mean()

Shade = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/Shade.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Shade_mean = Shade.mean()
Shade_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/Shade.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Shade_V0_mean = Shade_V0.mean()
Shade_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/Shade.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Shade_V100_mean = Shade_V100.mean()
#print 'Shade=', Shade_mean.describe()

Topwidth = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/Hyd_WT.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Topwidth_mean = Topwidth.mean()
Topwidth_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/Hyd_WT.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Topwidth_V0_mean = Topwidth_V0.mean()
Topwidth_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/Hyd_WT.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Topwidth_V100_mean = Topwidth_V100.mean()
Condition = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/Condition.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Condition_mean = Condition.mean()

"""
Sw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Sw_mean = Sw.mean()
Sw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Sw_V0_mean = Sw_V0.mean()
Sw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Sw_V100_mean = Sw_V100.mean()

print 'Sw=', Sw_mean.describe()
"""

WT = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_mean = WT.mean()
WT_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_V0_mean = WT_V0.mean()
WT_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Temp_H2O.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
WT_V100_mean = WT_V100.mean()

#print 'WT_p=', WT_mean.describe()
#print 'WT_p_total=', pd.DataFrame(WT).describe()
#print 'WT_V0=', WT_V0_mean.describe()

#Rkm = np.arange(13,64.5,0.5)
Rkm = np.arange(10.85,62.35,0.5)

Rkm = pd.DataFrame(Rkm, columns=['Rkm'])
print len(Rkm)

meas_mean = [16.329,nan,nan,nan,nan,nan,18.604,nan,nan,nan,nan,nan,nan,nan,20.018,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.939,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.992,	nan,	nan,	nan,	nan,	22.596,	nan,	nan,	23.016,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.851,	nan,	nan,	nan,	nan,	nan,	22.494,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.478,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	23.134,	nan,	nan,	nan,	nan,	nan,	23.214, nan, nan, nan, nan] #mean 4. -8.Aug
#correct?meas_mean = [16.329,nan,nan,nan,nan,nan,nan, nan, nan,18.604,nan,nan,nan,nan,nan,nan,nan,nan,20.018,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.939,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	21.992,	nan,	nan,	nan,	nan,	22.596,	nan,	nan,	23.016,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.851,	nan,	nan,	nan,	nan,	nan,	22.494,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	22.478,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	23.134,	nan,	nan,	nan,	nan,	nan,	23.214] #mean 4. -8.Aug
#meas_mean = [HB(89),nan,nan,nan,nan,nan,nan, nan, nan,TB(84.4),nan,nan,nan,nan,nan,nan,nan,nan,SD(80),nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	RD69,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	OO(65),	nan,	nan,	nan,	nan,	UO(62.5),	nan,	nan,	UW(61),	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	J3(54.5),	nan,	nan,	nan,	nan,	nan,	J4(51.5),	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	Z2(46.5),	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	nan,	WD(41),	nan,	nan,	nan,	nan,	nan,	BG(38), nan, nan, nan, nan] #mean 4. -8.Aug

print len(meas_mean)
#meas_mean = pd.Series(meas_mean)
#print 'WT_meas=', meas_mean.describe()

#fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(8,1, sharex= True)
fig, (ax1, ax2, ax3) = plt.subplots(3,1, sharex= True)

#fig.set_size_inches(3.39,2.54)
#plt.title("4-8 August 2013, Pinka")

class AnchoredText(AnchoredOffsetbox):
    def __init__(self, s, loc, pad=0.4, borderpad=0.5, prop=None, frameon=True):
        self.txt = TextArea(s,
                            minimumdescent=False)
        super(AnchoredText, self).__init__(loc, pad=pad, borderpad=borderpad,
                                           child=self.txt,
                                           prop=prop,
                                           frameon=frameon)

def my_formatter_2dig(x,p):
    return "%1.2f" %x

def my_formatter_1dig(x,p):
    return "%1.1f" %x

def my_formatter(x,p):
    return "%5.f" %x

at = AnchoredText("a",loc=2, frameon=True)
ax1.add_artist(at)
#ax1.suptitle(1,1,"1", fontsize=12, horizontalalignment='right')
#ax1.set(title='a')
#ax1.text(3,12, 'I', fontsize=40)
ax1.plot(Rkm, VTS_V0, color='black', linestyle='dashed', lw=0.5, label='VTS_V0')
ax1.plot(Rkm, VTS, color='black', lw=0.5, label='VTS_STQ')
ax1.plot(Rkm, VTS_V100, color='black', lw=1, label='VTS_V100')
ax1.get_yaxis().set_major_formatter(ticker.FuncFormatter(my_formatter_1dig))
ax1.set_ylim(-0.1,1.1)
ax1.set_xlim(8,70)
ax1.set_ylabel('view to sky [0-1]')
ax1.legend(fontsize='small')

at = AnchoredText("b",loc=2, frameon=True)
ax2.add_artist(at)
ax2.plot(Rkm, Shade_V0_mean, color='black', lw=0.5, linestyle="dashed", label="Shade, V0")
ax2.plot(Rkm, Shade_mean, color='black', lw=0.5, label="Shade, STQ")
ax2.plot(Rkm, Shade_V100_mean, color='black', lw=1.0, label="Shade, V100")
ax2.get_yaxis().set_major_formatter(ticker.FuncFormatter(my_formatter_1dig))
ax2.set_ylabel('shade [0-1]')
ax2.set_xlim(8,70)
ax2.legend(fontsize='small')

at = AnchoredText("c",loc=2, frameon=True)
ax3.add_artist(at)
#ax3.plot(Rkm, Topwidth_V0_mean, color='black', lw=0.5, linestyle="dashed", label="bankfull width, V0")
ax3.plot(Rkm, Topwidth_mean, color='black', lw=1.5)#, label="bankfull width, STQ")
#ax3.plot(Rkm, Topwidth_V100_mean, color='black', lw=1.0, label="bankfll width, V100")
ax3.get_yaxis().set_major_formatter(ticker.FuncFormatter(my_formatter))
ax3.set_ylabel('bankfull width [m]')
ax3.set_xlim(8,70)
ax3.set_xlabel('distance from source [km]')

#ax3_2 = ax3.twinx()
#ax3_2.plot(Rkm, Condition_mean, color='red', lw=1.0)#, label="anthropogen influence")
#ax3_2.get_yaxis().set_major_formatter(ticker.FuncFormatter(my_formatter))
#ax3_2.set_ylim(1, 5)
#ax3_2.set_ylabel('anthropogenic influence [1-5]')
#ax3.legend(fontsize='small')


#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure1_298p1.tiff')

plt.show()


