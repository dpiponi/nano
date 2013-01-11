"""
Doubly bearded ribbon.
"""

from nano import *

BEARDED_BEARDED5 = r"""
       A-B     C-D     E-F
      /   \   /   \   /   \
   o-o     o-o     o-o     o-o
      \   /   \   /   \   /
       A B     C D     E F
"""

dx = 0.142*units.nanometre
dy = 0.142*units.nanometre

B = 0*units.tesla
flux_per_plaquette = dx*dy*B

num_atoms, dimension, bonds, atoms = parse_diagram(BEARDED_BEARDED5)
h_poly = compute_hamiltonian(num_atoms, atoms, bonds, flux_per_plaquette)
h = eval_hamiltonian(num_atoms, h_poly, (1, 1))
display_band_structure_1d(num_atoms, h_poly)
