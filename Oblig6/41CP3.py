import numpy as np

def fitData_line(data):
    A = np.array([
        [1, (data[0][0]-1960)],
        [1, (data[1][0]-1960)],
        [1, (data[3][0]-1960)],
        [1, (data[4][0]-1960)]
    ])
    b = np.array([data[0][-1], data[1][-1], data[3][-1], data[4][-1]])
    x = np.linalg.solve(A.T@A, A.T@b)
    print(x)
    r = b-A@x
    RMSE = np.linalg.norm(r)/(4**(1/2))
    print("RMSE")
    print(RMSE)
    print("1980 estimate")
    print(x[0]+ x[1]*(1980-1960))



def fitData_parabola(data):
    A = np.array([
        [1, (data[0][0]-1960), (data[0][0]-1960)**2],
        [1, (data[1][0]-1960), (data[1][0]-1960)**2],
        [1, (data[3][0]-1960), (data[3][0]-1960)**2],
        [1, (data[4][0]-1960), (data[4][0]-1960)**2]
    ])
    b = np.array([data[0][-1], data[1][-1], data[3][-1], data[4][-1]])
    x =np.linalg.solve(A.T@A, A.T@b)
    print(x)
    r = b-A@x
    RMSE = np.linalg.norm(r)/(4**(1/2))
    print("RMSE")
    print(RMSE)
    print("1980 estimate")
    print(x[0]+ x[1]*(1980-1960)+ x[2]*(1980-1960)**2)

def fitdata_exponential(data):
    A = np.array([
        [1, (data[0][0]-1960)],
        [1, (data[1][0]-1960)],
        [1, (data[3][0]-1960)],
        [1, (data[4][0]-1960)]
    ])
    b = np.array([np.log(data[0][-1]), np.log(data[1][-1]), np.log(data[3][-1]), np.log(data[4][-1])])
    x = np.linalg.solve(A.T@A, A.T@b)
    x[0] = np.e**x[0]
    print(x)
    r = b-A@x
    RMSE = np.linalg.norm(r)/(4**(1/2))
    print("RMSE")
    print(RMSE)
    print("1980 estimate")
    print(x[0]*np.e**(x[1]*(1980-1960)))


if __name__ == "__main__":
    data = [
        [1960, 3039585530],
        [1970, 3707475887],
        [1980, 4452584592],
        [1990, 5281653820],
        [2000, 6079603571]
    ]
    print("Line")
    fitData_line(data)
    #fit(data[:][0], data[:][1], 2)
    print("Parabola")
    fitData_parabola(data)
    print("Exponential")
    fitdata_exponential(data)

