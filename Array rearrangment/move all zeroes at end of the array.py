
#MOVE ALL ZEROES AT END OF ARRAY
def move0sAT_end(arr,n):
     i=-1
     for j in range(0,n):
         if(arr[j]!=0):
             i=i+1

             arr[j],arr[i]=arr[i],arr[j]
     return arr





arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
print(move0sAT_end(arr,n))