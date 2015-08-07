```python
"""
LINE STYLES

By default, Matplotlib makes solid lines. Manually, this can be set using 
'linestyle' or 'ls' and one the options listed below.

linestyle description
'-'       solid
'--'      dashed, use 'dashes = (on, off)' to change the gaps
'-.'      dash_dot
':'       dotted
'None'    draw nothing
' '       draw nothing
''        draw nothing

MORE INFO:
http://matplotlib.org/api/artist_api.html#matplotlib.lines.Line2D.set_linestyle

RCPARAMS:
'lines.linestyle' sets the default line style

"""

import numpy
import matplotlib
import matplotlib.pyplot as plt

# make some data 
x = numpy.arange(5, 15, 0.1) # start, stop, step
y = numpy.sin(x)
z = numpy.cos(x)

# change the line style
plt.figure()
plt.plot(x, y, linestyle = ":")
plt.plot(x, z, ls = "--", dashes = (10,20))
plt.title("Different line styles")
plt.show()
plt.savefig("../figures/011_line_properties_linestyle")



```
![](/figures/011_line_properties_linestyle.png)
