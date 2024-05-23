'''
Find the synodic period (in days) of two planets given their sidereal periods (in days).
'''

def synodic(inferiorperiod, superiorperiod):
    T_i = float(inferiorperiod)
    T_s = float(superiorperiod)
    S = 1 / (1 / T_i - 1 / T_s)
    return S

def main():
    print("The synodic period is the time between oppositions for two planets orbiting a star.")
    print("Earth's sidereal period is roughly 365 days.")
    
    Ti = float(input("The sidereal period of the inferior planet (days): "))
    Tf = float(input("The sidereal period of the superior planet (days): "))
    
    Ts = synodic(Ti, Tf)
    print("The synodic period is", Ts, "days.")

if __name__ == "__main__":
    main()
