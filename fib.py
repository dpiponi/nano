import sys
import numpy
import math
import matplotlib.pyplot

def inc(n):
    if n==():
        return (1,)
    if n==(1,):
        return (0, 1)
    if n[0]==0:
        return normalise([1]+n[1:])
    if n[0]==1:
        return (0,)+inc(n[1:])

def normalise(n):
    if n[0]==0:
        return (0,)+normalise(n[1:])
    if n==(1,):
        return (1,)
    if n[0]==1 and n[1]==1:
        return (0, 0)+inc(n[2:])
    return (1, 0)+normalise(n[2:])

def decr(n):
    if n==():
        raise "No predecessor to 0"
    if n==(1):
        return ()
    if n==(0, 1):
        return (1,)
    if n[0]==1:
        return (0,)+n[1:]
    if n[0]==0 and n[1]==1:
        return (1, 0)+n[2:]
    i = 0
    while n[0]==0:
        i += 1
        n = n[1:]
    n = n[1:]
    i = i+1
    if n==():
        if i%2==0:
            return (i/2-1)*(1, 0)+(1,)
        else:
            return (0,)+((i-1)/2-1)*(1,0)+(1,)
    else:
        if i%2==0:
            return (i/2)*(1, 0)+n
        else:
            return (0,)+((i-1)/2)*(1, 0)+n

def val(n, a = 1, b = 1):
    if n==():
        return 0
    else:
        return n[0]*b+val(n[1:], b, a+b)

n = ()

#print decr([0, 0, 0, 1, 0, 1])
#sys.exit()

m = 1000

def chew(f, bite):
    n = 0
    if len(f)==0:
        return (f, 0)
    l = len(bite)
    while len(f)>=l and f[0:l] == bite:
        n += 1
        f = f[l:]
    return (f, n)

if 0:
    for i in xrange(m):
        print i, n, val(n)
        n = inc(n)

    for i in xrange(m, -1, -1):
        print i, n, val(n)
        n = decr(n)

# r = which region
# w = Fibonacci number

def mod7(n):
    if n==0:
        return 7
    if n==8:
        return 1
    return n

def type1(i):
    #print "type1"
    return ((i, (1,)), 7)

def type2(r, w, n, i):
    #print "type2"
    if i==1:
        return ((mod7(r-1), (1,)) if n==0 else (r, (0, 0)+(n-1)*(1, 0)+(1,)), 6)
    if i==2:
        return ((r, (0, 1)) if n==0 else (r, (0, 1, 0, 0)+(n-1)*(1, 0)+(1,)), 7)
    if i==3:
        return ((r, (0, 0)+w), 7)
    if i==4:
        return ((r, (1, 0)+w), 7)
    if i==5:
        return ((mod7(r+1), n*(0, 0)+(0, 1)), 1)
    if i==6:
        return ((mod7(r+1), (1,)), 1) if n==0 else ((mod7(r+1), (n-1)*(0, 0)+(0, 1)), 2)
    if i==7:
        return ((0, []), r) if n==0 else ((r, (n-1)*(1, 0)+(1,)), 4)

def type3(r, w, n, i):
    #print "type3"
    if i==1:
        return ((mod7(r-1), n*(1, 0)+(1,)), 5)
    if i==2:
        return ((mod7(r-1), (n+1)*(1, 0)+(1,)), 6)
    if i==3:
        return ((r, (0, 0)+w), 7)
    if i==4:
        return ((r, (1, 0)+w), 7)
    if i==5:
        return ((r, (0, 1)+w), 1)
    if i==6:
        return ((r, (0, 0, 1) if n==0 else (1, 0)+(n-1)*(0, 0)+(0, 1)), 1)
    if i==7:
        return ((r, (1,)), 2) if n==0 else ((r, (n-1)*(0, 0)+(0, 1)), 3)

def type4(r, w, n, u, i):
    #print "type4"
    if i==1:
        if n > 1:
            return ((r, (0, 0)+(n-1)*(1, 0)+u), 6)
        else:
            return ((r, (0, 0)+u), 6)
    if i==2:
        return ((r, (0, 1, 0, 0)+(n-1)*(1, 0)+u), 7)
    if i==3:
        return ((r, (0, 0)+w), 7)
    if i==4:
        return ((r, (1, 0)+w), 7)
    if i==5:
        return ((r, n*(0, 0)+(0, 1)+u), 1)
    if i==6:
        return ((r, (n-1)*(0, 0)+(0, 1)+u), 2)
    if i==7:
        if n > 1:
            return ((r, (n-1)*(1, 0)+u), 4)
        else:
            return ((r, u), 4)

def type5(r, w, n, u, i):
    #print "type5"
    if i==1:
       return ((r, (n*(0, 1)+[0]+u) if u != () else n*(0, 1)), 6)
    if i==2:
        return ((r, (n+1)*(0, 1) if u == () else (n+1)*(0, 1)+(0,)+u), 7)
    if i==3:
        return ((r, (0, 0)+w), 7)
    if i==4:
        return ((r, (1, 0)+w), 7)
    if i==5:
        return ((r, (0, 1)+w), 1)
    if i==6:
        return ((r, (1, 0)+(n-1)*(0, 0)+(1,)+u), 1)
    if i==7:
        return ((r, (n-1)*(0, 0)+(1,)+u), 3)

def type6(r, w, n, u, i):
    #print "type6"
    if i==1:
        if n>1:
            return ((r, (n-1)*(0, 1)+u), 5)
        else:
            #(v, q) = chew(u, [0])
            return ((r, u), 5)
    if i==2:
        return ((r, (1, 0)+(n-1)*(0, 1)+u), 6)
    if i==3:
        return ((r, (0, 0)+w), 7)
    if i==4:
        return ((r, (1, 0)+w), 7)
    if i==5:
        return ((r, (0, 1)+w), 1)
    if i==6:
        if u==():
            return ((r, n*(0, 0)+(1,)), 1)
        else:
            return ((r, n*(0, 0)+(1, 0)+u[2:]), 1)
    if i==7:
        if u==():
            assert n>1
            return ((r, (n-1)*(0, 0)+(1,)), 2)
        else:
            return ((r, (n-1)*(0, 0)+(1, 0)+u[2:]), 2)

def type7(r, w, n, u, i):
    #print "type7"
    if i==1:
        return ((r, n*(1, 0)+u), 5)
    if i==2:
        return ((r, (n+1)*(1, 0)+u), 6)
    if i==3:
        return ((r, (0, 0)+w), 7)
    if i==4:
        return ((r, (1, 0)+w), 7)
    if i==5:
        return ((r, (0, 1)+w), 1)
    if i==6:
        return ((r, (1, 0)+(n-1)*(0, 0)+(0, 1)+u), 1)
    if i==7:
        return ((r, (n-1)*(0, 0)+(0, 1)+u), 3)

def son_side((r, w), i):
    if (r, w) == (0, []):
        return type1(i)

    (u, n) = chew(w, (1, 0))
    if u == (1,):
        return type2(r, w, n, i)
    (u, n) = chew(w, (0, 0))
    if u == (0, 1):
        return type3(r, w, n, i)
    (u, n) = chew(w, (1, 0))
    if n>0 and u != () and u != (1,):
        return type4(r, w, n, u, i)
    (u, n) = chew(w, (0, 0))
    if n>0 and u[0] == 1:
        return type5(r, w, n, u[1:], i)
    (u, n) = chew(w, (0, 0))
    if n>0 and len(u)>=3 and u[0]==0 and u[1]==1:
        return type7(r, w, n, u[2:], i)
    (u, n) = chew(w, (0, 1))
    if u != () or n > 1:
        return type6(r, w, n, u, i)
    print w
    raise "UNIMPLEMENTED"

def test_path(s):
    print "-----"
    print "Testing", s
    p = (0, [])
    t = []
    v = []
    print p
    print "Out"
    print "Starting at", p
    for step in s:
        v = [p]+v
        op = p
        (p, i) = son_side(p, step)
        print "Out from", op, "along", step, "to", p, "back is", i
        t = [i]+t
    print "Back"
    for step in t:
        op = p
        (p, i) = son_side(p, step)
        print "Return from", op, "along", step, "to", p, "expecting", v[0]
        assert p == v[0]
        v = v[1:]
    print "Finished at", p
    assert p == (0, ())

if 0:
    for i in xrange(1, 8):
        test_path([i])

    for i in xrange(1, 8):
        for j in xrange(1, 8):
            test_path([i, j])

    for i in xrange(1, 8):
        for j in xrange(1, 8):
            for k in range(1, 8):
                test_path([i, j, k])

    for i in xrange(1, 8):
        for j in xrange(1, 8):
            for k in range(1, 8):
                for l in range(1, 8):
                    test_path([i, j, k, l])

    for i in xrange(1, 8):
        for j in xrange(1, 8):
            for k in range(1, 8):
                for l in range(1, 8):
                    for m in range(1, 8):
                        test_path([i, j, k, l, m])

    for i in xrange(1, 8):
        for j in xrange(1, 8):
            for k in range(1, 8):
                for l in range(1, 8):
                    for m in range(1, 8):
                        for n in range(1, 8):
                            test_path([i, j, k, l, m, n])

r7 = numpy.exp(2*math.pi*1j/7)
ir7 = r7.conjugate()
r14 = numpy.exp(2*math.pi*1j/14)
ir14 = r14.conjugate()
s = 0.33603173855089774

def to_uhp(z):
    return -1j*(z+1)/(z-1)

def to_disc(z):
    return (z-1j)/(z+1j)

def down(z):
    return ir14*to_disc(to_uhp(z)/s)

def rot(z):
    return r7*z

def irot(z):
    return ir7*z

def recurseWhite(n, z, p):
    if n==0:
        return []
    else:
        s2 = recurseBlack(n-1, z, son_side(p, 2)[0])
        s3 = recurseWhite(n-1, z, son_side(p, 3)[0])
        s4 = recurseWhite(n-1, z, son_side(p, 4)[0])
        return [(z,p)]+[(irot(down(z)), p) for (z, p) in s2]+[(down(z), p) for (z, p) in s3]+[(rot(down(z)), p) for (z, p) in s4]

def recurseBlack(n, z, p):
    if n==0:
        return []
    else:
        s3 = recurseBlack(n-1, z, son_side(p, 3)[0])
        s4 = recurseWhite(n-1, z, son_side(p, 4)[0])
        return [(z,p)]+[(down(z), p) for (z, p) in s3]+[(rot(down(z)), p) for (z, p) in s4]

if 0:
    for i in xrange(1, 8):
        points = recurseWhite(4, 0.0, (i, [1]))
        r = numpy.exp(2*math.pi*1j*(i+3.5)/7)
        w_points = [(0, (0, []))]+[(r*down(z), p) for (z, p) in points]
        matplotlib.pyplot.scatter(
            [w.real for (w, p) in w_points],
            [w.imag for (w, p) in w_points],
            marker = ','
            )
        for (w, p) in w_points:
            matplotlib.pyplot.annotate(str(p), (w.real, w.imag), size = 'xx-small')

#matplotlib.pyplot.show()

def step((i, f), t, side):
    ((i_new, f_new), bacl) = son_side((i, f), side)
    def t_new(z):
        return t(numpy.exp((side-3)*2*math.pi*1j/7)*down(z))
    return ((i_new, f_new), t_new)

def idn(z):
    return z

(p1, t1) = ((1, (1,)), idn)
(p2, t2) = step(p1, t1, 3)
(p3, t3) = step(p2, t2, 3)
(p4, t4) = step(p3, t3, 3)

print t3(down(0))

if 0:
    def recurse_w(n, (p, t)):
        if n==0:
            print t(0)
            return []
        else:
            return [(p, t)]+recurse_b(n-1, step(p, t, 2))+recurse_w(n-1, step(p, t, 3))+recurse_w(n-1, step(p, t, 4))

    def recurse_b(n, (p, t)):
        if n==0:
            print t(0)
            return []
        else:
            return [(p, t)]+recurse_b(n-1, step(p, t, 3))+recurse_w(n-1, step(p, t, 4))

#zs = recurse_w(4, ((1, [1]), idn))

if 0:
    matplotlib.pyplot.scatter(
        [t(0).real for (p, t) in zs],
        [t(0).imag for (p, t) in zs],
        marker = ',')

    for (p, t) in zs:
        matplotlib.pyplot.annotate(str(p), (t(0).real, t(0).imag), size = 'xx-small')

    matplotlib.lines.Line2D([0,0],[1,1])
    matplotlib.pyplot.show()

def psz(z):
    print z.real, ' ', z.imag

def line(p, q):
    print 200+200*p.real, 200+200*p.imag, "moveto", 200+200*q.real, 200+200*q.imag, "lineto stroke"

vertices = []
vertex_map = {}
edges = []
edge_map = {}
faces = []
face_map = {}

def add_vertex((p, z)):
    if not p in vertex_map:
        vertex_map[p] = len(vertices)
        vertices.append((p, z))

def add_edge(((p, w), (q, z))):
    add_vertex((p, w))
    add_vertex((q, z))
    if not (vertex_map[p], vertex_map[q]) in edge_map:
        edge_map[(vertex_map[p], vertex_map[q])] = len(edges)
        edges.append((vertex_map[p], vertex_map[q]))

def add_face((p, x), (q, y), (r, z)):
    add_vertex((p, x))
    add_vertex((q, y))
    add_vertex((r, z))
    if not (p, q, r) in edge_map:
        face_map[(vertex_map[p], vertex_map[q], vertex_map[r])] = len(faces)
        faces.append((vertex_map[p], vertex_map[q], vertex_map[r]))
    y = y(0)
    z = z(0)
    r = 0.333333*(x+y+z)
    print 200+200*r.real, 200+200*r.imag, "moveto"
    print "0.5 0.5 0.5 setgray 0.5 setlinewidth"
    print "-1 -1 rmoveto 2 0 rlineto 0 2 rlineto -2 0 rlineto 0 -2 rlineto stroke"

def recurse_w(n, (p, t)):
    add_vertex((p, t(0)))
    if n==0:
        w = step(p, t, 6)
        print "0.5 0.5 0.5 setgray 1.5 setlinewidth"
        line(t(0), w[1](0))
        add_edge(((p, t(0)), w))
        return
    else:
        u = step(p, t, 2)
        print "0 0 0 setgray 0.5 setlinewidth"
        line(t(0), u[1](0))
        recurse_b(n-1, u)
        add_edge(((p, t(0)), u))
        v = step(p, t, 3)
        print "0 0 0 setgray 0.5 setlinewidth"
        line(t(0), v[1](0))
        recurse_w(n-1, v)
        add_edge(((p, t(0)), v))
        add_face((p, t(0)), u, v)
        w = step(p, t, 4)
        print "0 0 0 setgray 0.5 setlinewidth"
        line(t(0), w[1](0))
        recurse_w(n-1, w)
        add_edge(((p, t(0)), w))
        add_face((p, t(0)), v, w)
        x = step(p, t, 5)
        print "0 0 0 setgray 1.5 setlinewidth"
        line(t(0), x[1](0))
        add_edge(((p, t(0)), x))
        add_face((p, t(0)), w, x)
        y = step(p, t, 6)
        print "0.5 0.5 0.5 setgray 1.5 setlinewidth"
        print "% Adding gray edge"
        line(t(0), y[1](0))
        add_edge(((p, t(0)), y))
        add_face((p, t(0)), x, y)

def recurse_b(n, (p, t)):
    add_vertex((p, t(0)))
    if n==0:
        w = step(p, t, 6)
        print "0.5 0.5 0.5 setgray 1.5 setlinewidth"
        line(t(0), w[1](0))
        add_edge(((p, t(0)), w))
        return
    else:
        u = step(p, t, 3)
        print "0 0 0 setgray 0.5 setlinewidth"
        line(t(0), u[1](0))
        recurse_b(n-1, u)
        add_edge(((p, t(0)), u))
        v = step(p, t, 4)
        print "0 0 0 setgray 0.5 setlinewidth"
        line(t(0), v[1](0))
        recurse_w(n-1, v)
        add_edge(((p, t(0)), v))
        add_face((p, t(0)), u, v)
        w = step(p, t, 5)
        print "0 0 0 setgray 1.5 setlinewidth"
        line(t(0), w[1](0))
        add_edge(((p, t(0)), w))
        add_face((p, t(0)), v, w)
        x = step(p, t, 6)
        print "0.5 0.5 0.5 setgray 1.5 setlinewidth"
        print "% Adding gray edge"
        line(t(0), x[1](0))
        add_edge(((p, t(0)), x))
        add_face((p, t(0)), w, x)

vertex_map[(0, ())] = len(vertices)
vertices.append(((0, ()), 0))

def circ(i):
    return lambda z:numpy.exp(2*math.pi*1j*(i+3.5)/7)*down(z)

for i in xrange(1, 8):
    q = numpy.exp(2*math.pi*1j*(i+3.5)/7)*down(0)
    print "0 0 0 setgray 0.5 setlinewidth"
    line(0, q)
    recurse_w(2, ((i, (1,)), lambda z:numpy.exp(2*math.pi*1j*(i+3.5)/7)*down(z)))
    add_edge((((0, ()), 0.0), ((i, (1,)), q)))
    add_face(((0, ()), 0.0), ((i, (1,)), circ(i)), ((mod7(i+1), (1,)), circ(i+1)))
    #r = numpy.exp(2*math.pi*1j*(i+3.5)/7)
    #w_points = [(0, (0, []))]+[(r*down(z), p) for (z, p) in points]

print "showpage"
print '%',len(vertices)
print '%',len(vertex_map)
print '%',len(edges)
print '%',len(edge_map)
print '%',len(faces)
print '%',len(face_map)

v = len(vertices)
e = len(edges)
f = len(faces)

euler = v-e+f

print '% euler =', euler
