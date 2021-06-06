
def productExceptSelf(nums, n):
    ans =[]
    prod =1
    for i in range(n):
        if nums[i]==0:
            p2=prod

        prod*=nums[i]

    for i in range(n):
        if(nums[i]==0):
            ans.append(p2)
        else:
            ans.append(prod//nums[i])

    print(ans)

if __name__ == '__main__':
    arr=[12,1,2,2,2,2,20,0]
    productExceptSelf(arr,len(arr))
