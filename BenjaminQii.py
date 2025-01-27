def solve():
    n = int(input())
    a = list(map(int, input().split()))

    counts = {}
    for num in a:
        counts[num] = counts.get(num, 0) + 1

    distinct_moos = set()
    unique_nums = list(counts.keys())

    for i in range(len(unique_nums)):
        x = unique_nums[i]
        for j in range(len(unique_nums)):
            if i == j:
                continue
            y = unique_nums[j]
            if counts[y] >= 2:
                distinct_moos.add((x, y, y))

    print(len(distinct_moos))

solve()
