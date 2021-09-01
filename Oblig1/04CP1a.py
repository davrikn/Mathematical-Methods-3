import numpy as np

xs = np.ones(14)
for i in range(0, xs.size):
    xs[i] = 10**((i*(-1)-1))

res = np.zeros((14, 3))

def ogFunc(x):
    return (1-(1/np.cos(x)))/(np.tan(x)**2)


def revFunc(x):
    return (-1/(1+(1/np.cos(x))))


for i in range(0, (xs.size)):
    res[i, 0] = xs[i]
    res[i, 1] = ogFunc(xs[i])
    res[i, 2] = revFunc(xs[i])


print(res)

