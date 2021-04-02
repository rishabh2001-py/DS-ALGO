arr = list(map(int, input("enter array").strip().split()))
max = 0
max2 = 0
for i in range(0, len(arr) - 1):
    if (arr[i] > max):
        max = arr[i]
    if (arr[i] < max and arr[i] > max2):
        max2 = arr[i]
print(max, max2)
