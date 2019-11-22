N = ['A', 'B', 'C', 'D', 'E', 'F']

A = [(0,1,2), (0,2,1), (0,3,2), (1,3,1), (2,5,5), (3,4,1), (3,5,3), (4,5,1)]

L = []

F = []

end = 0

def getNei (n):
    nei = []
    
    for (i,j,k) in A:
        if i==n:
            nei.append([j,k])
        elif j==n:
            nei.append([i,k])
    
    return nei


def updateF (m):
    global L, F
    
    for i in range(len(L)):
        if L[i][0]==m[0]:
            return
    
    i=0
    while i<len(F) and m[1]>=F[i][1]:
        if F[i][0]==m[0]:
            return
        i+=1
        
    F.insert(i,m)
    
    i+=1
    
    while i<len(F):
        if F[i][0]==m[0]:
            F.pop(i)
            return
        i+=1
    
    return


def majF ():
    global F,L
    m = F.pop(0)
    
    if m[0] == end:
        return m[1]
    
    nei = getNei(m[0])
    
    for j in range(len(nei)):
        updateF([nei[j][0], nei[j][1]+m[1]])
        
    L.append(m)

    return -1
    
    
def dijkstra (s, e):
    global end, F
    F.append([s,0])
    end = e
    
    i=-1
    while i==-1:
        i = majF()
    
    return i



