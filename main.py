# array sum pair found using set
def Findelement(arr, n, Sum):
    s = set()
    result = 0
    for i in range(0, n):
        temp = Sum - arr[i]
        if temp in s:
            result = 1
            return result
        s.add(arr[i])
    return result


arr = list(map(int, input("ENTER ARRAY::").strip().split(" ")))
Sum = int(input("enter d ::"))
n = len(arr)
result = Findelement(arr, n, Sum)
if (result == 0):
    print("pair not found")
else:
    print("pair found")
