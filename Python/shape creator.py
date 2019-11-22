import tkinter as tk
import random as rd


N = 80
M = 50

L = [   [   rd.randint(0,5)
        for j in range(M+1) ]
    for i in range(N+1) ]


size = 20
master = tk.Tk()
w = tk.Canvas(master, width=size*N, height=size*M, background="#000000")
w.pack()


colorval = "#%02x%02x%02x" % (255, 255, 255)
for i in range(N):
    for j in range(M):
        a = L[i][j]
        b = L[i+1][j]
        c = L[i][j+1]
        d = L[i+1][j+1]
        
        if (a==d and b==c):
            if (a!=b):
                w.create_line((i+.5)*size, j*size, (i+.5)*size, (j+1)*size, width=1, fill=colorval)
                w.create_line(i*size, (j+.5)*size, (i+1)*size, (j+.5)*size, width=1, fill=colorval)
            continue
        
        elif (a==d):
            if (a!=b):
                w.create_line((i+.5)*size, j*size, (i+1)*size, (j+.5)*size, width=1, fill=colorval)
            if (a!=c):
                w.create_line(i*size, (j+.5)*size, (i+.5)*size, (j+1)*size, width=1, fill=colorval)
            continue
        
        elif (b==c):
            if (b!=a):
                w.create_line(i*size, (j+.5)*size, (i+.5)*size, j*size, width=1, fill=colorval)
            if (b!=d):
                w.create_line((i+.5)*size, (j+1)*size, (i+1)*size, (j+.5)*size, width=1, fill=colorval)
            continue
        
        else:
            if a!=b:
                w.create_line((i+.5)*size, j*size, (i+.5)*size, (j+.5)*size, width=1, fill=colorval)
            if b!=d:
                w.create_line((i+1)*size, (j+.5)*size, (i+.5)*size, (j+.5)*size, width=1, fill=colorval)
            if d!=c:
                w.create_line((i+.5)*size, (j+1)*size, (i+.5)*size, (j+.5)*size, width=1, fill=colorval)
            if a!=c:
                w.create_line(i*size, (j+.5)*size, (i+.5)*size, (j+.5)*size, width=1, fill=colorval)
            continue
        
        
        #colorval = "#%02x%02x%02x" % (int(poten[i][j]*255), int(poten[i][j]*255), int(poten[i][j]*255))
        #w.create_line(i*size, j*size, i*size+size, j*size+size, width=1, fill=colorval)


tk.mainloop()