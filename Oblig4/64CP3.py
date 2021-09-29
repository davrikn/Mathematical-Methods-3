import numpy as np

def rk4(y0, fy, h, ranges):
    n = int((ranges[1]-ranges[0])/h)
    w = np.array([y0])
    t = ranges[0]
    for i in range(n):
        s1 = fy[0](t,w[i])
        s2 = fy[0](t+h/2, w[i]+(h/2)*s1)
        s3 = fy[0](t+h/2, w[i]+(h/2)*s2)
        s4 = fy[0](t+h, w[i]+h*s3)
        w1 = np.array([w[i]+(h/6)*(s1+2*s2+2*s3+s4)])
        w = np.append(w, w1, axis=0)
        t += h
    #print(w)
    return [w, t]



def Main():
    h = [0.1, 0.05, 0.025]
    ranges = [0,1]
    fy = [lambda t, w: (t**2)*w]
    y0 = np.array([1])
    w1 = rk4(y0, fy, h[0], ranges)
    w2 = rk4(y0, fy, h[1], ranges)
    w3 = rk4(y0, fy, h[2], ranges)
    print(w1[0][-1]+ " t: " +w1[-1]+ " error")
    print(w2[0][-1]+ " t: " +w2[-1]+ " error:")
    print(w3[0][-1]+ " t: " +w3[-1]+" error:")




if __name__ == "__main__":
    Main()