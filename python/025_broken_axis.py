
import numpy
import matplotlib 
import matplotlib.pyplot as plt

x = numpy.arange(100)
y = numpy.exp(-x/10)

# fig = plt.figure()

ax = [0] * 2

fig, (ax[0], ax[1]) = plt.subplots(1,2,sharey = True)

ax[0].plot(x,y)
ax[1].semilogx(x,y)

ax[0].set_xlim(0,5)
ax[1].set_xlim(5,100)

plt.show()
