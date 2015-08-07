import numpy
import matplotlib 
import matplotlib.pyplot as plt

plt.close("all")

fig = plt.figure()
ax = fig.add_subplot(111)

cs = matplotlib.patches.ConnectionStyle(
    "arc3",
    rad = 0.0
)









# arrows = [
#     [2,  9, 30, 10],
#     [6,  9, 15, 10],
#     [10, 9, 15, 20],
#     [14, 9, 15, 10],
#     [2,  5, 15, 10],
#     [6,  5, 15, 10],
#     [10, 5, 15, 10],
#     [14, 5, 15, 10],
#     [2,  1, 15, 10],
#     [6,  1, 15, 10],
#     [10, 1, 15, 10],
#     [14, 1, 15, 10],
# ]

x_list = [2,6,10,14]
y_list = [9,5,1]
dy = 2
dytext = 0.5

arrows = [[25,10], [15,10], [15, 20], [15,10]]



count = 0
for i in range(3):
    
    y = y_list[i]
    
    for j in range(4):
        x = x_list[j]
        hl = arrows[j][0]
        hw = arrows[j][1]
        
        if i == 1:
            mutation_scale = 2
        else:
            mutation_scale = 1
        
        posA = [x, y]
        posB = [x, y + dy]
        ast = "-|>, head_length = " + str(hl) + ", head_width = " + str(hw) 
        arrow = matplotlib.patches.FancyArrowPatch(posA = posA, posB = posB, connectionstyle = cs, arrowstyle = ast, mutation_scale = mutation_scale)
        ax.add_patch(arrow) 
        # ax.text(x, y + dy + dytext, "hl 15, hw 10", ha = "center")

        
        count += 1


# # make the arrow head a bit bigger
# x = 2
# y = 9
# dy = 2
# dytext = 0.5
# 
# posA = [x, y]
# posB = [x, y + dy]
# ast = "-|>, head_length = 15, head_width = 10" 
# arrow = matplotlib.patches.FancyArrowPatch(
#     posA = posA, 
#     posB = posB, 
#     connectionstyle = cs, 
#     arrowstyle = ast,
# )
# ax.add_patch(arrow) 
# ax.text(x, y + dy + dytext, "hl 15, hw 10", ha = "center")
# 
# 
# # make the arrow head a bit bigger
# x = 6
# y = 9
# dy = 2
# dytext = 0.5
# 
# posA = [x, y]
# posB = [x, y + dy]
# ast = "-|>, head_length = 30, head_width = 10" 
# arrow = matplotlib.patches.FancyArrowPatch(
#     posA = posA, 
#     posB = posB, 
#     connectionstyle = cs, 
#     arrowstyle = ast,
# )
# ax.add_patch(arrow) 
# ax.text(x, y + dy + dytext, "hl 30, hw 10", ha = "center")
# 
# 
# # make the arrow head a bit bigger
# x = 10
# y = 9
# dy = 2
# dytext = 0.5
# 
# posA = [x, y]
# posB = [x, y + dy]
# ast = "-|>, head_length = 10, head_width = 5" 
# arrow = matplotlib.patches.FancyArrowPatch(
#     posA = posA, 
#     posB = posB, 
#     connectionstyle = cs, 
#     arrowstyle = ast,
# )
# ax.add_patch(arrow) 
# ax.text(x, y + dy + dytext, "hl 10, hw 5", ha = "center")
# 
# 
# # make the arrow head a bit bigger
# x = 14
# y = 9
# dy = 2
# dytext = 0.5
# 
# posA = [x, y]
# posB = [x, y + dy]
# ast = "-|>, head_length = 10, head_width = 5" 
# arrow = matplotlib.patches.FancyArrowPatch(
#     posA = posA, 
#     posB = posB, 
#     connectionstyle = cs, 
#     arrowstyle = ast,
#     linewidth = 10
# )
# ax.add_patch(arrow) 
# ax.text(x, y + dy + dytext, "hl 10, hw 5", ha = "center")
# 
# 
# 
# 
# 
# # make the arrow head a bit bigger
# x = 14
# y = 6
# dy = 2
# dytext = 0.25
# 
# posA = [x, y]
# posB = [x, y + dy]
# ast = "-|>, head_length = 10, head_width = 5" 
# arrow = matplotlib.patches.FancyArrowPatch(
#     posA = posA, 
#     posB = posB, 
#     connectionstyle = cs, 
#     arrowstyle = ast,
#     linewidth = 10
# )
# ax.add_patch(arrow) 
# ax.text(x, y + dy + dytext, "hl 10, hw 5", ha = "center")
# 
# 
# 
# x = 14
# y = 3
# dy = 2
# dytext = 0.25
# 
# posA = [x, y]
# posB = [x, y + dy]
# ast = "-|>, head_length = 10, head_width = 5" 
# arrow = matplotlib.patches.FancyArrowPatch(
#     posA = posA, 
#     posB = posB, 
#     connectionstyle = cs, 
#     arrowstyle = ast,
#     mutation_scale = 2
# )
# ax.add_patch(arrow) 
# ax.text(x, y + dy + dytext, "hl 10, hw 5", ha = "center")
# 
# 
# x = 14
# y = 0.5
# dy = 2
# dytext = 0.25
# 
# posA = [x, y]
# posB = [x, y + dy]
# ast = "-|>, head_length = 10, head_width = 5" 
# arrow = matplotlib.patches.FancyArrowPatch(
#     posA = posA, 
#     posB = posB, 
#     connectionstyle = cs, 
#     arrowstyle = ast,
#     mutation_scale = 2
# )
# ax.add_patch(arrow) 
# ax.text(x, y + dy + dytext, "hl 10, hw 5", ha = "center")







ax.set_xlim(0,16)
ax.set_ylim(0,12)

plt.show()