"""
This script finds the change in right ascension and declination of a celestial body from J2000.0 (January 1st, 2000),
to today given the current right ascension and declination.
"""

from datetime import datetime, timedelta
import math as m

def get_fractional_year(date):
    year = date.year
    start_of_year = datetime(year, 1, 1, 0, 0, 0)
    end_of_year = datetime(year + 1, 1, 1, 0, 0, 0)
    year_length = (end_of_year - start_of_year).total_seconds()
    elapsed_time = (date - start_of_year).total_seconds()
    fractional_year = year + (elapsed_time / year_length)
    return fractional_year

current_utc_time = datetime.utcnow()
fractional_year = get_fractional_year(current_utc_time)

def deltaalpha(ascension, declination, t=fractional_year):
    T = (t - 2000.0) / 100.0
    M = 1.2812323 * T + 0.0003879 * T**2 + 0.0000101 * T**3
    N = 0.5567530 * T - 0.0001185 * T**2 - 0.0000116 * T**3
    ascension_rad = m.radians(ascension)
    declination_rad = m.radians(declination)
    achange = M + N * m.sin(ascension_rad) * m.tan(declination_rad)
    return achange

def deltad(ascension, t=fractional_year):
    T = (t - 2000.0) / 100.0
    N = 0.5567530 * T - 0.0001185 * T**2 - 0.0000116 * T**3
    ascension_rad = m.radians(ascension)
    dchange = N * m.cos(ascension_rad)
    return dchange

def main():
    ra = float(input("What is the current right ascension of the celestial body in degrees? "))
    dec = float(input("What is the current declination of the celestial body in degrees? "))
    
    rachange = deltaalpha(ra, dec)
    decchange = deltad(ra)
    
    oldra = ra - rachange
    olddec = dec - decchange
    
    print("Since J2000.0 the right ascension has changed by", rachange, "degrees.")
    print("Since J2000.0 the declination has changed by", decchange, "degrees.")
    print("On January 1st, 2000, the object was at a right ascension of", oldra, "and a declination of", olddec)

if __name__ == "__main__":
    main()
