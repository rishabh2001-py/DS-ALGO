

def getPrimeFactors(n):

    divisor = 2
    factor=[]

    while (divisor<=n):

        if(n%divisor)==0:
            factor.append(divisor)
            n=n/divisor
        else:
            divisor+=1

    print(factor)






if __name__ == '__main__':
    getPrimeFactors(630)








