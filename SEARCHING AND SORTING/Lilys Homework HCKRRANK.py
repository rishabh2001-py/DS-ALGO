def lilysHomework(arr):
    swap = 0
    m = []

    for i in range(len(arr)):
        m.append([arr[i], i])

    m.sort()
    print(m)
    print("-------///---------")
    j=0
    while(j<len(m)):
        print(j)
        if m[j][1] != j:
            m[m[j][1]],m[j]=m[j],m[m[j][1]]
            swap+=1
            j=j-1
        j=j+1



    print("-------///---------")
    return (swap)






#a=list(map(int,input("Enter Array 1:").strip().split()))
a=[3,4,2,5,1]
print(lilysHomework(a))