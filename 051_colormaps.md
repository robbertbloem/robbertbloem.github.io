```python
"""
COLORMAPS

A colormap is a dictionary for the RGB values. For each color, a list of tupples 
gives the different segments. Each segment is a point along the z-axis, ranging 
from 0 to 1. The colors for the levels is interpolated from these segments.

segment z-axis  end      start
i       z[i]    v0[i]    v1[i]
i+1     z[i+1]  v0[i+1]  v1[i+1]   
i+2     z[i+2]  v0[i+2]  v1[i+2]   

Levels between z[i] and z[i+1] will have colors between v1[i] and v0[i+1] etc. 
This makes it possible to 'jump' colors. v0[0] and v1[-1] are not used. 

Note:
I use contour plots to demonstrate the colormaps. 
http://matplotlib.org/examples/api/colorbar_only.html

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
ax = [0] * 4
for i in range(4):
    ax[i] = fig.add_subplot(2,2,i+1)


# colormap with jumping colors
cdict = {'red':   [ (0.0,   0.0, 0.0),
                    (0.5,   1.0, 0.0), # jump
                    (1.0,   1.0, 0.0),
                  ],
         'green': [ (0.0,   0.0, 0.0),
                    (1.0,   0.0, 0.0)
                  ],
         'blue':  [ (0.0,   0.0, 0.0),
                    (1.0,   0.0, 0.0)
                  ]
}
test_cmap = matplotlib.colors.LinearSegmentedColormap('test_colormap', cdict, 256)

# contour lines
CP1 = ax[0].contour(tx, ty, Z, cmap = test_cmap)
cbar = fig.colorbar(CP1, ax=ax[0])

# filled contours
CP2 = ax[1].contourf(tx, ty, Z, cmap = test_cmap)
cbar = fig.colorbar(CP2, ax=ax[1])

# colormap that has been used before
cdict = {'red':   [ (0.0,   0.0, 0.0),
                    (0.475, 1.0, 1.0),
                    (0.525, 1.0, 1.0),
                    (1.0,   1.0, 1.0)
                  ],
         'green': [ (0.0,   0.0, 0.0),
                    (0.475, 1.0, 1.0),
                    (0.525, 1.0, 1.0),
                    (1.0,   0.65, 0.0)
                  ],
         'blue':  [ (0.0,   1.0, 1.0),
                    (0.475, 1.0, 1.0),
                    (0.525, 1.0, 1.0),
                    (1.0,   0.0, 0.0)
                  ]
}
rwb_cmap = matplotlib.colors.LinearSegmentedColormap('rwb_colormap', cdict, 256)

# contour lines
CP3 = ax[2].contour(tx, ty, Z, cmap = rwb_cmap)
cbar = fig.colorbar(CP3, ax=ax[2])

# filled contours
CP4 = ax[3].contourf(tx, ty, Z, cmap = rwb_cmap)
cbar = fig.colorbar(CP4, ax=ax[3])

# set titles
ax[0].set_title("Red jump")
ax[1].set_title("Red jump")
ax[2].set_title("RWB")
ax[3].set_title("RWB")

plt.show()
plt.savefig("../figures/051_colormaps")

```
![](/figures/051_colormaps.png)
[Source](/python/051_colormaps.py)