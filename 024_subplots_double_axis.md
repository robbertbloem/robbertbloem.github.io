```python
"""
TWO X OR Y AXES IN ONE SUBPLOT

You can make a second x or y axis using the twinx() (make a new y-axis) and 
twiny() (make a new x-axis). 

I miss the logic why twinx() makes a y-axis, which is the reason I started these 
tutorials - as a reference for myself.

Note that I used some fancy coloring of the axes, which will be discussed later 
in example 031. 

"""

import numpy
import matplotlib
import matplotlib.pyplot as plt


x = numpy.arange(0,10,0.1) 
y = numpy.sin(x)
z = numpy.sqrt(x)

# make the figure object
fig = plt.figure()

# create some horizontal space
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.4, 
    hspace=None)

# twinx and twiny create a new axes instance, for two plots we need four axes
# instances
ax = [0] * 4

# make the left plot
ax[0] = fig.add_subplot(1, 2, 1)
# make the new y axis
ax[1] = ax[0].twinx()

# make the right plot
ax[2] = fig.add_subplot(1, 2, 2)
# make the new x-axis
ax[3] = ax[2].twiny()

# plot some data
# because we work in different axes instances, the color cycling does not work
ax[0].plot(x,y, c = "b")
ax[1].plot(x,z, c = "r")
ax[2].plot(x,y, c = "b")
ax[3].plot(x,z, c = "r")

# set some limits
ax[3].set_xlim(0,1) # will only affect ax[3]
ax[3].set_ylim(-1,1) # will also affect ax[2], because they share this axis

# set the title
ax[0].set_title("twinx()")
ax[2].set_title("twiny()")

# use colors to make it more clear, see example 031
ax[0].tick_params(axis='y', colors="b")
ax[1].tick_params(axis='y', colors="r")
ax[2].tick_params(axis='x', colors="b")
ax[3].tick_params(axis='x', colors="r")

plt.show()

plt.savefig("../figures/024_subplots_double_axis")




```
![](/figures/024_subplots_double_axis.png)
[Source](/python/024_subplots_double_axis.py)