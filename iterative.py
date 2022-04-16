import math
def iterative(x):
    y= 0.5+ math.sin(x)
    return y

a= float(input("Enter the guess: "))

for i in range(100):
    x1= iterative(a)
    a= x1

print("Value of root for eq1 is: ",x1)

