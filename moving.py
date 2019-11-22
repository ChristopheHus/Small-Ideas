import tkinter as tk
import time

fen = tk.Tk()

HEIGHT = 720
WIDTH = HEIGHT * 16 // 9

canvas = tk.Canvas(fen, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()

HEIGHT = HEIGHT - 10
WIDTH = WIDTH - 10
wid = WIDTH//2
hei = HEIGHT//2

sph = canvas.create_oval(0, 0, 20, 20, width=0, fill="#FFFF00")
x = 0
y = 0
vx = 0.
vy = 0.


quit = False
def onQuit (e=0):
    global quit, fen
    
    fen.destroy()
    quit = True
fen.bind('<Escape>', onQuit)


while not(quit):
    fen.update()
    time.sleep(1/30)
    
    if x<= wid:
        vx += 0.0000000005 * (wid-x)**3
    else:
        vx -= 0.0000000005 * (x-wid-1)**3
    
    if y<= hei:
        vy += 0.000000001 * (hei-y)**3
    else:
        vy -= 0.000000001 * (y-hei-1)**3
    
    x += int(vx)
    y += int(vy)
    
    canvas.move(sph, int(vx), int(vy))