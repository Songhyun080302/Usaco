def정의 solve풀다solve풀다(((()))))))):(((())))))))를 풀기:
    t = of의of의of의of의((((((((input입력input입력input입력input입력(((((((())))))))))))))))  # Number of test cases    t = int(입력 ()) # 테스트 케이스 수# 시험 사례 수 t = int(입력) # 테스트 케이스 수# Number of test cases    t = int(입력 ()) # 테스트 케이스 수# 시험 사례 수 t = int(입력) # 테스트 케이스 수# Number of test cases    t = int(입력 ()) # 테스트 케이스 수# 시험 사례 수 t = int(입력) # 테스트 케이스 수# Number of test cases    t = int(입력 ()) # 테스트 케이스 수# 시험 사례 수 t = int(입력) # 테스트 케이스 수
    for위해서 _ in에서 range범위range범위((((t)))):    _ 범위범위범위범위((((t))))에서:
        N, A, B = map지도map지도((((int, input입력input입력(((()))).split분열되다split분열되다(((())))))))        N, A, B = 지도지도지도지도((((int, 입력입력입력입력 (((()))).split분열되다split분열되다(((())))))))
        final_photo = [[[[input입력input입력(((()))).strip벗다strip벗다(((()))) for위해서 _ in에서 range범위((((N))))]]]]        final_photo = [[[[범위범위 내 _에 대한 입력입력 (((()))).스트립스트립스트립스트립 (((()))) ((((N))))]]]]
        
        of의
        first_photo = [[[[[[[[False거짓의]]]] * N for위해서 _ in에서 range범위((((N))))]]]]        first_photo = [[[[[[[[거짓]]]] * N for위해서 _ in에서 range범위 ((((N))))))))
        second_photo = [[[[[[[[False거짓의]]]] * N for위해서 _ in에서 range범위((((N))))]]]]        두 번째_사진 = [[[[[[[[거짓]]]] * N for위해서 _ in에서 range범위 ((((N))))))))]]]]
        
        possible = True진실의        가능성 = 참
        
        and그리고.
        for위해서 i in에서 range범위range범위((((N)))):        i의 범위범위범위범위((((N)))):
            for위해서 j in에서 range범위range범위((((N)))):            범위범위범위범위((((N))))의 j에 대해:
                if한다면 final_photo[i][[[[[j]]]] == 'B''B''B''B''B''B':                final_photo [[[[i][[j]]]] == 'B''B''B''B''B'인 경우:인 경우:
                    # If it's 'B', the star must be in both first and second photos                    # 'B'인 경우 별은 첫 번째 사진과 두 번째 사진 모두에 있어야 합니다.                    # 'B'라면 별은 첫 번째 사진과 두 번째 사진 # 'B' 인 경우 별은 첫 번째 사진과 두 번째 사진 모두에 있어야 합니다에 모두 있어야 합니다.
                    if i + B < N and j + A < N:                    i + B < N이고 j + A < N인 경우:                    i + B < N, j + A < N: i + B < N 이 고 j + A < N 인 경우:
                        first_photo[i][j] = True                        첫 번째_사진[i][j] = 참                        첫 번째_사진[i][j] = 트루 첫 번째_사진[i][j] = 참
                        second_photo[i + B][j + A] = True                        두 번째_사진 [i + B][j + A] = 참                        두 번째_사진 [i + B][j + A] = 트루 두 번째_사진 [i + B][j + A] = 참
                    else:                    그렇지 않으면:                    else:                    그렇지 않으면:
                        possible = False                        가능성 = 거짓                        가능성 = 거짓 가능성  = 거짓
                        break                        브레이크.                        break                        브레이크.
                elif final_photo[i][j] == 'G':                elif final_photo [i][j] == 'G':                elif final_photo [i][j] == 'G': elif final_photo [i][j] == 'G':
                    found_star = False                    found_star = 거짓                    found_star = 거짓 발견_star = 거짓
                    # Try placing the star in the first photo                    # 첫 번째 사진에 별을 배치해 보세요.                    # 첫 번째 사진 # 첫 번째 사진에 별을 배치해 보세요에 별을 배치해 보세요.
                    if i + B < N and j + A < N:                    i + B < N이고 j + A < N인 경우:                    i + B < N, j + A < N: i + B < N 이 고 j + A < N 인 경우:
                        if not first_photo[i][j] and not second_photo[i + B][j + A]:                        첫 번째_photo[i][j]가 아니고 두 번째_photo[i + B][j + A]가 아니라면:                        첫 번째_photo[i][j]가 아니고 두 번째_photo[i + B][j + A]가 아니라면:                        첫 번째_photo[i][j]가 아니고 두 번째_photo[i + B][j + A]가 아니라면:
                            first_photo[i][j] = True                            첫 번째_사진[i][j] = 참                            첫 번째_사진[i][j] = 트루 첫 번째_사진[i][j] = 참
                            second_photo[i + B][j + A] = False                            두 번째_사진 [i + B][j + A] = 거짓                            두 번째_사진 [i + B][j + A] = 거짓 두 번째_사진 [i + B][j + A] = 거짓
                            found_star = True                            found_star = 참                            found_star = 진정한 found_star = 참
                    
                    # Try placing the star in the second photo                    # 두 번째 사진에 별을 배치해 보세요.                    # 두 번째 사진 # 두 번째 사진에 별을 배치해 보세요에 별을 배치해 보세요.
                    if not found_star:                    발견되지 않은 경우_star:                    찾을 수 없는 경우_star: 발견되지 않은 경우_star:
                        if i + B < N and j + A < N:                        i + B < N이고 j + A < N인 경우:                        i + B < N, j + A < N: i + B < N 이 고 j + A < N 인 경우:
                            if not first_photo[i][j] and not second_photo[i + B][j + A]:                            첫 번째_photo[i][j]가 아니고 두 번째_photo[i + B][j + A]가 아니라면:                            첫 번째_photo[i][j]가 아니고 두 번째_photo[i + B][j + A]가 아니라면:                            첫 번째_photo[i][j]가 아니고 두 번째_photo[i + B][j + A]가 아니라면:
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
