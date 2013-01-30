"""
Compute energy levels and band structures for atomic nanostructures
drawn with ASCII art.
"""

# 3eV for graphene

import numpy
import numpy.linalg
import matplotlib.pyplot
import math
import sys
import operator
import units


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

def parse_diagram(diagram, dimension_hint = None, joins = '', bond_types = bond_types):
    """
    Convert diagram into lists of bonds and atoms.

    This function attempts to guess whether your diagram is aperiodic,
    periodic with one period or periodic with two periods.
    It does this using the geometry of the diagram, assuming it
    is planar. Sometimes you don't want planar geometry
    (eg. for spirals) and you simply want a single period.
    In that case, set `dimension_hint` equal to 1. It's a hint
    because it'll return an aperiodic structure if that's what
    your diagram looks like.
    """
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
                    if col in joins:
                        orig = orig_map[col]
                        path = vec(0, 0)
                    else:
                        orig = orig_map[col]
                        d = vec(i-orig[0], j-orig[1])
                        if dimension_hint == 1 or dimension == 0:
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

    # `eig` returns complex results but we know all of the
    # eigenstates have real energy.
    e = numpy.real(e)

    items = zip(e, v.T)
    items = sorted(items, key = operator.itemgetter(0))
    e, v = zip(*items)

    return (e, v)

def display_band_structure_1d(num_atoms, h_poly, cycles = 1, phase_offset = 0):
    """
    Display band structure on the 1d Brillouin zone.

    The following parameters affect only how the result is displayed:

    `cycles` is the number of times we wrap one brillouin zone around the
    horizontal axis. Simulates the effect of computing bands where the
    fundamental domain has been repeated `cycles` times.

    `phase_offset` shifts the graph in phase space.
    """
    x = []
    y = [[] for i in range(num_atoms)]
    n = 100*cycles
    for k in range(-n/2, n/2):
    # for k in range(0, n):
        alpha = 2*math.pi*k/n+phase_offset
        phase = numpy.exp(alpha*1j)
        #h_minus, h_zero, h_plus = compute_hamiltonian(num_atoms, atoms, bonds)
        #h = h_minus*phase.conjugate()+h_zero+h_plus*phase
        h = eval_hamiltonian(num_atoms, h_poly, (phase, 1))

        e, v = eigensystem(h)
        #print k,h,e

        x.append(alpha)
        for i in range(num_atoms):
            y[i].append(e[i])

    for i in range(num_atoms):
        # matplotlib.pyplot.plot(x, y[i])
        for cycle in range(0, cycles):
          matplotlib.pyplot.plot(x[0:100], y[i][100*cycle:100*(cycle+1)])
    # matplotlib.pyplot.show()

def simple_display_energy_levels_0d(num_atoms, h_poly):
    """
    Display energy levels for 0d nano-structure.
    Also show eigenstates.
    """
    h = eval_hamiltonian(num_atoms, h_poly, (1, 1))

    e, v = eigensystem(h)
    #print e

    matplotlib.pyplot.scatter(num_atoms*[0], e, s = 20, marker = '_')

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

