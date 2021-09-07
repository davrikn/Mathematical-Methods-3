import numpy as np

#TODO få til å funke

def gaussian(n, a, x):
    for i in range(n):
        if a[i][i] == 0:
            return "error"
        for j in range(i+1, n):
            mult = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - mult*a[i][k]
    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = a[i][n]
        for j in range(i+1,n):
            x[i] = x[i] -a[i][j]*x[j]
        x[i] = x[i]/a[i][i]
    return x


def main():
    al = 2
    a = hilbert(al)
    bl = 5
    b = hilbert(bl)
    cl = 10
    c = hilbert(cl)

    print(gaussian(al, a, np.zeros(al)))
    print(gaussian(bl, b, np.zeros(bl)))
    print(gaussian(cl, c, np.zeros(cl)))


def hilbert(n):


    a = []
    for i in range(n):
        row = []
        for j in range(n+1):
            row.append(1)
        a.append(row)
    print(a)

    for i in range(n):
        for j in range(n):
            a[i][j] = hilbertfunc(i+1, j+1)
    return a

def hilbertfunc(i, j):
    return 1/(i+j-1)


if __name__ == "__main__":
    main()
