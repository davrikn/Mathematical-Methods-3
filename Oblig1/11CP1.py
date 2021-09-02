import numpy as np


def bisect(a, b, tol, func):
    iterations = 0
    c = (a + b) / 2
    bisectresult = [["it", "a", "fa", "c", "fc", "b", "fb"]]

    while ((b - a) / 2 > tol):
        c = (a + b) / 2
        bisectresult.append([iterations, a, np.sign(a), c, np.sign(c), b, np.sign(b)])

        res = func(c)
        sign = np.sign(res)
        if (sign == np.sign(b)):
            b = c
        else:
            a = c
        iterations = iterations + 1
    return bisectresult


def main():
    tol = 0.0000001
    a = 2
    b = 3

    def func(x):
        return ((x ** 3) - 9)

    result = bisect(a, b, tol, func)
    for row in result:
        string = ""
        for data in row:
            string += str(data) + ", "
        print(string)


if __name__ == "__main__":
    main()
