# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:39:31 2019

@author: z3372528
"""

from matplotlib import pyplot as plt

x_totals = list()
y_totals = list()

def func(x):
    y = 3*x**2-10*x**3-2*x**4 + 30
    return y

def guess(x):
    x_totals.append(x)
    y = func(x)
    y_totals.append(y)
    print("A guess of " + str(x) + " returns " + str(y))
    plt.scatter(x_totals, y_totals)
    plt.show()
    return 

