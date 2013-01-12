"""
Compare http://en.wikipedia.org/wiki/Carbon_nanotube
In particular: http://en.wikipedia.org/wiki/File:Carbon_nanotube_bands.gif
"""

from nano import *
import matplotlib

TUBE_6_0a = r"""
    a-b     
   /   \   
  A     o-A 
   \   /    
    o-o      
   /   \    
  B     o-B 
   \   /    
    o-o      
   /   \    
  C     o-C 
   \   /    
    o-o      
   /   \    
  D     o-D 
   \   /    
    o-o     
   /   \    
  E     o-E 
   \   /    
    o-o     
   /   \    
  F     o-F      
   \   /
    a b
       
"""

TUBE_6_0b = r"""
  A   B   C   D   E   F  
 / \ / \ / \ / \ / \ / \ 
a   o   o   o   o   o   a
|   |   |   |   |   |    
b   o   o   o   o   o   b
 \ / \ / \ / \ / \ / \ / 
  o   o   o   o   o   o  
  |   |   |   |   |   |  
  A   B   C   D   E   F  
"""

num_atoms, dimension, bonds, atoms = parse_diagram(TUBE_6_0b, dimension_hint = None, joins = 'ab')
h_poly = compute_hamiltonian(num_atoms, atoms, bonds)
display_band_structure_1d(num_atoms, h_poly)

matplotlib.pyplot.show()
