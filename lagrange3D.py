import math as m
import struct
import random as r

def fix (L, inlog):
    mi = int(L[0][0])
    ma = int(L[0][0])
    
    for i in range(100):
        for j in range(100):
            if L[i][j]>=0:
                L[i][j] = int(L[i][j]+.5)
            else:
                L[i][j] = int(L[i][j]-.5)
            if L[i][j]>ma:
                ma = L[i][j]
            elif L[i][j]<mi:
                mi = L[i][j]
    
    if (inlog):
        ma = m.log(ma-mi+1)
    
        for i in range(100):
            for j in range(100):
                L[i][j] = 255 * m.log(L[i][j] - mi + 1) / ma
    else:
        for i in range(100):
            for j in range(100):
                L[i][j] = 255 * (L[i][j] - mi) / (ma - mi)
    return L


def writeFile (L):
    
    with open("C:/Users/Christophe/Desktop/test.pgm", "w") as f:
        f.write('P2\n')
        
        f.write('100 100\n')
        
        f.write('255\n')
        
        
        for j in range(100):
            for i in range(100):
                f.write(str(L[i][j]))
                if i==99:
                    f.write('\n')
                else:
                    f.write(' ')
                #f.write(struct.pack('B', L[i][j]))
    
    #with open("C:/Users/Christophe/Desktop/test.pgm", "ab") as f:


def norme (x, y):
    #return abs(x) + abs(y)
    #return max(abs(x), abs(y))
    return m.sqrt(x**2 + y**2)


def Q (L, i, x, y):
    
    n = 1
    m = 1
    xi, yi, zi = L[i]
    
    for j in range(len(L)):
        if j != i:
            tx, ty, tz = L[j]
            n *= norme(x-tx, y-ty)
            m *= norme(xi-tx, yi-ty)
    
    return zi*n/m

def P (L, x, y):
    z = 0
    
    for i in range(len(L)):
        z += Q (L,i,x,y)
    
    return z

def Ptot (L):
    
    return [ [P(L,x,y) for y in range(100) ] for x in range(100) ]
    
def fun_all (L, inlog):
    return writeFile (fix (Ptot (L), inlog))

def getRandL (n):
    L = []
    
    for k in range(n):
        L.append ((r.randint(0,99), r.randint(0,99), r.randint(70,180)))
    
    return L

