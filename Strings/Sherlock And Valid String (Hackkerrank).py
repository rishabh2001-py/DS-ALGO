import math
import os
import random
import re
import sys


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

#   s='aabbc'
#   set={1,2}
#   set={1,2} --> s='abbc' --> s='aabbc'
#   set={1,2} --> s='abbc' --> s='aabbc'
#   set={1,2} --> s='aabc'---> s= 'aabbc'
#   set ={1,2} --> s= 'aabc' ---> s='aabbc'
#   set={1,1} --> set={1} --> s="aabb"  return "true"

#  else: false


#    Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is
#   occur the same number of times. Given a string , determine if it is valid.
#    For example, if  s= "abc", it is a valid string because frequencies are {a:1,b:1,c:1}. So is s= "abcc"
#    because we can remove one 'c' and have 1 of each character in the remaining string. If s= 'abccc'
#    however, the string is not valid as we can only remove 1 occurrence of c . That would leave character
 #   frequencies of {a:1 b:1 c:2}.




def isValid(s):
    m = {}
    for i in range(len(s)):
        try:
            m[s[i]] += 1
        except:
            m[s[i]] = 1
    se = set(m.values())
    print(se)

    if (len(se) == 1):
        return "YES"
    if (len(se) > 2):
        return "NO"

    if len(se) == 2:
        for i in m.keys():
            m[i] -= 1
            temp = list(m.values())
            try:
                temp.remove(0)
            except:
                pass

            if (len(set(temp)) == 1):
                return "YES"
            m[i] += 1
        return "NO"
