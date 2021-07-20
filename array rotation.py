#array rotation by using swap method
#Time complexity : O(n * d)
#Auxiliary Space : O(1)
import math

a1=[1,2,3,4,5,6,7]
d=int(input("enter d element"))
n=len(a1)
for i in range(0,d):
    temp=a1[0]
    for j in range(0,n-1):
        a1[j]=a1[j+1]
    a1[n-1]=temp
print(a1)
