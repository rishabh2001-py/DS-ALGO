# s= 'abcd'


def getSubsequence(s,ans):

    if(len(s)==0):
      print(ans,end="  ")
      return


    char_at_start=s[0]   #s[0] = g
    rest_of_string=s[1:] #ros = fg
    getSubsequence(rest_of_string, ans + char_at_start)
    getSubsequence(rest_of_string ,ans+"")



if __name__ == "__main__":
    getSubsequence('gfg',"")




