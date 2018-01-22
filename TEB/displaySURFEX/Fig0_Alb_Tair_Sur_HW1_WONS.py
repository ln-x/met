# -*- coding: utf-8 -*-
__author__ = 'lnx'

import pandas as pd
import matplotlib.pyplot as plt
from CONVERTSURFEXTEXTE import loadfile
import numpy as np
import datetime
from matplotlib.dates import DateFormatter

S200wo_Ta = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171WO/TCANYON.TXT"
S200wo_Twa = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171WO/TWALLA1.TXT"
S200wo_Twb = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171WO/TWALLB1.TXT"
S200wo_Tg = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171WO/TROAD1.TXT"

S200ns_Ta = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171NS/TCANYON.TXT"
S200ns_Twa = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171NS/TWALLA1.TXT"
S200ns_Twb = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171NS/TWALLB1.TXT"
S200ns_Tg = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/200_Kreuzung_A_N/2017_170171NS/TROAD1.TXT"

S201wo_Ta = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170171WO/TCANYON.TXT"
S201wo_Twa = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170171WO/TWALLA1.TXT"
S201wo_Twb = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170171WO/TWALLB1.TXT"
S201wo_Tg = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170171WO/TROAD1.TXT"

S201ns_Ta = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170171NS/TCANYON.TXT"
S201ns_Twa = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170171NS/TWALLA1.TXT"
S201ns_Twb = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170171NS/TWALLB1.TXT"
S201ns_Tg = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/201_Kreuzung_B_N/2017_170171NS/TROAD1.TXT"

S200wo_Ta_values = loadfile(S200wo_Ta)
S200wo_Twa_values = loadfile(S200wo_Twa)
S200wo_Twb_values = loadfile(S200wo_Twb)
S200wo_Tg_values = loadfile(S200wo_Tg)

S200ns_Ta_values = loadfile(S200ns_Ta)
S200ns_Twa_values = loadfile(S200ns_Twa)
S200ns_Twb_values = loadfile(S200ns_Twb)
S200ns_Tg_values = loadfile(S200ns_Tg)

S201wo_Ta_values = loadfile(S201wo_Ta)
S201wo_Twa_values = loadfile(S201wo_Twa)
S201wo_Twb_values = loadfile(S201wo_Twb)
S201wo_Tg_values = loadfile(S201wo_Tg)

S201ns_Ta_values = loadfile(S201ns_Ta)
S201ns_Twa_values = loadfile(S201ns_Twa)
S201ns_Twb_values = loadfile(S201ns_Twb)
S201ns_Tg_values = loadfile(S201ns_Tg)

start = datetime.datetime(2017,6,19,0)
#print start.hour
numminutes = 2880
timelist = []
xaxis=[]
for x in range (0, numminutes,10):
    moment = start + datetime.timedelta(minutes = x)
    hour = moment.hour
    timelist.append(moment)
    xaxis.append(hour)
xaxis = xaxis[:-1]
timelist = timelist[:-1]

fig = plt.figure()
ax = fig.add_subplot(221)
ax.set_title(r"$\alpha_{G}$ =.13,WO")
ax.plot(timelist[:-144],S200wo_Ta_values[:-144], label="Lufttemperatur", color="yellow")#,linestyle="dashed")
ax.plot(timelist[:-144],S200wo_Twa_values[:-144], label="Wand A",color="red")
ax.plot(timelist[:-144],S200wo_Twb_values[:-144], label="Wand B",color="blue")
ax.plot(timelist[:-144],S200wo_Tg_values[:-144], label="Boden",color="black")
ax.set_ylim([0,70])
#ax.set_xlim([1,143])
ax.set_ylabel(u'Temperatur [°C]')

#ax1.legend(loc="lower center",fontsize='small')
#ax.set_xlabel('[UTC]')

ax = fig.add_subplot(222)
ax.set_title(r"$\alpha_{G}$ =.13,NS")
ax.plot(timelist[:-144],S200ns_Ta_values[:-144], label="Lufttemperatur", color="yellow")#,linestyle="dashed")
ax.plot(timelist[:-144],S200ns_Twa_values[:-144], label=u"Südfassade",color="red")
ax.plot(timelist[:-144],S200ns_Twb_values[:-144], label="Nordfassade",color="blue")
ax.plot(timelist[:-144],S200ns_Tg_values[:-144], label="Boden",color="black")
ax.set_ylim([0,70])
#ax.set_xlim([1,143])
plt.setp(ax.get_yticklabels(), visible=False)
#ax.set_ylabel(u'Temperatur [°C]')
#ax2.legend(loc="lower center",fontsize='small')
#ax.set_xlabel('[UTC]')

ax = fig.add_subplot(223)
ax.set_title(r"$\alpha_{G}$ =.56,WO")
ax.plot(timelist[:-144],S201wo_Ta_values[:-144], label="Lufttemperatur", color="yellow")#,linestyle="dashed")
ax.plot(timelist[:-144],S201wo_Twa_values[:-144], label=u"Südfassade",color="red")
ax.plot(timelist[:-144],S201wo_Twb_values[:-144], label="Nordfassade",color="blue")
ax.plot(timelist[:-144],S201wo_Tg_values[:-144], label="Boden",color="black")
ax.set_ylim([0,70])
#ax.set_xlim([1,143])
ax.set_ylabel(u'Temperatur [°C]')
myFmt = DateFormatter("%H")
ax.xaxis.set_major_formatter(myFmt)
#ax3.legend(loc="lower center",fontsize='small')
ax.set_xlabel('[UTC]')

ax = fig.add_subplot(224)
ax.set_title(r"$\alpha_{G}$ =.56,NS")  #HW1, 20.6.2017
ax.plot(timelist[:-144],S201ns_Ta_values[:-144], label="Lufttemperatur", color="yellow")#,linestyle="dashed")
ax.plot(timelist[:-144],S201ns_Twa_values[:-144], label=u"Südfassade",color="red")
ax.plot(timelist[:-144],S201ns_Twb_values[:-144], label="Nordfassade",color="blue")
ax.plot(timelist[:-144],S201ns_Tg_values[:-144], label="Boden",color="black")
plt.setp(ax.get_yticklabels(), visible=False)
#ax.set_ylabel(u'Temperatur [°C]')
#ax4.legend(loc="lower center",fontsize='small')
ax.set_xlabel('[UTC]')
ax.set_ylim([0,70])
#ax.set_xlim([1,143])
fig.autofmt_xdate(rotation=0)
myFmt = DateFormatter("%H")
ax.xaxis.set_major_formatter(myFmt)
plt.show()
