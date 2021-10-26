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
    x_init = [1,1]
    def F1(x):
        return [x[0]**2 + x[1]**2 - 1, (x[0]-1)**2 + x[1]**2 - 1]
    def DF1(x):
        return [[2*x[0], 2*x[1]], [2*(x[0]-1), 2*x[1]]]
    print("a)")
    print(mvnewton(x_init, F1, DF1, 100))

    def F2(x):
        return [x[0]**2 + 4*x[1]**2 - 4, 4*x[0]**2 + x[1]**2 - 4]
    def DF2(x):
        return [[2*x[0], 8*x[1]], [8*x[0], 2*x[1]]]
    print("b)")
    print(mvnewton(x_init, F2, DF2, 100))

    def F3(x):
        return [x[0]**2 - 4*x[1]**2 - 4, (x[0]-1)**2 + x[1]**2 - 4]
    def DF3(x):
        return [[2*x[0], -8*x[1]], [2*(x[0]-1), 2*x[1]]]
    print("c)")
    print(mvnewton(x_init, F3, DF3, 100))
