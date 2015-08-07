```python
"""
MAKING SUBPLOTS WITH ADD_AXES

However useful add_subplot is to quickly add some subplots, when you want more 
control over the positioning and size, you'll have to use add_axes instead. This 
function accepts a tupple (left_edge, bottom_edge, width, height). These values 
are relative. 

Example 1 shows a more or less random collection of axes instances. 

<s>For the even more anal people</s> I included example 2, which gives even more 
control over the positioning. 
First, a number of units for x and y is set. Then the left and bottom edges and 
the width and height of the subplots are set. Because the number of total of 
horizontal/vertical units are known, the l/b/w/h values can be made relative. 
Finally the figure size is fixed. 

See also the note about the aspect ration in example 022.

"""

import matplotlib
import matplotlib.pyplot as plt

### EXAMPLE 1 ###

# some more or less randomly placed subplots 

# make the figure object
fig = plt.figure()

# left, bottom, width, height
axes_coords = [
    (0.1, 0.1, 0.4, 0.4),
    (0.1, 0.5, 0.3, 0.4),
    (0.6, 0.6, 0.35, 0.3),
    (0.55, 0.1, 0.35, 0.7),
]

ax = [0] * 4

for i in range(4):
    ax[i] = fig.add_axes(axes_coords[i])

ax[0].set_title("make some space axes 1")
ax[1].set_title("axes 2 - oh no, what a mess!")
ax[2].set_title("axes 3")
ax[3].set_title("axes 4")

plt.show()

plt.savefig("../figures/023_0_subplots_add_axes")


### EXAMPLE 2 ###

# a 2x2 grid where all plots have the same size

axes_inch_per_unit = 0.3        # inch per unit (inch = 25.4 mm)
axes_x_units = 10               # horizontal nr of units
axes_y_units = 8                # vertical nr of units

axes_l = 1   / axes_x_units     # left edge of subplot, left column, in units
axes_r = 5.5 / axes_x_units     # left edge of subplot, right column, in units
axes_w = 3.5 / axes_x_units     # width of a subplot, in units

axes_t = 4.5 / axes_y_units     # lower edge of top row, in units
axes_b = 1   / axes_y_units     # lower edge of bottom row, in units
axes_h = 2.5 / axes_y_units     # height of a subplot, in units

axes_coords = [                 # array with coords for all subplots
    (axes_l, axes_t, axes_w, axes_h),
    (axes_r, axes_t, axes_w, axes_h),
    (axes_l, axes_b, axes_w, axes_h),
    (axes_r, axes_b, axes_w, axes_h),
]

fig_width = axes_inch_per_unit * axes_x_units   # width of figure, in inches
fig_height = axes_inch_per_unit * axes_y_units  # height of figure, in inches

fig = plt.figure(figsize = (fig_width, fig_height), dpi = 100) # init figure

ax = [0] * 4                    # init axes array

for i in range(4):
    ax[i] = fig.add_axes(axes_coords[i])    # init axes

ax[0].set_title("Ordnung...")
ax[1].set_title("...muss sein")

plt.show()

plt.savefig("../figures/023_1_subplots_add_axes")
```
![](/figures/023_0_subplots_add_axes.png)
![](/figures/023_1_subplots_add_axes.png)
[Source](/python/023_subplots_add_axes.py)