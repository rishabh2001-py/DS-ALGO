
# a={100,180,260,310,40,535,695}


def maxstock(arr,n):
    i=0
    profit = []
    while (i<n-1):

        while(i < n-1 and arr[i] >= arr[i+1]):
            i+=1
        mini=i

        if (i == n-2):
            return "Not found"

        while (i<n-1 and arr[i] <= arr[i+1]):
            i+=1
        maxi= i
        profit.append([mini,maxi])

    return profit






if __name__ == '__main__':
    a=[100,180,260,310,40,535,695]
    print(maxstock(a,len(a)))


