def inSequence( A, B, C):
    if(abs(A-B)%C==0):
        return 1
    else:
        return 0






if __name__ == '__main__':

    A=int(input("Enter First::"))
    B=int(input("Number to be searched::"))
    C=int(input("Common Differece::"))

    print(inSequence(A,B,C))
