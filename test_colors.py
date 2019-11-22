


def scalar_prod (A, B):
    
    if len(A) != len(B):
        return 0
    
    s = 0
    
    for i in range(len(A)):
        s += A[i] * B[i]
    
    return s


def norme_sq (x):
    
    s = 0
    
    for i in range(len(x)):
        s += x[i] * x[i]
    
    return s


def getCompose (x, a):
    
    Ct = [0 for _ in x]
    Cn = [0 for _ in x]
    
    sp = scalar_prod (x,a)
    n = norme_sq (a)
    
    for i in range(len(x)):
        Ct[i] = a[i] * sp / n
        
        Cn[i] = x[i] - Ct[i]
    
    
    return Ct, Cn



def sqrt (x, p):
    
    x1 = 1
    x2 = 3/2
    
    
    while (x2-x1 > p):
        xm = (x1+x2) / 2
        ym = xm * xm
        
        if ym < x:
            x1 = xm
        elif ym > x:
            x2 = xm
        else:
            return xm
    
    return (x1+x2)/2