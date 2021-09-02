import numpy as np


def func(x):
    return (2*x+2)**(1/3)


def fpi(x, tol, func):
    xs = [x, func(x)]
    i = 1
    while abs(xs[i] - xs[i - 1]) > tol:
        i += 1
        xs.append(func(xs[i-1]))
        print(xs[i])
    return xs


def main():
    x = 1
    tol = 0.00000001
    result = fpi(x, tol, func)
    print(result)

if __name__ == "__main__":
    main()
