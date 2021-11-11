def combinationSum(candidates,target):

        res = []

        def recur(cur,total,i):

            if total == target:

                res.append(cur.copy())

                return

            if i>=len(candidates) or total > target:
                return

            cur.append(candidates[i])
            recur(cur,total+candidates[i],i)

            cur.pop()

            recur(cur,total,i+1)


        recur([],0,0)

        return res


if __name__ == '__main__':

    arr = [2,3,6,7]
    print(combinationSum(arr,7))





