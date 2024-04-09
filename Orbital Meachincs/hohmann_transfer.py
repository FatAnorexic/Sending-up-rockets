'''
This file is a simple script that will take several inputs and return the hohmann transfer,
the Δv of the transfer, Δv necessessary to circularize the orbit, Phase angle for the transfer,
and the time for half the period of the transfer.
'''
from scipy.constants import gravitational_constant as G
import astropy as ast
import numpy as np

def period_transfer(a_hoh, mu):
    return 2*np.pi*np.sqrt(a_hoh**3/mu)

def phase_angle(t_hoh, ang_vel_target):
    return 180-0.5*t_hoh*ang_vel_target


def main():
    target=input('Enter the name of the target: ')
    m=float(input(f'Enter the mass of {target}: '))
    mu=G*m

    

if __name__=="__main__":
    main()