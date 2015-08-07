"""
MATH TEXT

Matplotlib can do some fancy stuff with text.
First, it can display a normal string.
Second, math text can parse a subset of LaTeX commands and is comparable to the 
inline display of LaTeX, ie. $a^2+b^2=c^2$. 
Finally there is full blown LaTeX: all text will be set in LaTeX. You have to 
set this in the rcParams. It is discussed in example 046.

MATH TEXT OR LATEX?

In short, LaTeX is more capable but slower. If you display plenty of equations, 
LaTeX is probably the better choice. 
The examples for math text show that the alignment and spacing is sometimes a 
bit off ('lim' and 'x' are not on one line, 'sum' and 'exp' overlap). However, 
if you only want to show the occasional Greek letter, math text is the better 
choice.




MATH TEXT STYLE

A problem with math text is that the default font styles differ. By default the 
normal text is 'sans-serif' and mathtext is 'serif'. Using rcParams this can be 
changed.



RCPARAMS:
'mathtext.fontset'  'cm', 'stix', 'stixsans'
'font.family'       'sans-serif', serif'



"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

plt.close("all")

# dic = matplotlib.rcParams
# group = "mathtext" 
# for key in dic:
#     if group in key:
#         print(key, dic[key])


style = "default" # "sans-serif" # "serif" # 

if style == "default":
    matplotlib.rcParams['mathtext.fontset'] = "cm"
    matplotlib.rcParams['font.sans-serif'] = ['Bitstream Vera Sans']
    matplotlib.rcParams['font.family'] = 'sans-serif'
elif style == "serif":
    matplotlib.rcParams['mathtext.fontset'] = "stix"
    matplotlib.rcParams['font.serif'] = ['Times New Roman']
    matplotlib.rcParams['font.family'] = 'serif'
elif style == "sans-serif":
    matplotlib.rcParams['mathtext.fontset'] = "stixsans"
    matplotlib.rcParams['font.sans-serif'] = ['Bitstream Vera Sans']
    matplotlib.rcParams['font.family'] = 'sans-serif'

fig = plt.figure()
ax = fig.add_subplot(111)

ax.text(0.1,0.9, "Normal text")
ax.text(0.1,0.8, r"\TeX, this is not parsed")
ax.text(0.1,0.7, r"$\lim_{x\to\infty}x$ limit")
ax.text(0.1,0.6, r"$\int_{0}^{\infty}dx\exp[x]$ integral")
ax.text(0.1,0.45, r"$\sum_{i=0}^{N} \exp[i]$ sum")

ax.text(0.1,0.3, r"The math text $\omega_1(\mu_2)$ can have a different style")

ax.set_xlim(0,1)
ax.set_ylim(0,1)

ax.set_title(style)

plt.show()

if style == "default":
    plt.savefig("../figures/045_0_text_mathtext")
elif style == "serif":
    plt.savefig("../figures/045_1_text_mathtext")
elif style == "sans-serif":
    plt.savefig("../figures/045_2_text_mathtext")


matplotlib.rcdefaults()