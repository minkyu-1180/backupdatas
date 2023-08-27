# IM 대비 14. 백준 3085 사탕게임
import sys
sys.stdin = open("사탕게임input.txt")


def bomboni(arr):
    max_c = 1
    for i in range(N):
        c = 1
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]:
                c += 1
            else:
                c = 1
            max_c = max(max_c, c)

    for j in range(N):
        c = 1
        for i in range(N-1):
            if arr[i][j] == arr[i+1][j]:
                c += 1
            else:
                c = 1
            max_c = max(max_c, c)

    return max_c

T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 0
    # 무조건 오른쪽 / 아래랑 교환
    for i in range(N):
        for j in range(N):
            if j + 1 < N:
                # 특정 열 기준 행교환
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
                row_c = bomboni(arr)
                # 다시 맞교환하여 진행
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

            if i + 1 < N:
                # 특정 행 기준 열교환
                arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
                col_c = bomboni(arr)
                # 바꾼 것 원래대로 돌려놓기
                arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            result = max(result, row_c, col_c)
    print(result)
