arr=list(map(int,input("enter array").strip().split()))
Sum=int(input("enter Sum"))
n=len(arr)
total=0
result=False
if(sum(arr)<Sum):
    print(result)
else:
    for i in range(0, n):
        for j in range(i, n):
            total = arr[i] + arr[j]
            if (total == Sum):
                result = True
                break
            else:
                total = 0
                print("loop iterate")
    print(result)





