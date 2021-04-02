#*Time complexity : O(n)
#Auxiliary Space : O(1)

                               #********JUGGLING ALGO FOR ARRAY ROTATION**********#
import math
arr=list(map(int,input("ENTER ARRAY::").strip().split(" ")))
d=int(input("enter d ::"))
n=len(arr)
g_c_d=math.gcd(n,d)
for i in range(g_c_d):
    temp=arr[i]
    j=i
    while(1):
        k=j+d
        if(k>=n):
            k=k-n
        if(k==i):
            break
        arr[j]=arr[k]
        j=k
    arr[j]=temp
    print("array after set",i,arr)
print(arr)