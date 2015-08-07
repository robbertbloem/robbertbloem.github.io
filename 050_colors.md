```python
"""
COLORS

RGB, HEX, FLOATS

Colors in Matplotlib are in RGB (red, green, blue). Matplotlib accepts a tupple 
with values between 0 (off) and 1 (on) for each color. Red is for example 
(1,0,0). You can find tables on the internet. Most tables give values between 0 
and 255 because there are really only 2**8 values for each color. You can also 
give the hexadecimal value. 00 is 0, FF is 255. The hex code for red is #FF0000.  
Finally, you can use a float ('0.5') for a grey scale.


COLOR NAMES

It is usually easier to use color names instead of RGB or HEX codes. Matplotlib 
has some 145 standard color names, you can print a list using 
'print(matplotlib.colors.cnames)'. 
Some color names have abbreviations. Note that while 'red' and 'blue' correspond 
to the RGB codes (1,0,0) and (0,0,1), green does not. Both 'grey' and 'gray' 
work.

Abbreviations, name and RGB tupple.
b   blue    (0.0,  0.0,  1.0)
g   green   (0.0,  0.5,  0.0)
r   red     (1.0,  0.0,  0.0)
c   cyan    (0.0,  0.75, 0.75)
m   magenta (0.75, 0.0,  0.75)
y   yellow  (0.75, 0.75, 0.0)
k   black   (0.0,  0.0,  0.0)
w   white   (1.0,  1.0,  1.0)




VISIBLE LIGHT SPECTRUM

To map from wavelength to RGB value, take a look here:
http://stackoverflow.com/a/3407960/2075269


"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

plt.close("all")

# print all color names
# print(matplotlib.colors.cnames)

fig = plt.figure()
ax = fig.add_subplot(111)

# red
ax.text(0.1, 0.9, "red", color = "red")                     # name
ax.text(0.1, 0.8, "r, also red", color = "r")               # abbreviation
ax.text(0.1, 0.7, "#FF0000, also red", color = "#FF0000")   # hex
ax.text(0.1, 0.6, "(1, 0, 0), also red", color = (1,0,0))   # rgb

# green
ax.text(0.6, 0.9, "green", color = "green")
ax.text(0.6, 0.8, "g, also green", color = "g")
ax.text(0.6, 0.7, "#00FF00, also green?", color = "#00FF00")
ax.text(0.6, 0.6, "(0,1,0), also green?", color = (0,1,0))
ax.text(0.6, 0.5, "(0, 0.5, 0), also green", color = (0,0.5,0))

# blue
ax.text(0.1, 0.4, "blue", color = "blue")
ax.text(0.1, 0.3, "b, also blue", color = "b")
ax.text(0.1, 0.2, "#0000FF, also blue", color = "#0000FF")
ax.text(0.1, 0.1, "(0, 0, 1), also blue", color = (0,0,1))

# class to convert from abbreviation, name or hex to RGB
CC = matplotlib.colors.ColorConverter()
rgb = CC.to_rgb("rosybrown")

# rosybrown
ax.text(0.6, 0.4, "rosybrown", color = "rosybrown")
# no abbreviation
ax.text(0.6, 0.2, "#BC8F8F, also rosybrown", color = "#BC8F8F")
ax.text(0.6, 0.1, "rgb, also rosybrown", color = rgb)

plt.show()

plt.savefig("../figures/050_colors")












```
![](/figures/050_colors.png)
[Source](/python/050_colors.py)