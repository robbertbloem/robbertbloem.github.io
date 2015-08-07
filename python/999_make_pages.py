from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import os
import re

import numpy
import matplotlib 
import matplotlib.pyplot as plt

re_comment_block = re.compile(r'\"{3}')

# def figure_files(filename, figurelist):
    

def make_page(filename, figlist):

    
    target_file = open("../" + filename[:-2] + "md", "w")
    target_file.write("```python\n")
    for line in open(filename):
        target_file.write(line)
    target_file.write("\n```\n")

    for fig in figlist:
        target_file.write("![](/figures/" + fig + ")\n")
        
    target_file.write("[Source](/python/" + filename[:-2] + "py)")


    
            

if __name__ == "__main__": 

    filelist = os.listdir(os.getcwd())
    figurelist = os.listdir("../figures/")

    for f in filelist:

        if f[0] != "9" and f[0] != "f" and f[0] != "h":
        
            figlist = []
            for fig in figurelist:
                if fig[:3] == f[:3]:    
                    figlist.append(fig)
        
            make_page(f, figlist)