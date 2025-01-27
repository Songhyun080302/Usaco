from collections import Counter

def solve():
    N = int(input())  # Read the length of the array
    arr = list(map(int, input().split()))  # Read the array
    
    count = Counter(arr)
    
    distinct_moos = set()
    
    for y in count:
        if count[y] < 2:
            continue  
        for x in count:
            if x != y:
                distinct_moos.add((x, y, y))
    
    print(len(distinct_moos))

