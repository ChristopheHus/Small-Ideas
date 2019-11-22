import matplotlib.pyplot as pl
import random as r
import math as m


def interpolation1 (y0, y1, y2, y3):
    
    d = -.5*y0 + 1.5*y1 - 1.5*y2 + .5*y3
    c = y0 - 2.5*y1 + 2*y2 - .5*y3
    b = (y2 - y0)/2
    a = y1
    
    return lambda x : d*x*x*x + c*x*x + b*x + a


def inter2 (y0, y1, y2, y3, y4, y5):
    
    a = y2
    b = .5*y3 - .5*y1
    c = .25*y0 - .5*y2 + .25*y4
    d = -.75*y0 + 3.125*y1 - 6.5*y2 + 6.75*y3 - 2.75*y4 + .125*y5
    e = .75*y0 - 4.25*y1 + 10*y2 - 10.5*y3 + 4.25*y4 - .25*y5
    f = -.25*y0 + 1.625*y1 - 4*y2 + 4.25*y3 - 1.75*y4 + .125*y5
    
    return lambda x : a + b*x + c*x*x + d*x*x*x + e*x*x*x*x + f*x*x*x*x*x





"""Yi = [r.randint(1,10) for i in range(21)]
Yip = [x for x in Yi]
for i in range(1,n-1):
    Yi[i] = .25*(Yip[i-1] + 2*Yip[i] + Yip[i+1])"""
Yi = [m.cos(m.pi*i/10) for i in range(21)]
n = len(Yi)



X = [i/100 for i in range((n-1)*100+1)]
Y = [0 for i in X]
Y2 = [0 for i in X]


for i in range(n):
    pl.scatter(i, Yi[i])


f = interpolation1(Yi[1],Yi[0],Yi[1],Yi[2])

for i in range(100):
    Y[i] = f(i/100)


for  i in range(1,n-2):
    f = interpolation1(Yi[i-1],Yi[i],Yi[i+1],Yi[i+2])
    
    for j in range(100):
        Y[i*100+j] = f(j/100)


f = interpolation1(Yi[n-3],Yi[n-2],Yi[n-1],Yi[n-2])

for i in range(101):
    Y[(n-2)*100+i] = f(i/100)



f = inter2(Yi[2], Yi[1], Yi[0], Yi[1], Yi[2], Yi[3])
for j in range(100):
    Y2[j] = f(j/100)

f = inter2(Yi[1], Yi[0], Yi[1], Yi[2], Yi[3], Yi[4])
for j in range(100):
    Y2[100+j] = f(j/100)


for i in range(2,n-3):
    f = inter2(Yi[i-2], Yi[i-1], Yi[i], Yi[i+1], Yi[i+2], Yi[i+3])
    
    for j in range(100):
        Y2[i*100+j] = f(j/100)


f = inter2(Yi[n-5], Yi[n-4], Yi[n-3], Yi[n-2], Yi[n-1], Yi[n-2])
for j in range(100):
    Y2[(n-3)*100+j] = f(j/100)

f = inter2(Yi[n-4], Yi[n-3], Yi[n-2], Yi[n-1], Yi[n-2], Yi[n-3])
for j in range(101):
    Y2[(n-2)*100+j] = f(j/100)




Yv = [m.cos(m.pi*i/1000) for i in range((n-1)*100+1)]
s1 = 0
s2 = 0
for i in range(len(Yv)):
    s1 += (Y[i]-Yv[i])**2
    s2 += (Y2[i]-Yv[i])**2
s1 = m.sqrt(s1 / len(Yv))
s2 = m.sqrt(s2 / len(Yv))

print(s1)
print(s2)


pl.plot(X,Yv)
#pl.plot(X, Y)
pl.plot(X,Y2)


pl.show()