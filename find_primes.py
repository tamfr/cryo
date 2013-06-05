num = 36
t = 2
c = 0
prim = range(num)

while c < num:
    k = 0  
    for i in range(1,t):     
        if t%i == 0:
            k = k+1           
    if k == 1:		
 		c = c + 1
 		prim[c-1] = t
    t = t+1

