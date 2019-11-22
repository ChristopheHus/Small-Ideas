L = []

def add1 (T,U=[]):
    global L
    
    if T[0]<3:
        if len(T)>1:
            L.append(U+[T[0]+1]+T[1:])
        else:
            L.append(U+[T[0]+1])
    
    for k in range(0,len(T)-1):
        if T[k]>T[k+1]:
            add1(T[k+1:],U+T[0:k+1])


def supprDbl (T):
    i = 1
    
    while i<len(T):
        if T[i]==T[i-1]:
            T.pop(i)
        else:
            i+=1
    
    return T

def add (T,k):
    global L
    
    L = []
    M = [T]
    
    for i in range(0,k):
        for a in M:
            add1(a)
            
        M = supprDbl(L)
        L = []
    
    return M