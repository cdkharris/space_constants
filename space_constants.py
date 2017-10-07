"""SI constants for space plasma physics

kb [J K-1] boltzmann constant
qe [C]     charge of an electron
me [kg]    mass of an electron
mp [kg]    mass of a proton
be [nT]    earth's magnetic field
           on the magnetic equator
           at the earth's surface
cl [m s-1] speed of light in a vacuum
e0 [F m-1] permittivity of free space
m0 [H m-1] permeability of free space
"""

import numpy as np

kb = 1.3807e-23 
qe = 1.6022e-19 
me = 9.1094e-31 
mp = 1.6726e-27 
be = 3.1000e-5  
cl = 2.9979e8   
e0 = 8.8542e-12 
m0 = 4*np.pi*1e-7
