# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from sympy import *

from sympy.parsing.sympy_parser import parse_expr
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


def cosine_series(Scrolledtext1,f, x0, x1, a=0, b=pi, niter=50, parsefun = False ):
    x, n = symbols("x,n")
    if parsefun:
        fx = parse_expr(f, evaluate=False)
    else:
        fx = f

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
        Scrolledtext1.insert(tk.INSERT,'iteration {}: {} \n'.format(i, N(approx)))

    p1 = approx
    p2 = fx
    p = plot(p1, p2, (x, x0, x1), show=false)
    # change the color of p2
    p[1].line_color = 'r'
    p.show()


def sine_series(Scrolledtext1, f, x0, x1, a=0, b=pi, niter=50, parsefun = False ):
    x, n = symbols("x,n")
    if parsefun:
        x, n = symbols("x,n")
        fx = parse_expr(f, evaluate=False)
    else:
        fx = f

    fn = parse_expr('(sqrt(2/pi)) * sin(n*x)', evaluate=False)

    cn = integrate(fn * fx, (x, a, b))

    coefn = parse_expr('sqrt(2/pi)', evaluate=False)

    bn = coefn * cn

    approx = 0
    for i in range(1, niter + 1):
        bi = bn.subs(n, i)
        term = parse_expr('sin(n*x)', evaluate=False).subs(n, i)
        approx += bi * term
        Scrolledtext1.insert(tk.INSERT,'iteration {}: {} \n'.format(i, N(approx)))

    p1 = approx
    p2 = fx
    p = plot(p1, p2, (x, x0, x1), show=false)
    # change the color of p2
    p[1].line_color = 'r'
    p.show()



def fourier_series(Scrolledtext1,f, x0, x1, a=-pi, b=pi, niter=50, parsefun = False ):
    x, n = symbols("x,n")
    init_printing(use_unicode=False, wrap_line=False, no_global=True)
    if parsefun:
        x, n = symbols("x,n")
        fx = parse_expr(f, evaluate=False)
    else:
        fx = f

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
        Scrolledtext1.insert(tk.INSERT,'iteration: {} {} \n'.format(i, approx))

    # Defined the function to be differentiated

    p1 = approx
    p2 = fx
    p = plot(p1, p2, (x, x0, x1), show=false)
    # change the color of p2
    p[1].line_color = 'r'
    p.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #x, n = symbols("x,n")
    #f1 = -2/pi * x
    #f2 = 2/pi * x - 1
    #cond1 = ((x > 0) & (x < pi /2 ))
    #cond2 = ((x >= pi/2) & (x < pi ))
    #f = Piecewise((f1, cond1),(f2, cond2))

    f = 'Piecewise((-2/pi * x, ((x > 0) & (x < pi /2 ))),(2/pi * x - 1, ((x >= pi/2) & (x < pi ))))'
    #sine_series(f,-3*pi,3*pi,niter=50)
    cosine_series(f, -3 * pi, 3 * pi, niter=50, parsefun= True)
    #fourier_series('x**2',-3*pi,3*pi,niter=50)
    #cosine_series('x', 0, 7, niter=50)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
