import numpy as np
# Forward difference method
n= int(input("Enter number of data points: "))
x= np.zeros(n)
y= np.zeros((n,n))
print("Enter data for x and y: ")

for i in range(n):
    x[i]= float(input('x['+str(i)+']='))
    y[i][0]=float(input('y['+str(i)+']='))

a= float(input("Enter the value for differentiation: "))
h= x[1]-x[0]
u= (a-x[0])/h

# Generating forward difference table
# for i in range(1,n):
#     for j in range(0,n-i):
#         y[j][i]= y[j+1][i-1] -y[j][i-1]
#
# print('\n Forward difference table\n')
# for k in range(n):
#     print(x[k], end='')
#     for l in range(0,n-k):
#         print('\t\t',(y[k][l]),end='')
#     print()
# ans= y[0][1]/h
#
# for m in range(2,n):
#    if (m%2==0):
#        ans+= (1/h)*(1/(m*(m-1)))*(y[0][m])
#    else:
#         ans += (1 / h) * (-1 / ((m-1)*m)) * (y[0][m])
#
# ans2= (1/(h**2))*(y[0][2]-(1/12)*y[0][4]+(1/12)*y[0][5]-(13/180)*y[0][6])
# print("Value of dy/dx at ",a," is ",ans)
# print("Value of d2y/dx2 at ",a," is ",ans2)

# Backward difference method
q= n-1
for i in range(1,n):
    for j in range(n-1,i-2,-1):
        y[j][i]=y[j][i-1] -y[j-1][i-1]
print('\n Backward difference table \n')
for i in range(n):
    print((x[i]),end='')
    for j in range(0,i+1):
        print('\t\t',(y[i][j]),end='')
    print()
ans= y[q][1]/h

for m in range(2,n):
       ans+= (1/h)*(1/m)*(y[q][m])

ans2= (1/(h**2))*(y[q][2]+y[q][3]+(11/12)*y[q][4]+(5/6)*y[q][5]+(137/180)*y[q][6])
print("Value of dy/dx at ",a," is ",ans)
print("Value of d2y/dx2 at ",a," is ",ans2)
