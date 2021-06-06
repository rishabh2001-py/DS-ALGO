def reverseString(s,n,i):

    if n==0:
        return

    reverseString(s[i+1:],n-1,i)
    print(s[0],end="")

def main():

    s = (input("Enter String"))
    reverseString(s,len(s),0)



main()