import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

PI = math.pi


def createPlot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    return ax


def LatticePlot(ax, points: np.array, plot_title=None):
    if(plot_title != None):
        ax.set_title(plot_title)
    for i in range(points[0].length):
        ax.scatter(points[0][i], points[1][i], points[2][i], c=points[3][i])
    return ax


def plot(plt):
    plt.plot
