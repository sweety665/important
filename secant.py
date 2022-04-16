import math

def secant(x):
    y= x**2.2-69
    return y

x0= float(input("Enter the interval a: "))
x1= float(input("Enter the interval b: "))
for i in range(5):
    fx0=secant(x0)
    fx1=secant(x1)
    x2= (x0*fx1-x1*fx0)/(fx1-fx0)
    x0,x1=x1,x2

print("Value of the root is: ",x1)