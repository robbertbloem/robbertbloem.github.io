"""
SUBPLOT, THE BASICS

Until now we plotted directly in a figure. Very useful when you want to plot 
something simple. For more complicated plots we need subplots. More to the 
point, we need an 'axes' instance. You do this with 'add_subplot(number of rows, 
number of columns, index)' The index starts at 1, not 0. It can be used with or 
without commas: 'add_subplot(222)' and 'add_subplot(2,2,2)' are both valid.

Each axes instance is independent from the others. You can (you have to) set 
titles, labels and limits for each axes instance. Because we use an axes 
instance, the functions 'title', 'xlabel' etc are prepended by 'set_', as 
discussed in example 020.

The advantage is that we can first plot the data for all axes, then assign the 
labels for all axes etc. 

You can see that the label of the right plot overlaps the left plot, in 
022_subplots_add_subplots we will see how we can fix that. 

"""

import numpy
import matplotlib
import matplotlib.pyplot as plt

# make some data 
x = numpy.arange(5,15,0.1) # start, stop, step
y = numpy.sin(x)
z = numpy.cos(x)

# make the figure object
fig = plt.figure()

# make the axes objects
ax = [0] * 2
for i in range(len(ax)):
    # one row, two columns. The index starts at 1, not 0.
    ax[i] = fig.add_subplot(1, 2, i+1) 

# first plot something in both axes
ax[0].plot(x,y)
ax[1].plot(x,z)

# now set the titles and labels
# plt.title("") -> ax.set_title("")
ax[0].set_title("Sine function")
ax[1].set_title("Cosine function")

# plt.xlabel("") -> ax.set_xlabel("")
ax[0].set_xlabel("x")
ax[1].set_xlabel("x")

# plt.ylabel("") -> ax.set_ylabel("")
ax[0].set_ylabel("sin(x)")
ax[1].set_ylabel("cos(x)")

# plt.xlim() -> ax.set_xlim()
ax[0].set_xlim(8,12)
ax[1].set_xlim(6,14)

# plt.ylim() -> ax.set_ylim()
ax[0].set_ylim(-0.9,1.1)
ax[1].set_ylim(-1.1,0.9)

plt.show()
plt.savefig("../figures/021_subplots_basics")



