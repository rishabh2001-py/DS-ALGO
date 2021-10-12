# # # array sum pair found using set
# # def Findelement(arr, n, Sum):
# #     s = set()
# #     result = 0
# #     for i in range(0, n):
# #         temp = Sum - arr[i]
# #         if temp in s:
# #             result = 1
# #             return result
# #         s.add(arr[i])
# #     return result
# #
# #
# # arr = list(map(int, input("ENTER ARRAY::").strip().split(" ")))
# # Sum = int(input("enter d ::"))
# # n = len(arr)
# # result = Findelement(arr, n, Sum)
# # if (result == 0):
# #     print("pair not found")
# # else:
# #     print("pair found")
#
#
# def quickSort(arr,low,high):
#
#
#     pivot = partition(arr,low,high)
#     if(low<high):
#         quickSort(arr,low,pivot-1)
#         quickSort(arr,pivot+1,high)
#
#
#
#
# def partition(arr,low,high):
#    pivot = low
#    i = low
#    j = high
#
#    while(i<j):
#
#        while(arr[pivot]<arr[i]):
#            i+=1
#
#        while(arr[pivot]>arr[i]):
#            j+=1
#
#        if i<j:
#            arr[high],arr[low] = arr[low],arr[high]
#
#    arr[pivot],arr[high] = arr[high],arr[pivot]
#
#    return high
#
#
#
# if __name__ == '__main__':
#     arr = [5,7,1,2,6,5]
#     quickSort(arr,0,len(arr)-1)
#     print(arr)
#
#







































