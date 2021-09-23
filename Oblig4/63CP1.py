import numpy as np

def Main():
    interval = [0,1]
    h = 0.25
    k = int((interval[1]-interval[0])/h)
    w = np.array([[1.0,0.0]])
    for i in range(k):
        w = np.append(w, w[i]+h*ydot(i*h, w[i]), axis=0)
    print(w)


def ydot(t,w):
    y = [lambda w : w[0]+w[1], lambda w : w[1]-w[0]]
    w1 = np.array([[y[0](w), y[1](w)]])
    return w1


if __name__ == "__main__":
    Main()