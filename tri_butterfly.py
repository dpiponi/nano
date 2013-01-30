from nano import *

TRI_RIBBON = r"""
  A - B - C - D - E - F - G - H - I - J - K - L - M - N - O - P - Q - R - S    
 / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \    
o - o - o - o - o - o - o - o - o - o - o - o - o - o - o - o - o - o - o - o    
 \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ /     
  A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S    
"""

dx = units.nanometre
dy = units.nanometre

bond_types = {
    '/' : (1.0, vec(1, -1), vec(-1, 1)),
    '\\': (1.0, vec(-1, -1), vec(1, 1)),
    '-' : (1.0, vec(0, -2), vec(0, 2))
}

num_atoms, dimension, bonds, atoms = parse_diagram(TRI_RIBBON,
                                                   bond_types = bond_types)

n = 1024
if 1:
    x = numpy.zeros((n, num_atoms*num_atoms), dtype = numpy.float32)
    y = numpy.zeros((n, num_atoms*num_atoms), dtype = numpy.float32)
    for l in range(0, n):
        print l
        B = 0.25*math.pi*units.hbar/units.electron_charge*float(l)/n # hex
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

    numpy.save('tri.%d.npy' % (n), y)
else:
    y = numpy.load('tri.%d.npy' % (n))

matplotlib.pyplot.figure(num=None, figsize=(16, 12), dpi=1000, facecolor='w', edgecolor='k')
for m in range(0, num_atoms*num_atoms):
    matplotlib.pyplot.plot(range(n), y[:, m], 'k', linewidth = 0.5)
    matplotlib.pyplot.axes(frameon=False)

frame = matplotlib.pyplot.gca()
frame.axes.get_xaxis().set_visible(False)
frame.axes.get_yaxis().set_visible(False)

matplotlib.pyplot.savefig("tri.1000.jpg")
