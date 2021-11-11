

def generate(s,res):

    if len(s) == 0:
        return

    if s not in res:
        res.add(s)

    for i in range(len(s)):

        ros = s[:i]+s[i+1:]

        generate(ros,res)






if __name__ == '__main__':

    s = 'xyz'
    res = set()
    ans= ""
    generate(s,res)
    print(sorted(res))