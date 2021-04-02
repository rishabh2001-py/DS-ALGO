#Given an array of size n and a number k, find all elements that appear more than n/2 times

#a=[2,1,2,3,1,1,1]
import operator
import datetime
import time
def MorethanNK(arr,n,k):
    freq={}
    x=n//k

    for i in range(0,n):
        if arr[i] in freq:
            freq[arr[i]]=freq[arr[i]]+1
        else:
            freq[arr[i]]=1
    for i in freq:
        if(freq[i] > x):
            print("Element ",i)





if __name__ == '__main__':
    s=input()
    arr=list(map(int,input("Enter array").strip().split()))
    n=len(arr)
    k=int(input("K: "))
    MorethanNK(arr,n,k)






