import tkinter as tk



f = tk.Tk()

canvas = tk.Canvas(f, width=800, height=600, background="#000000")
canvas.pack()


A = [400, 70]
B = [200, 400]
C = [700, 500]



canvas.create_line(A[0], A[1], B[0], B[1], fill="#FFFFFF")
canvas.create_line(A[0], A[1], C[0], C[1], fill="#FFFFFF")
canvas.create_line(B[0], B[1], C[0], C[1], fill="#FFFFFF")

#canvas.create_line((A[0]+B[0])/2+(A[1]-B[1])/2, (A[1]+B[1])/2+(B[0]-A[0])/2, (A[0]+B[0])/2-(A[1]-B[1])/2, (A[1]+B[1])/2-(B[0]-A[0])/2, fill="#FF0077")
#canvas.create_line((A[0]+C[0])/2+(A[1]-C[1])/2, (A[1]+C[1])/2+(C[0]-A[0])/2, (A[0]+C[0])/2-(A[1]-C[1])/2, (A[1]+C[1])/2-(C[0]-A[0])/2, fill="#FF0077")

M = [[C[1]-A[1], A[1]-B[1]], [A[0]-C[0], B[0]-A[0]]]

d = M[0][0]*M[1][1] - M[1][0]*M[0][1]

Mi = [[M[0][0]/d, -M[0][1]/d], [-M[1][0]/d, M[0][0]/d]]

tp = Mi[0][0]*(C[0]-B[0])/2 + Mi[0][1]*(C[1]-B[1])/2
t = Mi[1][0]*(C[0]-B[0])/2 + Mi[1][1]*(C[1]-B[1])/2


x = (A[0]+B[0])/2+(A[1]-B[1])*t
y = (A[1]+B[1])/2+(B[0]-A[0])*t


canvas.create_line((A[0]+B[0])/2, (A[1]+B[1])/2, x, y, fill="#FF00CC")
canvas.create_line((A[0]+C[0])/2, (A[1]+C[1])/2, x, y, fill="#FF00CC")
canvas.create_line((C[0]+B[0])/2, (C[1]+B[1])/2, x, y, fill="#FF00CC")


canvas.create_oval(x-5, y-5, x+5, y+5, fill="#00FFFF")

tk.mainloop()