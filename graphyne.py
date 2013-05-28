from nano import *
import sys

# begin = int(sys.argv[1])
# end = int(sys.argv[2])

# (6,6,12)-graphyne from
# http://iopscience.iop.org/1367-2630/14/11/113007/pdf/1367-2630_14_11_113007.pdf
# The ASCII art representation is sort of a hybrid of the two representations in that paper.
# Topologically it's the reduced version fig 4(c) p.7 in that paper.
# But I've arranged the dimensions of the ASCII art representation to match
# the unreduced version because computing the flux through a 'plaquette' requires
# correct geometry, not just topology.
# (Resize your window to see the full code.)

GRAPHYNE_RIBBON = r"""
A           B   C           D   E           F   G           H   I           J   K           L   M           N   O           P   Q           R   S           T   U           V   W           X   Y           Z   a           b                                  
             ` '             ` '             ` '             ` '             ` '             ` '             ` '             ` '             ` '             ` '             ` '             ` '             ` '             
              o               o               o               o               o               o               o               o               o               o               o               o               o              
   \     /         \     /         \     /         \     /         \     /         \     /         \     /         \     /         \     /         \     /         \     /         \     /         \     /         \     /   
                                                                                                                                                                                                                             
                                                                                                                                                                                                                             
      o               o               o               o               o               o               o               o               o               o               o               o               o               o      
      |       #       |       #       |       #       |       #       |       #       |       #       |       #       |       #       |       #       |       #       |       #       |       #       |       #       |      
      o               o               o               o               o               o               o               o               o               o               o               o               o               o                                                                                                                  
                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                         
   /     \         /     \         /     \         /     \         /     \         /     \         /     \         /     \         /     \         /     \         /     \         /     \         /     \         /     \                                                                                                               
              o               o               o               o               o               o               o               o               o               o               o               o               o              
             ' `             ' `             ' `             ' `             ' `             ' `             ' `             ' `             ' `             ' `             ' `             ' `             ' `             
o           o   o           o   o           o   o           o   o           o   o           o   o           o   o           o   o           o   o           o   o           o   o           o   o           o   o           o                             
|           |   |           |   |           |   |           |   |           |   |           |   |           |   |           |   |           |   |           |   |           |   |           |   |           |   |           |         
A           B   C           D   E           F   G           H   I           J   K           L   M           N   O           P   Q           R   S           T   U           V   W           X   Y           Z   a           b                                  
"""

# Numbers from table 1 p.9
t1 = -1.87
t2 = 1.36
t3 = 1.93

i = 1

bond_types = {
    '\'': (t1, vec(1, -1), vec(-1, 1)),
    '`':  (t1, vec(-1, -1), vec(1, 1)),
    '|' : (t1, vec(-1, 0), vec(1, 0)),

    '/':  (t2, vec(3, -3), vec(-3, 3)),
    '\\': (t2, vec(-3, -3), vec(3, 3)),

    '#':  (t3, vec(-5, 0), vec(5, 0))
}

# Not correct but it only affects the overall scalling of the plot
dx = units.nanometre
dy = units.nanometre

num_atoms, dimension, bonds, atoms = parse_diagram(GRAPHYNE_RIBBON, bond_types = bond_types)

name = '0011'

n = 1024 # 1024
if True:
    x = numpy.zeros((n, num_atoms*num_atoms), dtype = numpy.float32)
    y = numpy.zeros((n, num_atoms*num_atoms), dtype = numpy.float32)
    for l in range(0, n):
        print l
        B = 0.25*0.5*math.pi*units.hbar/units.electron_charge*float(l)/n # rect
        h_poly = compute_hamiltonian(num_atoms, atoms, bonds, B)
        p = 0
        for k in range(0, num_atoms):
            alpha = 2*math.pi*k/num_atoms
            phase = numpy.exp(alpha*1j)
            h = eval_hamiltonian(num_atoms, h_poly, (phase, 1))

            e, v = eigensystem(h)

            x[l, p:p+num_atoms] = l
            y[l, p:p+num_atoms] = e

            p += num_atoms

        y[l].sort()

    numpy.save('/Users/dan/Results/Graphyne/graphyne.'+name+'.%04d.npy' % i, y)
else:
    y = numpy.load('/Users/dan/Results/Graphyne/graphyne.'+name+'.%04d.npy' % i)

matplotlib.pyplot.figure(num=None, figsize=(40, 30), dpi=1000, facecolor='w', edgecolor='k')
for m in range(0, num_atoms*num_atoms):
    matplotlib.pyplot.plot(range(n), y[:, m], 'k', linewidth = 0.05)
    matplotlib.pyplot.axes(frameon=False)

frame = matplotlib.pyplot.gca()
frame.axes.get_xaxis().set_visible(False)
frame.axes.get_yaxis().set_visible(False)

matplotlib.pyplot.savefig('/Users/dan/Results/Graphyne/graphyne.'+name+'.%04d.jpg' % i)
