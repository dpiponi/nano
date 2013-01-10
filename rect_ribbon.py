from nano import *

RECT_RIBBON = r"""
A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z-a-b-c-d-e-f
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f
"""

b = 0.033*math.pi/2/4

num_atoms, dimension, bonds, atoms = parse_diagram(RECT_RIBBON)

print "dimension=", dimension

h_poly = compute_hamiltonian(num_atoms, atoms, bonds, b)
h = eval_hamiltonian(num_atoms, h_poly, (1, 1))

x = []
y = [[] for i in range(num_atoms)]
n = 400
for k in range(-n/2, n/2):
    alpha = 2*math.pi*k/n
    phase = numpy.exp(alpha*1j)
    h = eval_hamiltonian(num_atoms, h_poly, (phase, 1))

    e, v = eigensystem(h)
    if k == 100:
        for k in range(-16,16):
          matplotlib.pyplot.subplot(33,1,k+16+2)
          matplotlib.pyplot.plot(numpy.abs(v[k]*v[k]))

    x.append(alpha)
    for i in range(num_atoms):
        y[i].append(e[i])

matplotlib.pyplot.subplot(33,1,1)
for i in range(num_atoms):
    matplotlib.pyplot.plot(x, y[i])
matplotlib.pyplot.show()
