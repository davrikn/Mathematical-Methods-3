import numpy as np


def poly_horner(n, poly, x):
    result = poly[n]
    for i in range(0, n):
        result = result*x+poly[i]
    return result


def alt(x):
    qx = ((x**51)-1)/(x-1)
    return qx


def main():
    poly = np.ones(51)
    x = 1.00001
    n = len(poly)-1
    nested = poly_horner(n, poly, x)
    alternative = alt(x)
    print(alternative)
    dif = nested-alternative
    print(dif)


if __name__ == "__main__":
    main()
