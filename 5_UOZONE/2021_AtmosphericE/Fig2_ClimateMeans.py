import seaborn as sn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_at = {'Jan': [3.8, 0.4, 0.9], 'Feb': [-2.5, 3.4, 5.1], 'Mar':[-2.2,3.3,1.7], 'Apr':[5.1,1.4,1.6],
           'May':[3.1,-2.3,-1.1],'Jun':[2.9,4.9,0.4],'Jul':[2.0,1.7,0.6],'Aug':[3.4,2.5,1.7],'Sep':[2.1,1.3,1.5],'Oct':[2.8,1.8,1.0],'Nov':[1.4,2.8,1.1],'Dec':[1.7,2.5,2.1]}

df_at = pd.DataFrame(data_at, index=['2018','2019','2020'])
sn.heatmap(df_at, cbar_kws={'label': 'AT diff to 1981-2010 [°C]'},cmap="coolwarm") #bwr
#sn.heatmap(df, annot=True, annot_kws={'size': 7})
plt.show()

data_pr = {'Jan': [8, 34, -19], 'Feb': [-15, -26, 11], 'Mar':[-1,2,-31], 'Apr':[-38,-19,-37],
           'May':[2,76,12],'Jun':[-25,-24,22],'Jul':[57,-11,7],'Aug':[-23,-19,28],
           'Sep':[38,1,14],'Oct':[-9,-12,92],'Nov':[-2,-4,-35],'Dec':[-63,-48,-89]}

df_pr = pd.DataFrame(data_pr, index=['2018','2019','2020'])
sn.heatmap(df_at, cbar_kws={'label': 'PR diff to 1981-2010 [mm]'},cmap="BrBG") # , cmap="bwr")
plt.show()
