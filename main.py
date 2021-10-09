import numpy as np
import src


if __name__ == '__main__':
    d = str(input('Choose a bravais lattice type (eg: cubicp): '))
    src.plot.LatticePlot(src.lattice.getLattice(d))
