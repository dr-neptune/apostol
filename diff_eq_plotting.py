import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from typing import Callable, List
from math import sqrt
matplotlib.use('tkAgg')

def concentric_circles(x, y):
    return x**2 + y**2

def add_it_up(x, y):
    return x + y

def translate_it(x, y):
    return 3*x + 2*y**3

def another_one(x, y):
    x, y = abs(x), abs(y)
    return (1/2) * (sqrt(x**2 + 4*y) - x)

def plot_diff_eq(fn: Callable,
                 xlims: List[int] = [-5, 5],
                 ylims: List[int] = [-5, 5]):
    mesh_width = 0.05
    dir_field_x_template = np.linspace(-mesh_width / 2, mesh_width / 2, 100)
    for x in np.arange(xlims[0], xlims[1], mesh_width):
        for y in np.arange(ylims[0], ylims[1], mesh_width):
            curr_slope = fn(x, y)
            curr_intercept = y - curr_slope * x
            dir_field_xs = dir_field_x_template + x
            dir_field_ys = [curr_slope * dfx + curr_intercept for dfx in dir_field_xs]
            plt.plot(dir_field_xs, dir_field_ys, color="mediumpurple")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("dy/dx")
    plt.show()

plot_diff_eq(translate_it, [-2,2], [-2,2])
plot_diff_eq(another_one, [-2,2], [-2,2])
