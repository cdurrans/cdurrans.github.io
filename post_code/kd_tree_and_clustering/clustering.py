import kdtree
import plotly.graph_objects as go
import numpy as np 
import matplotlib.pyplot as plt
from random import randint

class Cluster:
    def __init__(self):
        self.processed = []
        self.points = []
        self.ids = []
        self.found_clusters = []

    def load(self, points):
        self.ids = [id for id in range(len(points))]
        self.points = points
        self.processed = [False for x in range(len(points))]

    def cluster(self, distance_tolerance):
        if not self.points:
            raise ValueError("Need to load points data first")
        tree = kdtree.KdTree()
        tree.insertPoints(self.points, self.ids)
        i = 0
        while i < len(self.points):
            if self.processed[i]:
                i += 1
                continue
            else:
                cluster = []
                cluster = self.__clusterHelper(i, cluster, tree, distance_tolerance)
                self.found_clusters.append(cluster)

    def __clusterHelper(self, indx, cluster, tree, distance_tolerance):
        self.processed[indx] = True 
        cluster.append(self.points[indx])
        nearest_ids = tree.search(self.points[indx], distance_tolerance)
        for id in nearest_ids:
            if not self.processed[id]:
                cluster = self.__clusterHelper(id, cluster, tree, distance_tolerance)
        return cluster
    
    def plot_3d(self):
        clusters_joined = list()
        clusters_colors = list()

        for cluster in self.found_clusters:
            rgb = (randint(0, 255), randint(0, 255),randint(0, 255))
            for pt in cluster:
                clusters_joined.append(pt)
                clusters_colors.append(rgb)

        clusters_joined = np.array(clusters_joined)
        dim_of_pts = (len(self.points[0]))
        try:
            xdata = clusters_joined[:,0]
            ydata = clusters_joined[:,1]
            zdata = clusters_joined[:,2]
        except Exception as ex:
            print(ex)
            clusters_joined = clusters_joined.view((clusters_joined.dtype[0], len(clusters_joined.dtype.names)))
            xdata = clusters_joined[:,0]
            ydata = clusters_joined[:,1]
            zdata = clusters_joined[:,2]

        fig = go.Figure(data=[go.Scatter3d(
                        x=xdata,
                        y=ydata,
                        z=zdata,
                        mode='markers',
                        marker=dict(
                            color=clusters_colors
                        ),
                hovertext=self.ids
                # ,hoverinfo='text'
                )])
        fig.show()
        return fig
