import numpy as np


def eulers(yd, h, min, max, tInit, yInit ):
    t = [tInit]
    y = [yInit]
    i = min
    step = 0
    while i < max:
        y.append(y[step]+h*yd(t[step], y[step]))
        t.append(h+t[step])
        i += h
        step += 1
    return y



def Main():
    h = 0.1
    min = 0
    max = 1
    tInit = 0
    yInit = 1
    def yd1(t,y):
        return t
    def yd2(t,y):
        return t**2*y
    def ye1(t):
        return 1+(t**2)/2
    def ye2(t):
        return np.e**((t**3)/3)
    ya = eulers(yd1, h, min, max, tInit, yInit)
    yb = eulers(yd2, h, min, max, tInit, yInit)
    print(yb)
    errA = ya[-1]-ye1(max)
    errB = yb[-1]-ye2(max)

    print(errA)
    print(errB)



if __name__ == "__main__":
    Main()