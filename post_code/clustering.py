import kdtree

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
