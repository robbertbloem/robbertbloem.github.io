```python
"""
AXIS RCPARAMS 

rcParams allows you to set the defaults. This is actually quite advanced (I only 
got in contact with it when I wrote those tutorials), but we will encounter it 
all over the place. 

Use one of the following two methods:
matplotlib.rcParams['group.key'] = value
matplotlib.rc('group', key1 = value1, key2 = value2)

Some of the groups are listed below:
"axes": face color (background), edge color (spine color), edge linewidth, 
labels, color cycle order, relative title size
"xtick"/"ytick": padding, tick size, label size, tick direction (in/out) 
"font": font size, style, weight, family: labels, tick labels, titles, text
"text": mostly latex related
"lines": line width and style, markers, colors
"figure": subplot_adjust defaults, figure size, color, dpi
"legend": spacing, 
"savefig": colors, dpi, extension
"grid":
"path":
"keymap":
"patch":
"image":

Each group has some keys. For example both "axes" and "lines" have a linewidth 
key. Every key has a value.

When using iPython, the new settings are stored for further plots. Reset to 
defaults using 'matplotlib.rcdefaults()'

MORE INFO:
A full list with parameters can be found here: 
http://matplotlib.org/users/customizing.html#a-sample-matplotlibrc-file
but I found that some keys are not used anymore. Below is a simple function that 
prints keys and values for a given group.


NOTE:
When using Python 3.3 on a Mac, Matplotlib will truncate strings (like labels 
and titles).
"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

# close all plots (useful with iPython)
plt.close("all")

# see values for keyword
# use "" to see all keys
dic = matplotlib.rcParams
group = "font" 
for key in dic:
    if group in key:
        print(key, dic[key])

# make some data 
x = numpy.arange(0, 10, 0.1) # start, stop, step
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
# all plotted lines will have a default linewidth of 2
matplotlib.rcParams['lines.linewidth'] = 2

# make the figure object, the axes, and plot something
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_title("Changing rcParams")
ax.text(x = 5, y = 0, s = "text")

plt.show()

plt.savefig("../figures/002_rcparams")

# go back to defaults
matplotlib.rcdefaults()
```
![](/figures/002_rcparams.png)
