"""
SPINES

Spines are the borders of the data. The left plot shows the default situation, 
the right plot is somewhat customized. The colors of the spines are changed, the 
spines have moved a bit. 

If you want to change all spines, you can use rcParams, otherwise you should use 
on of the methods below.


RCPARAMS:
'axes.edgecolor' spine color
'axes.linewidth' spine line width (set to zero to remove the spine)

Full list of functions: http://matplotlib.org/api/spines_api.html

"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

plt.close("all")

# make some data 
x = numpy.arange(0,10,0.1) # start, stop, step
y = numpy.sin(x)

# make the figure object
fig = plt.figure()
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.3, 
    hspace=None)
ax = [0] * 2
for i in range(2):
    ax[i] = fig.add_subplot(1,2,i+1)
    ax[i].plot(x,y)

ax[0].set_title("Default")
ax[1].set_title("Customized")

# set the color of the top and bottom spine
ax[1].spines['top'].set_color("r")
ax[1].spines['bottom'].set_color("g")

# move the left axis relative to the axes instance. Ie. 0 is the left edge 
# (normal position), 1 is the right edge. -0.1 means 10% to the left
ax[1].spines['left'].set_position(("axes", -0.1))

# move the right axis relative to the data in the axes
# does this work correctly? It should be at x-axis is 11, but it looks more like 
# 12
ax[1].spines['right'].set_position(("data", 11))


# you can also iterate over spines
for loc, spine in ax[1].spines.items():
    # use ax[1].spines.iteritems() in Python 2
    
    # change linewidth of bottom and top spine
    # note that the spines also get wider. 
    if loc in ['bottom', 'top']:
        spine.set_linewidth(4)

plt.show()

plt.savefig("../figures/031_axis_spines")