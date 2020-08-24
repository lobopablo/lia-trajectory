#%% Script information
# Name: test_atm_layer.py
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
from fnc import layer

#%% Tests that are meant to work
print('====== Tests that should work ======','\n')

testval = [0, 5000,11000,14000,20000,35000]
aux = np.arange(1,len(testval)+1)

for (index,value) in zip(aux,testval):
    print('Test #',index,' - ','The input value is ',value,sep='')
    b = layer(value)
    print('The layer value is',b,'\n')

#%% Tests that are NOT meant to work
print('====== Tests that should NOT work ======','\n')

testval = [-15,87000,'string']
aux = np.arange(1,len(testval)+1)

for (index,value) in zip(aux,testval):
    print('Test Mistake #',index,' - ','The input value is ',value,sep='')
    b = layer(value)
    print('The layer value is',b,'\n')

