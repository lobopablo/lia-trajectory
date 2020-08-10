#%% Script information
# Name: simulation.py
# Authors: Trajectory Team (Matias Pellegrini, Pablo Lobo)
# Owner: LIA Aerospace
# Date: July 2020
#
#%% Script description
#
# This is the simulation itself.
#
#%% Packages
#
import numpy as np
import matplotlib.pylab as plt
import c
#
#%% Initial Conditions
# Atmospheric properties
atm_temp = [c.atm_temp0]
atm_p = [c.atm_p0]
atm_rho = [c.atm_rho0]
# 
# Launch vehicle 
tita = 85                                # [deg] - Initial angle 
tita = (tita*np.pi)/180;                 # [rad] - Initial angle
m = [c.me+c.mprop]                       # [kg] - Total mass
# Dynamic parameters
dx = [0]                                 # [N] - Drag x-axis
dy = [0]                                 # [N] - Drag y-axis
thrustx = [c.thrust0*np.cos(tita)]       # [N] - Thrust x-axis
thrusty = [c.thrust0*np.sin(tita)]       # [N] - Thrust y-axis
# Kinematic parameters
t = [0]                                  # [s] - Initial time 
x = [0]                                  # [m] - Initial position x-axis
y = [0]                                  # [m] - Initial position y-axis
vx = [0]                                 # [m/s] - Initial velocity x-axis
vy = [0]                                 # [m/s] - Initial velocity y-axis
ax = [((thrustx[0]-dx[0])/m[0])]         # [m/s^2] - Initial acceleration x-axis
ay = [((thrusty[0]-dy[0])/m[0])-c.atm_g] # [m/s^2] - Initial acceleration y-axis

# Simulation characteristics
dt = 0.25                                # [s] - Time step
ct = 0                                   # [adim] - Step count
tmax = 130                               # [s] - Finish time
#
#%% Simulation
#
while (t[ct] <= tmax):
    # Kinematic parameters
    t.append(t[ct]+dt)
    x.append(x[ct]+vx[ct]*dt+((0.5*ax[ct])*(dt**2)))
    y.append(y[ct]+vy[ct]*dt+((0.5*ay[ct])*(dt**2)))
    vx.append(vx[ct]+dt*ax[ct])
    vy.append(vy[ct]+dt*ay[ct])
    tita=np.arctan(vy[ct+1]/vx[ct+1])
    
    # Atmospheric parameters
    atm_temp.append(c.atm_temp0-(y[ct+1]*c.atm_l))
    atm_p_aux1 = (c.atm_l*y[ct+1])/c.atm_temp0
    atm_p_aux2 = (c.atm_g*c.atm_m)/(c.atm_r*c.atm_l)
    atm_p.append(c.atm_p0*((1-atm_p_aux1)**atm_p_aux2))
    atm_rho.append((atm_p[ct+1]*c.atm_m)/(c.atm_r*atm_temp[ct+1]))
    
    # Drag
    dx.append(0.5*atm_rho[ct+1]*(vx[ct+1]**2)*c.cd*c.aref)
    dy.append(0.5*atm_rho[ct+1]*(vy[ct+1]**2)*c.cd*c.aref)
    
    if (t[ct] <= c.dt_burn): # Burning stage
        m.append(m[ct]-((c.mprop/c.dt_burn)*dt))
        
        thrustx.append((thrustx[ct]+(c.Ae*(c.Pe-atm_p[ct]))))
        thrusty.append((thrusty[ct]+(c.Ae*(c.Pe-atm_p[ct]))))
                
        ax.append((thrustx[ct+1]/m[ct+1])-(dx[ct+1]/m[ct+1]))
        ay.append((thrusty[ct+1]/m[ct+1])-c.atm_g-(dy[ct+1]/m[ct+1]))
        
        ct = ct+1
        
    else: # After engine shut down
        m.append(m[ct])
    
        thrustx.append(0)
        thrusty.append(0)
        
        ax.append(-(dx[ct+1]/m[ct+1]))
        
        if (vy[ct] >= 0):
            ay.append(-c.atm_g-(dy[ct+1]/m[ct+1]))
        else:
            ay.append(-c.atm_g+(dy[ct+1]/m[ct+1]))
            
        if(y[ct]<=0):
            break
                      
        ct = ct+1
#
#%% Plotting
#
fig, axs = plt.subplots(1,3,figsize=(15, 4));
axs[0].plot(t, y);
axs[0].set_ylabel('h(m)');
axs[0].set_xlabel('t(s)');
axs[1].plot(t, vy);
axs[1].set_ylabel('vy(m/s)');
axs[1].set_xlabel('t(s)');
axs[2].plot(t, ay);
axs[2].set_ylabel('ay(m/s2)')
axs[2].set_xlabel('t(s)');
plt.show()
#
fig, axs2 = plt.subplots(1,3,figsize=(15, 4));
axs2[0].plot(x, y);
axs2[0].set_ylabel('h(m)');
axs2[0].set_xlabel('x(m)');
axs2[1].plot(t, vx);
axs2[1].set_ylabel('vx(m/s)');
axs2[1].set_xlabel('t(s)');
axs2[2].plot(t, ax);
axs2[2].set_ylabel('ax(m/s2)')
axs2[2].set_xlabel('t(s)');
plt.show()
#
fig, axs3 = plt.subplots(1,3,figsize=(15, 4));
axs3[0].plot(t, m);
axs3[0].set_ylabel('m(kg)');
axs3[0].set_xlabel('t(s)');
axs3[1].plot(t, thrusty);
axs3[1].set_ylabel('T(N)');
axs3[1].set_xlabel('t(s)');
axs3[2].plot(t, dy);
axs3[2].set_ylabel('dy(N)')
axs3[2].set_xlabel('t(s)');
plt.show()