from collections import defaultdict

def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    count_map = defaultdict(set)
    for i in range(N - 1):
        if arr[i] != arr[i+1]: 
            count_map[arr[i+1]].add(arr[i])  # Add the preceding element to the set

    distinct_moos = set()
    for y in count_map:
        for x in count_map[y]:
            distinct_moos.add((x, y, y))

    print(len(distinct_moos))

if __name__ == "__main__":
    solve()
