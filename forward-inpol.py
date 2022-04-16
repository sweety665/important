import numpy as np

# Forward difference method

n= int(input("Enter number of data points: "))
x= np.zeros(n)
y= np.zeros((n,n))

print("Enter data for x and y: ")

for i in range(n):
    x[i]= float(input('x['+str(i)+']='))
    y[i][0]=float(input('y['+str(i)+']='))

a= float(input("Enter the value for differentiation"))
h= x[1]-x[0]
u= (a-x[0])/h
ans= y[0][0]
p=1

# Generating forward difference table
for i in range(1,n):
    for j in range(0,n-i):
        y[j][i]= y[j+1][i-1] -y[j][i-1]

print('\n Forward difference table\n')
for k in range(n):
    print(x[k], end='')
    for l in range(0,n-k):
        print('\t\t',(y[k][l]),end='')
    print()

for m in range(1,n):
    p= p*(u-m+1)/m
    ans= ans+p*y[0][m]

# Backward difference method

# for i in range(1,n):
#     for j in range(n-1,i-2,-1):
#         y[j][i]=y[j][i-1] -y[j-1][i-1]
# print('\n Backward difference table \n')
# for i in range(n):
#     print((x[i]),end='')
#     for j in range(0,i+1):
#         print('\t\t',(y[i][j]),end='')
#     print()
#
# for m in range(1,n):
#     p= p*(u+m-1)/n
#     ans= ans+p*y[n-1][m]
print("Value of the function at ",a," is ",ans)

