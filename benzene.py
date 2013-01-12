"""
I don't know if this really represents benzene.
But these two should give the same result.
"""

from nano import *
import matplotlib

BENZENE1 = r"""
   A-o-o-o-o-o-A
"""

BENZENE2 = r"""
    o-o
   /   \
  o     o
   \   /
    o-o
"""

num_atoms, dimension, bonds, atoms = parse_diagram(BENZENE2, dimension_hint = None, joins = 'A')
h_poly = compute_hamiltonian(num_atoms, atoms, bonds)
simple_display_energy_levels_0d(num_atoms, h_poly)

matplotlib.pyplot.show()
