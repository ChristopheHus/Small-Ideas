def hilbert (n):
    
    if n==0:
        return []
        
    def swap (A):
        B = []
        for i,j in A:
            B.append((j,i))
        return B
    
    def rev (A):
        B = []
        for i in range(len(A)-1,-1,-1):
            a, b = A[i]
            B.append((a,-b))
        return B
    
    K = hilbert(n-1)
    
    L = swap(K) + [(0,1)] + K
    
    L = L + [(1,0)] + rev(L)
    
    return L
    
    