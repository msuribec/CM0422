from math import inf

from sympy import *
import scipy.integrate as integratesci

def error_calc(f, approx, a, b, type):
    try:
        if type == 'math':
            the_error = error_math(f, approx, a, b)
        if type == 'scipy':
            the_error = error_scipy(f, approx, a, b)
    except :  # catch *all* exceptions
        the_error = inf
        print("Error could not be calculated")
    return the_error


def error_scipy(f, approx, a, b):
    x = symbols("x")
    fx = lambdify(x, (f - approx) ** 2, 'scipy')
    result = integratesci.quad(fx, a, b)
    return sqrt(result[0])

def error_math(f, approx, a, b):
    x = symbols("x")
    fx = lambdify(x, (f - approx) ** 2, 'math')
    result = integratesci.quad(fx, a, b)
    return sqrt(result[0])


def error_sympy(f, approx, a, b, x):
    print("error simpy")
    term = FU['TR9']((f - approx) * (f - approx))
    e2 = integrate(term, (x, a, b))
    return sqrt(N(e2))
