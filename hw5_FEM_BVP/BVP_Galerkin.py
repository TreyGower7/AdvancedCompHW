import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

"""
Solving the boundary value problem with 
    -y'' = x 
where
    y(0) = y(1) = 0
"""

#Let N = 3 as in problem statement
N = 3
#boundary condtions
a=0
b=1

#define my basis function
def basis(i,x):
    return np.sin(i*np.pi*x)

def K_and_fvec():
    """ Calculate Stiffness and load vector via the Galerkin method
     
     Args:

     Returns: Stiffness matrix (K_ij) and load vector (f_i)
    
    """
    K = np.zeros(N,N)
    sumresult=0
    for i in range(0, N):
        sumresult += basis(i,x)

def main():
    """ Main entry point of the script """
    solve_kf = K_and_fvec()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()


