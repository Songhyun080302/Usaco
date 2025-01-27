def solve():
    t = int(input())  # Read number of test cases

    for _ in range(t):  # Corrected indentation
        N, A, B = map(int, input().split())  # Read N, A, and B
        final_photo = [list(input().strip()) for _ in range(N)]  # Read final photo

        # Initialize the two photos with False (no stars initially)
        first_photo = [[False for _ in range(N)] for _ in range(N)]
        second_photo = [[False for _ in range(N)] for _ in range(N)]

        possible = True  # Start assuming it's possible to recreate the photo

        for i in range(N):
            for j in range(N):
                if final_photo[i][j] == 'B':
                    if i + B < N and j + A < N:
                        first_photo[i][j] = True
                        second_photo[i + B][j + A] = True
                    else:
                        possible = False
                        break
                elif final_photo[i][j] == 'G':
                    found_star = False
                    if i + B < N and j + A < N:
                        if not first_photo[i][j] and not second_photo[i + B][j + A]:
                            first_photo[i][j] = True
                            second_photo[i + B][j + A] = True
                            found_star = True
                    if not found_star:
                        possible = False
                        break

        if not possible:
            print(-1)
        else:
            star_count = sum(sum(row) for row in first_photo)
            print(star_count)
