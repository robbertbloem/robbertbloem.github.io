"""
CONTOUR PLOT LEGENDS

There are two sorts of legends: inline and a colorbar. 

Examples:
Left: inline and colorbar
Middle: colorbar horizontally positioned and labeled.
Right: colorbar contains the filled contours and contour lines. 

Note: When using Python 3.3 on a Mac, Matplotlib will truncate strings (like 
labels and titles).
"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

# make some data: a 2D grid
tx = numpy.arange(5,15,0.1)
ty = numpy.arange(10,20,0.1)
x = numpy.sin(tx)
y = numpy.cos(ty)
X, Y = numpy.meshgrid(x, y)
Z = X + Y

# initiate the figure
fig = plt.figure()
ax = [0] * 3
for i in range(3):
    ax[i] = fig.add_subplot(1,3,i+1)

# CONTOUR LINES
CP1 = ax[0].contour(Z)
# colorbar, default position
fig.colorbar(CP1, ax=ax[0])
# inline labels of the contours
plt.clabel(CP1)


# FILLED CONTOURS
# make plot
CP2 = ax[1].contourf(Z)
# add colorbar, horizontally oriented
cbar = fig.colorbar(CP2, ax=ax[1], orientation = "horizontal")
# set a label
cbar.ax.set_xlabel('Colorbar label')

# FILLED CONTOURS AND CONTOUR LINES
# make plot
CP3F = ax[2].contourf(Z, cmap = plt.cm.winter)
CP3L = ax[2].contour(Z, cmap = plt.cm.prism)
# add colorbar for fill
cbar = fig.colorbar(CP3F, ax=ax[2], ticks = None)
# add contour lines to the color bar
cbar.add_lines(CP3L)

plt.show()

plt.savefig("../figures/101_contour_plots_legends")
