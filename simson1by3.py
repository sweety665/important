import math

a= float(input("Enter the lower limit: "))
b= float(input("Enter the upper limit: "))
n= int(input("Enter no. of intervals: "))

def f(x):
    return math.sqrt(1-x**2)

def simpson(a,b,n):
    h= (b-a)/n
    sum = f(a)+f(b)
    for i in range(1,n):
        c= a+i*h
        if i%2==0:
            sum+=2*f(c)
        else:
            sum+=4*f(c)
    ans= (h/3)*sum
    print("Result through Simpson method is ",ans)

simpson(a,b,n)