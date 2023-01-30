print("running")
import time 
import math
z = 0
start = time.time()

for a in range(1000):
   
    for b in range(a, 1000):
        c = 1000 - (a+b)
        if a**2 + b**2 == c**2:
            print(a*b*c)
        
                    


duration = time.time() - start
print(duration)
        
            