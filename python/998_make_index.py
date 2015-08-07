from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import os

import numpy
import matplotlib 
import matplotlib.pyplot as plt



plot_props = numpy.array([
    ["000", "How to get a plot on the screen"],
    ["001", "Add labels and set limits"],
    ["002", "Usage of rcParams"],
    ["010", "Line colors"],
    ["011", "Line style"],
    ["012", "Line width"],
    ["013", "Markers"],
    ["020", "Figures, Axes and Artists"],
    ["021", "Subplots"],
    ["022", "add_subplot()"],
    ["023", "add_axes()"],
    ["024", "Double axes"],
    ["024", "Shared axes"],
    ["030", "Adjust ticks"],
    ["031", "Adjust spines (plot borders)"],
    ["032", "Adjust labels"],
    ["033", "Adjust using rcParams"],
    ["040", "Text basics"],
    ["041", "Text positioning"],
    ["042", "Text alignment"],
    ["043", "Text rotation"],
    ["044", "Text size"],
    ["045", "Math text"],
    ["050", "Colors"],
    ["051", "Color maps"],
    ["100", "Contour plots, lines and filled"],
    ["101", "Contour plot legends"],
    ["102", "Contour plot levels"],
    ["103", "Contour plot 'extend'"]
])

plot_groups = numpy.array([
    ["00", "Basics"],
    ["01", "Line properties"],
    ["02", "Sub plots"],
    ["03", "Adjust axes"],
    ["04", "Adjust text"],
    ["05", "Colors"],
    ["10", "Contour plots"]
])


# def write_header(f, py_filename):
#     f.write("<html>")
#     f.write("<head>")
#     f.write("<title>Matplotlib examples and reference: " + py_filename[4:-3] +"</title>")
#     f.write('<link rel="stylesheet" href="style.css">')
#     f.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
#     f.write("</head>")
#     f.write("<body>")

def write_header(f):
    f.write("<html>")
    f.write("<head>")
    f.write("<title>Matplotlib examples and reference: index</title>")
    f.write('<link rel="stylesheet" href="style.css">')
    f.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
    f.write("</head>")
    f.write("<body>")
    f.write("<h1>Matplotlib examples and reference</h1><p>After using Matplotlib for some time I saw that I had to look up the same things over and over again. 'How did I move the labels away from the axes?' The examples on the Matplotlib website are useful but too often too complicated. Different concepts are combined in a single example, leaving the user (me) to figure out how the example works, instead of finding a solution to my problem. </p><p>I started these pages as a reference for myself, but quickly realized that other people might be interested as well. It does however mean that the examples mostly treat what I use myself.</p><p>The examples in 'Basics' and 'Line properties' are enough to quick-and-dirty plot some data. The examples after that show further customizations to make 'publication quality' plots. </p><p>Examples 002 and 020 deserve some special attention. Example 002 explains the use of rcParams to change properties globally. Example 020 introduces the hierarchy of Matplotlib with Figures, Axes and Artists. It adds complexity but also flexibility and power to Matplotlib.</p>")

def write_footer(f):
    f.write('<a name="copyright"></a><h1>Information</h1><p>The plots where generated using Matplotlib 1.4.3, with Python 3.4.2 on Mac OS X 10.10.4. </p>')
    f.write("<h1>Copyright</h1><p>I hope you find the examples useful and that you can use them to make better figures. The examples, explanations and figures are however my work and I don't want you to reproduce them.</p>")
    f.write("</body>")
    f.write("</html>")


def make_html():
    # make html file, write header
    html_filename = "../index.html"
    html_file = open(html_filename, "w")    
    write_header(html_file)    

    html_list = os.listdir(os.getcwd())
    fig_path = os.getcwd()[:-6] + "/figures/"
    fig_list = os.listdir(fig_path)

    # print(fig_list)

    html_list = [n for n in html_list if n[:3] in plot_props[:,0]]

    for i in range(len(plot_groups)):
        
        temp_files = [n for n in html_list if n[:2] in plot_groups[i,0]]
        temp_props = [n for n in plot_props if n[0][:2] in plot_groups[i,0]]
        
        html_file.write('<h2>' + plot_groups[i][1] + '</h2>')
        
        html_file.write('<div id="table">')
        
        for j in range(len(temp_files)):

            if j % 3 == 0:
                html_file.write('<div class="row">')
            
            html_file.write('<span class="cell">')
            
            html_file.write('<a href="https://github.com/robbertbloem/robbertbloem.github.io/blob/master/' + temp_files[j][:-3] + '.md">')
            
            temp_figs = [n for n in fig_list if n[:3] in temp_files[j][:3]]  
            for fig in temp_figs:
                width = str(int(numpy.floor((220-2*len(temp_figs))/len(temp_figs))))
                html_file.write('<img width="' + width + 'px" src = "figures/' + fig + '" />')
            
            html_file.write('</br>' + temp_props[j][0] + ': ' + temp_props[j][1] + '</a></br>')
            html_file.write('</span>')

            if j % 3 == 2:
                html_file.write('</div>')  
    
        if len(temp_files) % 3 == 1:
            html_file.write('<span class="cell"></span>') 
            html_file.write('<span class="cell"></span>')  
            html_file.write('</div>')
            
        if len(temp_files) % 3 == 2:
            html_file.write('<span class="cell"></span>')  
            html_file.write('</div>')
    
        
        html_file.write('</div>')

    
    # write footer and close html file
    write_footer(html_file)
    html_file.close()


if __name__ == "__main__":

    make_html()