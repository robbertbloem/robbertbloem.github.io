```python

import numpy
import matplotlib 
import matplotlib.pyplot as plt

plt.close("all")

fig = plt.figure()
ax = fig.add_subplot(111)

### WEDGE ###
wedge = matplotlib.patches.Wedge(
    center = [2,10],
    r = 1,
    theta1 = 0,
    theta2 = 90,
    color = "y",    # sets face and edge color
    linewidth = 2
)
ax.add_patch(wedge) 

wedge = matplotlib.patches.Wedge(
    center = [2,10],
    r = 1,
    theta1 = 235,
    theta2 = 360,
    edgecolor = "k",
    facecolor = "orange",
    linewidth = 2
)
ax.add_patch(wedge) 

ax.text(2, 11.25, "Wedge", ha = "center")

### RECTANGLE ###

rectangle = matplotlib.patches.Rectangle(
    xy = [5,9],     # left bottom edge
    width = 1,
    height = 2
)
ax.add_patch(rectangle) 

ax.text(5.5, 11.25, "Rectangle", ha = "center")


### ELLIPSE ###

ellipse = matplotlib.patches.Ellipse(
    xy = [9,10],    # center
    width = 1,
    height = 2,
    angle = 45      # degrees
)
ax.add_patch(ellipse) 

ax.text(9, 11.25, "Ellipse", ha = "center")

### REGULAR POLYGON ###
regular_polygon = matplotlib.patches.RegularPolygon(
    xy = (2,7),   # tuple! center 
    numVertices = 5,
    radius = 1,
    orientation = 1 # radians, 1 rad ~= 57 degrees
)
ax.add_patch(regular_polygon) 

ax.text(2, 8.25, "Reg. polygon", ha = "center")



### POLYGON WITH ARBITRARY SHAPE ###

# default is a closed edge
xy = numpy.array([
    [4,6],
    [5,8],
    [6,6],
    [7,7]
])
polygon = matplotlib.patches.Polygon(
    xy = xy,
    linewidth = 2,
    facecolor = "y"
)
ax.add_patch(polygon) 
ax.text(5.5, 8.25, "Polygon closed", ha = "center")

# but we can also have an open edge
xy = numpy.array([
    [8,8],
    [9,6],
    [10,8],
    [11,7]
])
polygon = matplotlib.patches.Polygon(
    xy = xy,
    linewidth = 2,
    facecolor = "y",
    closed = False
)
ax.add_patch(polygon) 

ax.text(9.5, 8.25, "Polygon open", ha = "center")



### FANCY BBOXes ###

bbox = matplotlib.patches.FancyBboxPatch(
    xy = [1,2], 
    width = 1, 
    height = 2, 
    boxstyle = 'round', 
    bbox_transmuter = None, 
    mutation_scale = 1.0, 
    mutation_aspect = None
)
ax.add_patch(bbox) 
rectangle = matplotlib.patches.Rectangle(
    xy = [1,2], 
    width = 1,
    height = 2,
    color = "y"
)
ax.add_patch(rectangle)
ax.text(1.5, 0.5, "round", ha = "center")

bbox = matplotlib.patches.FancyBboxPatch(
    xy = [3,2], 
    width = 1, 
    height = 2, 
    boxstyle = 'sawtooth', 
    bbox_transmuter = None, 
    mutation_scale = 1.0, 
    mutation_aspect = None
)
ax.add_patch(bbox) 
rectangle = matplotlib.patches.Rectangle(
    xy = [3,2], 
    width = 1,
    height = 2,
    color = "y"
)
ax.add_patch(rectangle)
ax.text(3.5, 0.5, "sawtooth", ha = "center")

bbox = matplotlib.patches.FancyBboxPatch(
    xy = [6,2], 
    width = 1, 
    height = 2, 
    boxstyle = 'larrow', 
    bbox_transmuter = None, 
    mutation_scale = 1.0, 
    mutation_aspect = None
)
ax.add_patch(bbox) 
rectangle = matplotlib.patches.Rectangle(
    xy = [6,2], 
    width = 1,
    height = 2,
    color = "y"
)
ax.add_patch(rectangle)
ax.text(6.5, 0.5, "larrow", ha = "center")

boxstyle = matplotlib.patches.BoxStyle.Roundtooth(pad = 0.3)
bbox = matplotlib.patches.FancyBboxPatch(
    xy = [9,2], 
    width = 1, 
    height = 2, 
    boxstyle = boxstyle, 
    bbox_transmuter = None, 
    mutation_scale = 1.0, 
    mutation_aspect = None
)
ax.add_patch(bbox) 
rectangle = matplotlib.patches.Rectangle(
    xy = [9,2], 
    width = 1,
    height = 2,
    color = "y"
)
ax.add_patch(rectangle)
ax.text(9.5, 0.5, "roundtooth", ha = "center")

boxstyle = matplotlib.patches.BoxStyle("Square", pad = 0.3)
bbox = matplotlib.patches.FancyBboxPatch(
    xy = [12,2], 
    width = 1, 
    height = 2, 
    boxstyle = boxstyle, 
    bbox_transmuter = None, 
    mutation_scale = 1.0, 
    mutation_aspect = None
)
ax.add_patch(bbox) 
rectangle = matplotlib.patches.Rectangle(
    xy = [12,2], 
    width = 1,
    height = 2,
    color = "y"
)
ax.add_patch(rectangle)
ax.text(12.5, 0.5, "rectangle", ha = "center")

ax.text(8, 5, "Fancy bounding boxes (blue) with rectangle (yellow)", ha = "center")

ax.set_xlim(0,16)
ax.set_ylim(0,12)

plt.show()











```
[Source](/python/060_patches.py)