def merge(intervals):
    if len(intervals) == 0:
        return intervals

    intervals.sort()
    res = []
    res.append(intervals[0])
    for i in range(1, len(intervals)):

        sta = res.pop()
        # print(sta)
        if sta[1] >= intervals[i][0]:
            bound = max(sta[1], intervals[i][1])
            res.append([sta[0], bound])
        else:
            res.append(sta)
            res.append(intervals[i])

    return (res)

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    print(merge(arr))
