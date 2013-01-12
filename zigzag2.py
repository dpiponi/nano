"""
Zigzag nanoribbon two cells wide.
Compare http://en.wikipedia.org/wiki/Graphene_nanoribbons
"""

from nano import *
import matplotlib

ZIGZAG2 = r"""
   A-B     C
  /   \   /
 o     o-o
  \   /   \
   A B     C
"""

num_atoms, dimension, bonds, atoms = parse_diagram(ZIGZAG2)
h_poly = compute_hamiltonian(num_atoms, atoms, bonds)
h = eval_hamiltonian(num_atoms, h_poly, (1, 1))
display_band_structure_1d(num_atoms, h_poly)

matplotlib.pyplot.show()
