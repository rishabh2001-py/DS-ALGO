#b=10011

def B2D(b):
    new=b
    res=0
    base=1
    while(new!=0):
        rem=new%10
        new=int(new/10)
        res+=rem*(base)
        base=base*2
    print(res)    


if __name__ =='__main__':
    n=110101
    B2D(n)

