# sw academy 0802. 델타 연습
import sys
sys.stdin = open("deltainput.txt")

# 절댓값을 반환해주는 함수 정의
def diff(a, b):
    result = 0
    if a > b:
        result = a - b
    elif a < b:
        result = b - a
    return result

T = int(input())
for test_case in range(1, T+1):
    # N에는 무조건 5를 입력하긴 했음
    N = int(input())
    # 5 X 5 matrix 생성
    mtx = [list(map(int, input().split())) for _ in range(N)]
    result = [[0] * N for _ in range(N)]


    # row index나 col index가 0 혹은 N-1일 경우??
    # 1. 이웃이 2개인 요소들
    result[0][0] = diff(mtx[0][1], mtx[0][0]) + diff(mtx[1][0], mtx[0][0])
    result[0][N-1] = diff(mtx[0][N-2], mtx[0][N-1]) + diff(mtx[1][N-1], mtx[0][N-1])
    result[N-1][0] = diff(mtx[N-2][0], mtx[N-1][0]) + diff(mtx[N-1][1], mtx[N-1][0])
    result[N-1][N-1] = diff(mtx[N-2][N-1], mtx[N-1][N-1]) + diff(mtx[N-1][N-2], mtx[N-1][N-1])

    # 2. 이웃이 3개인 요소들
    for j in range(1, N-1):
        result[0][j] = diff(mtx[0][j-1], mtx[0][j]) + diff(mtx[0][j+1], mtx[0][j]) + diff(mtx[1][j], mtx[0][j])
        result[N-1][j] = diff(mtx[N-1][j-1], mtx[N-1][j]) + diff(mtx[N-1][j+1], mtx[N-1][j]) + diff(mtx[N-2][j], mtx[N-1][j])

    for i in range(1, N-1):
        result[i][0] = diff(mtx[i-1][0], mtx[i][0]) + diff(mtx[i+1][0], mtx[i][0]) + diff(mtx[i][1], mtx[i][0])
        result[i][N-1] = diff(mtx[i-1][N-1], mtx[i][N-1]) + diff(mtx[i+1][N-1], mtx[i][N-1]) + diff(mtx[i][N-2], mtx[i][N-1])
    # 3. 이웃이 4개인 요소들
    for i in range(1, N-1):
        for j in range(1, N-1):
            result[i][j] = diff(mtx[i-1][j], mtx[i][j]) + diff(mtx[i+1][j], mtx[i][j]) + diff(mtx[i][j-1], mtx[i][j]) + diff(mtx[i][j+1], mtx[i][j])

    result_val = 0
    for i in range(N):
        for j in range(N):
            result_val += result[i][j]

    print(f'#{test_case} {result_val}')



