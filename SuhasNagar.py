def solve():
    t = int(input())  

    for _ in range(t):  
        N, A, B = map(int, input().split())  
        final_photo = [list(input().strip()) for _ in range(N)]  

        first_photo = [[False] * N for _ in range(N)] 
        second_photo = [[False] * N for _ in range(N)]

        possible = True  

        for i in range(N):
            for j in range(N):
                if final_photo[i][j] == 'B':
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

        if not possible:
            print(-1)
        else:
            star_count = sum(sum(row) for row in first_photo)
            print(star_count)
