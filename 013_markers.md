```python
"""
MARKERS:

Besides plotting lines, you can also plot markers, or both. 
By default the markers have the color according to the color_cycle. The face and 
edge color and size can be changed. In the example below the alternative short 
names are given. I'm not in favor of using abbrevations in code, but 
markeredgewidth is a long name.

MORE INFO:
For a full list of markers, look here:
http://matplotlib.org/api/artist_api.html#matplotlib.lines.Line2D.set_marker

RCPARAMS:

"""

import numpy
import matplotlib
import matplotlib.pyplot as plt

# make some data 
x = numpy.arange(5, 15, 0.25) # start, stop, step
y = numpy.sin(x)
z = numpy.cos(x)

plt.figure()
# line with markers
plt.plot(x, y, marker = "H")
# markers only
plt.plot(x, z,              
    linestyle = "None",     # alt: ls           
    marker = "D",           
    markerfacecolor = "y",  # alt: mfc
    markeredgecolor = "r",  # alt: mec
    markeredgewidth = 2,    # alt: mew
    markersize = 8          # alt: ms
)

plt.title("Markers")
plt.show()
plt.savefig("../figures/013_markers")
```
![](/figures/013_markers.png)
[Source](/python/013_markers.py)