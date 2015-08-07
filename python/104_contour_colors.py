"""
COLORMAPS

A colormap is a dictionary for the RGB values. For each color, a list of tupples gives the different segments. Each segment is a point along the z-axis, ranging from 0 to 1. The colors for the levels is interpolated from these segments.

segment z-axis  end      start
i       z[i]    v0[i]    v1[i]
i+1     z[i+1]  v0[i+1]  v1[i+1]   
i+2     z[i+2]  v0[i+2]  v1[i+2]   

Levels between z[i] and z[i+1] will have colors between v1[i] and v0[i+1] etc. This makes it possible to 'jump' colors. v0[0] and v1[-1] are not used. 


"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

plt.close("all")

fig = plt.figure()
ax = fig.add_subplot(111)



CM1 = matplotlib.cm.get_cmap("summer")

# X = matplotlib.cm.ScalarMappable(cmap = CM1)
# 
# X.set_colorbar(fig, ax)
# cbar = fig.colorbar(X, ax=ax, ticks = None)



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

# use a colormap included in Matplotlib
CM1 = matplotlib.cm.get_cmap("summer")
ax[0].contour(tx, ty, Z, cmap = CM1)

V = [-1.8, -0.9, 0, 0.9, 1.8]
C = ["r", "g", "y", "b", "m"]
for i in range(len(V)):
    ax[1].contour(tx, ty, Z, levels = [V[i]], colors = C[i])





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

ax[2].contour(tx, ty, Z, cmap = test_cmap)


# colormap that has been used before
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

ax[3].contour(tx, ty, Z, cmap = rwb_cmap)




ax[0].set_title("Included: Summer")
ax[1].set_title("Self constructed color map")
ax[2].set_title("Self constructed color map")
ax[3].set_title("Color levels individually")














plt.show()


# plt.savefig("../figures/100_contour_plots_colors")











