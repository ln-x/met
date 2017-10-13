    import arcpy 
    import numpy as np 
    import pandas as pd 
    from pandas import DataFrame  
    #Create variable for feature class 
    fc = r'C:\Projects\MyGeodatabase.gdb\Groundwater\WaterQuality'  
    #Create field list with a subset of the fields (cannot include datetime fields for  
    #da.FeatureClassToNumPy tool) 
    fc_fields = ['OBJECTID', 'WellID', 'Aquifer', 'FlowPeriod', 'As_D_Val','Cu_D_Val','GWElev', 'MeasuringPtElev', 'Total_depth', 'E', 'N']  
    #Convert Feature Class to NumPy Array.  Due to the fact that NumPy arrays do not 
    #accept null values for integer fields, I had to convert null values to -99999 
    fc_np = arcpy.da.FeatureClassToNumPyArray(fc, fc_fields, skip_nulls = False, null_value = -99999)  
    #Convert NumPy array to pandas DataFrame.   
    fc_pd = DataFrame(fc_np)  7