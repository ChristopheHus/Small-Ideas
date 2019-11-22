import tkinter as tk
import time
import random as r
import math as m


FPS = 30


fen = tk.Tk()

canvas = tk.Canvas(fen, width=800, height=600, background='black')
canvas.pack()


quit = False

def onQuit (e=0):
    global quit, fen
    
    fen.destroy()
    quit = True
    
    

Terrain = []
Walls = []
Lines = []


def genTerrain():
    global Terrain, Walls
    
    def getDx ():
        ra = r.random()
        return m.ceil(m.log2(1/ra))
    
    Terrain = [(0,0)]
    
    x = getDx()
    y = 0
    
    while x<80:
        
        yy = r.randint(0,59)
        
        if yy!=y:
            
            Terrain.append((x*10, y*10))
            
            y = yy
            
            Terrain.append((x*10,y*10))
            
            x += getDx()
    
    Terrain.append((800, y*10))
    
    for i in range(len(Terrain)-1):
        
        x1, y1 = Terrain[i]
        x2, y2 = Terrain[i+1]
        
        Walls.append(calculCoef(x1, y1, x2, y2))



def drawTerrain ():
    global Terrain, canvas
    
    #canvas.delete('all')
    
    for i in range(len(Terrain)-1):
        
        x1, y1 = Terrain[i]
        x2, y2 = Terrain[i+1]
        
        canvas.create_line(x1, y1, x2, y2, fill='white')
        

def testCross (a1, b1, c1, d1, a2, b2, c2, d2):
    
    if c2 == 0:
        
        if c1 == 0:
            
            if d1 != d2:
                
                return False
                
            if a2 == 0:
                
                if a1 == 0:
                    
                    return b1 == b2
                
                t = (b2 - b1) / a1
                
                return (0 < t and t < 1)
                            
                    
            k1 = (b1-b2) / a2
            k2 = k1 + a1 / a2
            
            return (0<=k1 and k1<=1) or (k1<=0 and k2>=0) or (k1>=1 and k2<=1)
        
        t1 = (d2 - d1) / c1
        
        if a2 == 0:
            
            return (a1*t1 + b1 - b2 == 0) and (0 <= t1 and t1 <= 1)
            
        t2 = (a1*t1 + b1 - b2) / a2
        
        return ( 0 <= t1 and t1 <= 1 ) and ( 0 <= t2 and t2 <= 1 )
    
    a = a2 / c2
    
    if a1 - a*c1 == 0:
        k1 = (d1-d2) / c2
        k2 = k1 + c1 / c2
        
        return (0<=k1 and k1<=1) or (k1<=0 and k2>=0) or (k1>=1 and k2<=1)
    
    
    t1 = (b2 - b1 + a*(d1-d2)) / (a1 - a*c1)
    
    t2 = (c1*t1 + d1 - d2) / c2
    
    return ( 0 <= t1 and t1 <= 1 ) and ( 0 <= t2 and t2 <= 1 )
    

def getProj (w1, w2):
    
    a1, b1, c1, d1 = w1
    a2, b2, c2, d2 = w2
    
    a = a1
    b = -a2
    c = c1
    d = -c2
    e = b2-b1
    f = d2-d1
    
    det = a*d - b*c
    
    if det != 0:
        
        t = (d*e - b*f) / det
        
        return (a1*t + b1, c1*t + d1)
    
    #calcul à refaire
    w = a*a + c*c
    
    if w==0:
        if e==0 and f==0:
            return (b1, d1)
        else:
            return (-1, -1)
    
    
    alpha = (a*b + c*d) / w
    beta = (a*e + f*c) / w
    
    if alpha == 0:
        return (b2, d2)
    
    
    if beta < 0:
        return (-1, -1)
    
    t = max (beta-alpha, 0)
    
    return (a1*t + b1, c1*t + d1)
    
    


def calculCoef (x1, y1, x2, y2):
    
    return (x2-x1, x1, y2-y1, y1)
    

def getXi (x):
    global Terrain
    
    n = len(Terrain)
    
    if n==0:
        return -1
    
    x1, _ = Terrain[0]
    x2, _ = Terrain[n-1]
    
    if x<x1:
        return -1
    elif x>x2:
        return n-1
    
    i1 = 0
    i2 = n-1
    
    while i2-i1>1:
        im = (i1+i2) // 2
        xm, _ = Terrain[im]
        
        if xm>x:
            i2 = im
        else:
            i1 = im
    
    return i1
    


def drawLines (x, y):
    global Terrain, Walls, Lines
    
    i1 = getXi(x)
    
    Left = []
    Right = []
    
    
    for i2, (i,j) in enumerate(Terrain):
        
        a1, b1, c1, d1 = calculCoef(x, y, i, j)
        
        cross = False
        
        if i<=x:
            
            for k in range(min(i1,len(Walls)-1),i2,-1): # i1 -> i2+1
                
                a2, b2, c2, d2 = Walls[k]
                
                if testCross (a1, b1, c1, d1, a2, b2, c2, d2):
                    cross = True
                    break
            
            if not(cross):
                Left.append(i2)
        
        else:
            
            for k in range(max(i1,0),i2-1): # i1 -> i2-2
                
                a2, b2, c2, d2 = Walls[k]
                
                if testCross (a1, b1, c1, d1, a2, b2, c2, d2):
                    cross = True
                    break
            
            if not(cross):
                Right.append(i2)
    
    
    if i1>=0 and i1<=len(Terrain)-2:
        x1, y1 = Terrain[i1]
        x2, y2 = Terrain[i1+1]
        Lines.append(canvas.create_polygon(x,y, x1,y1, x2,y2 ,fill='purple'))
    
    
    n = len(Left)-2
    
    if n>=0:
        next = Left[n+1]
        prec = Left[n]
        
        while True:
            
            if next-prec > 1:
                xx, yy = Terrain[next]
                
                x1, y1 = getProj(calculCoef(x,y, xx,yy), Walls[prec])
                
                x2, y2 = Terrain[prec]
                Lines.append(canvas.create_polygon(x,y, x1,y1, x2,y2 ,fill='purple'))
                
            else:
                x1, y1 = Terrain[prec]
                x2, y2 = Terrain[next]
                Lines.append(canvas.create_polygon(x,y, x1,y1, x2,y2 ,fill='purple'))
            
            if n==0:
                break
            
            n -= 1
            next = prec
            prec = Left[n]
    
    
    N = len(Right)-1
    n = 1
    
    if N>=n:
        prec = Right[n-1]
        next = Right[n]
        
        while True:
            if next-prec > 1:
                xx, yy = Terrain[prec]
                
                x1, y1 = getProj(calculCoef(x,y, xx,yy), Walls[next-1])
                
                x2, y2 = Terrain[next]
                Lines.append(canvas.create_polygon(x,y, x1,y1, x2,y2 ,fill='purple'))
                
            else:
                x1, y1 = Terrain[prec]
                x2, y2 = Terrain[next]
                Lines.append(canvas.create_polygon(x,y, x1,y1, x2,y2 ,fill='purple'))
            
            if n==N:
                break
            
            n += 1
            prec = next
            next = Right[n]


def update():
    global fen, canvas, Lines
    
    x = fen.winfo_pointerx() - fen.winfo_rootx()
    y = fen.winfo_pointery() - fen.winfo_rooty()
    
    #for i in Lines:
    #   canvas.delete(i)
    canvas.delete('all')
    Lines = []
    
    drawLines(x,y)
    drawTerrain()
    
    
    


fen.bind('<Escape>', onQuit)
fen.protocol('WM_DELETE_WINDOW', onQuit)


genTerrain()
drawLines(400,500)
drawTerrain()


while not(quit):

    update()
    fen.update()
    
    time.sleep(1/FPS)