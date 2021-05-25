#Better Than Bubble Sort
# Optimised version of bubble



def InsertionSort(arr):

     for i in range(1,len(arr)):
         current=arr[i]
         j=i-1

         while(arr[j]>current and j>=0):
             arr[j+1]=arr[j]
             j-=1
         arr[j+1]=current
         print(arr)





arr = list(map(int, input('Enter Array').strip().split()))
print("Before Sorting:", arr)
InsertionSort(arr)
print("After Sorting:", arr)