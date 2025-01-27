def solve():
    t = int(input())  # Read number of test cases

    for _ in range(t):  # Loop through each test case
        N, A, B = map(int, input().split())  # Read N, A, and B
        final_photo = [list(input().strip()) for _ in range(N)]  # Read the final photo grid

        # Initialize the two photos with False (no stars initially)
        first_photo = [[False] * N for _ in range(N)] 
        second_photo = [[False] * N for _ in range(N)]

        possible = True  # Assume it is possible to recreate the photo

        # Iterate through each pixel of the final photo
        for i in range(N):
            for j in range(N):
                if final_photo[i][j] == 'B':
                    # If 'B', stars must be in both photos
                    if first_photo[i][j] or second_photo[i][j]:
                        possible = False
                        break
                    first_photo[i][j] = True
                    if i + B < N and j + A < N:
                        second_photo[i + B][j + A] = True
                    else:
                        possible = False
                        break

                elif final_photo[i][j] == 'G':
                    # If 'G', there must be exactly one star in either first or second photo
                    placed = False
                    if not first_photo[i][j]:
                        first_photo[i][j] = True
                        if i + B < N and j + A < N:
                            second_photo[i + B][j + A] = False
                        placed = True
                    if not placed and not second_photo[i][j]:
                        second_photo[i + B][j + A] = True
                        placed = True

                    if not placed:
                        possible = False
                        break

        # If it's not possible, output -1, else count the stars in the first photo
        if not possible:
            print(-1)
        else:
            star_count = sum(sum(row) for row in first_photo)
            print(star_count)

