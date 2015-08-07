"""
CONTOUR PLOTS, EXTEND

When no list of levels is given, the colormap will be scaled to the data, ie. 
all data will be plotted.
When a list is given, it will plot those contours. The 'extend' argument changes
the behavior when the data exceeds the levels of this list. Options are: 
'neither', 'both', 'min', 'max'. The examples below show how these affect the 
plots.


For my work, we look at light absorption differences. We plot data from 
'absorption' (blue) to 'negative absorption' (=transmission :), red). The zero-
level is no absorption. It is important that the color maps behave well around 
zero. 

The number of contours defines the number of contour lines. For N contours, 
there will be N-1 filled contour levels.
An even number of contour levels (for example [-1.5, -0.5, 0.5, 1.5]) will give 
an odd number of filled contours (here: red, white and blue). An odd number of 
contour levels (for example [-1,0,1]) will give two contours (here: red and 
blue). 
When N = odd the noise for absorption is approx 0 will be visible. 

Note: When using Python 3.3 on a Mac, Matplotlib will truncate strings (like 
labels and titles).
"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

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

# list with possibilities for extend
extends = ["neither", "both", "min", "max"]

# make some data: a 2D grid
tx = numpy.arange(5,15,0.1)
ty = numpy.arange(10,20,0.1)
x = numpy.sin(tx)
y = numpy.cos(ty)
X, Y = numpy.meshgrid(x, y)
Z = X + Y

# create the different levels
V = [
    [-1.5, -0.5, 0.5, 1.5],                 # Data < levels (odd)
    [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5],      # Data > levels (odd)
    [-1.4, -0.7, 0, 0.7, 1.4],              # Data < levels (even)
    [-2.1, -1.4, -0.7, 0, 0.7, 1.4, 2.1]    # Data > levels (even)
]
  
# initiate the figure
fig = plt.figure()
ax = [0] * 16
for i in range(16):
    ax[i] = fig.add_subplot(4,4,i+1)

# contourplots and colorbars
CP = [0] * 16
for i in range(4):
    for j in range(4):
        k = i*4 + j 
     
        CP[k] = ax[k].contourf(Z, levels = V[i], cmap = rwb_cmap, 
            extend = extends[j])
        if i == 0:
            ax[k].set_title("extend = " + extends[j])
        fig.colorbar(CP[k], ax = ax[k])

# set the labels
ax[0].set_ylabel("Data < lev (odd)")
ax[4].set_ylabel("Data > lev (odd)")
ax[8].set_ylabel("Data < lev (even)")
ax[12].set_ylabel("Data > lev (even)")

# show    
plt.show()

plt.savefig("../figures/103_contour_plots_extend")










