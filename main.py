import numpy as np
import vcrystal
from vcrystal import lattice
from vcrystal import plot


if __name__ == '__main__':
    d = str(input('Choose a bravais lattice type (eg: cubicp): '))
    plot.LatticePlot(tier=lattice.tiers(
        d), atom_type='space_filling', show_primitive=True)
