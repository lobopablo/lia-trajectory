#%% Script information
# Name: test_atm_p.py
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

testval = [0, 5000, 12000, 32000]
aux = np.arange(1,len(testval)+1)

for (index,value) in zip(aux,testval):
    print('Test #',index,sep='')
    print('The Z value is',value,'[m]')
    b, Lmb, Tmb, Hb, H, Pb = f.table4(value)
    print('The H value is',round(H*1000),'[m\']')
    print('The layer value is',b)
    print('The Lmb value is',Lmb,'[K/km\']')
    print('The Tmb value is',Tmb,'[K]')
    print('The Hb value is',Hb,'[km\']')
    print('The Pb value is',Pb,'[N/m^2]')
    tm = f.tm(Tmb,Lmb,H,Hb)
    print('The Tm value is',round(tm,3),'[K]')
    p = f.p(Tmb,Lmb,H,Hb,Pb)
    print('The p value is',round(p/100,3),'[mbar]','\n')

#%% Tests that are NOT meant to work

# print('====== Tests that should NOT work ======','\n')

# testval = [90000] # Try also: 'string', 90000, -15.
# aux = np.arange(1,len(testval)+1)

# for (index,value) in zip(aux,testval):
#     print('Test Mistake #',index,' - ','The input geometric height is ',value,sep='')
#     b, Lmb, Tmb, Hb, H, Pb = f.table4(value)
#     print('The H value is',round(H*1000),'[m\']')
#     p = f.p(Tmb,Lmb,H,Hb,Pb)
#     print('The p value is',round(p/100,3),'[mbar]','\n')