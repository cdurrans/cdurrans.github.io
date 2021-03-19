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

# myTree.traverse()
# myTree.plotTree()

pts_np = np.array(pts)

# fig = go.Figure(data=[go.Scatter3d(
#                 x=pts_np[:,0],
#                 y=pts_np[:,1],
#                 z=pts_np[:,2],
#                 mode='markers',
#                 # marker=dict(
#                 #     color=combined['topic']
#                 # ),
#         hovertext=ids
#         # ,hoverinfo='text'
#         )])
# fig.show()

search_pt = (6,8,10)
distance_tolerance = 4

result = myTree.search(search_pt, distance_tolerance)

print("Nearby points: ",result)

# plot_pts = np.vstack((pts_np,search_pt))

# color_type = list()
# for x in range(len(plot_pts)-1):
#     if x in result:
#         color_type.append("lightgreen")
#     else:
#         color_type.append("lightblue")
# #

# color_type.append("orange")

# fig = go.Figure(data=[go.Scatter3d(
#                 x=plot_pts[:,0],
#                 y=plot_pts[:,1],
#                 z=plot_pts[:,2],
#                 mode='markers',
#                 marker=dict(
#                     color=color_type
#                 ),
#         hovertext=ids
#         # ,hoverinfo='text'
#         )])
# fig.show()


from clustering import Cluster

myCluster = Cluster()
myCluster.load(pts)
myCluster.cluster(3)

myCluster.found_clusters


clusters_joined = list()
clusters_colors = list()

for cluster in myCluster.found_clusters:
    rgb = (randint(0, 255), randint(0, 255),randint(0, 255))
    for pt in cluster:
        clusters_joined.append(pt)
        clusters_colors.append(rgb)


clusters_joined = np.array(clusters_joined)
fig = go.Figure(data=[go.Scatter3d(
                x=clusters_joined[:,0],
                y=clusters_joined[:,1],
                z=clusters_joined[:,2],
                mode='markers',
                marker=dict(
                    color=clusters_colors
                ),
        hovertext=ids
        # ,hoverinfo='text'
        )])
fig.show()