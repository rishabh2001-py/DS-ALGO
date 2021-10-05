# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.



def eraseOverlapIntervals(intervals):
    intervals.sort()

    sta = []
    sta.append(intervals[0])
    print(intervals)
    for i in range(1, len(intervals)):

        ele = sta.pop()

        if ele[1] > intervals[i][0]:
            sta.append([ele[0], min(ele[1], intervals[i][1])])
        else:
            sta.append(ele)
            sta.append(intervals[i])
        # print(sta)

    print(sta)
    return (len(intervals) - len(sta))

if __name__ =='__main__':

    ans=eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
    print(ans)