import numpy as np

def ydot(w):
    y = [lambda w : (w[0]**2)*w[1]]
    w1 = np.array([y[0](w)])
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


def midtpunkt_metode(f,y_init,h,n):
   y = []
   y.append(y_init)
   for i in range(n):
      s1 = f(y[i])
      s2 = f(y[i]+0.5*h*s1)
      y.append(y[i]+h*s2)
   return y

def Main():
    h = 0.1
    ranges = [0,1]
    n = int((ranges[1]-ranges[0])/h)
    y0 = 1
    midtpunkt_metode(ydot, y0, h, n)
    #midpoint(y0, h, ranges)


if __name__ == "__main__":
    Main()