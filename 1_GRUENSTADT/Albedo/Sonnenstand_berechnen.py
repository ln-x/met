from __future__ import division
from math import pow, sqrt, sin, log, atan, sin, cos, pi, tan, acos, exp,radians, degrees, log10
from random import randint
from bisect import bisect

__author__ = 'hpl/lnx'


def CalcSolarPosition(lat, lon, hour, min, sec, offset, JDC):
    toRadians = pi/180.0
    toDegrees = 180.0/pi
    MeanObliquity = 23.0 + (26.0 + ((21.448 - JDC * (46.815 + JDC * (0.00059 - JDC * 0.001813))) / 60.0)) / 60.0
    Obliquity = MeanObliquity + 0.00256 * cos(toRadians*(125.04 - 1934.136 * JDC))
    Eccentricity = 0.016708634 - JDC * (0.000042037 + 0.0000001267 * JDC)
    GeoMeanLongSun = 280.46646 + JDC * (36000.76983 + 0.0003032 * JDC)

    while GeoMeanLongSun < 0:
        GeoMeanLongSun += 360
    while GeoMeanLongSun > 360:
        GeoMeanLongSun -= 360
    GeoMeanAnomalySun = 357.52911 + JDC * (35999.05029 - 0.0001537 * JDC)

    Dummy1 = toRadians*GeoMeanAnomalySun
    Dummy2 = sin(Dummy1)
    Dummy3 = sin(Dummy2 * 2)
    Dummy4 = sin(Dummy3 * 3)
    SunEqofCenter = Dummy2 * (1.914602 - JDC * (0.004817 + 0.000014 * JDC)) + Dummy3 * (0.019993 - 0.000101 * JDC) + Dummy4 * 0.000289
    SunApparentLong = (GeoMeanLongSun + SunEqofCenter) - 0.00569 - 0.00478 * sin(toRadians*((125.04 - 1934.136 * JDC)))

    Dummy1 = sin(toRadians*Obliquity) * sin(toRadians*SunApparentLong)
    Declination = toDegrees*(atan(Dummy1 / sqrt(-Dummy1 * Dummy1 + 1)))

    SunRadVector = (1.000001018 * (1 - pow(Eccentricity,2))) / (1 + Eccentricity * cos(toRadians*(GeoMeanAnomalySun + SunEqofCenter)))

    #======================================================
    #Equation of time (minutes)
    Dummy = pow((tan(Obliquity * pi / 360)),2)
    Dummy1 = sin(toRadians*(2 * GeoMeanLongSun))
    Dummy2 = sin(toRadians*(GeoMeanAnomalySun))
    Dummy3 = cos(toRadians*(2 * GeoMeanLongSun))
    Dummy4 = sin(toRadians*(4 * GeoMeanLongSun))
    Dummy5 = sin(toRadians*(2 * GeoMeanAnomalySun))
    Et = toDegrees*(4 * (Dummy * Dummy1 - 2 * Eccentricity * Dummy2 + 4 * Eccentricity * Dummy * Dummy2 * Dummy3 - 0.5 * pow(Dummy,2) * Dummy4 - 1.25 * pow(Eccentricity,2) * Dummy5))

    SolarTime = (hour*60.0) + min + (sec/60.0) + (Et - 4.0 * -lon + (offset*60.0))

    while SolarTime > 1440.0:
        SolarTime -= 1440.0
    HourAngle = SolarTime / 4.0 - 180.0
    if HourAngle < -180.0:
        HourAngle += 360.0

    Dummy = sin(toRadians*lat) * sin(toRadians*Declination) + cos(toRadians*lat) * cos(toRadians*Declination) * cos(toRadians*HourAngle)
    if Dummy > 1.0:
        Dummy = 1.0
    elif Dummy < -1.0:
        Dummy = -1.0

    Zenith = toDegrees*(acos(Dummy))
    Dummy = cos(toRadians*lat) * sin(toRadians*Zenith)
    if abs(Dummy) >= 0.000999:
        Azimuth = (sin(toRadians*lat) * cos(toRadians*Zenith) - sin(toRadians*Declination)) / Dummy
        if abs(Azimuth) > 1.0:
            if Azimuth < 0:
                Azimuth = -1.0
            else:
                Azimuth = 1.0

        Azimuth = 180 - toDegrees*(acos(Azimuth))
        if HourAngle > 0:
            Azimuth *= -1.0
    else:
        if lat > 0:
            Azimuth = 180.0
        else:
            Azimuth = 0.0
    if Azimuth < 0:
        Azimuth += 360.0

    AtmElevation = 90 - Zenith
    if AtmElevation > 85:
        RefractionCorrection = 0
    else:
        Dummy = tan(toRadians*(AtmElevation))
        if AtmElevation > 5:
            RefractionCorrection = 58.1 / Dummy - 0.07 / pow(Dummy,3) + 0.000086 / pow(Dummy,5)
        elif AtmElevation > -0.575:
            RefractionCorrection = 1735 + AtmElevation * (-518.2 + AtmElevation * (103.4 + AtmElevation * (-12.79 + AtmElevation * 0.711)))
        else:
            RefractionCorrection = -20.774 / Dummy
        RefractionCorrection = RefractionCorrection / 3600

    Zenith = Zenith - RefractionCorrection
    Altitude = 90 - Zenith
    Daytime = 0
    if Altitude > 0.0:
            Daytime = 1

    dir = bisect((0.0,67.5,112.5,157.5,202.5,247.5,292.5),Azimuth)-1

    return Altitude, Zenith, Daytime, dir


if __name__ == "__main__":
    print CalcSolarPosition(47, 16, 10, 0, 0, 0, 15)
    Altitude, Zenith, Daytime, dir = CalcSolarPosition(47, 16, 10, 0, 0, 0, 150)
    print Altitude, Zenith, Daytime, dir
