"""
Zigzag nanoribbon two cells wide
"""

from nano import *

CONJUGATED_CHAIN15 = r"""
o-o=o-o=o-o=o-o=o-o=o-o=o-o=o
"""

dx = 0.142*units.nanometre
dy = 0.142*units.nanometre

B = 0*units.tesla
flux_per_plaquette = dx*dy*B

num_atoms, dimension, bonds, atoms = parse_diagram(CONJUGATED_CHAIN15)
h_poly = compute_hamiltonian(num_atoms, atoms, bonds, flux_per_plaquette)
display_energy_levels_0d(CONJUGATED_CHAIN15, num_atoms, atoms, h_poly)
