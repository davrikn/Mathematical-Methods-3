import numpy as np
import scipy.sparse as sp

def CGM(a, b, x0, n, tol):
    d = []; r = []; x = []; alpha = []; beta = [];
    x.append(x0)
    d.append(b-a@x0)
    r.append(b-a@x0)
    for k in range(n):
        print(str(k))
        if (np.linalg.norm(r[k]) < tol):
            print("Iterations: " + str(k))
            return x[k]
        alpha.append(np.dot(np.transpose(r[k]),r[k])/(d[k].transpose()@a@d[k]))
        x.append(x[k]+np.dot(alpha[k],d[k]))
        r.append(r[k]-np.dot(alpha[k],np.dot(a,d[k])))
        beta.append((np.transpose(r[k+1])@r[k+1]) / (np.transpose(r[k])@r[k]))
        d.append(r[k+1] + np.dot(beta[k],d[k]))
    return x[k+1]

def main():
    n = [100,1000,10000]

    tol = np.finfo(float).eps
    #Create 100x100 sparse matrix with 3 on the diagonal and -1 over and under
    #Also create [1,1.....1,1] initial guess
    #And b vector [2.5, 1.5, 1.5...1.5, 1.0, 1.0, 1.5...1.5,2.5]
    a1 = sp.diags([-1,3,-1], [-1,0,1], shape=(n[0],n[0])).toarray()
    x1 = np.ones(shape=(n[0]))
    b1 = np.ones(shape=(n[0]))*1.5
    b1[0] = 2.5; b1[n[0]-1] = 2.5;
    b1[(int(n[0]/2))] = 1.0;
    b1[int((n[0]/2-1))] = 1.0

    #Create 1000x1000 sparse matrix with 3 on the diagonal and -1 over and under
    a2 = sp.diags([-1,3,-1], [-1,0,1], shape=(n[1],n[1])).toarray()
    x2 = np.ones(shape=(n[1]))
    b2 = np.ones(shape=(n[1]))*1.5
    b2[0] = 2.5; b2[n[1]-1] = 2.5;
    b2[(int(n[1]/2))] = 1.0;
    b2[int((n[1]/2-1))] = 1.0

    a3 = sp.diags([-1,3,-1], [-1,0,1], shape=(n[2],n[2])).toarray()
    x3 = np.ones(shape=(n[2]))
    b3 = np.ones(shape=(n[2]))*1.5
    b3[0] = 2.5; b3[n[2]-1] = 2.5;
    b3[(int(n[2]/2))] = 1.0;
    b3[int((n[2]/2-1))] = 1.0
    print("Start a1")
    print(CGM(a1,b1,x1, n[0],tol))
    print("a1 done")

    print("Start a2")
    print(CGM(a2,b2,x2, n[1], tol))
    print("a2 done")

    print("Start a3")
    print(CGM(a3,b3,x3, n[2], tol))
    print("a3 done")


if __name__ == "__main__":
    main()
