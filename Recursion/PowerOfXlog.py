

def powerX(x,n):

    if n==0:
        return 1
    ans=powerX(x,n//2)
    print(1)
    ans2=ans*ans
    if(n % 2 == 1):
        ans2=ans2*x
    return ans2


if __name__ == '__main__':
    print(powerX(2,9))

