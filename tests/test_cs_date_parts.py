#%% Script information
# Name: test_cs_date_parts.py
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

import fnc as f
from datetime import timedelta
#%% Testing

# Start
date1 = f.date_now()
[yr,mo,d,h,m,s] = f.date_parts(date1)

jd = f.JD(yr,mo,d,h,m,s)
tjd = f.jd2tjd(jd)
[a,b] = f.tjd2gmst(tjd)
print(date1)
print('GMST in degrees')
print(b, 'is the calculated value')

# Define the delta
# https://docs.python.org/3/library/datetime.html
delta = timedelta(days=0, seconds=4.0905, minutes=56, hours=23)

date2 = date1 + delta
[yr,mo,d,h,m,s] = f.date_parts(date2)

jd = f.JD(yr,mo,d,h,m,s)
tjd = f.jd2tjd(jd)
[a,b] = f.tjd2gmst(tjd)
print(date2)
print('GMST in degrees')
print(b, 'is the calculated value')