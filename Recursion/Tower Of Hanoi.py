
def toh(n,src,dest,helper):
    if n==0:
        return

    toh(n-1,src,helper,dest)

    print("Move from",src,"to",dest)

    toh(n-1,helper,dest,src)


def main():
    n =int(input("Enter Blocks"))
    toh(n,'A','C','B')


main()