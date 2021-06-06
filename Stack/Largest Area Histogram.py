 # we need to calculate left smaller boundry and right smaller boundry of each elemrnt of array
 #we will use stack and next smaller element approach on both sides
 #then we will just take the difference of  both the lb and rb array subsequent elements
 #and calculate the result ,in max variable


def largest_Area_histogram(arr):
    n=len(arr)
    s=[]
    lb = [-1]*n
    rb = [n]*n
 # ---- for right smaller ---
    for i in range(n-1,-1,-1):

        while(len(s)!=0):

            if (arr[i]>arr[top]):
                rb[i]=top
                #s.append(top)
                break
            else:
                top=s.pop()
        s.append(i)
        top=s.pop()
        s.append(top)
    print(rb)


#---for left smaller ---

    s=[]
    s.append(-1)
    for i in range(1,n):

        while (len(s) != 0):

            if (arr[i] > arr[top]):
                lb[i] = top
                s.append(top)
                break
            else:
                top = s.pop()

        s.append(i)
        top = s.pop()
        s.append(top)
    print(lb)

    mx=0
    diff=0
    for i in range(n):
        diff=(rb[i]-lb[i])-1
        mx=max(diff*arr[i],mx)
        print(mx)

    print(mx)

if __name__ == '__main__':

    arr=[5,4,3,2,1]
    largest_Area_histogram(arr)
