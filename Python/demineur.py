import random as rd
import tkinter as tk
import time

class mouseSim:
    def __init__(s,x,y):
        s.x = x
        s.y = y

N = 30
M = 20
B = 70

s = 20

L = [[0 for j in range(M)] for i in range(N)]
L2 = [[-2 for j in range(M)] for i in range(N)]
P = [[1. for j in range(M)] for i in range(N)]
gameover = False

master = tk.Tk()
w = tk.Canvas(master, width=s*N, height=s*M, background="#000000")
w.pack()


def genMap ():
    global L
    
    for i in range(B):
        x = rd.randint(0,N-1)
        y = rd.randint(0,M-1)
        
        while L[x][y]==-1:
            x = rd.randint(0,N-1)
            y = rd.randint(0,M-1)
        
        L[x][y] = -1
    
    for i in range(N):
        for j in range(M):
            if L[i][j]==-1:
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        if (k>=0 and k<N) and (l>=0 and l<M) and L[k][l]!=-1:
                            L[k][l] += 1

def draw ():
    global L2
    
    w.delete('all')
    bl = "#CCCCCC"
    for i in range(N):
        for j in range(M):
            if L2[i][j]==-2:
                w.create_rectangle(i*s,j*s,(i+1)*s-1,(j+1)*s-1,fill="#888888")
            else:
                w.create_rectangle(i*s,j*s,(i+1)*s-1,(j+1)*s-1,fill=bl)
                
                if L2[i][j]==1:
                    w.create_text((2*i+1)*s//2, (2*j+1)*s//2, text="1", fill="#884400")
                elif L2[i][j]==2:
                    w.create_text((2*i+1)*s//2, (2*j+1)*s//2, text="2", fill="#888844")
                elif L2[i][j]==3:
                    w.create_text((2*i+1)*s//2, (2*j+1)*s//2, text="3", fill="#888800")
                elif L2[i][j]==4:
                    w.create_text((2*i+1)*s//2, (2*j+1)*s//2, text="4", fill="#448800")
                elif L2[i][j]==5:
                    w.create_text((2*i+1)*s//2, (2*j+1)*s//2, text="5", fill="#008800")
                elif L2[i][j]==6:
                    w.create_text((2*i+1)*s//2, (2*j+1)*s//2, text="6", fill="#008844")
                elif L2[i][j]==7:
                    w.create_text((2*i+1)*s//2, (2*j+1)*s//2, text="7", fill="#008888")
                elif L2[i][j]==8:
                    w.create_text((2*i+1)*s//2, (2*j+1)*s//2, text="8", fill="#448888")
                elif L2[i][j]==-1:
                    w.create_text((2*i+1)*s//2, (2*j+1)*s//2, text="*", fill="#000000")

def manage (e):
    global L, L2, gameover
    
    def unlock (i,j,n):        
        L2[i][j] = L[i][j]
        end = True
        
        if L[i][j]==-1:
            return False
        
        if L[i][j]==0:
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if (k>=0 and k<N) and (l>=0 and l<M) and L2[k][l]==-2:
                        end = end and unlock(k,l,n+1)
        else:
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if (k>=0 and k<N) and (l>=0 and l<M) and L2[k][l]==-2:
                        if L[k][l]==0 and n==0:
                            end = end and unlock(k,l,n+1)
        return end
    
    i = e.x//s
    j = e.y//s
    
    gameover = gameover or not(unlock(i,j,0))
    
    #if gameover:
    #    L2 = L


def calcNewTurn (e):
    # P = chiffre / cases libres
    # P combiné = Prod Pi
    
    for i in range(N):
        for j in range(M):
            P[i][j] = 1
    
    for i in range(N):
        for j in range(M):
            if L2[i][j]>=0:
                cl = 0
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        if (k>=0 and k<N) and (l>=0 and l<M) and L2[k][l]==-2:
                            cl += 1
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        if (k>=0 and k<N) and (l>=0 and l<M) and L2[k][l]==-2:
                            P[k][l] *= L2[i][j] / cl
                            
    
    
w.bind('<Button-1>', manage)

genMap()

while 1:
    master.update_idletasks()
    master.update()
    draw()
    time.sleep(0.03)