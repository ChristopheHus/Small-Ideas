import glob

path = "C:\\Users\\Christophe\\Music\\"

paths = glob.glob(path+"*.mp3")


for fname in paths:
    
    L1 = (fname[26:-4]).split(' ')
    L = []
    
    for st in L1:
        s = ''
        if st == '&' or st == '-' or st == 'x':
            continue
            
        for c in st:
            if c=='(' or c==')' or c==',':
                continue
            else:
                s += c
        
        if s != 'Remix' and s != 'ft.' and s != 'Bootleg' and s != 'Cover' and s != 'Edit' and s!= 'Original' and s!='Mix' and s!= 'vs.' and s!= 'Cut':
            L.append(s)
        
    #print(L)
    
    
    with open(fname, 'r', errors='ignore') as f:
        
        s = ""
        
        k = 0
        M = ['I', 'n', 'f', 'o']
        i = 0
            
        
        while k<4 and i<10000:
            i += 1
            c = f.read(1)
            
            if c == M[k]:
                k += 1
            else:
                k = 0
                if c == M[0]:
                    k = 1
            
            s += c
        
        #print (s)
        
        for l in L:
            if s.find(l) == -1:
                print (fname[26:-4])
                print (l)
    
    
    
    
    
    
    
    
    
    
    
    
    
    