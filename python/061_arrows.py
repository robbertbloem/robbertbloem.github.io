"""
ARROWS 

Matplotlib has a bunch of options to make arrows.

AXES.ARROW

Axes.arrow(x,y,dx,dy) makes an arrow.

CONNECTION STYLES:
Angle: connect points A and B with a path. 'angleA' sets the angle from A and 'angleB' sets the angle towards B. 'rad' sets the radius of the curve (see note).
Angle3: same as 'Angle', but sets 'rad' for you.

Arc: make a Bezier curve. See Wikipedia for an explanation:
https://en.wikipedia.org/wiki/Bezier_curve
You can set the arm and angle for A and B and the radius (see note).
Arc3: as 'Arc', but you only have to set the radius. 

Note about the radius: in 'Angle' the radius is in points I think. With 'Arc', the radius is the distance between A and B. 

Bar: 


MATPLOTLIB.PATCHES.FANCYARROWPATCH

matplotlib.patches.FancyArrowPatch(posA, posB) also makes an arrow.

print(arrow.get_arrowstyle())


"""


import numpy
import matplotlib 
import matplotlib.pyplot as plt


plt.close("all")

fig = plt.figure()
ax = fig.add_subplot(111)

### AXES.ARROW() ###

# a very narrow arrow
ax.arrow(x = 1, y = 8, dx = 2, dy = 1)

# give it some width and change the colors
ax.arrow(
    x = 2, 
    y = 8, 
    dx = 2,
    dy = 1, 
    width = 0.1, 
    edgecolor = "r",
    facecolor = "y"
)

# the linestyle sets the edge of the arrow, not the path
ax.arrow(
    x = 3,
    y = 8,
    dx = 2,
    dy = 1,
    linestyle = "dashed",
    width = 0.1,
    facecolor = "y"
)

ax.text(2,9.5,"axes.arrow()")


### FANCY ARROW PATCH ###

# make the patch and add to the axes
posA = [5.5,8]
posB = [7.5,9]
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB,
    color = "b"
)
ax.add_patch(arrow) 

# again, with connectionstyle and the arrowstyle to the defaults
posA = [6.5,8]
posB = [8.5,9]
cs = matplotlib.patches.ConnectionStyle(
    "arc3", 
    rad = 0.0
)
ast = "simple" 
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast,
    color = "g"
)
ax.add_patch(arrow) 

# make the arrow head a bit bigger
posA = [7.5,8]
posB = [9.5,9]
cs = matplotlib.patches.ConnectionStyle(
    "arc3",
    rad = 0.0
)
ast = "-|>, head_length = 6, head_width = 3" 
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast,
    color = "r"
)
ax.add_patch(arrow) 

ax.text(6,9.5,"fancy arrow patch")


### ARC3 DEFLECTION ###

# give the connection a radius to make a curve
cs = matplotlib.patches.ConnectionStyle(
    "arc3", 
    rad = 1.0
)
ast = "-|>, head_length = 6, head_width = 3" 
posA = [1,5]
posB = [3,6]
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "b"
)
ax.add_patch(arrow) 

# not happy with the direction that the path deflects? 
# reverse posA and posB and the arrow direction. 
ast = "<|-, head_length = 6, head_width = 3"    
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posB, 
    posB = posA, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "g"
)
ax.add_patch(arrow) 

ax.text(1, 7, "arc3 deflection")

### ARC3 RADIUS ###

ast = "-|>, head_length = 6, head_width = 3" 
posA = [4,6]
posB = [6,7]

# rad = 1.0
cs = matplotlib.patches.ConnectionStyle(
    "arc3", 
    rad = 1.0
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "b"
)
ax.add_patch(arrow) 

# rad = 0.5
cs = matplotlib.patches.ConnectionStyle(
    "arc3", 
    rad = 0.5
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "g"
)
ax.add_patch(arrow) 

# rad = 2.0
cs = matplotlib.patches.ConnectionStyle(
    "arc3", 
    rad = 2.0
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "r"
)
ax.add_patch(arrow) 

ax.text(4, 7, "arc3 radius")


### ARC ANGLE ###

ast = "-|>, head_length = 6, head_width = 3" 

# set angle and arm to good settings
posA = [7,6]
posB = [9,7]
cs = matplotlib.patches.ConnectionStyle(
    "arc", 
    rad = 30.0, 
    angleA = 0, 
    angleB = 315, 
    armA = 40, 
    armB = 40
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "b"
)
ax.add_patch(arrow) 

# this looks a bit ridiculous 
posA = [7,5]
posB = [9,6]
cs = matplotlib.patches.ConnectionStyle(
    "arc", 
    rad = 30.0, 
    angleA = 0, 
    angleB = 315, 
    armA = 100, 
    armB = 100
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "g"
)
ax.add_patch(arrow) 

ax.text(7, 7, "arc angle")


### ANGLE3 ANGLE ###

ast = "-|>, head_length = 6, head_width = 3" 
posA = [1,1]
posB = [3,2]

# default angle
cs = matplotlib.patches.ConnectionStyle(
    "angle3", 
    angleA=90, 
    angleB=0
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "b"
)
ax.add_patch(arrow) 

# non-default angle
cs = matplotlib.patches.ConnectionStyle(
    "angle3", 
    angleA = 45, 
    angleB = -45
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "g"
)
ax.add_patch(arrow) 

ax.text(1, 3, "angle3 angle")

### ANGLE, RADIUS ###

ast = "-|>, head_length = 6, head_width = 3" 

# rad = 0.0
posA = [3.5,1]
posB = [5.5,2]
cs = matplotlib.patches.ConnectionStyle(
    "angle", 
    angleA = 45, 
    angleB = -45,
    rad = 0.0
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "b" 
)
ax.add_patch(arrow) 

# rad = 40.0
posA = [4,1]
posB = [6,2]
cs = matplotlib.patches.ConnectionStyle(
    "angle", 
    angleA = 45, 
    angleB = -45,
    rad = 40.0
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "g"
)
ax.add_patch(arrow) 

# rad = 60.0, a bit ridiculous
posA = [4.5,1]
posB = [6.5,2]
cs = matplotlib.patches.ConnectionStyle(
    "angle", 
    angleA = 45, 
    angleB = -45,
    rad = 60.0
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "r"
)
ax.add_patch(arrow) 

ax.text(4, 3, "angle radius")




### BAR ARMS AND ANGLE ###

ast = "-|>, head_length = 6, head_width = 3" 
posA = [7,2]
posB = [9,3]

# default bar
cs = matplotlib.patches.ConnectionStyle(
    "bar"
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "b"
)
ax.add_patch(arrow) 

# fraction
cs = matplotlib.patches.ConnectionStyle(
    "bar",
    fraction = 0.75
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "g"
)
ax.add_patch(arrow) 

# arms
cs = matplotlib.patches.ConnectionStyle(
    "bar",
    armA = 0.5,
    armB = 10.0,
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "r"
)
ax.add_patch(arrow) 


# angle
cs = matplotlib.patches.ConnectionStyle(
    "bar",
    angle = 45
)
arrow = matplotlib.patches.FancyArrowPatch(
    posA = posA, 
    posB = posB, 
    connectionstyle = cs, 
    arrowstyle = ast, 
    color = "c"
)
ax.add_patch(arrow) 


ax.text(7, 3, "bar arms and angle")






print(arrow.get_connectionstyle())




# ast = matplotlib.patches.ArrowStyle("-|>")#CurveFilledB()#head_length= 6, head_width= 3)







ax.set_xlim(0,10)
ax.set_ylim(0,10)

plt.show()

plt.savefig("../figures/061_arrows")