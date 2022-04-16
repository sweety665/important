import math
def bisection(x):
    y= x**2+x-math.cos(x)
    return y

a= int(input("Enter the guess a for interval: "))
b= int(input("Enter the guess b for interval: "))
n= int(input("Enter number of iterations: "))
c=0
if(bisection(a)*bisection(b)>=0):
    print("Incorrect intervals")
else:
    for i in range(n):
        c= (a+b)/2
        if(bisection(a)*bisection(c)<0):
            b=c
        else:
            a=c

print("Root of the equation is ", c)
