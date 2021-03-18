# cd C:\Files\cdurrans.github.io\post_code

import plotly.express as px
import plotly.graph_objects as go
import kdtree
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt
from random import seed
from random import randint

seed(1)
myTree = kdtree.KdTree()
pts = []
for id in range(0,45):
    pt = (randint(0, 10), randint(0, 10),randint(0, 10))
    pts.append(pt)
    # myTree.insert(pt, id)

ids = [id for id in range(0,45)]

myTree.insertPoints(pts,ids)


# import math
# import numpy as np

# def py_bivariate_normal_pdf(domain, mean, variance):
#     X = [[-mean+x*variance for x in range(int((-domain+mean)//variance), 
#                                                    int((domain+mean)//variance)+1)] 
#                   for _ in range(int((-domain+mean)//variance), 
#                                  int((domain+mean)//variance)+1)]
#     Y = [*map(list, zip(*X))]
#     R = [[math.sqrt(a**2 + b**2) for a, b in zip(c, d)] for c, d in zip(X, Y)]
#     Z = [[(1. / math.sqrt(2 * math.pi)) * math.exp(-.5*r**2) for r in r_sub] for r_sub in R]
#     X = [*map(lambda a: [b+mean for b in a], X)]
#     Y = [*map(lambda a: [b+mean for b in a], Y)]
#     return  np.array(X), np.array(Y), np.array(Z)

# x, y, z = py_bivariate_normal_pdf(3, 10, 3)
# index_values = [n for n in range(len(x))]


# fig = go.Figure(data=[go.Scatter3d(
#                 x=x,
#                 y=y,
#                 z=z,
#                 mode='markers'#,
#                 # marker=dict(
#                 #     color=combined['topic']
#                 # ),
#         # ,hoverinfo='text'
#         )])
# fig.show()


# myTree.traverse()
myTree.plotTree()



pts = np.array(pts)
index_values = [n for n in range(len(pts))]

fig = go.Figure(data=[go.Scatter3d(
                x=pts[:,0],
                y=pts[:,1],
                z=pts[:,2],
                mode='markers',
                # marker=dict(
                #     color=combined['topic']
                # ),
        hovertext=index_values
        # ,hoverinfo='text'
        )])
fig.show()