#Fisher–Yates shuffle Algorithm works in O(n) time complexity.
#To shuffle an array a of n elements (indices 0..n-1):
  #for i from n - 1 downto 1 do
      # j = random integer with 0 <= j <= i
       #exchange a[j] and a[i]
import  random
def randomize(arr,n):
    randnum=0
    for i in range (n-1,0,-1):
        randnum=random.randint(0,i)
        arr[i],arr[randnum]=arr[randnum],arr[i]
    return arr





arr = list(map(int, input("enter array").strip().split()))
n = len(arr)
print(randomize(arr,n))
print(randomize(arr,n))
print(randomize(arr,n))
print(randomize(arr,n))