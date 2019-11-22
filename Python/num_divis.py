
def genPrime ():
    global prime
    
    prime = [2]
    
    for i in range(3,10000):
        
        j = int(i**.5)
        
        
        k=0
        isp = True
        
        while isp and prime[k]<=j:
            if i%prime[k] == 0:
                isp = False
            k+=1
        
        if isp:
            prime.append(i)



def getDiv (n):
    div = []
    
    k=0
    
    while k<len(prime) and n>=prime[k]:
        
        while n%prime[k] == 0:
            n = n//prime[k]
            div.append(prime[k])
            
        k += 1
    
    return div
    
def getvp (t):
    k = 0
    vp = []
    
    for i in t:
        
        if i==k:
            vp[-1] += 1
        
        else:
            k = i
            vp.append(1)
    
    return vp

def getNDiv (n):
    t = getvp (getDiv(n))
    
    s = 1
    
    for i in t:
        s *= i+1
    
    return s
    
    
    
    
    
    
    
    
    
    