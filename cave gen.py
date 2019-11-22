import tkinter as tk
import random as rd
import time


N = 80
M = 50

perc = 60
L = [   [   1 if not(i==0 or j==0 or i==N or j==M) and (rd.randint(0,100)>perc) else 0
        for j in range(M+1) ]
    for i in range(N+1) ]


size = 20
master = tk.Tk()
w = tk.Canvas(master, width=size*N, height=size*M, background="#000000")
w.pack()

L2 = [[0 for j in range(M+1)] for i in range(N+1)]

l = 1
k1 = 4
k2 = 4

for n in range(0,5):
    for i in range(l,N-l+1):
        for j in range(l,M-l+1):
            L2[i][j] = 0
            for ii in range(-l,l+1):
                for jj in range(-l,l+1):
                    L2[i][j] += L[i+ii][j+jj]
                
    for i in range(1,N):
        for j in range(1,M):
            L[i][j] = 1 if L2[i][j]>k2 else (0 if L2[i][j]<k1 else L[i][j])

def draw ():
    w.delete('all')
    bl = "#FFFFFF"
    for i in range(N):
        for j in range(M):
            n = L[i][j]*8 + L[i+1][j]*4 + L[i][j+1]*2 + L[i+1][j+1]
            
            if n==0:
                continue
            elif n==1:
                w.create_polygon((i+.5)*size, (j+1)*size, (i+1)*size, (j+1)*size, (i+1)*size, (j+.5)*size, width=0,fill=bl)
            elif n==2:
                w.create_polygon(i*size, (j+.5)*size, (i+.5)*size, (j+1)*size, i*size, (j+1)*size, width=0,fill=bl)
            elif n==3:
                w.create_polygon(i*size, (j+.5)*size, (i+1)*size, (j+.5)*size, (i+1)*size, (j+1)*size, i*size, (j+1)*size, width=0,fill=bl)
            elif n==4:
                w.create_polygon((i+.5)*size, j*size, (i+1)*size, j*size, (i+1)*size, (j+.5)*size, width=0,fill=bl)
            elif n==5:
                w.create_polygon((i+.5)*size, j*size, (i+1)*size, j*size, (i+1)*size, (j+1)*size, (i+.5)*size, (j+1)*size, width=0,fill=bl)
            elif n==6:
                w.create_polygon(i*size, (j+.5)*size, (i+.5)*size, (j+1)*size, i*size, (j+1)*size, width=0,fill=bl)#(i+.5)*size, (j+.5)*size,  : 2
                w.create_polygon((i+.5)*size, j*size, (i+1)*size, j*size, (i+1)*size, (j+.5)*size, width=0,fill=bl)#(i+.5)*size, (j+.5)*size,  : 4
            elif n==7:
                w.create_polygon((i+.5)*size, j*size, (i+1)*size, j*size, (i+1)*size, (j+1)*size, i*size, (j+1)*size, i*size, (j+.5)*size, width=0,fill=bl)
            elif n==8:
                w.create_polygon(i*size, j*size, (i+.5)*size, j*size, i*size, (j+.5)*size, width=0,fill=bl)
            elif n==9:
                w.create_polygon(i*size, j*size, (i+.5)*size, j*size, i*size, (j+.5)*size, width=0,fill=bl)#(i+.5)*size, (j+.5)*size,  : 3
                w.create_polygon((i+1)*size, (j+.5)*size, (i+1)*size, (j+1)*size, (i+.5)*size, (j+1)*size, width=0,fill=bl) #(i+.5)*size, (j+.5)*size, : 1
            elif n==10:
                w.create_polygon(i*size, j*size, (i+.5)*size, j*size, (i+.5)*size, (j+1)*size, i*size, (j+1)*size, width=0,fill=bl)
            elif n==11:
                w.create_polygon(i*size, j*size, (i+.5)*size, j*size, (i+1)*size, (j+.5)*size, (i+1)*size, (j+1)*size, i*size, (j+1)*size, width=0,fill=bl)
            elif n==12:
                w.create_polygon(i*size, j*size, (i+1)*size, j*size, (i+1)*size, (j+.5)*size, i*size, (j+.5)*size, width=0,fill=bl)
            elif n==13:
                w.create_polygon(i*size, j*size, (i+1)*size, j*size, (i+1)*size, (j+1)*size, (i+.5)*size, (j+1)*size, i*size, (j+.5)*size, width=0,fill=bl)
            elif n==14:
                w.create_polygon(i*size, j*size, (i+1)*size, j*size, (i+1)*size, (j+.5)*size, (i+.5)*size, (j+1)*size, i*size, (j+1)*size, width=0,fill=bl)
            elif n==15:
                w.create_polygon(i*size, j*size, (i+1)*size, j*size, (i+1)*size, (j+1)*size, i*size, (j+1)*size, width=0,fill=bl)

isB1Down = False

def manage():
    X = mouse_x // size
    Y = mouse_y // size
    L[X][Y] = 1 - L[X][Y]

def press1 (event):
    global mouse_x, mouse_y
    mouse_x = event.x
    mouse_y = event.y
    global isB1Down
    isB1Down = True
def release1 (event):
    global mouse_x, mouse_y
    mouse_x = event.x
    mouse_y = event.y
    global isB1Down
    isB1Down = False

#mouseclick event
w.bind('<ButtonPress-1>', press1)
w.bind('<ButtonRelease-1>', release1)

#tk.mainloop()

while 1:
    master.update_idletasks()
    master.update()
    draw()
    if (isB1Down):
        manage()
    time.sleep(0.03)