# s= 'abcd'


def getSubsequence(s):

    if(len(s)==0):
      array_of_ss=list()
      array_of_ss.append("")
      return array_of_ss

    char_at_start=s[0]
    rest_of_string=s[1:]
    array_of_ss=getSubsequence(rest_of_string)
    main_res=[]
    for i in array_of_ss:
        main_res.append(""+i)
        main_res.append(char_at_start+i)
    return main_res





if __name__ == "__main__":
    res=getSubsequence('gfg')
    # s=set(res)
    # print(s)
    # print(len(s))




