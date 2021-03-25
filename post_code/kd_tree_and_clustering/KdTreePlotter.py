import numpy as np
from matplotlib import pyplot as plt
from dataclasses import dataclass
import kdtree

class KdTreePlotter:
    def __init__(self, tree):
        self.iteration = 0
        self.fig, self.ax = plt.subplots(1)
        self.tree = tree
        self.pts = self.pts = np.array(self.tree.get_points())
        self.plot = None
    
    @dataclass
    class Window:
        x_min: int
        x_max: int
        y_min: int
        y_max: int
        
    def __plot_2dTree(self, node, window, depth):
        if node:
            upper_window = window
            lower_window = window
            if depth % 2 == 0:
                x_pt = node.point[0]
                plt.plot([x_pt, x_pt],[window.y_min, window.y_max])
                lower_window.x_max = x_pt
                upper_window.x_min = x_pt
            else:
                y_pt = node.point[1]
                plt.plot([window.x_min, window.x_max],[y_pt, y_pt])
                lower_window.y_max = y_pt
                upper_window.y_min = y_pt
            self.__plot_2dTree(node.left_node, lower_window, depth+1)
            self.__plot_2dTree(node.right_node, upper_window, depth+1)
    #
    def __create_window(self):
        x_min = self.pts[:,0].min()
        x_max = self.pts[:,0].max()
        y_min = self.pts[:,1].min()
        y_max = self.pts[:,1].max()
        return self.Window(x_min, x_max, y_min, y_max)
        
        
    def plot_2dTree(self):
        assert len(self.tree.root.point) == 2,f"Must be a 2d tree, not a {len(self.tree.root.point)} one"
        window = self.__create_window()
        self.__plot_2dTree(self.tree.root, window, 0)
        plt.scatter(self.pts[:,0], self.pts[:,1])
        plt.show()





from matplotlib import pyplot as plt
pts = np.array([
(8, 7),
(6, 10),
(7, 12),
(2, 8),
(1, 14),
(2, 13),
(4, 13),
(2, 10),
(9, 4),
(5, 4),
(9, 3)])

myTree = kdtree.KdTree()
ids = [x for x in range(len(pts))]
myTree.insertPoints(pts,ids)
myTree.plotTree()

tree_plt = KdTreePlotter(myTree)
tree_plt.plot_2dTree()