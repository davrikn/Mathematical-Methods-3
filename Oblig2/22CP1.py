import numpy as np


def lu(n, a):
    print("lu")
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
    return[u,l]

def main():
    a = [[3,1,2],[6,3,4],[3,1,5]]
    b = [[4,2,0],[4,4,2],[2,2,3]]
    c = [[1,-1,1,2],[0,2,1,0],[1,3,4,4],[0,2,1,-1]]
    print(lu(3, a))
    print(lu(3, b))
    print(lu(4, c))


if __name__ == "__main__":
    main()