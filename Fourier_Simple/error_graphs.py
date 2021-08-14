from math import inf

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integratesci
from sympy import *


def loglog_plot(ns,ers,name):
    ns = np.array(ns)
    ers = np.array(ers)
    plt.loglog(ers,1/ns)
    plt.title("Log-log plot of Ej vs 1/j for " + name + " series")
    plt.xlabel("Ej")
    plt.ylabel("1/j")
    plt.show()


def error_and_graphs(_error, _graph, x, fx, approx, x0, x1, a, b, type_error):
    if _error:
        the_error = error_calc(fx, approx, a, b, type_error)
        print('\nerror: {} \n'.format(the_error))

    if _graph:
        graph_simple(x, fx, approx, x0, x1)
    return the_error


def graph_simple(x, fx, approx, x0, x1):
    p1 = approx
    p2 = fx
    p = plot(p1, p2, (x, x0, x1), show=false)
    # change the color of p2
    p[1].line_color = 'r'
    p.show()



def error_calc(f, approx, a, b, type):
    try:
        if type == 'math':
            the_error = error_math(f, approx, a, b)
        if type == 'scipy':
            the_error = error_scipy(f, approx, a, b)
    except:  # catch *all* exceptions
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
