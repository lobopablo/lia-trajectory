#%% Script information
# Name: test_cs_add_step.py
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

date1 = f.date_now()
print(date1)
delta = timedelta(days=0, seconds=0.2, minutes=0, hours=0)
date2 = date1 + delta
print(date2)