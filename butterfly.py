from nano import *

RECT_RIBBON = r"""
A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z-a-b-c-d-e-f-g-h-i-j-k-l-m-n
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n
"""

dx = units.nanometre
dy = units.nanometre

num_atoms, dimension, bonds, atoms = parse_diagram(RECT_RIBBON)

n = 256
y = numpy.zeros((n, num_atoms*num_atoms), dtype = numpy.float32)
for l in range(0, n):
    print l
    B = 0.5*math.pi*units.hbar/units.electron_charge*float(l)/n
    h_poly = compute_hamiltonian(num_atoms, atoms, bonds, B)
    p = 0
    for k in range(0, num_atoms):
        alpha = 2*math.pi*k/num_atoms
        phase = numpy.exp(alpha*1j)
        h = eval_hamiltonian(num_atoms, h_poly, (phase, 1))

        e, v = eigensystem(h)

        y[l, p:p+num_atoms] = e

        p += num_atoms

    y[l].sort()

for m in range(0, num_atoms*num_atoms):
    matplotlib.pyplot.plot(range(n), y[:, m], 'k')

matplotlib.pyplot.show()
