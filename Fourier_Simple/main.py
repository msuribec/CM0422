# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from sympy import *
from sympy.parsing.sympy_parser import parse_expr

from error_graphs import error_and_graphs
from error_graphs import loglog_plot

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


def cosine_series(f, x0, x1, a=0, b=pi, niter=50, parsefun=True, _error=False, _graph=False, _print=False,
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
            print('iteration {}: {} \n'.format(i, N(approx)))

    return error_and_graphs(_error, _graph, x, fx, approx, x0, x1, a, b, type_error)


def sine_series(f, x0, x1, a=0, b=pi, niter=50, parsefun=True, _error=False, _graph=False, _print=False,
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
            print('iteration {}: {} \n'.format(i, N(approx)))

    return error_and_graphs(_error, _graph, x, fx, approx, x0, x1, a, b, type_error)


def fourier_series(f, x0, x1, a=-pi, b=pi, niter=50, parsefun=True, _error=False, _graph=False, _print=False,
                   type_error='math'):
    x, n, fx = define_input(parsefun, f)

    fi0 = parse_expr('1/(sqrt(2*pi))', evaluate=False)
    fi_impar = parse_expr('1/(sqrt(pi)) * cos(n*x)', evaluate=False)
    fi_par = parse_expr('1/(sqrt(pi)) * sin(n*x)', evaluate=False)

    c0 = integrate(fi0 * fx, (x, a, b))
    c_impar = integrate(fi_impar * fx, (x, a, b))
    c_par = integrate(fi_par * fx, (x, a, b))

    coef0 = parse_expr('sqrt(2/pi)', evaluate=False)
    coef_impar = parse_expr('sqrt(1/pi)', evaluate=False)
    coef_par = coef_impar

    a0 = coef0 * c0
    an = coef_impar * c_impar
    bn = coef_par * c_par

    approx = a0 / 2
    for i in range(1, niter + 1):
        ai = an.subs(n, i)
        bi = bn.subs(n, i)
        term1 = parse_expr('cos(n*x)', evaluate=False).subs(n, i)
        term2 = parse_expr('sin(n*x)', evaluate=False).subs(n, i)
        approx += ai * term1 + bi * term2
        if _print:
            print('iteration {}: {} \n'.format(i, approx))

    return error_and_graphs(_error, _graph, x, fx, approx, x0, x1, a, b, type_error)



def error_analysis(name,nums,f, x0, x1, parsefun= True, _error= True):
    errs = []
    for n in nums:
        if name == 'cosine':
            er = cosine_series(f, x0, x1, niter= n, parsefun = parsefun, _error= True)
        elif name == 'sine':
            er =sine_series(f, x0, x1, niter= n, parsefun = parsefun, _error= True)
        else:
            er = fourier_series(f, x0, x1, niter= n, parsefun = parsefun, _error= True)
        errs.append(er)

    loglog_plot(nums,errs, name)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Ejemplo 1
    #f = 'Piecewise((-2/pi * x, ((x > 0) & (x < pi /2 ))),(2/pi * x - 1, ((x >= pi/2) & (x < pi ))))'
    #cosine_series(f, -3 * pi, 3 * pi, niter=50, _error=True, _print=True, _graph=True, type_error='math')


    f  = 'Piecewise((-2/pi * x, ((x > 0) & (x < pi /2 ))),(2/pi * x - 1, ((x >= pi/2) & (x < pi ))))'
    error_analysis('sine',[2,5,10,20,40],f, -3*pi, 3*pi)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
