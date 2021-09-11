import numpy as np

def CGM(a, b, x0, n):
    d = []; r = []; x = []; alpha = []; beta = [];
    x.append(x0)
    d.append(b-a@x0)
    r.append(b-a@x0)
    for k in range(n):
        if (np.linalg.norm(r[k]) == 0): return x[k]
        alpha.append(np.dot(np.transpose(r[k]),r[k])/(d[k].transpose()@a@d[k]))
        x.append(x[k]+np.dot(alpha[k],d[k]))
        r.append(r[k]-np.dot(alpha[k],np.dot(a,d[k])))
        beta.append((np.transpose(r[k+1])@r[k+1]) / (np.transpose(r[k])@r[k]))
        d.append(r[k+1] + np.dot(beta[k],d[k]))
    return x[k+1]

def main():
    a1 = np.array([[1,0],[0,2]])
    b1 = np.array([2,4])
    x01 = [0,0]

    a2 = np.array([[1,2], [2,5]])
    b2 = np.array([1,1])
    x02 = np.array([1,1])

    n = 2

    print(CGM(a1, b1, x01, n))
    print(CGM(a2, b2, x02, n))


if __name__ == "__main__":
    main()
