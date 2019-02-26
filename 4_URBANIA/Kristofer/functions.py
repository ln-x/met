
def DataArray_to_dataframe(array1, array2, array3):
    """
    Converts 3 DataArrays with metadata to an pandas DataFrame
    & drops XTIME so it can calculate the temporal means betweens he columns
    
    Input: 3 DataArray
    Output: 1 Dataframe, Mean of Columns
    """
    frame = array1.to_dataframe()
    frame[str(array2.name)] = array2.to_series()
    frame[str(array3.name)] = array3.to_series()
    #frame = frame.drop(columns=['XTIME'])
    #mean = frame.mean(axis=1)
    return frame #, mean

def DataArray_drop_to_Frame(array1, array2, array3):
    """
    Converts 3 DataArrays with metadata to an pandas DataFrame
    & drops XTIME so it can calculate the temporal means betweens he columns
    
    Input: 3 DataArray
    Output: 1 Dataframe, Mean of Columns
    """
    frame = array1.to_dataframe()
    frame[str(array2.name)] = array2.to_series()
    frame[str(array3.name)] = array3.to_series()
    #frame = frame.drop(columns=['XTIME'])
    frame = frame.drop(columns=['XLONG'])
    frame = frame.drop(columns=['XLAT'])
    #mean = frame.mean(axis=1)
    return frame #, mean




def collect_data(date, para, cuttime, region, region_sn, region_we, path):
    """
    cuts out the defined areas and calculates
    
    hourly median
    daily min / max
    
    for all 3 runs 
    used for MIN/MAX box plots
    Output: sorted list of all areas with runs as dataarray
    
    """
    import wrf
    import pandas as pd
    import xarray as xr
    import numpy as np
    from netCDF4 import Dataset
    from wrf import getvar

    
    filename = 'wrfout_d03_' + date + '_18_00_00.nc'
    
    ref = 'REF_Run_' + str(pd.to_datetime(date).year) # reference run
    spr = 'SPR_Run_' + str(pd.to_datetime(date).year) # sprawl run 
    opt = 'OPT_Run_' + str(pd.to_datetime(date).year) # optimized city run

    ref_filepath = path + ref + '/'
    spr_filepath = path + spr + '/'
    opt_filepath = path + opt + '/'

    ref_ncfile = Dataset(ref_filepath + filename)
    spr_ncfile = Dataset(spr_filepath + filename)
    opt_ncfile = Dataset(opt_filepath + filename)
    
    times = getvar(ref_ncfile, "Times", timeidx=wrf.ALL_TIMES, meta=False) # FC times in np.datetime64 format - very ugly
    init = pd.to_datetime(times[0]) # converts the numpy datetime to datetime datetime format
    init = str(init) # initial time of wrf dataset

    
    ref_data = getvar(ref_ncfile, para, timeidx=wrf.ALL_TIMES)
    spr_data = getvar(spr_ncfile, para, timeidx=wrf.ALL_TIMES)
    opt_data = getvar(opt_ncfile, para, timeidx=wrf.ALL_TIMES)

    ref_d={}
    spr_d={}
    opt_d={}
    
    for i,j in zip(region_sn, region_we):
        ref_d["{0}".format(i)] = ref_data.isel(south_north=slice(region_sn[i][0],region_sn[i][1]), 
          west_east=slice(region_we[j][0],region_we[j][1]))
        spr_d["{0}".format(i)] = spr_data.isel(south_north=slice(region_sn[i][0],region_sn[i][1]), 
          west_east=slice(region_we[j][0],region_we[j][1]))
        opt_d["{0}".format(i)] = opt_data.isel(south_north=slice(region_sn[i][0],region_sn[i][1]), 
          west_east=slice(region_we[j][0],region_we[j][1]))
    
    
    for name in ref_d:
        for t in cuttime:
            ref_d["{0}".format(name)] = ref_d["{0}".format(name)].where(ref_d["{0}".format(name)]['Time'].dt.day != t.day, drop=True).rename("{0}".format(name) + '_' + ref[:3])
            spr_d["{0}".format(name)] = spr_d["{0}".format(name)].where(spr_d["{0}".format(name)]['Time'].dt.day != t.day, drop=True).rename("{0}".format(name) + '_' + spr[:3])
            opt_d["{0}".format(name)] = opt_d["{0}".format(name)].where(opt_d["{0}".format(name)]['Time'].dt.day != t.day, drop=True).rename("{0}".format(name) + '_' + opt[:3])

    ref_math={}
    spr_math={}
    opt_math={}
    
    for name in ref_d:
        ref_math["{0}_median".format(name)] = ref_d["{0}".format(name)].groupby(ref_d["{0}".format(name)].Time.dt.hour).median() - 273.15
        ref_math["{0}_min".format(name)] = ref_d["{0}".format(name)].groupby(ref_d["{0}".format(name)].Time.dt.day).min(axis=0) - 273.15
        ref_math["{0}_max".format(name)] = ref_d["{0}".format(name)].groupby(ref_d["{0}".format(name)].Time.dt.day).max(axis=0) - 273.15
        spr_math["{0}_median".format(name)] = spr_d["{0}".format(name)].groupby(spr_d["{0}".format(name)].Time.dt.hour).median() - 273.15
        spr_math["{0}_min".format(name)] = spr_d["{0}".format(name)].groupby(spr_d["{0}".format(name)].Time.dt.day).min(axis=0) - 273.15
        spr_math["{0}_max".format(name)] = spr_d["{0}".format(name)].groupby(spr_d["{0}".format(name)].Time.dt.day).max(axis=0) - 273.15
        opt_math["{0}_median".format(name)] = opt_d["{0}".format(name)].groupby(opt_d["{0}".format(name)].Time.dt.hour).median() - 273.15
        opt_math["{0}_min".format(name)] = opt_d["{0}".format(name)].groupby(opt_d["{0}".format(name)].Time.dt.day).min(axis=0) - 273.15
        opt_math["{0}_max".format(name)] = opt_d["{0}".format(name)].groupby(opt_d["{0}".format(name)].Time.dt.day).max(axis=0) - 273.15
    
    reg_max = {}
    reg_min = {}
    reg_med = {}
    for name in ref_d:
        reg_max["{0}_max".format(name)] = DataArray_drop_to_Frame(ref_math["{0}_max".format(name)], spr_math["{0}_max".format(name)], opt_math["{0}_max".format(name)])
        reg_min["{0}_min".format(name)] = DataArray_drop_to_Frame(ref_math["{0}_min".format(name)], spr_math["{0}_min".format(name)], opt_math["{0}_min".format(name)])
        reg_med["{0}_median".format(name)] = DataArray_to_dataframe(ref_math["{0}_median".format(name)], spr_math["{0}_median".format(name)], opt_math["{0}_median".format(name)])

    reg_med = sorted(reg_med.items(), key=lambda x: x[0])
    reg_min = sorted(reg_min.items(), key=lambda x: x[0])
    reg_max = sorted(reg_max.items(), key=lambda x: x[0])

    return reg_med, reg_min, reg_max, init


def collect_data_speicherterm(date, para, cuttime, region, region_sn, region_we, path):
    """
    cuts out the defined areas and calculates
    
    hourly median
    daily min / max
    
    for all 3 runs 
    used for MIN/MAX box plots
    Output: sorted list of all areas with runs as dataarray
    
    """
    import wrf
    import pandas as pd
    import xarray as xr
    import numpy as np
    from netCDF4 import Dataset
    from wrf import getvar

    
    filename = 'wrfout_d03_' + date + '_18_00_00.nc'
    
    ref = 'REF_Run_' + str(pd.to_datetime(date).year) # reference run
    spr = 'SPR_Run_' + str(pd.to_datetime(date).year) # sprawl run 
    opt = 'OPT_Run_' + str(pd.to_datetime(date).year) # optimized city run

    ref_filepath = path + ref + '/'
    spr_filepath = path + spr + '/'
    opt_filepath = path + opt + '/'

    ref_ncfile = Dataset(ref_filepath + filename)
    spr_ncfile = Dataset(spr_filepath + filename)
    opt_ncfile = Dataset(opt_filepath + filename)
    
    times = getvar(ref_ncfile, "Times", timeidx=wrf.ALL_TIMES, meta=False) # FC times in np.datetime64 format - very ugly
    init = pd.to_datetime(times[0]) # converts the numpy datetime to datetime datetime format
    init = str(init) # initial time of wrf dataset

    
    ref_data = getvar(ref_ncfile, para, timeidx=wrf.ALL_TIMES)
    spr_data = getvar(spr_ncfile, para, timeidx=wrf.ALL_TIMES)
    opt_data = getvar(opt_ncfile, para, timeidx=wrf.ALL_TIMES)

    ref_d={}
    spr_d={}
    opt_d={}
    
    for i,j in zip(region_sn, region_we):
        ref_d["{0}".format(i)] = ref_data.isel(south_north=slice(region_sn[i][0],region_sn[i][1]), 
          west_east=slice(region_we[j][0],region_we[j][1]))
        spr_d["{0}".format(i)] = spr_data.isel(south_north=slice(region_sn[i][0],region_sn[i][1]), 
          west_east=slice(region_we[j][0],region_we[j][1]))
        opt_d["{0}".format(i)] = opt_data.isel(south_north=slice(region_sn[i][0],region_sn[i][1]), 
          west_east=slice(region_we[j][0],region_we[j][1]))
    
    
    for name in ref_d:
        for t in cuttime:
            ref_d["{0}".format(name)] = ref_d["{0}".format(name)].where(ref_d["{0}".format(name)]['Time'].dt.day != t.day, drop=True).rename("{0}".format(name) + '_' + ref[:3])
            spr_d["{0}".format(name)] = spr_d["{0}".format(name)].where(spr_d["{0}".format(name)]['Time'].dt.day != t.day, drop=True).rename("{0}".format(name) + '_' + spr[:3])
            opt_d["{0}".format(name)] = opt_d["{0}".format(name)].where(opt_d["{0}".format(name)]['Time'].dt.day != t.day, drop=True).rename("{0}".format(name) + '_' + opt[:3])

    ref_math={}
    spr_math={}
    opt_math={}
    
    for name in ref_d:
#        ref_math["{0}_median".format(name)] = ref_d["{0}".format(name)].groupby(ref_d["{0}".format(name)].Time.dt.hour).median() - 273.15
        ref_math["{0}_min".format(name)] = ref_d["{0}".format(name)].groupby(ref_d["{0}".format(name)].Time.dt.day).min(axis=0).median(dim={'south_north','west_east'}) - 273.15
#        ref_math["{0}_max".format(name)] = ref_d["{0}".format(name)].groupby(ref_d["{0}".format(name)].Time.dt.day).max(axis=0) - 273.15
#        spr_math["{0}_median".format(name)] = spr_d["{0}".format(name)].groupby(spr_d["{0}".format(name)].Time.dt.hour).median() - 273.15
        spr_math["{0}_min".format(name)] = spr_d["{0}".format(name)].groupby(spr_d["{0}".format(name)].Time.dt.day).min(axis=0).median(dim={'south_north','west_east'}) - 273.15
#        spr_math["{0}_max".format(name)] = spr_d["{0}".format(name)].groupby(spr_d["{0}".format(name)].Time.dt.day).max(axis=0) - 273.15
#        opt_math["{0}_median".format(name)] = opt_d["{0}".format(name)].groupby(opt_d["{0}".format(name)].Time.dt.hour).median() - 273.15
        opt_math["{0}_min".format(name)] = opt_d["{0}".format(name)].groupby(opt_d["{0}".format(name)].Time.dt.day).min(axis=0).median(dim={'south_north','west_east'}) - 273.15
#        opt_math["{0}_max".format(name)] = opt_d["{0}".format(name)].groupby(opt_d["{0}".format(name)].Time.dt.day).max(axis=0) - 273.15
    
#    reg_max = {}
    reg_min = {}
#    reg_med = {}
    for name in ref_d:
#        reg_max["{0}_max".format(name)] = DataArray_drop_to_Frame(ref_math["{0}_max".format(name)], spr_math["{0}_max".format(name)], opt_math["{0}_max".format(name)])
        reg_min["{0}_min".format(name)] = DataArray_to_dataframe(ref_math["{0}_min".format(name)], spr_math["{0}_min".format(name)], opt_math["{0}_min".format(name)])
#        reg_med["{0}_median".format(name)] = DataArray_to_dataframe(ref_math["{0}_median".format(name)], spr_math["{0}_median".format(name)], opt_math["{0}_median".format(name)])

#    reg_med = sorted(reg_med.items(), key=lambda x: x[0])
    reg_min = sorted(reg_min.items(), key=lambda x: x[0])
#    reg_max = sorted(reg_max.items(), key=lambda x: x[0])

    return reg_min, init
