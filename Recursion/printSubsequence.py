# s= 'abcd'


def getSubsequence(s,ans):

    if(len(s)==0):
      print(ans,end="  ")
      return


    char_at_start=s[0]
    rest_of_string=s[1:]
    getSubsequence(rest_of_string ,ans+"")
    getSubsequence(rest_of_string, ans+char_at_start)


if __name__ == "__main__":
    getSubsequence('gfg',"")




