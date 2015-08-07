```python
"""
COLORS

When you plot more data sets in a single plot, each line will get a different 
color according to the table below. By default, the first line in a plot is 
always blue, the second green, the seventh black. The eight line is blue again. 
Line colors can be manually set using c or color and the full name or single 
letter.

The basic colors can be called by a single letter (this is also the default 
order for cycling the colors (white is not used)):
b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white

RCPARAMS:
'axes.color_cycle' sets the order and colors for the color cycling
'lines.color' does not set the line color, it is overriden by the color_cyle

"""

import numpy
import matplotlib
import matplotlib.pyplot as plt

# list all colors
# print(matplotlib.colors.cnames)

# make some data 
x = numpy.arange(5,15,0.1) # start, stop, step
y = numpy.sin(x)
z = numpy.cos(x)

# default line coloring
plt.figure()
plt.plot(x, y) # blue
plt.plot(x, z) # green
plt.title("default coloring")
plt.show()
plt.savefig("../figures/010_0_line_properties_colors_default")

# set line colors manually
plt.plot(x, y, c = "cyan") 
plt.plot(x, z, color = "y") 
plt.title("manual coloring")
plt.show()
plt.savefig("../figures/010_1_line_properties_colors_manual")


```
![](/figures/010_0_line_properties_colors_default.png)
![](/figures/010_1_line_properties_colors_manual.png)
