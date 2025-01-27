def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        N, A, B = map(int, input().split())
        final_photo = [input().strip() for _ in range(N)]
        
        # Initialize the state of the first and second photos
        first_photo = [[False] * N for _ in range(N)]
        second_photo = [[False] * N for _ in range(N)]
        
        possible = True
        
        # Process the grid and check each cell
        for i in range(N):
            for j in range(N):
                if final_photo[i][j] == 'B':
                    # If it's 'B', the star must be in both first and second photos
                    if i + B < N and j + A < N:
                        first_photo[i][j] = True
                        second_photo[i + B][j + A] = True
                    else:
                        possible = False
                        break
                elif final_photo[i][j] == 'G':
                    found_star = False
                    # Try placing the star in the first photo
                    if i + B < N and j + A < N:
                        if not first_photo[i][j] and not second_photo[i + B][j + A]:
                            first_photo[i][j] = True
                            second_photo[i + B][j + A] = False
                            found_star = True
                    
                    # Try placing the star in the second photo
                    if not found_star:
                        if i + B < N and j + A < N:
                            if not first_photo[i][j] and not second_photo[i + B][j + A]:
                                first_photo[i][j] = False
                                second_photo[i + B][j + A] = True
                                found_star = True
                    
                    # If we can't find a valid placement for the star, it's impossible
                    if not found_star:
                        possible = False
                        break
        
        # If the configuration is not possible, output -1
        if not possible:
            print(-1)
        else:
            # Count the number of stars in the first photo
            star_count = sum(sum(row) for row in first_photo)
            print(star_count)

