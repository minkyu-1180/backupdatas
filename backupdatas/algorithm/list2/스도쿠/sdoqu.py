# 스도쿠 검증
import sys
sys.stdin = open("sdoquinput.txt")

T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    while result:
        # 행 하나씩 확인
        for i in range(9):
            if result == 0:

                break
            # 각 행마다 비교할 check_arr 생성
            check_arr = []
            # 각 열 별로 확인
            for j in range(9):

                # 이미 check_arr에 들어있는 경우(중복)
                if arr[i][j] in check_arr:
                    result = 0
                    break
                # check_arr에 들어가있지 않는 경우(중복X)
                else:
                    # 추가
                    check_arr.append(arr[i][j])

        # 열 하나씩 확인
        for j in range(9):
            for i in range(9):
                if result == 0:
                    break
            # 각 행마다 비교할 check_arr 생성
            check_arr = []
            # 각 열 별로 확인
            for i in range(9):
                # 이미 check_arr에 들어있는 경우(중복)
                if arr[i][j] in check_arr:
                    result = 0
                    break
                # check_arr에 들어가있지 않는 경우(중복X)
                else:
                    # 추가
                    check_arr.append(arr[i][j])

        # 3 X 3별로 확인
        # k = 0, 3, 6(시작 index)
        for k in range(0, 9, 3):
            check_arr = []
            if result == 0:
                break
            # i : k ~ k + 2
            for i in range(k, k + 3):
                if result == 0:
                    break
                # j : k ~ k + 2
                for j in range(k, k + 3):
                    if arr[i][j] in check_arr:
                        result = 0
                        break
                    else:
                        check_arr.append(arr[i][j])
        if result == 1:
            break
    print(f'#{test_case} {result}')




