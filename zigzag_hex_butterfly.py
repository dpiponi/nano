from nano import *

ZIGZAG_HEX_RIBBON = r"""
  A-B     C-D     E-B     G-H     I-J     K-L     M-N     O-P     Q-R     S-T     U-V     W-X     Y-Z     a-b    
 /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \    
o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o
 \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /    
  A B     C D     E B     G H     I J     K L     M N     O P     Q R     S T     U V     W X     Y Z     a b    
"""

dx = units.nanometre
dy = units.nanometre

num_atoms, dimension, bonds, atoms = parse_diagram(ZIGZAG_HEX_RIBBON)

n = 1024
x = numpy.zeros((n, num_atoms*num_atoms), dtype = numpy.float32)
y = numpy.zeros((n, num_atoms*num_atoms), dtype = numpy.float32)
for l in range(0, n):
    print l
    B = 0.25*0.5*math.pi*units.hbar/units.electron_charge*float(l)/n # hex
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

for m in range(0, num_atoms*num_atoms):
    matplotlib.pyplot.plot(range(n), y[:, m], 'k', linewidth = 0.05)
    matplotlib.pyplot.axes(frameon=False)
    frame = matplotlib.pyplot.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)

#matplotlib.pyplot.show()
matplotlib.pyplot.savefig("zigzag_hex.1000.jpg", dpi = 1000)
