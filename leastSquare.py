import matplotlib.pyplot as plt
n= int(input("enter the number of data pair: \n"))
x= eval(input("Enter the values of x: "))
y= eval(input("Enter the values of y: "))

print(x,y)
ysum,x2sum,xysum,xsum,xm,ym= 0,0,0,0,0,0

for i in range(n):
    xsum= x[i]+xsum
    ysum= y[i]+ysum
    x2sum= x[i]**2+x2sum
    xysum= x[i]*y[i] +xysum

for i in range(n):
    xm+=x[i]/n
    ym+=y[i]/n

a1= (n*xysum-xsum*ysum)/(n*x2sum-xsum**2)
a0= ym-a1*xm

print('value of slope is ',a1)
print('value of y-intercept',a0)
yn= []

for i in range(n):
    xt= a1*x[i]*a0
    yn.append(xt)

print(yn)

plt.plot(x,y)
plt.plot(x,yn)
plt.show()