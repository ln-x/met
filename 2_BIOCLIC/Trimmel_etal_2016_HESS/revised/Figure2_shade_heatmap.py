__author__ = 'lnx'

from pylab import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from matplotlib.offsetbox import AnchoredOffsetbox, AuxTransformBox, VPacker,\
    TextArea, DrawingArea
from pandas import Series, DataFrame
import calendar
from scipy import stats
import seaborn as sns


Condition = pd.read_csv('/home/lnx/PycharmProjects/HS/S250_P_STQ_2085_1a_MLF/outputfiles/Condition2.txt', skiprows=6, sep='\s+', index_col='Datetime') #, parse_dates="Datetime"
#print Condition
#Condition = Condition[:][5]

#temps_color = ["#FCF8D4", "#FAEAB9", "#FAD873", "#FFA500", "#FF8C00" ]
temps_color = ["#1b9e77","#d95f02"]

#sns.palplot(temps_color)
temps_cmap = mpl.colors.LinearSegmentedColormap.from_list("temp colors", temps_color)
#sns.set(style="darkgrid")
(figure, axes) = plt.subplots(figsize=(17,9))
sns.heatmap(Condition, cmap=temps_cmap,
            cbar_kws={"label":"anthropogenic influence"})
figure.tight_layout()
plt.show()

Rkm = np.arange(10.85,62.35,0.5)
Rkm = pd.DataFrame(Rkm, columns=['Rkm'])

fig, ax4 = plt.subplots(1,1, sharex= True)

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


#at = AnchoredText("d",loc=2, frameon=True)
#ax4.add_artist(at)
#sns.set(style="darkgrid")
#(figure, axes) = plt.subplots(figsize=(17,9))
ax4 = sns.heatmap(Condition, vmin=0.5, vmax=5.5, cmap=temps_cmap, xticklabels=False, yticklabels=False)
            #cbar_kws={"label":"anthropogenic influence"})
#figure.tight_layout()
#plt.legend()
plt.show()


