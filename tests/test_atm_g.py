#%% Script information
# Name: test_atm_g.py
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

print('Careful. Table II of the Standard has H and Z wrongly placed in some cases.','\n')

# Z value to be tested
testval = [0, 5000, 50000, 130000, 180000, 265000] 
# Theoretical value of the property
teo_val = [9.8066, 9.7912, 9.6530, 9.4175, 9.274, 9.0374]                      
aux = np.arange(1,len(testval)+1)

for (index,value,teov) in zip(aux,testval,teo_val):
    print('Test #',index,sep='')
    print('The Z value is',value,'[m]')
    g = f.g(value)
    print('The g value is',round(g,4),'[m/s^2]')
    print('The g value from table is',teov,'[m/s^2]','\n')
#%% Tests that are NOT meant to work

print('====== Tests that should NOT work ======','\n')

testval = [-50] # Try also: 'string', 90000, -15.
aux = np.arange(1,len(testval)+1)

for (index,value) in zip(aux,testval):
    print('Test Mistake #',index,' - ','The input geometric height is ',value,sep='')
    print('The Z value is',value,'[m]')
    g = f.g(value)
    print('The g value is',round(g,4),'[m/s^2]')
    print('The g value from table is',teov,'[m/s^2]','\n')