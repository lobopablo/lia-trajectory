#%% Script information
# Name: test_atm_rho.py
# Authors: Trajectory Team (Matias Pellegrini, Pablo Lobo)
# Owner: LIA Aerospace
#
#%% Script description
#|
# The aim of this script is to test the function XXXX within the category
# YYY in the fnc.py file, considering this file is named test_YYY_XXXX.
#%% Clear Console
cls = lambda: print("\033[2J\033[;H", end='')
cls()

import numpy as np
import fnc as f
#%% Tests that are meant to work
print('====== Tests that should work ======','\n')

# Z value to be tested
testval = [0, 5000, 12000, 21500, 33000, 49000, 52000, 65000, 76500] 
# Theoretical value of the property
teo_val = [1.225, 0.7364, 0.31194, 0.06988, 0.01157, 0.001163, 0.00080562, 1.6321*10**-4, 3.1792*10**-5]                      
aux = np.arange(1,len(testval)+1)

for (index,value,teov) in zip(aux,testval,teo_val):
    print('Test #',index,sep='')
    print('The Z value is',value,'[m]')
    b, Lmb, Tmb, Hb, H, Pb = f.table4(value)
    print('The H value is',round(H*1000),'[m\']')
    tm = f.tm(Tmb,Lmb,H,Hb)
    p = f.p(Tmb,Lmb,H,Hb,Pb)
    rho = f.rho(p,tm)
    print('The rho value is',round(rho,6),'[kg/m^3]')
    print('The rho value from table is',teov,'[kg/m^3]','\n')
#%% Tests that are NOT meant to work

print('====== Tests that should NOT work ======','\n')

testval = [90000] # Try also: 'string', 90000, -15.
aux = np.arange(1,len(testval)+1)

for (index,value) in zip(aux,testval):
    print('Test Mistake #',index,' - ','The input geometric height is ',value,sep='')
    b, Lmb, Tmb, Hb, H, Pb = f.table4(value)
    print('The H value is',round(H*1000),'[m\']')
    tm = f.tm(Tmb,Lmb,H,Hb)
    p = f.p(Tmb,Lmb,H,Hb,Pb)
    rho = f.rho(p,tm)
    print('The rho value is',round(rho,6),'[kg/m^3]')
    print('The rho value from table is',teov,'[kg/m^3]','\n')