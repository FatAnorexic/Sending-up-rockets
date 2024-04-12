'''
This file is a simple script that will take several inputs and return the hohmann transfer,
the Δv of the transfer, Δv necessessary to circularize the orbit, Phase angle for the transfer,
and the time for half the period of the transfer.
'''
from scipy.constants import gravitational_constant as G
import astropy as ast
import numpy as np
import csv

target=input('Enter the name of the target: ')
depart=input("Enter the name of the body you're departing from: ")
central_body=input('Enter the name of the central body: ')

def sma_hohmann(a_target, a_departure):
    #Takes the SMA of both the departure body and the target body, relative to the central mass in the 
    #system and returns the sma of the transfer orbit| or the sma of the hohmann transfer
    return (a_target+a_departure)/2

def period(a, mu):
    #returns the period of a given quantity to the central mass of the system. 
    return 2*np.pi*np.sqrt(a**3/mu)

def phase_angle(t_hoh, t_target):
    #This angle is the "transfer window" for your initial Δv burn. When the two bodies are at this angle
    #A hohmann transfer is possible. ang_vel_target is the angular velocity of the target around the central
    #body. IE: Mars around the Sun; Kennedy Space Center around Earths CM; etcetera.
    return (np.pi-np.pi*t_hoh/t_target)*180/np.pi

def ang_vel(t):
    #returns the angular velocity of an object based on the period of that object. 
    return (2*np.pi)/t


def main():
    
    #Get the mass of the central body of the system we are calculating for
    m=float(input(f'\nEnter the mass of {central_body}: '))

    #Get the radius of the target body from the central body in the system| for a perfectly circular orbit we only need the 
    #radius r(assuming the center of mass of the major body does not shift) However for any elliptical orbit we need the 
    #semi-major axis
    a_target=float(input(f'\nEnter the semi-major axis in meters of {target} from {central_body}: '))
    
    #Get the semi-major axis of the departing body in comparison to the central body of the system. IE Earth to Mars|
    #return the SMA of Earth in comparison to the sun. 
    a_departing=float(input(f'\nEnter the SMA of {depart} in relation to {central_body}: '))

    #Standard Gravitational Constant
    mu=G*m
    testing=test(a_target, a_departing, mu)
    csv_write(testing)
    

def test(a_t, a_d, mu):
    print(f'\nStandard Gravitational Constant: {mu:.3e} m**3/s**2\n')
    t_target=period(a_t, mu) 
    t_depart=period(a_d, mu)
    t_hoh=period(sma_hohmann(a_t,a_d), mu)
    print(f'Perioid of {target}: {t_target:.0f} s')
    print(f'period of {depart}: {t_depart:.0f} s')
    print(f'period of hohmann transfer: {t_hoh:.0f} s\n')
    return phase_angle(t_hoh, t_target)

def csv_write(param):
    file=open("test.txt", 'w')
    file.write(f'Phase Angle: {param:.2f}')
    file.close
        

if __name__=="__main__":
    main()