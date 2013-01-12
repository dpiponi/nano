"""
Doubly bearded ribbon.
"""

from nano import *
import matplotlib

BEARDED_BEARDED5 = r"""
       A-B     C-D     E-F
      /   \   /   \   /   \
   o-o     o-o     o-o     o-o
      \   /   \   /   \   /
       A B     C D     E F
"""

num_atoms, dimension, bonds, atoms = parse_diagram(BEARDED_BEARDED5)
h_poly = compute_hamiltonian(num_atoms, atoms, bonds, 0)
h = eval_hamiltonian(num_atoms, h_poly, (1, 1))
display_band_structure_1d(num_atoms, h_poly)

matplotlib.pyplot.show()
