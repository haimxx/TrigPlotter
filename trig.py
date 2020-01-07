#!/usr/bin/env python3

#author: Haim

import matplotlib.pyplot as plt
import numpy as np

# setting range
start = 0
end = 4*np.pi
step = 0.1

x = np.arange(start, end, step)
y = np.sin(x)
z = np.cos(x)

xlabel = 'x values from ' + str(start) + ' to ' + str(end)
title = 'Plot of sin and cos from ' + str(start) + ' to ' + str(end)

plt.xlabel(xlabel)
plt.ylabel('sin(x) and cos(x)')
plt.title(title)
plt.legend(['sin(x)', 'cos(x)'])

plt.plot(x, y, x, z)
plt.show()
