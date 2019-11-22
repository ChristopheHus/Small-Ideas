neg = '!'
operators = ['&','|']

def extractExprs(s):
    n = False
    e1 = ""
    e2 = ""
    op = ""
    
    c0 = 0
    c1 = len(s)-1
    w = s
    k = True
    while k   and   c0 < c1:
        if s[c0] == neg:
            n = not(n)
            c0 += 1
            w = s[c0:c1+1]
        if s[c0] == '('   and   s[c1] == ')':
            c0 += 1
            w = s[c0:c1]
            c1 -= 1
        else:
            k = False
    
    i = 0
    k = True
    while k:
        i += 1
        if i < len(w):
            k = not(w[i] in operators)
        else:
            k = False
        
    if i == len(w):
        op = ""
        e1 = w
        return n, op, e1, e2
            
    ci = i
    if w[ci-1] == neg:
        ci -= 1
        n = not(n)
    op = w[i]
        
    e1 = w[0:ci]
    e2 = w[i+1:len(w)]
    
    return n, op, e1, e2
    

class Expr:
    def __init__(a,s):
        a.n, a.op, a.e1, a.e2 = extractExprs(s)
        if (a.op!=""):
            a.e1 = Expr(a.e1)
            a.e2 = Expr(a.e2)



def simplificator(a):
    cn = 0
    for i in a:
        cn += i[1]
    
    if cn >= 2:
        a[2][0] = op[0]*(a[2][0]==op[1]) + op[1]*(a[2][0]==op[0])
        
        for i in a:
            i[1] = not(i[1])
    
    return a
