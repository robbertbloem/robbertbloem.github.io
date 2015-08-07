```python
"""
LATEX

As discussed in 045, Matplotlib can use LaTeX to make the text. To do this you 
have to set the rcParam. Using this mode requires a properly insalled LaTeX 
compiler.

Compared to the examples in 045, the spacing and alignment are much better. 

The font style is still different. The LaTeX font style can be changed with 
LaTeX commands (presumably). The font style for non-math-mode can be set with 
rcParams.

By default the tick labels are numbers set in LaTeX (see y-axis). This can be 
changed by assigning setting the tick labels by hand (see x-axis). Of course, it 
can be set to LaTeX again by using a raw sting and some dollar signs. The axis 
labels are however in non-LaTeX-mode. 

Math text always and LaTeX mode by default uses the inline LaTeX mode. The 
limits of a sum are displayed next to the sum instead of below and above. LaTeX 
mode allows the use of \displaystyle.







RCPARAMS:
'font.family'       'sans-serif', serif'


"""

import numpy
import matplotlib 
import matplotlib.pyplot as plt

plt.close("all")


matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = [r"\usepackage{amsmath}"]
# matplotlib.rcParams['font.family'] = 'serif'

fig = plt.figure()
ax = fig.add_subplot(111)

ax.text(0.1,0.9, "Normal text")
ax.text(0.1,0.8, r"\TeX, a frequency $\omega_1(\mu_1)$ bla")
ax.text(0.1,0.7, r"$\lim_{x\to\infty}x$ limit")
ax.text(0.1,0.6, r"$\displaystyle\lim_{x\to\infty}x$ limit")

ax.text(0.1,0.5, r"$\int_{0}^{\infty}dx\exp[x]$, integration")
ax.text(0.1,0.4, r"$\displaystyle\int_{0}^{\infty}dx\exp[x]$, integration")
ax.text(0.1,0.3,r"$\displaystyle\int_{0}^{\infty}\!\!\!dx\exp[x]$, integration") 
# uses \! to reduce spacing

ax.text(0.1,0.2, r"$\sum_{0}^{\infty}dx\exp[x]$, sum")
ax.text(0.1,0.05, r"$\displaystyle\sum_{0}^{\infty}dx\exp[x]$, sum")

ax.set_xlim(0,1)
ax.set_ylim(0,1)

ax.set_xlabel("Non-default behavior")
ax.set_xticklabels([r"$0.0$", "0.2", "0.4", "0.6", "0.8", "1.0"])

ax.set_ylabel("Default in LaTeX mode")

plt.show()

plt.savefig("../figures/046_text_latex")

matplotlib.rcdefaults()
```
![](/figures/046_text_latex.png)
[Source](/python/046_text_latex.py)