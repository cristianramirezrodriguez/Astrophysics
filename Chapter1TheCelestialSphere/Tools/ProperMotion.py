"""
Given initial declination (in degrees) and right ascension (in degrees),
and final declination and right ascension:

This script will allow you to find the angular distance traveled by the celestial object.

If you have the time elapsed between measurements the script will also allow you to find the proper motion.
"""

import numpy as np

# Function to find change in right ascension
def rachange(initra, finra):
    delra = finra - initra
    return delra

# Function to find change in declination
def dchange(initdec, findec):
    deld = findec - initdec
    return deld

# Function to find angular distance
def thetachange(initra, finra, initdec, findec):
    deltheta = np.sqrt((rachange(initra, finra) * np.cos(np.radians(initdec)))**2 + (dchange(initdec, findec))**2)
    return deltheta

# Function to find proper motion
def propermotion(initra, finra, initdec, findec, time):
    mu = thetachange(initra, finra, initdec, findec) / time
    return mu

def main():
    print("Given initial and final declinations and right ascensions, this script will find the angular distance traveled by the celestial object.")
    print("If you have the time elapsed between measurements, the script will also calculate the proper motion.")

    initra = float(input("Enter the initial right ascension (in degrees): "))
    initdec = float(input("Enter the initial declination (in degrees): "))
    finra = float(input("Enter the final right ascension (in degrees): "))
    findec = float(input("Enter the final declination (in degrees): "))
    
    deltheta = thetachange(initra, finra, initdec, findec)
    print(f"The angular distance traveled by the celestial object is {deltheta:.6f} degrees.")
    
    time_elapsed = input("Enter the time elapsed between measurements (in years), or press Enter to skip: ")
    if time_elapsed:
        time_elapsed = float(time_elapsed)
        mu = propermotion(initra, finra, initdec, findec, time_elapsed)
        print(f"The proper motion of the celestial object is {mu:.6f} degrees per year.")

if __name__ == "__main__":
    main()

