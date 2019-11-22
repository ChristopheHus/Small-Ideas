import random as r
import tkinter as tk
import time

L = [ [0 for i in range(200)] for j in range(200)]
nz = 2

for i in range(len(L)):
    L[i][0] = r.randint(128, 255)
    L[i][1] = r.randint(128, 255)

R = [254 for i in range(256)]
G = [0 for i in range(256)]
B = [0 for i in range(256)]

for i in range(128):
    R[i] = i*2
    G[i+128] = i*2



HEIGHT = 720
WIDTH = HEIGHT * 16 // 9

wid = WIDTH//2
hei = HEIGHT//2

fen = tk.Tk()
canvas = tk.Canvas(fen, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = tk.PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
quit = False

def onQuit (e=0):
    global quit, fen
    
    fen.destroy()
    quit = True
fen.bind('<Escape>', onQuit)

def update ():
    global L, nz
    n = len(L)-1
    
    for j in range(2,len(L[0])):
        L[0][j] = (2*L[0][j-1] + L[0][j-2] + L[1][j-1])//5
        L[n][j] = (2*L[n][j-1] + L[n][j-2] + L[n-1][j-1])//5
        
        zeros = (L[0][j] == 0) and (L[n][j]==0)
        
        for i in range(1, n):
            L[i][j] = (2*L[i][j-1] + L[i][j-2] + L[i-1][j-1] + L[i+1][j-1])//6
            zeros = zeros and (L[i][j]==0)
        
        if zeros:
            nz = j
            return


while not(quit):
    for j in range(2,nz):
        for i in range(len(L)):
            img.put( "#%02x%02x%02x" % (R[L[i][j]], G[L[i][j]], B[L[i][j]]), (i, len(L[0])-j+2) )
    
    update()
    
    for i in range(len(L)):
        L[i][0] = min( max(0,L[i][0]+r.randint(-16, 16)), 255)
        L[i][1] = min( max(0,L[i][1]+r.randint(-16, 16)), 255)
    
    fen.update()
    time.sleep(1/60)
