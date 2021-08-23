from functools import cmp_to_key

def mycmp(a,b):

    if a[0]!=b[0]:
        if(a[0]<b[0]):
            return True
        return False
    else:
        if(a[1] > b[1]):
            return True
        return False





def Sorting(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if(compare(arr[j],arr[j+1])):

                arr[j],arr[j+1] = arr[j+1],arr[j]




    print("Array After Sorting  ",arr)





if __name__ == '__main__':
    arr = [[6, 'Akash'], [9, 'Rishabh'], [4, 'Rohan'], [4, 'Yohoan'],[4,'Michael'],[9,'Groza']]
    # for i in range(4):
    #     a,b = map(int,input("Enter Pair :").split())
    #     arr.append([a,b])
    print(arr)
    # Sorting(arr)


    b = sorted(arr,key = cmp_to_key(mycmp))
    print(b)



