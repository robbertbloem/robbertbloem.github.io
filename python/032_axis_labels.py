"""
AXIS LABELS

A lot of what you can do with labels is also covered in the bit about text as 
the options are largely similar. Possibly most interesting is the ability to 
change the position relative to the axis. 

http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.set_xlabel

RCPARAMS:
'axes.labelcolor'   k       
'axes.labelsize'    medium  # medium is a relative size

"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

# make some data 
x = numpy.arange(0,10,0.1) # start, stop, step
y = numpy.sin(x)

# make the figure object, the axes, and plot something
fig = plt.figure()
ax = [0] * 2
for i in range(2):
    ax[i] = fig.add_subplot(1,2,i+1)
    ax[i].plot(x,y)

# set titles
ax[0].set_title("Default")
ax[1].set_title("Customized")

ax[0].set_xlabel("x-label")
ax[0].set_ylabel("y-label")

# http://matplotlib.org/api/font_manager_api.html#matplotlib.font_manager.FontProperties
fp = matplotlib.font_manager.FontProperties(family = "serif")

# labelpad is the distance between the axis and the label
# note that latex is a smaller font
ax[1].set_xlabel("x-label in serif",    # string
    labelpad = 20,                      # move it away from the axis
    fontproperties = fp,                # give font properties object
    backgroundcolor = "y",              # background xolor
    color = "r"                         # text color - to hurt your eyes
)
ax[1].set_ylabel(r"y-label with a $latex$ twist", labelpad = -20)

plt.show()

plt.savefig("../figures/032_axis_labels")