def Permutation(ques,ans):

    if len(ques)==0:
        print(ans)
        return

    for i in range(len(ques)):
        char_at_i = ques[i]
        rest_of_que=ques[:i]+ques[i+1:]
        Permutation(rest_of_que,ans+char_at_i)
        # Permutation(rest_of_que, ans)



if __name__ == '__main__':
    s='abc'
    ans=""
    Permutation(s,ans)








