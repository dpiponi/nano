"""
Compute energy levels and band structures for atomic nanostructures
drawn with ASCII art.
"""

import numpy
import numpy.linalg
import matplotlib.pyplot
import math
import sys
import operator
import units

diagram = r"""
       o-o
      /   \
     o     o-o
      \   /   \
       o-o     o
      /   \   /
     o     o-o
      \   /
       o-o
"""

diagram = r"""
       o-o
      /   \
   o-o     o-o
  /   \   /   \
 o     o-o     o
  \   /   \   /
   o-o     o-o
      \   /
       o-o
"""

diagram = r"""
o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o
"""

diagram = r"""
       o-o
      /   \
     o     o
      \   /
       o-o
"""

diagram = r"""
o-o=o-o=o-o=o-o=o-o=o-o=o-o=o
"""

diagram = r"""
          o-o
         /   \
      o-o     o-o
     /   \   /   \
  o-o     o-o     o-o
 /   \   /   \   /   \
o     o-o     o-o     o
 \   /   \   /   \   /
  o-o     o-o     o-o
"""

diagram = r"""
      o-o
     /   \
  o-o     o-o
 /   \   /   \
o     o-o     o-o
 \   /   \   /   \
  o-o     o-o     o
     \   /   \   /
      o-o     o-o
         \   /
          o-o
"""

diagram = r"""
          A-o
         /   \
      C-o     A
     /   \
  E-o     C
     \
      E
"""

diagram = r"""
      o-o
     /   \
    A     o-A
     \   /
      o-o
"""

diagram = r"""
      o-o
     /   \
    A     o-A
     \   /
      B-o     B
         \   /
          o-o
"""

diagram = r"""
      o-o
     /   \
    A     o-A
     \   /
      o-o
     /   \
    B     o-B
     \   /
      o-o
"""

diagram = r"""
    A-B
   /   \
  o     o
   \   /
    A B
"""

diagram = r"""
    A-B     C-D
   /   \   /   \
  o     o-o     o
   \   /   \   /
    A B     C D
"""

diagram = r"""
    A-B     C-D     E-F     G-H
   /   \   /   \   /   \   /   \
  o     o-o     o-o     o-o     o
   \   /   \   /   \   /   \   /
    A B     C D     E F     G H
"""

diagram = r"""
    A-B     C-D     E-F     G-H     I-J
   /   \   /   \   /   \   /   \   /   \
  o     o-o     o-o     o-o     o-o     o
   \   /   \   /   \   /   \   /   \   /
    o-o     o-o     o-o     o-o     o-o
   /   \   /   \   /   \   /   \   /   \
  o     o-o     o-o     o-o     o-o     o
   \   /   \   /   \   /   \   /   \   /
    A B     C D     E F     G H     I J
"""

diagram = r"""
    A-B     C-D     E-F     G-H     I-J
   /   \   /   \   /   \   /   \   /   \
  o     o-o     o-o     o-o     o-o     o
   \   /   \   /   \   /   \   /   \   /
    A B     C D     E F     G H     I J
"""

diagram = r"""
    A-B     C-D     E-F     G-H     I-J
   /   \   /   \   /   \   /   \   /   \
  o     o-o     o-o     o-o     o-o     o
   \   /   \   /           \   /   \   /
    o-o     o-o             o-o     o-o
   /   \   /   \           /   \   /   \
  o     o-o     o-o     o-o     o-o     o
   \   /   \   /   \   /   \   /   \   /
    A B     C D     E F     G H     I J
"""

diagram = r"""
    A-B     C-D     E-F
   /   \   /   \   /   \
  o     o-o     o-o     o-o
   \   /   \   /   \   /   \
    o-o     o-o     o-o     o-o
       \   /   \   /   \   /   \
        o-o     o-o     o-o     o-o
           \   /   \   /   \   /   \
            o-o     o-o     o-o     o-o
               \   /   \   /   \   /   \
                o-o     o-o     o-o     o
                   \   /   \   /   \   /
                    A B     C D     E F
"""

diagram = r"""
      o-o
     /   \
    A     o-A
     \   /
      o-o
     /   \
    C     o-C
     \   /
      D-o     D
         \   /
          o-o
"""

diagram = r"""
       o-o
      /   \
     o     o-o
      \   /   \
       o-o     o
          \   /
           o-o
"""

diagram = r"""

  o-o-o-o

"""

diagram = r"""
      o-o
     /   \
    A     o-A
     \   /
      o-o
     /   \
    C     o-C
     \   /
      D-o     D
         \   /
          o-o
"""

diagram = r"""
      o-o
     /   \
  o-o     o-o
 /   \   /   \
o     o-o     o
 \   /   \   /
  o-o     o-o
 /   \   /   \
o     o-o     o
 \   /   \   /
  o-o     o-o
     \   /
      o-o
"""

diagram = r"""
       A
       |
       o   o
      / \ / \
     o   o   o
     |   |   |
     o   o   o
      \ / \ /
       A   o
"""

diagram = r"""
   A       B
   |       |
   o   o   o   o   o
  / \ / \ / \ / \ / \
 o   o   o   o   o   o
 |   |   |   |   |   |
 o   o   o   o   o   o
  \ / \ / \ / \ / \ /
   o   A   o   B   o
"""

diagram = r"""
    A                 F
   /                   \
  o     o-o             o-o
   \   /   \               \
    o-o     o-o     o-o     o-o
       \       \   /   \       \
        o-o     o-o     o-o     o-o
           \       \       \   /   \
            o-o     o-o     o-o     o-o
               \   /   \   /           \
                o-o     o-o             o
                   \                   /
                    A                 F
"""

diagram = r"""
    A-B     C
   /   \   /
  o     o-o
   \   /   \
    A B     C
"""

diagram = r"""
o-o=o-o=o-o=o-o=o-o=o-o=o-o=o
"""

ZIGZAG1 = r"""
   A-B
  /   \
 o     o
  \   /
   A B
"""

ZIGZAG2 = r"""
   A-B     C
  /   \   /
 o     o-o
  \   /   \
   A B     C
"""

ZIGZAG5 = r"""
    A-B     C-D     E-F
   /   \   /   \   /   \
  o     o-o     o-o     o
   \   /   \   /   \   /
    A B     C D     E F
"""

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

ARMCHAIR2 = r"""
   A   B
   |   |
   o   o
    \ / \
     o   o
     |   |
     o   o
    / \ /
   A   B
"""

ARMCHAIR3 = r"""
   A   B   C
   |   |   |
   o   o   o
    \ / \ /
     o   o
     |   |
     o   o
    / \ / \
   A   B   C
"""

BEARDED_ZIGZAG2 = r"""
     A-B     C
    /   \   /
 o-o     o-o
    \   /   \
     A B     C
"""

BEARDED_BEARDED5 = r"""
       A-B     C-D     E-F
      /   \   /   \   /   \
   o-o     o-o     o-o     o-o
      \   /   \   /   \   /
       A B     C D     E F
"""

INTERFACE = r"""
o-o=o-o=o-o=o-o=o=o-o=o-o=o-o=o
"""

GRID23 = r"""
  o-o     o-o  
 /   \   /   \ 
o     o-o     o
 \   /   \   / 
  o-o     o-o  
 /   \   /   \ 
o     o-o     o
 \   /   \   / 
  o-o     o-o  
"""

GRID35 = r"""
  o-o     o-o     o-o
 /   \   /   \   /   \
o     o-o     o-o     o
 \   /   \   /   \   /
  o-o     o-o     o-o
 /   \   /   \   /   \
o     o-o     o-o     o
 \   /   \   /   \   /
  o-o     o-o     o-o
 /   \   /   \   /   \
o     o-o     o-o     o
 \   /   \   /   \   /
  o-o     o-o     o-o
     \   /   \   /
      o-o     o-o
"""

SIMPLE1 = r"""
A-B
| |
A B
"""

SIMPLE2 = r"""
A-B
| |
o-o
| |
A B
"""

MANY = r"""
A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z-a-b-c-d-e-f
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f
"""

#import console
numpy.set_printoptions(linewidth=200)

def vec(x, y):
    """
    Construct 2D numpy integer vector.
    This type is used for representing vectors within a nano-ribbon
    diagram.
    """
    return numpy.array([x, y], dtype = numpy.int32)

bond_types = {
    '/' : (1.0, vec(1, -1), vec(-1, 1)),
    '\\': (1.0, vec(-1, -1), vec(1, 1)),
    '-' : (1.0, vec(0, -1), vec(0, 1)),
    '=' : (1.5, vec(0, -1), vec(0, 1)),
    '|' : (1.0, vec(-1, 0), vec(1, 0))
}

def parse_diagram(diagram):
    p = diagram.split('\n')
    num_atoms = 0
    dimension = 0
    period0 = None
    period1 = None

    atoms = {}
    bonds = []
    orig_map = {}

    i = 0
    for row in p:
        j = 0
        for col in row:
            if col in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnpqrstuvwxyz':
                if col in orig_map:
                    orig = orig_map[col]
                    d = vec(i-orig[0], j-orig[1])
                    path = vec(0, 0)
                    if dimension == 0:
                        period0 = d
                        path = vec(1, 0)
                        dimension = 1
                    elif dimension == 1:
                        if (period0==d).all():
                            path = vec(1, 0)
                        else:
                            period1 = d
                            dimension = 2
                            path = vec(0, 1)
                    elif dimension == 2:
                        if (period0 == d).all():
                            path = vec(0, 1)
                        elif (period1 == d).all():
                            path = vec(1, 0)
                        elif (period0+period1 == d).all():
                            path = vec(1, 1)
                        else:
                            raise "Unknown period"
                    atoms[(i, j)] = (path, atoms[orig_map[col]][1])
                else:
                    orig_map[col] = (i, j)
                    atoms[(i, j)] = (vec(0, 0), num_atoms)
                    num_atoms += 1
            elif col == 'o':
                atoms[(i, j)] = (vec(0, 0), num_atoms)
                num_atoms += 1
            elif col in bond_types:
                (hop, src, dst) = bond_types[col]
                bonds.append((hop, (i+src[0], j+src[1]), (i+dst[0], j+dst[1])))
            j += 1
        i += 1

    return (num_atoms, dimension, bonds, atoms)

def compute_hamiltonian(num_atoms, atoms, bonds, flux_per_plaquette = 0):
    """
    Compute Hamiltonian for given graph.
    If it's periodic it computes the Hamiltonian as a polynomial
    in the reciprocal lattice vector.
    """
    zero = numpy.zeros((num_atoms, num_atoms),
            dtype = numpy.complex64)
    h_poly = {}

    for (w, (i0, j0), (i1, j1)) in bonds:
        (phase0, atom0) = atoms[(i0, j0)]
        (phase1, atom1) = atoms[(i1, j1)]

        exp0 = phase1[0]-phase0[0]
        exp1 = phase1[1]-phase0[1]

        if not (exp0, exp1) in h_poly:
            h_poly[( exp0,  exp1)] = numpy.copy(zero)
            h_poly[(-exp0, -exp1)] = numpy.copy(zero)

        # print "a-a ((",atom0, atom1,"))"
        # print (i0,j0),"->",(i1,j1)
        plaquettes = 0.5*(i1-i0)*(j0+j1)
        # print "plaquettes=",plaquettes
        mag_angle = flux_per_plaquette*plaquettes*units.electron_charge/units.hbar
        mag_phase = numpy.exp(1j*mag_angle)
        # print "area=",area
        # print "magangle=",mag_angle
        # print "magphase",w,mag_phase
        # print "exp0,exp1=",exp0,exp1

        h_poly[( exp0,  exp1)][atom0, atom1] += w*mag_phase
        h_poly[(-exp0, -exp1)][atom1, atom0] += w/mag_phase
    # print h_poly
    return h_poly

def eval_hamiltonian(num_atoms, h_poly, (phase0, phase1)):
    """
    Evaluate the Hamiltonian given as a polynomial for a
    particular choice of reciprocal lattice vector.
    """
    # print "phase=",(phase0, phase1)
    h = numpy.zeros((num_atoms, num_atoms),
                    dtype = numpy.complex64)

    for (exp0, exp1) in h_poly:
        # print phase0, phase1, exp0, exp1
        h += h_poly[(exp0, exp1)] * phase0**exp0 * phase1**exp1

    return h

def eigensystem(mat):
    """
    Compute eigenvalues and eigenvectors of matrix with
    results sorted in increasing order of eignevalue.
    """
    e, v = numpy.linalg.eig(mat)
    e = numpy.abs(e)

    items = zip(e, v.T)
    items = sorted(items, key = operator.itemgetter(0))
    e, v = zip(*items)

    return (e, v)

def display_band_structure_1d(num_atoms, h_poly):
    """
    Display band structure on the 1d Brillouin zone.
    """
    x = []
    y = [[] for i in range(num_atoms)]
    n = 400
    for k in range(-n/2, n/2):
        alpha = 2*math.pi*k/n
        phase = numpy.exp(alpha*1j)
        #h_minus, h_zero, h_plus = compute_hamiltonian(num_atoms, atoms, bonds)
        #h = h_minus*phase.conjugate()+h_zero+h_plus*phase
        h = eval_hamiltonian(num_atoms, h_poly, (phase, 1))

        e, v = eigensystem(h)

        x.append(alpha)
        for i in range(num_atoms):
            y[i].append(e[i])

    for i in range(num_atoms):
        matplotlib.pyplot.plot(x, y[i])
    matplotlib.pyplot.show()

def display_energy_levels_0d(diagram, num_atoms, atoms, h_poly):
    """
    Display energy levels for 0d nano-structure.
    Also show eigenstates.
    """
    h = eval_hamiltonian(num_atoms, h_poly, (1, 1))

    e, v = eigensystem(h)

    left = 0
    bottom = 0
    right = max([len(row) for row in diagram.split('\n')])
    top = len(diagram.split('\n'))

    plot_rows = numpy.ceil(math.sqrt(num_atoms+1))
    plot_cols = plot_rows

    for i in range(num_atoms):
        matplotlib.pyplot.subplot(plot_rows, plot_cols, i+1, axisbg="#000000")
        y = [atom[0] for atom in atoms]
        x = [atom[1] for atom in atoms]
        c = numpy.abs(v[i]*v[i])

        matplotlib.pyplot.title('E = %f' % numpy.real(e[i]), fontsize = 10)
        norm = matplotlib.colors.Normalize(vmin = min(c),
                                           vmax = max(0.0001, max(c)))
        #x = [0,0,1,1]
        #y = [0,1,0,1]
        #c = [1,2,3,4]
        matplotlib.pyplot.hexbin(x, y, C = c,
                                 gridsize = (right-left, top-bottom),
                                 extent = (left, right, bottom, top),
                                 cmap = matplotlib.pyplot.get_cmap("gray"),
                                 norm = norm
                                 )

    matplotlib.pyplot.subplot(plot_rows, plot_cols, num_atoms+1)
    matplotlib.pyplot.scatter(num_atoms*[0], e, s = 0.1)

    matplotlib.pyplot.tight_layout()
    matplotlib.pyplot.show()

def main():
  #diagram = BEARDED_ZIGZAG2
  #diagram = ZIGZAG2
  #diagram = BEARDED_BEARDED5
  diagram = MANY
  b = 0#0.033*math.pi/2/4

  num_atoms, dimension, bonds, atoms = parse_diagram(diagram)

  print "dimension=", dimension

  if dimension==2:
      if 0:
          n = 100
          x = numpy.zeros((n, n), dtype = numpy.float64)
          y = numpy.zeros((num_atoms, n, n), dtype = numpy.float64)
          for k0 in range(-n/2, n/2):
              for k1 in range(-n/2, n/2):
                  alpha0 = 2*math.pi*k0/n
                  alpha1 = 2*math.pi*k1/n
                  phase0 = numpy.exp(alpha0*1j)
                  phase1 = numpy.exp(alpha1*1j)
                  h_minus, h_zero, h_plus = compute_hamiltonian(num_atoms, atoms, bonds)
                  h = h_minus*phase.conjugate()+h_zero+h_plus*phase

                  e, v = eigensystem(h)

                  x.append(alpha)
                  for i in range(num_atoms):
                      y[i].append(e[i])

          for i in range(num_atoms):
              matplotlib.pyplot.plot(x, y[i], lod = True)
          matplotlib.pyplot.show()

  elif dimension == 1:
    h_poly = compute_hamiltonian(num_atoms, atoms, bonds, b)
    h = eval_hamiltonian(num_atoms, h_poly, (1, 1))
    # print h
    #sys.exit(1)
    display_band_structure_1d(num_atoms, h_poly)

  elif dimension==0:
      h_poly = compute_hamiltonian(num_atoms, atoms, bonds)
      display_energy_levels_0d(diagram, num_atoms, atoms, h_poly)

if __name__ == "__main__":
    main()
