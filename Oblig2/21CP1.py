import numpy as np

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
 #   return back_sub(n,a,b,x)


#    def back_sub(n, a, b, x):
#        for i in range(n-1,1):
#            for j in range(i+1, n-1):
#                b[i] = b[i]-a[i][j]*x[j]
#            x[i] = b[i]/a[i][i]
#        return x


def main():
    a = [[1,2,-1,2],
         [0,3,1,4],
         [2,-1,1,2]]
    n = 3
    x = np.zeros(n)

    print(gaussian(n, a, x))

if __name__ == "__main__":
    main()

