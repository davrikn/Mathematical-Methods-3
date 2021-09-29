import numpy as np

def ydot(t,w):
    y = [lambda t, w : (t**2)*w]
    w1 = np.array([y[0](t,w[0])])
    return w1

def midpoint(y0, h, ranges):
    n = int((ranges[1]-ranges[0])/h)
    w = np.array([y0])
    t = ranges[0]
    for i in range(n):
        w1 = np.array([w[i] + h * ydot(t+h/2,w[i]+(h/2)*ydot(t, w[i]))])
        w = np.append(w, w1, axis=0)
        t += h
    print(w)

def Main():
    h = 0.1
    range = [0,1]
    y0 = [1]
    midpoint(y0, h, range)


if __name__ == "__main__":
    Main()