"""
Armchair nanoribbon one cell wide
"""

from nano import *

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

diagram = ARMCHAIR1
B = 0

num_atoms, dimension, bonds, atoms = parse_diagram(ARMCHAIR1)
h_poly = compute_hamiltonian(num_atoms, atoms, bonds, B)
h = eval_hamiltonian(num_atoms, h_poly, (1, 1))
display_band_structure_1d(num_atoms, h_poly)
