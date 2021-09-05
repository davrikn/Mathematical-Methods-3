import numpy as np

# Kanskje bruke newtons istaden for bisection
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
    tol = 0.000001
    a = 0
    b = 50

    def func(r):
        return (((1 / 3) * (np.pi) * (r ** 2)*(0.1+2)) - (5 * 10 ** (-5)))

    result = bisect(a, b, tol, func)
    for row in result:
        string = ""
        for data in row:
            string += str(data) + ", "
        print(string)


if __name__ == "__main__":
    main()
