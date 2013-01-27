import sys
import numpy
import math
import matplotlib.pyplot

def inc(n):
    if n==[]:
        return [1]
    if n==[1]:
        return [0, 1]
    if n[0]==0:
        return normalise([1]+n[1:])
    if n[0]==1:
        return [0]+inc(n[1:])

def normalise(n):
    if n[0]==0:
        return [0]+normalise(n[1:])
    if n==[1]:
        return [1]
    if n[0]==1 and n[1]==1:
        return [0, 0]+inc(n[2:])
    return [1, 0]+normalise(n[2:])

def decr(n):
    if n==[]:
        raise "No predecessor to 0"
    if n==[1]:
        return []
    if n==[0, 1]:
        return [1]
    if n[0]==1:
        return [0]+n[1:]
    if n[0]==0 and n[1]==1:
        return [1, 0]+n[2:]
    i = 0
    while n[0]==0:
        i += 1
        n = n[1:]
    n = n[1:]
    i = i+1
    if n==[]:
        if i%2==0:
            return (i/2-1)*[1, 0]+[1]
        else:
            return [0]+((i-1)/2-1)*[1, 0]+[1]
    else:
        if i%2==0:
            return (i/2)*[1, 0]+n
        else:
            return [0]+((i-1)/2)*[1, 0]+n

def val(n, a = 1, b = 1):
    if n==[]:
        return 0
    else:
        return n[0]*b+val(n[1:], b, a+b)

n = []

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
    return ((i, [1]), 7)

def type2(r, w, n, i):
    #print "type2"
    if i==1:
        return ((mod7(r-1), [1]) if n==0 else (r, [0, 0]+(n-1)*[1, 0]+[1]), 6)
    if i==2:
        return ((r, [0, 1]) if n==0 else (r, [0, 1, 0, 0]+(n-1)*[1, 0]+[1]), 7)
    if i==3:
        return ((r, [0, 0]+w), 7)
    if i==4:
        return ((r, [1, 0]+w), 7)
    if i==5:
        return ((mod7(r+1), n*[0, 0]+[0, 1]), 1)
    if i==6:
        return ((mod7(r+1), [1]), 1) if n==0 else ((mod7(r+1), (n-1)*[0, 0]+[0, 1]), 2)
    if i==7:
        return ((0, []), r) if n==0 else ((r, (n-1)*[1, 0]+[1]), 4)

def type3(r, w, n, i):
    #print "type3"
    if i==1:
        return ((mod7(r-1), n*[1, 0]+[1]), 5)
    if i==2:
        return ((mod7(r-1), (n+1)*[1, 0]+[1]), 6)
    if i==3:
        return ((r, [0, 0]+w), 7)
    if i==4:
        return ((r, [1, 0]+w), 7)
    if i==5:
        return ((r, [0, 1]+w), 1)
    if i==6:
        return ((r, [0, 0, 1] if n==0 else [1, 0]+(n-1)*[0, 0]+[0, 1]), 1)
    if i==7:
        return ((r, [1]), 2) if n==0 else ((r, (n-1)*[0, 0]+[0, 1]), 3)

def type4(r, w, n, u, i):
    #print "type4"
    if i==1:
        if n > 1:
            return ((r, [0, 0]+(n-1)*[1, 0]+u), 6)
        else:
            return ((r, [0, 0]+u), 6)
    if i==2:
        return ((r, [0, 1, 0, 0]+(n-1)*[1, 0]+u), 7)
    if i==3:
        return ((r, [0, 0]+w), 7)
    if i==4:
        return ((r, [1, 0]+w), 7)
    if i==5:
        return ((r, n*[0, 0]+[0, 1]+u), 1)
    if i==6:
        return ((r, (n-1)*[0, 0]+[0, 1]+u), 2)
    if i==7:
        if n > 1:
            return ((r, (n-1)*[1, 0]+u), 4)
        else:
            return ((r, u), 4)

def type5(r, w, n, u, i):
    #print "type5"
    if i==1:
       return ((r, (n*[0, 1]+[0]+u) if u != [] else n*[0, 1]), 6)
    if i==2:
        return ((r, (n+1)*[0, 1] if u == [] else (n+1)*[0, 1]+[0]+u), 7)
    if i==3:
        return ((r, [0, 0]+w), 7)
    if i==4:
        return ((r, [1, 0]+w), 7)
    if i==5:
        return ((r, [0, 1]+w), 1)
    if i==6:
        return ((r, [1, 0]+(n-1)*[0, 0]+[1]+u), 1)
    if i==7:
        return ((r, (n-1)*[0, 0]+[1]+u), 3)

def type6(r, w, n, u, i):
    #print "type6"
    if i==1:
        if n>1:
            return ((r, (n-1)*[0, 1]+u), 5)
        else:
            #(v, q) = chew(u, [0])
            return ((r, u), 5)
    if i==2:
        return ((r, [1, 0]+(n-1)*[0, 1]+u), 6)
    if i==3:
        return ((r, [0, 0]+w), 7)
    if i==4:
        return ((r, [1, 0]+w), 7)
    if i==5:
        return ((r, [0, 1]+w), 1)
    if i==6:
        if u==[]:
            return ((r, n*[0, 0]+[1]), 1)
        else:
            return ((r, n*[0, 0]+[1, 0]+u[2:]), 1)
    if i==7:
        if u==[]:
            assert n>1
            return ((r, (n-1)*[0, 0]+[1]), 2)
        else:
            return ((r, (n-1)*[0, 0]+[1, 0]+u[2:]), 2)

def type7(r, w, n, u, i):
    #print "type7"
    if i==1:
        return ((r, n*[1, 0]+u), 5)
    if i==2:
        return ((r, (n+1)*[1, 0]+u), 6)
    if i==3:
        return ((r, [0, 0]+w), 7)
    if i==4:
        return ((r, [1, 0]+w), 7)
    if i==5:
        return ((r, [0, 1]+w), 1)
    if i==6:
        return ((r, [1, 0]+(n-1)*[0, 0]+[0, 1]+u), 1)
    if i==7:
        return ((r, (n-1)*[0, 0]+[0, 1]+u), 3)

def son_side((r, w), i):
    if (r, w) == (0, []):
        return type1(i)

    (u, n) = chew(w, [1, 0])
    if u == [1]:
        return type2(r, w, n, i)
    (u, n) = chew(w, [0, 0])
    if u == [0, 1]:
        return type3(r, w, n, i)
    (u, n) = chew(w, [1, 0])
    if n>0 and u != [] and u != [1]:
        return type4(r, w, n, u, i)
    (u, n) = chew(w, [0, 0])
    if n>0 and u[0] == 1:
        return type5(r, w, n, u[1:], i)
    (u, n) = chew(w, [0, 0])
    if n>0 and len(u)>=3 and u[0]==0 and u[1]==1:
        return type7(r, w, n, u[2:], i)
    (u, n) = chew(w, [0, 1])
    if u != [] or n > 1:
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
    assert p == (0, [])

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

p1 = (1, [1])
print p1
p2 = son_side(p1, 2)[0]
p3 = son_side(p1, 3)[0]
p4 = son_side(p1, 4)[0]
print p2, p3, p4
p5 = son_side(p2, 3)[0]
p6 = son_side(p2, 4)[0]
p7 = son_side(p3, 2)[0]
p8 = son_side(p3, 3)[0]
p9 = son_side(p3, 4)[0]
p10 = son_side(p4, 2)[0]
p11 = son_side(p4, 3)[0]
p12 = son_side(p4, 4)[0]
print p5, p6, p7, p8, p9, p10, p11, p12

matplotlib.pyplot.show()
