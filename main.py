import numpy as np
import src
from src import lattice
from src import plot


if __name__ == '__main__':
    d = str(input('Choose a bravais lattice type (eg: cubicp): '))
    plot.LatticePlot(tier=lattice.tiers(d), show_primitive=True)
