def solve():
    n = int(input())
    a = list(map(int, input().split()))

    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] != a[j]:
                ans += counts.get(a[j],0) - (j < n-1 and a[j] == a[j+1])
    print(ans)
solve()
