# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from sympy import *
from GraphingGUI import graph_simple
from sympy.simplify.fu import TR9
from sympy.parsing.sympy_parser import parse_expr
from error_graphs import error_and_graphs
from sympy import Piecewise, log, piecewise_fold

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def define_input(parsefun, f):
    x, n = symbols("x,n")
    if parsefun:
        fx = parse_expr(f, evaluate=False)
    else:
        fx = f
    return x, n, fx


def cosine_series(text1, f, x0, x1, a=0, b=pi, niter=50, parsefun=False, _error=False, _graph=False, _print=False,
                   type_error='math'):
    x, n, fx = define_input(parsefun, f)

    fi0 = parse_expr('1/(sqrt(pi))', evaluate=False)
    fn = parse_expr('(sqrt(2/pi)) * cos(n*x)', evaluate=False)

    c0 = integrate(fi0 * fx, (x, a, b))
    cn = integrate(fn * fx, (x, a, b))

    coef0 = parse_expr('2/sqrt(pi)', evaluate=False)
    coefn = parse_expr('sqrt(2/pi)', evaluate=False)

    a0 = coef0 * c0
    an = coefn * cn

    approx = a0 / 2
    for i in range(1, niter + 1):
        ai = an.subs(n, i)
        term = parse_expr('cos(n*x)', evaluate=False).subs(n, i)
        approx += ai * term
        if _print:
            text1.insert(tk.INSERT, 'iteration {}: {} \n'.format(i, N(approx)))

    error_and_graphs(text1,_error, _graph, x, fx, approx, x0, x1, a, b, type_error, name = 'cosine')


def sine_series(text1, f, x0, x1, a=0, b=pi, niter=50, parsefun=False, _error=False, _graph=False, _print=False,
                   type_error='math'):
    x, n, fx = define_input(parsefun, f)

    fn = parse_expr('(sqrt(2/pi)) * sin(n*x)', evaluate=False)

    cn = integrate(fn * fx, (x, a, b))

    coefn = parse_expr('sqrt(2/pi)', evaluate=False)

    bn = coefn * cn

    approx = 0
    for i in range(1, niter + 1):
        bi = bn.subs(n, i)
        term = parse_expr('sin(n*x)', evaluate=False).subs(n, i)
        approx += bi * term
        if _print:
            text1.insert(tk.INSERT, 'iteration {}: {} \n'.format(i, N(approx)))

    error_and_graphs(text1,_error, _graph, x, fx, approx, x0, x1, a, b, type_error, name = 'sine')

def fourier_series(text1, f, x0, x1, a=0, b=pi, niter=50, parsefun=False, _error=False, _graph=False, _print=False,
                   type_error='math'):
    x, n, fx = define_input(parsefun, f)

    fi0 = parse_expr('1/(sqrt(2*pi))', evaluate=False)
    fi_odd = parse_expr('1/(sqrt(pi)) * cos(n*x)', evaluate=False)
    fi_even = parse_expr('1/(sqrt(pi)) * sin(n*x)', evaluate=False)

    c0 = integrate(fi0 * fx, (x, a, b))
    c_impar = integrate(fi_odd * fx, (x, a, b))
    c_par = integrate(fi_even * fx, (x, a, b))

    coef0 = parse_expr('sqrt(2/pi)', evaluate=False)
    coef_odd = parse_expr('sqrt(1/pi)', evaluate=False)
    coef_even = coef_odd

    a0 = coef0 * c0
    an = coef_odd * c_impar
    bn = coef_even * c_par

    approx = a0 / 2
    for i in range(1, niter + 1):
        ai = an.subs(n, i)
        bi = bn.subs(n, i)
        term1 = parse_expr('cos(n*x)', evaluate=False).subs(n, i)
        term2 = parse_expr('sin(n*x)', evaluate=False).subs(n, i)
        approx += ai * term1 + bi * term2
        if _print:
            text1.insert(tk.INSERT, 'iteration {}: {} \n'.format(i, approx))

    error_and_graphs(text1,_error, _graph, x, fx, approx, x0, x1, a, b, type_error, name = '')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
