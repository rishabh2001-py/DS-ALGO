


def FirstOcurence(arr,key,n,i):
    if n==i :
        return -1


    if (arr[i] == key):
        return i

    return (FirstOcurence(arr,key,n,i+1))


def LastOcurenec(arr,key,n,i):

    if i==n:
        return -1

    restarray= LastOcurenec(arr,key,n,i+1)

    if(restarray!=-1):

        return  restarray
    if arr[i] == key:
        return i
    return -1




def main():
        #arr = list(map(int, input("Enter array").strip().split()))
        arr=[1,3,4,5,6,4,8,9]
        n = len(arr)
        key=int(input("Enter Key:"))
        print(FirstOcurence(arr,key,n,0 ))
        print(LastOcurenec(arr,key,n,0))
main()
