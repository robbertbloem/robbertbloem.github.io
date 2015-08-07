"""
FIGURES, AXESES AND ARTISTS

Also an advanced topic, but also one that pops up regularly.

Matplotlib has different hierarchical levels: a Figure contains Axes that 
contains Artist instances. 

The Artist instance is what you see. It contains Lines2D, Text and Patches 
(shapes) subclasses. The Axes instance is a single plot, containing some Artist 
instances like lines and text and an Axis instance to make the ticks and labels 
of the axes. A Figure instance contains one or more Axes instances. 

In the very basic plot from the first example this happens more or less 
automagically. 
plt.figure()    # make a Figure 
plt.plot(y)     # make an Axes and an Artist instance (called Lines2D)

The hierarchy is better visible when using this:
fig = plt.figure()          # make a Figure
ax = fig.add_subplot(111)   # make an Axes
li = ax.plot(x, y)          # make a Lines2D

This division is important when you want to customize plots. To change the line 
color, you have to change the Lines2D instance, not the Axes or Figure instance. 
When you want to resize the figure, address the Figure instance etc. 

Do I sound like Captain Obvious? Maybe, but Matplotlib is littered with 
shortcuts like the very first example, where you ignore all complexities, but 
which also makes it more difficult to understand what you are doing.


CHANGING PROPERTIES

Properties can be set in two ways (ignoring rcParams): by setting a property 
when creating an instance or by setting it after creation. 

In this example the two methods are used:
ax = fig.add_subplot(111, xlabel = "x")     # set xlabel during creation of axes 
ax.set_ylabel("y")                          # set ylabel after creation of axes
Note the difference between the argument 'xlabel' and function 'set_ylabel()'.

In this example we are indecisive about the line color:
li = ax.plot(x, y, color = "r") # color line red at creation    
li[0].set_color("g")            # color line green after creation
Note here that the Lines2D instance is a list. 

Besides the 'set_property', there is also the 'get_property'. 
li[0].get_color()
You can also see how many Line2D objects there are:
ax.get_lines()
Or see what the current Axes is:
plt.gca()

MORE COMPLEXITIES

- contourplots don't use Line2D instances but a Collection
- behind the scenes there are more complexities with FigureCanvas etc. I never 
encountered those while making and adjusting plots.
- Matplotlib has many shortcuts. In other examples we already encountered 
'color' and 'c', which set the line color. With the functions we can now add 
'set_color()' and 'set_c()'. 



"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

plt.close("all")

# make some data 
x = numpy.arange(5, 15, 0.25) 
y = numpy.sin(x)
z = numpy.cos(x)

# figure
fig = plt.figure()                      # make a Figure

# axes
ax = fig.add_subplot(111, xlabel = "x") # make an Axes and set xlabel
ax.set_ylabel("y")                      # set ylabel

# Lines2D
li = ax.plot(x, y, color = "r")         # make a Lines2D and set color
li[0].set_color("g")                    # change the color
print(li[0].get_color())                # should print 'g'

# get the number of Line2D objects in ax
print(ax.get_lines())                   # '<a list of 1 Line2D objects>'

# illustrate use of plt.gca()
ax = 0                                  # delete pointer to the Axes instance
ax2 = fig.gca()                         # get current axis  
ax2.plot(x, z, color = "k")             # add more data to the plot

# get the number of Line2D objects in ax2
print(ax2.get_lines())                  # '<a list of 2 Line2D objects>'

plt.show()

plt.savefig("../figures/020_figures_axes_artists")



