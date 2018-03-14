from TEB.displaySURFEX.CONVERTSURFEXTEXTE import loadfile
from TEB.displaySURFEX.CONVERTSURFEXTEXTE_UTCI import loadfile as loadfile_utci
import os
import shutil
import csv
import numpy as np

simnames=["100_Platz_A_N","100_Platz_A_N","101_Platz_B_N","102_Platz_A_A","103_Platz_B_B",\
"110_Platz_A_PV70","111_Platz_B_PV70", "200_Kreuzung_A_N","200_Kreuzung_A_N_25Grass","200_Kreuzung_A_N_25Trees",\
"200_Kreuzung_A_N_isolated","200_Kreuzung_A_N_PVroof" "200_Kreuzung_A_N_whiteroof",\
"201_Kreuzung_B_N","202_Kreuzung_A_A","203_Kreuzung_B_B","204_Kreuzung_B_W",\
"205_Kreuzung_W_W","210_Kreuzung_A_PV70", "211_Kreuzung_B_PV70"]
simperiods=["2017_170171WO","2017_170171NS","2016_365366WO","2016_365366NS"]
tempparameters= ["TCANYON","TWALLA1","TWALLB1", "TROAD1","TRAD_SHADE","TRAD_SUN"]
utcifiles =[""]

output = [[],[],[],[],[],[],[],[]]

for simname in simnames:
  for s in simperiods:
     try:
        path = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/lnx/" + simname + "/" + s + "/"
        for i in tempparameters:
        #    name[i] = "P"+i
        #    filepath = path + i + ".TXT"
        Ta = path + "TCANYON.TXT"
        Twa = path + "TWALLA1.TXT"
        Twb = path + "WALLB1.TXT"
        Tr = path + "TROAD1.TXT"
        MRTshade = path + "TRAD_SHADE.TXT"
        MRTsun = path + "TRAD_SUN.TXT"
        UTCIsun = path + "UTCI_OUTSUN.TXT"
        UTCIshade = path + "UTCI_OUTSHADE.TXT"
        Ta_values = loadfile(Ta)
        Twa_values = loadfile(Twa)
        #Twb_values = loadfile(Twb)
        #Tr_values = loadfile(Tr)
        #MRTshade_values = loadfile(MRTshade)
        #MRTsun_values = loadfile(MRTsun)
        #UTCIshade_values = loadfile_utci(UTCIshade)
        #UTCIsun_values = loadfile_utci(UTCIsun)
        print np.max(Ta_values), np.max(Twa_values)#, np.max(MRTshade_values),np.max(UTCIshade_values)
        #output[0].append(simname)
        #output[1].append(s)
        #output[2].append(np.max(Ta_values))
        #output[3].append(np.min(Ta_values))
        #output[4].append(np.max(Twa_values))
        #output[5].append(np.min(Twa_values))
        #output[6].append(np.max(Twb_values))
        #output[7].append(np.max(Twb_values))

        try:
          print "test"
          Ta_values = loadfile(Ta)


          #print type(simname)
       #except OSError: #IOError
        except Exception:
          pass
     except Exception:
         pass
#print len(output[0]),len(output[1]),len(output[2]),len(output[3])

simnames  = np.array(output[0])
per_ori  = np.array(output[1])
Ta_max = np.array(output[2])
Ta_min = np.array(output[3])
Twa_max = np.array(output[4])
Twa_min = np.array(output[5])
Twb_max = np.array(output[6])
Twb_min = np.array(output[7])

ab = np.zeros(simnames.size, dtype=[('var0', 'U32'),('var1', 'U32'), ('var2', float), ('var3', float),
              ('var4', float),('var5', float), ('var6', float),('var7', float)])
#print ab
ab['var0'] = simnames
ab['var1'] = per_ori
ab['var2'] = Ta_max
ab['var3'] = Ta_min
ab['var4'] = Twa_max
ab['var5'] = Twa_min
ab['var6'] = Twb_max
ab['var7'] = Twb_min

np.savetxt('test.txt', ab, fmt="%10s,%10s, %10.3f, %10.3f, %10.3f, %10.3f, %10.3f, %10.3f",
           header="simname,per_ori,Ta_max,Ta_min,Twa_max,Twa_min,Twb_max,Twb_min")

#with open('workfile.txt','w') as f:
#    np.savetxt(f,np.column_stack((output[0],output[1],output[2],output[3])),
#              fmt='%s,%32s,%2.2f,%2.2f',
#              header="simnam,dateORIE,Ta_max,Ta_min")
   # for slice_2d in b[1,1]:
#   np.savetxt(f,output,fmt='%10s;%10s;%3.2f;%3.2f',
#              header="simname;simperiod;Ta_max;Ta_min")

#f.close()


"""
        #os.chdir(path1)
        #print path1, print simname
        #files = os.listdir('./')
        #files = os.walk('./')
        #print files
        
        
        shutil.copytree(path1,path2)
		os.chdir(path1)
		with open('HeatSource_Control.csv','rb') as control :
			with open('fichier.csv','wb') as fichier :
				reader=csv.reader(control, delimiter=',', quotechar='|')
				writer=csv.writer(fichier,delimiter=',', quotechar='|')
				for row in reader :
					if row[0]=='2' :
						writer.writerow([row[0],row[1],name+"_049_"+s])
					elif row[0]=='4' :
						output=path2"outputfiles/"
						writer.writerow([row[0],row[1],output])
					elif row[0]=='5' :
						input=path2"inputfiles/"
						writer.writerow([row[0],row[1],input])
					else :
				writer.writerow(row)
		os.remove('HeatSource_Control.csv')
		os.rename('fichier.csv','HeatSource_Control.csv')
		execfile("Start_HS.py")
		shutil.rmtree(path1+"outputfiles/")
		shutil.copytree(path2+"ouputfiles/",path1+"outputfiles/")
		os.chdir("/home/heidi/hs")
		shutil.rmtree(path2)
"""