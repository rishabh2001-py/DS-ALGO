


def powerX(x,n):
    if(n==0):
        return 1
    power=powerX(x,n-1)
    pwr=power*x
    return pwr

if __name__ == '__main__':
    print(powerX(2,32))






