import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt
import pydot
import os
from networkx.drawing.nx_pydot import graphviz_layout

class Node:
    def __init__(self, id, point):
        self.id = id
        self.point = point
        self.left_node = None
        self.right_node = None

class KdTree:
    def __init__(self):
        self.root = None 
        self.G = nx.Graph()
        self.label_dict = dict()
        self.ids_set = set()
        self.sorted_ids = dict()
        self.save_images = False
        self.save_folder = os.getcwd()
        self.image_number = 0
    #
    def __insertHelper(self, node, point, id, depth):
        if node == None:
            node = Node(id, point)
        else:
            current_depth = depth % len(point)
            left = False
            if point[current_depth] < node.point[current_depth]:
                left = True
            if left:
                node.left_node = self.__insertHelper(node.left_node, point, id, depth+1)
                self.G.add_edge(node.id, node.left_node.id)
            else:
                node.right_node = self.__insertHelper(node.right_node, point, id, depth+1)
                self.G.add_edge(node.id, node.right_node.id)
        return node
    #
    def insert(self, point, id):
        if id in self.ids_set:
            raise ValueError(f"Point with id value: {id} already in tree.")
        self.ids_set.add(id)
        self.root = self.__insertHelper(self.root, point, id, 0)
        # self.plotTree()
        self.label_dict[id] = str(point)
        # if self.save_images:
        #     self.__save_image()
    #
    def __sortPoints(self, points_with_ids):
        """
        points_with_ids expects a dictionary with ids as the keys and points as the items
        """
        self.sorted_ids = dict()
        temp_key = list(points_with_ids.keys())[0]
        for idx in range(len(points_with_ids[temp_key])):
            sorted_points = sorted(points_with_ids.items(), key=lambda x: x[1][idx])
            sorted_ids = []
            for point_tuple in sorted_points:
                sorted_ids.append(point_tuple[0])
            self.sorted_ids[idx] = sorted_ids

    def insertPoints(self, points, ids):
        assert len(points) == len(ids)
        points_with_ids = dict(zip(ids, points))
        self.__sortPoints(points_with_ids)
        n = len(points)
        current_depth = 0
        while n:
            pt_id = self.sorted_ids[current_depth].pop(n//2)
            for key in self.sorted_ids.keys():
                if key == current_depth:
                    continue
                self.sorted_ids[key].remove(pt_id)
            self.insert(points_with_ids[pt_id], pt_id)
            current_depth = (current_depth + 1) % len(points_with_ids[pt_id])
            n -= 1

    def __searchHelper(self, target, node, depth, distance_tolerance, ids):
        if node:
            point_np = np.array(list(map(float,node.point)))
            target_np = np.array(list(map(float,target)))
            deltas = point_np - target_np
            distance_delta_ok = True
            for d in deltas:
                if abs(d) >= distance_tolerance:
                    distance_delta_ok = False
                    break
            #
            if distance_delta_ok:
                distance = 0.0
                for d in deltas:
                    distance = distance + (d * d)
                distance = np.sqrt(distance)
                if distance <= distance_tolerance:
                    ids.append(node.id)
            #
            current_depth = depth % len(target)
            if (target[current_depth] - distance_tolerance) < node.point[current_depth]:
                ids = self.__searchHelper(target, node.left_node, depth+1, distance_tolerance, ids)
            if (target[current_depth] + distance_tolerance) > node.point[current_depth]:
                ids = self.__searchHelper(target, node.right_node, depth+1, distance_tolerance, ids)
        return ids
    #
    def search(self, target, distance_tolerance):
        ids = []
        ids = self.__searchHelper(target, self.root, 0, distance_tolerance, ids)
        return ids
    #   
    def get_points(self):
        all_points = [self.root.point]
        current_level = [self.root]
        while current_level:
            next_level = list()
            for n in current_level:
                if n.left_node:
                    next_level.append(n.left_node)
                    all_points.append(n.left_node.point)
                if n.right_node:
                    next_level.append(n.right_node)
                    all_points.append(n.right_node.point)
            current_level = next_level
        return all_points
    #
    def plotTree(self):
        try:
            pos = graphviz_layout(self.G, prog="dot")
            nx.draw(self.G, pos, labels=self.label_dict, with_labels=True)
            plt.show()
        except Exception as ex:
            print(ex)
    #
    def enable_saving_imgs(self):
        self.save_images = True
    #
    def disable_saving_images(self):
        self.save_images = False
    #
    def set_saving_images_folder(self, file_directory):
        self.save_folder = file_directory
    #
    def __save_image(self):
        try:
            pos = graphviz_layout(self.G, prog="dot")
            nx.draw(self.G, pos, 
            labels=self.label_dict,
            with_labels=True)
            plt.savefig(os.path.join(self.save_folder,f"tree_img_{self.image_number}.png"))
            self.image_number += 1
        except Exception as ex:
            print(ex)





#Plot 2d plane in 3d plot
# import numpy as np
# import plotly.graph_objects as go
# height=2
# x= np.linspace(-1, 1, 75)
# y= np.linspace(0, 1, 100)
# z= height*np.ones((100,75))
# mycolorscale = [[0, '#aa9ce2'],
#                 [1, '#aa9ce2']]

# surf = go.Surface(x=x, y=y, z=z, colorscale=mycolorscale, showscale=False)
# layout = go.Layout(width=600,
#                   scene_camera_eye_z=0.75)
# fig = go.Figure(data=[surf], layout=layout)
# fig.show()




# checkValue = myTree.root
# while checkValue:
#     print(f"{checkValue.id}: {checkValue.point}")
#     checkValue = checkValue.left_node

