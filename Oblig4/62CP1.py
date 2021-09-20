
def trapezemethod(yd, ye, h, min, max, tInit, yInit):
    t = [tInit]
    y = [yInit]
    trunc = [0]
    step = 0
    i = tInit
    while i < max:
        t.append(t[step]+h)
        v = y[step]+h*yd(t[step], y[step])
        y.append(y[step]+(h/2)*(yd(t[step], y[step]) + yd(t[step+1], v)))
        trunc.append(y[step+1]-ye(t[step+1]))
        i+=h
        step +=1
    return [t, y, trunc]


def Main():
    h = 0.1
    min = 0
    max = 1
    tInit = 0
    yInit = 1
    def yd1(t,y):
        return t
    def ye1(t):
        return 1+(t**2)/2
    ans = trapezemethod(yd1, ye1, h, min, max, tInit, yInit)
    print(ans)
    for row in ans:
        for val in row:
            print
            '{:4}'.format(val),
        print

if __name__ == "__main__":
    Main()