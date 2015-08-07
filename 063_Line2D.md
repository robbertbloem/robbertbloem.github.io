```python
import numpy
import matplotlib 
import matplotlib.pyplot as plt

plt.close("all")

fig = plt.figure()
ax = fig.add_subplot(111)

# make data
x = numpy.arange(5, 16, 1) 
y = numpy.sin(x)
z = numpy.cos(x)

# add lines
l = [0] * 2
l[0] = matplotlib.lines.Line2D(x, y)
l[1] = matplotlib.lines.Line2D(x, z)
ax.add_line(l[0])
ax.add_line(l[1])


ax.set_xlim(5,15)
ax.set_ylim(-1.1,1.1)

plt.show()
```
[Source](/python/063_Line2D.py)