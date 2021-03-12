"""
Script for generating points, performing RANSAC on said points, and creating images for my blog post.

Created by Chris Durrans
3/12/2021
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation 

x_range_max = 100
y_slope = 3

def line_value(x, slope, intercept, jitter):
    return slope * x + intercept + np.random.normal(0.0, jitter, 1)[0]

def generate_random_points(x_points, y_points, n):
    """
    x_points: list of x values [0, 1, 2, ...] to choose from
    y_points: list of y values [0, 1, 2, ...] to choose from
    n: number of points returned
    """
    selected_x = np.random.choice(x_points, n)
    selected_y = np.random.choice(y_points, n)
    result = np.stack((selected_x,selected_y),axis=1)
    print(result)
    return result

def select_random_points(points, num_points):
    """
    points: numpy array of points
    num_points: number of points to return
    """
    points_indices = np.random.choice([x for x in range(points.shape[0])],num_points,False)
    random_points = []
    for point in points_indices:
        random_points.append(all_points[point])
    #
    random_points = np.stack([p for p in random_points])
    return random_points

def distance_to_line(point, line_points):
    """
    point: expects list or array of [x, y]
    line_points : expects matrix of size (2,2) ie [[x1, y1],[x2, y2]]
    """
    x1 = line_points[0,0]
    x2 = line_points[1,0]
    y1 = line_points[0,1]
    y2 = line_points[1,1] 
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    x_pt = point[0]
    y_pt = point[1]
    distance = (a*x_pt + b*y_pt + c)/math.sqrt(a*a + b*b)
    return distance

def ransac2d(points, distance_tolerance, iterations):
    """
    points: numpy array of points shaped (n,2)
    distance_tolerance: include points within distance_tolerance to line
    iterations: number of times to run process to find best line and points
    """
    ransac_best = np.empty((0,2), float)
    best_line = np.empty((0,2), float)
    for i in range(iterations):
        line_points = select_random_points(points, 2)
        ransac_pts = np.empty((0,2), float)
        for indx, point in enumerate(points):
            distance = distance_to_line(point, line_points)
            if abs(distance) < distance_tolerance:
                ransac_pts = np.append(ransac_pts, point.reshape((1,2)), axis=0)
        if len(ransac_pts) > len(ransac_best):
            ransac_best = ransac_pts
            best_line = line_points
    return ransac_best, best_line


x_points = []
y_points = []
for x in range(x_range_max):
    x_points.append(x)
    y_points.append(line_value(x, y_slope, 3, 10))

inliers = np.array(list(zip(x_points,y_points)))

y_points_range = []
for y in range(int(x_range_max * y_slope)):
    y_points_range.append(y)

outliers = generate_random_points(x_points, y_points_range, 30)
all_points = np.concatenate((inliers,outliers))

# See example plot
# random_points = select_random_points(all_points, 2)
fig, ax = plt.subplots()
ax.scatter(all_points[:,0], all_points[:,1], alpha=0.5)
# ax.plot(random_points[:,0], random_points[:,1])
ax.set_xlabel(r'x', fontsize=15)
ax.set_ylabel(r'y', fontsize=15)
ax.set_title('Ransac Points')
ax.grid(True)
fig.tight_layout()
plt.show()

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], marker="o", ls="")

distance_tolerance = 10

def init():
    ax.set_xlim(0, x_range_max)
    ax.set_ylim(0, int(x_range_max * y_slope))
    ax.scatter(all_points[:,0], all_points[:,1], alpha=0.5)
    ax.set_xlabel(r'x', fontsize=15)
    ax.set_ylabel(r'y', fontsize=15)
    ax.set_title('Ransac Demo')
    ax.grid(True)
    return ln,

def update(frame):
    random_points = select_random_points(all_points, 2)
    ransac_pts = np.empty((0,2), float)
    for indx, point in enumerate(all_points):
        distance = distance_to_line(point, random_points)
        if abs(distance) < distance_tolerance:
            ransac_pts = np.append(ransac_pts, point.reshape((1,2)), axis=0)
    ln.set_data(list(ransac_pts[:,0]), list(ransac_pts[:,1]))
    return ln,

ani = FuncAnimation(fig, update, interval=500, frames=[x for x in range(10)],
                    init_func=init, blit=True)

plt.show()
# ani.save('C:/Files/cdurrans.github.io/images/RANSAC/ransac_search.gif', dpi=80, writer='pillow')

found_pts, best_line = ransac2d(all_points, 10, 50)

# Final Plot
fig, ax = plt.subplots()
ax.scatter(all_points[:,0], all_points[:,1], alpha=0.5)
ax.scatter(found_pts[:,0], found_pts[:,1], alpha=0.5)
ax.plot(best_line[:,0], best_line[:,1])
ax.set_xlabel(r'x', fontsize=15)
ax.set_ylabel(r'y', fontsize=15)
ax.set_title('Ransac Final Result')
ax.grid(True)
fig.tight_layout()
plt.show()