#%% Script information
# Name: c.py
# Authors: Trajectory Team (Matias Pellegrini, Pablo Lobo)
# Owner: LIA Aerospace
# Date: July 2020
#
#%% Script description
#
# The aim of this module is defining constants for the simulation.
#
#%% Packages
import numpy as np
#
#%% Atmospheric Properties
#
atm_temp0 = 288.15      # [K] - Temperature @ SL
atm_p0 = 101325         # [Pa] - Pressure @ SL
atm_rho0 = 1.225        # [kg/m^3] - Density @ SL
atm_l = 0.0065          # [K/m] - Temperature lapse rate
atm_r = 8.31447         # [J/(mol*K)] - Ideal Gas Constants
atm_m = 0.0289654       # [kg/mol] - Dry Air Molar Mass
atm_g = 9.81            # [m/s^2] - Gravity @ SL
#
#%% Launch Vehicle Properties
#
me = 43                 # [kg] - Initial Mass
mprop = 22              # [kg] - Propellant Mass
cd = 0.35               # [adim] - Drag Coefficient
aref= np.pi*(0.1**2)    # [m^2] - Reference Area
dt_burn = 10            # [s] - Impulse Time
thrust0 = 5500          # [N] - Initial Thrust @ SL
Ae = 0.0059             # [m^2] - Area               
Pe = 101325             # [Pa] - Exhaust Pressure