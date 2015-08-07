```python
"""
CONTOUR PLOTS

There are two functions of interest: contour and contourf. The first plots 
contour lines, the second filled contours. Their behavior is very similar.

contour(Z): plot data Z
contour(X,Y,Z): plot data Z and axes X and Y
contour(X,Y,Z, contours = N): as before, use N levels
contour(X,Y,Z, levels = V): as before, levels as from list V

More information is found here:
http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.contour

The examples show contour lines, filled contours and a combination of both. In 
the last example the data exceeds the levels. More information can be found in 
103_contour_extend.


COLORMAPS

You can choose a default color map (an illustrated list can be found here:
http://www.loria.fr/~rougier/teaching/matplotlib/#colormaps ) or you can make 
one yourself. 
http://matplotlib.org/api/colors_api.html#matplotlib.colors.LinearSegmentedColormap


RCPARAMS
matplotlibrc contour.negative_linestyle   if 'linestyles = None' the default is 
  'solid' unless the lines are monochrome. In that case, negative contours will 
  take their linestyle from this setting.

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

# check the shape, if you want
# print(numpy.shape(X), numpy.shape(X))

# construct new color map, this one goes from red to white to blue
cdict = {'red':   [ (0.0,   0.0, 0.0),
                    (0.475, 1.0, 1.0),
                    (0.525, 1.0, 1.0),
                    (1.0,   1.0, 1.0)
                  ],
         'green': [ (0.0,   0.0, 0.0),
                    (0.475, 1.0, 1.0),
                    (0.525, 1.0, 1.0),
                    (1.0,   0.0, 0.0)
                  ],
         'blue':  [ (0.0,   1.0, 1.0),
                    (0.475, 1.0, 1.0),
                    (0.525, 1.0, 1.0),
                    (1.0,   0.0, 0.0)
                  ]
}
rwb_cmap = matplotlib.colors.LinearSegmentedColormap('rwb_colormap', cdict, 256)

# initiate the figure
fig = plt.figure()
ax = [0] * 6
for i in range(6):
    ax[i] = fig.add_subplot(2,3,i+1)

# CONTOUR LINES

# plot the contour lines
ax[0].contour(Z)

# set the contour lines to a single color, note that negative contours are 
# dashed
ax[1].contour(Z, colors = "k")

# use the color map for the contours
ax[2].contour(Z, cmap = rwb_cmap)


# FILLED CONTOURS

# plot the fill
ax[3].contourf(Z)

# use the colormap 
ax[4].contourf(Z, cmap = rwb_cmap)






# FILLED CONTOURS AND CONTOUR LINES

# create custom levels
V = numpy.linspace(-1.5, 1.5, 11)

# plot the filled contours. Note that tx and ty are the axes
ax[5].contourf(tx, ty, Z, V, cmap = rwb_cmap)

# contour lines. With linestyles = "solid", the negative lines are not dashed
ax[5].contour(tx, ty, Z, V, colors = "k", linestyles = "solid")


plt.show()


plt.savefig("../figures/100_contour_plots_colors")












```
![](/figures/100_contour_plots_colors.png)
[Source](/python/100_contour_plots_colors.py)