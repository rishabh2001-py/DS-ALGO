# a = [2,6,1,9,4,5,3]
# s= {1,2,3,4,5,6,9}
def findLongestConseqSubseq(arr, N):

    s=set(arr)
    maxcount=0
    currcount=0
    for i in range(N):
        if(arr[i]-1 not in s):

            j=arr[i]
            while(j in s):
                j+=1
                currcount+=1
            maxcount=max(maxcount,currcount)
    print(maxcount)




if __name__ == '__main__':
    findLongestConseqSubseq([2,1,4,5,6,0,9],7)









