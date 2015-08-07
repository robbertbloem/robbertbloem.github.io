```python
"""
CONTOUR PLOTS LEVELS

The levels in contour plots can be set automatically (default is 6), it can be 
set using the 'contours' keyword and you can set the explicit levels. 

"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

plt.close("all")

# define color map
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
    ax[i] = fig.add_subplot(2,2,i+1)
    
# no number of contours given
ax[0].contourf(tx, ty, Z, cmap = rwb_cmap)
ax[0].contour(tx, ty, Z, colors = "k")

# number of contours given
ax[1].contourf(tx, ty, Z, contours = 6, cmap = rwb_cmap)
ax[1].contour(tx, ty, Z, contours = 6, colors = "k")

# list with contour levels given
V = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
ax[2].contourf(tx, ty, Z, levels = V, cmap = rwb_cmap)
ax[2].contour(tx, ty, Z, levels = V, colors = "k")

plt.show()

plt.savefig("../figures/102_contour_plots_levels")
```
![](/figures/102_contour_plots_levels.png)
[Source](/python/102_contour_levels.py)