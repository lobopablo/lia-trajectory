#%% Script information
# Name: fnc.py
# Authors: Trajectory Team (Matias Pellegrini, Pablo Lobo)
# Owner: LIA Aerospace
#
#%% Script description
#
# The aim of this module is defining functions to be used in the simulation.
#
#%% Packages
import numpy as np
import c as c

#%% Atmospheric properties

# This block implements the US Standard Atmosphere 1976 model.
# As of 24Aug2020, only the 0-76km portion of the model is implemented.

def layer(H: float)->float: 
    # The aim of this function is to define which layer is the vehicle
    # currently flying through (according to Table 4 of the Standard)
    # 
    # === INPUTS ===
    # H [m'] - Geopotential height
    # === OUTPUTS === 
    # b [adim] - Subscript of the layer
    #
    # Input control
    try:
        int(H)
    except ValueError:
        try:
            float(H)
        except ValueError:
            print("Fn: layer. Input must be a number.")
            return
    # Cases
    if H>=0 and H<11000:
        b = 0
    elif H>=11000 and H<20000:    
        b = 1
    elif H>=20000 and H<32000:
        b = 2
    elif H>=32000 and H<47000:
        b = 3
    elif H>=47000 and H<51000:
        b = 4
    elif H>=51000 and H<71000:
        b = 5  
    elif H>=71000 and H<84852:
        b = 6
    elif H==84852:
        b = 7
    else: 
        print('Fn: Layer. H must be a value between 0 and 84852m')
        b = 'Error - Check H'
        return
    return b
        
def table4(Z: float):
    # The aim of this function is to define   the constants provided by 
    # Table 4 given the current geometrical height at which the vehicle is.
    # === INPUTS ===
    # Z [m] - Geometric height
    # === OUTPUTS === 
    # b [adim]      Subscript of the layer
    # Lmb [K/km']   Molecular-scale temperature gradient (Table 4)
    # Tmb [K]       Temperature constant
    # Hb [km']      Geopotential Height of the layer    (Table 4)
    # H [km']       Geopotential Height of the vehicle
    # Pb [N/m^2]    Pressure constant 
    # Input control
    try:
        int(Z)
    except ValueError:
        try:
            float(Z)
        except ValueError:
            print("Fn: table4. Input must be a number.")
            return
    # The layer is defined.
    ro = 6356.766 * 10**3      # [m] - Earth's radius - (Page 4)
    H = (Z*ro) / (ro + Z)      # [m'] - Geopotential height of the vehicle
    b = layer(H)               # [adim] - Subscript of the layer
    # Verifying b
    if b==None:
        print('Fn: table4. Z must be a value between 0m and 85999m.')
        return
    H = H*0.001               # [km'] - Geopotential height of the vehicle
    Hb_vec = np.array([0, 11, 20, 32, 47, 51, 71, 84.852])
    Lmb_vec = np.array([-6.5, 0, 1, 2.8, 0, -2.8, -2, 0])
    Tmb_vec = np.array([288.15, 216.65, 216.65, 228.65, 270.65, 270.65, 214.65, 186.946])
    pb_vec = np.array([101325, 22632.06, 5474.88, 868.01, 110.90, 66.93, 3.95])
    Hb = Hb_vec[b]
    Lmb = Lmb_vec[b]
    Tmb = Tmb_vec[b]
    Pb = pb_vec[b]
    return b, Lmb, Tmb, Hb, H, Pb

def tm(Tmb,Lmb,H,Hb):
    # The aim of this function is to estimate the Tm value according to
    # equation (23) of the US Standard Atmosphere 1976.
    # This function gives the temperature for the range 0-76km.
    # === INPUTS ===
    # Tmb [K]       Temperature constant
    # Lmb [K/km']   Molecular-scale temperature gradient
    # H [km']       Geopotential height of interest
    # Hb [km']      Geopotential Height for the particular layer (Table 4)
    # === OUTPUTS === 
    # Tm [K]     Temperature at given geopotential height H
    Tm = Tmb + Lmb*(H-Hb)     #  [K] - Temperature at given geopotential height H
    return Tm

def p(Tmb,Lmb,H,Hb,Pb):
    # The aim of this function is to estimate the pressure value according to
    # equation (33a 33b) of the US Standard Atmosphere 1976.
    # This function gives the pressure for the range 0-76km.
    # === INPUTS ===
    # Tmb [K]       Temperature constant
    # Lmb [K/km']   Molecular-scale temperature gradient
    # H [km']       Geopotential height of interest
    # Hb [km']      Geopotential Height for the particular layer (Table 4)
    # Pb [N/m^2]    Pressure constant
    # === OUTPUTS === 
    # P [N/m^2]     Pressure at given geopotential height H
    # === CONSTANTS ===
    go = 9.80665                # [m^2/s^2.m] - Gravity @ SL (Page 2)
    R = 8.31432 * 10**3         # [Nm / (kmol.K)] - Gas constant (Page 2)
    Mo = 28.9644                # [kg/kmol] - Mean Molecular Weight - (Page 9)
    if Lmb!=0:
        P = Pb*(Tmb / (Tmb + (Lmb*(H-Hb))))**((go*Mo*1000)/(R*Lmb))
    elif Lmb==0:
        P = Pb*np.exp((-go*Mo*(H-Hb)*1000)/(R*Tmb))
    return P

def rho(P,Tm):
    # The aim of this function is to estimate the density value according to
    # equation (42) of the US Standard Atmosphere 1976.
    # This function provides the density for the range 0-86km.
    # === INPUTS ===
    # Tm [K]           Temperature at given geopotential height H
    # P [N/m^2]        Pressure at given geopotential height H
    # === OUTPUTS === 
    # rho [kg/m^3]     Density at given geopotential height H
    # === CONSTANTS ===
    R = 8.31432 * 10**3        # [Nm / (kmol.K)] - Gas constant (Page 2)
    Mo = 28.9644               # [kg/kmol] - Mean Molecular Weight - (Page 9)
    rho = (P*Mo)/(R*Tm)        # [kg/m^3]  - Density (Eq 42)
    return rho
    
def Vs(Tm):
    # The aim of this function is to estimate the speed of sound value 
    # according to equation (50) of the US Standard Atmosphere 1976.
    # This function provides the speed of sound for the range 0-86km.
    # Applies only when the sound wave is a small perturbation on the 
    # ambient condition.
    # === INPUTS ===
    # Tm [K]          Temperature at given geopotential height H
    # === OUTPUTS === 
    # Vs [m/s]     Speed of sound at given temperature Tm(H)
    # === CONSTANTS ===
    R = 8.31432 * 10**3         # [Nm / (kmol.K)] - Gas constant (Page 2)
    Mo = 28.9644                # [kg/kmol] - Mean Molecular Weight - (Page 9)
    gamma = 1.4                 # [adim] - Ratio of Cp/Cv
    Vs = ((gamma*R*Tm)/Mo)**0.5 # [m/s] - Local speed of sound
    return Vs

def visc(Tm,rho):
    # The aim of this function is to estimate the dynamic and kinematic 
    # viscosity according to equations (51 and 52) of the US 
    # Standard Atmosphere 1976.
    # This function provides the speed of sound for the range 0-86km.
    # According to p10 of this standard, Tm = T for the 0-80km range.
    # From 80 to 86 the difference is very small. 
    # === INPUTS ===
    # Tm [K]          Temperature at given geopotential height H    
    # rho [km/m^3]    Density at given geopotential height H
    # === OUTPUTS === 
    # dvisc [N.s/m^2]              Dynamic Viscosity 
    # kvisc [m^2/s]                Kinematic Viscosity
    # === CONSTANTS ===
    beta = 1.458*10**-6         # [kg/s.m.K^0.5] - "Constant"
    S = 110.4                   # [K] - Sutherland's constant
    dvisc = (beta*Tm**1.5)/(Tm+S) # [N.s/m^2] - Dynamic viscosity
    kvisc = dvisc/rho           # [m^2/s] - Kinematic Viscosity    
    return dvisc, kvisc

def g(Z):
    # The aim of this function is to estimate the acceleration due to gravity
    # for a given geometric height, according to eq (17) of the US Standard
    # Atmosphere 1976.
    # === INPUT ===
    # Z [m]         Geometric height of interest
    # === OUTPUT ===
    # g [m/s^2]     Acceleration due to gravity at given Z
    # === CONSTANTS === (Page 8 of the Standard)
    ro = 6356766    # [m] - Effective radius of the earth at a certain latitude
    go = 9.80665    # [m/s^2] - Sea level value of the acceleration of gravity
    # Input control
    try:
        int(Z)
    except ValueError:
        try:
            float(Z)
        except ValueError:
            print("Fn: g. Input must be a number.")
            return
    if Z<0:
        print('Fn: g. Input must be positive.')
        return
    g = go * (ro / (ro+Z))**2
    return g
#%% Flight

# This block implements the different functions required for the
# simulation.py file to be able to simulate the flight of the launch 
# vehicle. Functions' assumptions and sources are documented in detail
# the Flight (Jupyter Notebook) document.

def mach(V,Vs):
    # The aim of this function is to calculate the local Mach number at the 
    # instant of interest.
    # === INPUTS ===
    # V [m/s]                   Local flow velocity 
    # Vs [m/s]                  Speed of sound in the medium at the local temperature
    # === OUTPUTS ===
    # M [adim]                  Local Mach Number
    M = V/Vs                    # [adim] - Local Mach Number
    return M

def re(V,kvisc,L):
    # The aim of this function is to calculate the local Reynolds number
    # at the instant of interest
    # === INPUTS ===
    # V [m/s]                   Local flow velocity    
    # kvisc [m^2/s]             Kinematic Viscosity
    # L [m]                     Characteristic length
    # === OUTPUTS ===
    # re [adim]                 Local Reynolds Number
    re = V * L / kvisc          # Local Reynolds Number
    return re

def thrust(m_dot,Ve,Pe,Po):
    # The aim of this function is to calculate the generated thrust
    # at the instant of interest. 
    # === INPUTS ===
    # m_dot [kg/s]              Mass flow of propellant being expelled
    # Ve [m/s]                  Exhaust velocity of the gases
    # Pe [N/m^2]                Exhaust pressure
    # Po [N/m^2]                Pressure outside the noZZle
    # === OUTPUTS ===
    # thrust [N]                Thrust
    # === CONSTANTS ===
    # c.Ae [m^2]                NoZZle exit surface
    thrust = m_dot*Ve + (Pe - Po)*c.Ae   