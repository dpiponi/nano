"""
Zigzag nanoribbon two cells wide
"""

from nano import *
import matplotlib

CONJUGATED_CHAIN15 = r"""
o-o=o-o=o-o=o-o=o-o=o-o=o-o=o
"""

num_atoms, dimension, bonds, atoms = parse_diagram(CONJUGATED_CHAIN15)
h_poly = compute_hamiltonian(num_atoms, atoms, bonds)
display_energy_levels_0d(CONJUGATED_CHAIN15, num_atoms, atoms, h_poly)

matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()
