#%% Script information
# Name: test_atm_table4.py
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

testval = [0, 5000,11000,14000,20000,35000]
aux = np.arange(1,len(testval)+1)

for (index,value) in zip(aux,testval):
    print('Test #',index,' - ','The input value is ',value,sep='')
    b, Lmb, Tmb, Hb, Hz, Pb = f.table4(value)
    print('The layer value is',b)
    print('The Lmb value is',Lmb,'[K/km\']')
    print('The Tmb value is',Tmb,'[K]')
    print('The Hb value is',Hb,'[km\']')
    print('The Hz value is',round(Hz,2),'[km\']')
    print('The Pb value is',Pb,'[N/m^2]','\n')

#%% Tests that are NOT meant to work
print('====== Tests that should NOT work ======','\n')

testval = [90000] # Try also: 'string', 90000, -15.
aux = np.arange(1,len(testval)+1)

for (index,value) in zip(aux,testval):
    print('Test Mistake #',index,' - ','The input value is ',value,sep='')
    b, Lmb, Tmb, Hb, Hz, Pb = f.table4(value)
    print('The layer value is',b)
    print('The Lmb value is',Lmb,'[K/km\']')
    print('The Tmb value is',Tmb,'[K]')
    print('The Hb value is',Hb,'[km\']')
    print('The Hz value is',round(Hz,2),'[km\']')
    print('The Pb value is',Pb,'[N/m^2]','\n')
