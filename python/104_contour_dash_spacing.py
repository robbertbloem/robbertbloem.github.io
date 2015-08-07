"""
CONTOUR PLOTS DASH SPACING AND LINE WIDTH

Each contour level in a contour plot is a LineCollection: a collection of lines. Editing properties of one such collection is different than changing properties of Line2D instance in linear plots. There are less options and we'll need to find the contour we want to change.

The Axes.get_children() function lists all the elements of the plot: Spines, Axis, some other stuff and a few objects labeled as '<matplotlib.collections.LineCollection object at 0x48ccb70>'. Each of these is one contour level. It seems they are ordered in the way of 'levels' (the default is from minimum to maximum). 

For each of these children we can look at a limited number of properties: line width and line style. Using set_linestyle() and set_linewidth() we can change these properties. In order to change the spacing of the dashes use set_dashes([(offset, (on, off))]). 


MORE INFO:
http://matplotlib.org/api/collections_api.html#matplotlib.collections.LineCollection

http://matplotlib.org/api/collections_api.html#matplotlib.collections.Collection

"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

plt.close("all")

# make some data: a 2D grid
tx = numpy.arange(5,15,0.1)
ty = numpy.arange(10,20,0.1)
x = numpy.sin(tx)
y = numpy.cos(ty)
X, Y = numpy.meshgrid(x, y)
Z = X + Y


# initiate the figure
fig = plt.figure()
ax = [0] * 2
for i in range(2):
    ax[i] = fig.add_subplot(1,2,i+1)

ax[0].contour(tx, ty, Z, colors = "k")


CP = ax[1].contour(tx, ty, Z, colors = "k")

for axc in ax[1].get_children():
    # print(axc)
    try:
        # print("Dashes:", axc.get_dashes())
        if axc.get_linestyles()[0][0] == 0: 
            axc.set_dashes([(0, (10.0, 5.0))])
            axc.set_linewidth(2)
            
    except:
        pass

ax[0].set_title("Default")
ax[1].set_title("Changed")


















plt.show()


# plt.savefig("../figures/100_contour_plots_colors")











