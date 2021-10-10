import numpy as np
import pandas as pd
from src import exceptions


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
        return getLattice('cubicp')

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


def constructor():
    arr_x, arr_y, arr_z = []
    i = 0
    while(True):
        x = float(input(f'Enter the {i}th x coordinate: '))
        arr_x.append(x)
        y = float(input(f'Enter the {i}th y coordinate: '))
        arr_y.append(y)
        z = float(input(f'Enter the {i}th z coordinate: '))
        arr_z.append(z)
        ex = str(input('Enter more sets of coordinates? y/n :'))
        if(ex.lower() == 'n'):
            break
    final = np.array(arr_x, arr_y, arr_z)
    return final
