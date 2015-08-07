"""
SUBPLOTS, A BIT MORE ADVANCED

Here we give two examples of what you can do when adding subplots. In the first 
example (left) we see how we can be creative with the columns and rows of the 
subplots. 

The example on the right shows how we can change the positioning of subplots 
relative to the figure and to each other using fig.subplots_adjust(). The values 
are relative to the figure. The lower left corner is (0,0), the upper right 
corner is (1,1). If top=1.1, it would extend above the upper limit of the 
figure. 

Note that the tick labels and the labels are outside of these limits. When you 
resize the figure, the space between the plots will change (because it is 
relative) but the labels will not. When you make it too small, labels will 
overlap the other axes. 

ASPECT RATIO

The plot on the right also shows the effect of using 'add_subplot(aspect = 
"equal")'. Normally when resizing a figure, xlim and ylim (whether set 
explicitly or not) is kept and the aspect ratio changes. Use 'add_subplot(aspect 
= "equal")' or 'add_subplot(aspect = num)' to get a fixed aspect ratio. (same 
for add_axes) 
http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.set_aspect

RCPARAMS:
'figure.subplot' sets the defaults for subplots_adjust
subplots_adjust(left    = 0.125, 
                bottom  = 0.1, 
                right   = 0.9, 
                top     = 0.9, 
                wspace  = 0.2, 
                hspace  = 0.2)

"""


import numpy
import matplotlib
import matplotlib.pyplot as plt

# make some data 
x = numpy.arange(5,15,0.1) # start, stop, step
y = numpy.sin(x)
z = numpy.cos(x)

# make the figure object
fig = plt.figure()

# make the axes objects
ax = [0] * 3

# 1 row, 2 colums, position 1: whole left part
ax[0] = fig.add_subplot(1, 2, 1) 
# 2 rows, 2 colums, position 2: upper right corner
ax[1] = fig.add_subplot(2, 2, 2) 
# 2 rows, 2 colums, position 4: lower right corner
ax[2] = fig.add_subplot(2, 2, 4) 

# plot some data
ax[0].plot(x,y)
ax[0].plot(x,z)
ax[1].plot(x,y)
ax[2].plot(x,z)

# titles and labels
ax[0].set_title("Axes 1: (1,2,1)")
ax[1].set_title("Axes 2: (2,2,2)")
ax[2].set_title("Axes 3: (2,2,4)")
ax[2].set_ylabel("An overlapping y-label")

plt.show()

plt.savefig("../figures/022_0_subplots_add_subplots")



# make the figure object
fig = plt.figure()

# make the axes objects
ax = [0] * 3

# move the left edge of the plots, increase the height between subplots
fig.subplots_adjust(left=0.4, bottom=None, right=None, top=None, wspace=None, 
    hspace=0.5)

# for the first one, fix the aspect ratio
ax[0] = fig.add_subplot(1, 2, 1, aspect = "equal")
ax[1] = fig.add_subplot(2, 2, 2) 
ax[2] = fig.add_subplot(2, 2, 4) 

# plot some data
ax[0].plot(x,y)
ax[0].plot(x,z)
ax[1].plot(x,y)
ax[2].plot(x,z)

# titles
ax[0].set_title("Axes 1: (1,2,1)\naspect = 'equal'")
ax[1].set_title("Axes 2: (2,2,2)")
ax[2].set_title("Axes 3: (2,2,4)")

plt.show()

plt.savefig("../figures/022_1_subplots_add_subplots")