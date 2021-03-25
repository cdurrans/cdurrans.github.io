import numpy as np
from matplotlib import pyplot as plt
from dataclasses import dataclass
import dataclasses
import kdtree

class KdTreePlotter:
    def __init__(self, tree):
        self.iteration = 0
        self.tree = tree
        self.pts = self.pts = np.array(self.tree.get_points())
        self.plot_data = []
    
    @dataclass
    class Window:
        x_min: int
        x_max: int
        y_min: int
        y_max: int
        
    def __plot_2dTree(self, node, window, depth):
        if node:
            upper_window = dataclasses.replace(window)
            lower_window = dataclasses.replace(window)
            if depth % 2 == 0:
                x_pt = node.point[0]
                self.plot_data.append(([x_pt, x_pt],[window.y_min, window.y_max]))
                lower_window.x_max = x_pt
                upper_window.x_min = x_pt
            else:
                y_pt = node.point[1]
                self.plot_data.append(([window.x_min, window.x_max],[y_pt, y_pt]))
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
        fig, ax = plt.subplots()
        plt.scatter(self.pts[:,0], self.pts[:,1])
        for plot_line in self.plot_data:
            # print(plot_line)
            ax.plot(plot_line[0],plot_line[1])
            # plt.pause(0.5)
        plt.show()






