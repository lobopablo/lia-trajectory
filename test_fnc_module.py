#%% Script information
# Name: test_fnc_module.py
# Authors: Trajectory Team (Matias Pellegrini, Pablo Lobo)
# Owner: LIA Aerospace
# Date: August 2020
#
#%% Script description
#
# The aim of this script is to test the different functions within fnc.py.
#%% Package
import fnc as f

cls = lambda: print("\033[2J\033[;H", end='')
cls()

#%% tm, table4 and layer
testvalue = 25600

b, Lmb, Tmb, Hb, Hz, Pb = f.table4(testvalue)
tm = f.tm(Tmb,Lmb,Hz,Hb)
print('\n Testing functions tm, table4 and layer')
print(b,Lmb,Tmb,Hb,Hz,tm, '\n b Lmb Tmb Hb Hz tm')

#%% p, table4 and layer
b, Lmb, Tmb, Hb, Hz, Pb = f.table4(testvalue)
p = f.p(Tmb,Lmb,Hz,Hb,Pb)
print('\n Testing functions p, table4 and layer')
print(b,Lmb,Tmb,Hb,Hz,Pb,p, '\n b Lmb Tmb Hb Hz Pb p')

