
def Revalgo(arr,start,end):

    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1
    return arr











arr = list(map(int, input("enter array").strip().split()))
d = int(input("enter d"))
n = len(arr)
(Revalgo(arr,0,n-1))
Revalgo(arr,0,d-1)
Revalgo(arr,d,n-1)
print(arr)
