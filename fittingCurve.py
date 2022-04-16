import matplotlib.pyplot as plt
import numpy as np
import sys

def gaussElim(n,t,y,u):
    a = np.array((t,y,u),float)
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
w= eval(input("Enter weights: "))

m = int(input("Enter the degree of polynomial: "))
n = len(x)
a,b,c = [],[],[]
xSum, ySum, wSum, wxSum, wx2Sum, wySum, wxySum, wx2ySum,wx3Sum,wx4Sum = 0,0,0,0,0,0,0,0,0,0
if len(x)!=len(y):
    print("ERROR")
else:
    plt.plot(x,y)
    for i in range(n):
        xSum += x[i]
        ySum += y[i]
        wSum += w[i]
        wxSum += x[i]*w[i]
        wx2Sum += w[i]*x[i]**2
        wySum += w[i]*y[i]
        wxySum += y[i]*x[i]*w[i]
        wx2ySum+= w[i]*(x[i]**2)*y[i]
        wx3Sum+= w[i]*x[i]**3
        wx4Sum+= w[i]*x[i]**4

    for i in range(m+2):
        if i==0:
            a.append(wSum)
            b.append(wxSum)
            c.append(wx2Sum)
        elif i==1:
            a.append(wxSum)
            b.append(wx2Sum)
            c.append(wx3Sum)
        elif (i==2):
            a.append(wx2Sum)
            b.append(wx3Sum)
            c.append(wx4Sum)
        elif (i==m+1):
            a.append(wySum)
            b.append(wxySum)
            c.append(wx2ySum)
    # print(a,b,c)
    w = len(a)-1
    rEqn = gaussElim(w,a,b,c)
    print(rEqn)
    for i in range(n):
        y[i]= rEqn[0]+ rEqn[1]*x[i]+ rEqn[2]*x[i]**2
    plt.plot(x,y)
    plt.show()
