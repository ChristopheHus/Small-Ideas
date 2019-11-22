def getExprs (s):
    L = [""]
    i = 0
    
    for c in s:
        if c == '+' or c == '*':
            L.append("")
            i += 1
        else:
            L[i] += c
    
    return L

def fix (s):
    r = ""   
     
    numLast = False
    alphaLast = False
    opLast = False
    requOp = False # ')'

    for c in s:
    
        if not(opLast):
            if c == '-':
                r += "+-"
                opLast = True
                numLast = False
                alphaLast = False
                requOp = False
                continue
            elif c == '/':
                r += "*/"
                numLast = False
                alphaLast = False
                requOp = False
                opLast = True
                continue
                
        if c == '*' or c == '+':
            if opLast:
                print('error : 2 op')
                return ""
            r += c
            numLast = False
            alphaLast = False
            requOp = False
            opLast = True
            continue
        
        elif c.isalpha():
            if numLast or requOp:
                r += '*'
            r += c
            numLast = False
            alphaLast = True
            requOp = False
            opLast = False
            continue
        
        elif c.isnumeric():
            if requOp:
                r += '*'
            r += c
            numLast = True
            alphaLast = False
            requOp = False
            opLast = False
            continue
        
        elif c == '(' or c == '[' or c == '{':
            if not(opLast):
                r += '*'
            r += '('
            
            numLast = False
            alphaLast = False
            requOp = False
            opLast = True
        
        elif c == ')' or c == ']' or c == '}':
            r += ')'
            numLast = False
            alphaLast = False
            requOp = True
            opLast = False
        
        else:
            continue
    
    return r


def constr (s):
    if s[0] == '(' and s[-1] == ')':
        test = False
        k = 0
        for c in s:
            if c == '(':
                k += 1
            elif c == ')':
                k -= 1
            elif k == 0:
                test = True
            elif k<0:
                print('error : parenthesis')
                return []
        if not(test):
            return constr(s[1:-1])
    
    L = []
    
    
    
    