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
    DIR_SWdown = fin->SWNORM
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


  SCA_SWdown = DIR_SWdown

  SCA_SWdown = (/DIR_SWdown * 0.15 /)
  
  
  CO2air = Snowf
  CO2air = 0.0

  
;.................... Final..........

 timef = cd_convert(time,"minutes since 2015-01-01 00:00:00")
 FORC_TIME_STEP =  60.0
 ZREF    = 2.0
 UREF    = 10.0
 
 FORC_TIME_STEP!0 = "con"
 ZREF!0 = "con"
 UREF!0 = "con"
 
 LON!0 = "yy"
 LON!1 = "xx"
 
 printVarSummary(LON)
 copy_VarCoords(LON,LAT)
 copy_VarCoords(LON,ZS)

 
 Tair!0 = "time"
 Tair!1 = "yy"
 Tair!2 = "xx"
 
 copy_VarCoords(Tair,Qair)
 copy_VarCoords(Tair,PSurf)
 copy_VarCoords(Tair,Rainf)
 copy_VarCoords(Tair,Snowf)
 copy_VarCoords(Tair,Wind)
 copy_VarCoords(Tair,Wind_DIR)
 copy_VarCoords(Tair,LWdown)
 copy_VarCoords(Tair,DIR_SWdown)
 copy_VarCoords(Tair,SCA_SWdown)
 copy_VarCoords(Tair,CO2air)
 
 timef!0 = "time"
 
 Tair&time = timef
 Qair&time = timef
 PSurf&time = timef
 Rainf&time = timef
 Snowf&time = timef
 Wind&time = timef
 Wind_DIR&time = timef
 LWdown&time = timef
 DIR_SWdown&time = timef
 SCA_SWdown&time = timef
 CO2air&time = timef
  
 
 outfile_name = "FORCING.nc"
 system(" 'rm' -f " + outfile_name)             ; removes the existing file.
 fout  = addfile(outfile_name, "c")             ; create a new netCDF file.
 filedimdef(fout,"time",-1,True)             ; make time record dimension
 
 
 fout->time=timef
 fout->FORC_TIME_STEP=FORC_TIME_STEP
 fout->ZREF=ZREF
 fout->UREF=UREF
 fout->Tair=Tair
 fout->Qair=Qair
 fout->PSurf=PSurf
 fout->Rainf=Rainf
 fout->Snowf=Snowf
 fout->Wind=Wind
 fout->Wind_DIR=Wind_DIR
 fout->LWdown=LWdown
 fout->DIR_SWdown=DIR_SWdown
 fout->SCA_SWdown=SCA_SWdown
 fout->CO2air=CO2air
 
 ;net shortwave radiation (W/m^2) =  {direct shortwave radiation (W/m^2) + diffused shortwave radiation (W/m^2)} (1 - surface albedo)
  
 ;ymd   = ut_calendar(time, -5)           ; -5 = type integer in yrs,mns,dys and hrs
 ;yrs   = ymd(:,0)
 ;mns   = ymd(:,1)
 ;dys   = ymd(:,2)
 ;hrs   = ymd(:,3)

 ;sind  = ind(yrs .eq. cyear .and. mns .eq. cmon .and. dys .eq. fstdy .and. hrs .eq. 6)    ; index of      01-month  06:00
 ;eind  = ind(yrs .eq. cyear .and. mns .eq. cmon .and. dys .eq. lstdy .and. hrs .eq. 18)   ; index of lastday-month  23:00

 ;tarray = ispan(sind,eind,1)
 ;ntim   = dimsizes(tarray)

 ;ntime               = (greg2jul(yrs,mns,dys,hrs) * 24.00 ) - base_julian
 ;itime0               = doubletoint(ntime(sind:eind))
 ;itime0@units         = "hours since 1950-01-01 00:00:00"
 ;itime0@calendar      = "standard"
 ;itime0@long_name     = "time"
 ;itime0@standard_name = "time"
 ;itime0!0             = "time"
 ;itime0&time          = itime0
 
 ;delete_VarAtts(invar,(/"MemoryOrder","FieldType"/))
 ;invar  = sqrt(ucomp^2+vcomp^2)
 ;copy_VarCoords(ucomp,invar)
 ;tmpvar(nt,:,:) = (/ wrf_user_getvar(fin,vnamesi(nv),tarray(nt)) /)
 
;"time"             "time"
;"FRC_TIME_STP"     "Forcing_Time_Step"
;"ZREF"             "Reference_Height"
;"UREF"             "Reference_Height_for_Wind"


;"LON"              "Longitude"
;"LAT"              "Latitude"
;"ZS"               "Surface_Orography"
;"PSurf"            "Surface_Pressure"                                            
;"Tair"             "Near_Surface_Air_Temperature"
;"Qair"             "Near_Surface_Specific_Humidity"                               

;"DIR_SWdown"       "Surface_Indicent_Direct_Shortwave_Radiation" 
;"SCA_SWdown"       "Surface_Incident_Diffuse_Shortwave_Radiation"
;"LWdown"           "Surface_Incident_Longwave_Radiation" 
;"Rainf"            "Rainfall_Rate"                       
;"Snowf"            "Snowfall_Rate"                       
;"Wind"             "Wind_Speed"                          
;"Wind_DIR"         "Wind_Direction"                  
;"CO2air"           "Near_Surface_CO2_Concentration"    


