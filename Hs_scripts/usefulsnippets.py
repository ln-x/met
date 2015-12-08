PLOTTING:

#default settings can be looked at and changed at: /usr/lib/python2.7/matplotlib/rcsetup.py !
# e.g. savefig.dpi = 100
#      savefig.format = png
#      figure.figsize [8.0,6.0] #inch
#      figure.dpi [80]



#a = [x for x in a if x != -9999]


#axes2.set_aspect('equal')

#plt.text(100, 100,'B',fontsize=50)


#fig.set_dpi(300)



# ax.set_xlim((0, 2*np.pi))
# ax.set_xticks([0, np.pi, 2*np.pi])

#ax.set_xticks([735077,735078,0.25])
#ax.set_xticks([0.125,0.25,0.375, 0.5, 0.625, 0.75, 0.875])

#plt.legend(loc=1, ncol=2, fontsize='small')

#plt.subplots_adjust(bottom=.2)
#plt.subplots_adjust(left=.2)


#fig.set_dpi(300)
#fig.set_figwidth(3.39) # 3.39 inch = 86 mm in 300dpi
#fig.set_figheight(2.54) #2.54 inch = 64.5 mm in 300dpi (86 *3/4)
#fig.set_size_inches(3.39,2.54)

#between subplots:  wspace=None



STATISTICS:

#Calculate RMSE for each timestep
rmse_uw = []
for i in x:
    rmse_uw.append(((uws[i] - uw[i])**2)**0.5)


# Calculate RMSE mean for whole period
rmse_m_uw = 0
for i in x:
    rmse_m_uw = rmse_m_uw + rmse_uw[i]
    #print 'i=',i, rmse_uw[i], rmse_m_uw
rmse_m_uw = rmse_m_uw/len(rmse_uw)
print "result= ", rmse_m_uw


