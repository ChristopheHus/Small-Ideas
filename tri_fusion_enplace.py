import random as r


def tri (T):
    
    s = 1
    l = len(T)
    
    while s<l :
        print("s =", s)
        p=0
        
        while p+s<l:
            
            print("p =", p)
            i=0
            
            while i<s:
                print (T[p:min(p+2*s,l)]," -> ", end='', sep='')
                j = p+s
                
                if T[j]<T[p+i]:
                    temp = T[p+i]
                    T[p+i] = T[j]
                    
                    j += 1
                    while j<min(p+2*s,l) and temp>T[j]:
                        T[j-1] = T[j]
                        j+=1
                    
                    T[j-1] = temp
                    
                i += 1
                
                print(T[p:min(p+2*s,l)])
            
            p += 2*s
        
        s *= 2
        
        
    return T