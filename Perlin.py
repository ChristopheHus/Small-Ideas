import random as r
import matplotlib.pyplot as pl


def perlinNoise (octave, size, so):
    n = so
    
    while 2**n<size:
        n += 1
        
    noise = [0 for i in range(size)]
    s = sum([.25**i for i in range(octave)])
    
    for i in range(octave):
        oct = [0 for j in range(2**n+1)]
        for j in range(2**(i+so)+1):
            oct[j*2**(n-i-so)] = r.randint(0,255)
        
        for j in range(2**(i+so)):
            y1 = oct[j*2**(n-i-so)]
            y2 = oct[(j+1)*2**(n-i-so)]
            f = lambda x : (y2-y1) * x**2 * (3 - 2*x) + y1
            
            for k in range(1,2**(n-i-so)):
                oct[k + j*2**(n-i-so)] = f(k/2**(n-i-so))
        
        for j in range(size):
            noise[j] += oct[j] * .25**i
            
    for i in range(size):
        noise[i] /= s
            
    return noise
        
        
x = [i for i in range(1024)]
y = perlinNoise(4,1024,2)

pl.plot(x,y)
pl.ylim(ymax=255,ymin=0)