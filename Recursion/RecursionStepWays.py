def stepWays(n):
    if n==1 or n==2 :
        return n
    if n==3:
        return 4

    new_ans= stepWays(n-1) + stepWays(n-2) + stepWays(n-3)
    return  new_ans


n=int(input("Enter steps:"))
print(stepWays(n))
