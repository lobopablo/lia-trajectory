#%% Script information
# Name: test_atm_tm.py
# Authors: Trajectory Team (Matias Pellegrini, Pablo Lobo)
# Owner: LIA Aerospace
#
#%% Script description
#
# The aim of this script is to test the function XXXX within the category
# YYY in the fnc.py file, considering this file is named test_YYY_XXXX.
#%% Clear Console
cls = lambda: print("\033[2J\033[;H", end='')
cls()

import numpy as np
import fnc as f
#%% Tests that are meant to work
print('====== Tests that should work ======','\n')

testval = [0, 5004,11019,14031,20063,35194, 69757,82559]
aux = np.arange(1,len(testval)+1)

for (index,value) in zip(aux,testval):
    print('Test #',index,' - ','The input geometric height is ',value,sep='')
    b, Lmb, Tmb, Hb, H, Pb = f.table4(value)
    print('The H value is',round(H*1000),'[m\']')
    tm = f.tm(Tmb,Lmb,H,Hb)
    print('The Tm value is',round(tm,3),'[K]','\n')

#%% Tests that are NOT meant to work

print('====== Tests that should NOT work ======','\n')

testval = [90000] # Try also: 'string', 90000, -15.
aux = np.arange(1,len(testval)+1)

for (index,value) in zip(aux,testval):
    print('Test Mistake #',index,' - ','The input geometric height is ',value,sep='')
    b, Lmb, Tmb, Hb, H, Pb = f.table4(value)
    print('The H value is',round(H*1000),'[m\']')
    tm = f.tm(Tmb,Lmb,H,Hb)
    print('The Tm value is',round(tm,3),'[K]','\n')