import numpy as np

def modGS(A, m, n):
    r = np.zeros(shape=[m,n])
    q = np.zeros(shape=[m, m])
    for j in range(n):
        y = A[j]
        #print("y")
        #print(y)
        for i in range(j):
            #print(i)
            #print("qi")
            #print(q[i])
            #print("qi transpose")
            #print(np.transpose(q[i]))
            r[i][j] = np.dot(q[i],y)
            #print("R")
            #print(r)
            y = y-r[i][j]*q[i]
            #print("Inner y")
            #print(y)
        r[j][j] = np.linalg.norm(y)
        #print("R")
        #print(r)
        #print("Y")
        #print(y)
        #print("Ynorm")
        #print(y/r[j][j])
        q[j] = y/r[j][j]
        #print(np.transpose(q))
        #print(q)
        #print("Q")
        #print(q)
    print("Q")
    print(np.transpose(q))
    print("R")
    print(r)

if __name__ == "__main__":
    A1 = [[4,3], [0,1]]
    n1 = 2
    m1 = n1
    A2 = [[1,1], [2,1]]
    n2 = 2
    m2 = n2
    A3 = [[2,1,2], [1,-1,1]]
    n3 = 2
    m3 = 3
    A4 = [[2,-2,2], [2,0,2], [8,-4,8]]
    n4 = 3
    m4 = 3

    #classicGS(A1,m1, n1)
    #classicGS(A2,m2, n2)
    #classicGS(A3,m3, n3)
    modGS(A4,m4, n4)


