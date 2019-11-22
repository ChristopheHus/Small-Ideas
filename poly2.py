class Poly2:
    
    def __init__ (s, l=[[]]):
        if (l==[[]]):
            s.mat = [[0 for j in range(10)] for i in range(10)]
        else:
            s.mat = l
    
    def __add__(s,o):
        return Poly2([[s.mat[i][j]+o.mat[i][j] for j in range(10)] for i in range(10)])
    
    def __mul__(s,o):
        mat = [[0 for j in range(10)] for i in range(10)]
        
        for i in range(10):
            for j in range(10):
                
                for k in range(10-i):
                    for l in range(10-j):
                        
                        mat[i+k][l+j] += s.mat[i][j] * o.mat [k][l]
        
        return Poly2(mat)
    
    def __str__(s):
        st = ""
        
        for j in range(10):
            for i in range(10):
                st += str(s.mat[i][j]) + " "
            st += "\n"
        
        return st


a = Poly2()
a.mat[0][0] = 1
a.mat[1][0] = 1
a.mat[0][1] = 1
a.mat[1][1] = 1
b = a*a
print(b)