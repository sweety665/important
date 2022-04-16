import math
import matplotlib.pyplot as plt
x = eval(input("Enter x: "))
p = eval(input("Enter y: "))
n = len(x)
y = []
x2Sum, xySum, ySum, xSum = 0,0,0,0
if len(x)!=len(p):
    print("ERROR")
else:
    plt.plot(x,p)
    for i in range(n):
        y.append(math.log(p[i]))
        xSum += x[i]
        ySum += y[i]
        x2Sum += x[i]**2
        xySum += x[i]*y[i]
    xm, ym = xSum/n, ySum/n
    a1 = (n*xySum-xSum*ySum)/(n*x2Sum-xSum**2)
    ao = ym - a1*xm
    a = math.exp(ao)
    for i in range(n):
        y[i] = a*math.exp(a1*x[i])
    print("a1= ",a1,"ao= ",ao,"y= ",y)
    plt.plot(x,y)
    plt.xlabel("x---->")
    plt.ylabel("y---->")
    plt.show()