# Importing NumPy Library
import numpy as np
import sys
def gaussElim(n,i,o,p):
    a = np.array((i,o,p),float)
    x = np.zeros(n,float)
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
        
        for j in range(i+1, n):
                # print(a)

                ratio = a[j][i]/a[i][i]
        
                for k in range(n+1):
                    a[j][k] = a[j][k] - ratio * a[i][k]
    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
    
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
    
        x[i] = x[i]/a[i][i]
        print(x)
    return x 
a = [24,59,175,197]
b = [59,175,575,684]
c = [175,575,2023,2496]    
n = len(a)-1
root = gaussElim(n,a,b,c)
print(root)