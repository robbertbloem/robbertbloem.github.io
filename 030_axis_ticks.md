```python
"""
AXIS TICKS

The ticks can be changed. The tick positions and labels can be set directly. 
Other options are found in the tick_params() function. You have to say which 
axis ('x', 'y' or 'both') and which ticks ('major', 'minor' or 'both') you want 
to change. A list with all the parameters can be found here:
http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.tick_params

Finally, you can change the rcParams. Below is the list for group = 'xtick' and 
the default values:
'xtick.minor.pad'    4  # distance from the axes
'xtick.direction'    in # pointing into the graph
'xtick.minor.size'   2
'xtick.color'        k
'xtick.major.pad'    4  
'xtick.major.size'   4
'xtick.labelsize'    medium

Note: When using Python 3.3 on a Mac, Matplotlib will truncate strings (like 
labels and titles).
"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

plt.close("all")

x = numpy.arange(0, 10, 0.1) 
y = numpy.sin(x)

fig = plt.figure()
ax = [0] * 2
for i in range(2):
    ax[i] = fig.add_subplot(1, 2, i+1)
    ax[i].plot(x, y)

ax[0].set_title("Default")
ax[1].set_title("Customized")




# Change the POSITIONS of x-ticks. It defaults to the major ticks, unless you 
# use the flag minor = True
ax[1].set_xticks([0, numpy.sqrt(2), 5, 7, 10])  # major, x
ax[1].set_yticks([-1, 0, 1])                    # major, y
ax[1].set_yticks([-0.5, 0.5], minor = True)     # minor, y

# It will automatically set LABELS for major ticks. You can set custom labels 
# for the ticks. Note:
# - the label can be an integer (0) or a string ("5")
# - the second label uses latex for sqrt(2) 
# - the empty label for 7
ax[1].set_xticklabels(
    [0, r"$\sqrt{2}$", "5", "", "bla"], # labels
    fontsize = 20,                      # fontsize
    color = "g",                        # color, only for the labels, not ticks
    rotation = 30                       # rotation in degrees
)
# again, use minor = True to affect those labels
ax[1].set_yticklabels(["A", "B"], minor = True)

# change TICK PARAMETERS
# change color to red for major and minor y 
# note that color of both ticks and labels change
ax[1].tick_params(axis = 'y', which = "both", colors = "r")
# change the length to 20 (points?) for major ticks of x and y
ax[1].tick_params(axis = 'both', which = "major", length = 20)
# give minor y ticks 
ax[1].tick_params(axis = 'y', which = "minor", 
    width = 5, 
    length = 5, 
    direction = "out"
)

plt.show()

plt.savefig("../figures/030_axis_ticks")
```
![](/figures/030_axis_ticks.png)
[Source](/python/030_axis_ticks.py)