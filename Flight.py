#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import environment
import vehicle

class flight:
    
    def __init__(self, environment, vehicle, """dependecies"""):
        """
        posible dependencies:
        - number of stages
        - max times of simulation
        - time steps
        - 
        """
        #variable initialization
        #introduce time passage function
        #define how to pass from one stage to the next
        #set simulation termination events (h=0, t=tmax, etc)
    
    def flight_powered:
        #powered flight calculations
    
    def flight_unpowered:
        #unpowered flight calculations
        #Is it really necessary? After all, the only difference is that there is no thrust
        #How can the same "calculation engine" be set so that some aspects (such as thrust) can be determined beforehand?
        #Idea: set the function with a dependency where this is set
            #such as: powered=true/false

