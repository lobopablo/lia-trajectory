#%% Script information
# Name: c.py
# Authors: Trajectory Team (Matias Pellegrini, Pablo Lobo)
# Owner: LIA Aerospace
#
#%% Script description
#
# The aim of this module is defining constants for the simulation.
#
#%% Packages
import numpy as np
#
#%% Launch Vehicle Properties
# Mass
M_st1_i = 5826                       # [kg] - Initial mass, stage #1
M_st1_f = 2026                       # [kg] - Final mass, stage #1 
M_st1_prop = M_st1_i - M_st1_f       # [kg] - Propellant mass, stage #1
M_st2_i = 1560                       # [kg] - Initial mass, stage #2
M_st2_f = 210                        # [kg] - Final mass, stage #2
M_st2_prop = M_st2_i - M_st2_f       # [kg] - Propellant mass, stage #1
M_payload = 75                       # [kg] - Payload mass
#
# Engine performance
Pe_st1 = 200 * 10**5                 # [N/m^2] - Exhaust presure, stage #1
Pe_st2 = 200 * 10**5                 # [N/m^2] - Exhaust pressure, stage #2
ISP_st1_SL = 272                     # [s] - ISP at SL, stage #1
ISP_st1_V = 293                      # [s] - ISP at Vacuum, stage #1
ISP_st2_V = 328                      # [s] - ISP at Vacuum, stage #2
#
# Propellant consumption
bt_st1 = 106                         # [s] - Burning time, stage #1
bt_st2 = 113                         # [s] - Burning time, stage #2
m_dot_st1 = M_st1_prop/bt_st1        # [kg/s] - Mass flow, stage #1
m_dot_st2 = M_st2_prop/bt_st2        # [kg/s] - Mass flow, stage #2
# 
# 


#%% Physical constants
g = 9.81                       # [m/s^2] - Gravity's acceleration



