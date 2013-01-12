"""
Armchair nanoribbon one cell wide
Compare http://en.wikipedia.org/wiki/Graphene_nanoribbons
"""

from nano import *
import matplotlib

ARMCHAIR1 = r"""
   A   B
   |   |
   o   o
    \ /
     o
     |
     o
    / \
   A   B
"""

num_atoms, dimension, bonds, atoms = parse_diagram(ARMCHAIR1)
h_poly = compute_hamiltonian(num_atoms, atoms, bonds)
h = eval_hamiltonian(num_atoms, h_poly, (1, 1))
display_band_structure_1d(num_atoms, h_poly)

matplotlib.pyplot.show()
