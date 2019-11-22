from tkinter import *
import random as rand
import time

quit = False
fen = Tk()
L = [i+1 for i in range(160)]
L2 = []

S = []

def onQuit (e=0):
    global quit, fen
    
    fen.destroy()
    quit = True
    
def shuffle ():
    l = len(L)
    
    for i in range(l-1, -1, -1):
        L2.append(L.pop(rand.randint(0,i)))
    
    for i in range(l):
        L.append(L2[i])
    

def tri_bulle ():
    for i in range(len(L), 1, -1):
        for j in range (1, i):
            if L[j-1] > L[j]:
                L[j-1], L[j] = L[j], L[j-1]
                S.append((j-1, j))
    

def tri_bulle2 ():
    i = len(L)
    j = 0
    
    while j < i:
        for k in range (i-1, j, -1):
            if L[k-1] > L[k]:
                L[k-1], L[k] = L[k], L[k-1]
                S.append((k-1, k))
        j += 1
        for k in range (k
        +1, i):
            if L[k-1] > L[k]:
                L[k-1], L[k] = L[k], L[k-1]
                S.append((k-1, k))
        i -= 1
            
                
def tri_fusion ():
    s = 1
    l = len(L)
    
    while s<l :
        p=0
        while p+s<l:
            i=0
            while i<s:
                j = p+s
                if L[j]<L[p+i]:
                    while j<min(p+2*s,l) and L[p+i]>L[j]:
                        j+=1
                    j-=1
                    
                    for k in range(0, s-i+1):
                        L[p+s-k], L[j-k] = L[j-k], L[p+s-k]
                        S.append((p+s-k,j-k))
                    
                    #Bubble entre p+i et j-s+i-1
                    
                    
                    
                    
                    
                    """L[p+i] = L[j]
                    S.append((p+i,j))
                    j += 1
                    while j<min(p+2*s,l) and temp>L[j]:
                        L[j-1] = L[j]
                        S.append((j-1,j))
                        j+=1
                    L[j-1] = temp"""
                i += 1
            p += 2*s
        s *= 2
        
        
def tri_rapide ():
    l = len(L)
    
    


fen.bind('<Escape>', onQuit)
fen.protocol('WM_DELETE_WINDOW', onQuit)


canv = Canvas (fen, width=800, height=600, background='black')
canv.pack()

shuffle()
tri_bulle2()

rects = []

for i in range(160):
    rects.append(canv.create_rectangle(i*5, 600, i*5+5, 600-3*L2[i], fill="red"))
    


while not(quit):
    if len(S)>0:
        a,b = S.pop(0)
        canv.move(rects[a], (b-a)*5, 0)
        canv.move(rects[b], (a-b)*5, 0)
        rects[a], rects[b] = rects[b], rects[a]
        
    
    
    
    fen.update()
    #tri()
    
    time.sleep(1/60)
    
