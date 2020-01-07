#!/usr/bin/env python3

# author: Haim

import matplotlib.pyplot as plt
import numpy as np

start, end, step = 0, 0, -1
file_name = "range"

# default values
default_start = 0
default_end = 4
default_step = 0.1


def check_values(start, end, step):
    """
    Function to check whether start, end and step values are valid
    """

    if start == end:
        print("Start and end values must be different! Using default values")
        start, end = default_start, default_end

    if start > end:
        print("Start value must be greater than end value! Using default values")
        start, end = default_start, default_end

    if step <= 0:
        print("Non-positive value for step argument! Using default value")
        step = default_step


# setting range
try:
    with open(file_name) as fo:
        info = fo.read()
    start, end, step = [float(i) for i in info.split()]
except FileNotFoundError:
    print("File wasn't found! Using default values")
    start, end, step = default_start, default_end, default_step

# sanity check
check_values(start, end, step)

x = np.arange(start*np.pi, end*np.pi, step)
y = np.sin(x)
z = np.cos(x)

xlabel = "x"
title = "Plot of sine and cosine from " + str(start) + "π to " + str(end) + "π"

plt.xlabel(xlabel)
plt.ylabel("sin(x) and cos(x)")
plt.title(title)
plt.legend(["sin(x)", "cos(x)"])

plt.plot(x, y, x, z)
plt.show()
