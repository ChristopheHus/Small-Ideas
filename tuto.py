def deplacement(a,k):
    while k>0:
        if a[k] < a[k-1]:
            a[k], a[k-1] = a[k-1], a[k]
        k = k-1

def tri_insertion(a):
    n = len(a)
    for k in range(1,n):
        deplacement(a,k)

import random as r
liste = []
for k in range(1000):
    liste.append(r.randint(0,1000))
    
tri_insertion(liste)

for k in range(999):
    if liste[k+1]<liste[k]:
        print("Error")
        print(k)
    
print("Terminated")