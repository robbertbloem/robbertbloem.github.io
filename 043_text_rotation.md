```python
"""
TEXT ROTATION

Text can be rotated, using the 'rotation' argument. The rotation is in degrees. 
For middle point of the rotation is depends on the horizontal and vertical 
alignment.

Note: When using Python 3.3 on a Mac, Matplotlib will truncate strings (like 
labels and titles).
"""


import matplotlib 
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# default ha and va
x = 0.15
y = 0.7
ax.plot([x,x],[y-0.1,y+0.1],c="k", alpha = 0.5)
ax.plot([x-0.05, x+0.15], [y,y],c="k", alpha = 0.5)
ax.text(x, y + 0.13, s = "default")
ax.text(x, y, s = "0 degrees")
ax.text(x, y, s = "30 degrees", rotation = 30)

# ha =  left, va = baseline
x = 0.45
y = 0.7
ax.plot([x,x],[y-0.1,y+0.1],c="k", alpha = 0.5)
ax.plot([x-0.05, x+0.15], [y,y],c="k", alpha = 0.5)
ax.text(x, y + 0.13, s = "ha = left\nva = baseline", ha = "left")
ax.text(x, y, s = "0 degrees", ha = "left", va = "baseline")
ax.text(x, y, s = "30 degrees", ha = "left", va = "baseline", rotation = 30)

# ha = left, va = bottom
x = 0.8
y = 0.7
ax.plot([x,x],[y-0.1,y+0.1],c="k", alpha = 0.5)
ax.plot([x-0.05, x+0.15], [y,y],c="k", alpha = 0.5)
ax.text(x, y + 0.13, s = "ha = left\nva = bottom", ha = "left")
ax.text(x, y, s = "0 degrees", ha = "left", va = "bottom")
ax.text(x, y, s = "30 degrees", ha = "left", va = "bottom", rotation = 30)

# ha = center, va = center
x = 0.15
y = 0.2
ax.plot([x,x],[y-0.1,y+0.1],c="k", alpha = 0.5)
ax.plot([x-0.1, x+0.1], [y,y],c="k", alpha = 0.5)
ax.text(x, y + 0.13, s = "ha = center\nva = center", ha = "center")
ax.text(x, y, s = "0 degrees", ha = "center", va = "center")
ax.text(x, y, s = "30 degrees", ha = "center", va = "center", rotation = 30)

# ha = right, va = top
x = 0.8
y = 0.2
ax.plot([x,x],[y-0.1,y+0.1],c="k", alpha = 0.5)
ax.plot([x-0.15, x+0.05], [y,y],c="k", alpha = 0.5)
ax.text(x, y + 0.13, s = "ha = right\nva = top", ha = "right")
ax.text(x, y, s = "0 degrees", ha = "right", va = "top")
ax.text(x, y, s = "30 degrees", ha = "right", va = "top", rotation = 30)

ax.set_xlim(0,1)
ax.set_ylim(0,1)



plt.show()

plt.savefig("../figures/043_text_rotation")



```
![](/figures/043_text_rotation.png)
[Source](/python/043_text_rotation.py)