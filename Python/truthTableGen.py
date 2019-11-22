def f(a,b,c,d):
    if (a+b+c+d==4):
        return '1'
    elif (a+b+c+d==0):
        return '0'
    elif (a+b+c+d==1):
        if (a==1 or c==1):
            s='A&!B'
        else:
            s='A&B'
        if (a==1 or b==1):
            s='!'+s
        return s
    elif (a+b+c+d==3):
        if (b==0 or d==0):
            s='A|!B'
        else:
            s='A|B'
        if (c==0 or d==0):
            s='!'+s
        return s
    else:
        if (a==c and b==d):
            if (a==1):
                return '!B'
            else:
                return 'B'
        elif (a==b and c==d):
            if (a==1):
                return '!A'
            else:
                return 'A'
        elif (a==1):
            return 'A<=>B'
        else:
            return 'A!<=>B'
            