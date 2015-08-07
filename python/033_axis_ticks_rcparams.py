"""
AXIS RCPARAMS

rcParams can be used to change defaults. Very similar to 002_rcparams.

Note: When using Python 3.3 on a Mac, Matplotlib will truncate strings (like 
labels and titles).
"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

plt.close("all")

# make some data 
x = numpy.arange(0,10,0.1) # start, stop, step
y = numpy.sin(x)


# axes (spine) linewidth 
# two notations, same effect
matplotlib.rc('axes', linewidth = 4)
matplotlib.rcParams['axes.linewidth'] = 4

# make the ticks longer
matplotlib.rcParams['ytick.major.size'] = 10
# move the tick labels away from the axes
matplotlib.rcParams['ytick.major.pad'] = 10
# make ticks and tick labels red
matplotlib.rcParams['ytick.color'] = "r"
# change the font size
matplotlib.rcParams['font.size'] = 24

# make the figure object, the axes, and plot something
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y)
ax.set_title("Changing rcParams")
ax.text(x=5, y=0, s = "text")

plt.show()
plt.savefig("../figures/033_axis_rcparams")

# go back to defaults
matplotlib.rcdefaults()