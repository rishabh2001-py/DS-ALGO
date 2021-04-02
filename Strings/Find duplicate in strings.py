# s="rishabh"
#d="h"
#counts=1


def DuplicateINstring(s,n):
    if(len(s)==0):
        print("No duplcates")
        return
    s2={}
    count=0
    for i in range(0,n):
        s2[s[i]]=0
    for i in range(0,n):
        s2[s[i]]+=1
        if(s2[s[i]]>1):
            print(s[i])



    print(s2)







if __name__ == '__main__':
    s=input("Enter string")
    DuplicateINstring(s,len(s))

