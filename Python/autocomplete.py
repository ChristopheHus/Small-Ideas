import random as r

def compr (a,b):
    if len(b)<len(a):
        for i in range(len(b)):
            if b[i]>a[i]:
                return True
            elif b[i]<a[i]:
                return False
        return False
    
    else:
        for i in range(len(a)):
            if b[i]>a[i]:
                return True
            elif b[i]<a[i]:
                return False
        return True

def genL ():
    
    global L
    
    def genStr (l):
        s = ""
        
        for j in range(l):
            s += chr( r.randint(97,122) )
        
        for j in range(len(L)):
            if compr(s,L[j]):
                L.insert(j,s)
                return
        
        L.append(s)
    
    for i in range(1000):
        genStr( r.randint(1,10) )
    
    return




def compl (s):
    
    global L
    
    def compr2 (a,b):
        
        if len(b)<len(a):
            for i in range(len(b)):
                if a[i]<b[i]:
                    return 1
                elif a[i]>b[i]:
                    return -1
            return -1
        
        for i in range(len(a)):
            if a[i] > b[i]:
                return -1
            elif a[i] < b[i]:
                return 1
                
        return 0
    
    min = 0
    max = len(L)-1
    
    k = compr2(s, L[min])
    
    if k>0:
        return []
    elif k==0:
        for i in range(min+1, len(L)):
            if compr2(s,L[i]) != 0:
                return L[min:i]
    
    k = compr2(s, L[max])
    
    if k<0:
        return []
    elif k==0:
        for i in range(max-1, -1, -1):
            if compr2(s,L[i]) != 0:
                return L[i+1:max+1]
    
    
    m = (min + max) // 2
    
    while m != min:
        k = compr2 (s,L[m])
        
        if k>0:
            max = m
        elif k<0:
            min = m
        else:
            min = m - 1
            max = m + 1
            while compr2(s, L[min]) == 0:
                min -= 1
            while compr2(s, L[max]) == 0:
                max += 1
            
            return L[min+1:max]
            
        
        m = (min + max) // 2
    
    return []