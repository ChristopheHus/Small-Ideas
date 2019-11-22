import matplotlib.pyplot as pl


def pgcd(a,b):
    i, j = a, b
    while j!=0:
        i, j = j, i%j
    return i
    
def copyF(i):
    return Fract(i.a, i.b)
    
def addF(i,j):
    return Fract(i.a*j.b + j.a*i.b, i.b*j.b)

def invF(i):
    return Fract(i.b, i.a)
    
def multF(i,j):
    return Fract(i.a*j.a, i.b*j.b)

class Fract:
    def __init__(s,a,b=1):
        s.a = a
        s.b = b
        s.simp()
    def simp(s):
        x = pgcd(s.a,s.b)
        s.a = int(s.a/x)
        s.b = int(s.b/x)
    def add(s,i):
        s.a = s.a*i.b + i.a*s.b
        s.b = s.b*i.b
        s.simp()
    def mult(s,i):
        s.a *= i.a
        s.b *= i.b
        s.simp()
    def inv(s):
        s.a, s.b = s.b, s.a
    def eval(s):
        return s.a/s.b
    def __str__(s):
        return str(s.a) + '/' + str(s.b)
        
class Poly:
    def __init__(s,l):
        s.l = [Fract(l[i]) for i in range(len(l))]
    def add(s,i):
        if len(s.l) < len(i.l):
            for k in range(len(s.l)):
                s.l[k].add(i.l[k])
            for k in range(len(s.l), len(i.l)):
                (s.l).append(copyF(i.l[k]))
        else:
            for k in range(len(i.l)):
                s.l[k].add(i.l[k])
    def mult(s,i):
        X = s.l[:]
        n = len(s.l) + len(i.l) - 1
        for k in range(len(s.l)):
            s.l[k] = Fract(0)
        for k in range(len(s.l),n):
            s.l.append(Fract(0))
        for j in range(len(i.l)):
            for k in range(len(X)):
                s.l[k+j].add(multF(i.l[j],X[k]))
    def eval(s,x):
        u = 1
        res = 0
        for i in range(len(s.l)):
            res += multF(s.l[i],Fract(u)).eval()
            u *= x
        return res
    def deriv(s,n=1):
        for i in range(n):
            for j in range(len(s.l)-1):
                s.l[j] = multF(Fract(j+1),s.l[j+1])
            s.l[len(s.l)-1] = Fract(0)
    def disp(s):
        for i in range(len(s.l)):
            print(str(s.l[i].a)+" / "+str(s.l[i].b))

def interpolation(X,Y):
    if len(X) != len(Y):
        return Poly([Fract(0)])
    P = Poly([])
    
    for i in range(len(Y)):
        b = 1
        for j in range(len(X)):
            if j!=i:
                b *= X[i]-X[j]
        a = Poly([Fract(Y[i],b)])
        for j in range(len(X)):
            if j!=i:
                a.mult(Poly([Fract(-X[j]),Fract(1)]))
        P.add(a)
    
    return P
    
def system (l):
    n = len(l)
    
    def swap (i,j):
        for k in range(n+1):
            l[i][k], l[j][k] = l[j][k], l[i][k]
    
    for i in range(n-1):
        w = i+1
        while l[i][i].eval() == 0:
            if w >= n:
                print("error : null matrix")
                return [0 for i in range(n)]
            swap (i,i+1)
            w += 1
        
        k = invF(l[i][i])
        for j in range(i,n+1):
            l[i][j].mult(k)
        
        for j in range(i+1,n):
            if l[j][i].eval() != 0:
                w = copyF(l[j][i])
                for k in range(i,n+1):
                    e = Fract(-1)
                    e.mult(multF(w,l[i][k]))
                    l[j][k].add(e)
    
    k = invF(l[n-1][n-1])
    l[n-1][n-1].mult(k)
    l[n-1][n].mult(k)
    
    for i in range(n-1,0,-1):
        for j in range(i-1,-1,-1):
            if l[j][i].eval() != 0:
                w = copyF(l[j][i])
                
                e = Fract(-1)
                e.mult(multF(w,l[i][n]))
                l[j][n].add(e)
                
                e = Fract(-1)
                e.mult(w)
                l[j][i].add(e)
    
    for i in range(n):
        print(l[i][n], end=', ')
    
    return [l[i][n].eval() for i in range(n)]
    
    
  
"""  
p = interpolation([0,1,2,3],[1,0,1,0])
q = interpolation([0,1,2,3],[0,1,0,1])

print("p :")
p.disp()
print("\nq :")
q.disp()

X = []
Y = []
Z = []
for i in range(801):
    X.append(i/100)
    Y.append(p.eval(i/100))
    Z.append(q.eval(i/100))
    
pl.plot(X,Y,color='c')
pl.plot(X,Z)
pl.ylim(ymax=10,ymin=0)
"""