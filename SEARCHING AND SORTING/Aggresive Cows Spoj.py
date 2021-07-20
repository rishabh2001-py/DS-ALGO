def aggresive_cows(nc,stall_arr):
    low=0
    high=max(stall_arr)
    ans=1
    while(low<high):
        current=stall_arr[0]
        mid=int(high+low//2)
        current_cow=1
        for i in range(1,len(stall_arr)):
            if(stall_arr[i]-current>=mid):
                current_cow+=1
                current=stall_arr[i]
            if(current_cow==nc):
                ans=mid
                break
        if(current_cow<nc):
            high=mid-1
        else:
            low=mid+1
    return ans

nc=int(input("Enter number of cows"))

stall_ar=list(map(int,input("Enter stall arr:").strip().split()))

print(aggresive_cows(nc,stall_ar))