```numpy
"""
LINE WIDTH

Default linewidth is 1. This can be changed using the 'linewidth' or 'lw' 
argument.

Note that the line width is absolute. When you resize the figure the line width 
remains the same. This is good if you have too much data and the plot is 
cluttered, but bad when you want to retain the look of the plot.

RCPARAMS:
lines.linewidth     1   # sets the default linewidth

"""

import numpy
import matplotlib
import matplotlib.pyplot as plt

# make some data 
x = numpy.arange(5,15,0.1) # start, stop, step
y = numpy.sin(x)
z = numpy.cos(x)

# change the linewidth
plt.figure()
plt.plot(x, y, linewidth = 2)
plt.plot(x, z, lw = 4)
plt.title("Different line widths")
plt.show()
plt.savefig("../figures/012_line_properties_linewidth")

```
![](/figures/012_line_properties_linewidth.png)
