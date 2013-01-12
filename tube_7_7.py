"""
Compare http://en.wikipedia.org/wiki/Carbon_nanotube
In particular: http://en.wikipedia.org/wiki/File:Carbon_nanotube_bands.gif
"""

from nano import *
import matplotlib

TUBE_7_7a = r"""
  a
 / \
A   A
|    
B   B
 \ / 
  o   
  |
  o
 / \ 
C   C
|    
D   D
 \ / 
  o
  |
  o
 / \ 
E   E
|    
F   F
 \ / 
  o
  |
  o
 / \ 
G   G
|    
H   H
 \ / 
  o
  |
  o
 / \ 
I   I
|    
J   J
 \ / 
  o
  |
  o
 / \ 
K   K
|    
L   L
 \ / 
  o
  |
  o
 / \ 
M   M
|    
N   N
 \ / 
  o
  |
  a
"""

TUBE_7_7b = r"""
  A-B     C-D     E-F     G-H     I-J     K-L     M-N    
 /   \   /   \   /   \   /   \   /   \   /   \   /   \   
a     o-o     o-o     o-o     o-o     o-o     o-o     o-a
 \   /   \   /   \   /   \   /   \   /   \   /   \   /   
  A B     C D     E F     G H     I J     K L     M N    
"""

num_atoms, dimension, bonds, atoms = parse_diagram(TUBE_7_7a, dimension_hint = None, joins = 'a')
h_poly = compute_hamiltonian(num_atoms, atoms, bonds)
display_band_structure_1d(num_atoms, h_poly)

matplotlib.pyplot.show()
