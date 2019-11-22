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
            c, d = b.as_integer_ratio()
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
        if s.b == 1:
            return str(s.a)
        elif s.a == 0:
            return "0"
            
        return str(s.a) + "/" + str(s.b)
    
    def eval (s):
        return s.a / s.b
        
    def __lt__(s, o):
        return s.a*o.b < o.a*s.b
    def __le__(s, o):
        return s.a*o.b <= o.a*s.b
    def __eq__(s, o):
        return (s - o).a == 0 
    def __ne__(s, o):
        return (s - o).a != 0 
    def __ge__(s, o):
        return s.a*o.b >= o.a*s.b
    def __gt__(s, o):
        return s.a*o.b > o.a*s.b



class Poly:
    def __init__ (s, L):
        
        if type(L) == Poly:
            s.L = []
            
            for i in L.L:
                s.L.append(i)
        
        elif type(L) == int:
            if L == 0:
                s.L = []
            else:
                s.L = [Frac(L)]
        elif type(L) == Frac:
            if L == 0:
                s.L = []
            else:
                s.L = [L]
        else:
            j = len(L)-1
            
            while j>=0 and L[j] == 0:
                j-=1
            
            if type(L[0]) == Frac:
                s.L = [L[i] for i in range(j+1)]
            else:
                s.L = [Frac(L[i]) for i in range(j+1)]
    
    def __add__ (s, o):
        if len(o.L) > len(s.L):
            M = [None for i in range(len(o.L))]
            
            for i in range(len(s.L)):
                M[i] = s.L[i] + o.L[i]
            
            for i in range(len(s.L),len(o.L)):
                M[i] = o.L[i]
        
        
        else:
            M = [None for i in range(len(s.L))]
            
            for i in range(len(o.L)):
                M[i] = s.L[i] + o.L[i]
            
            for i in range(len(o.L),len(s.L)):
                M[i] = s.L[i]
                
        return Poly(M)
    
    def __sub__ (s, o):
        if len(o.L) > len(s.L):
            M = [None for i in range(len(o.L))]
            
            for i in range(len(s.L)):
                M[i] = s.L[i] - o.L[i]
            
            for i in range(len(s.L),len(o.L)):
                M[i] = o.L[i]
        
        
        else:
            M = [None for i in range(len(s.L))]
            
            for i in range(len(o.L)):
                M[i] = s.L[i] - o.L[i]
            
            for i in range(len(o.L),len(s.L)):
                M[i] = s.L[i]
                
        return Poly(M)
    
    def __mul__ (s,o):
        if type(o)==Frac:
            M = [s.L[i] for i in range(len(s.L))]
            for i in range(len(s.L)):
                M[i] *= o
            return Poly(M)
        elif type(o) == float or type(o) == int:
            return s * Frac(o)
        
        M = [Frac(0) for i in range(len(s.L)+len(o.L)-1)]
        
        for i in range(len(s.L)):
            for j in range(len(o.L)):
                M[i+j] += s.L[i] * o.L[j]
        
        return Poly(M)
    
    def __rmul__ (s, o):
        return s * o
    
    def __floordiv__ (S, O):
        if len(O.L) > len(S.L):
            return Poly(0)
        else:
            if len(O.L) == 0:
                return None
            
            l1 = len(S.L) - 1
            l2 = len(O.L) - 1
            dl = l1 - l2 + 1
            
            L = [Frac(0) for i in range(dl)]
            
            M = [Frac(i) for i in S.L]
            
            for k in range(dl):
                l = dl - k - 1
                L[l] = M[l1-k] / O.L[l2]
                for i,e in enumerate(O.L):
                    M [l + i] -= L[l]*e
            
            return Poly(L)
    
    def __mod__ (S, O):
        if len(O.L) > len(S.L):
            return Poly(S)
        else:
            if len(O.L) == 0:
                return None
            
            l1 = len(S.L) - 1
            l2 = len(O.L) - 1
            dl = l1 - l2 + 1
            
            M = [Frac(i) for i in S.L]
            
            for k in range(dl):
                l = dl - k - 1
                a = M[l1-k] / O.L[l2]
                for i,e in enumerate(O.L):
                    M [l + i] -= a*e
            
            return Poly(M)
    
    def __lshift__ (S, a):
        if type(a) != int:
            return NotImplemented
        return Poly(S.L[a:])
    
    def __rshift__ (S, a):
        if type(a) != int:
            return NotImplemented
        return Poly(a*[Frac(0)] + S.L)
        
    def __str__ (s):
        if s.L == []:
            return "0"
        
        j = len(s.L)-1
        
        if j==0:
            return str(s.L[0])
        
        elif j==1:
            if s.L[1].eval() == 1:
                st = "X"
            else:
                st = str(s.L[1]) + ".X"
                
            if s.L[0].a > 0:
                st += " + " + str(s.L[0])
            elif s.L[0].a < 0:
                st += " - " + str(Frac(-s.L[0].a, s.L[0].b))
            
            return st
        
        if s.L[j].eval() == 1:
            st = "X^" + str(j)
        else:
            st = str(s.L[j]) + ".X^" + str(j)
        j-=1
        
        while j>=2:
            if s.L[j].a != 0:
                if s.L[j].eval()==1:
                    st += " + " + "X^" + str(j)
                else:
                    if s.L[j].a >= 0:
                        st += " + " + str(s.L[j]) + ".X^" + str(j)
                    else:
                        st += " - " + str(Frac(-s.L[j].a, s.L[j].b)) + ".X^" + str(j)
            j-=1
            
        if s.L[1].a != 0:
            if s.L[1].eval() == 1:
                st += " + " + "X"
            else:
                if s.L[1].a >= 0:
                    st += " + " + str(s.L[1]) + ".X"
                else:
                    st += " - " + str(Frac(-s.L[1].a, s.L[1].b)) + ".X"
        
        if s.L[0].a != 0:
            st += " + " + str(s.L[0])
        
        return st
    
    def __getitem__(S, a):
        if type(a) == slice:
            return S.L[a.start:a.stop:a.step]
        else:
            return S.L[a]
    
    def __setitem__(S, a, b):
        if type(a) == slice:
            S.L[a.start:a.stop:a.step] = b
        else:
            S.L[a] = b
        
    
    def eval (s,x):
        y = 1
        res = 0
        
        for i in s.L:
            res += i.eval()*y
            y *= x
        
        return res
    
    def chgVar (S, P):
        Q = Poly ([Frac(1)])
        M = Poly ([Frac(0)])
        
        for i in range(len(S.L)):
            M += Q * S.L[i]
            Q *= P
        
        return M
    
    def deriv (S, n):
        
        P = Poly(S)
        
        for k in range(n):
            M = []
            for i,e in enumerate(P.L[1:]):
                M.append(e * Frac(i+1))
            P.L = M
        
        return P
    
    def __len__ (S):
        return len(S.L) - 1
        

def interpolation (X, Y):
    P = Poly([])
    
    for i in range(len(X)):
        Q = Poly([Frac(1)])
        n = Frac(1)
        
        for j in range(len(X)):
            if j != i:
                Q *= Poly([X[j].neg(), Frac(1)])
                n *= X[i] - X[j]
        
        P += Q * (Y[i] / n)
    
    return P


import matplotlib.pyplot as pl
def draw (P, a, b):
    X = [(b-a)*i/1000 + a for i in range(1000)]
    Y = [P.eval(X[i]) for i in range(1000)]
    
    pl.plot(X, Y)