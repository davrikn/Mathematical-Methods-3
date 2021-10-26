import numpy as np

def mvnewton(x_init, F, DF, steps):
    x = [x_init]
    for k in range(steps):
        fx = -np.array(F(x[k]))
        dfx = DF(x[k])
        s = np.linalg.solve(dfx, fx)
        x.append(x[k]+s)
    return x[-1]

if __name__ == "__main__":
    x_init1 = [1,1]
    x_init2 = [-1, -1]
    def F(x):
        return [x[0]**3-x[1]**3+x[0], x[0]**2+x[1]**2-1]
    def DF(x):
        return [
            [3*x[0]**2 + 1, -3*x[1]**2],
            [2*x[0], 2*x[1]]
        ]

    print(mvnewton(x_init1, F, DF, 100))
    print(mvnewton(x_init2, F, DF, 100))