import numpy as np


fy = [lambda t,w: (t**2)*w[0]]

for i in range(10):
    print(i)

def mpStep(w,t,h):
    w1 = np.array([])
    np.append(w1, w+h*fy[0](t+h/2, w+h/2*fy[0](t, w)))
    return w1

def midpoint(fy, y0, h, ranges):
    n = int((ranges[1]-ranges[0])/h)
    print(n)
    w = np.array([[y0]])
    t = ranges[0]
    print(n)
    for i in range(n):
        np.append(w, mpStep(w[i][0], t, h))
        t += h
    print(w)






def Main():
    h = 0.1
    range = [0,1]
    y0 = 1
    midpoint(fy, y0, h, range)


if __name__ == "__main__":
    Main()