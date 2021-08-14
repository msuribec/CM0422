from math import inf

from sympy import *
import scipy.integrate as integratesci
from GraphingGUI import graph_data

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


def error_and_graphs(text1,_error, _graph, x, fx, approx, x0, x1, a, b, type_error,name):
    if _error:
        the_error = error_calc(fx, approx, a, b, type_error)
        text1.insert(tk.INSERT, '\nerror: {} \n'.format(the_error))

    if _graph:
        graph_data(fx, approx, x0, x1, name)


def error_calc(f, approx, a, b, type):
    try:
        if type == 'math':
            the_error = error_math(f, approx, a, b)
        if type == 'scipy':
            the_error = error_scipy(f, approx, a, b)
    except:  # catch *all* exceptions
        the_error = inf
        text1.insert(tk.INSERT, "Error could not be calculated")
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
    term = FU['TR9']((f - approx) * (f - approx))
    e2 = integrate(term, (x, a, b))
    return sqrt(N(e2))
