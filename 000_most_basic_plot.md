```numpy
"""
MOST BASIC PLOT

How to get data on the screen. You really need only three lines:
plt.figure()    # make a matplotlib instance
plt.plot(data)  # plot the data
plt.show()      # show the plot on the screen

If you use plt.plot(data) Matplotlib will make an x-axis from 0 to the number of
elements in data. Give plt.plot(x_axis, data) to define the x-axis yourself.

In both cases Matplotlib automatically determines the ranges that will be 
plotted.

"""

# NumPy is always useful
import numpy
# first load matplotlib
import matplotlib
# then load pyplot
import matplotlib.pyplot as plt

# make some data 
x = numpy.arange(5, 15, 0.1) # start, stop, step
y = numpy.sin(x)

# initialize a figure
plt.figure()

# plot the data
plt.plot(y)
plt.title("Only y is given")

# show the plot
plt.show()

# save the figure
plt.savefig("../figures/000_0_most_basic_plot")

# let's do that again, with x-axis
plt.figure()
plt.plot(x, y)
plt.title("Both x and y are given")
plt.show()

# save the figure
# no extension or file format means the default is used (png)
plt.savefig("../figures/000_1_most_basic_plot")

```
![](/figures/000_0_most_basic_plot.png)
![](/figures/000_1_most_basic_plot.png)
