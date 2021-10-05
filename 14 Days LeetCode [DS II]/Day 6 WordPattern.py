def wordPattern(pattern,s):
    m = {}
    # m2 ={}

    arr = []
    sep = 0
    for i in range(len(s)):

        if s[i] == " ":
            arr.append(s[sep:i])
            sep = i + 1

        if i == len(s) - 1:
            arr.append(s[sep:i + 1])

    if len(pattern) != len(arr):
        return False

    for i in pattern:
        m[i] = -1

    s = set()
    for i in range(len(pattern)):

        if (m[pattern[i]] == -1 or m[pattern[i]] == arr[i]):
            if arr[i] not in s:
                m[pattern[i]] = arr[i]
                s.add(arr[i])

        else:
            return False

    print(m)

    for i in m:

        if m[i] == -1:
            return False

    return True

if __name__ == '__main__' :

    print(wordPattern("abba","dog cat cat dog"))
