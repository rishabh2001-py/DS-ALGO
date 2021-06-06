def ReplaceWithpi(s,n,i):
    if n==0 or n==1:
        return

    if s[i] == 'p' and s[i+1] == 'i':
        print('3.14',end="")
        ReplaceWithpi(s[i+2:],n-2,i)
    else:
        print(s[i],end="")
        ReplaceWithpi(s[i + 1:], n - 1, i)


def main():

    s = (input("Enter String"))
    (ReplaceWithpi(s,len(s),0))



main()