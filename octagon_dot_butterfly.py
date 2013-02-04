from nano import *

TRI_RIBBON = r"""
    A-B   C-D   E-F   G-H   I-J   K-L   M-N   O-P   Q-R   S-T   U-V   W-X   Y-Z 
   /   \ /   \ /   \ /   \ /   \ /   \ /   \ /   \ /   \ /   \ /   \ /   \ /   \
  o     o     o     o     o     o     o     o     o     o     o     o     o     o     
  |     |     |     |     |     |     |     |     |     |     |     |     |     |     
  o     o     o     o     o     o     o     o     o     o     o     o     o     o     
   \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   /
    A B   C D   E F   G H   I J   K L   M N   O P   Q R   S T   U V   W X   Y Z 
"""

dx = units.nanometre
dy = units.nanometre

for i in xrange(53, 65):
    print "Frame", i

    a = i/64.0
    t1 = a
    t0 = 1-a

    bond_types = {
        '/' : (t1, vec(1, -1), vec(-1, 1)),
        '\\': (t1, vec(-1, -1), vec(1, 1)),
        '-' : (t0, vec(0, -1), vec(0, 1)),
        '|' : (t0, vec(-1, 0), vec(1, 0))
    }
    num_atoms, dimension, bonds, atoms = parse_diagram(TRI_RIBBON,
                                                       bond_types = bond_types)

    n = 512
    if 1:
        x = numpy.zeros((n, num_atoms*num_atoms), dtype = numpy.float32)
        y = numpy.zeros((n, num_atoms*num_atoms), dtype = numpy.float32)
        for l in range(0, n):
            if l%10==0:
                print l
            B = 0.5*math.pi*units.hbar/units.electron_charge*float(l)/n # hex
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
            print y[0], y[-1]

        numpy.save('dot_octagon.2.%04d.npy' % i, y)
    else:
        y = numpy.load('dot_octagon.2.%04d.npy' % i)

    matplotlib.pyplot.figure(num=None, figsize=(6, 4), dpi=1000, facecolor='w', edgecolor='k')
    for m in range(0, num_atoms*num_atoms):
        matplotlib.pyplot.ylim([-3.0, 3.0])
        matplotlib.pyplot.plot(range(n), y[:, m], 'k', linewidth = 0.5)
        matplotlib.pyplot.axes(frameon=False)

    frame = matplotlib.pyplot.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)

    matplotlib.pyplot.savefig("dot_octagon.2.%04d.jpg" % i)
