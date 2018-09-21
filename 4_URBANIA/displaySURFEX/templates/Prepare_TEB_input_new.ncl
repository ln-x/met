load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/wrf/WRFUserARW.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/wrf/WRF_contributed.ncl"


  aw    = 17.269388             ; constants for saturation
  bw    = 35.86                 ; vapor pressure over water
  ai    = 21.8745584            ; and ice
  bi    = 7.66                  ;
  Cn    = 2.16679               ; gK/J 
  
  infile = systemfunc("ls wrfout_d03*:00:00")
  nfiles = dimsizes(infile)
 
  if (.not.any(ismissing(infile) .and. nfiles .eq. 1)) then
    fin        = addfile(infile,"r")
    CTimes     = fin->Times                        ; times in a daily file.
    LON        = fin->XLONG(0,:,:)
    LAT        = fin->XLAT(0,:,:)
    ZS         = fin->HGT(0,:,:)
    Tair       = fin->T2
    PSurf      = fin->PSFC
    DIR_SWdown = fin->SWDOWN
    LWdown     = fin->GLW
    Prn        = fin->RAINNC
    Prc        = fin->RAINC
    ucomp      = fin->U10
    vcomp      = fin->V10  
    
    rh2m   = wrf_user_getvar(fin,"rh2",-1)
    rh2m   = where(rh2m .lt.   0.0,   0.0, rh2m)
    rh2m   = where(rh2m .gt. 100.0, 100.0, rh2m)
  end if
 time   = wrf_times_c(CTimes, 1)
 ntim   = dimsizes(time)
 dims   = dimsizes(Tair)
 nlat   = dims(1)
 nlon   = dims(2)
 print("nlat and nlon are "+nlat+"  "+nlon)
 
   
 Wind_DIR = wind_direction(ucomp,vcomp,0)
 Wind     = ucomp
 Wind     = (/ sqrt(ucomp^2+vcomp^2) /)                       ;wind_speed(ucomp,vcomp)
 
 printVarSummary(time)
 printVarSummary(LON)
 printVarSummary(LAT)
 printVarSummary(Tair)
 printVarSummary(PSurf)
 printVarSummary(ZS)
 printVarSummary(Wind_DIR)
 printVarSummary(Wind)

 printMinMax(rh2m,True)
 
;............... Humidity Calculation ( http://www.vaisala.com/Vaisala%20Documents/Application%20notes/Humidity_Conversion_Formulas_B210973EN-F.pdf ) ..........
; A = Cn · em / Tair  (g/m3)     
 Qair = rh2m                                           ; define new variable

 esm_wat = 6.1078 * exp(aw * (Tair-273.16)/(Tair-bw)) ; calculate es over water(land)
 esm_ice = 6.1078 * exp(ai * (Tair-273.16)/(Tair-bi)) ; calculate es over ice (frozed ground)
 esm     = where(Tair.lt.273.16,esm_ice,esm_wat)         ; combine them to get correct es
 em      = rh2m * esm                                       ; em is in Pa, divide by 100 to get result in hPa.
 
 Qair = ( Cn * em ) / Tair      ;; (g/m3)
 Qair = Qair * 0.001            ; kg/m3
  
 printVarSummary(Qair)
 printMinMax(Qair,True)

; ............. Calculation Rain and Snow rates .......
 
  accum  = Prn + Prc
  tmpv   = accum(1:ntim-1,:,:)                            ;trick to allocate memory and retain metadata.
  tmpv   = (accum(1:ntim-1,:,:) - accum(0:ntim-2,:,:))
     
  Rainf  = Prn
  Rainf(1:,:,:) = (/tmpv/)
  delete(tmpv)
    
  Rainf = (Rainf/3600.0)              ; kg/m2/
  Snowf = Rainf
  Snowf = 0.0
  
  
; .......................Diffuse Radiation........................

  printMinMax(DIR_SWdown,True)
  SCA_SWdown = DIR_SWdown

  SCA_SWdown = (/DIR_SWdown * 0.15 /)
  
  printMinMax(SCA_SWdown,True)
  
  
  CO2air = Snowf
  CO2air = 0.0

  
;.................... Final..........

 timef = cd_convert(time,"minutes since 2015-01-01 00:00:00")
 FORC_TIME_STEP =  3600.0D
 FORC_TIME_STEP!0 = "ncl_scalar"
 
 LON1d   = todouble(ndtooned(LON))
 LAT1d   = todouble(ndtooned(LAT))
 ZS1d    = todouble(ndtooned(ZS))
 
 ZREF1d    = LON1d
 UREF1d    = LON1d
 
 ZREF1d    = 2.0
 UREF1d   = 10.0
 
 ;FORC_TIME_STEP!0 = "con"
 ZREF1d!0 = "Number_of_points"
 UREF1d!0 = "Number_of_points"
 
 LON1d!0 = "Number_of_points"
 LAT1d!0 = "Number_of_points"
  ZS1d!0  = "Number_of_points"
 
 printVarSummary(LON)
 copy_VarCoords(LON,LAT)
 copy_VarCoords(LON,ZS)

 Tair1d       =  todouble(reshape(Tair,(/ntim,nlat*nlon/)))
 Qair1d       =  todouble(reshape(Qair,(/ntim,nlat*nlon/)))
 PSurf1d      =  todouble(reshape(PSurf,(/ntim,nlat*nlon/)))
 Rainf1d      =  todouble(reshape(Rainf,(/ntim,nlat*nlon/)))
 Snowf1d      =  todouble(reshape(Snowf,(/ntim,nlat*nlon/)))
 Wind1d       =  todouble(reshape(Wind,(/ntim,nlat*nlon/)))
 Wind_DIR1d   =  todouble(reshape(Wind_DIR,(/ntim,nlat*nlon/)))
 LWdown1d     =  todouble(reshape(LWdown,(/ntim,nlat*nlon/)))
 DIR_SWdown1d =  todouble(reshape(DIR_SWdown,(/ntim,nlat*nlon/)))
 SCA_SWdown1d =  todouble(reshape(SCA_SWdown,(/ntim,nlat*nlon/)))
 CO2air1d     =  todouble(reshape(CO2air,(/ntim,nlat*nlon/)))
                                     
 Tair1d!0 = "time"
 Tair1d!1 = "Number_of_points"

 CO2air1d@long_name ="CO2 Concentration"
 DIR_SWdown1d@long_name ="downward direct shortwave radiation"
 FORC_TIME_STEP@long_name ="forcing time step"
 LAT1d@long_name ="latitudes"
 LON1d@long_name ="longitudes"
 LWdown1d@long_name ="downward longwave radiation"
 PSurf1d@long_name ="surface pressure"
 Qair1d@long_name ="air specific humidity"
 Rainf1d@long_name ="rainfall rate"
 SCA_SWdown1d@long_name ="downward diffuse shortwave radiation"
 Snowf1d@long_name ="snowfall rate"
 Tair1d@long_name ="air temperature"
 UREF1d@long_name ="Reference_Height_for_Wind"
 Wind1d@long_name ="wind speed"
 Wind_DIR1d@long_name ="wind direction"
 ZREF1d@long_name ="Reference_Height"
 ZS1d@long_name ="surface orograhpy"

 
 CO2air1d@units ="kg/m3"
 DIR_SWdown1d@units ="W/m2"
 LAT1d@units ="degrees_north"
 LON1d@units ="degrees_east"
 LWdown1d@units ="W/m2"
 PSurf1d@units ="Pa"
 Qair1d@units ="Kg/Kg"
 Rainf1d@units ="Kg/m2/s"
 SCA_SWdown1d@units ="W/m2"
 Snowf1d@units ="Kg/m2/s"
 Tair1d@units ="K"
 UREF1d@units ="m"
 Wind1d@units ="m/s"
 Wind_DIR1d@units ="deg"
 ZREF1d@units ="m"
 ZS1d@units ="m"

 
 copy_VarCoords(Tair1d,Qair1d)
 copy_VarCoords(Tair1d,PSurf1d)
 copy_VarCoords(Tair1d,Rainf1d)
 copy_VarCoords(Tair1d,Snowf1d)
 copy_VarCoords(Tair1d,Wind1d)
 copy_VarCoords(Tair1d,Wind_DIR1d)
 copy_VarCoords(Tair1d,LWdown1d)
 copy_VarCoords(Tair1d,DIR_SWdown1d)
 copy_VarCoords(Tair1d,SCA_SWdown1d)
 copy_VarCoords(Tair1d,CO2air1d)
 
 timef!0 = "time"
 
 Tair1d&time = timef
 Qair1d&time = timef
 PSurf1d&time = timef
 Rainf1d&time = timef
 Snowf1d&time = timef
 Wind1d&time = timef
 Wind_DIR1d&time = timef
 LWdown1d&time = timef
 DIR_SWdown1d&time = timef
 SCA_SWdown1d&time = timef
 CO2air1d&time = timef
  
 
 outfile_name = "FORCING_1d_full.nc"
 system(" 'rm' -f " + outfile_name)             ; removes the existing file.
 fout  = addfile(outfile_name, "c")             ; create a new netCDF file.
 ;filedimdef(fout,"time",-1,True)             ; make time record dimension
 
 
 ;fout->time=timef
 fout->FRC_TIME_STP=FORC_TIME_STEP
 fout->ZREF=ZREF1d
 fout->ZS=ZS1d
 fout->UREF=UREF1d
 fout->Tair=Tair1d
 fout->Qair=Qair1d
 fout->PSurf=PSurf1d
 fout->Rainf=Rainf1d
 fout->Snowf=Snowf1d
 fout->Wind=Wind1d
 fout->Wind_DIR=Wind_DIR1d
 fout->LWdown=LWdown1d
 fout->DIR_SWdown=DIR_SWdown1d
 fout->SCA_SWdown=SCA_SWdown1d
 fout->CO2air=CO2air1d
 fout->LON=LON1d
 fout->LAT=LAT1d
