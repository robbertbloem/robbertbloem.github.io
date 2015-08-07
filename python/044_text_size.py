"""
TEXT SIZE

The fontsize can be set to an absolute value, in points, or to a relative value: 
'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' 

rcParams:
'font.size'         12      # default font size
'axes.labelsize'    medium  # axis labels
'axes.titlesize'    large   # plot title
'legend.fontsize'   large   # legend


FONT WEIGHT

A numeric value in range 0-1000 or 'ultralight', 'light', 'normal', 'regular', 
'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 
'extra bold', 'black'.

RCPARAMS:
'font.weight'       normal
'axes.labelweight'  normal


Note: When using Python 3.3 on a Mac, Matplotlib will truncate strings (like 
labels and titles).
"""


import numpy
import matplotlib 
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# fontsize, absolute
ax.text(0.05, 0.9, s = "fontsize default (12)")
ax.text(0.4, 0.9, s = "fontsize = 10", fontsize = 10)
ax.text(0.6, 0.9, s = "fontsize = 20", fontsize = 20)

# fontsize, relative
ax.text(0.05, 0.8, s = "fontsize default (12)")
ax.text(0.4, 0.8, s = "fontsize = 'large'", fontsize = "large")
ax.text(0.75, 0.8, s = "fontsize = 'small'", fontsize = "small")

# fontweight
ax.text(0.05, 0.7, s = "fontweight default (normal)")
ax.text(0.2, 0.65, s = "fontweight = 'ultralight'", weight = "ultralight")
ax.text(0.6, 0.65, s = "fontweight = 'bold'", weight = "bold")


plt.show()

plt.savefig("../figures/044_text_size")


