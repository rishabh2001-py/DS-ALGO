

#[1,3,2,4]
def next_Larger(arr,n):

    k=list()
    a=[-1]*n
    for i in range(n-1,-1,-1):

        if(len(k)==0):
            a[i]=-1

        elif(len(k)!=0 and top > arr[i]):
            a[i]=top
        elif(len(k)!=0 and top < arr[i]):
            while(len(k) !=0 ) :
                top=k.pop()
                if(top>arr[i]):
                    a[i]=top
                    k.append(top)
                    break

        k.append(arr[i])
        top=k.pop()
        k.append(arr[i])

    print(a)


arr=list(map(int,input("Enter LIST::").strip().split()))
n=len(arr)

next_Larger(arr,n)