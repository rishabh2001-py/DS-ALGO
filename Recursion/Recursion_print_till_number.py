
def dece(n):

    if n == 0:
        return
    print(n,end=" ")
    dece(n-1)

def inc(n):
    if n == 0:
        return
    inc(n-1)
    print(n,end=" ")

def main():
     n=int(input("Enter N:"))

     dece(n)
     print()
     inc(n)


main()
















