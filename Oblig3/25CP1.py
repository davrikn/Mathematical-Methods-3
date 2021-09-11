import numpy as np
import scipy.sparse as sp

def jacobi(a, b, k):
    n = np.size(b)
    d = np.diag(a)
    r = a-np.diag(d)
    x = 0
    for i in range(k):
        x = (b-np.dot(r,x)) / d
        print(i)
        print(np.linalg.norm(r))
    return x

def jacobi2(a,b,tol):
    n = np.size(b)
    d = np.diag(a)
    r = a-np.diag(d)
    x = np.zeros([n,1])
    for i in range(n):
        print()
        #x  = np.divide((b-) ,d)

def main():
    n = 100
    A = sp.diags([-1, 3, -1], [-1, 0, 1], shape=(n,n)).toarray()
    b = np.ones([n,1]);b[0]=2;b[n-1]=2;
    k = 36
    result = jacobi(A,b,k)
    print(result)

if __name__ == "__main__":
    main()