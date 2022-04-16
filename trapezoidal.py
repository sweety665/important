a= float(input("Enter the lower limit: "))
b= float(input("Enter the upper limit: "))
n= int(input("Enter the length: "))

def f(x):
    return 1/(1+x**2)

def trapezoidal(a,b,n):
    h= (b-a)/n
    sum1= f(a)+ f(b)

    for i in range(1,n):
        w= a+ i*h
        sum1+= 2* f(w)

    final = sum1 * h/2
    return final

result= trapezoidal(a,b,n)
print("Result by trapezoidal method is ",result)

