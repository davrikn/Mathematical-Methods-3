import matplotlib.pyplot as plt
import matplotlib_inline

import matplotlib.pyplot as pyplot
import numpy as np
import scipy.sparse
import scipy.sparse.linalg

# The following method returns the matrix A used in the exercises.
# The method make_A returns a so called sparse matrix. This is
# a matrix where most of the entries are zero. 
def make_A(n):
    data = np.array([[1,-4,6,-4,1]]).T@np.ones([1,n])   # multi diagonals, @ is 
                                                        #matrix multiplication 
    offset = np.array([-2,-1,0,1,2])                    # diagonal offsets
    A = scipy.sparse.dia_matrix((data,offset),(n,n))    # make sparse multi-diagonal 
                                                        # matrix
    A = A.tolil()  # Transform to a sparse matrix format that is suitable to 
                   #change individual entries.
    A[0,0:4] = np.array([16,-9,8/3,-1/4])               # Set special entries
    A[n-2:n,n-4:n] = np.array([[ 16,-60,  72,-28],      # that do not follow 
                               [-12, 96,-156, 72]])/17  # the 1,-4,6,-4,1 pattern.
    A = A.tocsc()
    return A

# The following method returns the vector on the right hand side of the
# Euler-Bernoulli equation.
def make_F(n):
    L=2;w=0.3;d=0.03                    # Set the dimensions of the beam.
    E=1.3e10;g=9.81;density=480         # Set the physical constants
    h=L/n;                              # Calculate the step length
    I= w * d**3 /12                     # Calculate the momentum of inertia 
    f = -density*w*d*g;                 # Calculate force per meter.
    F = h**4/(E*I)*f*np.ones([n,1])     # Right hand side of the
                                        # Euler-Bernoulli equation.
    return F 

# This function gives the exact solution of the unloaded beam
def y_exact_0(x):
    L = 2; w = 0.3; d = 0.03              # Set the dimensions of the beam.
    E = 1.3e10; g = 9.81; density = 480   # Set the physical constants
    I =  w * d**3 / 12                    # Calculate the momentum of inertia 
    f = -density*w*d*g;                   # Calculate force per meter.
    return (f/(24*E*I))*x*x*(((x-4*L)*x)+6*L**2)

def make_x(n):
    L=2
    h=L/n
    return np.linspace(h,L,n)

def oppg2():
    xMax = 1
    n = 1024
    h = xMax / n
    a = make_A(n)
    print(a)
    b = make_F(n)
    numericalEstimate = scipy.sparse.linalg.spsolve(a, b)
    exactSolution = []
    x_range = []
    error = []
    i = 0
    step = 0
    while i < xMax:
        x_range.append(i)
        exactSolution.append(y_exact_0(i))
        error.append(numericalEstimate[step] - exactSolution[step])
        i += h
        step += 1
    print(numericalEstimate)
    pyplot.plot(x_range, numericalEstimate)
    pyplot.plot(x_range, exactSolution)
    pyplot.plot(x_range, error)
    pyplot.legend(["Estimate", "Exact", "Error"])
    pyplot.show()

def idk(n, xMax):
    h = xMax / n
    a = make_A(n)
    #print(a)
    b = make_F(n)
    numericalEstimate = scipy.sparse.linalg.spsolve(a, b)
    exactSolution = []
    x_range = []
    error = []
    i = 0
    step = 0
    while i < xMax:
        if step == n: break
        numericalEstimate[step] = numericalEstimate[step].__abs__()
        x_range.append(i)
        exactSolution.append(y_exact_0(i).__abs__())
        error.append((numericalEstimate[step] - exactSolution[step]).__abs__())
        i += h
        step += 1
    #print(numericalEstimate)
    print(error[-1])
    pyplot.plot(x_range, numericalEstimate)
    pyplot.plot(x_range, exactSolution)
    pyplot.plot(x_range, error)
    pyplot.legend(["Estimate", "Exact", "Error"])
    pyplot.loglog()
    pyplot.show()
    return numericalEstimate

def oppg3():
    xmax = 2
    n = []
    ret = [["          y          ", "       estimate      ", "       error     "]]
    for i in range(1,10):
        n.append(10*2**i)

    for i in range(9):
        ans = idk(n[i],xmax)
        err = ans[-1] - y_exact_0(2)
        ret.append([y_exact_0(2), ans[-1], err])
        #print(f"Error = {err}")

    for i in range(9):
        print("--------------------------------------------------------------")
        print(str(ret[i][0]) + "|" + str(ret[i][1]) + "|" +str(ret[i][2]))
    #print(ret)

if __name__ == "__main__":
    #oppg2()
    oppg3()