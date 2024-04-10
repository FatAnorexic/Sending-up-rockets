'''
This file is a simple script that will take several inputs and return the hohmann transfer,
the Δv of the transfer, Δv necessessary to circularize the orbit, Phase angle for the transfer,
and the time for half the period of the transfer.
'''
from scipy.constants import gravitational_constant as G
import astropy as ast
import numpy as np

def period_transfer(a_hoh, mu):
    #Returns the period of hohmann transfer using the Semi major axis(a_hoh) of the initial transfer 
    #and the Standard gravitational constant µ.
    return 2*np.pi*np.sqrt(a_hoh**3/mu)

def phase_angle(t_hoh, t_target):
    #This angle is the "transfer window" for your initial Δv burn. When the two bodies are at this angle
    #A hohmann transfer is possible. ang_vel_target is the angular velocity of the target around the central
    #body. IE: Mars around the Sun; Kennedy Space Center around Earths CM; etcetera.
    return (np.pi-np.pi*t_hoh/t_target)*180/np.pi

def ang_vel_tartget(t_target):
    #This returns(in radians/s) the rate at which the target body is constantly revolving about the 
    #axis of the central body.
    return (2*np.pi)/t_target

def main():
    target=input('Enter the name of the target: ')
    central_body=input('Enter the name of the central body: ')
    m=float(input(f'Enter the mass of {central_body}: '))

    #Standard Gravitational Constant
    mu=G*m

    

if __name__=="__main__":
    main()