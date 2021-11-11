import numpy as np

def PowerIteration ( A , x , k ) :
    for i in range(0, k):
        u = x / np.linalg.norm(x)
        x = A.dot(u)
        lam = u.dot(x)
    u = x / np.linalg.norm(x)
    return lam, u

if __name__ == "__main__":
    A = np.array([[-14, 20, 10], [-19, 27, 12], [23, -32, -13]])
    u0 = np.array([1, 1, 1])
    lam, u = PowerIteration(A, u0, 100)
    print(" Lambda = {} , u = {} ". format(lam, u))
