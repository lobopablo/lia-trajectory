#%% Script information
# Name: test_cs_JD.py
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

# Example 3.4 (Vallado)
# Date: October 26, 1996, at 2:20 P.M. UT
yr = 1996
mo = 10
d = 26
h = 14
m = 20
s = 0
jd = f.JD(yr,mo,d,h,m,s)
print(jd)
print(2450383.09722222,'is the correct result')

# Example 3.5 (Vallado)
# Date: August 20, 1992, 12:14 P.M. UT1 
yr = 1992
mo = 8
d = 20
h = 12
m = 14
s = 0
jd = f.JD(yr,mo,d,h,m,s)
print(jd)
print(2448855.009722,'is the correct result')