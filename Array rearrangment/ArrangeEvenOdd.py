


def arrange(arr):

    start = -1

    for i in range(len(arr)):
        if(arr[i]%2==1):
            start+=1
            arr[i],arr[start] = arr[start],arr[i]
    print(arr)

    even = start+1
    odd = 0
    while(even < len(arr) and odd <len(arr) and arr[odd]&1 == 1):
        arr[even],arr[odd]=arr[odd],arr[even]
        even= even+1
        odd = odd+2
    print(arr)




if __name__ == '__main__':
    arr=[3,6,12,1,5,8]
    arrange(arr)