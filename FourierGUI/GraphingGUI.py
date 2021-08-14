import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from sympy import *
import scipy.integrate as integratesci
from sympy.utilities.lambdify import lambdify, implemented_function
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import scipy.integrate as integrate
import scipy.special as special


def graph_simple(x, fx, approx, x0, x1):
    p1 = approx
    p2 = fx
    p = plot(p1, p2, (x, x0, x1), show=false)
    # change the color of p2
    p[1].line_color = 'r'
    p.show()


def graph_data(fx,approx,x0,x1, name = ''):
    step = (x1-x0)/100
    xs = np.arange(x0, x1+1, step).astype(float)

    tf1 = translate(fx)
    tf2 = translate(approx)
    f_orig = tf1(xs)
    f_approx = tf2(xs)


    root = tk.Tk()
    figure1 = plt.Figure(figsize=(5, 4), dpi=100)
    ax1 = figure1.add_subplot(111)
    scatter1 = FigureCanvasTkAgg(figure1, root)
    scatter1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax1.set_xlabel('x')
    ax1.set_title('Approximation of f(x) using fourier series')
    ax1.plot(xs,f_orig,label='f(x)')
    ax1.plot(xs,f_approx,label = 'Fourier ' + name + ' series')
    leg = ax1.legend();

    root.mainloop()


def translate(sympyf):
    x = symbols("x")
    f = lambdify(x, sympyf, 'numpy')
    return f

