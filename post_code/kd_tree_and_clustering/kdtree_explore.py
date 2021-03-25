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
# myTree.enable_saving_imgs()
# myTree.set_saving_images_folder("C:/Files/images_kdtree/")
pts = []
n_pts = 10
for id in range(0,n_pts):
    pt = (randint(0, 10), randint(0, 10),randint(0, 10))
    pts.append(pt)
    # myTree.insert(pt, id)

ids = [id for id in range(0,n_pts)]

myTree.insertPoints(pts,ids)

# myTree.traverse()
myTree.plotTree()

# pts_np = np.array(pts)

# # fig = go.Figure(data=[go.Scatter3d(
# #                 x=pts_np[:,0],
# #                 y=pts_np[:,1],
# #                 z=pts_np[:,2],
# #                 mode='markers',
# #                 # marker=dict(
# #                 #     color=combined['topic']
# #                 # ),
# #         hovertext=ids
# #         # ,hoverinfo='text'
# #         )])
# # fig.show()

# search_pt = (6,8,10)
# distance_tolerance = 4

# result = myTree.search(search_pt, distance_tolerance)

# print("Nearby points: ",result)

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


# from clustering import Cluster
# import pandas as pd
# myCluster = Cluster()
# myCluster.load(pts)
# myCluster.cluster(3)
# myCluster.plot_3d()

# myCluster.plot_3d()
# fsname = "C:/Users/cdurrans/Downloads/536069_reports (1)/blog.csv"
# df = pd.read_csv(fsname)
# pts = list(df.to_records(index=False))

# test_ = []
# for p in pts:
#     test_.append(tuple(p))


# myCluster = Cluster()
# myCluster.load(pts)
# myCluster.cluster(600)

# myCluster.plot_3d()

# # import glob
# # from PIL import Image

# # # filepaths
# # fp_in = "/path/to/image_*.png"
# # fp_out = "/path/to/image.gif"

# # # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
# # img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
# # img.save(fp=fp_out, format='GIF', append_images=imgs,
# #          save_all=True, duration=200, loop=0)