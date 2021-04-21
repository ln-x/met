

ax1 = fig.add_subplot(312)
#fig.set_size_inches(3.39,2.54)
ax1 = plt.gca()
#ax2 = ax1.twinx() #JAEG, LOB, ZA, STEF
ax1.plot(nox_1990_2020_da['AT9STEF'][start:end], color='grey', label = "nox_obs_d_stef" )
#ax1.plot((wrfc_no[:456,109,58])*1000 + (wrfc_no2[:456,109,58])*1000, color='blue', label="nox_wrfc_h", linestyle="dotted")
ax1.plot(emep_nox_d, color='green', label="nox_emep_d", linestyle="dashed")
ax1.set_xlabel("days")
ax1.set_ylabel("ppb", size="medium")
#ax1.set_ylabel("mg m-2 h-1", size="medium")
#ax2.set_ylabel("degC", size="medium")
ax1.legend(loc='upper left')
#ax2.legend(loc='upper right')
#ax1.set_ylim(0, 5)
#ax2.set_ylim(10, 50)