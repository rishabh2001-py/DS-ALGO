
# Anagram Using Dictionary o(n)


def anagramOfstring(s1,s2):
    isAnagram = True
    m1={}
    if len(s1) != len(s2):
        print("Not Anagram")
        return
    for i in range(len(s1)):
        try:
            m1[s1[i]]+=1
        except:
            m1[s1[i]]=1

    print(m1)
    for i in s2:
        try:
            if m1[i]>0:
                m1[i]-=1
            elif m1[i] == 0:
                isAnagram = False
                break
        except:
            isAnagram = False
            break
    print(m1)
    print(isAnagram)



    


if __name__ == '__main__':
    s1="siilent"
    s2="listenn"
    
    anagramOfstring(s1,s2)




            
        
