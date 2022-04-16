import math
def newtonR(x):
    y= (x**math.sin(2))-4
    return y

def newtonDef(x):
    y= math.sin(2)*x**(math.sin(2)-1)
    return y

a= float(input("Enter the guess a: "))
n= int(input("Enter the number of iterations: "))
guess= 0
for i in range(n):
    guess= a- newtonR(a)/newtonDef(a)

print("Root of the equation, ", guess)