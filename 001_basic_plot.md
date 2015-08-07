```
"""
A LITTLE BIT LESS BARE BONES

A figure can have a title and the axes can be labeled. It is also possible to 
set the limits for the x and y axes. 

"""

import numpy
import matplotlib
import matplotlib.pyplot as plt

# make some data 
x = numpy.arange(5, 15, 0.1) # start, stop, step
y = numpy.sin(x)

# initialize a figure
plt.figure()

# plot the data
plt.plot(x, y)

# set labels and titles
# you can use LaTeX-labels
plt.xlabel("x")
plt.ylabel("y")
plt.title("sine-function")

# set the minimum and maximum for the axes.
plt.xlim(5, 14)     # min, max
plt.ylim(-0.9, 0.9) # min, max

# show the plot
plt.show()

# save the figure
plt.savefig("../figures/001_basic_plot")

```
![](images/001_basic_plot.png)
