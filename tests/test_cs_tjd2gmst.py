#%% Script information
# Name: test_cs_tjd2gmst.py
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

import fnc as f
#%% Tests that are meant to work

# Example 3.5 (Vallado)
# Date: August 20, 1992, 12:14 P.M. UT1 
yr = 1992
mo = 8
d = 20
h = 12
m = 14
s = 0
jd = f.JD(yr,mo,d,h,m,s)

tjd = f.jd2tjd(jd)

[a,b] = f.tjd2gmst(tjd)
print('GMST in seconds')
print(a, 'is the calculated value')
print(-232984181.0909255,'is the correct result')
print('GMST in degrees')
print(b, 'is the calculated value')
print(152.578787810,'is the correct result')

