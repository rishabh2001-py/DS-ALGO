global m
m = {0: "", 1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}


#arr[3,4,5]

def possibleWords(a, N):
    if N == 0:
        result_array = [""]
        return result_array

    start_char = a[0] #[3]
    roarray = a[1:]   # [4,5]

    resultarray = possibleWords(roarray, N - 1)
    main_array = []
    for i in (m[start_char]):

        for j in resultarray:
            main_array.append(i + j)

    return sorted(main_array)


if __name__ == '__main__':
    arr = [ 2, 3,4]
    res=(possibleWords(arr, len(arr)))
    print(res)
    print(len(res))
