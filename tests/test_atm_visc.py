#%% Script information
# Name: test_atm_visc.py
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
teo_val1 = [1.7894*10**-5, 1.6282*10**-5, 1.4216*10**-5, 1.4294*10**-5, \
            1.4992*10**-5, 1.7037*10**-5, 1.6956*10**-5, 1.5116*10**-5, \
            1.3595*10**-5 ]
        
teo_val2 = [1.4607*10**-5, 2.211*10**-5, 4.5574*10**-5, 2.0455*10**-4, \
            1.2955*10**-3, 1.4652*10**-2, 2.1047*10**-2, 9.2617*10**-2, \
            4.2761*10**-1 ]
aux = np.arange(1,len(testval)+1)

for (index,value,teov1,teov2) in zip(aux,testval,teo_val1,teo_val2):
    print('Test #',index,sep='')
    print('The Z value is',value,'[m]')
    b, Lmb, Tmb, Hb, H, Pb = f.table4(value)
    print('The H value is',round(H*1000),'[m\']')
    tm = f.tm(Tmb,Lmb,H,Hb)
    p = f.p(Tmb,Lmb,H,Hb,Pb)
    rho = f.rho(p,tm)
    dvisc, kvisc = f.visc(tm,rho)
    print('The dvisc value is',round(dvisc,8),'[N.s/m^2]')
    print('The dvisc value from table is',round(teov1,8),'[N.s/m^2]')
    print('The kvisc value is',round(kvisc,8),'[m^2/s]')
    print('The kvisc value from table is',round(teov2,8),'[m^2/s]','\n')
#%% Tests that are NOT meant to work

print('====== Tests that should NOT work ======','\n')

testval = [90000] # Try also: 'string', 90000, -15.
aux = np.arange(1,len(testval)+1)

for (index,value) in zip(aux,testval):
    print('Test Mistake #',index,' - ','The input geometric height is ',value,sep='')
    print('The Z value is',value,'[m]')
    b, Lmb, Tmb, Hb, H, Pb = f.table4(value)
    print('The H value is',round(H*1000),'[m\']')
    tm = f.tm(Tmb,Lmb,H,Hb)
    p = f.p(Tmb,Lmb,H,Hb,Pb)
    rho = f.rho(p,tm)
    dvisc, kvisc = f.visc(tm,rho)
    print('The dvisc value is',round(dvisc,8),'[N.s/m^2]')
    print('The dvisc value from table is',round(teov1,8),'[N.s/m^2]')
    print('The kvisc value is',round(kvisc,8),'[m^2/s]')
    print('The kvisc value from table is',round(teov2,8),'[m^2/s]','\n')