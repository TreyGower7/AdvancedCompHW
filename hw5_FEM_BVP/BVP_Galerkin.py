import numpy as np
import matplotlib.pyplot as plt

"""
Solving the boundary value problem with 
    -y'' = x 
where
    y(0) = y(1) = 0
"""

#Let N =3 as in problem statement
N = 3

#define my basis function
def basis(i,x):
    return np.sin(i*np.pi*x)

def K_and_fvec():
    """ Calculate Stiffness and load vector via the Galerkin method
     
     Args:

     Returns: Stiffness matrix (K_ij) and load vector (f_i)
    
    """

def main():
    """ Main entry point of the script """
    soln_kf = K_and_fvec()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()


