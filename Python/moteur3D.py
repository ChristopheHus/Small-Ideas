class Vector:
    
    def __init__(s, L):
        s.v = [ L[i] for i in range(4) ]
    
    def __add__(s, o):
        return Vector ( [ s.v[i]+o.v[i] for i in range(4) ] )
        
    def __sub__(s, o):
        return Vector ( [ s.v[i]-o.v[i] for i in range(4) ] )
    
    def __mul__(s, o):
        if type(o)==int or type(o)==float:
            return Vector ( [ o*s.v[i] for i in range(4) ] )
        
        return Vector ( [s.v[1]*o.v[2]-s.v[2]*o.v[1], s.v[2]*o.v[0]-s.v[0]*o.v[2], s.v[0]*o.v[1]-s.v[1]*o.v[0], max(s.v[3],o.v[3])] )
    
    def __truediv__(s, o):
        if type(o)==int or type(o)==float:
            return Vector ( [ s.v[i]/o for i in range(4) ] )
        
        return sum ( [ s.v[i]*o.v[i] for i in range(4) ] )
        
    def __str__(s):
        st = ""
        
        for i in range(4):
            st+= str(s.v[i]) + ", "
        return st[:-2]
    

class Matrix:
    
    def __init__(s, L):
        s.v = [ [L[i][j] for j in range(4)] for i in range(4)]
    
    def __add__(s, o):
        return Matrix ( [ [ s.v[i][j]+o.v[i][j] for j in range(4)] for i in range(4)] )
        
    def __sub__(s, o):
        return Matrix ( [ [ s.v[i][j]-o.v[i][j] for j in range(4)] for i in range(4)] )
    
    def __mul__(s, o):
        if type(o)==int or type(o)==float:
            return Matrix ( [ [ o*s.v[i][j] for j in range(4)] for i in range(4) ] )
           
        
        if type(o)==Vector:
            return Vector ( [ sum([s.v[j][i]*o.v[i] for i in range(4)]) for j in range(4) ] )
             
        if type(o)!=Matrix:
            return NotImplemented
        
        def val(i, j):
            c=0
            for k in range(4):
                c+= s.v[i][k]*o.v[k][j]
            return c
                
        return Matrix ( [ [ val(i,j) for j in range(4)] for i in range(4) ] )
        
    def __mod__(s, k):
        if type(k)!=int and type(k)!=float:
            return NotImplemented
        
        def modulo (i, k):
            if k<0:
                return -modulo (-i, -k)
            
            while i<0:
                i += k
            while i>=k:
                i -= k
            return i
        
        A = Matrix (s.v)
        
        for i in range(4):
            for j in range(4):
                A.v[i][j] = modulo (A.v[i][j], k)
                
        return A
        
    def __str__(s):
        st = ""
        
        for i in range(4):
            for j in range(4):
                st+= str(s.v[i][j]) + ", "
            st = st[:-2] + "\n"
        return st[:-1]



import tkinter as tk
import math as m
import time

HEIGHT = 720
WIDTH = HEIGHT * 16 // 9

wid = WIDTH//2
hei = HEIGHT//2

fen = tk.Tk()
canvas = tk.Canvas(fen, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = tk.PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

zbuf = [[0 for j in range(HEIGHT)] for i in range(WIDTH)]

space = []
lines = []

f = 200
n = 5
tana = 2.7

Mproj = Matrix([[hei/tana,0,wid,0],[0,hei/tana,hei,0],[0,0,1/(f-n),-n/(f-n)],[0,0,1,0]])
cam = [0, 0, -80, 0, 0]

quit = False

def onQuit (e=0):
    global quit, fen
    
    fen.destroy()
    quit = True
    
def projection ():
    global cam, space, Mproj
    M = Mproj \
        * Matrix([[m.cos(cam[4]),0,m.sin(cam[4]),0],[0,1,0,0],[-m.sin(cam[4]),0,m.cos(cam[4]),0],[0,0,0,1]]) \
        * Matrix([[m.cos(cam[3]),m.sin(cam[3]),0,0],[-m.sin(cam[3]),m.cos(cam[3]),0,0],[0,0,1,0],[0,0,0,1]]) \
        * Matrix([[1,0,0,-cam[0]],[0,1,0,-cam[1]],[0,0,1,-cam[2]],[0,0,0,1]])
    
    for i in range(len(space)):
        space[i].p = M*space[i]
    for i in range(len(space)):
        if space[i].p.v[3] != 0:
            space[i].p.v[0] /= space[i].p.v[3]
            space[i].p.v[1] /= space[i].p.v[3]
        else:
            space[i].p.v[0] = wid
            space[i].p.v[1] = hei
            space[i].p.v[3] = -n
        
    

def drawLine (a):
    global lines, space, img, zbuf
    
    L = []
    
    X = space[lines[a][0]].p.v
    Y = space[lines[a][1]].p.v
    
    dx = X[0] - Y[0]
    dy = X[1] - Y[1]
    dz = X[2] - Y[2]
    
    if dx==0 and dy==0:
        img.put( "#ffff00", (int(X[0]),int(Y[0])) )
        return
    
    w = max( abs(dx), abs(dy) )
    
    dx = dx / w
    dy = dy / w
    dz = dz / w
    
    for t in range(int(w)+1):
        x = round(Y[0] + t*dx)
        y = round(Y[1] + t*dy)
        z = Y[2] + t*dz
        
        if x>=0 and x<WIDTH and y>=0 and y<HEIGHT and z>=0 and z<1:# and z<zbuf[x][y]:
            img.put( "#%02x%02x%02x" % (255, 255, 255), (x, y) )
            #zbuf[x][y] = z
        # 0 -> orange
        # -64 -> jaune
        # 63 -> rouge
    
    return L

def genCube (M):
    global lines, space
    
    n = len(space)
    
    for i in range(3):
        lines.append([n+i, n+i+1])
    lines.append([n+3, n])
    
    for i in range(4):
        lines.append([n+i, n+i+4])
    
    for i in range(3):
        lines.append([n+i+4, n+i+5])
    lines.append([n+7, n+4])
    
    space.append(M*Vector([-1,-1,-1,1]))
    space.append(M*Vector([1,-1,-1,1]))
    space.append(M*Vector([1,1,-1,1]))
    space.append(M*Vector([-1,1,-1,1]))
    space.append(M*Vector([-1,-1,1,1]))
    space.append(M*Vector([1,-1,1,1]))
    space.append(M*Vector([1,1,1,1]))
    space.append(M*Vector([-1,1,1,1]))
    
def render ():
    global lines, zbuf
    
    for i in range(WIDTH):
        for j in range(HEIGHT):
            zbuf[i][j] = 1
            
    img.blank()
    projection()
    
    for i in range(len(lines)):
        drawLine(i)

M = Matrix([[50,0,0,0],[0,50,0,0],[0,0,50,0],[0,0,0,1]])

def lKey (e=0):
    cam[4] -= .05
    render()
    return
def rKey (e=0):
    cam[4] += .05
    render()
    return
def uKey (e=0):
    cam[2] += 5
    render()
    return
def dKey (e=0):
    cam[2] -= 5
    render()
    return

def resetKey (e=0):
    global cam

    cam = [0, 0, 0, 0, 0]

def turnKey (e):
    return

genCube(M)        
render()

    
fen.bind('<Escape>', onQuit)
fen.bind('<Up>', uKey)
fen.bind('<Down>', dKey)
fen.bind('<Left>', lKey)
fen.bind('<Right>', rKey)
fen.bind('r', resetKey)
fen.bind('e', turnKey)

fen.protocol('WM_DELETE_WINDOW', onQuit)


while not(quit):
    
    fen.update()
    
    time.sleep(1/60)