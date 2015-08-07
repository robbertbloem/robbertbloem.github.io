```python
"""
TEXT POSITION

The text can be positioned relative to the data or relative to the axes 
coordinates. In the latter case you'll need to transform the coordinates. 

Note: When using Python 3.3 on a Mac, Matplotlib will truncate strings (like 
labels and titles).
"""

import matplotlib 
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# relative to the data
ax.text(x = 5, y = 7.5, s = "x = 5, y = 7.5, data coordinates")

# relative to the axes instance (0,0) to (1,1)
ax.text(x = 0.5, y = 0.5, s = "x = 0.5, y = 0.5, axes coordinates", 
    transform = ax.transAxes)

# set the axes limits
ax.set_xlim(0,10)
ax.set_ylim(0,10)

plt.show()

plt.savefig("../figures/041_text_positioning")



```
![](/figures/041_text_positioning.png)
[Source](/python/041_text_positioning.py)