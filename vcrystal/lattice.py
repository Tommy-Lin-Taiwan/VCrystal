import numpy as np
import pandas as pd
from vcrystal import exceptions


def caseconv(string):
    return string.lower()


def tiers(type):
    type = caseconv(type)
    w1 = type[:5]
    t = type[-1]
    if(w1 == 'cubic'):
        if(t == 'p'):
            return 0
        elif(t == 'i'):
            return 1
        elif(t == 'f'):
            return 2
        else:
            exceptions.errors(0)
    elif(w1 == 'tetra'):
        if(t == 'p'):
            return 3
        elif(t == 'i'):
            return 4
        else:
            exceptions.errors(0)
    elif(w1 == 'hexag'):
        return 5
    elif(w1 == 'trigo'):
        return 6
    else:
        exceptions.errors(0)


def getLattice(tier: int):
    # cubic p lattice
    if(tier == 0):
        # array = [[x,y,z,show_color]]
        return np.array([
            [0.0, 0.0, 0.0, 'b'],
            [0.0, 0.0, 1.0, 'b'],
            [0.0, 1.0, 0.0, 'b'],
            [0.0, 1.0, 1.0, 'b'],
            [1.0, 0.0, 0.0, 'b'],
            [1.0, 0.0, 1.0, 'b'],
            [1.0, 1.0, 0.0, 'b'],
            [1.0, 1.0, 1.0, 'b'],
        ])

    # cubic I lattice
    elif(tier == 1):
        return np.array([
            [0.0, 0.0, 0.0, 'b'],
            [0.0, 0.0, 1.0, 'b'],
            [0.0, 1.0, 0.0, 'b'],
            [0.0, 1.0, 1.0, 'b'],
            [1.0, 0.0, 0.0, 'b'],
            [1.0, 0.0, 1.0, 'b'],
            [1.0, 1.0, 0.0, 'b'],
            [1.0, 1.0, 1.0, 'b'],
            [0.5, 0.5, 0.5, 'b'],
        ])

    # cubic F lattice
    elif(tier == 2):
        return np.array([
            [0.0, 0.0, 0.0, 'b'],
            [0.0, 0.0, 1.0, 'b'],
            [0.0, 1.0, 0.0, 'b'],
            [0.0, 1.0, 1.0, 'b'],
            [1.0, 0.0, 0.0, 'b'],
            [1.0, 0.0, 1.0, 'b'],
            [1.0, 1.0, 0.0, 'b'],
            [1.0, 1.0, 1.0, 'b'],
            [0.5, 0.5, 0.0, 'b'],
            [0.5, 0.5, 1.0, 'b'],
            [0.5, 0.0, 0.5, 'b'],
            [0.5, 1.0, 0.5, 'b'],
            [0.0, 0.5, 0.5, 'b'],
            [1.0, 0.5, 0.5, 'b'],
        ])
    else:
        return False


def getPrimitiveLattice(tier: int):
    # cubic P lattice
    if(tier == 0):
        res = getLattice(0)
        for point in res:
            point[3] = 'r'
        return res

    # cubic I lattice
    elif(tier == 1):
        # primitive vectors = a/2[1,1,1], [1,-1,1], [1,1,-1]
        return np.array([
            [0.0, 0.0, 0.0, 'r'],
            [0.5, 0.5, 0.5, 'r'],
            [0.5, -0.5, 0.5, 'r'],
            [0.5, 0.5, -0.5, 'r'],
            [1.0, 0.0, 1.0, 'r'],
            [1.0, 1.0, 0.0, 'r'],
            [1.0, 0.0, 0.0, 'r'],
            [1.5, 0.5, 0.5, 'r']
        ])
    else:
        return False

# need more consideration of array dtype


def constructor():
    arr = np.empty()
    i = 0
    while(True):
        i += 1
        x = str(input(f'Enter the {i}th x coordinate: '))
        y = str(input(f'Enter the {i}th y coordinate: '))
        z = str(input(f'Enter the {i}th z coordinate: '))
        color = str(
            input(f'Enter the {i}th color for the coordinate: ')).lower()
        if(color == 'blue' or color == 'b'):
            color = 'b'
        ex = str(input('Enter more sets of coordinates? y/n :'))
        # np.concatenate or arr.append()?
        arr = np.concatenate(arr, np.array([x, y, z, color]))
        if(ex.lower() == 'n'):
            break
    return arr


def addMotif(lattice: np.array, basis=None):
    # lattice: an 2d array
    # basis: an 2d array, [x,y,z,color]
    if(basis == None):
        pass
    else:
        if(type(basis) != np.array):
            exceptions.errors(1)
            pass
        else:
            newpoints = np.empty()
            for point in lattice:
                for motifs in basis:
                    if(motifs[0] == 0 and motifs[1] == 0 and motifs[2] == 0):
                        continue
                    else:
                        # newpoint = [x1+x2, y1+y2, z1+z2, motifs_color] then turned into str
                        newpoint = np.array[float(point[0])+float(motifs[0]), float(
                            point[1])+float(motifs[1]), float(point[2])+float(motifs[2]), motifs[3]]
                        newpoints = np.concatenate(newpoints, newpoint)
            lattice = np.concatenate(lattice, newpoints)
            return lattice


def __isInParam(point, origin, x_pos, y_pos, z_pos):
    if(point[0] < origin or point[0] > x_pos or point[1] < origin or point[1] > y_pos or point[2] < origin or point[2] > z_pos):
        return False
    else:
        return True


def __delByIndex(lattice, indices):
    # indices must be a list of integers
    for index in indices:
        lattice = np.delete(lattice, index)
    return lattice


def __changeByIndex(lattice, index_change, replace_with, indices: list):
    for index in indices:
        lattice[index][index_change] = replace_with
    return lattice


def sizeRestraint(lattice: np.array, origin=0.0, unit_size=1.0, mode='delete', color_select='auto'):
    x_pos, y_pos, z_pos = origin + unit_size
    disqualify = []
    index = 0
    for point in lattice:
        if(__isInParam(point, origin, x_pos, y_pos, z_pos)):
            index += 1
        else:
            disqualify.append(index)
            index += 1

    if(mode == 'delete'):
        return __delByIndex(lattice, disqualify)
    elif(mode == 'color'):
        if(color_select == 'auto'):
            c = 'grey'
        else:
            c = str(input(f'Input the color intended for out-of-box atoms: '))
        return __changeByIndex(lattice, 3, c, disqualify)
