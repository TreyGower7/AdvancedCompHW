import numpy as np
"""
Module Docstring
"""

__author__ = "Trey Gower"

def func(x):
    """ The function provided used to calculate f(x) """
    f = (x**2) - 3
    return f

def bisect_Method(tol, maxit, ends):
    """ The bisection method
     
     Args: A function f(x)

     Returns: The root of a polynomial 
    """
    #getting the endpoints from the array
    a = ends[0]
    b = ends[1]
    #iterations initialized
    it = 0

    #check endpoints for opposite signs
    fb = func(b)
    fa = func(a)

    if np.sign(fa) == np.sign(fb):
        return "Error: endpoints must have opposite signs"

    while it <= maxit:
        #midpoint calculation
        c = (a+b)/2

        #calculate function values
        fc = func(c)
        fa = func(a)

        if fc == 0 or (b-a)/2 < tol:
            root = "\nRoot found x = " + str(np.round(c,3)) + " in " + str(it) + " Iterations\n"
            return root
        
        #increment number of iterations
        it = it+1

        #assign closer endpoints for next iteration by intermediate value theorem
        if np.sign(fc) == np.sign(fa):
            a = c
        else:
            b = c
    return "Bisection Method failed by exceeding max steps"



def main():
    """ Main entry point of the app """
    tol = 1e-06
    maxit = 50
    ends = np.array([1,2])
    bisect = bisect_Method(tol, maxit, ends)

    print(bisect)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
