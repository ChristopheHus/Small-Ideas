import matplotlib.pyplot as pl


def mapto (x, x1, x2, y1, y2):
    return (y2-y1)*(x-x1)/(x2-x1) + y1

def inv (x):
    return 1-x

def slowSta (x, N):
    return x**N

def slowSto (x, N):
    return inv(slowSta(inv(x), N))

def swap (x, f, g):
    return inv(x)*f(x) + x*g(x)


def disp(f):
    X = [i/1000 for i in range(1001)]
    Y = [f(X[i]) for i in range(1001)]
    
    pl.plot(X,Y)
    pl.show()


inter = lambda n : lambda x : swap (x, lambda x: slowSta(x,n), lambda x: slowSto(x,n))
gauss = lambda n : lambda x: 4**n * slowSta(x,n)*slowSta(inv(x),n)

flatm = lambda n : lambda x : swap (x, lambda x: slowSto(x,n), lambda x: slowSta(x,n)) # n<4
flatu = lambda n : lambda x : swap (x, lambda x: slowSta(x,n), lambda x: slowSta(inv(x),n)) # n<4
round = lambda n : lambda x : swap (x, lambda x: slowSto(x,n), lambda x: inv(slowSta(x,n)))