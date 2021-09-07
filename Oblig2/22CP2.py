import numpy as np


def lu(n, a, b):
    u = []
    l = []
    for i in range(n):
        lr = []
        ur = []
        for j in range(n):
            ur.append(0)
            if (i == j):
                lr.append(1)
            else:
                lr.append(0)
        u.append(ur)
        l.append(lr)

    for i in range(n):
        u[0][i] = a[0][i]
        if a[i][i] == 0:
            return "error"
        for j in range(i+1, n):
            mult = a[j][i]/a[i][i]
            for k in range(n):
                a[j][k] = a[j][k] - mult*a[i][k]
                u[j][k] = a[j][k]
            l[j][i] = mult
    print(l)
    print(u)
    c = backsubl(n, l, b)
    print(c)
    x = backsubu(n, u, c)
    return x


def backsubl(n, l, b):
    c = []
    for i in range(n):
        c.append(0)
        for j in range(0, i):
            b[i] = b[i] - c[j]*l[i][j]
        c[i] = b[i]/l[i][i]
    return c

def backsubu(n, u, c):
    x = []
    c = c.copy()
    for i in range(n):
        x.append(0)

    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            c[i] = c[i] - u[i][j]*x[j]
        x[i] = c[i]/u[i][i]
    return x




def main():
    a = [[3,1,2],[6,3,4],[3,1,5]]
    ab = [0,1,3]
    b = [[4,2,0],[4,4,2],[2,2,3]]
    bb = [2,4,6]

    print(lu(3, a, ab))
    print(lu(3, b, bb))


if __name__ == "__main__":
    main()