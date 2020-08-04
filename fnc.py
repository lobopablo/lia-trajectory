#%% Script information
# Name: fnc.py
# Authors: Trajectory Team (Matias Pellegrini, Pablo Lobo)
# Owner: LIA Aerospace
# Date: August 2020
#
#%% Script description
#
# The aim of this module is defining functions to be used in the simulation.
#
#%% Packages

#%% Multival

def multival(z: float)->float: 
    ## The aim of this function is to provide the information presented in 
    # table 4 of the US Standard Atmosphere 1976
    # I&O
    # === INPUTS ===
    # z [m] - Geometric height
    # === OUTPUTS === 
    # b [adim] - Subscript
    # L [K/km'] - Molecular-scale temperature gradient
    # Hb [m'] - Geopotential Height
    # Function
    ro = 6356.766*10**3         # [m] - Earth's Radius (Page 4)
    Hb = (z*ro)/(ro+z)          # [m] - Geopotential height
    # Cases
    if Hb>=0 and Hb<11000:
        b = 0; L = -6.5
    elif Hb>=11000 and Hb<20000:    
        b = 1; L = 0
    elif Hb>=20000 and Hb<32000:
        b = 2; L = 1
    elif Hb>=32000 and Hb<47000:
        b = 3; L = 2.8
    elif Hb>=47000 and Hb<51000:
        b = 4; L = 0
    elif Hb>=51000 and Hb<71000:
        b = 5; L = -2.8    
    elif Hb>=71000 and Hb<84852:
        b = 6; L = -2   
    elif Hb==84852:
        b = 7; L = 0  
    return b, L, Hb
        


