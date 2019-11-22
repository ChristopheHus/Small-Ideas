import tkinter as tk
import random as rd
import math as mt


def f (x):
    
    if x<0:        
        return  1 / (2*(x-1)**2)
    
    else:
        return 1 - 1 / (2*(x+1)**2)



def scalprod (x, y):
    
    return x[0] * y[0] + x[1] * y[1]



N = 80
M = 50
size = 20

grads = [[[0,0,0] for j in range(M)] for i in range(N)]
poten = [[0. for j in range(M)] for i in range(N)]


def genGrads ():
    
    for i in range(N):
        for j in range(M):
            theta = rd.random() * mt.pi * 2
            
            grads[i][j][0] = mt.cos(theta)
            grads[i][j][1] = mt.sin(theta)
            grads[i][j][2] = rd.random()
    


def mngGrad (x,y):
    
    for i in range(N):
        for j in range(M):
            
            alpha = scalprod(grads[x][y], [(i-x), (j-y)])
            if (alpha>0):
                poten[i][j] += grads[x][y][2]
            elif (alpha<0):
                poten[i][j] -= grads[x][y][2]
            #poten[i][j] += grads[x][y][2] * f(scalprod(grads[x][y], [(i-x), (j-y)]))


def manage ():
    
    for i in range(1,N-1):
        for j in range(1,M-1):
            #mngGrad(i,j)
            
            poten[i-1][j-1] += grads[i][j][2] * scalprod(grads[i][j], [-1, -1])
            poten[i  ][j-1] += grads[i][j][2] * scalprod(grads[i][j], [0, -1])
            poten[i+1][j-1] += grads[i][j][2] * scalprod(grads[i][j], [1, -1])
            poten[i-1][j  ] += grads[i][j][2] * scalprod(grads[i][j], [-1, 0])
            #poten[i  ][j  ] += 
            poten[i+1][j  ] += grads[i][j][2] * scalprod(grads[i][j], [1, 0])
            poten[i-1][j+1] += grads[i][j][2] * scalprod(grads[i][j], [-1, 1])
            poten[i  ][j+1] += grads[i][j][2] * scalprod(grads[i][j], [0, 1])
            poten[i+1][j+1] += grads[i][j][2] * scalprod(grads[i][j], [1, 1])
            
            
            
            
            #poten[i][j] = (1-mt.cos(2*mt.pi*i/N))*(1-mt.cos(2*mt.pi*j/M))/4


def calcV (x0,y0,x1,y1,x2,y2,x3,y3, v0):
    V = [v0, v0, v0, v0]
    
    V[1] += (9*x0 - 5*y0 + 9*x1 + 5*y1 + 3*x2 - y2 + 3*x3 + y3) / 24
    V[2] += (5*x0 - 9*y0 + x1 - 3*y1 - 5*x2 - 9*y2 - x3 - 3*y3) / 24
    V[3] += (8*x0 - 2*y0 + x1 - 7*y1 + x2 + 5*y2 - 4*x3 - 2*y3) / 6
    
    return V



def normalise ():
    
    mi = poten[0][0]
    ma = poten[0][0]
    
    for i in range(N):
        for j in range(M):
            
            if poten[i][j]<mi:
                mi = poten[i][j]
                
            elif poten[i][j]>ma:
                ma = poten[i][j]
    
    
    for i in range(N):
        for j in range(M):
            poten[i][j] = (poten[i][j] - mi) / (ma-mi)



genGrads()
manage()
normalise()

master = tk.Tk()


w = tk.Canvas(master, width=size*N, height=size*M)
w.pack()


for i in range(N):
    for j in range(M):
        colorval = "#%02x%02x%02x" % (int(poten[i][j]*255), int(poten[i][j]*255), int(poten[i][j]*255))
        w.create_rectangle(i*size, j*size, i*size+size, j*size+size, fill=colorval, outline="")

"""
for i in range(N):
    for j in range(M):
        w.create_line(i*size+size//2, j*size+size//2, i*size+size//2+size//2*grads[i][j][0]*grads[i][j][2], j*size+size//2+size//2*grads[i][j][1]*grads[i][j][2], fill="red")
"""

tk.mainloop()