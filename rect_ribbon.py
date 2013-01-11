from nano import *

RECT_RIBBON = r"""
A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z-a-b-c-d-e-f
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f
"""

dx = 0.142*units.nanometre
dy = 0.142*units.nanometre

B = 400*units.tesla
flux_per_plaquette = dx*dy*B
print "B=",B
print "flux_per_plaquette=",flux_per_plaquette
print "mag_anlge/plaq=", flux_per_plaquette*units.electron_charge/units.hbar
import time
time.sleep(1)

num_atoms, dimension, bonds, atoms = parse_diagram(RECT_RIBBON)

h_poly = compute_hamiltonian(num_atoms, atoms, bonds, flux_per_plaquette)
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
        for k in range(-8,8):
          matplotlib.pyplot.subplot(17,1,k+8+2)
          matplotlib.pyplot.plot(numpy.abs(v[k]*v[k]))
          pass

    x.append(alpha)
    for i in range(num_atoms):
        y[i].append(e[i])

matplotlib.pyplot.subplot(17,1,1)
for i in range(num_atoms):
    matplotlib.pyplot.plot(x, y[i])
matplotlib.pyplot.show()
