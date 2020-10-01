#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Funcion que calcula la orbita a partir de 


# In[11]:


#se define una funcion que depende de los vectores de velocidad del vehiculo al momento de burnout
#esta funcion luego se puede incluir al la clase Flight para incorporar la ultima parte de la simulacion

import numpy as np

#El calculo se comienza a partir de los vectores r (posicion con respecto al centro de la tierra) 
#y v (velocidad al instante del burnout)

#v = [v1, v2, v3]
#r = [r1, r2, r3]

def orb_calc(r,v):
    
    #vector module calculation
    orb_r0 = np.sqrt(r[0]**2+r[1]**2+r[2]**2)
    orb_v0 = np.sqrt(v[0]**2+v[1]**2+v[2]**2)
    
    #--------------Semi-mayor axis--------------
    #Earth's gravitational parameter
    orb_mu = 398600
    #total energy calculation
    orb_xi = ((orb_v0**2)/2)-(orb_mu/orb_r0)
    #semi-mayor axis calculation
    orb_a = (-orb_mu)/(2*orb_xi)
    print ("semi-mayor axis=", orb_a)
    
    #-------------Excentricity-----------------
    #Excentricity vector calculation
    orb_e_vector = (1/orb_mu)*((((orb_v0**2)-(orb_mu/orb_r0))*r)-((np.dot(r, v)*v)))
    #Excentricity module calculation
    orb_e_mod = np.sqrt(orb_e_vector[0]**2+orb_e_vector[1]**2+orb_e_vector[2]**2)
    orb_e = orb_e_mod
    print ("excentricity=", orb_e)
    
    #-------------Inclination---------------
    #coord system I axis
    orb_eci_k = np.array([0, 0, 1])
    #Angular momemtum vector calculation
    orb_h_cross = np.cross(r, v)
    orb_h_mod = np.sqrt(orb_h_cross[0]**2+orb_h_cross[1]**2+orb_h_cross[2]**2)
    #Inclination cosine
    orb_i_cos = (np.dot(orb_eci_k, orb_h_cross))/orb_h_mod
    #Inclination
    orb_i = np.arccos(orb_i_cos)
    orb_i = (orb_i*180)/np.pi
    print("inclination=", orb_i)
    
    #------------Longitude of ascending node------
    #coord system I axis
    orb_eci_i = [1, 0, 0]
    #ascending node vector
    orb_n = np.cross(orb_eci_k, orb_h_cross)
    #ascending node vector module
    orb_n_mod = np.sqrt(orb_n[0]**2+orb_n[1]**2+orb_n[2]**2)
    #cosine of longitude of ascending node
    orb_omega_cos = np.dot(orb_eci_i, orb_n)/orb_n_mod
    #coord system J axis
    orb_eci_j = [0, 1, 0]
    #sine of longitude of ascending node
    orb_omega_sin = np.dot(orb_eci_j, orb_n)/orb_n_mod
    #orb_omega =np.arccos(orb_omega_cos)
    #orb_omega = (orb_omega*180)/np.pi
    #quadrant determination
    if orb_omega_cos>0 and orb_omega_sin>0:
        orb_omega = np.arccos(orb_omega_cos)
        orb_omega = (orb_omega*180)/np.pi
    elif orb_omega_cos<0 and orb_omega_sin>0:
        orb_omega = np.arccos(orb_omega_cos)
        orb_omega = (orb_omega*180)/np.pi
    elif orb_omega_cos<0 and orb_omega_sin<0:
        orb_omega = np.arccos(orb_omega_cos)
        orb_omega = (2*np.pi)-orb_omega
        orb_omega = (orb_omega*180)/np.pi
    elif orb_omega_cos>0 and orb_omega_sin<0:
        orb_omega = np.arccos(orb_omega_cos)
        orb_omega = (2*np.pi)-orb_omega
        orb_omega = (orb_omega*180)/np.pi
    else:
        orb_omega = "revisalo amigo, aca hay algo mal"
        
    print("longitude of ascending node=", orb_omega)
    
    #-----------Argument of periapsis-------------
    #argument of periapsis cosine
    orb_womega_cos = np.dot(orb_n, orb_e_vector)/(orb_n_mod*orb_e_mod)
    #quadrant determination
    if orb_e_vector[2]>0:
        orb_womega = np.arccos(orb_womega_cos)
        orb_womega = (orb_womega*180)/np.pi
    else:
        orb_womega = np.arccos(orb_womega_cos)
        orb_womega = (2*np.pi)-orb_womega
        orb_womega = (orb_womega*180)/np.pi
    
    print("argument of periapsis=", orb_womega)
    
    #----------True anomaly------------
    #true anomaly 
    orb_tita_cos = np.dot(orb_e_vector, r)/(orb_e_mod*orb_r0)
    #quadrant determination
    orb_tita_aux = np.dot(r, v)
    if orb_tita_aux>0:
        orb_tita = np.arccos(orb_tita_cos)
        orb_tita = (orb_tita*180)/np.pi
    else:
        orb_tita = np.arccos(orb_tita_cos)
        orb_tita = (2*np.pi)-orb_tita
        orb_tita = (orb_tita*180)/np.pi
    
    print("True anomaly=", orb_tita)
    
    return 
    


# In[12]:


r = np.array([9031.5, -5316.9, -1647.2])
v = np.array([-2.8640, 5.1112, -5.0805])

orb_calc(r, v)


# In[ ]:




