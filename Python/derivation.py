import matplotlib.pyplot as p


def deriv (Y, dx):
    
    if len(Y)==0:
        return []
    elif len(Y)==1:
        return [0]
    
    
    dY = [0 for y in Y]
    
    dY[0] = (Y[1] - Y[0]) / dx
    
    dY[-1] = (Y[-1] - Y[-2]) / dx
    
    
    for i in range(1, len(Y)-1):
        
        dY [i] = (Y[i+1] - Y[i-1]) / (2 * dx)
    
    
    return dY



def integr (Y, y0, dx):
    
    if len(Y)==0:
        return []
    elif len(Y)==1:
        return [y0]
    
    
    inte = [0 for i in Y]
    
    
    inte[0] = y0
    
    for i in range(1, len(Y)):
        
        inte[i] = (Y[i] + Y[i-1]) * dx / 2 + inte[i-1]
    
    
    return inte
    
    

dx = 1/100
X = [i*dx for  i in range(1000)]

Y = [x**2 for x in X]


p.plot(X,Y, color='b')

p.plot(X, integr(deriv(Y,dx),Y[0], dx), color='r')

p.show()

