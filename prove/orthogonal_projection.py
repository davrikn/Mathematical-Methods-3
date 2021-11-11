import numpy as np

#y is the vector you want to project onto w which is mxn
def proj(y, w):
    n = w.shape[0]
    m = w.shape[1]
    total = np.zeros(shape=(1,m))
    for i in range(n):
        u = w[i]
        total += np.dot((np.dot(y.T, u)/np.dot(u,u)), u)
    return total;

if __name__ == "__main__":
    y = np.array([3,6,-2,4])
    w = np.array([[1/2, -1/2, -1/2, 1/2],[1/2, 1/2, -1/2, -1/2]])

    print(proj(y,w))
