#!/usr/bin/env python3

# author: Haim

import sys
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

    return start, end, step


def load_args_from_file():
    """
    Loading arguments values from file, or default values if file
    doesn't exist
    """

    try:
        with open(file_name) as fo:
            info = fo.read()
        start, end, step = map(float, info.split())
    except FileNotFoundError:
        print("File wasn't found! Using default values")
        start, end, step = default_start, default_end, default_step

    return start, end, step


# setting arg values
if len(sys.argv) == 1:
    start, end, step = load_args_from_file()
elif len(sys.argv) != 4:
    print("Wrong argument number!\n Usage: start, end, step\n Using default values")
    start, end, step = default_start, default_end, default_step
else:
    sys.argv.pop(0)
    start, end, step = map(float, sys.argv)
    print(start, end, step)

# sanity check
start, end, step = check_values(start, end, step)

x = np.arange(start*np.pi, end*np.pi, step)
y = np.sin(x)
z = np.cos(x)

xlabel = "x"
title = "Plot of sine and cosine from " + \
    str(start) + "π to " + str(end) + "π" + " in " + str(step) + " steps"

plt.xlabel(xlabel)
plt.ylabel("sin(x) and cos(x)")
plt.title(title)
plt.legend(["sin(x)", "cos(x)"])

plt.plot(x, y, x, z)
plt.show()
