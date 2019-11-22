import math as m
import matplotlib.pyplot as pl
import numpy as np


fx = lambda t : m.cos(t)
fy = lambda t : m.sin(t)
dfx = lambda t : -m.sin(t)
dfy = lambda t : m.cos(t)

f = lambda L : [fx(L[0]), fy(L[1])]
df = lambda L,dt : [-L[1]*dt, L[0]*dt]


def sum2(L1,L2):
    return [L1[0]+L2[0],L1[1]+L2[1]]

def euler(T, x0, df):
    
    X = [0 for i in range(len(T))]    
    Y = [0 for i in range(len(T))]
    
    X[0] = x0[0]
    Y[0] = x0[1]
    
    for i in range(len(T)-1):
        dt = T[i+1] - T[i]
        
        dP = df([X[i],Y[i]],dt)
        X[i+1] = X[i]+dP[0]
        Y[i+1] = Y[i]+dP[1]
    
    return X,Y


def rungekutta(T,x0,df):
    
    X = [0 for i in range(len(T))]    
    Y = [0 for i in range(len(T))]
    
    X[0] = x0[0]
    Y[0] = x0[1]
    
    for i in range(len(T)-1):
        dt = T[i+1] - T[i]
        
        k1 = 1
        k2 = 1
        k3 = 1
        k4 = 1
        
        dP = df([X[i],Y[i]],dt)
        X[i+1] = X[i]+dP[0]
        Y[i+1] = Y[i]+dP[1]
    
    return X,Y


T = [i/100 for i in range(10001)]

x0 = [1,0]

X,Y = euler(T,x0,df)

pl.plot(X,Y)
pl.plot([fx(i/100) for i in range(1001)],[fy(i/100) for i in range(1001)])

pl.show()