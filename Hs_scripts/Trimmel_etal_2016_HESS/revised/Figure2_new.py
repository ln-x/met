__author__ = 'lnx'

from pylab import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from matplotlib.offsetbox import AnchoredOffsetbox, AuxTransformBox, VPacker,\
    TextArea, DrawingArea
from pandas import Series, DataFrame

VTS = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS = VTS.mean()
VTS_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/S251_P_V0_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS_V0 = VTS_V0.mean()
VTS_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/S252_P_V100_2085_1a_MLF/outputfiles/VTS.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
VTS_V100 = VTS_V100.mean()

Sw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Sw_mean = Sw.mean()
Sw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Sw_V0_mean = Sw_V0.mean()
Sw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_SR6.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Sw_V100_mean = Sw_V100.mean()

print 'Sw=', Sw_mean.describe()


Lw = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw_mean = Lw.mean()
Lw_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw_V0_mean = Lw_V0.mean()
Lw_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_TR.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Lw_V100_mean = Lw_V100.mean()

print 'Lw=', Lw_mean.describe()


Cv = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_mean = Cv.mean()
Cv_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_V0_mean = Cv_V0.mean()
Cv_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_Conv.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cv_V100_mean = Cv_V100.mean()

print 'Cv_p=', Cv_mean.describe()


Ev = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_mean = Ev.mean() #*(-1)
Ev_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_V0_mean = Ev_V0.mean() #*(-1)
Ev_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_Evap.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Ev_V100_mean = Ev_V100.mean() #*(-1)

print 'Ev_=', Ev_mean.describe()
#print 'Ev_mt=', Ev_mt_mean.describe()

Cd = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_STQ_2013_p/outputfiles_20130804_08/Heat_Cond.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cd_mean = Cd.mean() #*(-1)
Cd_V0 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V0_2013_MLF_p/outputfiles_20130804_08/Heat_Cond.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cd_V0_mean = Cd_V0.mean() #*(-1)
Cd_V100 = pd.read_csv('/home/lnx/PycharmProjects/HS/298_P500_V100_2013_MLF_p/outputfiles_20130804_08/Heat_Cond.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
Cd_V100_mean = Cd_V100.mean() #*(-1)

print 'Cd=', Cd_mean.describe()



Bal_V0_mean = Sw_V0_mean + Lw_V0_mean + Cv_V0_mean + Ev_V0_mean + Cd_V0_mean
Bal_mean = Sw_mean + Lw_mean + Cv_mean + Ev_mean + Cd_mean
Bal_V100_mean = Sw_V100_mean + Lw_V100_mean + Cv_V100_mean + Ev_V100_mean + Cd_V100_mean

print "Bal_V0_mean", Bal_V0_mean.mean() #54.8867543404
print "Bal STQ_mean", Bal_mean.mean() #54.8867543404
print "Bal_V100_mean", Bal_V100_mean.mean() #22.2423318387
print "Bal_V0_max", Bal_V0_mean.max() #199.786929167
print "Bal STQ_max", Bal_mean.max() #136.396542803
print "Bal_V100_max", Bal_V100_mean.max() #90.8038903983

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

fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(8,1, sharex= True)
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
ax1.get_yaxis().set_major_formatter(ticker.FuncFormatter(my_formatter_2dig))
ax1.set_ylim(0,1)
ax1.set_xlim(8,70)
ax1.set_ylabel('view to sky')
ax1.legend(fontsize='small')

at = AnchoredText("b",loc=2, frameon=True)
ax2.add_artist(at)
ax2.plot(Rkm, Sw_V0_mean, color='black', lw=0.5, linestyle="dashed", label="Q_sw, V0")
ax2.plot(Rkm, Sw_mean, color='black', lw=0.5, label="Q_sw, STQ")
ax2.plot(Rkm, Sw_V100_mean, color='black', lw=1.0, label="Q_sw, V100")
ax2.get_yaxis().set_major_formatter(ticker.FuncFormatter(my_formatter))
ax2.set_ylabel('[W m-2]')
ax2.legend(fontsize='small')

at = AnchoredText("c",loc=2, frameon=True)
ax3.add_artist(at)
ax3.plot(Rkm, Lw_V0_mean, color='black', lw=0.5, linestyle="dashed", label="Q_lw, V0")
ax3.plot(Rkm, Lw_mean, color='black', lw=0.5, label="Q_lw, STQ")
ax3.plot(Rkm, Lw_V100_mean, color='black', lw=1.0, label="Q_lw, V100")
ax3.get_yaxis().set_major_formatter(ticker.FuncFormatter(my_formatter))
ax3.set_ylabel('[W m-2]')
ax3.legend(fontsize='small')

at = AnchoredText("d",loc=2, frameon=True)
ax4.add_artist(at)
ax4.plot(Rkm, Ev_V0_mean, color='black', lw=0.5, linestyle='dashed', label="LE, V0")
ax4.plot(Rkm, Ev_mean, color='black', lw=0.5, label="LE, STQ")
ax4.plot(Rkm, Ev_V100_mean, color='black', lw=1.0, linestyle='solid', label="LE, V100")
ax4.get_yaxis().set_major_formatter(ticker.FuncFormatter(my_formatter))
ax4.set_ylabel('[W m-2]')
ax4.legend(fontsize='small')

at = AnchoredText("e",loc=2, frameon=True)
ax5.add_artist(at)
ax5.plot(Rkm, Cv_V0_mean, color='black', lw=0.5, linestyle="dashed", label="H, V0")
ax5.plot(Rkm, Cv_mean, color='black', lw=0.5, label="H, STQ")
ax5.plot(Rkm, Cv_V100_mean, color='black', lw=1.0, label="H, V100")
ax5.get_yaxis().set_major_formatter(ticker.FuncFormatter(my_formatter))
ax5.set_ylabel('[W m-2]')
ax5.legend(fontsize='small')

at = AnchoredText("f",loc=2, frameon=True)
ax6.add_artist(at)
ax6.plot(Rkm, Cd_V0_mean, color='black', lw=0.5, linestyle="dashed", label="Cd, V0")
ax6.plot(Rkm, Cd_mean, color='black', lw=0.5, label="Cd, STQ")
ax6.plot(Rkm, Cd_V100_mean, color='black', lw=1.0, label="Cd, V100")
ax6.get_yaxis().set_major_formatter(ticker.FuncFormatter(my_formatter))
ax6.set_ylabel('[W m-2]')
ax6.legend(fontsize='small')

at = AnchoredText("g",loc=2, frameon=True)
ax7.add_artist(at)
ax7.plot(Rkm, Bal_V0_mean, color='black', lw=0.5, linestyle="dashed", label="Bal, V0")
ax7.plot(Rkm, Bal_mean, color='black', lw=0.5, label="Bal, STQ")
ax7.plot(Rkm, Bal_V100_mean, color='black', lw=1.0, label="Bal, V100")
ax7.get_yaxis().set_major_formatter(ticker.FuncFormatter(my_formatter))
ax7.set_ylabel('[W m-2]')
ax7.legend(fontsize='small')

at = AnchoredText("h",loc=2, frameon=True)
ax8.add_artist(at)
ax8.plot(Rkm, WT_V0_mean, color='black', linestyle="dashed", lw=0.5, label='WT_V0')
ax8.plot(Rkm, WT_mean, color='black', lw=0.5, label='WT_STQ')
ax8.plot(Rkm, WT_V100_mean, color='black', linestyle="solid", lw=1.0, label='WT_V100')
ax8.plot(Rkm, meas_mean, marker='x',linestyle="none", color='blue', lw=0.5, label='measured')
ax8.get_yaxis().set_major_formatter(ticker.FuncFormatter(my_formatter))
ax8.set_xlabel('distance from source [km]')
ax8.set_ylabel('[degC]')
ax8.legend(fontsize='small')

#fig.savefig('/home/lnx/2_Documents/_BioClic/_Simulationen/HS_Output_analysis/2015Paper/Figure1_298p1.tiff')

plt.show()


