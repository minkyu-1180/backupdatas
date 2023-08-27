# IM 대비 17. 스도쿠 검증
import sys
sys.stdin = open("스도쿠검증input.txt")

# 스도쿠검증 함수
# 중간에 스도쿠검증이 불가능할 경우 멈춰야 하기 때문에 함수로 제작
def sdoku(arr):
    # 1. row별로 스도쿠 검증
    for i in range(9):
        # 각 열이 1 ~ 9로 채워져있는가?
        # 중복이 없는가?
        row_arr = [0] * 10
        for j in range(9):
            row_arr[arr[i][j]] += 1
            if row_arr[arr[i][j]] == 2:
                return 0
    # 2. col별로 스도쿠 검증
    for j in range(9):
        col_arr = [0] * 10
        for i in range(9):
            col_arr[arr[i][j]] += 1
            if col_arr[arr[i][j]] == 2:
                return 0


    # 3. 3 X 3별로 스도쿠 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):

            # (i, j)을 시작으로 한 3X3 매트릭스 생성
            tri_arr = [0] * 10
            for k in range(3):
                for l in range(3):
                    tri_arr[arr[i+k][j+l]] += 1
                    if tri_arr[arr[i+k][j+l]] == 2:
                        return 0
    # 4. 위의 세 과정 통과
    return 1




T = int(input())
for test_case in range(1, T+1):
    # 9X9의 매트릭스
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = sdoku(arr)
    print(f'#{test_case} {result}')