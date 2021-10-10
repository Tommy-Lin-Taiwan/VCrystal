import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import vcrystal
from vcrystal import lattice, exceptions

PI = math.pi


def __add_title(ax, plot_title):
    ax.set_title(plot_title)


def __scatters(ax, points, size):
    print(f'points = {points}')
    for point in points:
        print(point)
        ax.scatter(float(point[0]), float(point[1]),
                   float(point[2]), c=point[3], s=size)


def __plotlines(ax, points, color='r'):
    for i in range(points[0].length):
        for j in range(i, points[0].length):
            ax.plot([float(points[0][i]), float(points[1][i]), float(points[2][i])], [
                    float(points[0][j]), float(points[1][j]), float(points[2][j])], c=color)


def __plot_type(type: str):
    # this space-filling size needs to be determined by the crystal structure!!
    if(type[:4] == 'spac'):
        return 10000
    elif(type[:4] == "ball"):
        return 1500
    elif(type == 'dot'):
        return 20


def LatticePlot(tier: int, atom_type='space_filling', plot_title=None, lines=False, show_conventional=True, show_primitive=False, size_restrain=False, origin=0.0, restraint=1.0, out_of_box_mode='delete'):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    atom_size = __plot_type(atom_type)
    if(plot_title != None):
        __add_title(plot_title)
    if(lines):
        pass
    else:
        if(show_conventional):
            points_conv = lattice.getLattice(tier)
            if(size_restrain):
                points_conv = lattice.sizeRestraint(
                    points_conv, origin=origin, unit_size=restraint, mode=out_of_box_mode)
                print(points_conv)
            __scatters(ax, points_conv, size=atom_size)
        if(show_primitive):
            points_prim = lattice.getPrimitiveLattice(tier)
            print(f'1.{points_prim}')
            if(size_restrain):
                points_prim = lattice.sizeRestraint(
                    points_prim, origin=origin, unit_size=restraint, mode=out_of_box_mode)
                print(f'2.{points_prim}')
            __scatters(ax, points_prim, size=atom_size)
    plt.show()
