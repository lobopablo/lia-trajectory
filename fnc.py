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
    return thrust

#%% Coordinate Systems

# This block implements the different functions required to transform
# the different tensors from one coordinate system to another.
# Source: Zipfel.

def Tge(long,lat):
    # The aim of this function is to calculate the transformation matrix 
    # between the geographical and Earth coordinate systems. 
    # Zipfel (3.13)
    # === INPUTS ===
    # long [rad]              longitude
    # lat [rad]               Latitude
    # === OUTPUTS ===
    # tge [3x3 mat]           T_GE
    # Create the basic values
    slon = np.sin(long)
    clon = np.cos(long)
    slat = np.sin(lat)
    clat = np.cos(lat)
    # Create 9 positions
    ind11 = -slat*clon; 
    ind12 = -slat*slon
    ind13 = clat
    ind21 = -slon
    ind22 = clat
    ind23 = 0
    ind31 = -clat*clon
    ind32 = -clat*slon
    ind33 = -slon
    # Create the matrix itself
    tge = np.array([[ind11, ind12, ind13],[ind21, ind22, ind23],[ind31, ind32, ind33]])  
    return tge

def Tmv(bang):
    # The aim of this function is to calculate the transformation matrix 
    # between the load factor and velocity coordinate systems. 
    # Zipfel (8.22)
    # === INPUTS ===
    # bang [rad]              Bank Angle
    # === OUTPUTS ===
    # tmv [3x3 mat]           T_MV
    # Create the basic values
    sba = np.sin(bang)
    cba = np.cos(bang)
    # Create 9 positions
    ind11 = 1 
    ind12 = 0
    ind13 = 0
    ind21 = 0
    ind22 = -cba
    ind23 = sba
    ind31 = 0
    ind32 = -sba
    ind33 = cba
    # Create the matrix itself
    tmv = np.array([[ind11, ind12, ind13],[ind21, ind22, ind23],[ind31, ind32, ind33]])  
    return tmv

def Tvg(gamma,chi):
    # The aim of this function is to calculate the transformation matrix 
    # between the flight path and geographic coordinate systems. 
    # Zipfel (3.25)
    # === INPUTS ===
    # gamma [rad]              Heading Angle
    # chi [rad]                Flight Path Angle
    # === OUTPUTS ===
    # tvg [3x3 mat]            T_VG
    # Create the basic values
    schi = np.sin(chi)
    cchi = np.cos(chi)
    sgamma = np.sin(gamma)
    cgamma = np.cos(gamma)
    # Create 9 positions
    ind11 = cchi*cgamma 
    ind12 = cgamma*schi
    ind13 = -sgamma
    ind21 = -schi
    ind22 = -cchi
    ind23 = 0
    ind31 = sgamma*cchi
    ind32 = sgamma*schi
    ind33 = cchi
    # Create the matrix itself
    tvg = np.array([[ind11, ind12, ind13],[ind21, ind22, ind23],[ind31, ind32, ind33]])  
    return tvg

def JD(yr,mo,d,h,min,s):
    # The aim of this function is to calculate the Julian Date 
    # Source: Vallado, Algorithm #14
    # Unless specified, JD usually implies a time based on UT1
    # Equation valid from years 1900 to 2100
    # === INPUTS ===
    # yr [adim]                Year of interest
    # mo [adim]                Month of interest (1 to 12)
    # d [adim]                 Day of interest (1 to 31)
    # h [adim]                 Hour of interest (0 to 23)
    # min [adim]               Min of interest (0 to 59)
    # s [adim]                 Seconds of interest (0 to 59)
    # === OUTPUTS ===
    # jdate [adim]             Julian Date
    # Function
    jdate = 367*yr - int((7*(yr+int((mo+9)/12)))/4) + int((275*mo)/9) + d + 1721013.5 + ((((s/60)+min)/60) + h)/24
    return jdate

def jd2tjd(jdate):
    # The aim of this function is to calculate the number of Julian centuries 
    # elapsed from the epoch J2000.0. 
    # Source: Vallado, Eq. (3.42)
    # Equation valid for epoch J2000.0, see p.183 for other epochs
    # === INPUTS ===
    # jdate [julian date]     Julian date, as provided by function JD
    # === OUTPUTS ===
    # Function
    # tjdate [centuries]      Julian centuries elapsed since J2000.0 epoch
    tjdate = (jdate - 2451545)/36525
    return tjdate

def tjd2gmst(tjdate):
    # The aim of this function is to calculate the Greenwich Mean Sidereal Time
    # given the number of Julian centuries elapsed from the epoch J2000.0.
    # Source: Vallado, Eq. (3.47)
    # === INPUTS ===
    # tjdate [centuries]      Julian centuries elapsed since J2000.0 epoch
    # === OUTPUTS ===
    # gmst_s [s]              GMST in seconds
    # gmst_d [°]              GMST in degrees
    # Function
    gmst_s = 67310.54841 + (876600*3600 + 8640184.812866)*tjdate + 0.093104*tjdate**2 - 6.2*10**-6* (tjdate**3)
    # Reduce this quantity to a result within the range of 86400s
    secs_day = 86400
    gmst_aux = gmst_s % secs_day
    # Convert to degrees
    gmst_d = gmst_aux / 240
    # Convert to an angle in the 0-360 range
    if gmst_d < 0:
        gmst_d += 360   
    return gmst_s, gmst_d

def date_now():
    # The aim of this function is to return the date at time of invoking it.
    # === INPUTS ===
    # 
    # === OUTPUTS ===
    # date_out [datetime]        Date at time of function invoking
    # Function
    from datetime import datetime
    date = datetime.now()
    return date

def date_parts(date_in):
    # The aim of this function is to return the different values stored in the 
    # input datetime value.
    # === INPUTS ===
    # date_in [datetime]       Input date
    # === OUTPUTS ===
    # yr [int]                 Year on input date
    # m [int]                  Month on input date
    # d [int]                  Day on input date
    # h [int]                  Hour on input date
    # m [int]                  Minute on input date
    # s [int]                  Second on input date
    yr = date_in.year
    mo = date_in.month
    d = date_in.day
    h = date_in.hour
    m = date_in.minute
    s = date_in.second
    return yr, mo, d, h, m, s