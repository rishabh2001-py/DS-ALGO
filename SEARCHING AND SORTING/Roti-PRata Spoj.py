def logic(chef_Rank, parata, l, mid):
    time = 0
    par = 0

    for i in range(0, l):
        time = chef_Rank[i]
        j = 2

        while (time <= mid):
            par = par + 1
            time = time + chef_Rank[i] * j
            j = j + 1
    if parata <= par:
            return 1
    else:
            return 0


def solution(chef_Rank, parata, l):
    lb = 0
    ub = 10 ** 8
    ans = 0

    while (lb <= ub):
        mid = (lb + ub) // 2
        if (logic(chef_Rank, parata, l, mid)):
            ans = mid
            ub = mid - 1
        else:
            lb = mid + 1
    return ans


if __name__ == '__main__':
    chef_Rank = list(map(int, input("Enter chef Rank").strip().split()))
    parata = int(input("Enter Number of Prata:"))
    l = len(chef_Rank)
    print(solution(chef_Rank, parata, l))
