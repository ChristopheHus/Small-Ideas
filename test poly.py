def fun1 (s):
    
    L = ['']
    Neg = [False]
    mul = False
    i = 0
    
    for c in s:
        if mul:
            mul = False
            if c == '*':
                L[i] += '^'
                continue
            else:
                L[i] += '*'
        
        if c == '+':
            L.append('')
            Neg.append(False)
            i += 1
        elif c == '-':
            L.append('')
            Neg.append(True)
            i += 1
            
        elif c == ' ':
            continue
            
        elif c == '.':
            L[i] += '*'
        
        elif c == '*':
            mul = True
            
        elif c.isalpha():
            if L[i] != '' and L[i][-1] != '*':
                L[i] += '*' + c
            else:
                L[i] += c
            
        else:
            L[i] += c
    
    for a,b in zip(L,Neg):
        M = ['']
        i = 0
        
        for c in a:
            if c == '*':
                M.append('')
                i += 1
            else:
                M[i] += c
        
        
        
        
    
    return L, Neg