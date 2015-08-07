"""
TEXT

Titles, labels, tick labels, annotation etc can be customized. Here we will look 
at some decoration: font-families and colors. 

You can give the options directly in some function, or you can use 
fontproperties. This allows you to set all properties in one place. 

Font properties API:
http://matplotlib.org/api/font_manager_api.html#matplotlib.font_manager.FontProperties

These functions list all fontnames:
matplotlib.font_manager.OSXInstalledFonts(directories=None, fontext='ttf')
matplotlib.font_manager.win32InstalledFonts(directory=None, fontext='ttf')

RCPARAMS:
'text.color'    k           # default color
'font.family'   sans-serif  # standard font family

Note: When using Python 3.3 on a Mac, Matplotlib will truncate strings (like 
labels and titles).
"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# defaults
ax.text(x = 0.1, y = 0.9, s = "A small test sentence with defaults")

# change size and color in a function
ax.text(x = 0.1, y = 0.8, s = "Changing fontsize and color", fontsize = 20, 
    color = "r", backgroundcolor = "y")

# make a font properties instance, give some values
fp = matplotlib.font_manager.FontProperties(
    family = ["serif", "fantasy"],
    size = 16
)
# use the font property instance to set the values
ax.text(x = 0.1, y = 0.7, s = "Using fontproperties", fontproperties = fp)

# use the font properties to import a custom font
fp = matplotlib.font_manager.FontProperties(
    size = 16
)
fp.set_name("Georgia")
ax.text(x = 0.1, y = 0.6, s = "Using an imported font (should be serif)", 
    fontproperties = fp)

plt.show()

plt.savefig("../figures/040_text")


