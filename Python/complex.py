def gcd (a,b):
    
    while b!=0:
        a, b = b, a%b
        
    return a
    

class Frac:
    
    def simplify (s):
        c = gcd(s.a, s.b)
        s.a = s.a // c
        s.b = s.b // c
    
    def __init__ (s, a=0, b=1):
        if type(a) == float:
            s.a, s.b = a.as_integer_ratio()
            c, d = float(b).as_integer_ratio()
            s.a *= d
            s.b *= c
        elif type(a) == Frac:
            s.a = a.a
            s.b = a.b
        elif type(a) == int:
            if b<0:
                s.a = -a
                s.b = -b
            else:
                s.a = a
                s.b = b
        else:
            s.a = 0
            s.b = 1
        
        s.simplify()
        
    def __neg__(s):
        return Frac(-s.a, s.b)
    def __pos__(s):
        return Frac(s)
    def __abs__(s):
        return Frac(abs(s.a), s.b)
    def __int__(s):
        return s.a // s.b
    def __float__(s):
        return s.a / s.b
    def __invert__(s):
        return Frac(s.b, s.a)
    
    def __add__ (s, o):
        if type(o) != Frac:
            return s + Frac(o)
        return Frac (s.a * o.b + o.a * s.b, s.b * o.b)
    def __radd__ (s, o):
        return s + o
    
    def __sub__ (s, o):
        if type(o) != Frac:
            return s - Frac(o)      
        return Frac (s.a * o.b - o.a * s.b, s.b * o.b)
    def __rsub__ (s, o):
        return - (s - o)
    
    def __mul__ (s,o):
        if type(o) != Frac:
            return s * Frac(o)
        return Frac (s.a * o.a, s.b * o.b)
    def __rmul__(s,o):
        return s * o
    
    def __truediv__ (s,o):
        if type(o) != Frac:
            return s / Frac(o)
        return Frac (s.a * o.b, s.b * o.a)
    def __rtruediv__ (s,o):
        return ~(s/o)
    
    def __mod__ (s,o):
        if type(o) != Frac:
            return s % Frac(o)
        return Frac ((s.a * o.b) % (o.a * s.b), s.b * o.b)
    def __rmod__(s, o):
        return Frac(o) % s
    
    def __floordiv__(s,o):
        if type(o) != Frac:
            return s // Frac(o)
        return Frac((s.a * o.b) // (o.a * s.b))
    def __rfloordiv__(s,o):
        return Frac(o) // s
    
    def __pow__ (s, o, m=-1):
        if m==-1:
            if type(o) != Frac:
                return pow(s, Frac(o))
            return Frac(pow (s.a, o.a/o.b), pow (s.b, o.a/o.b))
        else:
            if type(o) != Frac:
                return pow(s, Frac(o), m)
            return Frac(pow (s.a, o.a/o.b, m), pow (s.b, o.a/o.b, m))
    def __rpow__(s, o, m):
        return pow(Frac(o), s, m)
    
    def __str__ (s):
        if s.a == 0:
            return "0"
        elif s.b == 1:
            return str(s.a)
            
        return str(s.a) + "/" + str(s.b)
    
    def eval (s):
        return s.a / s.b
        
    def __lt__(s, o):
        if type(o) != Frac:
            return s < Frac(o)
        return s.a*o.b < o.a*s.b
    def __le__(s, o):
        if type(o) != Frac:
            return s <= Frac(o)
        return s.a*o.b <= o.a*s.b
    def __eq__(s, o):
        if type(o) != Frac:
            return s == Frac(o)
        return (s - o).a == 0 
    def __ne__(s, o):
        if type(o) != Frac:
            return s != Frac(o)
        return (s - o).a != 0 
    def __ge__(s, o):
        if type(o) != Frac:
            return s >= Frac(o)
        return s.a*o.b >= o.a*s.b
    def __gt__(s, o):
        if type(o) != Frac:
            return s > Frac(o)
        return s.a*o.b > o.a*s.b


class Complex:
    
    def __init__ (self, a,b=Frac(0)):
        if type(a)==Frac:
            self.re = a
        else:
            self.re = Frac(a)
        if type(b)==Frac:
            self.im = b
        else:
            self.im = Frac(b)
    
    def __neg__(s):
        return Complex(-Frac(s.re), -Frac(s.im))
    def __pos__(s):
        return Complex(Frac(s.re), Frac(s.im))
    def __abs__(s):
        return (s.re*s.re + s.im*s.im)**.5
    def __int__(s):
        return int(s.re)
    def __float__(s):
        return float(s.re)
    def __invert__(s):
        return Complex(Frac(s.re), -Frac(s.im))
    
    def __add__ (s, o):
        if type(o) != Complex:
            return s + Complex(o)
        return Complex (s.re+o.re, s.im+o.im)
    def __radd__ (s, o):
        return s + o
    
    def __sub__ (s, o):
        if type(o) != Complex:
            return s - Complex(o)      
        return Complex (s.re-o.re, s.im-o.im)
    def __rsub__ (s, o):
        return - (s - o)
    
    def __mul__ (s,o):
        if type(o) != Complex:
            return s * Complex(o)
        return Complex (s.re*o.re - s.im*o.im, s.re*o.im + s.im*o.re)
    def __rmul__(s,o):
        return s * o
    
    def __truediv__ (s,o):
        if type(o) != Complex:
            return s / Complex(o)
        c = s * (~o)
        a = o.re*o.re + o.im*o.im
        c.re /= a
        c.im /= a
        return c
    def __rtruediv__ (s,o):
        return Complex(o)/s
    
    def __pow__ (s, o, m=-1):
        if m==-1:
            if type(o) != Frac:
                return pow(s, Frac(o))
            return Frac(pow (s.a, o.a/o.b), pow (s.b, o.a/o.b))
        else:
            if type(o) != Frac:
                return pow(s, Frac(o), m)
            return Frac(pow (s.a, o.a/o.b, m), pow (s.b, o.a/o.b, m))
    def __rpow__(s, o, m):
        return pow(Frac(o), s, m)
    
    def __str__ (s):
        if s.re==0 and s.im==0:
            return "0"
        elif s.re==0:
            return str(s.im)+"i"
        elif s.im==0:
            return str(s.re)
        elif s.im==-1:
            return str(s.re) + "-i"
        elif s.im<0:
            return str(s.re) + str(s.im) + "i"
        elif s.im==1:
            return str(s.re) + "+i"
            
        return str(s.re) + "+" + str(s.im) + "i"
        
    def __lt__(s, o):
        if type(o) != Complex:
            return s < Complex(o)
        return s.a*o.b < o.a*s.b
    def __le__(s, o):
        if type(o) != Complex:
            return s <= Complex(o)
        return s.a*o.b <= o.a*s.b
    def __eq__(s, o):
        if type(o) != Complex:
            return s == Complex(o)
        return (s - o).a == 0 
    def __ne__(s, o):
        if type(o) != Complex:
            return s != Complex(o)
        return (s - o).a != 0 
    def __ge__(s, o):
        if type(o) != Complex:
            return s >= Complex(o)
        return s.a*o.b >= o.a*s.b
    def __gt__(s, o):
        if type(o) != Complex:
            return s > Complex(o)
        return s.a*o.b > o.a*s.b
    
def addl (L1,L2,c):
    return [ b+a*c  for a,b in zip(L1,L2)]

def subl (L1, L2, c):
    return [ b-a*c  for a,b in zip(L1,L2)]
    
def divl (L, c):
    return [ a/c for a in L]
    
def printl (L):
    s = "[ "
    for a in L:
        s += str(a) + ", "
    return s[:-2] + " ]"

def printM ():
    print(printl(L1))
    print(printl(L2))
    print(printl(L3))
    
"""L1 = [Complex(2), Complex(3), Complex(4)]
L2 = [Complex(0,2),Complex(-3),Complex(0,-4)]
L3 = [Complex(2,2),Complex(0,6),Complex(-8,8)]"""


def f():
    
    L1 = [Complex(2), Complex(3), Complex(4)]
    L2 = [Complex(0,2),Complex(-3),Complex(0,-4)]
    L3 = [Complex(2,2),Complex(0,6),Complex(-8,8)]
    
    K1 = [Complex(1), Complex(0), Complex(0)]
    K2 = [Complex(0), Complex(1), Complex(0)]
    K3 = [Complex(0), Complex(0), Complex(1)]
    
    K2 = subl(K1, K2, L2[0]/L1[0])
    L2 = subl(L1, L2, L2[0]/L1[0])
    
    K3 = subl(K1, K3, L3[0]/L1[0])
    L3 = subl(L1, L3, L3[0]/L1[0])
    
    K3 = subl(K2, K3, L3[1]/L2[1])
    L3 = subl(L2, L3, L3[1]/L2[1])
    
    
    K3 = divl(K3, L3[2])
    L3 = divl(L3, L3[2])
    
    
    K2 = subl(K3,K2,L2[2])
    L2 = subl(L3,L2,L2[2])
    
    K1 = subl(K3,K1,L1[2])
    L1 = subl(L3,L1,L1[2])
    
    K2 = divl(K2, L2[1])
    L2 = divl(L2, L2[1])
    
    K1 = subl(K2,K1,L1[1])
    L1 = subl(L2,L1,L1[1])
    
    K1 = divl(K1, L1[0])
    L1 = divl(L1, L1[0])
    
    
    
    print(printl(L1))
    print(printl(L2))
    print(printl(L3))
    
    print("----------")
    
    print(printl(K1))
    print(printl(K2))
    print(printl(K3))
    
    
    #verif
    
    
    M = [[Complex(2), Complex(3), Complex(4)],\
        [Complex(0,2), Complex(-3), Complex(0,-4)],\
        [Complex(2,2), Complex(0,6), Complex(-8,8)]]
    
    K = [K1, K2, K3]
    
    R = [[0 for j in range(3)] for i in range(3)]
    
    for i in range(3):
        for j in range(3):
            s = Complex(0)
            for k in range(3):
                s += M[i][k] * K[k][j]
            R[i][j] = s
    
    print(printl(R[0]))
    print(printl(R[1]))
    print(printl(R[2]))



def g (L):
    
    A = [\
            [Complex(1), Complex(0), Complex(0), Complex(0)],\
            [Complex(Frac(-3,4),Frac(3,4)), Complex(0,Frac(-1,2)), Complex(Frac(1,2)), Complex(Frac(1,4),Frac(-1,4))],\
            [Complex(0,Frac(-2,3)), Complex(Frac(1,2),Frac(1,6)), Complex(Frac(-1,2),Frac(1,6)), Complex(0,Frac(1,3))],\
            [Complex(Frac(1,8),Frac(1,8)), Complex(Frac(-1,8),Frac(1,8)), Complex(Frac(1,8),Frac(-1,8)), Complex(Frac(-1,8),Frac(-1,8))]\
        ]
    
    """for a in A:
        print(printl(a))"""
    
    R = [Complex(0) for i in A[0]]
    
    for i,a in enumerate(L):
        R = addl(A[i], R, a)
    
    
    print(printl(R))



import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D

def plot (z0, z1, z2, z3):
    
    a1 = z0
    a2 = Complex(Frac(-3,4),Frac(3,4))*z0 + Complex(0,Frac(-1,2))*z1 + Complex(Frac(1,2))*z2 + Complex(Frac(1,4),Frac(-1,4))*z3
    a3 = Complex(0,Frac(-2,3))*z0 + Complex(Frac(1,2),Frac(1,6))*z1 + Complex(Frac(-1,2),Frac(1,6))*z2 + Complex(0,Frac(1,3))*z3
    a4 = Complex(Frac(1,8),Frac(1,8))*z0 + Complex(Frac(-1,8),Frac(1,8))*z1 + Complex(Frac(1,8),Frac(-1,8))*z2 + Complex(Frac(-1,8),Frac(-1,8))*z3
    
    N = 50
    
    X = [i/N for j in range(N+1) for i in range(N+1)]
    Y = [j/N for j in range(N+1) for i in range(N+1)]
    Z = [0 for j in range(N+1) for i in range(N+1)]
    
    for i,(x,y) in enumerate(zip(X,Y)):
        c = Complex(Frac(int(x*N),N),Frac(int(y*N),N))
        Z[i] = float(c*(a1 + c*(a2 + c*(a3 + c*a4))))
    
    fig = pl.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot_trisurf(X,Y,Z)
    pl.show()