"""
SHARE AN AXIS BETWEEN TWO SUBPLOTS

If you want to share an axes between two subplots, simply use 'sharex' or 
'sharey' when creating the subplot. 

"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

ax = [0] * 2

fig = plt.figure()

ax[0] = fig.add_subplot(121)
ax[1] = fig.add_subplot(122, sharey=ax[0])

x1 = numpy.arange(0,5)
y1 = numpy.arange(0,5)

x2 = numpy.arange(5,10)
y2 = numpy.arange(5,10)

ax[0].plot(x1,y1)
ax[1].plot(x2,y2)

plt.show()

plt.savefig("../figures/025_subplots_shared_axis")
