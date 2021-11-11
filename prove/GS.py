import numpy as np

def QR_GS(A):
    (m,n) = A.shape
    R=np.zeros([n,n])
    Q=np.zeros([m,n])
    for j in range(n):
        y=A[:,j]
        for i in range(j):
            R[i,j]=Q[:,i].T@A[:,j]
            y=y-R[i,j]*Q[:,i]
        R[j,j]=np.sqrt(y.T@y)
        Q[:,j]=y/R[j,j]
    return Q, R

def QR_GS_modified(A):
    (m , n ) =A.shape
    R = np.zeros ([n, n])
    Q = np.zeros ([m, n])
    for j in range(n):
        y=A[:,j]
        for i in range(j):
            R[i,j]=Q[:,i].T@y
            y=y-R[i,j]*Q[:,i]
        R[j,j]=np.sqrt(y.T@y)
        Q[:,j]=y/R[j,j]
    return Q,R



if __name__ == "__main__":
    A = np.array([[2,-2, 2],[2,0,2],[5,-4,8]])
    Q , R = QR_GS(A)
    print("Q")
    print(Q)
    print("R")
    print(R)
    print("Should be A")
    print(Q@R)