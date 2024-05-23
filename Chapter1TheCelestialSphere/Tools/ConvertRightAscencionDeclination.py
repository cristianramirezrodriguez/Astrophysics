

#Function to convert a right ascension angle in degrees to time cooridnates 
def deg_to_hms(angle):
    deg = float(angle)
    hours = int(angle // 15)
    minutes = int((deg % 15) * 4)
    seconds = (deg % (1/4)) * 240
    return hours, minutes, seconds

#Function to convert to a right ascension angle in degrees
def hms_to_deg(hours, minutes, seconds):
    h = float(hours)
    m = float(minutes)
    s = float(seconds)
    angle = (h * 15) + (m * 15 / 60) + (s * 15 / 3600)
    return angle

#Function to convert declination from degrees to standard form
#e.g. 20.5125 degrees would become +20 deg 30' 45"
def deg_to_dms(angle):
    deg = float(angle)
    degrees = int(deg)
    arcminutes = int((deg - degrees) * 60)
    arcseconds = (deg - degrees - arcminutes / 60) * 3600
    return degrees, arcminutes, arcseconds

#Function to convert declination from standard form to degree
#e.g. 20.5125 degrees would become +20 deg 30' 45"
def dms_to_deg(degrees, arcminutes, arcseconds):
    deg = float(degrees)
    am = float(arcminutes)
    ars = float(arcseconds)
    angle = degrees + arcminutes / 60 + arcseconds / 3600
    return angle

def main():
    print("Choose conversion type:")
    print("1. Right Ascension (RA)")
    print("2. Declination (Dec)")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        print("Choose RA conversion type:")
        print("1. Degrees to Hours, Minutes, Seconds")
        print("2. Hours, Minutes, Seconds to Degrees")
        ra_choice = input("Enter 1 or 2: ")

        if ra_choice == '1':
            deg = float(input("Enter RA in degrees: "))
            hours, minutes, seconds = deg_to_hms(deg)
            print(f"{deg} degrees is {hours}h {minutes}m {seconds:.2f}s")
        elif ra_choice == '2':
            hours = int(input("Enter hours: "))
            minutes = int(input("Enter minutes: "))
            seconds = float(input("Enter seconds: "))
            deg = hms_to_deg(hours, minutes, seconds)
            print(f"{hours}h {minutes}m {seconds:.2f}s is {deg:.6f} degrees")
        else:
            print("Invalid choice.")

    elif choice == '2':
        print("Choose Dec conversion type:")
        print("1. Degrees to Degrees, Arcminutes, Arcseconds")
        print("2. Degrees, Arcminutes, Arcseconds to Degrees")
        dec_choice = input("Enter 1 or 2: ")

        if dec_choice == '1':
            deg = float(input("Enter Dec in degrees: "))
            degrees, arcminutes, arcseconds = deg_to_dms(deg)
            print(f"{deg} degrees is {degrees}° {arcminutes}' {arcseconds:.2f}\"")
        elif dec_choice == '2':
            degrees = int(input("Enter degrees: "))
            arcminutes = int(input("Enter arcminutes: "))
            arcseconds = float(input("Enter arcseconds: "))
            deg = dms_to_deg(degrees, arcminutes, arcseconds)
            print(f"{degrees}° {arcminutes}' {arcseconds:.2f}\" is {deg:.6f} degrees")
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
