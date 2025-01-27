def solve():
    t = int(input())
    for _ in range(t):
        N, A, B = map(int, input().split())
        grid = [list(input()) for _ in range(N)]
        
        stars = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 'B': 
                    stars += 1
                elif grid[i][j] == 'G':
                    # Check if placing a star here is valid
                    if i + B < N and j + A < N and grid[i + B][j + A] != 'B':
                        stars += 1
                    else:
                        # If no valid placement for 'G', it's impossible
                        stars = -1
                        break
            if stars == -1:
                break
        print(stars)

if __name__ == "__main__":
    solve()
