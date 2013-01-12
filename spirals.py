"""
Graphene spirals
See http://arxiv.org/abs/1301.2226 page 4.
(The second page 4, not the first one!)
"""

from nano import *
import matplotlib

SPIRAL1 = r"""
              A-A
"""

SPIRAL2 = r"""
              A-A
             /    
            B     B
             \   /
              o-o
"""

SPIRAL3 = r"""
             
                    
              A-A
             /    
            B     B
             \   / 
              o-o  
             /   \ 
          C-o     o-C
             \   /
              o-o
"""

SPIRAL4 = r"""
             
                    
              A-A
             /    
            B     B
             \   / 
              o-o  
             /   \ 
          C-o     o-C
         /   \   /    
        D     o-o     D
         \   /   \   /
          o-o     o-o
             \   /
              o-o
"""

SPIRAL5 = r"""
             
                    
              A-A
             /    
            B     B
             \   / 
              o-o  
             /   \ 
          C-o     o-C
         /   \   /    
        D     o-o     D
         \   /   \   /
          o-o     o-o
         /   \   /   \
      E-o     o-o     o-E
         \   /   \   /
          o-o     o-o
             \   /
              o-o
"""

SPIRALS = [SPIRAL1, SPIRAL2, SPIRAL3, SPIRAL4, SPIRAL5]

for size in range(0, 5):
  num_atoms, dimension, bonds, atoms = parse_diagram(SPIRALS[size],
                                                     dimension_hint = 1)
  h_poly = compute_hamiltonian(num_atoms, atoms, bonds)
  matplotlib.pyplot.subplot(1, 5, size+1)
  display_band_structure_1d(num_atoms, h_poly, cycles = 6, phase_offset = math.pi/2)

matplotlib.pyplot.show()
