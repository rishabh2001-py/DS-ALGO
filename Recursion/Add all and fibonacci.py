
def add_till_n(n):

    if n == 0:
        return 0

    return add_till_n(n-1) + n

def fibonacci(n):
    if n==1 or n==0:
        return n

    return fibonacci(n-1) + fibonacci(n-2)





def main():

    n = int(input("Enter Integer"))
    print(add_till_n(n))
    for i in range(n):
        print(fibonacci(i),end =" ")


main()