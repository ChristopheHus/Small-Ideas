neg = '!' # negation symbol
boo = 'True'
operators = ['&','|',':'] # bool -> bool operators' symbols
# AND ; OR ; XNOR
vars = [] # ['a',False,-1,-1,-1] : value, not it, reference to parent, reference to childs
v2 = []
otv = 0

def testP (s, c0, c1):
    if s[c0] != '('   or   s[c1] != ')':
        return False
    p=0
    for i in range(c0,c1):
        if s[i]=='(':
            p += 1
        elif s[i]==')':
            p-=1
        if p == 0:
            return False
    return True


def extractExprs(s):
    n = False
    c0 = 0
    c1 = len(s)-1
    w = s
    k = True
    z = False
    while k   and   c0 < c1:
        if s[c0] == neg:
            z = not(z)
            c0 += 1
            w = s[c0:c1+1]
        if testP (s, c0, c1) :
            c0 += 1
            w = s[c0:c1]
            c1 -= 1
            if (z):
                z = False
                n = not(n)
        else:
            k = False
    
    i = -1
    k = True
    if (z):
        w = '!' + w
    print("w :",w)
    while k:
        i += 1
        if i < len(w):
            p = (w[i] == '(')
            while p>0:
                i += 1
                p += (w[i] == '(') - (w[i] == ')')
            if w[i] in operators:
                k = False
        else:
            k = False
        
    if i == len(w):
        op = ""
        if w[0]=='!':
            e1 = w[1:len(w)]
            n = True
        else:
            e1 = w
        
        return n, e1, "", ""
            
    ci = i
    if w[ci-1] == neg:
        ci -= 1
        n = not(n)
    op = w[i]
    
    e1 = w[0:ci]
    e2 = w[i+1:len(w)]
    
    return n, op, e1, e2
    

def extract (s,i,ele):
    global vars
    global v2
    
    n, op, e1, e2 = extractExprs(s)
    
    if e1=="":
        v2.append([op,n,i,ele,-1])
    else:
        vars.append([op,n,i,-1,-1])
        w = len(vars)-1
        vars[i][ele+2] = w
        
        extract (e1,w,1)
        extract (e2,w,2)


def sortV ():
    global vars
    global otv
    vp = []
    l = []
    l2 = [-1 for i in vars]
    
    varsPos = 0
    for i in range(len(vars)):
        if len(vars[i])!=0:
            if vars[i][3] == -1:
                l.append(i)
            else:
                l.insert(varsPos,i)
                varsPos += 1
    
    for i in range(len(l)):
        l2[l[i]] = i
        vp.append(vars[l[i]])
    l2.append(-1)
        
    for i in range(len(l)):
        vp[i][2] = l2[vp[i][2]]
        vp[i][3] = l2[vp[i][3]]
        vp[i][4] = l2[vp[i][4]]
        
    vars = vp
    otv = varsPos
    
    
    

        
def genTree (s):
    global vars
    global v2
    global otv
    
    n, op, e1, e2 = extractExprs(s)
    vars = [[op,n,-1,-1,-1]]
    
    if e1!='':
        extract (e1,0,1)
        extract (e2,0,2)
        
        otv = len(vars)
        vordre = [0]
        
        for i in range(1,len(v2)):
            x = 0
            k = True
            while k:
                if x<len(vordre):
                    if v2[i][0]<v2[vordre[x]][0]:
                        k = False
                        vordre.insert (x,i)
                    else:
                        x +=1
                else:
                    k = False
                    vordre.append (i)
        
        for i in vordre:
            vars.append ([v2[i][0],v2[i][1],v2[i][2],-1,-1])
            vars [v2[i][2]] [v2[i][3]+2] = len(vars)-1
        v2 = []


def equals (e1, e2):
    global vars
    
    if vars[e1][0] != vars[e2][0] or vars[e1][1] != vars[e2][1]:
        return False
    if vars[e1][3] == -1 and vars[e2][3] == -1:
        return True
    return ( equals(vars[e1][3],vars[e2][3]) and equals(vars[e1][4],vars[e2][4]) )   or   ( equals(vars[e1][3],vars[e2][4]) and equals(vars[e1][4],vars[e2][3]) )
    
def equalsAbs (e1,e2):
    global vars
    
    if vars[e1][0] != vars[e2][0]:
        return False
    if vars[e1][3] == -1 and vars[e2][3] == -1:
        return True
    return ( equals(vars[e1][3],vars[e2][3]) and equals(vars[e1][4],vars[e2][4]) )   or   ( equals(vars[e1][3],vars[e2][4]) and equals(vars[e1][4],vars[e2][3]) )
    
def delVar (i):
    global vars
    todel = [i]
    while len(todel)>0:
        if vars[todel[0]][3] != -1:
            todel.append(vars[todel[0]][3])
        if vars[todel[0]][4] != -1:
            todel.append(vars[todel[0]][4])
        vars[todel[0]] = []
        todel.pop(0)
    

def simplify ():
    global vars
    global otv
    global boo
    
    # Not simplification by going down the tree
    for i in range(otv):
        a = vars[i][3]
        b = vars[i][4]
        nn = vars[i][1] + vars[a][1] + vars[b][1]
        print (nn, vars[i][0])
        
        if (nn>=2):
            if vars[i][0]==operators[0]:
                #!a !& !b --> a | b
                vars[i][0] = operators[1]
                vars[i][1] = not (vars[i][1])
                vars[a][1] = not (vars[a][1])
                vars[b][1] = not (vars[b][1])
                
            elif vars[i][0]==operators[1]:
                #!a !| !b --> a & b
                vars[i][0] = operators[0]
                vars[i][1] = not (vars[i][1])
                vars[a][1] = not (vars[a][1])
                vars[b][1] = not (vars[b][1])
                
            elif vars[i][0]==operators[2]:
                #!a <=> !b ou !a !<=> b --> a <=> b
                vars[i][1] = False
                vars[a][1] = False
                vars[b][1] = False
            
    # Similar vars simplification
    op = list(range(otv,len(vars)))
    
    while not(0 in op):
        op1 = op[:]
        op = []
        for i in op1:
            if not(vars[i][2] in op):
                op.append(vars[i][2])
        
        for i in op:
            a = vars[i][3]
            b = vars[i][4]
            if equalsAbs (a,b):
                if vars[a][1] == vars[b][1]:
                    if vars[i][0] == operators[0]: # A AND A = A
                        vars[i] = [vars[a][0], vars[a][1] != vars[i][1], vars[i][2], vars[a][3], vars[a][4]]
                        vars[a] = []
                        vars[b] = []
                    elif vars[i][0] == operators[1]: # A OR A = A
                        vars[i] = [vars[a][0], vars[a][1] != vars[i][1], vars[i][2], vars[a][3], vars[a][4]]
                        vars[a] = []
                        vars[b] = []
                    elif vars[i][0] == operators[2]: # A <=> A = True
                        vars[i] = [boo, vars[i][1], vars[i][2], -1, -1]
                        vars[a] = []
                        vars[b] = []
                else:
                    if vars[i][0] == operators[0]: # A AND !A = False
                        vars[i] = [boo, not(vars[i][1]), vars[i][2], -1, -1]
                        vars[a] = []
                        vars[b] = []
                    elif vars[i][0] == operators[1]: # A OR !A = True
                        vars[i] = [boo, vars[op][1], vars[i][2], -1, -1]
                        vars[a] = []
                        vars[b] = []
                    elif vars[i][0] == operators[2]: # A <=> !A = False
                        vars[op] = [boo, not(vars[op][1]), vars[i][2], -1, -1]
                        vars[a] = []
                        vars[b] = []
                            
            elif vars[a][0] == boo or vars[b][0] == boo:
                if vars[b][0] == boo:
                    a, b = b, a
                if vars[a][1]:
                    if vars[i][0] == operators[0]: # False AND B = False
                        vars[i] = [boo, not(vars[i][1]), vars[i][2], -1, -1]
                        vars[a] = []
                        vars[b] = []
                    elif vars[i][0] == operators[1]: # False OR B = B
                        vars[i] = [vars[b][0], vars[b][1] != vars[i][1], vars[i][2], vars[b][3], vars[b][4]]
                        vars[a] = []
                        vars[b] = []
                    elif vars[i][0] == operators[2]: # False <=> B = !B
                        vars[i] = [vars[b][0], vars[b][1] == vars[i][1], vars[i][2], vars[b][3], vars[b][4]]
                        vars[a] = []
                        vars[b] = []
                else:
                    if vars[i][0] == operators[0]: # True AND B = B
                        vars[i] = [vars[b][0], vars[b][1] != vars[i][1], vars[i][2], vars[b][3], vars[b][4]]
                        vars[a] = []
                        vars[b] = []
                    elif vars[i][0] == operators[1]: # True OR B = True
                        vars[i] = [boo, vars[i][1], vars[i][2], -1, -1]
                        vars[a] = []
                        vars[b] = []
                    elif vars[i][0] == operators[2]: # True <=> B = B
                        vars[i] = [vars[b][0], vars[b][1] != vars[i][1], vars[i][2], vars[b][3], vars[b][4]]
                        vars[a] = []
                        vars[b] = []
    
    sortV ()
    
    #2 floor simplifications
    op1 = []
    for i in range(otv,len(vars)):
        if vars[i][2] != -1:
            op1.append(vars[i][2])
    
    while not(0 in op1):
        op = []
        for i in op1:
            if vars[i][2] != -1:
                op.append(vars[i][2])
        op1 = op
                
        for i in op:
            a = vars[i]
            b = vars[a[3]]
            c = vars[a[4]]
            
            w1, w2, w3, w4 = -1, -1, -1, -1
            if equals (vars[b[3]], vars[c[3]]):
                w1, w2, w3, w4 = b[3], c[3], b[4], c[4]
            elif equals (vars[b[3]], vars[c[4]]):
                w1, w2, w3, w4 = b[3], c[4], b[4], c[3]
            elif equals (vars[b[4]], vars[c[3]]):
                w1, w2, w3, w4 = b[4], c[3], b[3], c[4]
            elif equals (vars[b[4]], vars[c[4]]):
                w1, w2, w3, w4 = b[4], c[4], b[3], c[3]
            
            # a&b | a&c -> a&(b|c)
            # a|b & a|c -> a|(b&c)
            if w1!=-1 and (b[0]==c[0] and b[1]==c[1]) and a[0] != operators[2]: # b[1] = False if b[1]==c[1] because of previous simplifications
                vars[i][0] = b[0]
                vars[w2] = []
                z1 = vars[i][3]
                z2 = vars[i][4]
                vars[i][3] = w1
                vars[i][4] = z1
                vars[z1] = [a[0], False, i, w3, w4]
                vars[z2] = []
                
            if a[0] == operators[1] and (equals(vars[w3], vars[w4])):
                #a&b | a!|b -> a<=>b
                if ((b[0]==operators[0] and not(b[1])) and (c[0]==operators[1] and c[1])) or ((c[0]==operators[0] and not(c[1])) and (b[0]==operators[1] and b[1])):
                    vars[i][0] = operators[2]
                    vars[a[3]] = []
                    vars[a[4]] = []
                    vars[i][3] = w1
                    vars[i][4] = w3
                
                elif ((b[0]==operators[0] and b[1]) and (c[0]==operators[1] and not(c[1]))) or ((c[0]==operators[0] and c[1]) and (b[0]==operators[1] and not(b[1]))):
                    delVar(a[3])
                    delVar(a[4])
                    vars[i][0] = boo
                    vars[i][3], vars[i][4] = -1, -1
