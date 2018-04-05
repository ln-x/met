import pandas as pd

path = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/"
file = path + "BUILT2.txt"
file2 = "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/Garden.txt"
file3= "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/FRAC_WATER2.txt"
file4= "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/FRAC_NATURE2.txt"
file5= "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/FRAC_TOWN2_sca.txt"
file6= "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/FRAC_TOWN2_str.txt"
file7= "/home/lnx/MODELS/SURFEX/2_source/SURFEX_TRUNK_4818/trunk/MY_RUN/KTEST/hapex/FRAC_TOWN2.txt"

BUILT = pd.read_csv(file, sep='\t', names=["lat","lon","val"])
GARDEN = pd.read_csv(file2, sep='\t', names=["lat","lon","val"])
FRAC_WATER = pd.read_csv(file3, sep='\t', names=["lat","lon","val"])
FRAC_NATURE = pd.read_csv(file4, sep='\t', names=["lat","lon","val"])
FRAC_TOWN_S3 = pd.read_csv(file5, sep='\t', names=["lat","lon","val"])
FRAC_TOWN_S4 = pd.read_csv(file6, sep='\t', names=["lat","lon","val"])
FRAC_TOWN_STQ = pd.read_csv(file7, sep='\t', names=["lat","lon","val"])

print (FRAC_TOWN_STQ["val"].value_counts()*111110.9)/1000000
print (FRAC_TOWN_S3["val"].value_counts()*111110.9)/1000000
print (FRAC_TOWN_S4["val"].value_counts()*111110.9)/1000000


exit()

'''update Nature fraction for increased Town fraction'''

FRAC_NATURE_S3 = FRAC_NATURE.copy()
FRAC_NATURE_S4 = FRAC_NATURE.copy()
FRAC_NATURE_S3["val"] = 1 - FRAC_WATER["val"] - FRAC_TOWN_S3["val"]
FRAC_NATURE_S4["val"] = 1 - FRAC_WATER["val"] - FRAC_TOWN_S4["val"]


#print FRAC_NATURE_S3.head()


#FRAC_NATURE_S3.to_csv(path + "FRAC_NATURE_baulandreserve.txt", sep='\t', index=None, header=None)
#FRAC_NATURE_S4.to_csv(path + "FRAC_NATURE_structured1.txt", sep='\t', index=None, header=None)



'''check BUILT/GARDEN fraction'''
#print BUILT.head(), BUILT["val"]*1.1
#FRAC_TOWN_S3_buff["val"] = FRAC_TOWN_S3_buff.apply(lambda x: x["val"] * 0 if x[0] > LAT_MAX10)# else x["val"], axis=1)


addBUILT = BUILT["val"]*0.1
BUILT110 = BUILT.copy()
BUILT110["val"] = BUILT["val"]+addBUILT
GARDENred = GARDEN.copy()
GARDENred["val"] = GARDEN["val"]-addBUILT
BUILTGARDEN_old = BUILT["val"]+GARDEN["val"]
BUILTGARDEN_new = BUILT110["val"]+GARDENred["val"]
##print BUILTGARDEN_old.loc[BUILTGARDEN_old > 1.0] - BUILTGARDEN_new.loc[BUILTGARDEN_new > 1.0]


#BUILT110.to_csv( path + "BUILT110_new.txt", sep='\t', index=None, header=None)
#GARDENred.to_csv(path + "Garden_new.txt", sep='\t', index=None, header=None)

print len(FRAC_TOWN_S4), len(FRAC_NATURE), len(BUILT), len(BUILT110), len(GARDEN)