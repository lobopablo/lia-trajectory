#%% Script information
# Name: simulation2.py
# Authors: Trajectory Team (Matias Pellegrini, Pablo Lobo)
# Owner: LIA Aerospace
#
#%% Script description
#
# This is the simulation itself.
#
#%% Packages
#
import numpy as np
import matplotlib.pylab as plt
import c as c
import fnc as f
#%% Initial Conditions
#
# Atmospheric properties at Launch Site
Z_0 = 0                                  # [m] - Initial altitude over SL
b, Lmb, Tmb, Hb, Hz, Pb = f.table4(Z_0)    
T = f.tm(Tmb,Lmb,Hz,Hb)                  # [K] - Initial Temperature
P = f.p(Tmb,Lmb,Hz,Hb,Pb)                # [N/m^2] - Initial Pressure
rho = f.rho(P,T)                         # [kg/m^3] - Initial Density
Vs = f.Vs(T)                             # [m/s] - Initial Speed of Sound
dvisc, kvisc = f.visc(T,rho)               
#
# Dynamics
D = [0]                                  # [N] - Drag Force
T = [0]                                  # [N] - Thrust
L = [0]                                  # [N] - Lift Force
m = [c.M_st1_i]                          # [kg] - Initial mass of the vehicle
W = [m[0]*c.g]                           # [m/s^2] - Weight of the vehicle
#
# Kinematics
t = [0]                                  # [s] - Initial time 
x = [0]                                  # [m] - Initial position x-axis
y = [0]                                  # [m] - Initial position y-axis
z = [0]                                  # [m] - Initial position z-axis
vx = [0]                                 # [m/s] - Initial velocity x-axis
vy = [0]                                 # [m/s] - Initial velocity y-axis
vz = [0]
ax = [((thrustx[0]-dx[0])/m[0])]         # [m/s^2] - Initial acceleration x-axis
ay = [((thrusty[0]-dy[0])/m[0])-c.atm_g] # [m/s^2] - Initial acceleration y-axis

# Simulation characteristics
dt = 0.25                                # [s] - Time step
ct = 0                                   # [adim] - Step count
tmax = c.bt_st1 + ct_bt_st2              # [s] - Finish time