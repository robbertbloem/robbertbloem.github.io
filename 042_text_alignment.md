```python
"""
TEXT ALIGNMENT

Text can be aligned horizontally and vertically using 'ha' (left, right, center) 
and 'va' (top, center, bottom, baseline). Default is baseline, left.

Note: When using Python 3.3 on a Mac, Matplotlib will truncate strings (like 
labels and titles).
"""


import matplotlib 
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# horizontal alignment
ax.plot([0.5,0.5],[0.55,1],c="k", alpha = 0.5)

ax.text(x = 0.5, y = 0.9, s = "default ha")
ax.text(x = 0.5, y = 0.8, s = "ha = left", ha = "left")
ax.text(x = 0.5, y = 0.7, s = "ha = center", ha = "center")
ax.text(x = 0.5, y = 0.6, s = "ha = right", ha = "right")

# vertical alignment 
ax.plot([0,1], [0.4,0.4], c="k", alpha = 0.5)

ax.text(x = 0.05, y = 0.4, s = "default va")
ax.text(x = 0.25, y = 0.4, s = "va = baseline", va = "baseline")
ax.text(x = 0.45, y = 0.4, s = "va = bottom", va = "bottom")
ax.text(x = 0.65, y = 0.4, s = "va = center", va = "center")
ax.text(x = 0.85, y = 0.4, s = "va = top", va = "top")

# set axes limits
ax.set_xlim(0,1)
ax.set_ylim(0,1)



plt.show()

plt.savefig("../figures/042_test_alignment")



```
![](/figures/042_test_alignment.png)
[Source](/python/042_text_alignment.py)