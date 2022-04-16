import numpy as np
import sys

def gaussElim(n,t,y,u):
    a = np.array((t,y,u))
    x = np.zeros(n)
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
    return x

x = eval(input("Enter x: "))
y = eval(input("Enter y: "))
# x = [1,3,4,6]
# y = [0.63,2.05,4.08,10.78]
m = int(input("Enter the degree of polynomial: "))
n = len(x)
a,b,c = [],[],[]
xSum, ySum, x2Sum, x3Sum, x4Sum, xySum, x2ySum = 0,0,0,0,0,0,0
if len(x)!=len(y):
    print("ERROR")
else:
    for i in range(n):
        xSum += x[i]
        ySum += y[i]
        x2Sum += x[i]**2
        x3Sum += x[i]**3
        x4Sum += x[i]**4
        xySum += x[i]*y[i]
        x2ySum += y[i]*x[i]**2
    for i in range(m+2):
        if i==0:
            a.append(len(x))
            b.append(xSum)
            c.append(x2Sum)
        elif i==1:
            a.append(xSum)
            b.append(x2Sum)
            c.append(x3Sum)
        elif (i==2):
            a.append(x2Sum)
            b.append(x3Sum)
            c.append(x4Sum)
        elif (i==m+1):
            a.append(ySum)
            b.append(xySum)
            c.append(x2ySum)
    # print(a,b,c)
    w = len(a)-1
    rEqn = gaussElim(w,a,b,c)
    # print(rEqn)
    for i in range(len(rEqn)):
        print("a"+str(i)+"= ",rEqn[i],"\n")
