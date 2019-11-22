

def calc_sqrt (x, p):
    
    y = x
    dy = (x-y*y) / 2
    
    while abs(dy) > p:
        y = y + dy / y
        dy = (x-y*y) / 2
    
    return y + dy / y