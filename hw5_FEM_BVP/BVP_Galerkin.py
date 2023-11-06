import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

"""
Solving the boundary value problem with 
    -y'' = x 
where
    y(0) = y(1) = 0
"""
#define my basis function
def Basis(i,x):
    return np.sin(i*np.pi*x)

#define my basis function
def Basis_deriv(i,x):
    return i*np.pi*np.cos(i*np.pi*x)

def Galerkin_kf(N,a,b):
    """ Calculate Stiffness and load vector via the Galerkin method and solve ku=f
     
     Args:

     Returns: Stiffness matrix (K_ij) and load vector (f_i)
    
    """
    K = np.zeros((N,N))
    f = np.zeros((N))
    for i in range(N):
        integrand_rhs = lambda x: x * Basis_deriv(i,x)
        # a =0 and b =1
        f[i] = quad(integrand_rhs,a,b)[0]
        for j in range(N):
            integrand_lhs = lambda x: Basis_deriv(i,x) * Basis_deriv(j,x)
            # a =0 and b =1
            K[i][j] = quad(integrand_lhs,a,b)[0]
    
    return [K,f]

def trial_function(coeff,x,N):
    soln = 0.0
    for i in range(1, N+1):
        soln += coeff[i-1] * Basis(i, x)
    return soln

def main():
    """ Main entry point of the script """
    #Let N = 3 as in problem statement
    N = 3
    #boundary condtions
    x_val =.5
    a=0
    b=1
    Kf = Galerkin_kf(N,a,b)

    print(Kf[0])
    print(Kf[1])

    #solve for the coefficients
    coeff = np.linalg.solve(Kf[0],Kf[1])
    #calculate approximate solution given an x value
    approximate = trial_function(coeff, x_val, N)

    print(approximate + ' at ' + ' x = ' + str(x_val))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()


