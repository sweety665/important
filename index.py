import numpy as np

n= int(input("Enter the number of data points: "))
x= np.zeros(n)
y= np.zeros((n,n))

print("Enter data for x and y: ")

for i in range(n):
    x[i]= float(input('x['+ str(i)+']='))
    y[i][0]= float(input('y['+str(i)+']='))

a= float(input("Enter the vlaue at which you want to interpolate: "))
h= x[1]-x[0]
u= (a-x[n-1])/h
ans= y[n-1][0]
p=1

for i in range(1,n):
    for j in range(n-1,i-2,-1):
        y[j][i]= y[j][i-1]- y[j-1][i-1]

print('\n Backward Difference Table\n')
for i in range(0,n):
    print((x[i]),end='')
    for j in range(0,i+1):
        print('\t\t', (y[i][j]),end='')
    print()

for m in range(1,n):
    p= p* (u+m-1)/m
    ans= ans+ p*y[n-1][m]

print("Value of the function at ",a," is ",ans)