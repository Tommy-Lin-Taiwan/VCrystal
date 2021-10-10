import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import src
from src import lattice, exceptions

PI = math.pi


def add_title(ax, plot_title):
    ax.set_title(plot_title)


def scatters(ax, points):
    for point in points:
        ax.scatter(float(point[0]), float(point[1]),
                   float(point[2]), c=point[3])


def plotlines(ax, points, color='r'):
    for i in range(points[0].length):
        for j in range(i, points[0].length):
            ax.plot([float(points[0][i]), float(points[1][i]), float(points[2][i])], [
                    float(points[0][j]), float(points[1][j]), float(points[2][j])], c=color)


def LatticePlot(tier: int, plot_title=None, lines=False, show_conventional=True, show_primitive=False):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if(plot_title != None):
        add_title(plot_title)
    if(lines):
        pass
    else:
        if(show_conventional):
            points_conv = lattice.getLattice(tier)
            scatters(ax, points_conv)
        if(show_primitive):
            points_prim = lattice.getPrimitiveLattice(tier)
            scatters(ax, points_prim)
    plt.show()
