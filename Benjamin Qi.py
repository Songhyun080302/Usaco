def solve():
    N = int(input())
    arr = list(map(int, input().split()))  
    
    from collections import defaultdic
    count_map = defaultdict(set) 
    
  
    for i in range(N - 1, 0, -1):
        if arr[i] == arr[i - 1]: 
            count_map[arr[i]].add(arr[i - 1])  
    
    distinct_moos = set()  
    for y in count_map:
        for x in count_map[y]:
            distinct_moos.add((x, y)) 
    
    print(len(distinct_moos))  
